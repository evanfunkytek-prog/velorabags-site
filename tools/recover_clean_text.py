# -*- coding: utf-8 -*-
"""Recover text corrupted by the 376b5c8 -> 13c18f0 mojibake passes.

Why this exists
---------------
Commit 376b5c8 re-encoded page text as GBK, so every character outside ASCII
turned into a run of CJK bytes:

    " - "    (spaced em dash)  ->  "???"   shown as  "??? "
    "12-25"  (en dash range)   ->  "12??5"

Commit 13c18f0 then replaced the leading CJK byte (plus, where present, the
"?" that had swallowed a following character) with a bare em dash.  That
"cleanup" silently:

  * dropped the space after a real em dash:  "text - more"  ->  "text -more"
  * dropped a character inside en-dash ranges: "12-25"      ->  "12-5"

Both are data loss, not style choices, and they ship malformed copy to
Google.  This tool restores the original characters by locally re-aligning
each damaged region against the last clean revision (1ced177) and rewriting
only that span.

Usage:  python tools/recover_clean_text.py [--apply]
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = "1ced177"
DASH = "\u2014"
MARKERS = ("\u9225", "\u8133", "\u63D1", "\u922B", "\u9358", "\u8DEF", "\uFFFD")
SKIP_DIRS = {".git", "research", "tools", "node_modules", "package", "dist"}
MIN_CTX = 12
ANCHOR = 24
SPAN = 70


def git_show(rev, path):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, path)], cwd=ROOT,
                       stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8-sig", "replace")


def norm(s):
    """Neutralise the Velora -> Verlora rename so contexts still line up."""
    return s.replace("Verlora", "Velora")


def align(nref, out, i, delta):
    """Ref index of the damaged character, matched on preceding context."""
    base = i + delta
    for size in (60, 44, 30, 20, MIN_CTX):
        ctx = norm(out[max(0, i - size):i])
        if len(ctx) < MIN_CTX:
            continue
        j = nref.find(ctx, max(0, base - 500), base + 500)
        if j < 0:
            j = nref.find(ctx)
        if j >= 0:
            return j + len(ctx)
    return None


def needs_repair(out, i, nref, delta):
    """True when this em dash carries a 13c18f0 corruption signature."""
    nxt = out[i + 1:i + 2]
    if nxt.isdigit() or nxt in MARKERS:
        return True
    if out[i - 1:i] == " " and nxt != " ":
        return True
    j = align(nref, out, i, delta)
    if j is None:
        return False
    if nref[j:j + 1] != out[i:i + 1]:
        return True          # the reference used a different dash family
    # clean text keeps a space (or a tag) after a spaced em dash
    return nref[j + 1:j + 2] == " " and nxt != " "


def local_repair(out, i, nref, delta):
    """Return (head_end, ref_text, ref_start) for the damaged span."""
    j = align(nref, out, i, delta)
    if j is None:
        return None
    head = norm(out[i:])
    best = None
    for t in range(0, SPAN):
        w = head[1 + t:1 + t + ANCHOR]
        if len(w) < ANCHOR or any(m in w for m in MARKERS):
            continue
        for s in range(0, SPAN):
            if nref[j + s:j + s + ANCHOR] == w:
                if best is None or t + s < best[0]:
                    best = (t + s, t, s)
                break
    if best is None:
        return None
    _, t, s = best
    # nref is brand-normalised; put the shipped spelling back
    return (i + 1 + t, nref[j:j + s].replace("Velora", "Verlora"), j)


def fix_file(path, rel):
    raw = open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    ref = git_show(REF, rel)
    if ref is None:
        return None, txt, bom, [("NOREF", "", "")]
    if "\r\n" in txt:
        ref = ref.replace("\r\n", "\n").replace("\n", "\r\n")
    nref = norm(ref)

    out = txt
    delta = 0
    log = []
    for _ in range(300):
        moved = False
        starts = [k for k, ch in enumerate(out) if ch in MARKERS]
        starts += [m.start() for m in re.finditer(DASH, out)
                   if needs_repair(out, m.start(), nref, delta)]
        for i in sorted(starts):
            if out[i] not in MARKERS and not needs_repair(out, i, nref, delta):
                continue
            hit = local_repair(out, i, nref, delta)
            if hit is None:
                log.append(("UNRESOLVED", out[max(0, i - 22):i], out[i:i + 24]))
                continue
            end, span, refj = hit
            if out[i:end] == span:
                continue
            log.append(("FIX", out[max(0, i - 22):i], span))
            delta = (refj + len(span)) - end
            out = out[:i] + span + out[end:]
            moved = True
            break
        if not moved:
            break
    return ref, out, bom, log


def html_files():
    found = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(".html"):
                found.append(os.path.relpath(os.path.join(base, name), ROOT)
                             .replace(os.sep, "/"))
    return sorted(found)


def main():
    apply = "--apply" in sys.argv
    total = 0
    unresolved = []
    for rel in html_files():
        _ref, fixed, bom, log = fix_file(os.path.join(ROOT, rel), rel)
        if not log:
            continue
        if any(k == "NOREF" for k, _a, _b in log):
            unresolved.append((rel, "no clean revision"))
            continue
        for kind, before, after in log:
            if kind == "UNRESOLVED":
                unresolved.append((rel, (before + " [--] " + after).strip()))
            else:
                total += 1
                print("  %-38s %s ==> %s" % (rel, before, after))
        if apply:
            data = fixed.encode("utf-8")
            if bom:
                data = b"\xef\xbb\xbf" + data
            open(os.path.join(ROOT, rel), "wb").write(data)
    print("\nrecovered spans: %d" % total)
    if unresolved:
        print("UNRESOLVED (%d):" % len(unresolved))
        for rel, why in unresolved:
            print("  %-38s %s" % (rel, why))
    print("mode: %s" % ("APPLIED" if apply else "dry run"))


if __name__ == "__main__":
    main()
