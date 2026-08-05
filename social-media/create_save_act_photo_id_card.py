#!/usr/bin/env python3
"""Social card: the 83% photo-ID polling figure vs. what H.R. 22 (SAVE Act) actually requires.

Anchored to content/fact-checks/2026-02-10-save-act-voter-id.md, July 31 2026 update.
Claim-level verdict in that entry: "TRUE, but MISSING CONTEXT" for the 83% figure.
The card concedes the number up front, then shows the documentary-proof requirement.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, GOLD, MUTED, BORDER,
                      WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(62, "MISSING CONTEXT")
y = c.title(y, "The 83% Is Real. The Bill Is Not About Photo ID.", size=29)
y = c.subtitle(y + 6, "He cited the polling. Here is what H.R. 22 actually asks voters to produce.", size=16)
y = c.divider(y + 14)

# ---- two-column contrast -------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 440
lx, rx = 44, 44 + col_w + 16
top = y + 4

# left: what the polling measured
c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 26, "WHAT THE POLLING ASKED", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 48, "Pew, Aug. 4 to 10, 2025, n=3,554", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 132, "PHOTO ID", size=62, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 206, "83% support it. That is accurate.", size=19, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 246, "Republicans 95%. Democrats 71%.", size=16, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 288, "Newest poll splits the question:", size=16, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "Fox, July 17 to 20, 2026", size=15, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 346, "83% to register. 77% to vote.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 396, "Voter ID is genuinely popular.", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 416, "This site said so in February.", size=14, fill=MUTED, anchor="mm")

# right: what the bill requires
c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 26, "WHAT H.R. 22 REQUIRES", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 48, "SAVE Act, House-passed text", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 132, "IN PERSON", size=54, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 206, "Proof of citizenship, delivered", size=19, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 232, "to an election office.", size=19, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 274, "A standard REAL ID does not count.", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 302, "It must show citizenship.", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 340, "Passport, or a photo ID plus a", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 366, "certified birth certificate.", size=16, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 396, "The words married and maiden", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 416, "do not appear in the bill.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 20

# ---- cost and wait strip -------------------------------------------------
strip_h = 152
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 22, "WHAT COMPLIANCE COSTS AND TAKES IN NY-23", size=16, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab, col) in enumerate([
    ("$30", "NY birth certificate, by mail", NAVY),
    ("10 to 12 wks", "standard processing time", RED),
    ("$165", "first-time adult passport", NAVY),
]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 76, val, size=36, impact=True, fill=col, anchor="mm")
    c.text(cx, y + 120, lab, size=14, bold=True, fill=DARK, anchor="mm")
y += strip_h + 20

# ---- kicker --------------------------------------------------------------
kick_h = 104
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 36, "New York issues an Enhanced License that proves citizenship, so many here are covered.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 70, "Most states do not. The polling asked about a card. The bill asks for documents.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 24

c.text(c.w / 2, y, "Sources: Pew Research Center  ·  Fox News Poll  ·  H.R. 22 text (govinfo)", size=15, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 22, "NY DMV  ·  NY Dept. of Health  ·  U.S. Dept. of State", size=15, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_act_photo_id_card.png"),
       to_desktop=True)
