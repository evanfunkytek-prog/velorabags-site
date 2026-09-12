# -*- coding: utf-8 -*-
"""Re-apply the shared header and footer to every page.

Same job as the chrome stage of build.py, but byte-safe: published pages are
UTF-8 with BOM and CRLF, and the stock writer would silently strip both. This
keeps each file's existing encoding intact.
"""
import re

from common import rp, pages
from templates import header, footer

HEADER_RE = re.compile(r"<header\b.*?</header>", re.S)
FOOTER_RE = re.compile(r"<footer\b.*?</footer>", re.S)
WAFLOAT_RE = re.compile(r'<a[^>]*class="wa-float".*?</a>', re.S)
JS_RE = re.compile(r'<script src="[^"]*main\.js[^"]*"></script>', re.I)


def sync_one(relpath):
    path = rp(*relpath.split("/"))
    raw = open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    crlf = "\r\n" in text
    p = "../" if "/" in relpath else ""

    head_html = header(p)
    foot_html = footer(p)
    if crlf:
        head_html = head_html.replace("\n", "\r\n")
        foot_html = foot_html.replace("\n", "\r\n")

    if HEADER_RE.search(text):
        text = HEADER_RE.sub(lambda _m: head_html, text, count=1)
    text = FOOTER_RE.sub("", text)
    text = WAFLOAT_RE.sub("", text)
    text = JS_RE.sub("", text)
    text = text.replace("</body>", foot_html + "</body>")

    open(path, "wb").write((b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8"))
    return not bom


def sync_all():
    changed = 0
    no_bom = []
    for relpath in pages():
        if sync_one(relpath):
            no_bom.append(relpath)
        changed += 1
    return changed, no_bom


if __name__ == "__main__":
    n, no_bom = sync_all()
    print("  chrome   -> header/footer synced on %d pages" % n)
    if no_bom:
        print("  note     -> %d page(s) had no BOM: %s" % (len(no_bom), ", ".join(no_bom[:5])))
