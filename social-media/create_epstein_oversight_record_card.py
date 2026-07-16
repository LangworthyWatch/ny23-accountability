#!/usr/bin/env python3
"""Epstein Oversight participation card — who he showed up for vs. stayed out of. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "MISSING CONTEXT")
y = c.title(y, "He Chose Which Epstein Proceedings to Attend", size=27)
y = c.subtitle(y + 8, "On the House Oversight Committee, the pattern is in who he showed up for",
               size=15)
y = c.divider(y + 18)

# --- Panel 1: showed up / acted ---
p1 = y + 16
p1h = 236
c.panel(44, p1, c.w - 44, p1 + p1h)
c.rect(44, p1, c.w - 44, p1 + 44, fill=GREEN, radius=8)
c.rect(44, p1 + 28, c.w - 44, p1 + 44, fill=GREEN)  # square off bottom of header
c.text(74, p1 + 22, "WHERE HE SHOWED UP", size=17, bold=True, fill=WHITE, anchor="lm")
c.bullets(74, p1 + 78, [
    "Questioned Bill Clinton for hours (Feb 27, 2026)",
    "Called Clinton 'quite candid' afterward",
    "Voted yes on the Epstein files bill, after Trump reversed",
    "Says Ghislaine Maxwell should not be pardoned",
], accent=GREEN, step=40, size=16)

# --- Panel 2: stayed out ---
p2 = p1 + p1h + 22
p2h = 178
c.panel(44, p2, c.w - 44, p2 + p2h)
c.rect(44, p2, c.w - 44, p2 + 44, fill=RED, radius=8)
c.rect(44, p2 + 28, c.w - 44, p2 + 44, fill=RED)
c.text(74, p2 + 22, "WHERE HE STAYED OUT", size=17, bold=True, fill=WHITE, anchor="lm")
c.bullets(74, p2 + 78, [
    "No-show for the Wexner deposition, Epstein's billionaire patron",
    "Zero Republicans attended that one",
    "Not among the 5 R votes to subpoena AG Bondi over withheld files",
], accent=RED, step=40, size=16)

c.text(c.w / 2, p2 + p2h + 74, "He can show up when he wants to. He picks his moments.",
       size=18, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, p2 + p2h + 108,
       "As of July 16, 2026, the GOP majority he sits on has still held no survivor hearing.",
       size=15, fill=MUTED, anchor="mm")

c.kicker(c.h - 176,
         "He questioned Bill Clinton for hours and praised his candor.",
         "He skipped the deposition of the man who bankrolled Epstein.")
c.footer_bar()
c.save("social-media/epstein_oversight_record_card.png", to_desktop=True)
