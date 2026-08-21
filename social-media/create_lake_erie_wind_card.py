#!/usr/bin/env python3
"""Social card: "Albany pushes wind turbines in Lake Erie" vs. the record.

Anchored to content/fact-checks/2026-08-19-lake-erie-wind-albany-utility-bills.md
(verdict: MISLEADING). Published Aug 21, 2026.

Hero is the zero: state Lake Erie wind projects. Green left = what is true
(bills are high; concede first). Red right = what the posts blame, checked
against NYSERDA, DPS, DEC, and the Governor's office.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"Albany Pushes Wind Turbines in Lake Erie." Which Project?', size=29)
y = c.subtitle(y + 6, 'Hamburg rally with Bruce Blakeman, Aug 18. Checked against NYSERDA, the PSC, DEC, and the Governor\'s office.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(126, y + 2 + hero_h / 2, "0", size=76, impact=True, fill=RED, anchor="mm")
c.text(196, y + 40, "state Lake Erie wind projects. No solicitation,", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 70, "no application, no plan, per NYSERDA and the Governor.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 100, "The turbines in his photo are on land in Lackawanna. Built 2007.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT IS TRUE", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "bills really are high", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "+81%", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 188, "wholesale natural gas price,", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "January 2026 vs. January 2025.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "NYISO: gas is \"the most significant", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 278, "driver of wholesale electricity costs.\"", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "The fuel the posts want more of", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 338, "is the one that drove the bill.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT THE POSTS BLAME", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, '"radical climate policies out of Albany"', size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 122, "7.7%", size=58, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 188, "of a NYSEG electric bill is", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 214, "climate policy, per the PSC.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 252, "The gas \"choke\" law has never taken", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 278, "effect and covers new buildings only.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 316, "DEC approved a new gas pipeline", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 338, "into NYC in November 2025.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: what got a vote ---------------------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT HE SAYS HE IS FIGHTING FOR, AND WHAT HE VOTED FOR", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([("Energy Choice Act", "no floor vote; silent on delivery", "rates and gas prices"),
                                    ("H.R. 1 (his Aye)", "repealed wind and solar credits:", "est. $78 to $192 per household by 2035"),
                                    ("Data centers", "Blakeman would lift the pause the", "Governor tied to utility bills")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=19, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "Bills are high. The state's own regulator says why.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "It is not Lake Erie, and it is not a law that has never taken effect.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Sources: NYSERDA Great Lakes Wind Feasibility Study  ·  NY DPS Climate Act report, Sept 2025  ·  NYISO", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "NY DEC  ·  Governor's office  ·  House Clerk Roll Call 190  ·  Energy Innovation  ·  Rhodium Group", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lake_erie_wind_card.png"), to_desktop=True)
