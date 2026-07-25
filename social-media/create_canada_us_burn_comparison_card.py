#!/usr/bin/env python3
"""Five-season acres-burned comparison, Canada vs the United States.
House style via lib/card.py. No verdict badge: this is a data explainer, not a
fact-check of a specific claim, and every badge in this project is a published
verdict label. Companion context for the Canada wildfire 'policy choice' entry."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, ORANGE, MUTED, DARK, WHITE

c = Card(scale=3)
c.brand_bar()

y = c.title(74, "Canada Burns 3.5x What the U.S. Does", size=33)
y = c.subtitle(y + 8, "Millions of acres burned per season, 2022 to 2026", size=16)
y = c.divider(y + 20)

# legend
ly = y + 12
c.rect(388, ly - 8, 412, ly + 8, fill=ORANGE, radius=3)
c.text(422, ly, "Canada", size=15, bold=True, fill=DARK, anchor="lm")
c.rect(548, ly - 8, 572, ly + 8, fill=NAVY, radius=3)
c.text(582, ly, "United States", size=15, bold=True, fill=DARK, anchor="lm")

rows = [
    ("2022", 4.4, 7.6),
    ("2023", 45.7, 2.7),
    ("2024", 13.3, 8.9),
    ("2025", 21.7, 5.1),
    ("2026 so far", 7.4, 3.9),
]

py0 = ly + 32
row_h = 96
panel_bot = py0 + row_h * len(rows) + 14
c.panel(44, py0, c.w - 44, panel_bot)

bx = 236
bx_max = c.w - 214
maxv = 45.7
yy = py0 + 54
for label, ca, us in rows:
    c.text(70, yy, label, size=17, bold=True, fill=DARK, anchor="lm")
    for val, color, off in ((ca, ORANGE, -20), (us, NAVY, 20)):
        barw = max((val / maxv) * (bx_max - bx), 5)
        c.rect(bx, yy + off - 15, bx + barw, yy + off + 15, fill=color, radius=4)
        c.text(bx + barw + 14, yy + off, f"{val}M", size=16, bold=True, fill=color, anchor="lm")
    yy += row_h

y = panel_bot + 28
c.text(c.w / 2, y, "Canada's worst season on record was the quietest U.S. year in the window.",
       size=16, fill=MUTED, anchor="mm")

# four-season totals behind the headline
sy = y + 24
for x0, x1, label, val, color in (
    (44, 532, "Canada, 2022 to 2025", "85.2M acres", ORANGE),
    (548, c.w - 44, "United States, 2022 to 2025", "24.3M acres", NAVY),
):
    c.panel(x0, sy, x1, sy + 76)
    mid = (x0 + x1) / 2
    c.text(mid, sy + 24, label, size=14, fill=MUTED, anchor="mm")
    c.text(mid, sy + 52, val, size=26, bold=True, fill=color, anchor="mm")

c.kicker(c.h - 214,
         "Most of the gap is not management. It is lightning, remoteness, and policy.",
         "About 40% of Canada's forest sits in zones where fires are not fought at all.")

c.text(c.w / 2, c.h - 88, "Sources: National Interagency Fire Center; CIFFC / Natural Resources Canada",
       size=13, fill=MUTED, anchor="mm")
c.footer_bar()
c.save("social-media/canada_us_burn_comparison_card.png", to_desktop=True)
