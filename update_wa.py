import os

old_snippet = '<a href="https://wa.me/8613798275895" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><img src="assets/img/wa-float.jpg" alt="WhatsApp"></a>'
new_snippet = '<a href="https://wa.me/8613798275895?text=Hi,%20I%27m%20interested%20in%20your%20custom%20bags,%20please%20send%20catalog%20and%20price%20list." class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><img src="assets/img/wa-chat.jpg" alt="WhatsApp"></a>'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_snippet in content:
                new_content = content.replace(old_snippet, new_snippet)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {path}")
