#!/usr/bin/env python3
"""Social card: the "Surge to Save Newborns Act" announcement vs. the abolished RUSP advisory committee.

Anchored to content/fact-checks/2026-09-25-surge-to-save-newborns-act.md (verdict: MISSING CONTEXT).

Hero is the date HHS terminated the committee that builds the screening panel. Left column is the fair
reading. Right column is what was left out, from HHS's own Federal Register notices, govinfo and the
Clerk. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '$35M a Year to Implement the Newborn Screening Panel. Who Builds It Now?', size=27)
y = c.subtitle(y + 6, 'Sept 25, 2026: the "Surge to Save Newborns Act," announced with Jim and Jill Kelly. What the announcement left out.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 46, "April 1, 2025", size=36, impact=True, fill=RED, anchor="mm")
c.text(170, y + 88, "the day HHS terminated the", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(170, y + 106, "newborn screening committee", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "The Advisory Committee on Heritable Disorders in Newborns and Children", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "decided what goes on the panel. It voted to add Krabbe disease in 2024.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "He thanked it by name then. On Sept 25 he credited \"the advisory committee\"", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "again. He did not say it no longer exists. HHS's own notices say it does not.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 352
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The gap is real: a federal", True),
        ("recommendation does not fund a", True),
        ("state lab. States lag for years.", True),
        ("", False),
        ("The bill is bipartisan (with Rep.", False),
        ("Schrier) and fits his Krabbe", False),
        ("record since 2023.", False),
        ("", False),
        ("New York already screens for", False),
        ("Krabbe. The babies helped are", False),
        ("mostly born in other states.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT WAS LEFT OUT", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The panel's expert committee is", True),
        ("gone. Its replacement: a $700,000", True),
        ("contractor \"workgroup\" (Aug 2026).", True),
        ("", False),
        ("He already co-leads H.R. 4709, which", False),
        ("would restore the committee. It has", False),
        ("sat in his own committee since", False),
        ("Sept 10, 2025. No markup.", False),
        ("", False),
        ("Medicaid pays for 4 in 10 births. He", False),
        ("voted to cut it by $911 billion.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHERE THE $35 MILLION COMES FROM", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, "The Surge to Save Newborns coalition (Hunter's Hope and 15 other groups, supported by Travere Therapeutics and BioMarin)", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, "asked Congress for a one-time $173 million. The bill: $35 million a year, 2027 to 2031. New York's estimated share: $7.6 million.", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, 'Jim Kelly, Sept 25: "We already got a note out to Mr. Kennedy, and hopefully we\'re going to be able to sit down with him."', size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'July 2024, his release: thanks to "the Advisory Committee on Heritable Disorders in Newborns and Children for their thorough review."',
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "A bill to implement the panel faster, with no word on who decides what is on it.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: Federal Register, Aug 14 2025, Dec 22 2025, Aug 12 2026  ·  CRS R48757  ·  govinfo H.R. 4709 status and text  ·  Facebook Live transcript, Sept 25 2026", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Manatt Health for the coalition, Mar 2026  ·  KFF, Oct 2025  ·  House Clerk Rolls 145 and 190 (2025)  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "surge_newborns_card.png"), to_desktop=True)
