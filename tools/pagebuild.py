# -*- coding: utf-8 -*-
"""Head/SEO normalisation and page chrome stitching."""
import os, re
import content as C
from common import (rp, read, write, pages, esc, plain, abs_url, asset_url, tidy,
                    jsonld, org_node, iso_dt, SITE, BRAND, CSS_VERSION, link_prefix)
from templates import header, footer

HEAD_RE = re.compile(r"<head>.*?</head>", re.S)
HEADER_RE = re.compile(r"<header\b.*?</header>", re.S)
FOOTER_RE = re.compile(r"<footer\b.*?</footer>", re.S)
WAFLOAT_RE = re.compile(r'<a[^>]*class="wa-float".*?</a>', re.S)
JS_RE = re.compile(r'<script src="[^"]*main\.js[^"]*"></script>', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)">', re.S)
IMG_RE = re.compile(r'<img[^>]+src="([^"]+)"[^>]*>', re.I)
IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.I)


def add_lazy_loading(s):
    """Lazy-load below-the-fold content images without delaying the hero image."""
    first_content_image = False

    def replace(match):
        nonlocal first_content_image
        tag = match.group(0)
        src_match = re.search(r'\bsrc="([^"]+)"', tag, re.I)
        src = src_match.group(1).lower() if src_match else ""
        if (not src or src.endswith(".svg") or "logo.svg" in src
                or "favicon" in src or "wa-float" in src):
            return tag
        if "loading=" in tag.lower():
            first_content_image = True
            return tag
        if not first_content_image:
            first_content_image = True
            return tag
        if tag.rstrip().endswith("/>"):
            return tag.rstrip()[:-2].rstrip() + ' loading="lazy"/>'
        return tag[:-1] + ' loading="lazy">'

    return IMG_TAG_RE.sub(replace, s)


