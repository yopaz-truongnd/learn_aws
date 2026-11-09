#!/usr/bin/env python3
"""
Tự động xuất từ vựng từ file CSV sang gói thẻ Anki .apkg phân chia 20 từ / Unit.
HOÀN TOÀN ĐỘC LẬP (Self-Contained): Tự khởi tạo SQLite database và nhúng sẵn
Note Type 4000Book1 chuẩn, không phụ thuộc vào bất kỳ file mẫu .apkg bên ngoài nào.

Cấu trúc 11 trường:
1.  №: Số thứ tự thẻ
2.  Keyword: Từ vựng tiếng Anh
3.  Suggestion: Gợi ý điền từ dạng t__ __ __ __ __ __ __ __ __n
4.  Short Vietnamese: Nghĩa tiếng Việt ngắn gọn
5.  Keyword_Sound: Âm thanh từ (để trống nếu chưa có)
6.  Image: Ảnh minh họa (để trống)
7.  Transcription: Phiên âm quốc tế IPA chuẩn UK/US
8.  Explanation: Câu ngữ cảnh có Cloze {{c1::từ_khóa}}
9.  Meaning_Sound: Âm thanh giải nghĩa (để trống)
10. Example_Sound: Âm thanh câu ví dụ (để trống)
11. Full Vietnamese: Ngữ cảnh chuyên ngành AWS + link video Udemy kèm timestamp
"""

