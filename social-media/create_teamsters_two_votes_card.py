#!/usr/bin/env python3
"""Social card: the two votes behind the Teamsters endorsement.

Anchored to content/fact-checks/2026-08-28-teamsters-endorsement-labor-record.md
(verdict: MISSING CONTEXT). Published Aug 28, 2026.

Hero is the sequence: Nay on the rule at 5:30, Yea on the bill at 7:05, the same
day. Green left = the bill vote, which is real and cost him something (concede
first). Red right = the rule vote, which is the one that decided whether the
bill could be considered at all.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'Two Votes on the Teamsters Bill. Ninety Minutes Apart.', size=31)
y = c.subtitle(y + 6, 'He says the endorsement recognized "a record of results." Here is the record, June 9, 2026.', size=15)
y = c.divider(y + 12)

# ---- hero: the two votes ------------------------------------------------
hero_h = 126
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
mid = c.w / 2
c.text(mid - 250, y + 44, "5:30 PM", size=20, bold=True, fill=MUTED, anchor="mm")
c.text(mid - 250, y + 92, "NAY", size=54, impact=True, fill=RED, anchor="mm")
c.text(mid - 92, y + 44, "on the rule that let the bill", size=15, bold=True, fill=DARK, anchor="lm")
c.text(mid - 92, y + 68, "be considered at all.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(mid - 92, y + 100, "It passed 221 to 201 only because eleven", size=13, fill=MUTED, anchor="lm")
c.text(mid - 92, y + 118, "Republicans crossed over. He was not one.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 330
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "THEN, AT 7:05 PM", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 54, "and this vote is real", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 112, "YEA", size=56, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 168, "on the bill itself, one of only", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 194, "20 Republicans out of 212.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 232, "He broke with his conference", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 258, "to cast it. That is not free.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 296, "Two of the five endorsed Republicans", size=13, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 316, "voted for the rule as well.", size=13, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHY THE RULE VOTE MATTERED", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 54, "it was the one that decided", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 108, "NO RULE,", size=40, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 152, "NO BILL VOTE", size=40, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 200, "Had the rule failed, there would", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 226, "have been nothing to vote on.", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 264, "It had to be pried out of the Rules", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 284, "Committee, where he sits, by a", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 304, "discharge petition.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT ELSE THE ENDORSEMENT POST LEAVES OUT", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([
        ("One bill", "the Teamsters called it a \"litmus test\"", "and said every endorsee passed it"),
        ("$0", "in Teamsters PAC money to him", "across 2022, 2024 and 2026"),
        ("0 of 358", "measures he has sponsored or cosponsored", "is a trucking or driver bill")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=21, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 30, "He did vote for the bill, and it cost him something with his own party.",
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 62, "He also voted against letting it reach the floor.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: House Clerk Roll Calls 215 and 216, June 9, 2026  ·  H. Res. 1140 and H.R. 5408 BILLSTATUS (govinfo)", size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 19, "FEC bulk files itpas2 and cm, 2022 to 2026  ·  Teamsters Joint Council 16  ·  WETM", size=12, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "teamsters_two_votes_card.png"), to_desktop=True)
