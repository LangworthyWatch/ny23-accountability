#!/usr/bin/env python3
"""Social card: the Newstead Community Center earmark, announced by three offices the same day.

Anchored to content/fact-checks/2026-08-06-newstead-community-center-shared-earmark.md
(verdict: MISSING CONTEXT). NOTE: that entry is draft:true pending Facebook permalinks
and a request for comment. Do not post this card until the entry is live.

Color logic per the house card audit: the two announcement panels are PARALLEL items
(the same appropriation described twice), so they use plain navy-outlined panels rather
than the red/green adversarial treatment.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(60, "MISSING CONTEXT")
y = c.title(y, "One Appropriation. Three Offices. Same Day.", size=31)
y = c.subtitle(y + 6, "The Newstead Community Center money is real. So are the senators.", size=16)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#EDF2F7", outline=BORDER)
c.text(178, y + 2 + hero_h / 2, "$5,000,000", size=46, impact=True, fill=NAVY, anchor="mm")
c.text(330, y + 38, "for one 32,000 sq ft community center in", size=18, bold=True, fill=DARK, anchor="lm")
c.text(330, y + 66, "the Town of Newstead, Erie County.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(330, y + 96, "Announced by three offices on Feb. 4, 2026.", size=14, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two parallel panels (same money, described twice) -------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 344
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill=WHITE, outline=NAVY, width=2)
c.text(lx + col_w / 2, top + 32, "HIS RELEASE", size=17, bold=True, fill=NAVY, anchor="mm")
c.text(lx + col_w / 2, top + 56, "February 4, 2026", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 104, "\"he has secured", size=19, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 132, "$5,000,000 in Community", size=19, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 160, "Project Funding\"", size=19, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "Mentions of Schumer", size=16, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 240, "or Gillibrand:", size=16, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 286, "NONE", size=34, impact=True, fill=RED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill=WHITE, outline=NAVY, width=2)
c.text(rx + col_w / 2, top + 32, "THEIR RELEASE", size=17, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 56, "February 4, 2026, the same day", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 104, "Schumer and Gillibrand", size=19, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 132, "list the identical", size=19, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 160, "$5,000,000 project", size=19, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 214, "One of seven in a", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 240, "$9,275,000 WNY package.", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 286, "Same 880 seniors, 350 youth.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- what is not in dispute ---------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(c.w / 2, y + 26, "WHAT IS NOT IN DISPUTE", size=15, bold=True, fill=GREEN, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab) in enumerate([("The money is real", "enacted in the FY26 approps bill"),
                                ("He did secure it", "a House sponsor is required"),
                                ("Newstead is his", "Erie County, in NY-23")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 62, val, size=19, bold=True, fill=GREEN, anchor="mm")
    c.text(cx, y + 92, lab, size=13, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 100
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 34, "It is not $5 million from him plus $5 million from them. It is one appropriation.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 68, "Announced again in August, six months later, as new.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 20

c.text(c.w / 2, y, "Sources: Rep. Langworthy press release, Feb. 4 2026  ·  Sens. Schumer and Gillibrand, same date", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "FY 2026 Consolidated Appropriations Act, enacted Feb. 3 2026", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "newstead_shared_earmark_card.png"),
       to_desktop=True)
