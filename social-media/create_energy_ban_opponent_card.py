#!/usr/bin/env python3
"""Social card: "now you know my opponent supports [the gas and propane ban]" vs. what the opponent said on stage.

Anchored to content/fact-checks/2026-10-15-energy-ban-debate-clips.md (verdict: FALSE; Claim 2 TRUE, Claim 3 MISLEADING).

Hero is a two-word contrast: his post ("SUPPORTS IT") vs. the opponent's own words at the same debate ("NEVER").
Red = the claim, navy = the record (adversarial contrast without a partisan green). The middle panel carries the
rest of the exchange with per-claim verdicts so the TRUE finding is on the card too. Light house style, 1080x1080,
no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, GOLD, ORANGE, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "FALSE")
y = c.title(y, 'His Post: "Now You Know My Opponent Supports" the Ban.', size=27)
y = c.title(y + 2, 'On the Same Stage, His Opponent Said the Opposite.', size=27)
y = c.subtitle(y + 6, "Oct 9, 2026 campaign post about the Oct 6 WETM debate. What the debate video shows.", size=15)
y = c.divider(y + 12)

# ---- hero: two-word contrast -------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 306
lx, rx = 44, 44 + col_w + 16
top = y + 2

c.panel(lx, top, lx + col_w, top + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 28, "HIS CAMPAIGN POST, OCT 9", size=14, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 100, "SUPPORTS IT", size=60, impact=True, fill=RED, anchor="mm")
for i, ln in enumerate([
        '"You already know that Governor',
        "Hochul's natural gas and propane ban",
        "is a dangerous, expensive disaster.",
        'But now you know my opponent',
        'supports it."']):
    c.text(lx + col_w / 2, top + 166 + i * 26, ln, size=15, bold=(i >= 3), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
c.text(rx + col_w / 2, top + 28, "HIS OPPONENT, SAME DEBATE (22:41)", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 100, "NEVER", size=60, impact=True, fill=NAVY, anchor="mm")
for i, ln in enumerate([
        '"I also believe that the state\'s climate',
        'law is too aggressive, and I will never',
        'support things like bans on wood-burning',
        'stoves or propane or no more hookups',
        'for natural gas."']):
    c.text(rx + col_w / 2, top + 166 + i * 26, ln, size=15, bold=(1 <= i <= 3), fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- the rest of the exchange --------------------------------------------------
rows = [
    ("TRUE", GREEN, '"My opponent OPPOSES" the Energy Choice Act (Oct 8 post).',
     "He said so on stage at 21:35. The clip stops seconds before his anti-ban answer."),
    ("MISLEADING", ORANGE, '"He believes that you should be mandated to be in an all-electric home."',
     "No law or proposal we found mandates that. His opponent said the opposite."),
    ("CONTEXT", NAVY, 'What "the ban" is: the All-Electric Buildings Act.',
     "New buildings only; existing homes exempt. Suspended by court order until at least Dec 31, 2026."),
]
row_h = 84
box_h = 40 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 24, "THE REST OF THE EXCHANGE", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (label, color, line1, line2) in enumerate(rows):
    ry = y + 44 + i * row_h
    c.rect(66, ry + 6, 206, ry + 40, fill=color, radius=6)
    c.text(136, ry + 23, label, size=14, bold=True, fill=WHITE, anchor="mm")
    c.text(226, ry + 14, line1, size=15, bold=True, fill=DARK, anchor="lm")
    c.text(226, ry + 38, line2, size=14, fill=DARK, anchor="lm")
y += box_h + 14

# ---- kicker ------------------------------------------------------------------
kick_h = 104
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 33, "Opposing his federal bill is a real disagreement. It is not the same as supporting the state ban.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 68, "His opponent said he will never support the ban. The post says he does.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: WETM debate video, Oct 6, 2026 (21:35-24:29)  ·  Langworthy campaign posts, Oct 8-9  ·  NY Energy Law 11-104  ·  Mulhern Gas v. Mosley stipulation, Nov 2025",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "energy_ban_opponent_card.png"), to_desktop=True)
