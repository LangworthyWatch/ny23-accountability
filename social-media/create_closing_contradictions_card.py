#!/usr/bin/env python3
"""Closing series 4 of 5: what he said, then how he voted. Anchored to Epstein (2025-07-18, 2026-01-14),
Russia sanctions waiver (2026-10-19), Rules tariff blockade (2026-07-03), H.R. 9237 Rules vote (2026-07-03)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "THE RECORD, 4 OF 5")
y = c.title(y, "What He Said. Then How He Voted.", size=30)
y = c.subtitle(y + 6, "Four times the words and the recorded vote point in opposite directions. All from committee reports and his own letters.", size=14)
y = c.divider(y + 12)

rows = [
    ("EPSTEIN FILES",
     '"I have never opposed the release of the documents." (letters, Sept 2025 and March 2026)',
     "July 17, 2025: voted No in the Rules Committee on the binding amendment to force DOJ to release them.",
     "Never signed the discharge petition that forced the vote (218 signatures, Nov 12, 2025)."),
    ("RUSSIA",
     '"Every moment that goes by without severe consequences is a threat to the entire globe." (Feb 24, 2022)',
     "Voted Nay on the $60 billion Ukraine supplemental (Apr 20, 2024). Voted Yea on the 2026 sanctions law",
     "with a presidential waiver. The waiver was used Oct 16, 2026 to set the new sanctions aside."),
    ("TARIFFS",
     'Toured a Jamestown manufacturer to praise "American made." A Jamestown plant\'s insolvency filing named tariffs.',
     "Rules Committee record votes 37, 54, 55: Nay on letting the House vote to end the tariffs.",
     "Floor, Feb 11, 2026, Roll 65: Nay on ending the Canada tariff emergency. It passed 219 to 211."),
    ("VETERANS",
     "Not a cosponsor of H.R. 9237, which paired a popular benefit with cuts to future",
     "sleep-apnea and tinnitus ratings that the VFW and DAV opposed. June 23, 2026, Rules Committee:",
     "voted No on letting the House vote for the benefit without the cuts. Then voted to close the rule."),
]
row_h = 140
for i, (tag, l1, l2, l3) in enumerate(rows):
    top = y + i * (row_h + 8)
    c.panel(44, top, c.w - 44, top + row_h, fill=WHITE if i % 2 else "#FFF5F5", outline="#FEB2B2" if i % 2 == 0 else BORDER)
    c.text(64, top + 28, tag, size=14, bold=True, fill=RED, anchor="lm")
    c.text(64, top + 58, l1, size=12.5, bold=True, fill=DARK, anchor="lm")
    c.text(64, top + 86, l2, size=12.5, fill=DARK, anchor="lm")
    c.text(64, top + 112, l3, size=12.5, fill=DARK, anchor="lm")
y = y + 4 * (row_h + 8) + 8

kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "He holds New York's only seat on the committee that decides what the House may vote on.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 56, "Three times, he used it to keep the vote from happening.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: H. Rept. 119-15, 119-707 committee votes  ·  House Clerk rolls  ·  his constituent letters on file  ·  P.L. 119-111  ·  VFW, DAV statements", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entries at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closing_4_contradictions_card.png"), to_desktop=True)
