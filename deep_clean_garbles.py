import os

# 定义全站乱码清理逻辑（针对已发现的所有乱码变体）
garble_patterns = [
    ("鈥?", "—"),
    ("鈥", "—"),
    ("虏", "²"),
    ("鈥敱浂", " — ")
]

def clean_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for old, new in garble_patterns:
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Deep Cleaned: {path}")

# 执行清理
for root, dirs, files in os.walk(r'C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目'):
    if '.git' in dirs: dirs.remove('.git')
    for file in files:
        if file.endswith('.html'):
            clean_file(os.path.join(root, file))
