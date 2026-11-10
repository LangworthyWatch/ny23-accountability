#!/usr/bin/env python3
"""
check_built_links.py: find internal links in the BUILT site (public/) that point
at pages that don't exist.

Why the built site and not the markdown: drafts are never built, so a published
entry that links to a draft shows up here as a missing target. That is exactly
the failure that produced three live 404s found in the Nov 10, 2026 audit. Paths
listed in public/_redirects count as resolved.

Usage:  python3 scripts/check_built_links.py [public_dir]
Exit:   0 = no broken links, 1 = broken links found, 2 = error.
Run after `hugo --gc --minify`, before deploy.
"""
import os
import re
import sys
from collections import defaultdict
from urllib.parse import unquote

HREF_RE = re.compile(r'''(?:href|src)=["']?(/[^"'\s>#?]*)''')
SKIP_PREFIXES = ("/pagefind/", "//")


def load_redirects(public):
    sources = set()
    path = os.path.join(public, "_redirects")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8", errors="ignore"):
            parts = line.split()
            if parts and not parts[0].startswith("#"):
                sources.add(parts[0].rstrip("/") or "/")
    return sources


def resolves(public, url, redirects):
    u = unquote(url)
    if (u.rstrip("/") or "/") in redirects:
        return True
    target = os.path.join(public, u.lstrip("/"))
    if u.endswith("/"):
        return os.path.exists(os.path.join(target, "index.html"))
    return (os.path.exists(target)
            or os.path.exists(os.path.join(target, "index.html"))
            or os.path.exists(target + ".html"))


def main():
    public = sys.argv[1] if len(sys.argv) > 1 else "public"
    if not os.path.isdir(public):
        print(f"ERROR: {public}/ not found; build the site first", file=sys.stderr)
        return 2
    redirects = load_redirects(public)
    broken = defaultdict(set)
    pages = 0
    for root, _, files in os.walk(public):
        if "/pagefind" in root:
            continue
        for name in files:
            if not name.endswith(".html"):
                continue
            pages += 1
            src = os.path.join(root, name)
            html = open(src, encoding="utf-8", errors="ignore").read()
            for url in set(HREF_RE.findall(html)):
                if url.startswith(SKIP_PREFIXES) or "," in url:  # "," = regex flags in inline JS, not a path
                    continue
                if not resolves(public, url, redirects):
                    broken[url].add("/" + os.path.relpath(src, public).replace("index.html", ""))
    if not broken:
        print(f"check_built_links: clean ({pages} pages scanned)")
        return 0
    print(f"check_built_links: {len(broken)} broken internal target(s) across {pages} pages")
    for url in sorted(broken):
        srcs = sorted(broken[url])
        print(f"  {url}")
        for s in srcs[:5]:
            print(f"      linked from {s}")
        if len(srcs) > 5:
            print(f"      ... and {len(srcs) - 5} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
