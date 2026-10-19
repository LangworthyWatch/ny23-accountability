#!/usr/bin/env python3
"""Social card: his 2022 "severe consequences" statement vs. the Oct 16, 2026 waiver under the sanctions law he voted for.

Anchored to content/fact-checks/2026-10-19-russia-ukraine-record-sanctions-waiver.md (verdict: DOCUMENTED PATTERN).

Hero: his words (2022) vs. the event (2026). Navy for his words, red for the record. Middle: his votes and his public
record since June 2024. Fair reading on the card; Starshield labeled as reports with denials. 1080x1080, no em dashes.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, "2022: \"Every Moment... Without Severe Consequences Is a Threat.\"", size=24)
y = c.title(y + 2, "2026: The Sanctions Law He Voted For Was Just Waived.", size=26)
y = c.subtitle(y + 6, "His statements and House votes, 2022-2026, beside the October 16, 2026 waiver.", size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 230
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
c.text(lx + col_w / 2, top + 26, "HIS WORDS, FEB 24, 2022", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(lx + col_w / 2, top + 84, "\"SEVERE", size=50, impact=True, fill=NAVY, anchor="mm")
c.text(lx + col_w / 2, top + 134, "CONSEQUENCES\"", size=40, impact=True, fill=NAVY, anchor="mm")
for i, ln in enumerate(['"every moment that goes by without severe', 'consequences is a threat to the entire globe"']):
    c.text(lx + col_w / 2, top + 178 + i * 22, ln, size=13.5, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 26, "OCTOBER 16, 2026", size=14, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 106, "WAIVED", size=72, impact=True, fill=RED, anchor="mm")
for i, ln in enumerate(["The President waived the 2026 law's tariffs and", "nearly all its other Russia sanctions provisions."]):
    c.text(rx + col_w / 2, top + 178 + i * 22, ln, size=13.5, bold=(i == 0), fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- the record -------------------------------------------------------------------------------
rows = [("Voted for the law", "Yea on the 2026 sanctions law. Its Section 115 lets the President waive it with a written certification."),
        ("No recorded vote on narrowing it", "He recorded no votes at the Sept 14 Rules Committee meeting on the bill."),
        ("Ukraine aid votes", "Nay on the 2023 and 2024 aid bills and the 2026 Ukraine Support Act."),
        ("Since June 2024", "No press release on Russia or Ukraine, and none we found on the waiver.")]
row_h = 52
box_h = 40 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 22, "HIS RECORD", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (lab, txt) in enumerate(rows):
    ry = y + 42 + i * row_h
    c.text(66, ry + 14, lab, size=15, bold=True, fill=NAVY, anchor="lm")
    c.text(66, ry + 36, txt, size=13.5, fill=DARK, anchor="lm")
y += box_h + 12

# ---- fair reading ---------------------------------------------------------------------------------
fr_h = 120
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate(["He opposed the 2024 aid bill over non-military spending, a forgivable loan and other concerns.",
                        "The 2022 statement came as party chair, criticizing a president of the other party.",
                        "Reports that the White House limited Ukraine's satellite access are denied by the administration.",
                        "Four GOP senators asked the Pentagon's inspector general to investigate."]):
    c.text(c.w / 2, y + 46 + i * 21, ln, size=13, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------------
kick_h = 80
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "2022: \"Biden's weakness.\" 2023: \"American weakness invites aggression.\"", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 54, "2026: no public word we could find on the waiver.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: House Clerk roll calls  ·  P.L. 119-111  ·  H. Rept. 119-825  ·  White House order, Oct 16, 2026  ·  his statements and newsletter  ·  Reuters  ·  The Hill",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "russia_waiver_card.png"), to_desktop=True)
