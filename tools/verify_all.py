import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_DIR = os.path.join(BASE_DIR, 'topics')

all_ok = True

print("=== 1. Checking HTML Structure & Bilingual Parity in topics/ ===")
html_files = [
    f for f in sorted(os.listdir(TOPICS_DIR))
    if f.endswith('.html') and not f.endswith('.backup.html')
]

print(f"Checking {len(html_files)} topic files (skipping *.backup.html)...")
for fname in html_files:
    fpath = os.path.join(TOPICS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    div_open = len(re.findall(r'<div\b', content))
    div_close = len(re.findall(r'</div>', content))
    lang_vi = len(re.findall(r'class=["\']lang-vi["\']', content))
    lang_en = len(re.findall(r'class=["\']lang-en["\']', content))

    status = "OK" if div_open == div_close and lang_vi == lang_en else "MISMATCH"
    if status == "MISMATCH":
        all_ok = False
    print(f"[{status}] {fname}: div({div_open}/{div_close}), lang(vi:{lang_vi}, en:{lang_en})")

print("\n=== 2. Checking Foreign Characters (Arabic, Persian, Cyrillic, CJK, Thai) ===")
foreign_pattern = re.compile(
    r'[\u0600-\u06FF\u0400-\u04FF\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF\u0E00-\u0E7F]'
)
foreign_errors = 0

scan_targets = [
    os.path.join(BASE_DIR, 'index.html'),
    os.path.join(BASE_DIR, 'README.md'),
    os.path.join(BASE_DIR, 'CLAUDE.md'),
]

for target in scan_targets:
    if os.path.isfile(target):
        with open(target, 'r', encoding='utf-8') as f:
            for idx, line in enumerate(f, 1):
                if foreign_pattern.search(line):
                    print(f"[FOREIGN CHAR] {os.path.relpath(target, BASE_DIR)}:{idx}: {line.strip()[:100]}")
                    foreign_errors += 1

for folder in ['topics', 'lectures']:
    folder_path = os.path.join(BASE_DIR, folder)
    if os.path.isdir(folder_path):
        for root, _, files in os.walk(folder_path):
            for file in sorted(files):
                if file.endswith('.backup.html'):
                    continue
                if file.endswith(('.md', '.html')):
                    p = os.path.join(root, file)
                    with open(p, 'r', encoding='utf-8') as f:
                        for idx, line in enumerate(f, 1):
                            if foreign_pattern.search(line):
                                print(f"[FOREIGN CHAR] {os.path.relpath(p, BASE_DIR)}:{idx}: {line.strip()[:100]}")
                                foreign_errors += 1

if foreign_errors > 0:
    all_ok = False
    print(f"Found {foreign_errors} lines with unexpected foreign characters.")
else:
    print("[OK] No unexpected foreign characters found.")

print("\n=== 3. Checking Internal Links (href & src) ===")
link_errors = 0
files_to_check_links = [os.path.join(BASE_DIR, 'index.html')] + [
    os.path.join(TOPICS_DIR, f) for f in html_files
]

for fpath in files_to_check_links:
    with open(fpath, 'r', encoding='utf-8') as f:
        s = f.read()
    d = os.path.dirname(fpath)
    for h in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', s):
        # Ignore external links or empty strings
        if h.startswith(('http://', 'https://', 'mailto:', 'tel:')) or not h:
            continue
        target_path = os.path.normpath(os.path.join(d, h))
        if not os.path.exists(target_path):
            print(f"[BROKEN LINK] {os.path.relpath(fpath, BASE_DIR)} -> {h}")
            link_errors += 1

if link_errors > 0:
    all_ok = False
    print(f"Found {link_errors} broken internal links.")
else:
    print("[OK] All internal links exist.")

print("\n" + "=" * 50)
result_text = "ALL PASSED" if all_ok else "ERRORS FOUND"
print("OVERALL RESULT:", result_text)
print("=" * 50)

if not all_ok:
    sys.exit(1)
