#!/usr/bin/env python3
"""Social card: 35 press releases since the war began, none about it. September 17, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, DARK, GOLD, RED, RED_DK, GREEN,
                      MUTED, BORDER, WHITE)

c = Card(scale=3)

GREEN_BG = "#F0FFF4"; GREEN_BD = "#9AE6B4"
RED_BG = "#FFF5F5"; RED_BD = "#FEB2B2"

c.brand_bar()
y = c.badge(60, "DOCUMENTED PATTERN")
y = c.title(y, "35 Press Releases Since the War Began.", size=33)
y += 4
y = c.subtitle(y, "None of them mention it. He has voted eight times against ending it.", size=15)
y = c.divider(y + 10, margin=48, pad=16)

# ── 35 vs 0 ──
PT, PB = y, y + 372
MID = c.w / 2
c.panel(44, PT, MID - 8, PB, fill=GREEN_BG, outline=GREEN_BD, radius=8)
c.panel(MID + 8, PT, c.w - 44, PB, fill=RED_BG, outline=RED_BD, radius=8)
lcx = (44 + MID - 8) / 2
rcx = (MID + 8 + c.w - 44) / 2

c.text(lcx, PT + 26, "WHAT HIS OFFICE PUT OUT", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(lcx, PT + 46, "Feb. 28 to Sept. 16, 2026", size=12, fill=MUTED, anchor="mm")
c.text(lcx, PT + 122, "35", size=92, impact=True, fill=GREEN, anchor="mm")
c.text(lcx, PT + 186, "press releases", size=16, bold=True, fill=DARK, anchor="mm")
for i, s in enumerate(['"Condemn Socialism" vote statement', 'Concord grape juice purchase',
                       '1,500 beagles released', 'Canadian wildfire smoke',
                       'Insider trading bill passage', 'Airport and water grants']):
    c.text(lcx, PT + 222 + i * 23, s, size=13, fill="#4A5568", anchor="mm")

c.text(rcx, PT + 26, "THOSE THAT MENTION THE WAR", size=14, bold=True, fill=RED_DK, anchor="mm")
c.text(rcx, PT + 46, "same office, same window", size=12, fill=MUTED, anchor="mm")
c.text(rcx, PT + 122, "0", size=92, impact=True, fill=RED, anchor="mm")
c.text(rcx, PT + 186, "not one", size=16, bold=True, fill=DARK, anchor="mm")
for i, s in enumerate(['No mention of Iran, the cost,', 'or the votes to end it',
                       'No floor remarks in the Sept. 14 debate', '',
                       'He did put out a statement on', 'U.S. airstrikes on Iran in June 2025']):
    c.text(rcx, PT + 222 + i * 23, s, size=13,
           fill=("#4A5568" if i < 3 else MUTED), anchor="mm")

y = PB + 16

# ── Vote strip ──
SH = 124
c.panel(44, y, c.w - 44, y + SH, fill="#EDF2F7", outline=None, radius=8)
c.text(c.w / 2, y + 24, "WAR POWERS RESOLUTIONS TO END IT, MARCH TO SEPTEMBER 2026",
       size=13, bold=True, fill=NAVY, anchor="mm")
for cx, big, lab, col in [(c.w * 0.22, "8", "votes on the floor", NAVY),
                          (c.w * 0.50, "8", "times he voted No", RED),
                          (c.w * 0.78, "3", "passed the House anyway", NAVY)]:
    c.text(cx, y + 66, big, size=42, impact=True, fill=col, anchor="mm")
    c.text(cx, y + 100, lab, size=13, fill=DARK, anchor="mm")
y += SH + 14

# ── Cost callout ──
CH = 76
c.panel(44, y, c.w - 44, y + CH, fill="#FFFBEB", outline=GOLD, radius=8)
c.text(c.w / 2, y + 26, "WHAT IT HAS COST, PER CBO, SEPT. 15", size=13, bold=True, fill="#975A16", anchor="mm")
c.text(c.w / 2, y + 52, "$38 billion, plus $2 to $3 billion a month.  Diesel here: $4.10 to $6.31 a gallon.",
       size=14.5, fill=DARK, anchor="mm")
y += CH + 12

y = c.kicker(y,
             'He said on Sept. 10: "I have oversight over the entire federal government."',
             'CBO, Sept. 15: "DoD did not respond to CBO\'s requests for information."',
             h=96)

c.text(c.w / 2, y + 24, "Sources: langworthy.house.gov press releases (all 445 searched)  ·  CBO  ·  EIA  ·  House Clerk Roll Call 307",
       size=11.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 45, "langworthywatch.org/fact-checks/2026-06-18-epic-fury-cost-vs-cuts/",
       size=12.5, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save("social-media/iran_silence_card.png", to_desktop=True)
print("saved")
