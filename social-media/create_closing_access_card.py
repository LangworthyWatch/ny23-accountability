#!/usr/bin/env python3
"""Closing series 2 of 5: who can reach him, who funds him. Anchored to 2026-10-16-who-funds-him-and-who-can-reach-him
(FEC through Sept 30, 2026), correspondence tracker, tele-town-hall pattern, Oversight attendance entry."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "THE RECORD, 2 OF 5")
y = c.title(y, "Who Can Reach Him. Who Funds Him.", size=30)
y = c.subtitle(y + 6, "His own FEC filings through Sept 30, 2026. The committee's own vote sheets. 26 constituent letters.", size=15)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 430
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 30, "REACHING HIM", size=16, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 96, "0", size=58, impact=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 142, "in-person public town halls", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 164, "since he took office in January 2023", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["26 of 26 constituent letters answered",
                       "with form letters. Two different people,",
                       "two different topics, one reply time:",
                       "12:44 PM, March 11, 2026.",
                       "Tele-town halls: same-day notice,",
                       "recurring postponements."]):
    c.text(lx + col_w / 2, top + 206 + i * 28, t, size=13, bold=(i == 3), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#EDF2F7", outline=BORDER)
c.text(rx + col_w / 2, top + 30, "FUNDING HIM", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 96, "55 cents", size=50, impact=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 142, "of every campaign dollar from PACs", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 164, "$1,201,227 of $2,199,540 this cycle", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["At most 17 cents from donors with",
                       "addresses in his district. Counting only",
                       "ZIP codes entirely inside NY-23: 9 cents.",
                       "",
                       "Donors outside New York gave $259,013.",
                       "ZIPs wholly inside NY-23 gave $194,775."]):
    c.text(rx + col_w / 2, top + 206 + i * 28, t, size=13, bold=(i == 2), fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 132
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 30, "SHOWING UP", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 64, "He says he takes \"the 'Oversight' in Oversight Committee seriously.\" The committee's vote sheets record him absent", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 90, "for 69 of its 145 markup roll calls this Congress. He did not attend its Feb 2026 deposition of Les Wexner.", size=13, fill=DARK, anchor="mm")
y += strip_h + 14

kick_h = 100
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "A representative you cannot question in person, who answers by form letter, and whose money comes from somewhere else.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "That is the record. Every number is his own filing.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: FEC .fec filings, 8 reports through Sept 30, 2026 (memo entries excluded)  ·  Census ZIP-to-district file  ·  Oversight Committee vote sheets  ·  WSKG Apr 2025", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entries at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closing_2_access_card.png"), to_desktop=True)
