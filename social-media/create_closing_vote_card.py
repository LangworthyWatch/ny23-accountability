#!/usr/bin/env python3
"""Closing series 1 of 5: the vote and what it did in NY-23. Anchored to published entries (rural health fund,
Schuyler hospital, Chautauqua SNF cluster, beagle posts, Epic Fury). Light house style, 1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "THE RECORD, 1 OF 5")
y = c.title(y, "One Vote, Cast Twice. What It Did Here.", size=30)
y = c.subtitle(y + 6, "H.R. 1, the One Big Beautiful Bill Act. Roll 145, May 22, 2025: Yea. Roll 190, July 3, 2025: Aye.", size=15)
y = c.divider(y + 12)

hero_h = 130
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(190, y + 44, "$911 billion", size=40, impact=True, fill=RED, anchor="mm")
c.text(190, y + 82, "cut from federal Medicaid", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(190, y + 100, "(Congressional Budget Office)", size=12, fill=MUTED, anchor="mm")
c.text(360, y + 30, "450,000 New Yorkers lost health coverage on July 1, 2026.", size=16, bold=True, fill=DARK, anchor="lm")
c.text(360, y + 58, "The state's own count. His posts about it: zero.", size=15, fill=DARK, anchor="lm")
c.text(360, y + 84, "His posts about beagles, May through June: 30.", size=15, fill=DARK, anchor="lm")
c.text(360, y + 110, "Also cut: $206 billion from SNAP and related programs.", size=14, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

rows = [
    ("SCHUYLER", "The county hospital is on a published at-risk list for the cuts.", "He has never mentioned it."),
    ("CHAUTAUQUA", "A nursing home that closed was staffed below the federal minimum.", "His vote blocked enforcing that minimum until 2034."),
    ("RURAL FUND", "The $76 million he calls a \"historic investment\" is less than", "one-hundredth of one percent of the Medicaid cut in the same law."),
    ("OVERSIGHT", "His committee has held no hearing on where that money went.", "The same months: $132 billion in Operation Epic Fury costs."),
]
row_h = 108
for i, (tag, l1, l2) in enumerate(rows):
    top = y + i * (row_h + 10)
    c.panel(44, top, c.w - 44, top + row_h, fill=WHITE, outline=BORDER)
    c.text(64, top + row_h / 2, tag, size=16, bold=True, fill=RED, anchor="lm")
    c.text(230, top + 40, l1, size=16, bold=True, fill=DARK, anchor="lm")
    c.text(230, top + 70, l2, size=16, fill=DARK, anchor="lm")
y = y + 4 * (row_h + 10) + 8

kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "The fund is real. The law it came in is the one that put the hospital on the list.",
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "Every line above links to a published fact-check with sources.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: House Clerk rolls 145 and 190  ·  CBO via KFF  ·  NY State of Health  ·  Public Citizen at-risk list  ·  CMS staffing data  ·  his posts Sept 4, 10, 11, 2026", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entries at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closing_1_vote_card.png"), to_desktop=True)
