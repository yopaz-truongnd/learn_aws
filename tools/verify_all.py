import os
import re

topics_dir = os.path.join(os.getcwd(), 'topics')
files = [f for f in os.listdir(topics_dir) if f.endswith('.html')]

print(f"Checking {len(files)} topic files...")
all_ok = True
for fname in sorted(files):
    fpath = os.path.join(topics_dir, fname)
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

print("OVERALL RESULT:", "ALL PASSED" if all_ok else "ERRORS FOUND")
