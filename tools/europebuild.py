# -*- coding: utf-8 -*-
"""Render the Europe / EU market pages.

Every page is generated from a record in eucontent.PAGES so the head,
header, footer and structured data stay identical to the rest of the site.
Files are written UTF-8 with BOM and CRLF to match the published pages.
"""
import os

from common import rp, abs_url, asset_url, org_node, SITE
from pagebuild import build_head
from templates import header, footer

PLUS_ICON = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
             'stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>')


def faq_html(items, head):
    eyebrow, h2 = head
    rows = []
    for q, a in items:
        rows.append('<div class="faq-item reveal"><button class="faq-q">%s%s</button>'
                    '<div class="faq-a">%s</div></div>' % (q, PLUS_ICON, a))
    return ('<section class="section">\n  <div class="container">\n'
            '    <div class="section-head reveal"><span class="eyebrow">%s</span>'
            '<h2>%s</h2></div>\n    <div class="faq-list">\n      %s\n    </div>\n'
            '  </div>\n</section>' % (eyebrow, h2, "\n      ".join(rows)))


def cta_html(cta, p):
    eyebrow, h2, lead, label, href = cta
    return ('<section class="cta-dark">\n  <div class="container cta-inner reveal">\n'
            '    <span class="eyebrow eyebrow-light">%s</span>\n'
            '    <h2>%s</h2>\n    <p class="lead">%s</p>\n'
            '    <a class="btn btn-primary btn-lg" href="%s%s">%s</a>\n'
            '  </div>\n</section>' % (eyebrow, h2, lead, p, href, label))


def breadcrumb(page):
    items = [{"@type": "ListItem", "position": 1, "name": "Home",
              "item": SITE + "/"}]
    pos = 2
    if page.get("parent"):
        items.append({"@type": "ListItem", "position": pos,
                      "name": page["parent"], "item": abs_url("europe.html")})
        pos += 1
    items.append({"@type": "ListItem", "position": pos,
                  "name": page["crumb"], "item": abs_url(page["slug"])})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def faq_node(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def render(page):
    slug = page["slug"]
    p = "../" if "/" in slug else ""
    image = asset_url(page.get("image", "assets/img/hero-bags-full.webp"))
    graph = [org_node(), breadcrumb(page)]
    if page.get("faq"):
        graph.append(faq_node(page["faq"]))
    ld = {"@context": "https://schema.org", "@graph": graph}
    parts = ["<!doctype html>", '<html lang="en">',
             build_head(p, slug, page["title"], page["desc"], image, ld),
             "<body>", "", header(p), "", "<main>", page["main"].strip()]
    if page.get("faq"):
        parts.append(faq_html(page["faq"], page["faq_head"]))
    if page.get("cta"):
        parts.append(cta_html(page["cta"], p))
    parts += ["</main>", "", footer(p), "</body>", "</html>", ""]
    return "\n".join(parts)


def save(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(b"\xef\xbb\xbf" + text.replace("\n", "\r\n").encode("utf-8"))


def build_europe():
    import eucontent
    for page in eucontent.PAGES:
        save(rp(*page["slug"].split("/")), render(page))
    return len(eucontent.PAGES)


if __name__ == "__main__":
    print("  europe   -> regenerated %d pages" % build_europe())
