#!/usr/bin/env python3
"""E&C comparison from the same govinfo BILLSTATUS bulk snapshot.
Usage: python3 -I compare_ec.py <bulk_dir>  (scope: H.R. bills only)"""
import glob, os, sys, collections
import xml.etree.ElementTree as ET
bulk = sys.argv[1]
rows = []
for f in glob.glob(os.path.join(bulk, "x-hr", "*.xml")):
    b = ET.parse(f).getroot().find("bill")
    ec = [c for c in b.findall("committees/item") if c.findtext("systemCode") == "hsif00"]
    if not ec:
        continue
    acts = [(a.findtext("name") or "").lower() for a in ec[0].findall("activities/item")]
    codes = {a.findtext("actionCode") for a in b.findall("actions/item")}
    rows.append(dict(spon=b.findtext("sponsors/item/bioguideId"), name=b.findtext("sponsors/item/fullName"),
                     party=b.findtext("sponsors/item/party"),
                     markup=any(x.startswith("markup") for x in acts), reported=any(x.startswith("reported") for x in acts),
                     passedH="8000" in codes, law="36000" in codes))
def t(rs, label):
    n = len(rs)
    m = sum(r["markup"] for r in rs); rp = sum(r["reported"] for r in rs); p = sum(r["passedH"] for r in rs); l = sum(r["law"] for r in rs)
    print(f"{label}: n={n}  EC full-cmte markup={m} ({m/n:.1%})  EC reported={rp} ({rp/n:.1%})  passed House={p} ({p/n:.1%})  enacted={l}")
t(rows, "All E&C-referred H.R. bills")
t([r for r in rows if r["party"] == "R"], "R-sponsored E&C-referred H.R.")
t([r for r in rows if r["party"] == "D"], "D-sponsored E&C-referred H.R.")
t([r for r in rows if r["spon"] == "L000600"], "Langworthy-sponsored E&C-referred H.R.")
by = collections.defaultdict(lambda: [0, 0, 0, ""])
for r in rows:
    by[r["spon"]][0] += 1; by[r["spon"]][1] += r["markup"]; by[r["spon"]][2] += r["reported"]; by[r["spon"]][3] = r["name"]
print("\nSponsors ranked by # E&C-referred H.R. bills marked up by full E&C (top 40); n_sponsors=", len(by))
rank = sorted(by.items(), key=lambda kv: (-kv[1][1], -kv[1][2]))
for i, (k, v) in enumerate(rank[:40], 1):
    print(f"{i:3d}. {v[3]}  sponsored={v[0]} markedup={v[1]} reported={v[2]}")
pos = [i for i, (k, v) in enumerate(rank, 1) if k == "L000600"]
higher = sum(1 for k, v in by.items() if v[1] > by["L000600"][1])
print(f"\nLangworthy: {by['L000600']}; sponsors with strictly more full-cmte-markup bills: {higher}")
