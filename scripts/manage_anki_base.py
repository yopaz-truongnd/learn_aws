#!/usr/bin/env python3
"""
Quản lý Deck Anki cơ sở hoàn thiện (Master Base Deck): anki.apkg
Tự động nạp cơ sở dữ liệu hiện có (bao gồm toàn bộ 132 từ vựng, hình ảnh, âm thanh TTS),
và khi thêm từ vựng mới sẽ NỐI TIẾP vào Deck cơ sở mà không làm mất dữ liệu cũ.

Các tính năng:
1. info: Kiểm tra thông tin hiện tại của anki.apkg (số thẻ, các Unit, ảnh, âm thanh)
2. add <file.csv>: Nạp file CSV từ vựng mới, lọc từ chưa có, tự động điền tiếp vào Unit đang mở
   hoặc tạo Unit mới (mỗi Unit 20 từ), đóng gói lại anki.apkg hoàn chỉnh.
3. export_tsv: Xuất toàn bộ từ vựng hiện có trong anki.apkg ra file TSV 11 cột chuẩn Anki.
"""

import sys
import os
import csv
import json
import time
import shutil
import hashlib
import sqlite3
import zipfile
import tempfile
import subprocess
import html
import re

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import IPA_MAP and make_cloze / make_suggestion from export_anki_4000
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from export_anki_4000 import IPA_MAP, get_ipa, make_suggestion, make_cloze, format_time
except ImportError:
    IPA_MAP = {}
    def get_ipa(w): return f"/{w}/"
    def make_suggestion(w): return f"<div>{w}</div>"
    def make_cloze(s, w): return s
    def format_time(s): return ""

ZSTD_BIN = "/opt/homebrew/bin/zstd" if os.path.exists("/opt/homebrew/bin/zstd") else "zstd"

def find_zstd():
    if os.path.exists(ZSTD_BIN):
        return ZSTD_BIN
    import shutil
    z = shutil.which("zstd")
    if z:
        return z
    raise RuntimeError("Không tìm thấy lệnh zstd trên hệ thống! Vui lòng cài đặt qua brew install zstd.")

