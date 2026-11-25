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
            "Custom Handbag & Bag Manufacturer | OEM/ODM | Verlora Bags",
            "Custom handbags, totes, crossbody and travel bags from a Guangzhou OEM/ODM factory. MOQ 100 standard / 300 custom.",
        ),
        "products.html": (
            "Custom Bags Catalog | OEM/ODM Products | Verlora Bags",
            "Explore custom handbags, totes, backpacks, travel bags and reusable packaging from a Guangzhou OEM/ODM factory. Standard styles from 100 pcs; custom orders from 300 pcs.",
        ),
        "custom-handbags.html": (
            "Custom Handbags & Fashion Totes | OEM Manufacturer",
            "OEM/ODM handbags and fashion totes in PU leather, canvas and linen. Standard styles from 100 pcs; custom orders from 300 pcs. Customize shape, lining, hardware, logo and packaging.",
        ),
        "products/handbag-tote.html": (
            "Custom Handbags & Fashion Totes | OEM/ODM",
            "Custom handbags and everyday totes in PU leather, coated canvas or washed cotton. Standard styles from 100 pcs; custom orders from 300 pcs.",
        ),
        "products/crossbody-sling.html": (
            "Custom Crossbody & Sling Bags | OEM/ODM",
            "Custom crossbody and sling bags with adjustable straps, branded hardware and practical compartments. Standard styles from 100 pcs; custom orders from 300 pcs.",
        ),
        "products/jute-bags.html": (
            "Custom Jute Shopping Bags | OEM/ODM",
            "Custom jute shopping bags with printed branding, flexible handles and export packing. Standard styles from 100 pcs; custom orders from 300 pcs.",
        ),
        "products/duffel-weekender.html": (
            "Custom Duffel & Weekender Bags for Travel | Verlora Bags",
            "Custom duffel and weekender bags for travel and gym programs. MOQ 100 standard / 300 custom.",
        ),
        "products/travel-shoulder-bag.html": (
            "Custom Travel Shoulder Bags | OEM/ODM Manufacturer",
            "Custom travel shoulder bags with adjustable straps and zip compartments. OEM/ODM branding, MOQ 100 standard / 300 custom.",
        ),
        "products/backpack.html": (
            "Custom Laptop Backpacks | OEM/ODM Manufacturer",
            "Custom laptop backpacks with padded 14-17 inch sleeves, durable shells and branded details. OEM/ODM production from Guangzhou, MOQ 100 standard / 300 custom.",
        ),
        "blog/bag-factory-qc-checklist.html": (
            "Bag QC Checklist for Importers | Verlora Bags",
            "A practical quality control checklist for importing custom bags from Guangzhou, covering materials, stitching, branding, testing and shipment checks.",
        ),
        "blog/eco-reusable-bag-trends-2026.html": (
            "2026 Reusable Bag Trends | Verlora Bags",
            "Explore recycled materials, water-based inks and lower-impact packaging options shaping reusable bag programmes in 2026.",
        ),
        "blog/handbag-materials-pu-canvas-linen.html": (
            "PU, Canvas or Linen Handbag Materials | Verlora",
            "Compare PU leather, PU-trimmed, canvas and linen handbag constructions, with sourcing questions for structure, lining, hardware and sampling.",
        ),
        "blog/custom-handbag-development-sketch-to-sample.html": (
            "Custom Handbag Development: Sketch to Sample",
            "A practical sketch-to-sample workflow for custom handbags: tech pack, dimensions, materials, hardware, sample review and bulk approval.",
        ),
        "blog/custom-handbag-moq-sampling-lead-time.html": (
            "Custom Handbag MOQ, Sampling & Lead Time",
            "Plan a custom handbag order with MOQ 100 for standard styles, MOQ 300 for custom development, 3-5 day sampling and 15-25 day production.",
        ),
        "blog/custom-canvas-tote-bags-spec-guide.html": (
            "Custom Canvas Tote Bags: Spec & Print Guide",
            "A buyer's guide to custom canvas totes: fabric weight, handles, gussets, lining, printing, MOQ, sampling and QC.",
        ),
        "blog/custom-travel-bags-backpacks-oem-guide.html": (
            "Custom Travel Bags & Backpacks: OEM Guide",
            "Specify custom duffels, travel shoulder bags and laptop backpacks: materials, structure, branding, testing, MOQ and lead time.",
        ),
        "blog/custom-promotional-bags-corporate-guide.html": (
            "Custom Promotional Bags for Corporate Programs",
            "Compare non-woven, woven PP, paper, jute and canvas promotional bags, plus printing, MOQ, sampling, QC and packing.",
        ),
        "products/personalized-coated-linen-bag.html": (
            "Custom Coated Linen Bag | OEM/ODM | Verlora",
            "Custom coated linen bags with personalized branding for gifting and retail programmes. MOQ 100 standard / 300 custom.",
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
        desc = desc.replace("Standard styles from 100 pcs; custom orders from 300 pcs", "MOQ 100 standard / 300 custom")
        if relpath == "products.html":
            desc = "Explore custom handbags, totes, backpacks, travel bags and reusable packaging from a Guangzhou OEM/ODM factory. MOQ 100 standard / 300 custom."
        if relpath.startswith("products/") and len(desc) > 160:
            desc = "Custom " + plain(title).split("|")[0].strip() + ". MOQ 100 standard / 300 custom. OEM/ODM production from Guangzhou."
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
        elif relpath == "custom-handbags.html":
            organization = org_node()
            organization["@id"] = SITE + "/#organization"
            ld = {"@context": "https://schema.org", "@graph": [
                organization,
                {"@type": "WebSite", "@id": SITE + "/#website",
                 "name": BRAND, "url": SITE + "/",
                 "publisher": {"@id": SITE + "/#organization"}},
                {"@type": "CollectionPage", "name": title,
                 "description": desc, "url": abs_url(relpath),
                 "isPartOf": {"@id": SITE + "/#website"},
                 "about": {"@type": "Thing", "name": "Custom handbags and fashion totes"}},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Products", "item": SITE + "/products"},
                    {"@type": "ListItem", "position": 3, "name": "Custom Handbags", "item": abs_url(relpath)}]}]}
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
                  "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"}}
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
        # Apply the confirmed commercial facts consistently to generated product copy.
        s = s.replace("MOQ 300 pcs per style and colourway", "Standard styles from 100 pcs; custom orders from 300 pcs")
        s = s.replace("MOQ 300 pcs per style", "Standard styles from 100 pcs; custom orders from 300 pcs")
        s = s.replace("MOQ 300 pcs", "Standard styles from 100 pcs; custom orders from 300 pcs")
        s = s.replace("A pre-production sample usually takes 7-10 days.", "A pre-production sample usually takes 3-5 days after artwork approval.")
        if relpath.startswith("blog/") and relpath != "blog.html":
            s = add_blog_resource_links(s, p)
        s = add_lazy_loading(s)
        s = tidy(s)
        write(rp(*relpath.split("/")), s)
        if not noindex:
            indexable.append(relpath)
    return indexable
