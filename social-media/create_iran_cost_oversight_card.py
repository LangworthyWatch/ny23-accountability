#!/usr/bin/env python3
"""Social card: CBO prices the Iran war, the pump, and eight war powers votes. September 17, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      MUTED, LIGHTGRAY, BORDER, WHITE)

c = Card(scale=3)

# ── Header ──
c.brand_bar()
y = c.badge(64, "DOCUMENTED PATTERN")
y = c.title(y, "The War Now Has a Price Tag.", size=36)
y += 6
y = c.subtitle(y, "The nonpartisan CBO priced it on September 15. The House has voted eight times to end it.", size=15)
y = c.divider(y + 12, margin=48, pad=18)

# ── Two parallel cost panels (navy outlines: parallel facets, not claim vs. reality) ──
PT, PB = y, y + 356
MID = c.w / 2
c.panel(44, PT, MID - 8, PB, fill=WHITE, outline=BORDER, radius=8)
c.panel(MID + 8, PT, c.w - 44, PB, fill=WHITE, outline=BORDER, radius=8)

lcx = (44 + MID - 8) / 2
rcx = (MID + 8 + c.w - 44) / 2

c.text(lcx, PT + 26, "WHAT CBO SAYS IT HAS COST", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(lcx, PT + 46, "Defense Dept., through Aug. 1", size=12, fill=MUTED, anchor="mm")
c.text(lcx, PT + 128, "$38B", size=84, impact=True, fill=NAVY, anchor="mm")
c.text(lcx, PT + 192, "and it keeps running", size=15, bold=True, fill=DARK, anchor="mm")
for i, s in enumerate(["plus $2 to $3 billion every month", "$13.1B of it: missile interceptors",
                       "half to two-thirds of the U.S.", "interceptor stock used since June 2025",
                       "at least 5 years to rebuild it"]):
    c.text(lcx, PT + 228 + i * 23, s, size=13, fill="#4A5568", anchor="mm")

c.text(rcx, PT + 26, "WHAT IT COSTS IN NY-23", size=14, bold=True, fill=RED_DK, anchor="mm")
c.text(rcx, PT + 46, "week before the war, to Sept. 14", size=12, fill=MUTED, anchor="mm")
c.text(rcx, PT + 128, "+$2.21", size=84, impact=True, fill=RED, anchor="mm")
c.text(rcx, PT + 192, "a gallon, diesel", size=15, bold=True, fill=DARK, anchor="mm")
for i, s in enumerate(["diesel: $4.10 to $6.31 (EIA)", "gasoline: $2.89 to $4.34 (NY, EIA)",
                       "CBO: the war raised the price of", "gasoline, diesel and, through freight,",
                       "most other goods"]):
    c.text(rcx, PT + 228 + i * 23, s, size=13, fill="#4A5568", anchor="mm")

y = PB + 10
c.text(c.w / 2, y + 12, "CBO attributes part of that fuel increase to the war, not all of it. Prices move for many reasons.",
       size=12, fill=MUTED, anchor="mm")

# ── The vote strip ──
y += 32
SH = 140
c.panel(44, y, c.w - 44, y + SH, fill="#EDF2F7", outline=None, radius=8)
c.text(c.w / 2, y + 24, "WAR POWERS RESOLUTIONS TO END IT, MARCH 2026 TO SEPTEMBER 2026",
       size=13, bold=True, fill=NAVY, anchor="mm")
cols = [(c.w * 0.22, "8", "votes on the floor", NAVY),
        (c.w * 0.50, "8", "times he voted No", RED),
        (c.w * 0.78, "3", "passed the House anyway", NAVY)]
for cx, big, lab, col in cols:
    c.text(cx, y + 70, big, size=46, impact=True, fill=col, anchor="mm")
    c.text(cx, y + 112, lab, size=13.5, fill=DARK, anchor="mm")
y += SH

# ── What the price tag leaves out (gold callout) ──
y += 18
CH = 74
c.panel(44, y, c.w - 44, y + CH, fill="#FFFBEB", outline=GOLD, radius=8)
c.text(c.w / 2, y + 27, "WHAT THE $38 BILLION LEAVES OUT", size=13, bold=True, fill="#975A16", anchor="mm")
c.text(c.w / 2, y + 51, "CBO excludes future veterans' health care and disability compensation.", size=14, fill=DARK, anchor="mm")
y += CH

# ── Kicker: his claim against CBO's sentence ──
y += 18
y = c.kicker(y,
             'He said on Sept. 10: "I have oversight over the entire federal government."',
             'CBO, Sept. 15: "DoD did not respond to CBO\'s requests for information."',
             h=104)

# ── Sources ──
c.text(c.w / 2, y + 30, "Sources: CBO, \"Estimating the Cost of Combat Operations Against Iran\" (Sept. 15, 2026)  ·  EIA weekly retail prices  ·  House Clerk Roll Call 307",
       size=11.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 54, "langworthywatch.org/fact-checks/2026-06-18-epic-fury-cost-vs-cuts/",
       size=12.5, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save("social-media/iran_cost_oversight_card.png", to_desktop=True)
print("saved")
