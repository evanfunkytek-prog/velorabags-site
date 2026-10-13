from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent
PRODUCTS = ROOT / 'products'
CHECK = ['index.html', 'products/duffel-weekender.html', 'products/travel-shoulder-bag.html', 'products/backpack.html']

errors = []
html_files = sorted(ROOT.rglob('*.html'))
html_files = [p for p in html_files if 'EliteBox-结构化数据修复' not in p.parts]
for path in html_files:
    text = path.read_text(encoding='utf-8-sig')
    if '<title>' not in text:
        errors.append(f'{path.relative_to(ROOT)}: missing title')
    if '<link rel="canonical"' not in text and path.name != '404.html':
        errors.append(f'{path.relative_to(ROOT)}: missing canonical')
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            json.loads(raw)
        except Exception as exc:
            errors.append(f'{path.relative_to(ROOT)}: invalid JSON-LD: {exc}')

sitemap = ROOT / 'sitemap.xml'
root = ET.parse(sitemap).getroot()
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
locs = [x.text for x in root.findall('sm:url/sm:loc', ns)]
for loc in locs:
    if 'verlorabags.com' not in loc:
        errors.append(f'sitemap foreign host: {loc}')

for rel in CHECK:
    text = (ROOT / rel).read_text(encoding='utf-8-sig')
    print(f'CHECK {rel}')
    for pattern in [r'<title>(.*?)</title>', r'<h1[^>]*>(.*?)</h1>', r'<link rel="canonical" href="(.*?)">']:
        m = re.search(pattern, text, re.S)
        print(' ', pattern, '=>', re.sub(r'\s+', ' ', m.group(1)).strip() if m else 'MISSING')
    print('  product_jsonld=', bool(re.search(r'"@type":"Product"', text)))
    print('  aggregateRating=', 'aggregateRating' in text)
    print('  review=', '"review"' in text)

print('html_files=', len(html_files))
print('sitemap_urls=', len(locs))
print('sitemap_lastmod=', sorted(set(re.findall(r'<lastmod>(.*?)</lastmod>', sitemap.read_text(encoding='utf-8')))))
print('errors=', errors)
if errors:
    raise SystemExit(1)
