#!/usr/bin/env python3
"""Social card: one hero number for the Iran war's cost, with the local fuel line. September 17, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, DARK, GOLD, RED, RED_DK, GREEN,
                      MUTED, BORDER, WHITE)

c = Card(scale=3)

c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, "What the Iran War Has Cost.", size=34)
y += 4
y = c.subtitle(y, "The nonpartisan CBO put a number on it September 15. He has voted eight times against ending it.", size=14.5)
y = c.divider(y + 10, margin=48, pad=14)

# ── Hero: one number, full width ──
HT = 278
c.panel(44, y, c.w - 44, y + HT, fill=WHITE, outline=BORDER, radius=8)
c.text(c.w / 2, y + 30, "DEFENSE DEPARTMENT COST THROUGH AUGUST 1, 2026", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 126, "$38,000,000,000", size=66, impact=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 196, "and $2 to $3 billion more for every month it continues", size=19, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 232, "$13.1 billion of it replaces missile interceptors. CBO says the U.S. has burned through half to", size=12.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 252, "two thirds of that stockpile since June 2025, and rebuilding it will take at least five years.", size=12.5, fill=MUTED, anchor="mm")
y += HT + 16

# ── What it looks like here ──
LH = 168
c.panel(44, y, c.w - 44, y + LH, fill="#FFF5F5", outline="#FEB2B2", radius=8)
c.text(c.w / 2, y + 26, "AND WHAT IT LOOKS LIKE AT THE PUMP HERE", size=14, bold=True, fill=RED_DK, anchor="mm")
c.text(c.w / 2, y + 47, "week before the war started, to September 14", size=12, fill=MUTED, anchor="mm")
for cx, before, after, lab in [(c.w * 0.30, "$4.10", "$6.31", "diesel, our region"),
                               (c.w * 0.70, "$2.89", "$4.34", "gasoline, New York")]:
    c.text(cx - 62, y + 98, before, size=30, impact=True, fill=MUTED, anchor="mm")
    c.text(cx, y + 98, "to", size=15, fill=DARK, anchor="mm")
    c.text(cx + 62, y + 98, after, size=30, impact=True, fill=RED, anchor="mm")
    c.text(cx, y + 136, lab, size=13.5, fill=DARK, anchor="mm")
y += LH + 8
c.text(c.w / 2, y + 12, "CBO found the war raised the price of gasoline, diesel and, through freight costs, most other goods. It attributes part of the rise to the war, not all of it.",
       size=11.5, fill=MUTED, anchor="mm")
y += 30

# ── Votes strip ──
SH = 126
c.panel(44, y, c.w - 44, y + SH, fill="#EDF2F7", outline=None, radius=8)
c.text(c.w / 2, y + 22, "VOTES TO END IT, MARCH TO SEPTEMBER 2026", size=13, bold=True, fill=NAVY, anchor="mm")
for cx, big, lab, col in [(c.w * 0.22, "8", "votes on the floor", NAVY),
                          (c.w * 0.50, "8", "times he voted No", RED),
                          (c.w * 0.78, "3", "passed anyway", NAVY)]:
    c.text(cx, y + 66, big, size=42, impact=True, fill=col, anchor="mm")
    c.text(cx, y + 102, lab, size=13.5, fill=DARK, anchor="mm")
y += SH + 12

y = c.kicker(y,
             "CBO could not get the Pentagon to answer: \"DoD did not respond to CBO's requests for information.\"",
             "In 35 press releases since the war began, his office has not mentioned it once.",
             h=100)

c.text(c.w / 2, y + 28, "Sources: CBO, \"Estimating the Cost of Combat Operations Against Iran\" (Sept. 15, 2026)  ·  EIA weekly retail prices  ·  House Clerk  ·  langworthy.house.gov",
       size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 50, "langworthywatch.org/fact-checks/2026-06-18-epic-fury-cost-vs-cuts/",
       size=12.5, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save("social-media/iran_cost_hero_card.png", to_desktop=True)
print("saved")
