#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Velora Bags static site build pipeline.

Usage:  python tools/build.py [css|product|chrome|seo|package|all]
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import templates, productbuild, pagebuild, seobuild, packagebuild
from common import pages


def indexable():
    return [p for p in pages() if p != "404.html"]


def stage_css():
    templates.build_css()
    print("  css      -> assets/css/style.css")


def stage_product():
    n = productbuild.build_products()
    print("  product  -> regenerated %d product detail pages" % n)
    c = productbuild.build_catalog()
    print("  catalog  -> products.html lists %d programmes" % c)


def stage_chrome():
    n = len(pagebuild.rewrite_chrome([]))
    print("  chrome   -> normalised head/header/footer on %d pages" % n)


def stage_seo():
    n = seobuild.build_sitemap(indexable())
    seobuild.build_robots()
    print("  seo      -> sitemap.xml (%d urls) + robots.txt" % n)


def stage_package():
    kept, wanted = packagebuild.build_package()
    files, size = packagebuild.zip_package()
    print("  package  -> %d assets kept (%d referenced), %d files, %.1f MB zip"
          % (kept, wanted, files, size / 1048576))


STAGES = {"css": stage_css, "product": stage_product, "chrome": stage_chrome,
          "seo": stage_seo, "package": stage_package}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    order = ["css", "product", "chrome", "seo", "package"] if which == "all" else [which]
    print("Velora Bags build: %s" % ", ".join(order))
    for name in order:
        STAGES[name]()
    print("done.")
