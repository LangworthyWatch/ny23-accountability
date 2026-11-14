#!/usr/bin/env python3
"""Know NY-23: district profile from ACS 2025 1-year detailed tables (table-based summary file).

Geographies: NY-23 on 119th Congress lines (5001900US3623), New York (0400000US36), US (0100000US),
plus all 26 NY districts for rank. Derived MOEs use the Census Bureau's approximation formulas
(sums: root of summed squared MOEs; proportions: sqrt(MOEx^2 - p^2*MOEy^2)/Y, falling back to + when negative).
Usage (from this folder): python3 acs_profile.py acs
"""
import csv, math, os, sys

D = sys.argv[1]
NY23, NYS, US = "5001900US3623", "0400000US36", "0100000US"
NYCDS = [f"5001900US36{n:02d}" for n in range(1, 27)]

labels = {}
with open(os.path.join(D, "ACS20251YR_Table_Shells.txt")) as f:
    for r in csv.DictReader(f, delimiter="|"):
        labels[r["Unique ID"]] = r["Label"]

def load(t):
    out = {}
    with open(os.path.join(D, f"acsdt1y2025-{t.lower()}.dat")) as f:
        rd = csv.reader(f, delimiter="|")
        hdr = next(rd)
        for row in rd:
            if row[0] in (NY23, NYS, US) or row[0] in NYCDS:
                out[row[0]] = dict(zip(hdr, row))
    return out

cache = {}
def val(geo, uid):
    t = uid.split("_")[0]
    if t not in cache:
        cache[t] = load(t)
    r = cache[t][geo]
    e, m = r[f"{t}_E{uid.split('_')[1]}"], r[f"{t}_M{uid.split('_')[1]}"]
    return float(e), float(m) if m not in ("", "-555555555", "-222222222") else 0.0

def ssum(geo, uids):
    es, ms = zip(*(val(geo, u) for u in uids))
    return sum(es), math.sqrt(sum(m * m for m in ms))

def prop(geo, num, den):
    x, mx = ssum(geo, num) if isinstance(num, list) else val(geo, num)
    y, my = ssum(geo, den) if isinstance(den, list) else val(geo, den)
    p = x / y
    rad = mx * mx - p * p * my * my
    mp = math.sqrt(rad if rad >= 0 else mx * mx + p * p * my * my) / y
    return 100 * p, 100 * mp

def ids(t, pred):
    return [u for u, l in labels.items() if u.startswith(t + "_") and pred(u, l)]

def rng(t, a, b):
    return [f"{t}_{i:03d}" for i in range(a, b + 1)]

# age bands from B01001 (verified by label below)
U18 = rng("B01001", 3, 6) + rng("B01001", 27, 30)
O65 = rng("B01001", 20, 25) + rng("B01001", 44, 49)
for u in U18 + O65:
    assert any(k in labels[u] for k in ("Under 5", "5 to 9", "10 to 14", "15 to 17", "65 and 66", "67 to 69", "70 to 74", "75 to 79", "80 to 84", "85 years")), (u, labels[u])
UNINS = ids("B27001", lambda u, l: l.startswith("No health insurance"))
BA = ids("B15003", lambda u, l: l.split()[0] in ("Bachelor's", "Master's", "Professional", "Doctorate"))
assert len(BA) == 4, BA
MCAID = ["C27007_004", "C27007_007", "C27007_010", "C27007_014", "C27007_017", "C27007_020"]
MCARE = ["C27006_004", "C27006_007", "C27006_010", "C27006_014", "C27006_017", "C27006_020"]

METRICS = [
    ("Population", lambda g: val(g, "B01003_001"), "n"),
    ("Median age", lambda g: val(g, "B01002_001"), "y"),
    ("Age 65+ (% of pop.)", lambda g: prop(g, O65, "B01001_001"), "%"),
    ("Under 18 (% of pop.)", lambda g: prop(g, U18, "B01001_001"), "%"),
    ("White, non-Hispanic (%)", lambda g: prop(g, "B03002_003", "B03002_001"), "%"),
    ("Median household income", lambda g: val(g, "B19013_001"), "$"),
    ("Per capita income", lambda g: val(g, "B19301_001"), "$"),
    ("Below poverty (% of people)", lambda g: prop(g, "B17001_002", "B17001_001"), "%"),
    ("Households with Social Security income (%)", lambda g: prop(g, "B19055_002", "B19055_001"), "%"),
    ("Households with SSI (%)", lambda g: prop(g, "B19056_002", "B19056_001"), "%"),
    ("Households receiving SNAP (%)", lambda g: prop(g, "B22001_002", "B22001_001"), "%"),
    ("People with Medicaid/means-tested coverage (%)", lambda g: prop(g, MCAID, "C27007_001"), "%"),
    ("People with Medicare (%)", lambda g: prop(g, MCARE, "C27006_001"), "%"),
    ("Uninsured (%)", lambda g: prop(g, UNINS, "B27001_001"), "%"),
    ("Veterans (% of adults)", lambda g: prop(g, "B21001_002", "B21001_001"), "%"),
    ("Bachelor's degree or higher (% of 25+)", lambda g: prop(g, BA, "B15003_001"), "%"),
    ("Homeowners (% of households)", lambda g: prop(g, "B25003_002", "B25003_001"), "%"),
    ("Median home value", lambda g: val(g, "B25077_001"), "$"),
    ("Households with broadband of any type (%)", lambda g: prop(g, "B28002_004", "B28002_001"), "%"),
    ("Households with no internet access (%)", lambda g: prop(g, "B28002_013", "B28002_001"), "%"),
    ("Unemployment rate (civilian labor force)", lambda g: prop(g, "B23025_005", "B23025_003"), "%"),
    ("Workers who drove alone (%)", lambda g: prop(g, "B08301_003", "B08301_001"), "%"),
]

