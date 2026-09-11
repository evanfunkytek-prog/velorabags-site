import os

# 定义修复逻辑
# 规则：匹配乱码特征并恢复为正确的英文标点或符号
replacements = [
    {
        "path": "about.html",
        "subs": [
            ("About Velora 鈥?Bag Factory", "About Velora — Bag Factory"),
            ("five continents 鈥?starting", "five continents — starting"),
            ("18,000 m虏", "18,000 m²"),
            ("knows your product 鈥?and big", "knows your product — and big"),
            ("your carton 鈥?retail-ready", "your carton — retail-ready"),
            ("Rush options exist 鈥?but", "Rush options exist — but"),
            ("Yes 鈥?two owned sites", "Yes — two owned sites"),
            ("develop 1鈥? rounds", "develop 1-3 rounds")
        ]
    },
    {
        "path": "industries.html",
        "subs": [
            ("beauty and promo markets 鈥?OEM/ODM", "beauty and promo markets — OEM/ODM"),
            ("and order rhythm 鈥?we have", "and order rhythm — we have"),
            ("D2C labels 鈥?small runs", "D2C labels — small runs"),
            ("300鈥?00 pcs", "300-500 pcs"),
            ("2鈥? week samples", "2-3 week samples"),
            ("1,000鈥?,000 pcs", "1,000-3,000 pcs")
        ]
    }
]

for item in replacements:
    full_path = os.path.join(r"C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目", item["path"])
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old_txt, new_txt in item["subs"]:
            new_content = new_content.replace(old_txt, new_txt)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned: {item['path']}")
