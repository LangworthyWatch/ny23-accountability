#!/usr/bin/env python3
"""Social card: State of the District, health access, September 2026.

Anchored to content/fact-checks/2026-09-08-state-of-the-district-health-access.md
(verdict: MISSING CONTEXT; district profile).

Hero is FPI's finding (8 hospitals, most of any district). Three layer panels:
hospitals, pharmacies, food. Concession panel first-in-order below the hero
(losses predate him; Rite Aid was a bankruptcy). Kicker is his own June 2026
town-hall line against the count. Every figure is in the entry and traces to a
retained file. Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'State of the District: Health Access in NY-23, September 2026', size=28)
y = c.subtitle(y + 6, 'What the district has, what it has lost, and what independent analysts say is at risk.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(150, y + 68, "8", size=84, impact=True, fill=RED, anchor="mm")
c.text(250, y + 32, "NY-23 hospitals on the Fiscal Policy Institute's at-risk list,", size=16, bold=True, fill=DARK, anchor="lm")
c.text(250, y + 60, '"the most of any district in the state."', size=16, bold=True, fill=DARK, anchor="lm")
c.text(250, y + 92, "Threshold: over 25% of revenue from Medicaid and public appropriations.", size=13, fill=MUTED, anchor="lm")
c.text(250, y + 114, "Brooks-TLC in Dunkirk: 97%. Bertrand Chaffee, Arnot Ogden, Cuba Memorial: over 40%.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- three layer panels -------------------------------------------------
gap = 14
pw = (c.w - 88 - 2 * gap) // 3
ph = 300
panels = [
    ("HOSPITALS", "2 closed", ["since 2000: Salamanca", "(2000), Silver Creek (2020).", "", "If the at-risk list closed,", "New York's emergency care", "desert population would rise", "182% (Cornell PAD)."]),
    ("PHARMACIES", "28 closed", ["since Jan. 2023, out of 130.", "25 were Rite Aid, 24 of the", "28 in 2025 alone.", "", "Six places now have none:", "Mayville, Silver Creek, Eden,", "Alfred, Salamanca, Lancaster."]),
    ("FOOD", "1 in 7", ["food insecure, in every", "county: 12.7% (Tioga) to", "15.6% (Chautauqua).", "", "Feeding America, Map the", "Meal Gap, 2023 data.", ""]),
]
for i, (hd, big, lines) in enumerate(panels):
    x0 = 44 + i * (pw + gap)
    c.panel(x0, y, x0 + pw, y + ph, fill="#EDF2F7" if i != 1 else "#FFF5F5", outline=BORDER if i != 1 else "#FEB2B2")
    c.text(x0 + pw / 2, y + 30, hd, size=15, bold=True, fill=NAVY, anchor="mm")
    c.text(x0 + pw / 2, y + 72, big, size=34, bold=True, fill=RED if i == 1 else NAVY, anchor="mm")
    for j, ln in enumerate(lines):
        c.text(x0 + pw / 2, y + 116 + j * 24, ln, size=13, fill=DARK, anchor="mm")
y += ph + 14

# ---- fair reading -------------------------------------------------------
fr_h = 96
c.panel(44, y, c.w - 44, y + fr_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(c.w / 2, y + 26, "THE FAIR READING", size=15, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 52, "Rural hospital and pharmacy loss is national and decades old. The pharmacies closed in a corporate", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 74, "bankruptcy, not by any vote. The $212M rural health award is real. None of that is attributed to him.", size=13, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker -------------------------------------------------------------
kick_h = 108
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 30, 'June 2026 town hall: "every rural hospital that I\'ve met is not on the verge of closure', size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 52, 'no matter what people are trying to sell you."', size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 84, "He voted for the law the at-risk analyses model. Eight of those hospitals are in his district.", size=16, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14

c.text(c.w / 2, y, "Sources: Fiscal Policy Institute, June 27 2025  ·  NYSED pharmacy registry, pulled Sept 8 2026  ·  NYSNA  ·  Cornell Program on Applied Demographics", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Feeding America Map the Meal Gap  ·  House Clerk Roll 190  ·  Method, data files, and every source at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "state_of_district_health_card.png"), to_desktop=True)
