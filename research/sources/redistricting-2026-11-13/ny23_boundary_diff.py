#!/usr/bin/env python3
"""Diff NY-23 between the 118th Congress map (2022, court-drawn) and the 119th (2024, Legislature),
using Census 2020-block-based relationship files (land area) and Vintage 2024 subcounty estimates (population).
Run from this folder: python3 ny23_boundary_diff.py"""
import csv
def load(f, cdcol):
    rows = list(csv.reader(open(f, encoding='utf-8-sig'), delimiter='|'))
    i = {k: n for n, k in enumerate(rows[0])}; out = {}
    for r in rows[1:]:
        if r[i[cdcol]] != '3623' or int(r[i['AREALAND_PART']]) == 0: continue
        tot = int(r[i['AREALAND_COUSUB_20']])
        out[r[i['GEOID_COUSUB_20']]] = (r[i['NAMELSAD_COUSUB_20']], round(100*int(r[i['AREALAND_PART']])/tot, 1) if tot else 0)
    return out
a = load('tab20_cd11820_cousub20_st36.txt', 'GEOID_CD118_20'); b = load('tab20_cd11920_cousub20_st36.txt', 'GEOID_CD119_20')
pop = {(r['COUNTY'], r['NAME']): int(r['ESTIMATESBASE2020']) for r in csv.DictReader(open('sub-est2024_36.csv', encoding='latin-1')) if r['SUMLEV'] == '061'}
for label, x, y in (("OUT", a, b), ("IN", b, a)):
    for g, (n, p) in sorted(x.items()):
        q = y.get(g, (n, 0))[1]
        if p > q + 1: print(f"{label} county {g[2:5]} {n}: {q}% -> {p}% of land" if label == "IN" else f"{label} county {g[2:5]} {n}: {p}% -> {q}% of land", "| 2020 base pop (whole town):", pop.get((g[2:5], n)))