import sys
import os
import csv
import json
import re
import html
import time
import hashlib
import sqlite3
import zipfile
import tempfile

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# Bảng phiên âm quốc tế IPA chuẩn (UK/US) cho toàn bộ từ vựng khóa học
IPA_MAP = {
    'accelerate': "/əkˈsel.ə.reɪt/",
    'accelerated': "/əkˈsel.ə.reɪ.tɪd/",
    'accessible': "/əkˈses.ə.bəl/",
    'across': "/əˈkrɒs/",
    'adjacent': "/əˈdʒeɪ.sənt/",
    'advance': "/ədˈvɑːns/",
    'advanced': "/ədˈvɑːnst/",
    'Advisor': "/ədˈvaɪ.zər/",
    'advisor': "/ədˈvaɪ.zər/",
    'alphabetical': "/ˌæl.fəˈbet.ɪ.kəl/",
    'alternative': "/ɒlˈtɜː.nə.tɪv/",
    'approach': "/əˈprəʊtʃ/",
    'architecture': "/ˈɑː.kɪ.tek.tʃər/",
    'argument': "/ˈɑːɡ.jə.mənt/",
    'arguments': "/ˈɑːɡ.jə.mənts/",
    'around': "/əˈraʊnd/",
    'at-rest': "/æt rest/",
    'attention': "/əˈten.ʃən/",
    'automate': "/ˈɔː.tə.meɪt/",
    'base': "/beɪs/",
    'based': "/beɪst/",
    'benefit': "/ˈben.ɪ.fɪt/",
    'benefits': "/ˈben.ɪ.fɪts/",
    'bill': "/bɪl/",
    'billing': "/ˈbɪl.ɪŋ/",
    'bootstrap': "/ˈbuːt.stræp/",
    'bootstrapping': "/ˈbuːt.stræp.ɪŋ/",
    'briefly': "/ˈbriːf.li/",
    'cache': "/kæʃ/",
    'caching': "/ˈkæʃ.ɪŋ/",
    'certain': "/ˈsɜː.tən/",
    'clone': "/kləʊn/",
    'cloning': "/ˈkləʊ.nɪŋ/",
    'combine': "/kəmˈbaɪn/",
    'combined': "/kəmˈbaɪnd/",
    'commonly': "/ˈkɒm.ən.li/",
    'compatible': "/kəmˈpæt.ə.bəl/",
    'complex': "/ˈkɒm.pleks/",
    'complicate': "/ˈkɒm.plɪ.keɪt/",
    'complicated': "/ˈkɒm.plɪ.keɪ.tɪd/",
    'configuration': "/kənˌfɪɡ.əˈreɪ.ʃən/",
    'confuse': "/kənˈfjuːz/",
    'confusing': "/kənˈfjuː.zɪŋ/",
    'consist': "/kənˈsɪst/",
    'consists': "/kənˈsɪsts/",
    'cost': "/kɒst/",
    'credential': "/krəˈden.ʃəl/",
    'credentials': "/krəˈden.ʃəlz/",
    'deactivate': "/diːˈæk.tɪ.veɪt/",
    'deactivated': "/diːˈæk.tɪ.veɪ.tɪd/",
    'dedicate': "/ˈded.ɪ.keɪt/",
    'dedicated': "/ˈded.ɪ.keɪ.tɪd/",
    'demonstrate': "/ˈdem.ən.streɪt/",
    'depth': "/depθ/",
    'describe': "/dɪˈskraɪb/",
    'describing': "/dɪˈskraɪ.bɪŋ/",
    'deserve': "/dɪˈzɜːv/",
    'difficulty': "/ˈdɪf.ɪ.kəl.ti/",
    'directly': "/daɪˈrekt.li/",
    'discuss': "/dɪˈskʌs/",
    'disregard': "/ˌdɪs.rɪˈɡɑːd/",
    'distribute': "/dɪˈstrɪb.juːt/",
    'distributed': "/dɪˈstrɪb.juːtɪd/",
    'drill': "/drɪl/",
    'efficiency': "/ɪˈfɪʃ.ən.si/",
    'eligible': "/ˈel.ɪ.dʒə.bəl/",
    'emphasis': "/ˈem.fə.sɪs/",
    'enhance': "/ɪnˈhɑːns/",
    'enhanced': "/ɪnˈhɑːnst/",
    'entire': "/ɪnˈtaɪər/",
    'failover': "/ˈfeɪlˌəʊ.vər/",
    'failure': "/ˈfeɪ.ljər/",
    'feller': "/ˈfel.ər/",
    'forecast': "/ˈfɔː.kɑːst/",
    'frequency': "/ˈfriː.kwən.si/",
    'fully': "/ˈfʊl.i/",
    'granular': "/ˈɡræn.jə.lər/",
    'guarantee': "/ˌɡær.ənˈtiː/",
    'guarantees': "/ˌɡær.ənˈtiːz/",
    'handle': "/ˈhæn.dəl/",
    'illustrate': "/ˈɪl.ə.streɪt/",
    'improve': "/ɪmˈpruːv/",
    'inbound': "/ˈɪn.baʊnd/",
    'infrastructure': "/ˈɪn.frəˌstrʌk.tʃər/",
    'initiate': "/ɪˈnɪʃ.i.eɪt/",
    'insufficient': "/ˌɪn.səˈfɪʃ.ənt/",
    'interest': "/ˈɪn.trəst/",
    'interested': "/ˈɪn.trəs.tɪd/",
    'invalidation': "/ɪnˌvæl.ɪˈdeɪ.ʃən/",
    'latency': "/ˈleɪ.tən.si/",
    'leaderboard': "/ˈliː.də.bɔːd/",
    'leverage': "/ˈliː.vər.ɪdʒ/",
    'lifecycle': "/ˈlaɪfˌsaɪ.kəl/",
    'map': "/mæp/",
    'mapped': "/mæpt/",
    'memcached': "/memˈkæʃt/",
    'mistake': "/mɪˈsteɪk/",
    'mistakes': "/mɪˈsteɪks/",
    'monitor': "/ˈmɒn.ɪ.tər/",
    'monitoring': "/ˈmɒn.ɪ.tər.ɪŋ/",
    'mostly': "/ˈməʊst.li/",
    'necessary': "/ˈnes.ə.ser.i/",
    'nightmare': "/ˈnaɪt.meər/",
    'nowadays': "/ˈnaʊ.ə.deɪz/",
    'obviously': "/ˈɒb.vi.əs.li/",
    'otherwise': "/ˈʌð.ə.waɪz/",
    'outbound': "/ˈaʊt.baʊnd/",
    'overview': "/ˈəʊ.və.vjuː/",
    'partition': "/pɑːˈtɪʃ.ən/",
    'partitioning': "/pɑːˈtɪʃ.ən.ɪŋ/",
    'period': "/ˈpɪə.ri.əd/",
    'policy': "/ˈpɒl.ə.si/",
    'policies': "/ˈpɒl.ə.siz/",
    'potentially': "/pəˈten.ʃəl.i/",
    'pretty': "/ˈprɪt.i/",
    'previous': "/ˈpriː.vi.əs/",
    'principle': "/ˈprɪn.sə.pəl/",
    'probably': "/ˈprɒb.ə.bli/",
    'provide': "/prəˈvaɪd/",
    'provided': "/prəˈvaɪ.dɪd/",
    'purpose': "/ˈpɜː.pəs/",
    'purposes': "/ˈpɜː.pə.sɪz/",
    'quick': "/kwɪk/",
    'quicker': "/ˈkwɪk.ər/",
    'read-intensive': "/riːd ɪnˈten.sɪv/",
    'recommendation': "/ˌrek.ə.menˈdeɪ.ʃən/",
    'recommendations': "/ˌrek.ə.menˈdeɪ.ʃənz/",
    'reduce': "/rɪˈdʒuːs/",
    'reference': "/ˈref.ər.əns/",
    'regardless': "/rɪˈɡɑːd.ləs/",
    'replacement': "/rɪˈpleɪs.mənt/",
    'replica': "/ˈrep.lɪ.kə/",
    'represent': "/ˌrep.rɪˈzent/",
    'represented': "/ˌrep.rɪˈzen.tɪd/",
    'science': "/ˈsaɪ.əns/",
    'scratch': "/skrætʃ/",
    'scratched': "/skrætʃt/",
    'separate': "/ˈsep.ər.eɪt/",
    'separated': "/ˈsep.ər.eɪtɪd/",
    'separately': "/ˈsep.ər.ət.li/",
    'several': "/ˈsev.ər.əl/",
    'simplification': "/ˌsɪm.plɪ.fɪˈkeɪ.ʃən/",
    'simplify': "/ˈsɪm.plɪ.faɪ/",
    'simplified': "/ˈsɪm.plɪ.faɪd/",
    'spend': "/spend/",
    'standard': "/ˈstæn.dəd/",
    'standpoint': "/ˈstænd.pɔɪnt/",
    'statement': "/ˈsteɪt.mənt/",
    'strategy': "/ˈstræt.ə.dʒi/",
    'stuff': "/stʌf/",
    'such': "/sʌtʃ/",
    'summary': "/ˈsʌm.ər.i/",
    'surface': "/ˈsɜː.fɪs/",
    'technology': "/tekˈnɒl.ə.dʒi/",
    'technologies': "/tekˈnɒl.ə.dʒiz/",
    'template': "/ˈtem.pleɪt/",
    'terminate': "/ˈtɜː.mɪ.neɪt/",
    'termination': "/ˌtɜː.mɪˈneɪ.ʃən/",
    'therefore': "/ˈðeə.fɔːr/",
    'threshold': "/ˈθreʃ.həʊld/",
    'thresholds': "/ˈθreʃ.həʊldz/",
    'turn': "/tɜːn/",
    'turns': "/tɜːnz/",
    'uniqueness': "/juːˈniːk.nəs/",
    'unstructured': "/ʌnˈstrʌk.tʃəd/",
    'utility': "/juːˈtɪl.ə.ti/",
    'various': "/ˈveə.ri.əs/",
    'warehouse': "/ˈweə.haʊs/",
    'warehousing': "/ˈweəˌhaʊ.zɪŋ/",
    'within': "/wɪˈðɪn/",
    'workload': "/ˈwɜːk.ləʊd/",
    'workloads': "/ˈwɜːk.ləʊdz/",
}

