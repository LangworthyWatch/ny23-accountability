#!/usr/bin/env python3
"""Social card: the NY Harbor capsizing post vs. the sworn complaint.

Anchored to content/fact-checks/2026-08-20-ny-harbor-capsizing-immigration-framing.md
(verdict: MISSING CONTEXT). NOTE: entry is draft:true pending the office
comment window. DO NOT POST until it publishes - the caption URL would 404.

Hero is the zero: mentions of immigration in the nine-page federal complaint.
Green left = what the complaint alleges (concede first; his safety facts
track it). Red right = what the post adds that no document says.
Tone: restrained. Two people died; the card names no victim.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'The Complaint Is About a License. His Post Is About a Border.', size=29)
y = c.subtitle(y + 6, 'His Aug 20 post on the Liberty Island capsizing, checked against the sworn federal complaint.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(126, y + 2 + hero_h / 2, "0", size=76, impact=True, fill=RED, anchor="mm")
c.text(196, y + 40, "mentions of immigration status in the nine-page", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 70, "federal complaint, the SDNY release, or the charge.", size=18, bold=True, fill=DARK, anchor="lm")
c.text(196, y + 100, "The status claim comes from a DHS press release nine days later.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT THE COMPLAINT ALLEGES", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "his safety facts track it", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "14 on 10", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 188, "people aboard vs. rated capacity.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "No Coast Guard credential.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 252, "No infant life vest. The parents asked;", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 278, "he told them to hold the baby.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 316, "All of it is alleged, not proven.", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 338, "No plea entered. Next court date Sept 9.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT THE POST ADDS", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, "that no charging document says", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 116, "\"RECKLESS\"", size=40, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 162, "is not the charge.", size=32, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 218, "The federal count is misconduct or", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 244, "neglect of a ship officer: negligence.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 270, "The word is not in the complaint.", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 316, "Deaths \"from his illegal endangerment when", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 338, "he had no business being in our country\"", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: what the post leaves out ------------------------------------
strip_h = 118
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHAT THE POST LEAVES OUT", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([("The company", "complaint: no Coast Guard licensure", "found; a boat it chartered burned in 2025"),
                                    ("The precedent", "2022 Hudson drowning: same statute,", "same harbor, no immigration statement"),
                                    ("The fix", "a license, an inspection,", "and an infant life vest")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=19, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "He names the driver's immigration status. He does not name the business that sold the ticket.",
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "Deportation does not license a vessel or put a life jacket on a boat.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 18

c.text(c.w / 2, y, "Sources: U.S. v. Hernandez, 26 MAG 3226 (S.D.N.Y.), sworn complaint  ·  SDNY press release, Aug 10  ·  DHS release, Aug 19", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "Associated Press  ·  NY Department of State  ·  SDNY, U.S. v. Cruz (2022 Hudson River case)", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "harbor_capsizing_card.png"), to_desktop=True)
