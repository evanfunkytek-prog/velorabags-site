# -*- coding: utf-8 -*-
"""Regenerate thin product detail pages and rebuild the catalog page."""
import os, re, html
import content as C
from common import rp, read, write, esc, plain, WA, BRAND
from pagebuild import collect_products, CATEGORY_TABS

ICON_BOX = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>'
ICON_STACK = '<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>'
ICON_CLOCK = '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'
ICON_TAG = '<path d="M20.6 13.4L12 22l-9-9V4h9l8.6 8.6a1.4 1.4 0 0 1 0 2z"/><circle cx="7.5" cy="7.5" r="1.5"/>'
ICON_TRUCK = '<path d="M14 17V6H2v11h12z"/><path d="M14 9h4l3 3v5h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>'
ICON_SHIELD = '<path d="M12 3l7 3v6c0 4.4-3 8.2-7 9-4-.8-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>'
ICON_SWATCH = '<circle cx="12" cy="12" r="9"/><path d="M12 3v18"/><path d="M3.6 9h16.8"/>'
ICON_BOXES = '<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 12l9 4 9-4"/><path d="M3 17l9 4 9-4"/>'

BOILERPLATE = "Premium quality custom bag solution designed for retail and brand programs"


def svg(path):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
            + path + "</svg>")


def fact_rows(rows):
    return "\n        ".join(
        '<div class="product-fact-row">{icon}<dt>{k}</dt><dd>{v}</dd></div>'.format(
            icon=svg(icon), k=esc(k), v=esc(v))
        for k, v, icon in rows)


def attr_rows(rows):
    return "\n      ".join(
        '<div class="attr"><b>{k}</b>{v}</div>'.format(k=esc(k), v=esc(v))
        for k, v in rows)


def config_card(title, text, icon):
    return ('<article class="config-card reveal"><h3>{icon}{title}</h3><p>{text}</p></article>'
            .format(icon=svg(icon), title=esc(title), text=esc(text)))


def faq_items(items):
    out = []
    for q, a in items:
        out.append('<div class="faq-item"><button class="faq-q" type="button" aria-expanded="false">'
                   '{q}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
                   '<path d="M12 5v14M5 12h14"/></svg></button>'
                   '<div class="faq-a">{a}</div></div>'.format(q=esc(q), a=esc(a)))
    return "\n      ".join(out)


def related_cards(items, p):
    out = []
    for x in items:
        img = x["image"].replace("../", "")
        out.append("""<article class="card reveal">
  <div class="card-media"><a href="{p}products/{f}"><img src="{p}{img}" alt="{name}" width="480" height="440" loading="lazy"></a></div>
  <div class="card-body"><h3><a href="{p}products/{f}">{name}</a></h3>
  <div class="card-meta"><span class="spec-line">OEM / ODM</span><a class="card-link" href="{p}products/{f}">View &rarr;</a></div></div>
</article>""".format(p=p, f=x["file"], img=img, name=esc(x["name"])))
    return "\n".join(out)


def cat_attrs(prod):
    cat = C.CATS[prod["cat"]]
    return [
        ("Material", cat["material"]),
        ("Lining &amp; finish", cat["finish"]),
        ("Branding", cat["branding"]),
        ("Handles &amp; hardware", cat["handles"]),
        ("Size range", cat["sizes"]),
        ("MOQ", "300 pcs per style and colourway"),
        ("Lead time", "15-25 days after sample approval"),
        ("Packing &amp; testing", "Polybag + export carton. " + cat["testing"]),
    ]


def pdp_main(prod, p, lead, s):
    cat = C.CATS[prod["cat"]]
    name = prod["name"]
    img = prod["image"].replace("../", "")
    q = html.escape(name, quote=True)
    hero_rows = [
        ("Material", cat["material"].split(",")[0], ICON_BOX),
        ("MOQ", "300 pcs per style", ICON_STACK),
        ("Lead time", "15-25 days", ICON_CLOCK),
    ]
    if BOILERPLATE in lead or not lead:
        lead = prod["blurb"] or cat["label"]
    intro = C.CATEGORY_INTRO.get(prod["cat"], "")
    cards = [
        config_card("Material & construction",
                    cat["material"] + ". " + cat["finish"] + ".", ICON_SWATCH),
        config_card("Branding & hardware",
                    cat["branding"] + ". " + cat["handles"] + ".", ICON_TAG),
        config_card("Order & logistics",
                    "MOQ 300 pcs per style. Lead time 15-25 days after sample approval. "
                    "Polybag and export carton packing as standard.", ICON_TRUCK),
    ]
    faq = [("Can you make %s in a custom size?" % name,
            cat["sizes"] + ". Send a drawing or a reference sample and our pattern room will match it."),
           (C.FAQ_BASE[0][0], C.FAQ_BASE[0][1].format(branding=cat["branding"]))]
    faq += C.FAQ_BASE[1:]
    others = [x for x in collect_products()
              if x["file"] != prod["file"] and x["cat"] == prod["cat"]][:3]
    if len(others) < 3:
        pool = [x for x in collect_products() if x["file"] != prod["file"] and x not in others]
        others += pool[:3 - len(others)]
    return """<main>
<section class="section" style="padding:32px 0 0">
  <div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="{p}index.html">Home</a> / <a href="{p}products.html">Products</a> / <span>{name}</span></nav></div>
</section>

<section class="section" style="padding-top:36px">
  <div class="container product-detail">
    <div class="detail-media reveal"><img src="{img}" alt="{name}" width="800" height="800"></div>
    <div class="detail-copy reveal delayed-1">
      <div class="tag-list"><span>OEM / ODM</span><span>Custom logo</span><span>{catlabel}</span></div>
      <h1>{name}</h1>
      <p class="lead">{lead}</p>
      <dl class="product-facts">
        {hero}
      </dl>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{p}quote.html?product={q}">Request a quote</a>
        <a class="btn btn-whatsapp" href="{wa}" target="_blank" rel="noopener">WhatsApp us</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--cream-100);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Customisation</span>
      <h2>Built around your spec sheet</h2>
      <p class="lead">{intro}</p>
    </div>
    <div class="config-grid">
      {cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Specifications</span><h2>Technical snapshot</h2></div>
    <div class="attr-grid">
      {attrs}
    </div>
  </div>
</section>

<section class="section" style="background:#fbf9f5;border-top:1px solid var(--line)">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Questions</span><h2>{name} FAQ</h2></div>
    <div class="faq-list">
      {faq}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">You may also like</span><h2>Related programmes</h2></div>
    <div class="product-grid">
{related}
    </div>
  </div>
</section>

<section class="quote-strip">
  <div class="container">
    <b>Ready to spec this style?</b>
    <span style="color:rgba(255,255,255,.9)">Share your target price and volume &mdash; we reply within one business day.</span>
    <a class="btn" href="{p}quote.html?product={q}">Get a quote</a>
  </div>
</section>
</main>""".format(p=p, q=q, wa=WA, name=esc(name), img=p + img, catlabel=esc(cat["label"]),
                  lead=esc(lead), hero=fact_rows(hero_rows), intro=esc(intro),
                  cards="\n      ".join(cards), attrs=attr_rows(cat_attrs(prod)),
                  faq=faq_items(faq), related=related_cards(others, p))

