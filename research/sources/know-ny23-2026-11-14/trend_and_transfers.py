#!/usr/bin/env python3
"""Know NY-23: (1) population 2020-2025 on current (119th) lines by summing Vintage 2025 town/city estimates,
(2) county population 2010-2025, (3) BEA personal current transfer receipts as a share of personal income, 2024.
Usage (from this folder): python3 trend_and_transfers.py ."""
import csv, os, sys
D = sys.argv[1]
p = lambda f: os.path.join(D, f)

# (1) cousubs in NY-23 (119th), by land share
rel = list(csv.reader(open(os.path.join(D, "..", "redistricting-2026-11-13", "tab20_cd11920_cousub20_st36.txt"), encoding="utf-8-sig"), delimiter="|"))
i = {k: n for n, k in enumerate(rel[0])}
inside = {}
for r in rel[1:]:
    if r[i["GEOID_CD119_20"]] != "3623" or int(r[i["AREALAND_PART"]]) == 0:
        continue
    tot = int(r[i["AREALAND_COUSUB_20"]])
    inside[r[i["GEOID_COUSUB_20"]]] = (r[i["NAMELSAD_COUSUB_20"]], int(r[i["AREALAND_PART"]]) / tot if tot else 0)
pop = {}
for r in csv.DictReader(open(p("pep/sub-est2025_36.csv"), encoding="latin-1")):
    if r["SUMLEV"] == "061":
        pop["36" + r["COUNTY"] + r["COUSUB"]] = (r["NAME"], int(r["ESTIMATESBASE2020"]), int(r["POPESTIMATE2025"]))
whole, part = [], []
for g, (n, share) in inside.items():
    if g not in pop:
        print("NO PEP MATCH", g, n, share); continue
    (whole if share >= 0.995 else part).append((g, n, share) + pop[g][1:])
b0 = sum(x[3] for x in whole); b1 = sum(x[4] for x in whole)
print(f"Whole towns/cities in NY-23: {len(whole)}; 2020 base {b0:,} -> 2025 {b1:,}  ({b1 - b0:+,}, {100 * (b1 - b0) / b0:+.2f}%)")
for x in sorted(part, key=lambda x: x[0]):
    print(f"  PARTIAL {x[0]} {x[1]}: {100 * x[2]:.1f}% of land in NY-23; whole-town 2020 {x[3]:,} -> 2025 {x[4]:,} ({100 * (x[4] - x[3]) / x[3]:+.1f}%)")
# biggest gainers/losers among whole units
ch = sorted(whole, key=lambda x: x[4] - x[3])
print("  largest losses:", [(x[1], x[4] - x[3]) for x in ch[:6]])
print("  largest gains:", [(x[1], x[4] - x[3]) for x in ch[-6:]])
gains = sum(1 for x in whole if x[4] > x[3]); print(f"  units that grew: {gains} of {len(whole)}")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ny23_towns_pop_2020_2025.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["geoid", "name", "land_share_in_ny23", "base2020", "est2025"])
    for x in sorted(whole + part): w.writerow([x[0], x[1], round(x[2], 4), x[3], x[4]])

# (2) county trend
C = {"003": "Allegany", "009": "Cattaraugus", "013": "Chautauqua", "015": "Chemung", "029": "Erie",
     "063": "Niagara", "097": "Schuyler", "101": "Steuben", "107": "Tioga"}
c10 = {r["COUNTY"]: int(r["CENSUS2010POP"]) for r in csv.DictReader(open(p("pep/co-est2020-alldata_NY.csv"), encoding="latin-1")) if r["STATE"] == "36" and r["SUMLEV"] == "050"}
c25 = {r["COUNTY"]: (int(r["ESTIMATESBASE2020"]), int(r["POPESTIMATE2025"])) for r in csv.DictReader(open(p("pep/co-est2025-alldata_NY.csv"), encoding="latin-1")) if r["STATE"] == "36" and r["SUMLEV"] == "050"}
print("\nCounty population: 2010 census, 2020 base, 2025 estimate")
for k, n in C.items():
    a, (b, c) = c10[k], c25[k]
    print(f"  {n:12s} {a:>9,} {b:>9,} {c:>9,}   2010-25 {100 * (c - a) / a:+.1f}%   2020-25 {100 * (c - b) / b:+.1f}%")
st10 = sum(c10.values()); st20 = sum(v[0] for v in c25.values()); st25 = sum(v[1] for v in c25.values())
print(f"  New York     {st10:>9,} {st20:>9,} {st25:>9,}   2010-25 {100 * (st25 - st10) / st10:+.1f}%   2020-25 {100 * (st25 - st20) / st20:+.1f}%")

# (3) BEA transfers share
rows = list(csv.reader(open(p("bea/CAINC4_NY_US.csv"), encoding="latin-1")))
h = rows[0]; yi = {y: h.index(y) for y in ("2004", "2014", "2024")}
v = {}
for r in rows[1:]:
    if len(r) < len(h): continue
    fips = r[0].strip().strip('"').strip()
    if r[4] in ("10", "47"):
        v[(fips, r[4])] = {y: r[j] for y, j in yi.items()}
print("\nPersonal current transfer receipts as % of personal income (BEA CAINC4, line 47 / line 10)")
for fips, n in [("36" + k, nm) for k, nm in C.items()] + [("36000", "New York"), ("00000", "United States")]:
    out = []
    for y in ("2004", "2014", "2024"):
        try: out.append(f"{y}: {100 * float(v[(fips, '47')][y]) / float(v[(fips, '10')][y]):.1f}%")
        except Exception as e: out.append(f"{y}: n/a")
    print(f"  {n:14s}", "  ".join(out))
