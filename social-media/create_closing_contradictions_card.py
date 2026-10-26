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
y = c.subtitle(y + 6, "Thirteen members of the Rules Committee decide what reaches the House floor. He is the only New Yorker on it.", size=14)
y = c.divider(y + 12)

rows = [
    ("EPSTEIN FILES",
     'Wrote to constituents, twice: "I have never opposed the release of the documents."',
     "July 2025: voted in committee to block the amendment forcing their release.",
     "Never signed the petition that finally forced the vote."),
    ("TARIFFS",
     "A Jamestown furniture plant closed and named tariffs in its filing.",
     "Three committee votes to keep the House from voting on ending the tariffs.",
     "When the floor vote finally came, Feb 11, 2026: voted to keep them."),
    ("VETERANS",
     "A veterans bill paired a popular benefit with disability-rating cuts the VFW and DAV opposed.",
     "June 2026: voted in committee against letting the House pass the benefit without the cuts.",
     "Then voted to close the rule."),
]
row_h = 212
for i, (tag, l1, l2, l3) in enumerate(rows):
    top = y + i * (row_h + 10)
    c.panel(44, top, c.w - 44, top + row_h, fill="#FFF5F5" if i % 2 == 0 else WHITE, outline="#FEB2B2" if i % 2 == 0 else BORDER)
    c.text(64, top + 40, tag, size=16, bold=True, fill=RED, anchor="lm")
    c.text(64, top + 84, l1, size=15, bold=True, fill=DARK, anchor="lm")
    c.text(64, top + 122, l2, size=15, fill=DARK, anchor="lm")
    c.text(64, top + 158, l3, size=15, fill=DARK, anchor="lm")
y = y + 3 * (row_h + 10) + 8

kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "He holds New York's only seat on the committee that decides what the House may vote on.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 56, "Three times, he used it to keep the vote from happening.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: Rules Committee reports (votes recorded by name)  ·  House Clerk Roll 65  ·  his constituent letters on file  ·  VFW and DAV statements", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entries at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closing_4_contradictions_card.png"), to_desktop=True)
