import os
import re

files_to_upgrade = [
    'aws_analytics.html',
    'aws_congratulations.html',
    'aws_containers.html',
    'aws_disaster_recovery.html',
    'aws_iam_advanced.html',
    'aws_monitoring.html',
    'aws_other_services.html',
    'aws_practice_exam.html',
    'aws_security.html',
    'aws_serverless.html',
    'aws_solution_architectures.html',
    'aws_storage_extras.html',
    'aws_vpc.html',
    'aws_whitepapers.html'
]

for filename in files_to_upgrade:
    filepath = os.path.join('topics', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all <div class="mermaid-diagram"> that do NOT have <div class="mermaid-src
    def replacer(match):
        inner = match.group(1).strip()
        if '<div class="mermaid-src' in inner:
            return match.group(0)
        
        # Clean inner code if necessary
        clean_code = inner.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        
        return f'''<div class="mermaid-diagram">
    <div class="mermaid-src lang-vi" style="display:none">
{clean_code}
    </div>
    <div class="mermaid-src lang-en" style="display:none">
{clean_code}
    </div>
    <div class="mermaid-output"></div>
  </div>'''

    new_content = re.sub(r'<div class="mermaid-diagram"[^>]*>(.*?)</div>', replacer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Upgraded {filename}")
    else:
        print(f"No changes needed for {filename}")

print("Upgrade finished.")
