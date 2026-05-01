#!/usr/bin/env python3
"""
Parse local FEC bulk files → static/data/campaign_finance.json.

Pulls individual + earmarked + PAC contributions to Langworthy's committee
(C00817932) across the 2022, 2024, and 2026 cycles.
"""

import json, re
from collections import defaultdict
from pathlib import Path

COMMITTEE_ID = "C00817932"
FEC_DIR      = Path.home() / "data/public-ledger/federal/fec"
OUT_FILE     = Path(__file__).parent.parent / "static/data/campaign_finance.json"

# ── Industry keyword mapping (employer/occupation → category) ─────────────────
INDUSTRY_MAP = [
    # Named companies first (specific wins over generic)
    (["blackstone", "carlyle", "kkr", "apollo", "ares", "brookfield", "cerberus",
      "blackrock", "vanguard", "fidelity", "merrill", "goldman", "morgan stanley",
      "jpmorgan", "citigroup", "wells fargo", "pimco", "citadel", "renaissance",
      "dune capital", "shl investment", "morningside", "bear stearns"], "Finance / Investment"),
    (["corning inc", "corning glass", "crystal window", "st. pauly", "st pauly",
      "manufactur", "industrial", "equipment", "factory", "textile", "apparel",
      "window", "door systems", "lumber", "hardware", "furniture", "haworth",
      "wegmans"], "Manufacturing / Industry"),
    (["lippes", "harter secrest", "woods oviatt", "mayer brown", "davis polk",
      "skadden", "sullivan", "kirkland", "wilmer", "sidley", "reed smith",
      "attorney", "lawyer", "law firm", "law office", "legal", "counsel", "llp", "pllc"], "Law / Legal Services"),
    (["big dog strategies", "premier network", "the premier", "strategy group",
      "republican", "gop", "pac", "political", "campaign", "committee",
      "lobbying", "government affairs", "public affairs", "advocacy"], "Political / PAC"),
    (["nycbs", "roswell park", "kaleida", "buffalo general", "catholic health",
      "physician", "doctor", "medical", "health", "hospital", "clinic",
      "dental", "dentist", "optom", "ophth", "pharma", "biotech",
      "atwal eye", "eye care", "cancer", "blood specialist", "veterinar"], "Healthcare / Pharma"),
    (["torrey farms", "farm", "agriculture", "dairy", "crop", "livestock",
      "agri", "grain", "vineyard", "winery", "maple", "greenhouse"], "Agriculture"),
    (["realtor", "real estate", "realty", "property", "developer",
      "construction", "builder", "gravel", "concrete", "excavat",
      "gernatt", "paraclete", "pinto"], "Real Estate / Construction"),
    (["retired", "self employed", "self-employed", "homemaker", "not employed",
      "none", "n/a"], "Retirees / Self-Employed"),
    (["bank", "financial", "finance", "investment", "capital", "securities",
      "asset management", "hedge fund", "private equity", "venture capital",
      "wealth management", "trust", "advisor", "broker", "trading"], "Finance / Investment"),
    (["insurance", "mutual of omaha", "new york life", "northwestern mutual",
      "aig", "allstate", "state farm", "underwr"], "Insurance"),
    (["oil", "gas", "energy", "pipeline", "refin", "coal", "mining",
      "electric", "utility", "power", "petroleum", "natural gas"], "Energy / Natural Resources"),
    (["tech", "software", "computer", "data", "digital", "internet",
      "cloud", "crypto", "blockchain", "it ", "saas", "ai ", "silicon",
      "study logic", "dba "], "Technology"),
    (["retail", "wholesale", "distribution", "supply", "try-it distribut",
      "beverage", "liquor", "grocery"], "Retail / Distribution"),
    (["hotel", "restaurant", "food service", "hospitality", "tourism",
      "catering", "tavern", "brewery", "distill"], "Hospitality / Food Service"),
    (["transport", "trucking", "logistics", "freight", "auto", "automotive",
      "dealership", "railroad", "airline"], "Transportation"),
    (["media", "publishing", "broadcast", "television", "communications",
      "telecom", "cable", "wireless", "phone"], "Media / Communications"),
    (["education", "university", "college", "school", "professor", "teacher",
      "academic"], "Education"),
    (["military", "veteran", "defense", "lockheed", "raytheon", "boeing",
      "northrop", "general dynamics", "bae systems"], "Defense"),
    (["nonprofit", "foundation", "charity", "religious", "church",
      "diocese", "ministry"], "Nonprofit / Religious"),
    (["government", "federal", "state", "county", "municipal", "public sector",
      "city of", "town of"], "Government / Public Sector"),
    (["consulting", "consultant", "management consulting", "strategy", "advisory",
      "mckinsey", "bain", "deloitte", "accenture", "pwc", "kpmg", "ey "], "Consulting"),
]

