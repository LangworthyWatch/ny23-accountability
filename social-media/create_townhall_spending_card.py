#!/usr/bin/env python3
"""Social card: official communications spending, talking at constituents vs. listening.

Anchored to content/fact-checks/2026-05-02-tele-town-hall-pattern.md
(published verdict: DOCUMENTED PATTERN; August 2026 spending update).

All figures from 13 quarters of House Statement of Disbursements, 2023Q1-2026Q1,
published at static/data/office_communications_spending.csv.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(60, "DOCUMENTED PATTERN")
y = c.title(y, "One Ad Buy Cost More Than 20 Town Halls", size=30)
y = c.subtitle(y + 6, "Three years of his office's own spending records, 2023 to 2026.", size=16)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 124
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(158, y + 2 + hero_h / 2, "$150,000", size=52, impact=True, fill=RED, anchor="mm")
c.text(292, y + 42, "for a single advertising buy, Aug. 15 to Sep. 2, 2024.", size=17, bold=True, fill=DARK, anchor="lm")
c.text(292, y + 72, "His office held 38 tele-town halls in three years.", size=17, bold=True, fill=DARK, anchor="lm")
c.text(292, y + 102, "That one payment exceeds the cost of twenty of them.", size=14, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 360
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 34, "TALKING AT YOU", size=17, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 58, "advertising", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 142, "$623,882", size=46, impact=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 210, "78 payments", size=17, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 258, "Two quarters carry 79%", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 284, "of every advertising dollar.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 322, "Four quarters: under $2,000.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(rx + col_w / 2, top + 34, "WHERE YOU TALK BACK", size=17, bold=True, fill=GREEN, anchor="mm")
c.text(rx + col_w / 2, top + 58, "tele-town halls", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 142, "$281,795", size=46, impact=True, fill=GREEN, anchor="mm")
c.text(rx + col_w / 2, top + 210, "38 events", size=17, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 258, "45 cents for every dollar", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 284, "spent the other direction.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 322, "Zero events billed in 2024 Q4.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- fairness strip -----------------------------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 26, "WHAT WE CHECKED AND DID NOT FIND", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab) in enumerate([("No violation", "ads ran outside the 60-day blackout"),
                                ("No overlap", "no shared official/campaign vendors"),
                                ("~25 cents", "per constituent reached, by his count")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 66, val, size=22, impact=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 98, lab, size=12, bold=True, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 104
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 36, "This is not about the price of any one call. It is about where the money goes.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 70, "No in-person town halls since January 2023.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 20

c.text(c.w / 2, y, "Source: House Statement of Disbursements, 13 quarters, 2023 Q1 to 2026 Q1", size=14, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "Full dataset published at langworthywatch.org/data/", size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "townhall_spending_card.png"),
       to_desktop=True)
