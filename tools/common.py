# -*- coding: utf-8 -*-
"""Shared helpers for the Velora Bags build pipeline."""
import os, re, json, html
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = C.SITE
BRAND = C.BRAND
EMAIL = C.EMAIL
PHONE = C.PHONE
WA = C.WA
ADDRESS = C.ADDRESS
HOURS = C.HOURS
CSS_VERSION = "2.3"
LOGO_VERSION = "1.2"
SKIP_DIRS = {".git", "research", "tools", "package", "dist", "node_modules"}


def rp(*parts):
    return os.path.join(ROOT, *parts)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def read(path):
    with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
        return fh.read().replace("\r\n", "\n")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def pages():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(".html"):
                out.append(rel(os.path.join(base, name)))
    return sorted(out)


def esc(text):
    return html.escape(text or "", quote=True)


def plain(text):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    return re.sub(r"\s+", " ", text).strip()


def abs_url(relpath):
    return SITE + "/" + relpath.lstrip("/")


def asset_url(src):
    src = (src or "").replace("\\", "/")
    while src.startswith("../"):
        src = src[3:]
    if not src.startswith("assets/"):
        src = "assets/img/hero-bags-full.webp"
    return SITE + "/" + src


def jsonld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def org_node():
    return {"@type": "Organization", "name": BRAND, "url": SITE + "/",
            "logo": SITE + "/assets/svg/logo.svg",
            "email": EMAIL, "telephone": PHONE,
            "address": {"@type": "PostalAddress",
                        "streetAddress": "No. 8 Huasheng Rd, Shiling",
                        "addressLocality": "Guangzhou",
                        "addressRegion": "Guangdong",
                        "addressCountry": "CN"}}
