# -*- coding: utf-8 -*-
"""sitemap.xml / robots.txt generation."""
from common import rp, write, SITE

BUILD_DATE = "2026-09-11"


def entry(relpath, priority, freq, date=BUILD_DATE):
    loc = SITE + "/" if relpath == "index.html" else SITE + "/" + relpath
    return ("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq>"
            "<priority>%.1f</priority></url>" % (loc, date, freq, priority))


def build_sitemap(indexable):
    top = {"index.html", "products.html", "quote.html", "contact.html",
           "about.html", "factory-tour.html", "certifications.html",
           "industries.html", "blog.html"}
    rows = []
    order = {name: i for i, name in enumerate(
        ["index.html", "products.html", "about.html", "factory-tour.html",
         "certifications.html", "industries.html", "quote.html", "contact.html", "blog.html"])}
    def sort_key(relpath):
        if relpath in order:
            return (0, order[relpath], relpath)
        if relpath.startswith("products/"):
            return (1, 0, relpath)
        if relpath.startswith("blog/"):
            return (2, 0, relpath)
        return (3, 0, relpath)
    for relpath in sorted(indexable, key=sort_key):
        if relpath == "index.html":
            rows.append(entry(relpath, 1.0, "weekly"))
        elif relpath in ("products.html", "quote.html"):
            rows.append(entry(relpath, 0.9, "weekly"))
        elif relpath == "contact.html":
            rows.append(entry(relpath, 0.8, "monthly"))
        elif relpath.startswith("products/"):
            rows.append(entry(relpath, 0.8, "monthly"))
        elif relpath.startswith("blog/") and relpath != "blog.html":
            rows.append(entry(relpath, 0.6, "monthly"))
        elif relpath == "blog.html":
            rows.append(entry(relpath, 0.7, "weekly"))
        elif relpath in top:
            rows.append(entry(relpath, 0.7, "monthly"))
        else:
            rows.append(entry(relpath, 0.5, "yearly"))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    write(rp("sitemap.xml"), xml)
    return len(rows)


def build_robots():
    write(rp("robots.txt"),
          "User-agent: *\n"
          "Allow: /\n"
          "Disallow: /404.html\n\n"
          "Sitemap: %s/sitemap.xml\n" % SITE)