class AnkiBaseDeck:
    def __init__(self, apkg_path="anki.apkg"):
        self.apkg_path = os.path.abspath(apkg_path)
        self.zstd_bin = find_zstd()

    def exists(self):
        return os.path.exists(self.apkg_path)

    def inspect(self):
        """Đọc và phân tích thông tin deck hiện tại"""
        if not self.exists():
            return None

        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.apkg_path, "r") as z:
                z.extractall(tmpdir)

            p21b = os.path.join(tmpdir, "collection.anki21b")
            p21 = os.path.join(tmpdir, "collection.anki21")
            subprocess.run([self.zstd_bin, "-d", "-q", "-f", p21b, "-o", p21], check=True)

            conn = sqlite3.connect(p21)
            cur = conn.cursor()

            decks = dict(cur.execute("SELECT id, name FROM decks").fetchall())
            notes = cur.execute("SELECT id, guid, mid, flds, tags FROM notes ORDER BY id").fetchall()
            cards = cur.execute("SELECT id, nid, did, due FROM cards ORDER BY id").fetchall()

            card_deck_map = {c[1]: c[2] for c in cards}

            vocab_list = []
            sound_count = 0
            image_count = 0

            for n in notes:
                flds = n[3].split("\x1f")
                card_no = flds[0]
                word = flds[1]
                short_vi = flds[3] if len(flds) > 3 else ""
                has_sound = bool(flds[4]) if len(flds) > 4 else False
                has_img = bool(flds[5]) if len(flds) > 5 else False
                ipa = flds[6] if len(flds) > 6 else ""
                cloze = flds[7] if len(flds) > 7 else ""
                full_vi = flds[10] if len(flds) > 10 else ""

                if has_sound:
                    sound_count += 1
                if has_img:
                    image_count += 1

                did = card_deck_map.get(n[0], 0)
                deck_name = decks.get(did, "Default")

                vocab_list.append({
                    "note_id": n[0],
                    "guid": n[1],
                    "card_no": card_no,
                    "word": word,
                    "short_vi": short_vi,
                    "has_sound": has_sound,
                    "has_img": has_img,
                    "ipa": ipa,
                    "cloze": cloze,
                    "full_vi": full_vi,
                    "deck_id": did,
                    "deck_name": deck_name,
                    "tags": n[4]
                })

            # Đếm số thẻ theo Unit
            unit_counts = {}
            for v in vocab_list:
                dname = v["deck_name"].split("\x1f")[-1]
                unit_counts[dname] = unit_counts.get(dname, 0) + 1

            return {
                "total_notes": len(notes),
                "total_cards": len(cards),
                "sound_count": sound_count,
                "image_count": image_count,
                "unit_counts": unit_counts,
                "vocab_list": vocab_list,
                "decks": decks
            }

    def print_info(self):
        info = self.inspect()
        if not info:
            print(f"❌ Không tìm thấy file base: {self.apkg_path}")
            return

        print("=" * 65)
        print(f"📦 ANKI MASTER BASE DECK: {os.path.basename(self.apkg_path)}")
        print(f"📊 Tổng số từ vựng / Thẻ: {info['total_notes']} thẻ")
        print(f"🔊 Số thẻ có âm thanh TTS: {info['sound_count']} thẻ")
        print(f"🖼️  Số thẻ có hình ảnh minh họa: {info['image_count']} thẻ")
        print("📑 Phân bố các Unit (20 từ / Unit):")
        for uname, cnt in sorted(info['unit_counts'].items()):
            remain = 20 - cnt
            remain_str = f" (còn trống {remain} chỗ)" if remain > 0 else " (ĐÃ ĐẦY)"
            print(f"   • {uname}: {cnt} từ{remain_str}")
        print("=" * 65)

    def add_from_csv(self, csv_path):
        """Thêm từ mới từ file CSV vào deck base anki.apkg"""
        if not os.path.exists(csv_path):
            print(f"❌ Không tìm thấy file CSV: {csv_path}")
            return False

        if not self.exists():
            print(f"❌ Không tìm thấy file base anki.apkg để nối tiếp!")
            return False

        info = self.inspect()
        existing_words = {v["word"].lower(): v for v in info["vocab_list"]}
        existing_count = info["total_notes"]

        # 1. Đọc CSV và phát hiện từ mới
        new_items = []
        with open(csv_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                word = (row.get("Từ") or "").strip()
                meaning = (row.get("Nghĩa") or "").strip()
                sentence = (row.get("Câu gốc") or "").strip()
                course = (row.get("Bài học") or "").strip()
                seconds = (row.get("Giây") or "").strip()
                link = (row.get("Liên kết") or "").strip()

                if not word:
                    continue

                w_lower = word.lower()
                if w_lower in existing_words:
                    continue  # Đã có trong base, bỏ qua để bảo vệ media

                new_items.append({
                    "word": word,
                    "meaning": meaning,
                    "sentence": sentence,
                    "course": course,
                    "seconds": seconds,
                    "link": link
                })

        print(f"🔍 Đã quét file CSV '{csv_path}':")
        print(f"   • Từ đã có sẵn trong anki.apkg: {len(existing_words)} từ")
        print(f"   • Từ MỚI cần thêm vào: {len(new_items)} từ")

        if not new_items:
            print("✨ Không có từ vựng mới nào cần thêm. Base anki.apkg đã đầy đủ!")
            return True

        # Sao lưu anki.apkg trước khi cập nhật
        backup_path = self.apkg_path + ".bak"
        shutil.copy2(self.apkg_path, backup_path)
        print(f"💾 Đã tạo bản sao lưu an toàn: {os.path.basename(backup_path)}")

        # 2. Xử lý thêm từ mới vào database
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.apkg_path, "r") as z:
                z.extractall(tmpdir)

            p21b = os.path.join(tmpdir, "collection.anki21b")
            p21 = os.path.join(tmpdir, "collection.anki21")
            subprocess.run([self.zstd_bin, "-d", "-q", "-f", p21b, "-o", p21], check=True)

            conn = sqlite3.connect(p21)
            cur = conn.cursor()

            # Lấy thông tin ID cao nhất hiện tại
            max_nid = cur.execute("SELECT max(id) FROM notes").fetchone()[0] or 1794198345690
            max_cid = cur.execute("SELECT max(id) FROM cards").fetchone()[0] or 1794198845690

            # Lấy danh sách Decks hiện tại
            decks_raw = cur.execute("SELECT id, name FROM decks").fetchall()
            decks_map = {name: did for did, name in decks_raw}

            # Xác định Unit đang mở
            # Unit 07: id 1794198481373
            card_no = existing_count
            now_ts = int(time.time())

            for item in new_items:
                card_no += 1
                unit_idx = ((card_no - 1) // 20) + 1
                unit_name = f"Unit {unit_idx:02d}"
                full_deck_name = f"AWS SAA-C03 Vocabulary (Stephane Maarek)\x1f{unit_name}"

                # Kiểm tra deck đã tồn tại trong decks table chưa
                if full_deck_name not in decks_map:
                    # Tạo deck mới
                    new_did = 1794198481366 + unit_idx
                    desc_str = f"{unit_name} (20 từ)"
                    desc_bytes = desc_str.encode("utf-8")
                    kind_blob = bytes([0x0A, len(desc_bytes) + 4, 0x08, 0x01, 0x22, len(desc_bytes)]) + desc_bytes
                    cur.execute(
                        "INSERT INTO decks (id, name, mtime_secs, usn, common, kind) VALUES (?,?,?,?,?,?)",
                        (new_did, full_deck_name, now_ts, -1, b'', kind_blob)
                    )
                    decks_map[full_deck_name] = new_did

                did = decks_map[full_deck_name]
                w = item["word"]
                meaning = item["meaning"]
                sentence = item["sentence"]
                course = item["course"]
                seconds = item["seconds"]
                link = item["link"]

                suggestion = make_suggestion(w)
                short_vi = meaning.capitalize()
                ipa = get_ipa(w)
                cloze_exp = make_cloze(sentence, w)

                time_str = format_time(seconds)
                time_badge = f" ({time_str})" if time_str else ""
                lecture_id = link.rstrip("/").split("/")[-1] if "/lecture/" in link else ""
                lecture_title = f"Lecture {lecture_id}" if lecture_id else "Bài giảng Udemy"

                full_vi = (
                    f'<div style="margin: 0px 0px 5px">'
                    f'<i><b>{html.escape(w)}</b> {ipa}</i><br />'
                    f'<ul>'
                    f'<li><b>Nghĩa tiếng Việt:</b> <font color="#cc0000"><b>{html.escape(meaning)}</b></font></li>'
                    f'<li><b>Câu ngữ cảnh:</b> {html.escape(sentence)}</li>'
                    f'<li><b>Khóa học:</b> {html.escape(course)}</li>'
                    f'<li><a href="{link}" target="_blank" style="color:#1e88e5;font-weight:bold;text-decoration:none;">'
                    f'▶ Xem video trên Udemy: {lecture_title}{time_badge}'
                    f'</a></li>'
                    f'</ul>'
                    f'</div>'
                )

                flds_list = [
                    str(card_no),
                    w,
                    suggestion,
                    short_vi,
                    "", # Sound (để trống chờ người dùng generate TTS trong Anki)
                    "", # Image (để trống chờ add image)
                    ipa,
                    cloze_exp,
                    "",
                    "",
                    full_vi
                ]

                flds_str = "\x1f".join(flds_list)
                mid = 1397924728878
                new_nid = max_nid + (card_no - existing_count)
                new_cid = max_cid + (card_no - existing_count)
                guid_s = f"aws_saa_c03_vocab_{card_no}_{time.time()}"
                guid = hashlib.md5(guid_s.encode('utf-8')).hexdigest()[:10]
                tags = f" AWS_SAA-C03 Stephane_Maarek {unit_name.replace(' ', '_')} "
                csum = int(hashlib.sha1(str(card_no).encode("utf-8")).hexdigest()[:8], 16)
                sfld = w

                cur.execute(
                    "INSERT INTO notes (id, guid, mid, mod, usn, tags, flds, sfld, csum, flags, data) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (new_nid, guid, mid, now_ts, -1, tags, flds_str, sfld, csum, 0, "")
                )

                cur.execute(
                    "INSERT INTO cards (id, nid, did, ord, mod, usn, type, queue, due, ivl, factor, reps, lapses, left, odue, odid, flags, data) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (new_cid, new_nid, did, 0, now_ts, -1, 0, 0, card_no, 0, 0, 0, 0, 0, 0, 0, 0, "")
                )

            conn.commit()
            conn.close()

            # Nén lại collection.anki21b
            subprocess.run([self.zstd_bin, "-16", "-q", "-f", p21, "-o", p21b], check=True)
            if os.path.exists(p21):
                os.remove(p21)

            # Đóng gói zip anki.apkg
            temp_out = os.path.join(tmpdir, "updated.apkg")
            with zipfile.ZipFile(temp_out, "w", zipfile.ZIP_DEFLATED) as z_out:
                for fname in sorted(os.listdir(tmpdir)):
                    if fname not in ("updated.apkg", "collection.anki21"):
                        fpath = os.path.join(tmpdir, fname)
                        if os.path.isfile(fpath):
                            z_out.write(fpath, fname)

            # Ghi đè vào anki.apkg chính
            shutil.copy2(temp_out, self.apkg_path)

        print(f"🎉 ĐÃ CẬP NHẬT THÀNH CÔNG VÀO '{os.path.basename(self.apkg_path)}'!")
        print(f"📈 Tổng số thẻ hiện tại: {card_no} thẻ (đã thêm {len(new_items)} từ mới).")
        self.print_info()
        return True

    def export_tsv(self, tsv_path="dist/anki_4000_format.tsv"):
        """Xuất toàn bộ deck ra file TSV 11 cột"""
        info = self.inspect()
        if not info:
            print(f"❌ Không thể xuất TSV: Không tìm thấy deck base!")
            return False

        os.makedirs(os.path.dirname(os.path.abspath(tsv_path)), exist_ok=True)
        with open(tsv_path, "w", encoding="utf-8") as f:
            f.write("#separator:Tab\n")
            f.write("#html:true\n")
            f.write("#tags column:12\n")

            for v in info["vocab_list"]:
                # Fields 0 to 10
                flds = [
                    v["card_no"],
                    v["word"],
                    make_suggestion(v["word"]),
                    v["short_vi"],
                    "[sound:...]" if v["has_sound"] else "",
                    "[image:...]" if v["has_img"] else "",
                    v["ipa"],
                    v["cloze"],
                    "",
                    "",
                    v["full_vi"]
                ]
                clean_flds = [f.replace("\t", " ").replace("\n", " ") for f in flds]
                row_str = "\t".join(clean_flds) + f"\t{v['tags'].strip()}\n"
                f.write(row_str)

        print(f"✅ Đã xuất {len(info['vocab_list'])} từ vựng ra file TSV: {tsv_path}")
        return True

def main():
    manager = AnkiBaseDeck("anki.apkg")

    if len(sys.argv) < 2 or sys.argv[1] in ("info", "status"):
        manager.print_info()
    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Sử dụng: python3 scripts/manage_anki_base.py add <duong_dan_file.csv>")
            sys.exit(1)
        manager.add_from_csv(sys.argv[2])
    elif sys.argv[1] in ("export_tsv", "export"):
        out_tsv = sys.argv[2] if len(sys.argv) > 2 else "dist/anki_4000_format.tsv"
        manager.export_tsv(out_tsv)
    else:
        print("Lệnh hợp lệ: info, add <file.csv>, export_tsv [out.tsv]")

if __name__ == "__main__":
    main()
