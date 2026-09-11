import os
import re

# 定义替换逻辑
subs = [
    (r'\bVelora Bags\b', 'Verlora Bags'),
    (r'\bVelora\b', 'Verlora'),
    (r'velorabags\.com', 'verlorabags.com'),
    (r'VELORA', 'VERLORABAGS')
]

# 排除目录
exclude_dirs = {'.git', 'tools', '__pycache__', 'node_modules'}

count = 0
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
                print(f"Corrected: {file}")
                count += 1

print(f"Total files corrected: {count}")
