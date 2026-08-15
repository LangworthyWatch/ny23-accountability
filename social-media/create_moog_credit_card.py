#!/usr/bin/env python3
"""Social card: "millions for Moog" vs. the record.

Anchored to content/fact-checks/2026-08-14-moog-defense-credit-claim.md
(verdict: MISSING CONTEXT). NOTE: entry is draft:true with three holds.
DO NOT POST until it publishes - the caption URL would 404.

Hero is the zero: defense or aerospace companies among the 65 funding
requests he has published across four cycles (15+15+15+20, FY24-FY27).
Green left = his real, verified amendment (concede first). Red right =
what the caption claimed, which the rules make structurally impossible.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'A Real Amendment on the Record. Not Money for Moog.', size=29)
y = c.subtitle(y + 6, 'The caption said he "fought to bring home millions for Moog." Checked against the rules he works under.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(126, y + 2 + hero_h / 2, "0", size=76, impact=True, fill=RED, anchor="mm")
c.text(196, y + 40, "defense or aerospace companies among the 65 funding", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 70, "requests he has published across four years.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 100, "House rules BAN earmarks to for-profit companies. Moog is publicly traded.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT IS ON THE RECORD", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "and it is not trivial", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "$7M", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 188, "photonics amendment, bipartisan", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "with Rep. Tim Kennedy (D).", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "Adopted by the House, July 2025.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 278, "Verified at the primary source.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "A transfer between Navy accounts.", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 338, "It names no company.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT THE CAPTION CLAIMED", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, '"bring home millions for Moog"', size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 116, "NO SUCH", size=40, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 162, "ROUTE EXISTS", size=40, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 218, "Moog's federal money is competitively", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 244, "bid contracts, $17M to $43M each.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 270, "No House member awards them.", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 316, "The building he was celebrating is", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 338, "Moog's own $150 million investment.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: his own words -----------------------------------------------
strip_h = 110
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "HIS OWN WORDS THAT DAY, THREE WAYS", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab) in enumerate([("On the record", "his quote in Moog's release makes no funding claim"),
                                ("Second post", '"fight for investments" in programs: defensible'),
                                ("The caption", '"millions for Moog": the claim this checks')]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 58, val, size=19, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 88, lab, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "Advocating for a program account is real work, and he did some. Verified.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "It is not the same thing as bringing home money for a company.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Sources: House Rules Committee  ·  Congressional Record  ·  his published FY24-FY27 request lists", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "House Appropriations CPF guidance  ·  USASpending  ·  Moog and NYS announcements", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "moog_credit_card.png"), to_desktop=True)
