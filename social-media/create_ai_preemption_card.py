#!/usr/bin/env python3
"""Social card: "50 states writing 50 different sets of rules" vs. his vote for a ten-year ban on state AI laws.

Anchored to the September 2026 update of content/fact-checks/2026-02-state-preemption-pattern.md
(verdict: DOCUMENTED PATTERN).

Hero is the Senate tally that struck the provision he voted for: 99 to 1. Left column is the fair
reading. Right column is his AI record, from official rosters, his own press archive and the
committee calendar. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, '"50 States, 50 Sets of Rules"? He Voted for Zero States, for Ten Years.', size=27)
y = c.subtitle(y + 6, 'Sept 23, 2026: "America needs one clear federal framework" for AI. The record behind it, from his own votes.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 46, "99 to 1", size=44, impact=True, fill=RED, anchor="mm")
c.text(170, y + 88, "the Senate vote that struck", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(170, y + 106, "the provision he voted for", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "May 22, 2025: he voted Yea on the House budget bill whose sec. 43201(c)", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "barred every state from enforcing any AI law for ten years.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "New York's AI safety law would have been unenforceable. The Senate removed", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "the provision on July 1, 2025. Only one senator voted to keep it.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("A bipartisan AI framework bill does", True),
        ("exist, from Reps. Obernolte and", True),
        ("Trahan. Its preemption was narrowed.", True),
        ("", False),
        ("A patchwork of state laws is a real", False),
        ("concern shared across both parties.", False),
        ("", False),
        ("Not every preemption is partisan:", False),
        ("the AM radio bill he cosponsored", False),
        ("has 158 Democrats on it. It is", False),
        ("listed as preemption, not as a jab.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, '"I WORK ON AI POLICY EVERY DAY"', size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("AI bills he has cosponsored this", True),
        ("Congress, by title: none. Last", True),
        ("Congress: two, both joined the same", True),
        ("day in March 2024. Neither passed.", True),
        ("", False),
        ("Press releases, 2023 to now: 397.", False),
        ("Mentioning AI: four, all in passing.", False),
        ("", False),
        ("House AI task force, 2024: 24", False),
        ("members. Not one of them.", False),
        ("His committee's AI hearings in 2026: 1.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "THE PATTERN, NOW EIGHT INSTANCES", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, "Energy Choice Act (NY gas rules) · Supplements Act (NY sales law) · AI letter vs. NY's RAISE Act · SECURE Data Act (NY privacy law)", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, "Ten-year AI ban vote · BUSES Act (NYC idling law) · AM Radio Act (state/local AM rules) · \"one clear federal framework\"", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, 'Sept 4, on the city\'s members wanting local control: "Rules for thee, not for me."', size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "The House sat 377 hours through Aug 31 and voted on 65 days, the fewest of any midterm year since 1994.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, '"Hundreds of hours" on AI: a claim no record we found supports.',
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: H.R. 1 as passed by the House, sec. 43201(c)  ·  House Clerk Roll 145 (May 22 2025)  ·  Senate Commerce Committee, Jul 1 2025  ·  Congressional Record résumé", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Congress.gov cosponsorships (691 bills)  ·  his 397 press releases  ·  docs.house.gov calendar  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai_preemption_card.png"), to_desktop=True)
