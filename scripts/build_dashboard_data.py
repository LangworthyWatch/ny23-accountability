#!/usr/bin/env python3
"""Generate static/data/dashboard.json from fact-check frontmatter."""

import json
import os
import re
from datetime import datetime
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content" / "fact-checks"
OUT_FILE    = Path(__file__).parent.parent / "static" / "data" / "dashboard.json"

SKIP = {"_template", "_template-", "example-entry"}

TOPIC_MAP = {
    "economy": "Economy",
    "agriculture": "Agriculture",
    "healthcare": "Healthcare",
    "immigration": "Immigration",
    "rule of law": "Rule of Law",
    "transparency": "Transparency",
    "oversight": "Oversight",
    "campaign finance": "Campaign Finance",
    "infrastructure": "Infrastructure",
    "veterans": "Veterans",
    "energy": "Energy",
    "environment": "Environment",
    "defense": "Defense",
    "social": "Social Services",
    "local impact": "Local Impact",
    "government": "Government Operations",
    "federal": "Federal Programs",
    "labor": "Labor",
    "ethics": "Ethics",
    "tax": "Tax Policy",
    "civil": "Civil Liberties",
    "foreign": "Foreign Policy",
    "food": "Food Security",
    "constituent": "Constituent Service",
    "voting": "Voting Record",
    "legislative": "Legislative Record",
    "healthcare": "Healthcare",
}

def normalize_topic(raw):
    raw = raw.strip().strip('"')
    first = raw.split("/")[0].strip().lower()
    for key, val in TOPIC_MAP.items():
        if first.startswith(key):
            return val
    return raw.split("/")[0].strip().title()

def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

entries = []
for path in sorted(CONTENT_DIR.glob("*.md")):
    if any(skip in path.stem for skip in SKIP) or path.name == "_index.md":
        continue
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm.get("draft", "").lower() == "true":
        continue
    verdict = fm.get("verdict", "").upper().strip()
    topic   = normalize_topic(fm.get("topic", "Other"))
    date    = fm.get("date", "")[:10]
    title   = fm.get("title", path.stem).strip()
    # Build URL slug from filename
    slug = path.stem
    if not verdict:
        continue
    entries.append({
        "title":   title,
        "date":    date,
        "verdict": verdict,
        "topic":   topic,
        "url":     f"/fact-checks/{slug}/",
    })

entries.sort(key=lambda e: e["date"], reverse=True)

# Verdict counts
verdict_counts = {}
for e in entries:
    verdict_counts[e["verdict"]] = verdict_counts.get(e["verdict"], 0) + 1

# By topic
topic_counts = {}
for e in entries:
    topic_counts[e["topic"]] = topic_counts.get(e["topic"], 0) + 1

# By month (YYYY-MM)
month_counts = {}
for e in entries:
    if e["date"] and len(e["date"]) >= 7:
        m = e["date"][:7]
        month_counts[m] = month_counts.get(m, 0) + 1

# Sort months
month_counts = dict(sorted(month_counts.items()))

# Most common verdict
top_verdict = max(verdict_counts, key=verdict_counts.get) if verdict_counts else ""

out = {
    "generated":     datetime.now().strftime("%Y-%m-%d"),
    "total":         len(entries),
    "top_verdict":   top_verdict,
    "verdicts":      dict(sorted(verdict_counts.items(), key=lambda x: -x[1])),
    "by_topic":      dict(sorted(topic_counts.items(), key=lambda x: -x[1])),
    "by_month":      month_counts,
    "entries":       entries,
}

OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(f"Written {len(entries)} entries → {OUT_FILE}")
print(f"Verdicts: {verdict_counts}")
print(f"Topics:   {topic_counts}")
