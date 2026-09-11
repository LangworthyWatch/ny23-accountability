#!/usr/bin/env python3
"""Social card: "handcuffs on law enforcement" vs what the district's own sheriffs and ICE's reports say.

Anchored to the Sept 11, 2026 update of
content/fact-checks/2026-09-03-law-and-order-posts-withheld-hsgp-funding.md (verdict: MISSING CONTEXT).

Hero is ICE's own number: one 287(g) encounter in all of New York, May through July 2026.
Left column is the fair reading (the ban is real, reimbursement is lost, jail warrant service ends).
Right column is the record: three NY-23 agencies, both sheriffs' own words, the $87M still owed.
Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Handcuffs on Law Enforcement." His Own Counties\' Sheriffs Say Otherwise.', size=27)
y = c.subtitle(y + 6, 'Sept 10 and 11, 2026: two more posts on Hochul and ICE. Six since Aug 26. Still no word on the $87M.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 52, "1", size=56, impact=True, fill=RED, anchor="mm")
c.text(170, y + 96, "287(g) encounter in all of NY", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "ICE's own monthly reports for its local partners: one encounter", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "statewide in May, June and July 2026 combined (Cattaraugus, June 5).", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "That is the enforcement the new state law ended when it voided", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "every 287(g) agreement on Aug 25. It began as a grand larceny arrest.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The ban is real. Local Cops, Local", True),
        ("Crimes Act, signed May 27, voided all", True),
        ("287(g) agreements as of Aug 25.", True),
        ("", False),
        ("Counties lose federal reimbursement", False),
        ("for deputies' time. Deputies can no", False),
        ("longer serve ICE warrants in the jail.", False),
        ("", False),
        ("15 sheriffs, incl. Cattaraugus, are", False),
        ("suing. The policy fight is real and", False),
        ("this site takes no side in it.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT HIS DISTRICT'S SHERIFFS SAID", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Cattaraugus Sheriff Butler: the law", True),
        ("bars civil immigration enforcement,", True),
        ('"something our deputies were not', True),
        ('doing in the first place."', True),
        ("", False),
        ("Steuben Legislature chair: \"I don't", False),
        ("believe we've participated in any of", False),
        ('those sorts of actions."', False),
        ("", False),
        ("Both counties complied. Both keep", False),
        ("working with ICE on criminal cases.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "HIS WORDS, CAMPAIGN PAGE, SEPT 10 AND 11", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, '"Kathy Hochul fights for violent illegal immigrants... while putting the handcuffs on law enforcement."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, '"She shields violent, criminal, illegal immigrants while shackling the cops trying to protect your family."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "Three of the 12 agencies the state notified were in NY-23: the Cattaraugus and Steuben sheriffs and Allegany village police.", size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "Six posts about backing the police since Aug 26. $17.7 million in federal grants for his counties' sheriffs is still unpaid.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "He has not mentioned the money once.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: Spectrum News, Aug 18 2026 (ICE 287(g) encounter reports)  ·  Wellsville Sun, Aug 25 2026 (Sheriff Butler)  ·  WSKG, Jul 28 and Aug 27 2026", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "NY AG letter, Jul 24 2026  ·  Gov. Hochul, Aug 25 and Sept 1 2026  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "handcuffs_287g_card.png"), to_desktop=True)
