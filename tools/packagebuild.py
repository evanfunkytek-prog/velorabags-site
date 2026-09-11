# -*- coding: utf-8 -*-
"""Build the deployable package folder and zip it."""
import os, re, shutil, zipfile
from common import rp, read, write, pages, SKIP_DIRS, SITE, BRAND, EMAIL, PHONE

PKG = rp("package")
ZIP = rp("velorabags-website-%s.zip" % "2026-09-11")
REF_RE = re.compile(r'(?:href|src)="((?:\.\./)*assets/[^"?#]+)', re.I)
CSS_REF_RE = re.compile(r'url\(["\']?((?:\.\./)*assets/[^"\')]+)')


def used_assets():
    used = set()
    for relpath in pages():
        text = read(rp(*relpath.split("/")))
        for m in REF_RE.findall(text):
            used.add(os.path.normpath(m).replace(os.sep, "/"))
        for m in CSS_REF_RE.findall(text):
            used.add(os.path.normpath(m).replace(os.sep, "/"))
    css = read(rp("assets", "css", "style.css"))
    for m in CSS_REF_RE.findall(css):
        used.add(os.path.normpath(m).replace(os.sep, "/"))
    return used


def build_package():
    if os.path.isdir(PKG):
        shutil.rmtree(PKG)
    os.makedirs(PKG)
    # html pages
    for relpath in pages():
        dst = os.path.join(PKG, *relpath.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(rp(*relpath.split("/")), dst)
    for name in ("robots.txt", "sitemap.xml"):
        shutil.copy2(rp(name), os.path.join(PKG, name))
    # only referenced assets
    used = used_assets()
    kept = 0
    for asset in sorted(used):
        src = rp(*asset.split("/"))
        if not os.path.isfile(src):
            continue
        dst = os.path.join(PKG, *asset.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        kept += 1
    return kept, len(used)


def zip_package():
    if os.path.exists(ZIP):
        os.remove(ZIP)
    count = 0
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for base, dirs, files in os.walk(PKG):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in sorted(files):
                full = os.path.join(base, name)
                arc = os.path.relpath(full, PKG).replace(os.sep, "/")
                zf.write(full, arc)
                count += 1
    return count, os.path.getsize(ZIP)
