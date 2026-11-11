#!/usr/bin/env python3
"""Context post: State aid per resident vs. 2024 presidential margin, 57 counties outside NYC (FY2024).
Data: The Public Ledgers, ny-state-aid deep dive, county table FY2024 (thepublicledgers.org/data/ny_state_aid_counties_2024.csv,
retained in research/sources/aid-comparison-2026-11-11/). Indicative county figures; no causal reading."""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import (Card, NAVY, INK, AMBER, AMBER_TXT, GRAY, LINE, SLATE, SLATE_TINT, SLATE_LINE, WHITE,
                         CONTENT_TOP, CONTENT_BOTTOM, FRAME_INSET)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "research/sources/aid-comparison-2026-11-11/tpl_ny_state_aid_counties_2024.csv")))
        if r["name"] != "New York City"]
NY23 = {"Allegany County", "Cattaraugus County", "Chautauqua County", "Chemung County", "Schuyler County", "Steuben County", "Tioga County"}
LI = {"Nassau County", "Suffolk County"}

c = Card()
top = c.top_bar("CONTEXT") + FRAME_INSET
y = top + 26
c.text(64, y, "STATE AID TO LOCAL GOVERNMENTS, PER RESIDENT, FY2024", size=15, bold=True, fill=AMBER_TXT, anchor="lt")
y += 30
y = c.wrap(64, y, "Upstate, the Counties That Voted Most Heavily for Trump Get the Most State Aid", 952, size=34, bold=True, fill=NAVY, leading=1.15)
y += 8
y = c.wrap(64, y, "Each dot is one of the 57 counties outside New York City. NY-23's seven whole counties are amber.", 952, size=17, fill=GRAY)

# plot area
px0, px1 = 150, 1000
py0, py1 = y + 34, y + 34 + 470
xmin, xmax = -55, 55
ymin, ymax = 1500, 4800
X = lambda m: px0 + (m - xmin) / (xmax - xmin) * (px1 - px0)
Y = lambda v: py1 - (v - ymin) / (ymax - ymin) * (py1 - py0)
for v in (2000, 3000, 4000):
    c.rect(px0, Y(v), px1, Y(v) + 1, fill=LINE)
    c.text(px0 - 12, Y(v), f"${v:,}", size=14, fill=GRAY, anchor="rm")
c.rect(X(0), py0, X(0) + 2, py1, fill=SLATE_LINE)
c.text(X(0) - 10, py1 + 22, "Harris won", size=14, fill=GRAY, anchor="rm")
c.text(X(0) + 10, py1 + 22, "Trump won", size=14, fill=GRAY, anchor="lm")
for t in (-40, -20, 20, 40):
    c.text(X(t), py1 + 46, f"{abs(t)} pts", size=13, fill=GRAY, anchor="mm")
c.text((px0 + px1) / 2, py1 + 72, "2024 presidential margin", size=14, bold=True, fill=INK, anchor="mm")
# dots: others first, then NY-23 on top
def dot(r, fill, rad, outline=None):
    x, yy = X(float(r["margin"])), Y(float(r["state"]))
    c.d.ellipse([c._p(x - rad), c._p(yy - rad), c._p(x + rad), c._p(yy + rad)], fill=fill,
                outline=outline, width=c._p(1.5) if outline else 0)
for r in rows:
    if r["name"] not in NY23:
        dot(r, NAVY if r["name"] not in LI else "#8A97AA", 7)
for r in rows:
    if r["name"] in NY23:
        dot(r, AMBER, 10, outline=INK)
labels = {"Cattaraugus County": (14, -2, "lm"), "Allegany County": (14, 0, "lm"), "Steuben County": (2, -26, "mm"),
          "Chemung County": (-14, 8, "rm"), "Schuyler County": (14, 10, "lm")}
for r in rows:
    if r["name"] in labels:
        dx, dy, an = labels[r["name"]]
        c.text(X(float(r["margin"])) + dx, Y(float(r["state"])) + dy, r["name"].replace(" County", ""), size=14, bold=True, fill=INK, anchor=an)
# Chautauqua and Tioga sit together near +22 pts, ~$3,300: one leader-line label
ct = [r for r in rows if r["name"] in ("Chautauqua County", "Tioga County")]
cx = sum(X(float(r["margin"])) for r in ct) / 2; cy = sum(Y(float(r["state"])) for r in ct) / 2
c.rect(cx + 12, cy - 1, cx + 120, cy + 1, fill=INK)
c.text(cx + 126, cy - 9, "Chautauqua", size=14, bold=True, fill=INK, anchor="lm")
c.text(cx + 126, cy + 9, "and Tioga", size=14, bold=True, fill=INK, anchor="lm")
for r in rows:
    if r["name"] in LI:
        c.text(X(float(r["margin"])) + 10, Y(float(r["state"])) + 16, r["name"].replace(" County", ""), size=13, fill=GRAY, anchor="lm")
y = py1 + 96

# what it does and doesn't mean
s_h = 104
c.rect(64, y, c.w - 64, y + s_h, fill=SLATE_TINT, outline=SLATE_LINE, width=2, radius=6)
c.text(88, y + 22, "WHY", size=15, bold=True, fill=SLATE, anchor="lm")
c.wrap(88, y + 38, "The school-aid formula sends more to places with less property and income to tax. Rural upstate counties have the least, and they also voted most heavily Republican. Statewide, counting New York City and federal aid too, counties Trump won and counties Harris won come out about even.",
       c.w - 176, size=16, fill=INK, leading=1.28)
c.foot("Data: The Public Ledgers analysis of NYS Comptroller local-finance filings, FY2024; NYS Board of Elections",
       "thepublicledgers.org/deep-dives/ny-state-aid/")
assert y + s_h < CONTENT_BOTTOM - 8, (y + s_h, CONTENT_BOTTOM)
c.save(os.path.join(ROOT, "social-media/state_aid_vote_card.png"), to_desktop=True)