def classify(employer, occupation):
    text = f"{employer} {occupation}".lower()
    for keywords, category in INDUSTRY_MAP:
        if any(k in text for k in keywords):
            return category
    return "Other / Unclassified"

def parse_contributions(filepath, cycles):
    """Parse a pipe-delimited FEC indiv or oth file for our committee."""
    results = []
    if not filepath.exists():
        return results
    with open(filepath, encoding="latin-1", errors="replace") as f:
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) < 15:
                continue
            # Direct contribution (field 0) OR earmarked (field 15)
            if parts[0] == COMMITTEE_ID or (len(parts) > 15 and parts[15] == COMMITTEE_ID):
                try:
                    amt = float(parts[14]) if parts[14] else 0
                    date = parts[13]  # MMDDYYYY
                    year = int(date[-4:]) if len(date) == 8 else 0
                    employer   = parts[11].strip() if len(parts) > 11 else ""
                    occupation = parts[12].strip() if len(parts) > 12 else ""
                    name       = parts[7].strip()  if len(parts) > 7  else ""
                    state      = parts[10].strip() if len(parts) > 10 else ""
                    results.append({
                        "amt":        amt,
                        "year":       year,
                        "employer":   employer,
                        "occupation": occupation,
                        "name":       name,
                        "state":      state,
                        "cycle":      cycles,
                    })
                except (ValueError, IndexError):
                    continue
    return results

# ── Load all cycles ───────────────────────────────────────────────────────────
all_contribs = []
for fname, cycle in [
    ("indiv22.txt", 2022), ("oth22.txt", 2022),
    ("indiv24.txt", 2024), ("oth24.txt", 2024),
    ("indiv26.txt", 2026), ("oth26.txt", 2026),
]:
    path = FEC_DIR / fname
    c = parse_contributions(path, cycle)
    print(f"  {fname}: {len(c)} contributions")
    all_contribs.extend(c)

# ── Aggregate by industry ─────────────────────────────────────────────────────
industry_totals  = defaultdict(lambda: {"total": 0, "count": 0})
cycle_totals     = defaultdict(lambda: {"total": 0, "count": 0, "individual": 0, "pac": 0})
state_totals     = defaultdict(float)
top_employers    = defaultdict(lambda: {"total": 0, "count": 0})

for c in all_contribs:
    amt   = c["amt"]
    cycle = c["cycle"]
    industry = classify(c["employer"], c["occupation"])
    industry_totals[industry]["total"] += amt
    industry_totals[industry]["count"] += 1
    cycle_totals[cycle]["total"] += amt
    cycle_totals[cycle]["count"] += 1
    if c["state"]:
        state_totals[c["state"]] += amt
    if c["employer"] and c["employer"].upper() not in ("RETIRED", "N/A", "NONE", "", "SELF-EMPLOYED", "NOT EMPLOYED"):
        key = c["employer"].title()
        top_employers[key]["total"] += amt
        top_employers[key]["count"] += 1

# Sort
industry_sorted = dict(sorted(industry_totals.items(), key=lambda x: -x[1]["total"]))
top_emp_sorted  = dict(list(sorted(top_employers.items(), key=lambda x: -x[1]["total"]))[:20])
state_sorted    = dict(sorted(state_totals.items(), key=lambda x: -x[1])[:15])
cycle_sorted    = {str(k): v for k, v in sorted(cycle_totals.items())}

out = {
    "generated":   __import__("datetime").date.today().isoformat(),
    "committee_id": COMMITTEE_ID,
    "total_raised": sum(c["amt"] for c in all_contribs),
    "total_donors": len(all_contribs),
    "by_industry":  {k: {"total": round(v["total"]), "count": v["count"]}
                     for k, v in industry_sorted.items()},
    "by_cycle":     {k: {"total": round(v["total"]), "count": v["count"]}
                     for k, v in cycle_sorted.items()},
    "by_state":     {k: round(v) for k, v in state_sorted.items()},
    "top_employers": {k: {"total": round(v["total"]), "count": v["count"]}
                      for k, v in top_emp_sorted.items()},
}

OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(json.dumps(out, indent=2))
print(f"\nWritten → {OUT_FILE}")
print(f"Total raised (itemized): ${out['total_raised']:,.0f} across {out['total_donors']} records")
print(f"Top industry: {list(out['by_industry'].keys())[0] if out['by_industry'] else 'n/a'}")
