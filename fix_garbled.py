import os

def fix_garbled_text(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Fix the specific garbled pattern
                new_content = content.replace('鈫?/a>', '&rarr;</a>')
                new_content = new_content.replace('鈫', '&rarr;')
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed: {path}")

if __name__ == "__main__":
    fix_garbled_text(r'C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目')
