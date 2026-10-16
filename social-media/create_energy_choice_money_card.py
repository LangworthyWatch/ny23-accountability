#!/usr/bin/env python3
"""Social card: the Energy Choice Act's drafter and named supporters as donors.

Anchored to content/fact-checks/2026-10-16-energy-choice-act-supporter-money.md (verdict: DOCUMENTED PATTERN).

Hero pairs two parallel facts (not claim vs. reality, so navy panels, no red/green): NEFI's PAC ranks him #1, and six
of the 17 supporters named in his own release gave $54,000. Bars show the six. The fair reading sits on the card, not
just in the caption. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, 'The Group That Says It "Helped Draft" His Energy Choice Act', size=26)
y = c.title(y + 2, "Made Him Its Top PAC Recipient.", size=26)
y = c.subtitle(y + 6, "FEC filings, 2025-26 cycle, his campaign and leadership PAC. Checked against his own list of the bill's supporters.", size=14)
y = c.divider(y + 12)

# ---- hero: two parallel facts ---------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 196
lx, rx = 44, 44 + col_w + 16
top = y + 2
for x0, label, big, lines in [
    (lx, "NEFI HOME COMFORT PAC", "#1",
     ["of 10 candidate and party committees", "it paid this cycle: $9,263 to his campaign.", 'NEFI says it "helped draft" the bill.']),
    (rx, "SIX OF THE BILL'S NAMED SUPPORTERS", "$54,000",
     ["to his campaign and leadership PAC.", "6 of the 17 groups his June 2025", "press release listed as backers."]),
]:
    c.panel(x0, top, x0 + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
    c.text(x0 + col_w / 2, top + 26, label, size=14, bold=True, fill=NAVY, anchor="mm")
    c.text(x0 + col_w / 2, top + 82, big, size=58, impact=True, fill=NAVY, anchor="mm")
    for i, ln in enumerate(lines):
        c.text(x0 + col_w / 2, top + 134 + i * 22, ln, size=14, bold=(i == 0), fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- bars ------------------------------------------------------------------------
bars = [("National Association of Home Builders", 20000, "$20,000"),
        ("National Propane Gas Association", 10000, "$10,000"),
        ("National Energy & Fuels Institute (NEFI)", 8500, "$8,500"),
        ("American Gas Association", 7500, "$7,500"),
        ("Plumbing-Heating-Cooling Contractors", 5000, "$5,000"),
        ("Energy Marketers of America", 3000, "$3,000")]
row_h = 40
box_h = 44 + row_h * len(bars) + 8
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 22, "PAC GIFTS FROM THE SUPPORTERS HE NAMED, 2025-26", size=14, bold=True, fill=NAVY, anchor="mm")
bx0, bx1 = 420, c.w - 160
for i, (name, amt, lab) in enumerate(bars):
    ry = y + 48 + i * row_h
    c.text(400, ry + 14, name, size=14, bold=True, fill=DARK, anchor="rm")
    w = (bx1 - bx0) * amt / 20000
    c.rect(bx0, ry + 3, bx0 + w, ry + 25, fill=NAVY, radius=4)
    c.text(bx0 + w + 10, ry + 14, lab, size=14, bold=True, fill=NAVY, anchor="lm")
y += box_h + 12

# ---- timing + fair reading ------------------------------------------------------
fr_h = 132
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE TIMING, AND THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate([
        "Home builders' $10,000 arrived Nov 26, 2025, between the bill's subcommittee and full-committee votes.",
        "Legal and disclosed. PACs often give to members who already agree with them; the propane",
        "group's checks went out in identical batches to other members. NEFI's PAC also funds Democrats.",
        "The $54,000 is about 4% of the $1.28 million in PAC and party money his committees took in."]):
    c.text(c.w / 2, y + 50 + i * 22, ln, size=13.5, bold=(i == 0), fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ----------------------------------------------------------------------
kick_h = 80
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "A documented sequence, not proof of a deal.", size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 54, "Know who backs the bill with money, not just letters.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 12

c.text(c.w / 2, y, "Sources: FEC filings of Langworthy for Congress, Circle the Wagons PAC and NEFI Home Comfort PAC  ·  his June 5, 2025 release  ·  NEFI, Sept 16, 2025  ·  govinfo BILLSTATUS H.R. 3699",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "energy_choice_money_card.png"), to_desktop=True)
