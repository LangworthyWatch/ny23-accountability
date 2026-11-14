#!/usr/bin/env python3
"""Know NY-23: where household income comes from, district-wide (ACS 2025 1-year aggregate income tables).
Share of aggregate household income (B19025) from earnings (B19061), Social Security (B19065), retirement income (B19069),
SSI (B19066) and public assistance (B19067). ACS counts cash income only: Medicare, Medicaid and SNAP are not in it.
MOE of a share: sqrt(MOEx^2 - p^2*MOEy^2)/Y (Census approximation). Usage: python3 acs_income_sources.py <dir with acsdt1y2025-b190xx.dat>"""
import csv, math, os, sys
D = sys.argv[1]
G = [("NY-23", "5001900US3623"), ("New York", "0400000US36"), ("US", "0100000US")]
NYCDS = [f"5001900US36{n:02d}" for n in range(1, 27)]
def load(t):
    out = {}
    for r in csv.reader(open(os.path.join(D, f"acsdt1y2025-{t}.dat")), delimiter="|"):
        if r[0] != "GEO_ID": out[r[0]] = (float(r[1]), float(r[2]))
    return out
tot = load("b19025")
def share(t, g):
    x, mx = load(t)[g]; y, my = tot[g]; p = x / y
    rad = mx * mx - p * p * my * my
    return 100 * p, 100 * math.sqrt(rad if rad >= 0 else mx * mx + p * p * my * my) / y
for lab, t in [("Earnings (wages and self-employment)", "b19061"), ("Social Security", "b19065"), ("Retirement income (pensions, IRAs)", "b19069"),
               ("Supplemental Security Income", "b19066"), ("Public assistance (cash)", "b19067")]:
    line = f"{lab:40s}" + "".join(f"  {n} {share(t, g)[0]:5.1f}% ±{share(t, g)[1]:.1f}" for n, g in G)
    rk = sorted(NYCDS, key=lambda g: -share(t, g)[0]).index("5001900US3623") + 1
    print(line, f"  rank {rk}/26")
top = sorted(NYCDS, key=lambda g: -share("b19065", g)[0])[:5]
print("Social Security share, top 5 NY districts:", "; ".join(f"NY-{g[-2:]} {share('b19065', g)[0]:.1f}±{share('b19065', g)[1]:.1f}" for g in top))
