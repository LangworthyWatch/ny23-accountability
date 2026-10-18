#!/usr/bin/env python3
"""Social card: "I'm proud to secure $1.4 million" (post) vs. "announced" (his own release) for the Chemung ARC grant.

Anchored to content/fact-checks/2026-10-18-chemung-arc-sewer-credit-claim.md (verdict: MISSING CONTEXT).

Hero is his own two verbs: the Facebook post says SECURE; the press release it links says ANNOUNCED. Red = the claim,
navy = the record. The record rows carry the award process, the no-earmark finding and Schumer's same-day claim; the
fair reading (support letters possible; Schumer claims credit too) is on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, "\"I'm Proud to Secure $1.4 Million\" for Chemung County Sewers.", size=26)
y = c.title(y + 2, "His Own Press Release Says He Announced It.", size=26)
y = c.subtitle(y + 6, "Oct 16, 2026 post on his official page and the Oct 15 release it links. The grant is real.", size=15)
y = c.divider(y + 12)

# ---- hero: his two verbs -------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 236
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 28, "HIS FACEBOOK POST, OCT 16", size=14, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 92, "SECURE", size=62, impact=True, fill=RED, anchor="mm")
for i, ln in enumerate(['"I\'m proud to secure $1.4 million', 'for Chemung County..."', "The post never names the agency", "that awarded it."]):
    c.text(lx + col_w / 2, top + 150 + i * 23, ln, size=14.5, bold=(i < 2), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
c.text(rx + col_w / 2, top + 28, "HIS PRESS RELEASE, OCT 15", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 92, "ANNOUNCED", size=62, impact=True, fill=NAVY, anchor="mm")
for i, ln in enumerate(['"Congressman Nick Langworthy today', 'announced that Chemung County has been', 'awarded a $1.4 million grant from the', 'Appalachian Regional Commission (ARC)..."']):
    c.text(rx + col_w / 2, top + 150 + i * 23, ln, size=14.5, bold=(i >= 2), fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- the record ------------------------------------------------------------------------
rows = [("How it was awarded", "ARC grants start with the state and are reviewed and funded by ARC, a federal-state agency."),
        ("Not an earmark", "His project request lists for 2024 through 2027 include no Chemung sewer project."),
        ("Same-day claim", "Sen. Schumer announced it too and says the money is from the 2021 infrastructure law."),
        ("His role", "His release describes none. We found no support letter (such letters are usually not public).")]
row_h = 54
box_h = 40 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 22, "WHAT THE RECORD SHOWS", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (lab, txt) in enumerate(rows):
    ry = y + 44 + i * row_h
    c.text(66, ry + 14, lab, size=15, bold=True, fill=NAVY, anchor="lm")
    c.text(66, ry + 36, txt, size=14, fill=DARK, anchor="lm")
y += box_h + 12

# ---- fair reading ------------------------------------------------------------------------
fr_h = 100
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate(["Announcing grants is normal, and the sewer upgrade is a real local need.",
                        "Members can write support letters for ARC applications; if he did, that is a real role.",
                        "Sen. Schumer's \"I'm proud to deliver\" is the same kind of claim."]):
    c.text(c.w / 2, y + 48 + i * 22, ln, size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 27, "$1.4 million from ARC, plus $1.4 million in state money, for a $2.8 million project.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 57, "Good news for Chemung County. \"Secure\" is a bigger claim than the record supports.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 12

c.text(c.w / 2, y, "Sources: Langworthy release, Oct 15, 2026  ·  Schumer release, Oct 15, 2026  ·  ARC  ·  Southern Tier Central Regional Planning Board  ·  his FY24-27 project requests",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chemung_arc_card.png"), to_desktop=True)
