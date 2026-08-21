#!/usr/bin/env python3
"""Social card: the CHECK Act post vs. the bill's own record.

Anchored to content/fact-checks/2026-08-11-check-act-price-tags-transparency.md
(verdict: MISSING CONTEXT). Published Aug 21, 2026.

Hero is the zero: cosponsors, and no action since introduction. Green left =
what the bill really does (PBM oversight is real policy; concede first).
Red right = the January vote that actually moved NY-23 premiums.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'A Price Tag Is Not a Price Cut.', size=32)
y = c.subtitle(y + 6, 'His Aug 11 post on the CHECK Act, checked against the bill text, the committee record, and his votes.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(126, y + 2 + hero_h / 2, "0", size=76, impact=True, fill=RED, anchor="mm")
c.text(196, y + 40, "cosponsors, and zero actions since the day", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 70, "he introduced it on June 3, 2026.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 100, "Left off both committee markups that advanced other transparency bills.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT THE BILL REALLY DOES", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "and it is real policy", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "$100,000", size=52, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 188, "per day penalty on middlemen who", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "withhold data from employer plans.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "Plus a 45 day explanation of benefits", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 278, "and an itemized bill before collections.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "PBM oversight matters in a district", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 338, "that has lost independent pharmacies.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT IT DOES NOT DO", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, '"at the doctor\'s office, you should know"', size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 122, "NOTHING", size=48, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 188, "in the bill posts a price", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 214, "before you get care.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 252, "Every duty runs to employers, or to", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 278, "patients after the visit is over.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 316, "Surprise bills were banned in 2022. The", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 338, "gap left, ground ambulance, is not in it.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: the vote that moved premiums --------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT ACTUALLY MOVED NEW YORK PREMIUMS: JANUARY 8, 2026", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([("Nay", "on H.R. 1834, the subsidy extension.", "It passed 230 to 196 without him"),
                                    ("63% to 43%", "share of NY marketplace consumers", "getting financial help, 2025 to 2026"),
                                    ("+$104/mo", "average premium increase for those", "still eligible for help (up 19.5%)")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=22, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "The CHECK Act would tell a Chautauqua County family what their care costs.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "It would not change what they pay for it. The January vote did.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Sources: H.R. 9117 text and BILLSTATUS (govinfo)  ·  E&C hearing record, June 10, 2026  ·  E&C markup releases", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "House Clerk Roll Calls 4, 10, 11  ·  NY State of Health 2026 Coverage Update  ·  Brookings  ·  Health Affairs", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_act_card.png"), to_desktop=True)
