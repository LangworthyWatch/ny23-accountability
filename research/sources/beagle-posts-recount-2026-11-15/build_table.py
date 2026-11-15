#!/usr/bin/env python3
"""Build the entry's post table from ledger.csv. Excerpts keep his spelling; emoji are dropped (disclosed in the entry).
Usage (from this folder): python3 build_table.py > table.md"""
import csv, re, datetime
rows = [r for r in csv.DictReader(open("ledger.csv", encoding="utf-8")) if "EXCLUDED" not in r["notes"]]
EMO = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍]")
FMT = {"text": "Text", "photo": "Photo", "multi-photo": "Photos", "video": "Video", "link-share": "Link",
       "share-of-other-post": "Shared post", "self-share": "Reshared his own post"}
def clean(t):
    t = EMO.sub("", t).replace("\n", " ")
    t = re.sub(r"\s*(See less|See more)\s*$", "", t.strip())
    return re.sub(r"\s{2,}", " ", t).strip()
def excerpt(t, n=190):
    t = clean(t)
    if len(t) <= n: return t
    cut = t[:n]
    m = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
    return (cut[:m + 1] if m > 80 else cut.rsplit(" ", 1)[0]) + " …"
SPECIAL = {
    "09": lambda r: f"\"{excerpt(r['text'])}\" Shared Judge Jeanine Pirro's May 6 post about Big Dog Ranch Rescue.",
    "26": lambda r: f"\"{excerpt(r['text'], 150)}\" (The post does not name the speaker; the video caption at that point reads \"MARK POCAN.\")",
    "28": lambda r: "Reshared his June 4 WMTV video post, adding three \"100\" emoji.",
    "30": lambda r: f"\"{excerpt(r['text'], 200)}\" Shared Secretary Kennedy's June 15 post, which begins \"Today USDA Secretary Brooke Rollins and I secured a major win for animal welfare.\"",
}
print("| # | Date | What he posted (excerpt) | Format | Capture |")
print("|---|---|---|---|---|")
for i, r in enumerate(rows, 1):
    d = datetime.date.fromisoformat(r["date_iso"])
    ds = d.strftime("%B %-d") + (" (approx.; shown as \"5 days ago\" on Nov. 15)" if r["date_relative"].lower().startswith("y") else "")
    body = SPECIAL[r["n"]](r) if r["n"] in SPECIAL else f"\"{excerpt(r['text'])}\""
    pi = r["private_individuals"].lower().startswith("yes")
    cap = "Not published (shows members of the public)" if pi else f"[View](/images/fact-checks/beagle-posts-2026-11-15/{r['n']}-{r['date_iso']}.jpg)"
    print(f"| {i} | {ds} | {body} | {FMT.get(r['format'], r['format'])} | {cap} |")
