# -*- coding: utf-8 -*-
"""Shared helpers for the Verlora Bags build pipeline."""
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
SKIP_DIRS = {".git", "research", "tools", "package", "dist", "node_modules",
             "EliteBox-Packaging", "Verlora-\u7d22\u5f15\u4fee\u590d-20261013"}


def rp(*parts):
    return os.path.join(ROOT, *parts)


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def read(path):
    with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
        return fh.read().replace("\r\n", "\n")


def write(path, text):
    """Write text, preserving the conventions of the file already on disk.

    Published pages are UTF-8 with BOM and CRLF, the stylesheet is CRLF with
    no BOM, generated XML is plain LF. Rebuilding must not silently change
    any of that, so match whatever is there rather than imposing one style.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bom = crlf = False
    if os.path.exists(path):
        with open(path, "rb") as fh:
            raw = fh.read()
        bom = raw.startswith(b"\xef\xbb\xbf")
        crlf = b"\r\n" in raw
    body = text.replace("\r\n", "\n")
    if crlf:
        body = body.replace("\n", "\r\n")
    with open(path, "wb") as fh:
        fh.write((b"\xef\xbb\xbf" if bom else b"") + body.encode("utf-8"))


def pages():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS
                   and not d.startswith(".")
                   and not os.path.isdir(os.path.join(base, d, ".git"))]
        for name in files:
            if name.endswith(".html"):
                out.append(rel(os.path.join(base, name)))
    return sorted(out)


def link_prefix(relpath):
    """Link prefix for the header/footer templates.

    Normal pages use "" at the root and "../" one level down. The 404 page is
    different: Cloudflare serves it for any missing path, so its links have to
    be root-absolute. With a relative prefix the browser would resolve them
    against the directory of the typed URL, so /products/nope would ask for
    /products/assets/css/style.css and render unstyled.
    """
    if relpath == "404.html":
        return "/"
    return "../" if "/" in relpath else ""


def esc(text):
    return html.escape(text or "", quote=True)


def plain(text):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    return re.sub(r"\s+", " ", text).strip()


PROTECTED_RE = re.compile(r"<(pre|textarea)\b.*?</\1>", re.S | re.I)
BLANK_RUN_RE = re.compile(r"(?:\r\n|\n){2,}")


def tidy(text):
    """Collapse runs of blank lines to a single blank line.

    The chrome rebuild removes blocks (old header/footer, wa-float anchor,
    main.js tag) but leaves their blank lines behind, so every regeneration
    added a few more empty lines to every page. Collapsing the runs makes the
    pipeline idempotent: running it twice produces no further diff. Whitespace
    inside <pre> and <textarea> is preserved.
    """
    eol = "\r\n" if "\r\n" in text else "\n"
    out = []
    pos = 0
    for m in PROTECTED_RE.finditer(text):
        out.append(BLANK_RUN_RE.sub(eol + eol, text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(BLANK_RUN_RE.sub(eol + eol, text[pos:]))
    return "".join(out)


def abs_url(relpath):
    relpath = relpath.lstrip("/")
    if relpath == "index.html":
        return SITE + "/"
    if relpath.endswith(".html"):
        relpath = relpath[:-5]
    return SITE + "/" + relpath


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
            "image": SITE + "/assets/img/factory-hero.webp",
            "logo": SITE + "/assets/svg/logo.svg",
            "email": EMAIL, "telephone": PHONE,
            "address": {"@type": "PostalAddress",
                        "streetAddress": "No. 8 Huasheng Rd, Shiling",
                        "addressLocality": "Guangzhou",
                        "addressRegion": "Guangdong",
                        "addressCountry": "CN"}}
