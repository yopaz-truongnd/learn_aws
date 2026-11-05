#!/usr/bin/env python3
"""
So sánh 2 file CSV từ vựng:
- lecturesub-tu-vung.csv
- lecturesub-tu-vung (1).csv

Tìm ra:
1. Những từ KHÔNG CHUNG trong cả 2 file (Symmetric Difference: (A \ B) ∪ (B \ A))
2. Những từ chỉ có trong file mới (B \ A)
3. Những từ trùng nhau ở cả 2 file (A ∩ B)
"""

import os
import sys
import csv

# Đảm bảo UTF-8 cho console
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def load_vocab(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Không tìm thấy file: {path}")
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    vocab_map = {}
    for r in rows:
        w = r.get('Từ', '').strip()
        if w:
            vocab_map[w] = r
    return vocab_map, fieldnames, rows

def write_csv(path, rows, fieldnames):
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)

def main():
    file1 = sys.argv[1] if len(sys.argv) > 1 else 'lecturesub-tu-vung.csv'
    file2 = sys.argv[2] if len(sys.argv) > 2 else 'lecturesub-tu-vung (1).csv'

    map1, fields1, rows1 = load_vocab(file1)
    map2, fields2, rows2 = load_vocab(file2)

    set1 = set(map1.keys())
    set2 = set(map2.keys())

    common_words = set1 & set2
    only_in_1 = set1 - set2
    only_in_2 = set2 - set1
    diff_words = set1 ^ set2  # Những từ không chung trong cả 2 file

    print("=" * 60)
    print(f"File 1: '{file1}' có {len(set1)} từ vựng.")
    print(f"File 2: '{file2}' có {len(set2)} từ vựng.")
    print(f"-> Số từ CHUNG ở cả 2 file: {len(common_words)} từ.")
    print(f"-> Số từ KHÔNG CHUNG ở cả 2 file: {len(diff_words)} từ.")
    print("=" * 60)

    # 1. Tạo file chứa TẤT CẢ các từ không chung giữa 2 file (Symmetric Difference)
    diff_rows = []
    # Giữ thứ tự xuất hiện ở file 1 trước, sau đó là file 2
    for r in rows1:
        if r.get('Từ', '').strip() in diff_words:
            diff_rows.append(r)
    for r in rows2:
        w = r.get('Từ', '').strip()
        if w in diff_words and w not in map1:
            diff_rows.append(r)

    out_diff = 'tu-vung-khong-chung.csv'
    write_csv(out_diff, diff_rows, fields1 or fields2)
    print(f"✅ Đã tạo file '{out_diff}' chứa {len(diff_rows)} từ không chung giữa 2 file.")

    # 2. Tạo file chứa riêng các từ mới chỉ có trong file (1) mà file gốc chưa có
    only_2_rows = [map2[w] for w in only_in_2 if w in map2]
    out_only_new = 'tu-vung-moi.csv'
    write_csv(out_only_new, only_2_rows, fields2 or fields1)
    print(f"✅ Đã tạo file '{out_only_new}' chứa {len(only_2_rows)} từ mới chỉ có trong file '{file2}'.")

if __name__ == '__main__':
    main()
