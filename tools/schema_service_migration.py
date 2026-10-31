"""One-off migration: Product -> Service structured data on product pages.

Why: Google requires offers / review / aggregateRating on Product markup.
This site sells custom OEM bags with no published prices, so every Product
node is reported as "invalid item" in Search Console. Service markup is the
honest fit: it describes the OEM manufacturing service without inventing a price.

Usage (run from the site root):
    python tools/schema_service_migration.py --check
    python tools/schema_service_migration.py --apply
"""
import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCK = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
ORG_ID = "https://www.verlorabags.com/#organization"
SERVICE_TYPE = "Custom OEM bag manufacturing"


def convert(node):
    out = {"@type": "Service"}
    for key in ("name", "image", "description"):
        if node.get(key):
            out[key] = node[key]
    out["serviceType"] = SERVICE_TYPE
    out["provider"] = node.get("manufacturer") or {"@id": ORG_ID}
    out["areaServed"] = "Worldwide"
    props = []
    if node.get("category"):
        props.append({"@type": "PropertyValue", "name": "Category", "value": node["category"]})
    if node.get("material"):
        props.append({"@type": "PropertyValue", "name": "Material", "value": node["material"]})
    if props:
        out["additionalProperty"] = props
    if node.get("url"):
        out["url"] = node["url"]
    return out


def migrate_html(text):
    """Return (new_text, converted_count)."""
    converted = [0]

    def repl(match):
        head, raw, tail = match.group(1), match.group(2), match.group(3)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match.group(0)
        nodes = data["@graph"] if isinstance(data, dict) and "@graph" in data else [data]
        changed = False
        for i, node in enumerate(nodes):
            if isinstance(node, dict) and node.get("@type") == "Product":
                nodes[i] = convert(node)
                converted[0] += 1
                changed = True
        if not changed:
            return match.group(0)
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        return head + payload + tail

    return BLOCK.sub(repl, text), converted[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--check", action="store_true", help="explicit dry run")
    ap.add_argument("--dir", default=str(ROOT / "products"))
    args = ap.parse_args()

    files = sorted(pathlib.Path(args.dir).glob("*.html"))
    total_files = total_nodes = 0
    for path in files:
        raw = path.read_bytes()
        bom = raw.startswith(b"\xef\xbb\xbf")
        text = raw.decode("utf-8-sig")
        new_text, count = migrate_html(text)
        if not count:
            continue
        total_files += 1
        total_nodes += count
        if args.apply:
            data = new_text.encode("utf-8")
            if bom:
                data = b"\xef\xbb\xbf" + data
            path.write_bytes(data)
        print("%-6s %-42s %d node(s)" % ("write" if args.apply else "would", path.name, count))

    mode = "applied" if args.apply else "dry-run"
    print("\n%s: %d file(s), %d Product node(s) -> Service" % (mode, total_files, total_nodes))
    if not args.apply and total_nodes:
        print("re-run with --apply to write the changes")


if __name__ == "__main__":
    main()
