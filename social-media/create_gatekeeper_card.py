#!/usr/bin/env python3
"""Social card: House Rules Committee gatekeeper pattern, June 9 2026 closed rule.
Claim (his own description of the seat) vs record: ten motions to make an
amendment in order, ten Nay votes, zero allowed (H. Rept. 119-690, RV 357-366),
then he moved to report the rule himself (RV 367, 7-4).
DOCUMENTED PATTERN, matching the published entry. 1080x1080, no em dashes."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, DARK, GREEN, RED, MUTED, WHITE

GREEN_BG, GREEN_LN = "#EBF8F0", "#9AE6B4"
RED_BG,   RED_LN   = "#FFF5F5", "#FEB2B2"
STRIP_BG           = "#EDF2F7"

c = Card()
c.brand_bar()

y = c.badge(62, "DOCUMENTED PATTERN")
y = c.title(y - 6, "He Holds New York's Only Seat", size=32)
y = c.title(y + 4, "on the Committee That Picks the Votes", size=32)
y = c.subtitle(y + 10, "June 9, 2026  ·  H. Res. 1345  ·  House Report 119-690", size=16)
y = c.divider(y + 14)

col_w = (1080 - 44 * 2 - 16) // 2
col_h = 418
lx, rx = 44, 44 + col_w + 16

# ---- LEFT: what he says the seat is for ---------------------------------
c.panel(lx, y, lx + col_w, y + col_h, fill=GREEN_BG, outline=GREEN_LN, radius=8)
cxl = lx + col_w / 2
c.text(cxl, y + 28, "WHAT HE SAYS THE SEAT IS FOR", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(cxl, y + 50, "his own House website", size=14, fill=MUTED, anchor="mm")
c.text(cxl, y + 130, '"a seat at the table', size=25, bold=True, fill=NAVY, anchor="mm")
c.text(cxl, y + 164, 'on major legislation"', size=25, bold=True, fill=NAVY, anchor="mm")
for i, s in enumerate(["The Rules Committee decides which",
                       "amendments the full House may",
                       "even vote on."]):
    c.text(cxl, y + 214 + i * 26, s, size=17, fill=DARK, anchor="mm")
c.text(cxl, y + 322, "1 of 9", size=36, impact=True, fill=NAVY, anchor="mm")
c.text(cxl, y + 356, "majority seats on the committee", size=15, fill=DARK, anchor="mm")
c.text(cxl, y + 388, "and the only New Yorker on it", size=14, fill=MUTED, anchor="mm")

# ---- RIGHT: what the record shows ---------------------------------------
c.panel(rx, y, rx + col_w, y + col_h, fill=RED_BG, outline=RED_LN, radius=8)
cxr = rx + col_w / 2
c.text(cxr, y + 28, "WHAT THE RECORD SHOWS", size=16, bold=True, fill=RED, anchor="mm")
c.text(cxr, y + 50, "one closed rule, four measures", size=14, fill=MUTED, anchor="mm")
c.text(cxr, y + 132, "10", size=104, impact=True, fill=RED, anchor="mm")
c.text(cxr, y + 200, "amendments he voted", size=19, bold=True, fill=DARK, anchor="mm")
c.text(cxr, y + 224, "to keep off the House floor", size=19, bold=True, fill=DARK, anchor="mm")
for i, s in enumerate(["Restore the Medicaid and ACA cuts",
                       "Restore part of the SNAP cuts",
                       "Extend the ACA premium tax credits",
                       "Bar Jan. 6 settlement payments"]):
    c.text(cxr, y + 260 + i * 26, s, size=17, fill=DARK, anchor="mm")
c.text(cxr, y + 374, "and 0 he voted to allow", size=19, bold=True, fill=RED, anchor="mm")
c.text(cxr, y + 400, "Record votes 357 to 366", size=13, fill=MUTED, anchor="mm")
y += col_h + 20

# ---- stat strip ----------------------------------------------------------
strip_h = 146
c.panel(44, y, 1080 - 44, y + strip_h, fill=STRIP_BG, outline=None, radius=8)
c.text(540, y + 26, "THE SAME VOTE ON FIVE UNRELATED FIGHTS", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(540, y + 46, "Medicaid  ·  tariffs  ·  veterans  ·  the Epstein files  ·  ICE and CBP funding",
       size=14, fill=MUTED, anchor="mm")
for cx, big, cap in [(248, "5", "fights, one direction"),
                     (540, "10 of 10", "motions blocked, June 9"),
                     (832, "7 to 4", "his motion to report carried")]:
    c.text(cx, y + 92, big, size=36, impact=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 124, cap, size=15, fill=DARK, anchor="mm")
y += strip_h + 18

# ---- kicker --------------------------------------------------------------
y = c.kicker(y,
             "He sponsored the rule, managed the hour of debate, and moved the previous question.",
             "Both floor votes were party line: 214 to 211, then 213 to 211.")

c.text(540, y + 28, "Sources: House Report 119-690 (committee votes by name)  ·  House Clerk Rolls 210 and 211  ·  Congressional Record H4004-4006",
       size=14, fill=MUTED, anchor="mm")
c.text(540, y + 52, "langworthywatch.org/fact-checks/2026-07-16-rules-committee-gatekeeper-pattern/",
       size=15, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(__file__), "gatekeeper_card.png"), to_desktop=True)
print("saved gatekeeper_card.png")
