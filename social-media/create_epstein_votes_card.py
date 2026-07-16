#!/usr/bin/env python3
"""Epstein VOTES card — procedural blocking votes vs. final passage. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "MISSING CONTEXT")
y = c.title(y, "His Epstein Votes: Block the Binding Path,", size=27)
y = c.title(y + 34, "Then Vote Yes on Final Passage", size=27)
y = c.subtitle(y + 12, "He sits on the Rules Committee, which decides what reaches the floor",
               size=15)
y = c.divider(y + 18)

# --- Panel 1: the blocking votes ---
p1 = y + 16
p1h = 250
c.panel(44, p1, c.w - 44, p1 + p1h)
c.rect(44, p1, c.w - 44, p1 + 44, fill=RED, radius=8)
c.rect(44, p1 + 28, c.w - 44, p1 + 44, fill=RED)
c.text(74, p1 + 22, "VOTES THAT BLOCKED THE BINDING PATH", size=17, bold=True,
       fill=WHITE, anchor="lm")
c.bullets(74, p1 + 80, [
    "Jul 14, 2025: NO on the amendment to force file release (Rules Cmte)",
    "Jul 15, 2025: YES on previous question, foreclosing a floor vote (RC 194)",
    "Sep 2, 2025: NO on motions to force the bill up (Rules Cmte)",
    "Nov 18, 2025: YES on the rule that tabled the discharge petition",
], accent=RED, step=44, size=15)

# --- Panel 2: final passage ---
p2 = p1 + p1h + 22
p2h = 128
c.panel(44, p2, c.w - 44, p2 + p2h)
c.rect(44, p2, c.w - 44, p2 + 44, fill=GREEN, radius=8)
c.rect(44, p2 + 28, c.w - 44, p2 + 44, fill=GREEN)
c.text(74, p2 + 22, "THEN, FINAL PASSAGE", size=17, bold=True, fill=WHITE, anchor="lm")
c.bullets(74, p2 + 84, [
    "Nov 18, 2025: YES on H.R. 4405, after Trump reversed (RC 289, 427 to 1)",
], accent=GREEN, step=44, size=15)

c.text(c.w / 2, p2 + p2h + 52,
       "Every roll call above is confirmed from the House Clerk's records.",
       size=15, fill=MUTED, anchor="mm")

c.kicker(c.h - 176,
         "He never voted against releasing the files.",
         "He voted against every binding step that would have forced them out sooner.")
c.footer_bar()
c.save("social-media/epstein_votes_card.png", to_desktop=True)
