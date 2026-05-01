#!/usr/bin/env python3
"""
Fetch Langworthy's voting record from GovTrack → static/data/votes.json.

GovTrack is free and requires no API key.
Uses option.winner as party-line proxy (Republicans are majority in
both the 118th and 119th Congresses Langworthy has served).
"""

import json, urllib.request, time
from collections import defaultdict
from pathlib import Path
from datetime import datetime

PERSON_ID = 456927   # GovTrack person ID for Nicholas Langworthy
OUT_FILE  = Path(__file__).parent.parent / "static/data/votes.json"

CATEGORY_LABELS = {
    "procedural":  "Procedural",
    "passage":     "Passage",
    "passage-suspension": "Passage (Suspension)",
    "amendment":   "Amendment",
    "nomination":  "Nomination",
    "cloture":     "Cloture",
    "veto-override": "Veto Override",
    "other":       "Other",
    "quorum":      "Quorum",
    "leadership":  "Leadership",
    "recommit":    "Recommit",
}

# Known key votes from our fact-checks — hard-code for the notable section
KEY_VOTES = [
    {"date": "2025-07-03", "label": "One Big Beautiful Bill (SNAP cut $186.7B)", "pos": "Yea",  "party_line": True},
    {"date": "2026-04-30", "label": "FISA Sec. 702 warrantless extension (S.4465)", "pos": "Yea",  "party_line": True},
    {"date": "2026-04-30", "label": "Farm Bill H.R. 7567 (House passage)", "pos": "Yea",  "party_line": True},
    {"date": "2026-01-22", "label": "Massie amendment: defund drunk-driving detection", "pos": "Yea",  "party_line": False},
    {"date": "2024-04-12", "label": "FISA warrant requirement amendment (Biggs, 2024)", "pos": "Yea",  "party_line": False},
    {"date": "2024-04-12", "label": "FISA reauthorization RISAA (2024)", "pos": "Nay",   "party_line": False},
]

def fetch_page(offset):
    url = f"https://www.govtrack.us/api/v2/vote_voter?person={PERSON_ID}&limit=300&offset={offset}"
    req = urllib.request.Request(url, headers={"User-Agent": "LangworthyWatch/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

print("Fetching votes from GovTrack...")
all_records = []
offset = 0
total_count = None

while True:
    try:
        data = fetch_page(offset)
    except Exception as e:
        print(f"  Error at offset {offset}: {e}")
        break

    if total_count is None:
        total_count = data["meta"]["total_count"]
        print(f"  Total votes: {total_count}")

    records = data.get("objects", [])
    if not records:
        break

    all_records.extend(records)
    print(f"  Fetched {len(all_records)} / {total_count}")

    if len(all_records) >= total_count:
        break
    offset += 300
    time.sleep(0.3)   # be polite

# ── Aggregate ─────────────────────────────────────────────────────────────────
total      = len(all_records)
missed     = 0
with_winner= 0
by_category= defaultdict(lambda: {"yea": 0, "nay": 0, "missed": 0, "total": 0})
by_month   = defaultdict(int)
by_year    = defaultdict(lambda: {"cast": 0, "missed": 0, "with_winner": 0})

MISSED_KEYS = {"P", "0", "Absent", "Not Voting", ""}

for rec in all_records:
    opt  = rec.get("option", {})
    key  = opt.get("key", "")
    win  = opt.get("winner", False)
    date = rec.get("created", "")[:10]
    year = date[:4]

    vote_obj  = rec.get("vote", {})
    category  = vote_obj.get("category", "other") or "other"
    cat_label = CATEGORY_LABELS.get(category, category.title())

    by_category[cat_label]["total"] += 1

    if key in ("P", "0") or "not" in str(opt.get("value","")).lower() or key == "":
        missed += 1
        by_category[cat_label]["missed"] += 1
        by_year[year]["missed"] += 1
        continue

    # Voted
    by_year[year]["cast"] += 1
    if date[:7]:
        by_month[date[:7]] += 1

    if key == "+":
        by_category[cat_label]["yea"] += 1
    elif key == "-":
        by_category[cat_label]["nay"] += 1

    if win:
        with_winner += 1
        by_year[year]["with_winner"] += 1

cast        = total - missed
winner_pct  = round(with_winner / cast * 100, 1) if cast > 0 else 0
miss_pct    = round(missed / total * 100, 1) if total > 0 else 0

# ── Year-over-year rates ──────────────────────────────────────────────────────
yoy = {}
for yr, v in sorted(by_year.items()):
    c = v["cast"]
    yoy[yr] = {
        "cast": c,
        "missed": v["missed"],
        "miss_pct": round(v["missed"] / (c + v["missed"]) * 100, 1) if (c + v["missed"]) > 0 else 0,
        "with_winner_pct": round(v["with_winner"] / c * 100, 1) if c > 0 else 0,
    }

result = {
    "generated":       datetime.today().isoformat()[:10],
    "source":          "GovTrack.us (free, no key required)",
    "member_id":       "L000600",
    "govtrack_id":     PERSON_ID,
    "total_votes":     total,
    "votes_cast":      cast,
    "missed":          missed,
    "miss_pct":        miss_pct,
    "with_winner_pct": winner_pct,
    "by_category":     {k: dict(v) for k, v in sorted(by_category.items(), key=lambda x: -x[1]["total"])},
    "by_month":        dict(sorted(by_month.items())),
    "by_year":         yoy,
    "key_votes":       KEY_VOTES,
    "note": (
        "with_winner_pct = % of votes cast where Langworthy voted with the winning side. "
        "Since Republicans hold the House majority in both congresses he has served, "
        "this closely approximates party-line voting."
    ),
}

OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(json.dumps(result, indent=2))
print(f"\nWritten → {OUT_FILE}")
print(f"Total: {total} | Cast: {cast} | Missed: {miss_pct}% | With majority: {winner_pct}%")
