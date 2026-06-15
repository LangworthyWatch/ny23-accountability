#!/usr/bin/env python3
"""
prepublish_lint.py — scan a fact-check draft for provisional language that
reads as finished.

The danger isn't a wrong number; it's a *provisional* claim that looks
identical to a verified one once it's in prose. "Confirmed by elimination,"
"per the report's state-by-state data," "[link to be added]" — these are
honest placeholders that quietly become load-bearing at publish. This linter
produces a confirm-or-cut punch list so nothing provisional ships by accident.

Usage:  python prepublish_lint.py <path-to-entry.md>
Exit:   0 = clean, 1 = findings, 2 = error.

Deterministic and non-blocking — it flags, the human decides. Pairs with
/prepublish-lint (the command) and runs at the tail of /claim-audit.
"""
import re
import sys

# (regex, severity, why / what-to-do).  Severity: BLOCK > HEDGE > SOFT.
PATTERNS = [
    (r"by elimination", "BLOCK",
     "vote/fact asserted indirectly — read it verbatim (verify_fact.py rollcall)"),
    (r"per the report'?s? (?:state-by-state |)data", "BLOCK",
     "figure deferred to unspecified data — cite the exact table/figure"),
    (r"\[link to be added[^\]]*\]|\[to be added[^\]]*\]|link to be added", "BLOCK",
     "placeholder link — secure the URL or cut the sentence"),
    (r"\[citation needed\]|\[source\?\]|\[cite\]", "BLOCK",
     "missing citation marker"),
    (r"\b(?:TODO|TBD|FIXME|XXX)\b", "BLOCK",
     "unfinished-work marker left in text"),
    (r"\bplaceholder\b", "BLOCK", "literal 'placeholder' left in text"),
    (r"almost certainly|all but certain|virtually certain", "HEDGE",
     "near-certain inference stated softly — confirm to fact or cut"),
    (r"\bappears to\b|\bseems to\b|\bsuggests that\b|\bpresumably\b", "HEDGE",
     "inference language — verify the underlying fact"),
    (r"reportedly|allegedly", "HEDGE",
     "second-hand framing — trace to the primary source"),
    (r"~\s*\$?\d|\broughly\b|\bapproximately\b|\babout \$?\d|\bestimated\b", "SOFT",
     "approximation — fine if intended, confirm it isn't a stand-in for a known exact figure"),
]

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def split_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[: end + 4], text[end + 4:]
    return "", text


def main():
    if len(sys.argv) != 2:
        print("usage: prepublish_lint.py <path-to-entry.md>", file=sys.stderr)
        return 2
    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    fm, body = split_frontmatter(raw)
    # blank out HTML comments so the pre-publish checklist's own words
    # (which legitimately quote these patterns) don't self-trigger
    body_nocomments = COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    lines = raw.splitlines()
    nocomment_lines = (fm + body_nocomments).splitlines()

    findings = []  # (severity, lineno, snippet, why)
    for i, line in enumerate(nocomment_lines, 1):
        for rx, sev, why in PATTERNS:
            for mm in re.finditer(rx, line, re.IGNORECASE):
                snippet = line.strip()[:100]
                findings.append((sev, i, mm.group(0), snippet, why))

    # frontmatter publish-gate checks
    is_published = re.search(r"^draft:\s*false", fm, re.MULTILINE)
    if is_published:
        if re.search(r'^archived_url:\s*""\s*$', fm, re.MULTILINE):
            findings.append(("HEDGE", 0, "archived_url: \"\"", "(frontmatter)",
                             "draft:false but archived_url empty — archive sources first"))
        if re.search(r'source_url:\s*"https://www\.facebook\.com/RepLangworthy"', fm):
            findings.append(("HEDGE", 0, "generic source_url", "(frontmatter)",
                             "draft:false but source_url is the generic FB page — use the post permalink"))
        if re.search(r"Pre-publish checklist", body):
            findings.append(("SOFT", 0, "pre-publish checklist comment", "(html comment)",
                             "draft:false but the pre-publish checklist comment is still present"))

    if not findings:
        print(f"✓ prepublish_lint: clean — {path}")
        return 0

    order = {"BLOCK": 0, "HEDGE": 1, "SOFT": 2}
    findings.sort(key=lambda x: (order[x[0]], x[1]))
    label = {"BLOCK": "BLOCK (confirm-or-cut before publish)",
             "HEDGE": "HEDGE (verify the underlying fact)",
             "SOFT": "SOFT  (approximation — intended?)"}
    cur = None
    n = len(findings)
    for sev, ln, hit, snippet, why in findings:
        if sev != cur:
            print(f"\n== {label[sev]} ==")
            cur = sev
        loc = f"L{ln}" if ln else "frontmatter"
        print(f"  {loc:>6}  «{hit}»  — {why}")
        if snippet and snippet != hit:
            print(f"          {snippet}")
    print(f"\n{n} finding(s). Non-blocking — confirm or cut each before flipping draft:false.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
