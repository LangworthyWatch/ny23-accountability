#!/usr/bin/env python3
"""Social card: H.R. 7008's coverage scope vs. the poll Langworthy cites.

Anchored to content/fact-checks/2026-07-21-stock-trading-ban-sell-loophole.md
(published verdict: MISLEADING; August 2026 update).

Hero stat is the zero: "President", "Vice President" and "executive branch"
appear zero times in the House-passed text (BILLS-119hr7008eh, verified).
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(60, "MISLEADING")
y = c.title(y, "The Stock Ban He Passed Stops at Congress", size=31)
y = c.subtitle(y + 6, "It reaches Members, spouses and dependent children. That is the whole list.", size=16)
y = c.divider(y + 12)

# ---- hero stat -----------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(126, y + 2 + hero_h / 2, "0", size=78, impact=True, fill=RED, anchor="mm")
c.text(196, y + 38, "times the words President, Vice President, or", size=19, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 68, "executive branch appear in the bill's text.", size=19, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 98, "Searched in the House-passed version, BILLS-119hr7008eh.", size=14, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two-column contrast -------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT THE POLL ASKED", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 116, "86%", size=64, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 186, "favor prohibiting Members from", size=17, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 212, "TRADING individual stocks.", size=17, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "R 87%  ·  D 88%  ·  I 81%", size=16, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 302, "This is his own graphic.", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 326, "The number is accurate.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE BILL DOES", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 96, "BUYING: BANNED", size=30, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 144, "SELLING: ALLOWED", size=30, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 196, "Sales permitted with 7 to 14 days", size=17, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 222, "advance public notice.", size=17, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 258, "That notice is a real constraint.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 302, "It is not the prohibition", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 326, "the 86% were asked about.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- passage strip -------------------------------------------------------
strip_h = 108
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 26, "IT DID PASS THE HOUSE. HE IS RIGHT ABOUT THAT.", size=16, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab) in enumerate([("232-198", "House passage, July 22, 2026"),
                                ("Roll Call 280", "Langworthy voted yes"),
                                ("Senate", "where it sits now")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 60, val, size=26, impact=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 90, lab, size=13, bold=True, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker --------------------------------------------------------------
kick_h = 106
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 36, "A Cabinet secretary could buy and sell individual stocks the day this became law.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 72, "Nothing in the bill would touch them.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 20

c.text(c.w / 2, y, "Sources: H.R. 7008 as passed by the House (govinfo)  ·  House Roll Call 280", size=14, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "Poll figures from the graphic in his own August 4 post", size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stock_ban_scope_card.png"),
       to_desktop=True)