def add_blog_resource_links(s, p):
    """Give every article useful paths to products, solutions and quotation."""
    if 'data-seo-related-resources="blog"' in s:
        return s
    block = """<section class="section" data-seo-related-resources="blog" style="background:var(--cream-100);border-top:1px solid var(--line)">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Next steps</span><h2>Plan your bag programme</h2></div>
    <p class="lead">Compare relevant <a href="{p}products/jute-bags">material programmes</a>, review <a href="{p}products/backpack">travel bag options</a>, or explore our <a href="{p}industries">industry solutions</a> before sending a brief.</p>
    <p><a class="btn btn-primary" href="{p}quote">Request a factory quote</a> <a class="btn" href="{p}factory-tour">See the Guangzhou factory</a></p>
  </div>
</section>
""".format(p=p)
    return s.replace("</main>", block + "</main>", 1)


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
    if relpath != "404.html":
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
    if C.GSC_VERIFICATION:
        out.append('<meta name="google-site-verification" content="%s">'
                   % esc(C.GSC_VERIFICATION))
    if C.BING_VERIFICATION:
        out.append('<meta name="msvalidate.01" content="%s">'
                   % esc(C.BING_VERIFICATION))
    if C.GA4_ID:
        out.append('<script async src="https://www.googletagmanager.com/gtag/js'
                   '?id=%s"></script>' % C.GA4_ID)
        out.append('<script>window.dataLayer=window.dataLayer||[];function gtag()'
                   '{dataLayer.push(arguments);}gtag("js",new Date());'
                   'gtag("config","%s");</script>' % C.GA4_ID)
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
    seo_overrides = {
        "index.html": (
            "Custom Bags Manufacturer | Guangzhou OEM/ODM Factory",
            "Custom bags from a Guangzhou factory: OEM/ODM travel, jute, canvas and reusable bag programmes for brands and retailers. Request a quote.",
        ),
        "products/duffel-weekender.html": (
            "Custom Duffel & Weekender Bags for Travel | Verlora Bags",
            "Custom duffel and weekender bags for travel and gym programs, with reinforced bases, shoe compartments, trolley sleeves and branding. MOQ 300 pcs, OEM/ODM.",
        ),
        "products/travel-shoulder-bag.html": (
            "Custom Travel Shoulder Bags | OEM/ODM Manufacturer",
            "Custom travel shoulder bags with adjustable straps and zip compartments. OEM/ODM branding, MOQ 300 pcs and factory-direct production.",
        ),
        "products/backpack.html": (
            "Custom Laptop Backpacks | OEM/ODM Manufacturer",
            "Custom laptop backpacks with padded 14-17 inch sleeves, durable shells and branded details. OEM/ODM production from Guangzhou, MOQ 300 pcs.",
        ),
    }
    for relpath in pages():
        s = read(rp(*relpath.split("/")))
        p = link_prefix(relpath)
        t = TITLE_RE.search(s)
        title = plain(t.group(1)) if t else BRAND
        d = DESC_RE.search(s)
        desc = plain(d.group(1)) if d else ""
        if relpath in seo_overrides:
            title, desc = seo_overrides[relpath]
        img = asset_url(main_image(s))
        if relpath.startswith("blog/") and relpath != "blog.html":
            share = C.BLOG_IMAGES.get(relpath.split("/", 1)[1])
            if share:
                img = asset_url(share)
        noindex = relpath in {"404.html", "privacy.html", "terms.html"}
        ld = None
        if relpath == "index.html":
            organization = org_node()
            organization["@id"] = SITE + "/#organization"
            ld = {"@context": "https://schema.org", "@graph": [
                organization,
                {"@type": "WebSite", "@id": SITE + "/#website",
                 "name": BRAND, "url": SITE + "/",
                 "publisher": {"@id": SITE + "/#organization"}}]}
        elif relpath.startswith("products/"):
            prod = prods.get(relpath.split("/", 1)[1])
            if prod:
                cat = C.CATS[prod["cat"]]
                if relpath in seo_overrides:
                    desc = seo_overrides[relpath][1]
                if not desc:
                    desc = prod["blurb"]
                organization = org_node()
                organization["@id"] = SITE + "/#organization"
                ld = {"@context": "https://schema.org", "@graph": [
                    organization,
                    {"@type": "WebSite", "@id": SITE + "/#website",
                     "name": BRAND, "url": SITE + "/",
                     "publisher": {"@id": SITE + "/#organization"}},
                    {"@type": "Product", "name": prod["name"],
                     "image": asset_url(prod["image"]),
                     "description": desc,
                     "category": cat["label"],
                     "material": cat["material"],
                     "brand": {"@type": "Brand", "name": BRAND},
                     "manufacturer": {"@id": SITE + "/#organization"},
                     "url": abs_url(relpath)},
                    {"@type": "BreadcrumbList", "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                        {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/products"},
                        {"@type": "ListItem", "position": 3, "name": prod["name"], "item": abs_url(relpath)}]}]}
        elif relpath.startswith("blog/") and relpath != "blog.html":
            ld = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title, "description": desc, "image": img,
                  "datePublished": iso_dt(C.BLOG_DATES.get(relpath.split("/", 1)[1], C.BUILD_DATE)),
                  "dateModified": iso_dt(C.BUILD_DATE),
                  "mainEntityOfPage": abs_url(relpath),
                  "publisher": org_node(),
                  "author": {"@type": "Organization", "name": BRAND}}
        s = HEAD_RE.sub(lambda _m: build_head(p, relpath, title, desc, img, ld, noindex), s, count=1)
        chrome_head, chrome_foot = header(p), footer(p)
        if p == "/":
            # the templates emit "/." for the home link; keep it as plain "/"
            chrome_head = chrome_head.replace('href="/."', 'href="/"')
            chrome_foot = chrome_foot.replace('href="/."', 'href="/"')
        if HEADER_RE.search(s):
            s = HEADER_RE.sub(lambda _m: chrome_head, s, count=1)
        s = FOOTER_RE.sub("", s)
        s = WAFLOAT_RE.sub("", s)
        s = JS_RE.sub("", s)
        s = s.replace("</body>", chrome_foot + "</body>")
        # Cloudflare Pages serves clean extensionless URLs; keep internal links on the same canonical form.
        if relpath != "404.html":
            def clean_href(match):
                path = match.group("path")
                if path.endswith("index"):
                    path = path[:-5] or "."
                return match.group("prefix") + path + match.group("suffix")
            s = re.sub(r'(?P<prefix>href=")(?P<path>(?:\.\./|/)?[^"#?]+)\.html(?P<suffix>(?:[?#][^"]*)?")', clean_href, s)
        if relpath.startswith("blog/") and relpath != "blog.html":
            s = add_blog_resource_links(s, p)
        s = add_lazy_loading(s)
        s = tidy(s)
        write(rp(*relpath.split("/")), s)
        if not noindex:
            indexable.append(relpath)
    return indexable
