import os

# 定义修复逻辑
replacements = [
    {
        "path": "blog/how-to-choose-bag-fabrics.html",
        "old_part": "non-negotiable",
        "target_line": "When durability is non-negotiable",
        "new_line": "            <p>When durability is non-negotiable — such as in backpacks or travel duffels — Oxford fabric (especially 600D to 1680D) is the winner. It's water-resistant, highly abrasion-resistant, and perfect for commuter tech bags.</p>"
    },
    {
        "path": "blog/eco-reusable-bag-trends-2026.html",
        "old_part": "longer news",
        "target_line": "The global ban on single-use plastics is no longer news",
        "new_line": "            <p>The global ban on single-use plastics is no longer news — the new headline is Circularity. Brands are moving beyond 'reusable' and demanding 'recycled' and 'recyclable'.</p>"
    }
]

for item in replacements:
    full_path = os.path.join(r"C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目", item["path"])
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(full_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if item["target_line"] in line:
                    f.write(item["new_line"] + "\n")
                    print(f"Fixed: {item['path']}")
                else:
                    f.write(line)
