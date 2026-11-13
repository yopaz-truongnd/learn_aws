with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'class="module-title"' in line:
        title_content = []
        for j in range(i, min(i+5, len(lines))):
            title_content.append(lines[j].strip())
            if '</div>' in lines[j]:
                break
        print(f"Line {i+1}: " + " ".join(title_content))
