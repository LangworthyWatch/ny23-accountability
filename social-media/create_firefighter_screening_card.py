#!/usr/bin/env python3
"""Social card: "fighting in Washington" for firefighter cancer screenings vs. the bill rosters.

Anchored to content/fact-checks/2026-09-21-firefighter-cancer-screening-bills.md
(verdict: MISSING CONTEXT).

Hero is the count: 0 of 2 firefighter cancer screening bills cosponsored. Left column is the
fair reading (what he does support, from official rosters and Clerk votes). Right column is
the gap. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Fighting in Washington" for Firefighter Cancer Screenings? Check the Bills.', size=27)
y = c.subtitle(y + 6, 'Sept 21, 2026, Clarence Center Fire Department. His office\'s advisory "did not identify a specific bill."', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 46, "0 of 2", size=46, impact=True, fill=RED, anchor="mm")
c.text(170, y + 88, "firefighter cancer screening", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(170, y + 106, "bills he has cosponsored", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "FIRE Cancer Act, H.R. 1610: federal grant money for fire departments", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "to provide cancer screenings. 7 cosponsors, incl. Rep. Lawler. Not him.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "The fire fighters' union lists it under \"Expanding Access to Cancer Screenings.\"", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "Also not on H.R. 2921, the federal firefighter cancer detection bill (11).", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT HE DOES SUPPORT", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Voted Yea on the defense bill that", True),
        ("made firefighter cancer a line-of-duty", True),
        ("death, and on the 2024 fire grants law.", True),
        ("", False),
        ("Cosponsors the PFAS-free gear bill,", False),
        ("the 9/11 health funding fix, and the", False),
        ("fallen-heroes act (signed on nine", False),
        ("days before it passed).", False),
        ("", False),
        ("Cosponsors the Medicare cancer", False),
        ("screening bill, with 337 others.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT HE HAS NOT SIGNED", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Both firefighter cancer screening", True),
        ("and detection bills: H.R. 1610", True),
        ("and H.R. 2921.", True),
        ("", False),
        ("HERO Act: responder mental health.", False),
        ("Federal Firefighters Families First.", False),
        ("Public safety collective bargaining", False),
        ("(Garbarino and Lawler are on it).", False),
        ("", False),
        ("Volunteer First Responder Housing", False),
        ("Act, a New York Republican's bill.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "HIS WORDS, OFFICIAL PAGE, SEPT 21", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, '"Early detection is the key to saving lives and that\'s why I\'m fighting in Washington', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, 'to expand access to cancer screenings and treatments."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "The fair reading: most members are on neither small bill, and showing up at a volunteer company's screening counts.", size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "The FIRE Cancer Act would let departments like Clarence Center's use federal grants for the screening he attended.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "Seven members have signed it. He is not one of them.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: govinfo BILLSTATUS cosponsor rosters (12 bills)  ·  House Clerk Roll Calls 2025-320 and 2024-194  ·  IAFF 2026 Legislative Issues Book", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Fingerlakes1, Sept 20 2026  ·  his official Facebook page, Sept 21 2026  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "firefighter_screening_card.png"), to_desktop=True)
