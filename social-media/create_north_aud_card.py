#!/usr/bin/env python3
"""Social card: the HUD inspector-general letter about Buffalo vs. what is pending in NY-23.

Anchored to content/fact-checks/2026-09-09-north-aud-probe-not-his-district.md
(verdict: MISSING CONTEXT).

Hero is the geography: the project he asked a federal IG to investigate is in
NY-26. Left column concedes (jurisdiction is real; the subsidy question is
contested). Right column is the district record the same week, each item a
published entry. Kicker turns his adviser's "affects the region" rationale on
the withheld police money. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'He Asked a Federal Inspector General to Probe a Buffalo Project. It Is Not His District.', size=25)
y = c.subtitle(y + 6, 'Sept 8, 2026: a letter to HUD about the North Aud Block at Canalside. Here is what was pending at home.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 128
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 56, "NY-26", size=44, impact=True, fill=RED, anchor="mm")
c.text(170, y + 96, "not NY-23", size=15, bold=True, fill=MUTED, anchor="mm")
c.text(310, y + 30, "The project is in downtown Buffalo, represented by Rep. Tim Kennedy.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(310, y + 56, 'Buffalo News: "Langworthy doesn\'t represent downtown Buffalo or Canalside."', size=14, fill=DARK, anchor="lm")
c.text(310, y + 84, 'His adviser: his Oversight seat gives him jurisdiction "on a project that', size=13, fill=MUTED, anchor="lm")
c.text(310, y + 104, 'affects the region, not just the footprint of the site."', size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 322
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Oversight jurisdiction is real. A", True),
        ("member can ask an IG about any", True),
        ("federally funded project.", True),
        ("", False),
        ("The subsidy question is contested:", False),
        ("$609,000 of public support per", False),
        ("apartment, up from a $10M RFP.", False),
        ("", False),
        ("He has worked district issues this", False),
        ("year: grapes, grants, biosimilars.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "PENDING IN NY-23 THE SAME WEEK", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("$87M in police and counterterror", True),
        ("grants withheld from NY, $17.7M of", True),
        ("it for county sheriffs. No statement.", True),
        ("", False),
        ("8 hospitals on a federal at-risk list,", False),
        ("most of any district. His line: not", False),
        ('"on the verge of closure."', False),
        ("", False),
        ("28 pharmacies closed since 2023.", False),
        ("Six places now have none.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT HE ASKED THE INSPECTOR GENERAL TO REVIEW, PER THE BUFFALO NEWS", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, '"Whether the jump in public subsidies raises concerns regarding procurement integrity,', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, 'internal controls, waste, fraud or abuse." He added: "I\'m not accusing anyone of anything."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "The letter itself has not been released. Quotes are as reported.", size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'His office says the Buffalo project "affects the region, not just the footprint of the site."',
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "By that standard, what region does $87 million in withheld police funding affect?",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: Buffalo News, Sept 9 2026  ·  WIVB, Sept 8 2026  ·  Census Bureau geocoder (119th CD)  ·  Gov. Hochul, Sept 1 2026", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Fiscal Policy Institute, June 2025  ·  NYSED pharmacy registry, Sept 8 2026  ·  Full entries and sources at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "north_aud_card.png"), to_desktop=True)
