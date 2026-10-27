#!/usr/bin/env python3
"""Fill the Content-Security-Policy inline-script hashes into public/_headers after a Hugo build.

Why: the site is static (Cloudflare Pages, no server), so a strict CSP cannot use nonces. Inline
scripts (gtag init, nav toggle, the search/tracker/dashboard/fact-checks-index page scripts) are
allowed by SHA-256 hash instead. Hashes change whenever a template's inline script changes, so they
are computed from the built output on every deploy rather than maintained by hand.

Run after `hugo` and `pagefind`, before `wrangler pages deploy`:
    python3 scripts/csp_headers.py

Reads public/_headers (copied by Hugo from static/_headers), replaces the token
{{INLINE_SCRIPT_HASHES}} with the hashes of every inline <script> found under public/ except
public/graphics/ (standalone Plotly/vis exports, which get their own looser policy in _headers),
and writes public/_headers back. Exits non-zero if the token is missing or no HTML was found.
"""
import base64, glob, hashlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
HEADERS = os.path.join(PUBLIC, "_headers")
TOKEN = "{{INLINE_SCRIPT_HASHES}}"
INLINE = re.compile(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", re.S)

def main():
    if not os.path.exists(HEADERS):
        sys.exit("csp_headers: public/_headers not found (run hugo first)")
    text = open(HEADERS, encoding="utf-8").read()
    if TOKEN not in text:
        sys.exit("csp_headers: token %s not present in public/_headers" % TOKEN)
    hashes, pages = {}, 0
    for f in glob.glob(os.path.join(PUBLIC, "**", "*.html"), recursive=True):
        if os.path.relpath(f, PUBLIC).startswith("graphics" + os.sep):
            continue
        pages += 1
        html = open(f, encoding="utf-8", errors="ignore").read()
        for m in INLINE.finditer(html):
            body = m.group(1)
            if not body.strip():
                continue
            h = "sha256-" + base64.b64encode(hashlib.sha256(body.encode("utf-8")).digest()).decode()
            hashes.setdefault(h, os.path.relpath(f, PUBLIC))
    if pages == 0:
        sys.exit("csp_headers: no HTML pages found under public/")
    joined = " ".join("'%s'" % h for h in sorted(hashes) if ("'%s'" % h) not in text)
    out = text.replace(TOKEN, joined)
    out = re.sub(r"[ ]{2,}", " ", out).replace(" ;", ";")
    open(HEADERS, "w", encoding="utf-8").write(out)
    print("csp_headers: %d inline script hash(es) from %d pages written to public/_headers" % (len(hashes), pages))
    for h, where in sorted(hashes.items(), key=lambda kv: kv[1]):
        print("  ", h, "<-", where)

if __name__ == "__main__":
    main()
