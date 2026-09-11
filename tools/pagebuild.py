# -*- coding: utf-8 -*-
"""Head/SEO normalisation and page chrome stitching."""
import os, re
import content as C
from common import (rp, read, write, pages, esc, plain, abs_url, asset_url,
                    jsonld, org_node, SITE, BRAND, CSS_VERSION)
from templates import header, footer

HEAD_RE = re.compile(r"<head>.*?</head>", re.S)
HEADER_RE = re.compile(r"<header\b.*?</header>", re.S)
FOOTER_RE = re.compile(r"<footer\b.*?</footer>", re.S)
WAFLOAT_RE = re.compile(r'<a[^>]*class="wa-float".*?</a>', re.S)
JS_RE = re.compile(r'<script src="[^"]*main\.js[^"]*"></script>', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)">', re.S)
IMG_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)


def main_image(s):
    m = re.search(r'class="detail-media[^"]*"[^>]*>\s*<img[^>]+src="([^"]+)"', s)
    if m:
        return m.group(1)
    body = s.split("<body", 1)[-1]
    for src in IMG_RE.findall(body):
        if ("assets/img/" in src and "wa-" not in src and "logo" not in src
                and ".svg" not in src.lower()):
            return src
    return "assets/img/hero-bags-full.webp"


def build_head(p, relpath, title, desc, image, ld=None, noindex=False):
    out = ['<meta charset="utf-8">',
           '<meta name="viewport" content="width=device-width, initial-scale=1">',
           "<title>%s</title>" % esc(title)]
    if desc:
        out.append('<meta name="description" content="%s">' % esc(desc))
    if noindex:
        out.append('<meta name="robots" content="noindex, follow">')
    else:
        out.append('<link rel="canonical" href="%s">' % abs_url(relpath))
    ogtype = "article" if (relpath.startswith("blog/")) else "website"
    out += ['<meta property="og:type" content="%s">' % ogtype,
            '<meta property="og:site_name" content="%s">' % esc(BRAND),
            '<meta property="og:locale" content="en_US">',
            '<meta property="og:title" content="%s">' % esc(title),
            '<meta property="og:description" content="%s">' % esc(desc or title),
            '<meta property="og:url" content="%s">' % abs_url(relpath),
            '<meta property="og:image" content="%s">' % image,
            '<meta name="twitter:card" content="summary_large_image">',
            '<meta name="twitter:title" content="%s">' % esc(title),
            '<meta name="twitter:description" content="%s">' % esc(desc or title),
            '<meta name="twitter:image" content="%s">' % image,
            '<link rel="icon" href="%sassets/svg/favicon.svg" type="image/svg+xml">' % p,
            '<link rel="stylesheet" href="%sassets/css/style.css?v=%s">' % (p, CSS_VERSION)]
    if ld:
        out.append(jsonld(ld))
    return "<head>\n" + "\n".join(out) + "\n</head>"


CATEGORY_TABS = [
    ("all", "All products"),
    ("bags", "Totes &amp; shoppers"),
    ("travel", "Travel &amp; outdoor"),
    ("eco", "Eco &amp; packaging"),
    ("promo", "Promotional"),
]

CAT_GROUP = {
    "jute": "bags", "linen": "bags", "canvas": "bags", "tote": "bags",
    "backpack": "travel", "duffel": "travel", "trolley": "travel",
    "laptop": "travel", "polyester": "travel",
    "nonwoven": "eco", "wovenpp": "eco", "paper": "eco", "tyvek": "eco",
    "cooler": "promo", "pvc": "promo", "mesh": "promo", "felt": "promo",
    "drawstring": "promo",
}


def collect_products():
    out = []
    d = rp("products")
    for name in sorted(os.listdir(d)):
        if not name.endswith(".html"):
            continue
        s = read(os.path.join(d, name))
        m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        cat = C.PAGE_CAT.get(name, "jute")
        out.append({"file": name,
                    "name": plain(m.group(1)) if m else name[:-5].replace("-", " ").title(),
                    "image": main_image(s),
                    "cat": cat,
                    "group": CAT_GROUP.get(cat, "promo"),
                    "blurb": C.PAGE_BLURB.get(name, "")})
    return out


def rewrite_chrome(indexable):
    """Normalise <head>, header and footer on every page. Returns indexable paths."""
    prods = {x["file"]: x for x in collect_products()}
    for relpath in pages():
        s = read(rp(*relpath.split("/")))
        p = "../" if "/" in relpath else ""
        t = TITLE_RE.search(s)
        title = plain(t.group(1)) if t else BRAND
        d = DESC_RE.search(s)
        desc = plain(d.group(1)) if d else ""
        img = asset_url(main_image(s))
        if relpath.startswith("blog/") and relpath != "blog.html":
            share = C.BLOG_IMAGES.get(relpath.split("/", 1)[1])
            if share:
                img = asset_url(share)
        noindex = relpath == "404.html"
        ld = None
        if relpath == "index.html":
            ld = {"@context": "https://schema.org", "@graph": [
                org_node(),
                {"@type": "WebSite", "name": BRAND, "url": SITE + "/"}]}
        elif relpath.startswith("products/"):
            prod = prods.get(relpath.split("/", 1)[1])
            if prod:
                cat = C.CATS[prod["cat"]]
                if not desc:
                    desc = prod["blurb"]
                ld = {"@context": "https://schema.org", "@graph": [
                    {"@type": "Product", "name": prod["name"],
                     "image": asset_url(prod["image"]),
                     "description": desc,
                     "category": cat["label"],
                     "material": cat["material"],
                     "brand": {"@type": "Brand", "name": BRAND},
                     "manufacturer": org_node(),
                     "url": abs_url(relpath)},
                    {"@type": "BreadcrumbList", "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                        {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/products.html"},
                        {"@type": "ListItem", "position": 3, "name": prod["name"], "item": abs_url(relpath)}]}]}
        elif relpath.startswith("blog/") and relpath != "blog.html":
            ld = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title, "description": desc, "image": img,
                  "datePublished": C.BLOG_DATES.get(relpath.split("/", 1)[1], C.BUILD_DATE),
                  "dateModified": C.BUILD_DATE,
                  "mainEntityOfPage": abs_url(relpath),
                  "publisher": org_node(),
                  "author": {"@type": "Organization", "name": BRAND}}
        s = HEAD_RE.sub(lambda _m: build_head(p, relpath, title, desc, img, ld, noindex), s, count=1)
        if HEADER_RE.search(s):
            s = HEADER_RE.sub(lambda _m: header(p), s, count=1)
        s = FOOTER_RE.sub("", s)
        s = WAFLOAT_RE.sub("", s)
        s = JS_RE.sub("", s)
        s = s.replace("</body>", footer(p) + "</body>")
        write(rp(*relpath.split("/")), s)
        if not noindex:
            indexable.append(relpath)
    return indexable
