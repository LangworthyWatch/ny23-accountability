#!/usr/bin/env python3
"""Fracking explainer, entry 2026-11-01-fracking-explainer-pennsylvania-record (MISSING CONTEXT).
Figures: EIA (production), PA PUC (impact fee), BLS QCEW 2024 (jobs/pay), Census PEP (population 2010-2024),
PA grand jury 2020, Coterra plea 2022, Pitt/DEP 2023. All retained under research/sources/fracking-explainer-2026-11-01/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  NOV 1, 2026")
y = c.title(y, "\"Enriched Next-Door Counties in Pennsylvania.\"", size=29)
y = c.title(y - 2, "The Next-Door Counties, by the Numbers.", size=29)
y = c.subtitle(y + 6, "The New York Post's line, shared on his page Oct 30. His own op-ed: \"growing populations,\" \"East and West Berlin.\"", size=14)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 400
lx, rx = 44, 44 + col_w + 16
top = y + 2

# LEFT: what Pennsylvania got (the reasonable part)
c.panel(lx, top, lx + col_w, top + col_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT PENNSYLVANIA GOT", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 96, "16%", size=60, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 142, "of all U.S. natural gas, from a state that", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 164, "produced under 1% of it in 2008", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["$243.9 million in impact fees in 2025,",
                       "$3.12 billion since 2012, most of it local.",
                       "11,180 direct gas jobs statewide (BLS, 2024),",
                       "two-tenths of one percent of the workforce.",
                       "Cheaper gas: $15.04 vs. New York's $17.58 per Mcf.",
                       "Real money. Reported here in full."]):
    c.text(lx + col_w / 2, top + 204 + i * 30, t, size=13, bold=(i == 5), fill=DARK, anchor="mm")

# RIGHT: the next-door counties
c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "THE NEXT-DOOR COUNTIES, 2010 TO 2024", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 96, "-12%", size=60, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 142, "population, Susquehanna County, Pa.", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 164, "home of the Dimock gas field, across from Broome", size=13, fill=MUTED, anchor="mm")
# mini table
cx = [rx + 24, rx + 196, rx + 290, rx + 392]
hy = top + 198
for x, h in zip(cx, ["County", "People", "Jobs*", "Pay 2024"]):
    c.text(x, hy, h, size=11.5, bold=True, fill=MUTED, anchor="lm")
rows = [("Bradford, Pa.", "-4.8%", "-8.9%", "$60,899"),
        ("Susquehanna, Pa.", "-12.0%", "-3.1%", "$49,991"),
        ("Tioga, Pa.", "-2.9%", "-3.0%", "$50,266"),
        ("Chemung, N.Y.", "-8.7%", "-10.2%", "$58,195"),
        ("Steuben, N.Y.", "-7.0%", "-7.6%", "$74,444"),
        ("Tioga, N.Y.", "-6.8%", "+4.1%", "$69,400")]
for i, r in enumerate(rows):
    ry = hy + 24 + i * 26
    col = NAVY if "N.Y." in r[0] else DARK
    for x, v in zip(cx, r):
        c.text(x, ry, v, size=12.5, bold=(x == cx[0]), fill=col, anchor="lm")
c.text(rx + col_w / 2, top + 384, "*private jobs 2014-2024, the earliest county data available", size=10.5, fill=MUTED, anchor="mm")
y = top + col_h + 14

strip_h = 166
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 30, "WHAT IT COST, PER PENNSYLVANIA'S OWN INSTITUTIONS", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 62, "2020 grand jury: the Health Dept.'s \"wait and see\" approach was \"unacceptable\"; drilling should be 2,500 ft from homes, not 500.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 92, "Dimock, 2022: the driller pleaded no contest, $16.29 million for a water line and 75 years of residents' water bills.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 126, "2023 state-commissioned studies: lymphoma 5 to 7x within a mile of a well; asthma attacks 4 to 5x. Associations, not proof.", size=12.5, bold=True, fill=DARK, anchor="mm")
y += strip_h + 14

kick_h = 112
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 36, "New York's ban was imposed in 2014-15 and written into law in April 2020, before Gov. Hochul took office. A governor cannot lift it alone.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 72, "Every county on both sides of the line lost people. The New York side pays more.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: EIA  ·  PA Public Utility Commission  ·  BLS QCEW 2024  ·  Census population estimates  ·  43rd PA Grand Jury (2020)  ·  PA DEP review of the Pitt studies (2023)", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-11-01-fracking-explainer-pennsylvania-record/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fracking_explainer_card.png"), to_desktop=True)