def fmt(v, kind):
    e, m = v
    if kind == "$":
        return f"${e:,.0f} ± {m:,.0f}"
    if kind == "n":
        return f"{e:,.0f} ± {m:,.0f}"
    if kind == "y":
        return f"{e:.1f} ± {m:.1f}"
    return f"{e:.1f}% ± {m:.1f}"

rows = []
print(f"{'Measure':48s} {'NY-23':>20s} {'New York':>20s} {'US':>20s}  rank/26 (1=highest)")
for name, fn, kind in METRICS:
    a, b, c = fn(NY23), fn(NYS), fn(US)
    allcd = sorted(((fn(g)[0], g) for g in NYCDS), reverse=True)
    rank = [g for _, g in allcd].index(NY23) + 1
    print(f"{name:48s} {fmt(a, kind):>20s} {fmt(b, kind):>20s} {fmt(c, kind):>20s}  {rank}")
    rows.append([name, kind, a[0], a[1], b[0], b[1], c[0], c[1], rank])

# industry shares, civilian employed 16+ (male + female lines)
print("\nIndustry (civilian employed 16+), NY-23 vs NY vs US; rank of NY-23 share among 26 NY districts")
sect = [(i, labels[f"C24030_{i:03d}"].rstrip(":")) for i in range(3, 29) if labels[f"C24030_{i:03d}"].endswith(":") or i in (6, 7, 8, 9, 13, 27, 28)]
for i, lab in sect:
    uid = [f"C24030_{i:03d}", f"C24030_{i + 27:03d}"]
    a, b, c = (prop(g, uid, "C24030_001") for g in (NY23, NYS, US))
    allcd = sorted(((prop(g, uid, "C24030_001")[0], g) for g in NYCDS), reverse=True)
    rank = [g for _, g in allcd].index(NY23) + 1
    print(f"  {lab[:60]:60s} {a[0]:5.1f} ±{a[1]:.1f}  NY {b[0]:5.1f}  US {c[0]:5.1f}  rank {rank}")
    rows.append(["IND: " + lab, "%", a[0], a[1], b[0], b[1], c[0], c[1], rank])
# a few detail lines
for i in (4, 23, 22):
    uid = [f"C24030_{i:03d}", f"C24030_{i + 27:03d}"]
    a, b, c = (prop(g, uid, "C24030_001") for g in (NY23, NYS, US))
    print(f"  detail: {labels[f'C24030_{i:03d}']:55s} {a[0]:5.1f} ±{a[1]:.1f}  NY {b[0]:5.1f}  US {c[0]:5.1f}")
    rows.append(["IND detail: " + labels[f"C24030_{i:03d}"], "%", a[0], a[1], b[0], b[1], c[0], c[1], ""])

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "acs2025_ny23_profile.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["measure", "kind", "ny23", "ny23_moe", "nys", "nys_moe", "us", "us_moe", "ny23_rank_of_26_desc"])
    w.writerows(rows)

if os.environ.get("NEIGHBORS"):
    print("\nTop/bottom neighbors for ranked claims (estimate ± MOE)")
    want = {"Median age", "Age 65+ (% of pop.)", "People with Medicare (%)", "Veterans (% of adults)", "White, non-Hispanic (%)",
            "Median home value", "Workers who drove alone (%)", "Households with Social Security income (%)", "Unemployment rate (civilian labor force)",
            "Homeowners (% of households)"}
    for name, fn, kind in METRICS:
        if name not in want: continue
        allcd = sorted(((fn(g), g) for g in NYCDS), key=lambda x: -x[0][0])
        pos = [g for _, g in allcd].index(NY23)
        sl = allcd[max(0, pos - 2): pos + 3]
        print(" ", name, "|", "; ".join(f"NY-{g[-2:]} {fmt(v, kind)}" for v, g in sl))
    def ind(g, i): return prop(g, [f"C24030_{i:03d}", f"C24030_{i + 27:03d}"], "C24030_001")
    allcd = sorted(((ind(g, 7), g) for g in NYCDS), key=lambda x: -x[0][0])
    print("  Manufacturing |", "; ".join(f"NY-{g[-2:]} {v[0]:.1f}±{v[1]:.1f}" for v, g in allcd[:4]))
