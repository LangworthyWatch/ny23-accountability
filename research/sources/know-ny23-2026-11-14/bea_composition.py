#!/usr/bin/env python3
"""Know NY-23: BEA CAINC35 (2022) composition of transfer receipts for the five whole counties, NY and US,
plus CAINC4 transfer share for the five combined. Usage (from this folder): python3 bea_composition.py"""
import csv
W = ["36003", "36009", "36013", "36015", "36107"]
def load(f, year):
    rows = list(csv.reader(open(f, encoding="latin-1"))); h = rows[0]; j = h.index(year); v = {}
    for r in rows[1:]:
        if len(r) < len(h): continue
        try: v[(r[0].strip().strip('"').strip(), r[4])] = float(r[j])
        except ValueError: pass
    return v
v = load("bea/CAINC35_NY_US.csv", "2022")
for L, n in [("2000", "From governments"), ("2110", "Social Security"), ("2220", "Medicaid and other public medical care"), ("2210", "Medicare"),
             ("2300", "Income maintenance"), ("2330", "  of which SNAP"), ("2500", "Veterans' benefits")]:
    w = sum(v[(f, L)] for f in W) / sum(v[(f, "1000")] for f in W)
    print(f"{n:42s} five whole {100*w:5.1f}%  NY {100*v[('36000', L)]/v[('36000', '1000')]:5.1f}%  US {100*v[('00000', L)]/v[('00000', '1000')]:5.1f}%")
for y in ("2004", "2014", "2024"):
    x = load("bea/CAINC4_NY_US.csv", y)
    print(y, "five whole counties transfers/personal income:", round(100 * sum(x[(f, "47")] for f in W) / sum(x[(f, "10")] for f in W), 1), "%", "($K", sum(x[(f, "47")] for f in W), "of", sum(x[(f, "10")] for f in W), ")")