MAIN_RE = re.compile(r"<main\b.*?</main>", re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
LEAD_RE = re.compile(r'<p class="lead">(.*?)</p>', re.S)


def build_products():
    rebuilt = 0
    for prod in collect_products():
        path = rp("products", prod["file"])
        s = read(path)
        if 'class="quote-strip"' in s:
            continue
        m = LEAD_RE.search(s)
        lead = plain(m.group(1)) if m else ""
        new_main = pdp_main(prod, "../", lead, s)
        if MAIN_RE.search(s):
            s = MAIN_RE.sub(lambda _m: new_main, s, count=1)
        else:
            s = s.replace("<body>", "<body>\n" + new_main, 1)
        write(path, s)
        rebuilt += 1
    return rebuilt


def build_catalog():
    prods = collect_products()
    cards = []
    for x in prods:
        img = x["image"].replace("../", "")
        cards.append("""      <article class="category-card reveal p-item" data-cat="{cats}">
        <div class="category-media"><a href="products/{f}"><img src="{img}" alt="{name}" width="480" height="440" loading="lazy"></a></div>
        <div class="category-body"><h3>{name}</h3><a href="products/{f}" class="category-link">View &rarr;</a></div>
      </article>""".format(cats=x["group"] + " " + x["cat"], f=x["file"], img=img, name=esc(x["name"])))
    tabs = "\n      ".join(
        '<button class="tab-btn{act}" data-filter="{key}" type="button">{label}</button>'.format(
            act=" is-active" if key == "all" else "", key=key, label=label)
        for key, label in CATEGORY_TABS)
    main = """<main>
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">OEM / ODM catalog</span>
    <h1>Custom Bag Programmes</h1>
    <p class="lead">Every style below is a starting point. We re-engineer materials, hardware and branding to fit your brand. Filter by category, then send us your spec for a fast quote.</p>
  </div>
</section>

<section class="section">
  <div class="container" data-filter-grid>
    <div class="tabs" role="tablist">
      {tabs}
    </div>
    <div class="product-grid">
{cards}
    </div>
    <p class="empty-state">No styles in this category yet &mdash; <a href="quote.html">ask us, we probably make it</a>.</p>
    <p class="xf-page-note" style="display:block;text-align:center;color:var(--muted);margin-top:32px">{count} programmes in the current catalog. Need something else? <a href="quote.html">Send us a reference</a>.</p>
  </div>
</section>

<section class="section" style="background:#f7f6f2;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="container split">
    <div class="split-copy reveal">
      <span class="eyebrow">Direct from factory</span>
      <h2>We make bags to your drawing, not our menu</h2>
      <p class="lead">Send a photo, a sketch, or a competitor sample. Our pattern room will reverse-engineer it and quote you within two days.</p>
      <a class="btn btn-primary" href="quote.html">Send your reference</a>
    </div>
    <div class="split-media reveal delayed-1"><img src="assets/img/factory-hero.webp" alt="Bag production line at the Velora factory" width="560" height="460" loading="lazy"></div>
  </div>
</section>

<section class="quote-strip">
  <div class="container">
    <b>Looking for a style that is not listed?</b>
    <span style="color:rgba(255,255,255,.9)">Most of our business starts from a photo and a target price.</span>
    <a class="btn" href="quote.html">Get a quote</a>
  </div>
</section>
</main>""".format(tabs=tabs, cards="\n".join(cards), count=len(prods))
    s = read(rp("products.html"))
    s = MAIN_RE.sub(lambda _m: main, s, count=1)
    write(rp("products.html"), s)
    return len(prods)
