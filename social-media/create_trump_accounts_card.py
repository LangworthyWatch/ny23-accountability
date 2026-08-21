#!/usr/bin/env python3
"""Social card: "accounts for every American child" vs. the statute.

Anchored to content/fact-checks/2026-08-20-trump-accounts-every-child.md
(verdict: MISSING CONTEXT). Published Aug 21, 2026.

Hero is the share: about 1 in 5 NY-23 minors get the $1,000 by end-2028
(about 1 in 14 on the day of the post). Green left = what is true (the
account really is open to nearly every child; concede first). Red right =
the $1,000 eligibility the post leaves out.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Accounts for Every American Child." The $1,000 Is Not for Every Child.', size=28)
y = c.subtitle(y + 6, 'His Aug 20 post linking trumpaccounts.gov, checked against the law he voted for (P.L. 119-21, Sec. 70204).', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(150, y + 2 + hero_h / 2, "1 in 5", size=64, impact=True, fill=RED, anchor="mm")
c.text(270, y + 40, "NY-23 children will qualify for the $1,000 deposit", size=18, bold=True, fill=DARK, anchor="lm")
c.text(270, y + 70, "by the end of 2028. On the day he posted: about 1 in 14.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(270, y + 100, "NY DOH births and Census 2024 under-18 counts, seven whole NY-23 counties.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT IS TRUE", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "the account itself", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "Under 18", size=52, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 188, "with a Social Security number:", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "nearly every child can open one.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "Live since July 4, 2026.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 278, "About 7 million signed up nationally.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "Created by H.R. 1. He voted Aye,", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 338, "Roll Call 190, July 3, 2025.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT THE POST LEAVES OUT", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, "the $1,000 \"jump start\"", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 122, "2025 to 2028", size=44, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 188, "birth years only. U.S. citizens only.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 214, "Parent must file Form 4547.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 252, "Born in 2024? Account, no deposit.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 278, "Born in 2029? Same.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 316, "Earnings taxed as ordinary income", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 338, "on withdrawal, unlike a 529.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: wealthy family ----------------------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "\"YOU SHOULDN'T HAVE TO BE BORN INTO A WEALTHY FAMILY\"", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([("$5,839", "the $1,000 alone at 18,", "at the 10.3% return the site advertises"),
                                    ("$303,757", "if a family also deposits the", "$5,000 maximum every year"),
                                    ("7% vs 1%", "bottom- vs top-quintile children left", "without accounts under opt-in (Urban)")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=22, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "The account is real and nearly universal. The deposit is the pitch.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "Four birth years, citizens only, and a form. The post mentions none of it.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Sources: P.L. 119-21 Sec. 70204 (govinfo)  ·  IRS Form 4547 and IR-2026-42  ·  JCT JCX-35-25  ·  FactCheck.org, July 2026", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "Urban Institute, Jan and July 2026  ·  NY DOH Vital Statistics 2023  ·  Census Bureau Vintage 2024  ·  House Clerk Roll Call 190", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "trump_accounts_card.png"), to_desktop=True)
