#!/usr/bin/env python3
"""Fracking explainer, entry 2026-11-01-fracking-explainer-pennsylvania-record (MISSING CONTEXT). v2: bar-chart frame, no party framing.
Figures: EIA (production), PA PUC (impact fee), BLS QCEW 2014/2024 (jobs/pay), Census PEP (population 2010-2024),
PA grand jury 2020, Pitt/DEP 2023. All retained under research/sources/fracking-explainer-2026-11-01/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  NOV 1, 2026")
y = c.title(y, "\"Enriched Next-Door Counties in Pennsylvania.\"", size=29)
y = c.title(y - 2, "Every One of Them Has Lost People Since 2010.", size=29)
y = c.subtitle(y + 6, "The New York Post's line, shared on his page Oct 30. His own op-ed: \"growing populations,\" \"East and West Berlin.\"", size=14)
y = c.divider(y + 12)

# Slim strip: what Pennsylvania got
strip_h = 92
c.panel(44, y, c.w - 44, y + strip_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(c.w / 2, y + 22, "WHAT PENNSYLVANIA GOT, AND IT IS REAL", size=13, bold=True, fill=GREEN, anchor="mm")
stats = [("16%", "of all U.S. gas"), ("$243.9M", "impact fees, 2025"), ("11,180", "direct gas jobs, 0.2% of workforce"), ("$15.04", "per Mcf vs. NY's $17.58")]
sw = (c.w - 88) / 4
for i, (big, small) in enumerate(stats):
    cx = 44 + sw * i + sw / 2
    c.text(cx, y + 50, big, size=22, bold=True, fill=GREEN, anchor="mm")
    c.text(cx, y + 74, small, size=11, fill=DARK, anchor="mm")
y += strip_h + 14

# Hero: bar chart of population change + jobs + pay
hero_h = 420
c.panel(44, y, c.w - 44, y + hero_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 28, "THE NEXT-DOOR COUNTIES: POPULATION CHANGE, 2010 TO 2024", size=15, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 50, "Pennsylvania's three most-drilled border counties and the three New York counties directly across the line", size=11.5, fill=MUTED, anchor="mm")
rows = [("Bradford, Pa.", -4.8, "-8.9%", "$60,899", RED),
        ("Susquehanna, Pa.", -12.0, "-3.1%", "$49,991", RED),
        ("Tioga, Pa.", -2.9, "-3.0%", "$50,266", RED),
        ("Chemung, N.Y.", -8.7, "-10.2%", "$58,195", NAVY),
        ("Steuben, N.Y.", -7.0, "-7.6%", "$74,444", NAVY),
        ("Tioga, N.Y.", -6.8, "+4.1%", "$69,400", NAVY)]
base_x = 600          # zero line
label_x = 70
scale = 330 / 12.0    # px per percentage point
jobs_x, pay_x = 760, 900
hy = y + 78
c.text(label_x, hy, "County", size=11, bold=True, fill=MUTED, anchor="lm")
c.text(base_x - 8, hy, "People, 2010-2024", size=11, bold=True, fill=MUTED, anchor="rm")
c.text(jobs_x, hy, "Jobs*", size=11, bold=True, fill=MUTED, anchor="mm")
c.text(pay_x, hy, "Avg. pay 2024", size=11, bold=True, fill=MUTED, anchor="mm")
row_h = 46
for i, (name, pop, jobs, pay, col) in enumerate(rows):
    ry = hy + 30 + i * row_h
    c.text(label_x, ry, name, size=14, bold=True, fill=col, anchor="lm")
    w = abs(pop) * scale
    c.rect(base_x - w, ry - 13, base_x, ry + 13, fill=col, outline=None)
    c.text(base_x - w - 8, ry, f"{pop:.1f}%", size=14, bold=True, fill=col, anchor="rm")
    c.text(jobs_x, ry, jobs, size=13, fill=DARK, anchor="mm")
    c.text(pay_x, ry, pay, size=13, bold=True, fill=DARK, anchor="mm")
c.rect(base_x, hy + 12, base_x + 1, hy + 30 + 5 * row_h + 14, fill=BORDER, outline=None)
c.text(c.w / 2, y + hero_h - 44, "Susquehanna County, Pa., home of the Dimock gas field, lost the most. The New York side pays more.", size=13, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + hero_h - 20, "*private-sector jobs, 2014-2024, the earliest county data on the federal open-data service. Sources: Census population estimates; BLS QCEW.", size=10.5, fill=MUTED, anchor="mm")
y += hero_h + 14

# Cost strip
cost_h = 96
c.panel(44, y, c.w - 44, y + cost_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(c.w / 2, y + 24, "WHAT IT COST, PER PENNSYLVANIA'S OWN INSTITUTIONS", size=13, bold=True, fill=RED, anchor="mm")
c.text(c.w / 2, y + 50, "2020 statewide grand jury: the state's \"wait and see\" approach to health was \"unacceptable\"; wells belong 2,500 feet from homes, not 500.", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 74, "2023 state-commissioned studies: lymphoma 5 to 7x within a mile of a well; asthma attacks 4 to 5x. Associations, not proof.", size=12, fill=DARK, anchor="mm")
y += cost_h + 14

kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "Pennsylvania chose the gas and its costs. New York chose neither.", size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 64, "The border counties on both sides are losing people either way.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: EIA  ·  PA Public Utility Commission  ·  BLS QCEW  ·  Census  ·  43rd PA Grand Jury (2020)  ·  PA DEP review of the Pitt studies (2023)", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-11-01-fracking-explainer-pennsylvania-record/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fracking_explainer_card.png"), to_desktop=True)