def get_ipa(word):
    clean = word.strip()
    if clean in IPA_MAP:
        return IPA_MAP[clean]
    if clean.lower() in IPA_MAP:
        return IPA_MAP[clean.lower()]
    clean_cap = clean.capitalize()
    if clean_cap in IPA_MAP:
        return IPA_MAP[clean_cap]
    return f"/{clean}/"

def format_time(seconds_str):
    try:
        sec = float(seconds_str)
        m = int(sec // 60)
        s = int(sec % 60)
        return f"{m:02d}:{s:02d}"
    except (ValueError, TypeError):
        return ""

def make_suggestion(word):
    """Tạo gợi ý dạng t__ __ __ __ __ __ __ __ __n theo chuẩn 4000Book1"""
    clean = word.strip()
    if len(clean) <= 1:
        return f"<div>{clean}</div>"
    if len(clean) == 2:
        return f"<div>{clean[0]}__</div>"
    middle = "__ " * (len(clean) - 2)
    return f"<div>{clean[0]}{middle}{clean[-1]}</div>"

def make_cloze(sentence, word):
    """
    Đục lỗ {{c1::...}} trong câu ngữ cảnh.
    Hỗ trợ cả trường hợp word là từ nguyên bản (base form)
    nhưng trong câu ngữ cảnh xuất hiện dưới dạng chia thì/số nhiều (inflected form), ví dụ:
    word="describe" -> câu có "describing" -> {{c1::describing}}
    word="policy"   -> câu có "policies"   -> {{c1::policies}}
    """
    # 1. Khớp chính xác từ nguyên bản
    pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
    if pattern.search(sentence):
        return pattern.sub(lambda m: f"{{{{c1::{m.group(0)}}}}}", sentence, count=1)

    # 2. Sinh các dạng biến thể hình thái học (inflections) phổ biến
    w = word.lower()
    variants = []
    if w.endswith("e"):
        stem = w[:-1]
        variants.extend([w + "s", w + "d", stem + "ing", w + "ing"])
    elif w.endswith("y") and len(w) > 1 and w[-2] not in "aeiou":
        stem = w[:-1]
        variants.extend([stem + "ies", stem + "ied", w + "ing", w + "s"])
    else:
        variants.extend([w + "s", w + "es", w + "ed", w + "ing"])
        if len(w) >= 3 and w[-1] not in "aeiou" and w[-2] in "aeiou" and w[-3] not in "aeiou":
            double_c = w + w[-1]
            variants.extend([double_c + "ed", double_c + "ing"])

    if w.endswith("k"):
        variants.extend([w + "er", w + "est"])
    elif w.endswith("e"):
        variants.extend([w + "r", w + "st"])

    special = {
        "failure": ["feller", "failures"],
        "credential": ["credentials"],
        "technology": ["technologies"],
        "policy": ["policies"],
        "workload": ["workloads"],
        "recommendation": ["recommendations"],
        "purpose": ["purposes"],
        "benefit": ["benefits"],
        "threshold": ["thresholds"],
        "mistake": ["mistakes"],
        "argument": ["arguments"],
        "bootstrap": ["bootstrapping", "bootstrapped"],
        "warehouse": ["warehousing", "warehouses"],
        "cache": ["caching", "cached", "caches"],
        "partition": ["partitioning", "partitioned", "partitions"],
        "monitor": ["monitoring", "monitored", "monitors"],
        "clone": ["cloning", "cloned", "clones"],
        "map": ["mapped", "mapping", "maps"],
        "turn": ["turns", "turned", "turning"],
        "bill": ["billing", "billed", "bills"],
        "base": ["based", "basing", "bases"]
    }
    if w in special:
        variants.extend(special[w])

    for v in variants:
        pat = re.compile(rf"\b{re.escape(v)}\b", re.IGNORECASE)
        if pat.search(sentence):
            return pat.sub(f"{{{{c1::{word}}}}}", sentence, count=1)

    # 3. Fallback theo tiền tố (stem) nếu từ có độ dài >= 4
    if len(w) >= 4:
        pat_stem = re.compile(rf"\b{re.escape(w[:4])}\w*", re.IGNORECASE)
        if pat_stem.search(sentence):
            return pat_stem.sub(f"{{{{c1::{word}}}}}", sentence, count=1)

    # 4. Fallback tìm chuỗi con không phân biệt hoa thường
    pattern2 = re.compile(re.escape(word), re.IGNORECASE)
    if pattern2.search(sentence):
        return pattern2.sub(f"{{{{c1::{word}}}}}", sentence, count=1)

    return sentence

def make_guid(idx):
    s = f"aws_saa_c03_vocab_{idx}_{time.time()}"
    return hashlib.md5(s.encode('utf-8')).hexdigest()[:10]

# Định nghĩa chuẩn Note Type 4000Book1
def get_4000book1_model(parent_deck_id):
    return {
        "id": 1397924728878,
        "name": "4000Book1",
        "type": 1,  # 1 = Cloze model
        "mod": 1600352298,
        "usn": 0,
        "sortf": 0,  # field 0 (№)
        "did": parent_deck_id,
        "tmpls": [
            {
                "name": "Cloze",
                "ord": 0,
                "qfmt": (
                    "<div style='font-family: Arial; font-size: 14px;color:blue;text-align: left;font-weight:bold;'>AWS SAA-C03 · Card No.: {{№}}</div><br>\n"
                    "<div style='text-align: center;'>{{Image}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 26px;color:red;text-align: left;'>{{Suggestion}}</div><br>\n\n"
                    "<div style='font-family: Arial; font-size: 20px;text-align: left;'>{{cloze:Explanation}}</div><br>\n"
                    "<div style='font-family: Arial; font-size: 20px;color:blue;text-align: left;'>{{Short Vietnamese}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 22px;text-align: left;'>{{type:cloze:Explanation}}\n"
                ),
                "afmt": (
                    "<div style='font-family: Arial; font-size: 14px;color:blue;text-align: left;font-weight:bold;'>AWS SAA-C03 · Card No.: {{№}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 24px;text-align: center;'>{{type:cloze:Explanation}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 24px;color:blue;text-align:center;'>{{Transcription}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 22px;text-align: left;'>{{cloze:Explanation}}</div>\n\n"
                    "<div style='text-align: center;'>{{Image}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 22px;color:black;text-align:center;'>{{Keyword}}</div>\n"
                    "<div style='font-family: Arial; font-size: 20px;color:black;text-align:center;'>{{Transcription}}</div>\n"
                    "<div style='font-family: Arial; font-size: 22px;color:blue;text-align:center;'>{{Short Vietnamese}}</div>\n\n"
                    "<div style='font-family: Arial; font-size: 18px;color:black;text-align:left;'>Keyword {{Keyword_Sound}}</div>\n"
                    "<div style='font-family: Arial; font-size: 18px;color:black;text-align:left;'>Meaning {{Meaning_Sound}}</div>\n"
                    "<div style='font-family: Arial; font-size: 18px;color:black;text-align:left;'>Example {{Example_Sound}}</div></br>\n\n"
                    "<div style='font-family: Arial; font-size: 20px;text-align: left;'>{{Full Vietnamese}}</div>"
                ),
                "bqfmt": "",
                "bafmt": "",
                "did": None,
                "bfont": "",
                "bsize": 0
            }
        ],
        "flds": [
            {"name": "№", "ord": 0, "sticky": True, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Keyword", "ord": 1, "sticky": True, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Suggestion", "ord": 2, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Short Vietnamese", "ord": 3, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Keyword_Sound", "ord": 4, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Image", "ord": 5, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Transcription", "ord": 6, "sticky": False, "rtl": False, "font": "Lucida Sans Unicode", "size": 20, "media": []},
            {"name": "Explanation", "ord": 7, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Meaning_Sound", "ord": 8, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Example_Sound", "ord": 9, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Full Vietnamese", "ord": 10, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []}
        ],
        "css": (
            ".card {\n font-family: arial; line-height: 1.5em;\n font-size: 20px;\n color: black;\ntext-align: center;\n background-color: white;\n}\n"
            ".cloze {\n font-weight: bold;\n color: blue;\n}\n\n"
            "#typeans {\n padding-top: 0.5em;\n text-align: center;\n max-width: 300px;\n}\n"
            "input#typeans {\n border-radius: 19px\n}\n"
            ".Translation {\n font-family: Lucida Sans Unicode;\n color: gray;\n padding-top: 0.5em;\n}\n\n"
            "div span {\n max-width: 900px;\n display: inline-block;\n text-align:left;\n}\n\n"
            ".English {\n padding: 1em;\n}\n"
            ".English IMG {\n float:left;\n}\n\n"
            ".card {color: black; background-color: #f3f3f3;}\n"
            "#typeans span {background-color: #f3f3f3;}\n"
            ".typeBad {color: #dc322f;font-weight:bold;font-size: 23px;}\n"
            ".typeMissed, .typePass {  color: #268bd2;font-weight:bold;font-size: 23px;}\n"
            ".typeGood{color: #2ed85a;font-weight:bold;} \n\n"
            ".Vietnamese {\nborder-radius:10px;\nline-height:1.4em;\nfont-family:tahoma;\nfont-size:16px;\n}\n"
        ),
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "latexsvg": False,
        "req": [[0, "any", [0, 2, 3, 5, 7]]],
        "vers": [],
        "tags": []
    }

def make_deck(deck_id, name, desc=""):
    return {
        "id": deck_id,
        "mod": int(time.time()),
        "name": name,
        "usn": 0,
        "lrnToday": [0, 0],
        "revToday": [0, 0],
        "newToday": [0, 0],
        "timeToday": [0, 0],
        "collapsed": False,
        "browserCollapsed": False,
        "desc": desc,
        "dyn": 0,
        "conf": 1,
        "extendNew": 0,
        "extendRev": 0
    }

def main():
    # Đường dẫn mặc định tính theo thư mục gốc dự án (chạy được từ bất kỳ thư mục nào)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_csv = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, "data", "lecturesub-tu-vung.csv")
    output_apkg = sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, "dist", "AWS_SAA_C03_Vocabulary.apkg")
    output_tsv = sys.argv[3] if len(sys.argv) > 3 else os.path.join(root, "dist", "anki_4000_format.tsv")
    for out_path in (output_apkg, output_tsv):
        out_dir = os.path.dirname(os.path.abspath(out_path))
        os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(input_csv):
        print(f"❌ Lỗi: Không tìm thấy file CSV đầu vào tại '{input_csv}'.")
        sys.exit(1)

    items = []
    with open(input_csv, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            word = (row.get("Từ") or "").strip()
            meaning = (row.get("Nghĩa") or "").strip()
            sentence = (row.get("Câu gốc") or "").strip()
            course = (row.get("Bài học") or "").strip()
            seconds = (row.get("Giây") or "").strip()
            link = (row.get("Liên kết") or "").strip()

            if not word:
                continue

            card_no = str(i + 1)
            suggestion = make_suggestion(word)
            short_vi = meaning.capitalize()
            ipa = get_ipa(word)
            cloze_explanation = make_cloze(sentence, word)

            time_str = format_time(seconds)
            time_badge = f" ({time_str})" if time_str else ""
            lecture_id = link.rstrip("/").split("/")[-1] if "/lecture/" in link else ""
            lecture_title = f"Lecture {lecture_id}" if lecture_id else "Bài giảng Udemy"

            full_vi = (
                f'<div style="margin: 0px 0px 5px">'
                f'<i><b>{html.escape(word)}</b> {ipa}</i><br />'
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

            fields_11 = [
                card_no,            # 0: №
                word,               # 1: Keyword
                suggestion,         # 2: Suggestion
                short_vi,           # 3: Short Vietnamese
                "",                 # 4: Keyword_Sound
                "",                 # 5: Image
                ipa,                # 6: Transcription
                cloze_explanation,  # 7: Explanation
                "",                 # 8: Meaning_Sound
                "",                 # 9: Example_Sound
                full_vi             # 10: Full Vietnamese
            ]

            items.append(fields_11)

    print(f"Loaded {len(items)} items from {input_csv}.")

    WORDS_PER_UNIT = 20
    total_units = (len(items) + WORDS_PER_UNIT - 1) // WORDS_PER_UNIT

    # 1. Ghi file TSV 11 cột để người dùng có thể import thủ công nếu muốn
    with open(output_tsv, "w", encoding="utf-8") as f:
        f.write("#separator:Tab\n")
        f.write("#html:true\n")
        f.write("#tags column:12\n")
        for idx, flds in enumerate(items):
            unit_idx = (idx // WORDS_PER_UNIT) + 1
            clean_flds = [f.replace("\t", " ").replace("\n", " ") for f in flds]
            row_str = "\t".join(clean_flds) + f"\tAWS_SAA-C03 Stephane_Maarek Unit_{unit_idx:02d}\n"
            f.write(row_str)

    print(f"✅ Đã tạo file TSV chuẩn 11 cột: {output_tsv}")

    # 2. Tạo trực tiếp file .apkg tự chứa (Self-Contained) - KHÔNG cần file mẫu .apkg bên ngoài
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, 'collection.anki2')
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Tạo cấu trúc các bảng SQLite theo đúng chuẩn Anki
        cur.executescript('''
            CREATE TABLE col (
                id              integer primary key,
                crt             integer not null,
                mod             integer not null,
                scm             integer not null,
                ver             integer not null,
                dty             integer not null,
                usn             integer not null,
                ls              integer not null,
                conf            text not null,
                models          text not null,
                decks           text not null,
                dconf           text not null,
                tags            text not null
            );

            CREATE TABLE notes (
                id              integer primary key,
                guid            text not null,
                mid             integer not null,
                mod             integer not null,
                usn             integer not null,
                tags            text not null,
                flds            text not null,
                sfld            integer not null,
                csum            integer not null,
                flags           integer not null,
                data            text not null
            );

            CREATE TABLE cards (
                id              integer primary key,
                nid             integer not null,
                did             integer not null,
                ord             integer not null,
                mod             integer not null,
                usn             integer not null,
                type            integer not null,
                queue           integer not null,
                due             integer not null,
                ivl             integer not null,
                factor          integer not null,
                reps            integer not null,
                lapses          integer not null,
                left            integer not null,
                odue            integer not null,
                odid            integer not null,
                flags           integer not null,
                data            text not null
            );

            CREATE TABLE revlog (
                id              integer primary key,
                cid             integer not null,
                usn             integer not null,
                ease            integer not null,
                ivl             integer not null,
                lastIvl         integer not null,
                factor          integer not null,
                time            integer not null,
                type            integer not null
            );

            CREATE TABLE graves (
                usn             integer not null,
                oid             integer not null,
                type            integer not null
            );

            CREATE INDEX ix_notes_usn on notes (usn);
            CREATE INDEX ix_cards_usn on cards (usn);
            CREATE INDEX ix_revlog_usn on revlog (usn);
            CREATE INDEX ix_cards_nid on cards (nid);
            CREATE INDEX ix_cards_sched on cards (did, queue, due);
            CREATE INDEX ix_revlog_cid on revlog (cid);
            CREATE INDEX ix_notes_csum on notes (csum);
        ''')

        # Cấu hình decks
        parent_deck_id = 1710000000000
        parent_deck_name = "AWS SAA-C03 Vocabulary (Stephane Maarek)"

        decks = {
            "1": {
                "id": 1,
                "mod": 0,
                "name": "Default",
                "usn": 0,
                "lrnToday": [0, 0],
                "revToday": [0, 0],
                "newToday": [0, 0],
                "timeToday": [0, 0],
                "collapsed": True,
                "browserCollapsed": True,
                "desc": "",
                "dyn": 0,
                "conf": 1,
                "extendNew": 0,
                "extendRev": 0
            },
            str(parent_deck_id): make_deck(
                parent_deck_id, parent_deck_name, "Bộ thẻ từ vựng tiếng Anh SAA-C03 phân chia 20 từ / Unit."
            )
        }

        unit_deck_map = {}
        for u in range(1, total_units + 1):
            subdeck_id = parent_deck_id + u
            subdeck_name = f"{parent_deck_name}::Unit {u:02d}"
            unit_deck_map[u] = subdeck_id
            decks[str(subdeck_id)] = make_deck(subdeck_id, subdeck_name, f"Unit {u:02d} ({WORDS_PER_UNIT} từ)")

        # Cấu hình models
        model_obj = get_4000book1_model(parent_deck_id)
        models = {str(model_obj["id"]): model_obj}

        # Cấu hình dconf & conf
        dconf = {
            "1": {
                "id": 1,
                "mod": 0,
                "name": "Default",
                "usn": 0,
                "maxTaken": 60,
                "autoplay": True,
                "timer": 0,
                "replayq": True,
                "new": {
                    "bury": False,
                    "delays": [1.0, 10.0],
                    "initialFactor": 2500,
                    "ints": [1, 4, 0],
                    "order": 1,
                    "perDay": 20
                },
                "rev": {
                    "bury": False,
                    "ease4": 1.3,
                    "ivlFct": 1.0,
                    "maxIvl": 36500,
                    "perDay": 200,
                    "hardFactor": 1.2
                },
                "lapse": {
                    "delays": [10.0],
                    "leechAction": 1,
                    "leechFails": 8,
                    "minInt": 1,
                    "mult": 0.0
                },
                "dyn": False,
                "newMix": 0,
                "newPerDayMinimum": 0,
                "interdayLearningMix": 0,
                "reviewOrder": 0,
                "newSortOrder": 0,
                "newGatherPriority": 0
            }
        }

        conf = {
            "dueCounts": True,
            "creationOffset": -600,
            "schedVer": 2,
            "curDeck": 1,
            "newSpread": 0,
            "estTimes": True,
            "sortType": "noteFld",
            "collapseTime": 1200,
            "activeDecks": [1],
            "addToCur": True,
            "dayLearnFirst": False,
            "timeLim": 0,
            "nextPos": 1,
            "sortBackwards": False,
            "curModel": model_obj["id"]
        }

        now_sec = int(time.time())
        now_ms = int(time.time() * 1000)

        # Chèn vào bảng col
        cur.execute(
            "INSERT INTO col (id, crt, mod, scm, ver, dty, usn, ls, conf, models, decks, dconf, tags) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (1, 1608498000, now_ms, now_ms, 11, 0, 0, 0, json.dumps(conf), json.dumps(models), json.dumps(decks), json.dumps(dconf), "{}")
        )

        # Chèn notes và cards
        start_id_note = now_ms
        start_id_card = now_ms + 500000

        for idx, flds in enumerate(items):
            unit_idx = (idx // WORDS_PER_UNIT) + 1
            assigned_deck_id = unit_deck_map[unit_idx]

            nid = start_id_note + idx
            cid = start_id_card + idx
            guid = make_guid(idx)
            flds_joined = "\x1f".join(flds)
            sfld = flds[0]  # Sort field là №
            csum = int(hashlib.sha1(sfld.encode('utf-8')).hexdigest()[:8], 16)
            tags = f" AWS_SAA-C03 Stephane_Maarek Unit_{unit_idx:02d} "

            # Chèn note
            cur.execute(
                "INSERT INTO notes (id, guid, mid, mod, usn, tags, flds, sfld, csum, flags, data) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nid, guid, model_obj["id"], now_sec, 0, tags, flds_joined, sfld, csum, 0, "")
            )

            # Chèn card gán đúng vào Subdeck của Unit
            cur.execute(
                "INSERT INTO cards (id, nid, did, ord, mod, usn, type, queue, due, ivl, factor, reps, lapses, left, odue, odid, flags, data) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (cid, nid, assigned_deck_id, 0, now_sec, 0, 0, 0, idx + 1, 0, 0, 0, 0, 0, 0, 0, 0, "")
            )

        conn.commit()
        conn.close()

        # Đóng gói thành file .apkg hoàn chỉnh
        with zipfile.ZipFile(output_apkg, "w", zipfile.ZIP_DEFLATED) as z_out:
            z_out.write(db_path, "collection.anki2")
            z_out.writestr("media", "{}")

    print(f"🎉 ĐÃ TẠO THÀNH CÔNG GÓI ANKI TỰ CHỨA (SELF-CONTAINED): {output_apkg}")
    print(f"📊 Đã chia {len(items)} từ vựng thành {total_units} Units (mỗi Unit {WORDS_PER_UNIT} từ):")
    for u in range(1, total_units + 1):
        count = min(WORDS_PER_UNIT, len(items) - (u - 1) * WORDS_PER_UNIT)
        print(f"   • Unit {u:02d}: {count} từ")
    print(f"👉 File hoàn toàn tự chứa, không phụ thuộc vào bất kỳ file mẫu nào!")

if __name__ == "__main__":
    main()
