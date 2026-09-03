#!/usr/bin/env python3
"""Social card: three law-and-order posts vs the withheld HSGP money.

Anchored to content/fact-checks/2026-09-03-law-and-order-posts-withheld-hsgp-funding.md
(verdict: MISSING CONTEXT). Published Sept 3, 2026.

Hero is the $87M still withheld. Green left concedes first (expo did go on,
the withholding is executive action, not his). Red right is what the posts
leave out. All figures from the Sept 30, 2025 and Sept 1, 2026 Hochul
releases, the NY AG's D.R.I. case release, and the NYS Comptroller.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'Three Law and Order Posts. Zero Words on the Withheld Police Money.', size=30)
y = c.subtitle(y + 6, 'Aug 26 to 28, 2026. He says sheriffs "should be supported." Here is the funding record.', size=15)
y = c.divider(y + 12)

# ---- hero: the withheld money -------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(196, y + 62, "$87M", size=58, impact=True, fill=RED, anchor="mm")
c.text(340, y + 30, "in FY2025 counterterrorism and police grants is still", size=15, bold=True, fill=DARK, anchor="lm")
c.text(340, y + 54, "withheld from New York, almost a year after the", size=15, bold=True, fill=DARK, anchor="lm")
c.text(340, y + 78, 'President posted that he had "reversed the cuts."', size=15, bold=True, fill=DARK, anchor="lm")
c.text(340, y + 102, "The $100M that did arrive followed a federal court order.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 322
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, line in enumerate([
        ("The DHS job expo he defended", True),
        ("really did go on, relocated to the", True),
        ("Coast Guard base, Sept 1 and 2.", True),
        ("", False),
        ("The state AG dispute he posted", False),
        ("about is a real policy fight.", False),
        ("", False),
        ("The withholding is the executive", False),
        ("branch's action, not a House vote.", False),
        ("There was no delegation letter", False),
        ("he refused to sign.", False)]):
    txt, bold = line
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE POSTS LEAVE OUT", size=16, bold=True, fill=RED, anchor="mm")
for i, line in enumerate([
        ("SHSP, the grant that equips county", True),
        ("sheriffs and police in every NY", True),
        ("county, was cut 90.8 percent:", True),
        ("$61.2M down to $5.6M.", True),
        ("", False),
        ("All eight NY-23 counties get it.", False),
        ("", False),
        ("A 12-state lawsuit and a December", False),
        ("court order forced the partial", False),
        ("restoration. $17.7M of the sheriff", False),
        ("and police money is still missing.", False)]):
    txt, bold = line
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 116
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT WE FOUND, AND DID NOT FIND", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([
        ("3 posts", "on law and order in three days,", "campaign and official pages"),
        ("3 colleagues", "publicly pressed the administration:", "Malliotakis, Lawler, Garbarino"),
        ("0 statements", "from him on the cuts located in his", "press archive or either FB page")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 52, val, size=20, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 78, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 96, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'His Aug 26 post: "Our sheriffs are on the frontlines... they should be supported."',
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "The sheriff grant program is owed $17.7 million. He has not mentioned it.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: Gov. Hochul releases, Sept 30 2025 and Sept 1 2026  ·  NY AG, D.R.I. summary judgment Dec 2025  ·  NYS Comptroller", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "WKBW  ·  House Clerk Roll 190  ·  Full timeline and sources at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "law_and_order_hsgp_card.png"), to_desktop=True)
