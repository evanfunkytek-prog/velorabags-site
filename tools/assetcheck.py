# -*- coding: utf-8 -*-
"""Asset hygiene check for the Verlora Bags site.

Usage:  python tools/assetcheck.py

Fails (exit 1) when a page points at an image that is not on disk.
Warns about dead weight (images nothing references) and oversize files,
because those two things are what made the repo heavy before.
"""
import os
import re
import sys

from common import rp, SKIP_DIRS

TEXT_EXT = {".html", ".htm", ".css", ".js", ".json", ".xml", ".txt", ".md",
            ".svg", ".yml", ".yaml"}
RASTER_EXT = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif"}
REF_RE = re.compile(r"assets[\\/]([A-Za-z0-9_\-./]+\.(?:jpg|jpeg|png|webp|avif|gif|svg))", re.I)
MAX_FILE_KB = 300
MAX_FOLDER_MB = 12


def _walk():
    for base, dirs, files in os.walk(rp()):
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS and not d.startswith(".")
                   and not os.path.isdir(os.path.join(base, d, ".git"))]
        for name in files:
            yield os.path.join(base, name)


def scan():
    refs = {}
    for path in _walk():
        if os.path.splitext(path)[1].lower() not in TEXT_EXT:
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue
        for hit in REF_RE.findall(text):
            refs.setdefault(hit.replace("\\", "/"), set()).add(
                os.path.relpath(path, rp()).replace(os.sep, "/"))

    missing = sorted(r for r in refs if not os.path.isfile(rp("assets", *r.split("/"))))
    orphans, oversize, total, count = [], [], 0, 0
    for path in _walk():
        ext = os.path.splitext(path)[1].lower()
        if ext not in RASTER_EXT:
            continue
        rel = os.path.relpath(path, rp("assets")).replace(os.sep, "/")
        size = os.path.getsize(path)
        total += size
        count += 1
        if rel.lower() not in refs:
            orphans.append((rel, size))
        elif size > MAX_FILE_KB * 1024:
            oversize.append((rel, size))

    return {"refs": refs, "missing": missing, "orphans": sorted(orphans, key=lambda x: -x[1]),
            "oversize": sorted(oversize, key=lambda x: -x[1]),
            "total": total, "count": count}


def main():
    r = scan()
    print("asset check: %d image references, %d image files, %.1f MB"
          % (len(r["refs"]), r["count"], r["total"] / 1048576))

    for rel in r["missing"]:
        who = ", ".join(sorted(r["refs"][rel])[:4])
        print("  ERROR  missing file  assets/%s   (referenced by %s)" % (rel, who))

    for rel, size in r["orphans"]:
        print("  WARN   unreferenced  %-58s %6.0f KB  nothing on the site uses it"
              % ("assets/" + rel, size / 1024))

    for rel, size in r["oversize"]:
        print("  WARN   oversize      %-58s %6.0f KB  over the %d KB budget"
              % ("assets/" + rel, size / 1024, MAX_FILE_KB))

    if r["total"] > MAX_FOLDER_MB * 1048576:
        print("  WARN   total         assets/ folder is %.1f MB (budget %d MB)"
              % (r["total"] / 1048576, MAX_FOLDER_MB))

    if not r["missing"] and not r["orphans"] and not r["oversize"]:
        print("  OK     no broken references, no dead weight, all files within budget")
    return 1 if r["missing"] else 0


if __name__ == "__main__":
    sys.exit(main())
