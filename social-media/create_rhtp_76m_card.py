#!/usr/bin/env python3
"""Social card: the $76 million rural health post, the same award a third time.

Anchored to the Sept 4, 2026 addendum on
content/fact-checks/2026-06-02-rural-health-transformation-212m.md
(verdict: MISSING CONTEXT).

Hero is the arithmetic: three announcements, one $212M award, and the loss
figures the announcements never mention. Green left concedes first (the
money is real, NY-23 counties are targeted, an NY-23 applicant exists).
Figures from NY DOH's own funding guidance, CMS's release, KFF, and HANYS,
all retained in research/sources/rhtp-76m-2026-09/.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'Three Announcements, One Award. He Announced This $76 Million in December.', size=26)
y = c.subtitle(y + 6, 'Sept 4 post: "this $76 million statewide investment delivers on that promise."', size=15)
y = c.divider(y + 12)

# ---- hero: the timeline -------------------------------------------------
hero_h = 124
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
third = (c.w - 88) // 3
for i, (d, l1, l2) in enumerate([
        ("Dec 30, 2025", "Press release:", "\"$212 million\" for NY"),
        ("Jul 15, 2026", "Centralus event:", "the $50B fund, again"),
        ("Sep 4, 2026", "Facebook: \"$76 million\"", "= $76,190,022 of the $212M")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 34, d, size=19, bold=True, fill=RED, anchor="mm")
    c.text(cx, y + 64, l1, size=13, fill=DARK, anchor="mm")
    c.text(cx, y + 84, l2, size=13, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 110, "Source for the last box: New York's own funding guidance. Applications for that money closed July 14.", size=12, fill=MUTED, anchor="mm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 330
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The money is real: $212,058,207", True),
        ("to New York for FY2026.", True),
        ("", False),
        ("Seven NY-23 counties are among", False),
        ("the 48 eligible for this piece.", False),
        ("", False),
        ("A Cattaraugus health system said", False),
        ("in July it was applying. Rural", False),
        ("providers do need the help.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE POST LEAVES OUT", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The same law he voted for cuts", True),
        ("$137 billion from rural Medicaid.", True),
        ("The fund replaces about 37%.", True),
        ("", False),
        ("NY hospitals: $8 to $10 billion a", False),
        ("year in losses at full effect (HANYS).", False),
        ("", False),
        ("\"We created\" it: the Senate added", False),
        ("the fund just before passage (KFF).", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 116
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "THE SCALE", size=15, bold=True, fill=NAVY, anchor="mm")
for i, (val, l1, l2) in enumerate([
        ("$76M", "today's post, a slice of", "the December award"),
        ("$212M", "New York's whole first-year", "award, all four initiatives"),
        ("$8 to 10B", "per year: what NY hospitals", "lose under the same law")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 52, val, size=20, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 78, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 96, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "Nine months and three announcements after the award, no NY-23 hospital has been named to receive any of it.",
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "The fund ends in 2030. Sixty-four percent of the Medicaid cuts land after that.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: NY DOH Rural Community Health Integration funding guidance  ·  CMS release, Sept 4 2026  ·  NY DOH and CMS award, Dec 2025", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "KFF, A Closer Look at the $50 Billion Rural Health Fund  ·  HANYS / GNYHA  ·  Fingerlakes1, Sept 4 2026  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rhtp_76m_card.png"), to_desktop=True)
