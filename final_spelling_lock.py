import os
import re

# 终极对齐逻辑
subs = [
    (r'VERLORABAGS', 'VERLORA'),
    (r'Verlorabags', 'Verlora'),
    (r'\bVerlora Bags\b', 'Verlora Bags')
]

exclude_dirs = {'.git', 'tools', '__pycache__', 'node_modules'}

for root, dirs, files in os.walk(r'C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith(('.html', '.xml', '.txt', '.js', '.json')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = content
            for pattern, replacement in subs:
                new_content = re.sub(pattern, replacement, new_content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Verified: {file}")
