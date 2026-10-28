# -*- coding: utf-8 -*-
"""sitemap.xml / robots.txt generation."""
import os
import re
import subprocess

import content as C
from common import rp, write, SITE

BUILD_DATE = C.BUILD_DATE
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_dates = {}


def last_modified(relpath):
    """Real last commit date for a page, so lastmod is not a single build stamp."""
    if relpath in _dates:
        return _dates[relpath]
    date = ""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", relpath.replace("\\", "/")],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=15)
        date = out.stdout.strip()
    except Exception:
        date = ""
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        date = BUILD_DATE
    _dates[relpath] = date
    return date


def clean_path(relpath):
    relpath = relpath.replace("\\", "/")
    if relpath == "index.html":
        return ""
    return relpath[:-5] if relpath.endswith(".html") else relpath


def entry(relpath, priority, freq, date=None):
    clean = clean_path(relpath)
    date = date or last_modified(relpath)
    loc = SITE + "/" if not clean else SITE + "/" + clean
    return ("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq>"
            "<priority>%.1f</priority></url>" % (loc, date, freq, priority))


def build_sitemap(indexable):
    top = {"index.html", "products.html", "quote.html", "contact.html",
           "about.html", "factory-tour.html", "certifications.html",
           "industries.html", "blog.html", "europe.html", "eu-compliance.html"}
    rows = []
    order = {name: i for i, name in enumerate(
        ["index.html", "products.html", "about.html", "factory-tour.html",
         "certifications.html", "industries.html", "quote.html", "contact.html",
         "blog.html", "europe.html", "eu-compliance.html"])}
    def sort_key(relpath):
        if relpath in order:
            return (0, order[relpath], relpath)
        if relpath.startswith("products/"):
            return (1, 0, relpath)
        if relpath.startswith("blog/"):
            return (2, 0, relpath)
        if relpath.startswith("markets/"):
            return (3, 0, relpath)
        return (4, 0, relpath)
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
        elif relpath.startswith("markets/"):
            rows.append(entry(relpath, 0.8, "monthly"))
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
