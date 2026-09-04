#!/usr/bin/env python3
"""Social card: the BUSES Act post vs the committee record.

Anchored to content/fact-checks/2026-09-04-buses-act-bounty-post-vs-committee-record.md
(verdict: MISLEADING). Published Sept 4, 2026.

Hero is the contradiction inside his own post: the caption says the bill
"ends" the bounty program; the video attached to it has him urging a yes on
the Peters amendment that lets the program continue. Green left concedes
first (the exchange and the $895K are real; the safety concern is real).
Red right is what the caption leaves out. Figures from the committee's own
recording and recap, the bill text, and NYC DEP rules, all retained.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, 'His Caption Says the Bill "Ends" the Bounty Program. His Video Says Otherwise.', size=26)
y = c.subtitle(y + 6, 'The BUSES Act, Sept 2 markup vs. Sept 3 Facebook post. Same clip, two stories.', size=15)
y = c.divider(y + 12)

# ---- hero: caption vs clip -----------------------------------------------
hero_h = 128
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(64, y + 30, "THE CAPTION, SEPT 3", size=13, bold=True, fill=RED, anchor="lm")
c.text(64, y + 56, '"My BUSES Act ends this Big Brother bounty hunt."', size=17, bold=True, fill=DARK, anchor="lm")
c.text(64, y + 88, "THE VIDEO HE ATTACHED, AT 3:50", size=13, bold=True, fill=NAVY, anchor="lm")
c.text(64, y + 114, '"I urge my colleagues to vote in favor of this amendment." It lets the program continue.', size=15, bold=True, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 318
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("He did battle Ocasio-Cortez. Her", True),
        ("amendment failed 23 to 25.", True),
        ("", False),
        ("Top earner in NYC's idling program:", False),
        ("$895,737 since 2019 (NY Post).", False),
        ("", False),
        ("A pre-trip engine check has no", False),
        ("clear exemption in city rules. That", False),
        ("gap is real, and the amendment he", False),
        ("backed was written to close it.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE CAPTION LEAVES OUT", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("NYC already exempts school buses", True),
        ("loading passengers, running", True),
        ("wheelchair lifts, and keeping", True),
        ("kids warm or cool.", True),
        ("", False),
        ("A Democrat's amendment narrowed", False),
        ("his bill to those purposes and lets", False),
        ("cities amend their programs, not", False),
        ("end them. He thanked him. Adopted", False),
        ("by voice vote. The program lives.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 116
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "FROM THE COMMITTEE'S OWN RECORDING, SEPT 2", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([
        ("Voice vote", "Peters amendment adopted,", "with his support (86:40)"),
        ("23 to 25", "Ocasio-Cortez amendment fails,", "his vote no (106:35)"),
        ("26 to 22", "bill reported, the closest vote", "of the ten bills that day")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 52, val, size=20, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 78, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 96, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'Ocasio-Cortez, in the clip he posted: penalizing drivers for helping a kid in a wheelchair "is a fairy tale."',
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "The city's rules say the same thing. So does the amendment he voted for.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: House Energy and Commerce markup video and recap, Sept 2 2026  ·  H.R. 9317 text and filed amendments (docs.house.gov)", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "NYC Admin Code 24-163 and DEP idling rules  ·  New York Post, Nov 4 2025  ·  Full timeline and timestamps at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "buses_act_card.png"), to_desktop=True)
