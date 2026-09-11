import os
import re

# This regex matches ANY version of the wa-float anchor tag we might have created
pattern = re.compile(r'<a href="https://wa\.me/8613798275895[^"]*" class="wa-float"[^>]*>.*?</a>', re.DOTALL)

new_html = '<a href="https://wa.me/8613798275895?text=Hi,%20I%27m%20interested%20in%20your%20custom%20bags,%20please%20send%20catalog%20and%20price%20list." class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><img src="https://sc04.alicdn.com/kf/A1d19b8924d044a798471b09eef33c6ecw.jpg" alt="WhatsApp"></a>'

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
                print(f"Force Repaired: {path}")
