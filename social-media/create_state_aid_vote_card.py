#!/usr/bin/env python3
"""Context post v2: State aid per resident by 2024 presidential margin, three groups of the 57 counties outside NYC (FY2024).
Data: The Public Ledgers ny-state-aid county table FY2024 (retained in research/sources/aid-comparison-2026-11-11/).
Groups computed population-weighted from the county table (indicative; the 20-point cut is a reporting choice, shown
against a five-bin breakdown in the research README). v1 was a 57-dot scatter."""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import (Card, NAVY, INK, AMBER, AMBER_TXT, AMBER_TINT, GRAY, LINE, SLATE, SLATE_TINT, SLATE_LINE,
                         CONTENT_BOTTOM, FRAME_INSET)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "research/sources/aid-comparison-2026-11-11/tpl_ny_state_aid_counties_2024.csv")))
        if r["name"] != "New York City"]
f = lambda r, k: float(r[k])
def agg(sel, k):
    pop = sum(f(r, "pop") for r in sel); return sum(f(r, k) * f(r, "pop") for r in sel) / pop
groups = [("Counties Harris won", [r for r in rows if f(r, "margin") <= 0], NAVY),
          ("Trump won by under 20 points", [r for r in rows if 0 < f(r, "margin") < 20], NAVY),
          ("Trump won by 20 or more", [r for r in rows if f(r, "margin") >= 20], AMBER)]
vals = [(lab, len(sel), agg(sel, "state"), agg(sel, "fv"), col) for lab, sel, col in groups]
hi = vals[2][2]
rest = agg([r for r in rows if f(r, "margin") < 20], "state")      # every other upstate county, population-weighted
pct = round((hi / rest - 1) * 100)

c = Card()
y = c.top_bar("CONTEXT") + FRAME_INSET + 30
c.text(64, y, "STATE AID TO LOCAL GOVERNMENTS, PER RESIDENT, FY2024", size=15, bold=True, fill=AMBER_TXT, anchor="lt")
y += 30
y = c.wrap(64, y, f"Upstate Counties Trump Won by 20+ Points Get About {pct}% More State Aid Per Resident Than the Rest", 952, size=34, bold=True, fill=NAVY, leading=1.12)
y += 8
y = c.wrap(64, y, "The 57 counties outside New York City, grouped by the 2024 presidential vote.", 952, size=18, fill=GRAY)
y += 40

bx0, bx1 = 64, c.w - 64 - 170
unit = (bx1 - bx0) / 3700
for lab, n, v, fv, col in vals:
    c.text(bx0, y, f"{lab} ({n})", size=19, bold=True, fill=INK, anchor="lt")
    y += 32
    c.rect(bx0, y, bx0 + v * unit, y + 50, fill=col, radius=4)
    c.text(bx0 + v * unit + 14, y + 25, f"${v:,.0f}", size=36, impact=True, fill=NAVY if col == NAVY else AMBER_TXT, anchor="lm")
    y += 62
    c.text(bx0, y, f"Property value per resident: ${fv/1000:,.0f}K", size=16, fill=GRAY, anchor="lt")
    y += 52
y += 2
c.rect(64, y, c.w - 64, y + 56, fill=AMBER_TINT, outline=AMBER, width=2, radius=6)
c.text(84, y + 28, "Six of NY-23's seven whole counties are in the 20-or-more group.", size=19, bold=True, fill=INK, anchor="lm")
y += 76
fair_h = 104
c.rect(64, y, c.w - 64, y + fair_h, fill=SLATE_TINT, outline=SLATE_LINE, width=2, radius=6)
c.text(88, y + 22, "WHY", size=15, bold=True, fill=SLATE, anchor="lm")
c.wrap(88, y + 38, "Aid formulas don't look at votes. School aid sends more to places with less property and income to tax, and the most heavily Republican rural counties have the least. Statewide, with New York City and federal aid counted, Trump and Harris counties come out about even.",
       c.w - 176, size=16, fill=INK, leading=1.28)
assert y + fair_h < CONTENT_BOTTOM - 6, (y + fair_h, CONTENT_BOTTOM)
c.foot("Data: The Public Ledgers analysis of NYS Comptroller local-finance filings, FY2024; NYS Board of Elections",
       "thepublicledgers.org/deep-dives/ny-state-aid/")
c.save(os.path.join(ROOT, "social-media/state_aid_vote_card.png"), to_desktop=True)
print("pct", pct, "rest", round(rest), [(v[0], round(v[2]), round(v[3])) for v in vals])
