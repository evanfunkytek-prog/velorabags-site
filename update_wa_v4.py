import os
import re

# 使用用户提供的最新高清图标
new_image_url = 'https://sc04.alicdn.com/kf/A5690f913a027426aaca663ff7859bb08q.jpg'

pattern = re.compile(r'<a href="https://wa\.me/8613798275895[^"]*" class="wa-float"[^>]*>.*?</a>', re.DOTALL)

new_html = f'<a href="https://wa.me/8613798275895?text=Hi,%20I%27m%20interested%20in%20your%20custom%20bags,%20please%20send%20catalog%20and%20price%20list." class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><img src="{new_image_url}" alt="WhatsApp"></a>'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if pattern.search(content):
                new_content = pattern.sub(new_html, content)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"WhatsApp Updated: {path}")
