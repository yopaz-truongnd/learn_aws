import os
import re

print("=== Checking all Mermaid diagrams in topics/ ===")
for f in sorted(os.listdir('topics')):
    if f.endswith('.html') and not f.endswith('.backup.html'):
        p = os.path.join('topics', f)
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        
        matches = list(re.finditer(r'<div class="mermaid-diagram"[^>]*>', content))
        if matches:
            for idx, m in enumerate(matches):
                start = m.end()
                # find closing div for mermaid-diagram
                # it may have inner divs or not
                has_src = 'class="mermaid-src' in content[start:start+100]
                print(f"{f} [Diagram {idx+1}]: has_src={has_src}")
