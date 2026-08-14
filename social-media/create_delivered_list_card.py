#!/usr/bin/env python3
"""Social card: his own Aug 12 2026 "proud to have delivered" list, checked line by line.

Rows are drawn ONLY from published, live entries. The Newstead $5,000,000 item on
his list is deliberately omitted: its entry is draft:true pending permalinks and a
request for comment, so there is nothing live to link.

Verdicts match the published entries exactly:
  Jasper-Troupsburg  2026-06-10-jasper-troupsburg-fema-award        MOSTLY TRUE
  Allegany water     2026-07-16-allegany-water-funding-third-announce  DOCUMENTED PATTERN
  Chautauqua mental  2026-07-17-chautauqua-mental-health-grant-credit  MISSING CONTEXT
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, BRONZE, MUTED, BORDER, WHITE, LIGHTGRAY)

ROWS = [
    ("$60.5M  Jasper-Troupsburg School Campus", "MOSTLY TRUE", GREEN, "#EBF8F0", "#9AE6B4",
     "The award is real and the superintendent credits him by name."),
    ("$1.25M  Allegany County Water System", "DOCUMENTED PATTERN", RED, "#FFF5F5", "#FEB2B2",
     "Same money, announced a third time. The senators secured it too."),
    ("$1M  Chautauqua Co. Dept. of Mental Hygiene", "MISSING CONTEXT", BRONZE, "#FFFAF0", "#F6C177",
     "The county won it by applying. A member does not pick the winner."),
]

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "3 OF 10 CHECKED")
y = c.title(y, "He Listed 10 Things He Delivered", size=31)
y = c.subtitle(y + 6, "We had already fact-checked three of them. Here is how they came back.", size=16)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 116
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#EDF2F7", outline=BORDER)
c.text(132, y + 2 + hero_h / 2, "1 of 3", size=46, impact=True, fill=NAVY, anchor="mm")
c.text(236, y + 40, "came back clean. We say so first, because it is true.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(236, y + 72, "The other two were already documented here.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(236, y + 100, "Verdict labels below are exactly as published. Nothing upgraded for effect.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 14

# ---- rows ---------------------------------------------------------------
row_h, gap = 168, 12
for i, (item, verdict, col, fill, outline, note) in enumerate(ROWS):
    ry = y + i * (row_h + gap)
    c.panel(44, ry, c.w - 44, ry + row_h, fill=fill, outline=outline)
    c.text(70, ry + 38, item, size=19, bold=True, fill=DARK, anchor="lm")
    c.text(70, ry + 86, verdict, size=26, impact=True, fill=col, anchor="lm")
    c.text(70, ry + 132, note, size=15, fill=DARK, anchor="lm")
y = y + len(ROWS) * (row_h + gap) + 6

# ---- kicker -------------------------------------------------------------
kick_h = 106
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 34, "His framing is fair: once the budget is set, bring money home. We are not disputing that.",
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 72, "The question is who else secured it, and who actually applied.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Source: his own post, Aug. 12, 2026  ·  three published fact-checks at langworthywatch.org", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "delivered_list_card.png"), to_desktop=True)
