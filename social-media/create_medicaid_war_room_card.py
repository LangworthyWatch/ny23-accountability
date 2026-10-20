#!/usr/bin/env python3
"""Social card: "we took swift and decisive action against 50 high-risk Medicaid providers" (Oct 20, 2026 official
page) beside the CMS release it draws on.

Anchored to content/fact-checks/2026-10-20-medicaid-fraud-war-room-credit-claim.md (verdict: MISLEADING).

Hero: navy = the numbers check out (50 providers, $203.3M); red = who acted (42 OIG notices + 15 state actions).
Middle: the record. Fair reading on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"We Took Swift and Decisive Action Against', size=26)
y = c.title(y + 2, '50 High-Risk Medicaid Providers."', size=26)
y = c.title(y + 4, "The Action Was Taken by CMS, HHS's Inspector General and the States.", size=19, fill=DARK)
y = c.subtitle(y + 6, "His October 20, 2026 post on his official page, beside the CMS announcement it draws on.", size=14)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 214
lx, rx = 44, 44 + col_w + 16
top = y + 2
for x0, fill, outline, color, label, big, l1, l2 in [
    (lx, "#EDF2F7", "#A3BFD9", NAVY, "THE NUMBERS MATCH CMS", "50", "providers, about $203.3 million", "CMS announcement, July 28, 2026"),
    (rx, "#FFF5F5", "#FEB2B2", RED, "WHO TOOK THE ACTION", "42 + 15", "42 exclusion notices from HHS's", "inspector general; 15 state actions (7 overlap)"),
]:
    c.panel(x0, top, x0 + col_w, top + hero_h, fill=fill, outline=outline)
    c.text(x0 + col_w / 2, top + 26, label, size=14, bold=True, fill=color, anchor="mm")
    c.text(x0 + col_w / 2, top + 98, big, size=72, impact=True, fill=color, anchor="mm")
    c.text(x0 + col_w / 2, top + 162, l1, size=15, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + col_w / 2, top + 186, l2, size=14, fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- the record ----------------------------------------------------------------------------
rows = [("Who acted", "CMS's Medicaid Fraud War Room, HHS's Office of Inspector General and state Medicaid agencies."),
        ("What his committee did", "Oversight: letters to states, three subcommittee hearings. He isn't on that subcommittee or listed at the hearings."),
        ("What the $203 million measures", "What the 50 providers were paid since Jan 1, 2025. CMS gives no figure for how much was halted."),
        ("Where the cases stand", "Most were proposed exclusions that providers had 30 days to contest. CMS gave no count of final ones.")]
row_h = 54
box_h = 40 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 22, "WHAT THE RECORD SHOWS", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (lab, txt) in enumerate(rows):
    ry = y + 42 + i * row_h
    c.text(66, ry + 14, lab, size=15, bold=True, fill=NAVY, anchor="lm")
    c.text(66, ry + 36, txt, size=13.5, fill=DARK, anchor="lm")
y += box_h + 12

# ---- fair reading ---------------------------------------------------------------------------
fr_h = 104
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate(["The enforcement is real, and so is the committee's oversight. He has his own Medicaid screening bill.",
                        "\"Halting\" matches CMS's own headline, which says the War Room \"stops\" the payments.",
                        "\"We\" can be read broadly, but the post opens \"As a member of the Energy and Commerce Committee.\""]):
    c.text(c.w / 2, y + 48 + i * 21, ln, size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 86
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "His committee asked questions and held hearings.", size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 58, "The executive branch and the states took the action.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: CMS, July 28, 2026  ·  House Energy and Commerce Committee, Mar 5, 2026  ·  House Committee Repository  ·  House Clerk  ·  42 CFR 1001.2001",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "medicaid_war_room_card.png"), to_desktop=True)
