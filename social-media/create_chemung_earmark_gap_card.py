#!/usr/bin/env python3
"""Card A — the Chemung earmark gap. House style, 1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, ORANGE

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "The County He Barely Funds", size=34)
y = c.subtitle(y + 6, "Langworthy's directed funding (earmarks), dollars per resident", size=15)
y = c.divider(y + 18)

rows = [
    ("Erie (home area)", 85.16, GREEN),
    ("Allegany", 83.34, GREEN),
    ("Cattaraugus", 81.62, GREEN),
    ("Schuyler", 56.94, MUTED),
    ("Chautauqua", 34.65, MUTED),
    ("Tioga", 30.96, MUTED),
    ("Steuben", 24.13, MUTED),
    ("Chemung", 5.84, RED),
]
py0 = y + 10
row_h = 62
panel_bot = py0 + row_h * len(rows) + 18
c.panel(44, py0, c.w - 44, panel_bot)

bx = 300
bx_max = c.w - 150
maxv = 85.16
yy = py0 + 46
for label, val, color in rows:
    c.text(70, yy, label, size=16, bold=True, fill=DARK, anchor="lm")
    barw = max((val / maxv) * (bx_max - bx), 6)
    c.rect(bx, yy - 13, bx + barw, yy + 13, fill=color, radius=4)
    vs = f"${val:,.0f}" if val >= 10 else f"${val:.2f}"
    c.text(bx + barw + 14, yy, vs, size=16, bold=True, fill=color, anchor="lm")
    yy += row_h

y = panel_bot + 26
c.text(c.w / 2, y, "The dollars broadly track need, with one county far below the rest.",
       size=15, fill=MUTED, anchor="mm")

c.kicker(c.h - 210,
         "Every other county got at least $24 per resident.",
         "Chemung, populous and poorer, got $5.84: one earmark, to a college.")
c.footer_bar()
c.save("social-media/chemung_earmark_gap_card.png", to_desktop=True)
