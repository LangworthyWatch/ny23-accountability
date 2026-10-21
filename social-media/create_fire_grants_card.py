#!/usr/bin/env python3
"""Social card: "proud to have helped secure" two FEMA fire grants (Olean radios, Ellicottville air packs).

Anchored to content/fact-checks/2026-10-22-olean-ellicottville-fire-grants.md (verdict: MOSTLY TRUE).

Mostly-true layout: the two grants as navy stat tiles, then what holds up (navy) beside what the posts leave out
(red), then who chose the winners (gold), kicker. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MOSTLY TRUE")
y = c.title(y, '"Proud to Have Helped Secure" Two Fire Grants.', size=28)
y = c.title(y + 4, '"Helped" Holds Up. Here Is What the Posts Leave Out.', size=21, fill=DARK)
y = c.subtitle(y + 6, "Two October 2026 posts on his official page, beside FEMA and federal award records.", size=14)
y = c.divider(y + 12)

# ---- two grants -------------------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 206
lx, rx = 44, 44 + col_w + 16
top = y + 2
for x0, label, big, l1, l2 in [
    (lx, "OLEAN FIRE: RADIOS", "$70,714", "FEMA firefighter grant", "Fiscal 2025 round, announced Sept 2026"),
    (rx, "ELLICOTTVILLE FIRE: AIR PACKS", "$212,992", "FEMA firefighter grant", "Fiscal 2024 round, award period began Sept 30, 2025"),
]:
    c.panel(x0, top, x0 + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
    c.text(x0 + col_w / 2, top + 26, label, size=14, bold=True, fill=NAVY, anchor="mm")
    c.text(x0 + col_w / 2, top + 94, big, size=60, impact=True, fill=NAVY, anchor="mm")
    c.text(x0 + col_w / 2, top + 150, l1, size=15, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + col_w / 2, top + 176, l2, size=13.5, fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- holds up vs left out -------------------------------------------------------------------
col_h = 272
c.panel(lx, y, lx + col_w, y + col_h, fill=WHITE, outline="#A3BFD9")
c.text(lx + col_w / 2, y + 26, "WHAT HOLDS UP", size=15, bold=True, fill=NAVY, anchor="mm")
for i, ln in enumerate(["The amounts match the records.", "",
                        "He voted for the spending laws", "that funded both grant rounds.", "",
                        "His office has hosted FEMA", "grant-writing seminars for", "local departments."]):
    c.text(lx + col_w / 2, y + 66 + i * 24, ln, size=14, bold=(i in (0, 2, 5)), fill=DARK, anchor="mm")
c.panel(rx, y, rx + col_w, y + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, y + 26, "WHAT THE POSTS LEAVE OUT", size=15, bold=True, fill=RED, anchor="mm")
for i, ln in enumerate(["How the winners were chosen:", "FEMA scored applications;", "Congress has no role.", "",
                        "The Ellicottville grant's award", "period began in Sept 2025.", "",
                        "Olean also moved to apply for", "a fire engine; we found no award."]):
    c.text(rx + col_w / 2, y + 62 + i * 23, ln, size=14, bold=(i in (0, 4, 7)), fill=DARK, anchor="mm")
y += col_h + 12

# ---- who chose ------------------------------------------------------------------------------
fr_h = 104
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "WHO PICKED THE WINNERS", size=14, bold=True, fill="#744210", anchor="mm")
c.text(c.w / 2, y + 54, "The departments wrote the applications. FEMA scored them by computer, then panels", size=13.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 78, "of fire-service reviewers scored the top ones. The process gives Congress no role.", size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 27, "Not earmarks: neither grant is in his Community Project Funding requests.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 57, '"Helped secure" fits the record. "Secured" would not.', size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: FEMA AFG notices, FY2024 and FY2025  ·  USAspending.gov  ·  City of Olean, June 23, 2026  ·  House Clerk  ·  his releases",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fire_grants_card.png"), to_desktop=True)
