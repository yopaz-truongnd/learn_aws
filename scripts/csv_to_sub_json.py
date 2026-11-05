#!/usr/bin/env python3
"""
Chuyển đổi danh sách từ vựng từ file CSV (phụ đề bài giảng) sang file JSON
theo đúng cấu trúc của extension phụ đề (như sub.json).

Cấu trúc mỗi object:
{
    "createdAt": 1793642768732,
    "id": "[\"en\",\"vi\",\"represented\"]",
    "meaning": "đại diện",
    "sentence": "And all of these can be represented on the map right here.",
    "sourceLanguage": "en",
    "srsDueDate": 0,
    "srsEase": 2.5,
    "srsInterval": 0,
    "srsLastReviewed": 0,
    "srsRepetitions": 0,
    "targetLanguage": "vi",
    "time": 144.932229,
    "title": "Course: Ultimate AWS Certified Solutions Architect Associate 2026 | Udemy",
    "url": "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/learn/lecture/26097978",
    "word": "represented"
}
"""

import sys
import os
import csv
import json
import time

# Đảm bảo UTF-8 cho console Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def csv_to_sub_json(input_csv, output_json, existing_json=None):
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Khong tim thay file CSV dau vao: {input_csv}")

    # Nếu có file JSON hiện tại, đọc để bảo toàn createdAt và trạng thái SRS đã học
    existing_map = {}
    if existing_json and os.path.exists(existing_json):
        try:
            with open(existing_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict) and 'word' in item:
                            existing_map[item['word']] = item
        except Exception as e:
            print(f"[Canh bao] Khong the doc file JSON hien tai ({existing_json}): {e}")

    items = []
    base_time_ms = int(time.time() * 1000)

    with open(input_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            word = row.get('Từ', '').strip()
            if not word:
                continue

            meaning = row.get('Nghĩa', '').strip()
            source_lang = row.get('Nguồn', 'en').strip() or 'en'
            target_lang = row.get('Đích', 'vi').strip() or 'vi'
            sentence = row.get('Câu gốc', '').strip()
            title = row.get('Bài học', '').strip()
            url = row.get('Liên kết', '').strip()

            # Chuyển đổi thời gian (giây) sang float
            time_raw = row.get('Giây', '0').strip()
            try:
                time_val = float(time_raw)
            except ValueError:
                time_val = 0.0

            # ID theo chuẩn: '["en","vi","word"]' (không có khoảng trắng sau dấu phẩy)
            item_id = json.dumps([source_lang, target_lang, word], ensure_ascii=False, separators=(',', ':'))

            # Bảo tồn dữ liệu cũ nếu từ này đã từng tồn tại
            old_item = existing_map.get(word, {})

            created_at = old_item.get('createdAt')
            if not created_at:
                # Nếu từ mới, gán timestamp tăng dần theo thứ tự
                created_at = base_time_ms + index * 1000

            item = {
                "createdAt": int(created_at),
                "id": item_id,
                "meaning": meaning,
                "sentence": sentence,
                "sourceLanguage": source_lang,
                "srsDueDate": old_item.get('srsDueDate', 0),
                "srsEase": float(old_item.get('srsEase', 2.5)),
                "srsInterval": old_item.get('srsInterval', 0),
                "srsLastReviewed": old_item.get('srsLastReviewed', 0),
                "srsRepetitions": old_item.get('srsRepetitions', 0),
                "targetLanguage": target_lang,
                "time": time_val,
                "title": title,
                "url": url,
                "word": word
            }

            items.append(item)

    # Đảm bảo thư mục đích tồn tại
    out_dir = os.path.dirname(output_json)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=4, sort_keys=True)

    print(f"[OK] Da chuyen doi thanh cong {len(items)} tu vung tu '{input_csv}' sang '{output_json}'.")
    return items

if __name__ == '__main__':
    # Đường dẫn mặc định
    default_input = 'lecturesub-tu-vung.csv'
    if not os.path.exists(default_input) and os.path.exists('data/lecturesub-tu-vung.csv'):
        default_input = 'data/lecturesub-tu-vung.csv'

    default_output = 'sub.json'

    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_file = sys.argv[2] if len(sys.argv) > 2 else default_output

    csv_to_sub_json(input_file, output_file, existing_json=output_file)
