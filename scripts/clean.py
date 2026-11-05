#!/usr/bin/env python3
"""
Script dọn dẹp các tệp JSON, CSV và bản build sinh ra liên quan tới script từ vựng Anki.

Các tệp được dọn dẹp:
  1. sub.json (file JSON tạo từ CSV cho extension phụ đề)
  2. Các file CSV tạm sinh ra trong quá trình so sánh / tải về:
     - tu-vung-khong-chung.csv
     - tu-vung-moi.csv
     - lecturesub-tu-vung (*).csv
  3. Thư mục dist/ (các file build của Anki: .apkg, .tsv)

Tính năng an toàn:
  - Luôn liệt kê danh sách tệp trước khi xóa.
  - Luôn yêu cầu người dùng gõ xác nhận (y/N) trước khi thực hiện xóa.
  - Có thể dùng cờ -y hoặc --yes để tự động xác nhận khi cần.

Cú pháp:
    python scripts/clean.py          # Quét, liệt kê và hỏi xác nhận trước khi xóa
    python scripts/clean.py -y       # Tự động xác nhận xóa mà không cần hỏi
"""

import os
import sys
import glob

# Đảm bảo UTF-8 cho console
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def find_targets(root_dir):
    targets = []

    # 1. File JSON sinh ra từ CSV
    sub_json = os.path.join(root_dir, 'sub.json')
    if os.path.exists(sub_json):
        targets.append(sub_json)

    # 2. Các file CSV tạm / so sánh ở thư mục gốc
    csv_patterns = [
        'tu-vung-khong-chung.csv',
        'tu-vung-moi.csv',
        'lecturesub-tu-vung (*).csv',
        'diff_*.csv'
    ]
    for pattern in csv_patterns:
        for f in glob.glob(os.path.join(root_dir, pattern)):
            if os.path.isfile(f) and f not in targets:
                targets.append(f)

    # 3. Các file build trong dist/
    dist_dir = os.path.join(root_dir, 'dist')
    if os.path.exists(dist_dir):
        for f in glob.glob(os.path.join(dist_dir, '*')):
            if os.path.isfile(f):
                targets.append(f)

    # 4. Cache python (__pycache__)
    for current_root, dirs, _ in os.walk(root_dir):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(current_root, '__pycache__')
            targets.append(pycache_path)

    return targets

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    auto_yes = '-y' in sys.argv or '--yes' in sys.argv

    targets = find_targets(root_dir)

    print("=" * 65)
    print("🧹 TRÌNH DỌN DẸP TỆP TIN ANKI & VOCABULARY (learn_aws)")
    print("=" * 65)

    if not targets:
        print("✨ Dự án hoàn toàn sạch sẽ! Không tìm thấy tệp JSON, CSV tạm hoặc file build nào cần dọn.")
        print("=" * 65)
        return

    print(f"Phát hiện {len(targets)} tệp / thư mục dự kiến xóa:")
    for i, t in enumerate(targets, 1):
        rel = os.path.relpath(t, root_dir)
        print(f"  {i}. {rel}")
    print("-" * 65)

    # Hỏi xác nhận nếu không có cờ -y
    if not auto_yes:
        try:
            choice = input("⚠️  Bạn có chắc chắn muốn XÓA các tệp trên không? (y/N): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n❌ Đã hủy thao tác.")
            return

        if choice not in ('y', 'yes'):
            print("❌ Đã hủy thao tác. Không có tệp nào bị xóa.")
            print("=" * 65)
            return

    # Thực hiện xóa
    deleted_count = 0
    import shutil
    for t in targets:
        rel = os.path.relpath(t, root_dir)
        try:
            if os.path.isfile(t):
                os.remove(t)
                print(f"  [Đã xóa file] {rel}")
                deleted_count += 1
            elif os.path.isdir(t):
                shutil.rmtree(t)
                print(f"  [Đã xóa thư mục] {rel}")
                deleted_count += 1
        except Exception as e:
            print(f"  [Lỗi khi xóa {rel}]: {e}")

    print("=" * 65)
    print(f"✅ Đã dọn dẹp thành công {deleted_count} mục.")
    print("=" * 65)

if __name__ == '__main__':
    main()
