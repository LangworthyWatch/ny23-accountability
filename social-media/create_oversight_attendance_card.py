#!/usr/bin/env python3
"""Social card: "I take the Oversight seriously" vs. the committee's attendance and vote record.

Anchored to content/fact-checks/2026-09-10-oversight-seriously-attendance-record.md
(verdict: MISSING CONTEXT).

Hero is the stat: 69 of 145 markup roll calls not voting. Left column is the fair
reading (in DC every day; E&C conflicts; present at the big hearings). Right column
is the record (three whole markups, the 22-21 OBBBA transmittal, 7 of 12 hearings).
Strip carries his own words. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'He Says He Takes "Oversight" Seriously. Here Is the Committee\'s Own Record.', size=26)
y = c.subtitle(y + 6, 'Sept 10, 2026: he cites his Oversight seat to justify probing a Buffalo project. Its own vote sheets, compiled.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 52, "69 of 145", size=40, impact=True, fill=RED, anchor="mm")
c.text(170, y + 94, "markup roll calls: not voting", size=14, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "Every recorded vote at Oversight markups this Congress, per the", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "committee's posted sheets. A blank row means he was not in the room.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "Hearings: present at 7 of the 12 with published transcripts.", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "No proxy voting in committee. He has no Oversight subcommittee seat.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "THE FAIR READING", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("He was in Washington every one of", True),
        ("those days: House floor votes on", True),
        ("each date (Clerk records).", True),
        ("", False),
        ("Energy and Commerce hearings he", False),
        ("sits on started at 10:15 AM on both", False),
        ("2025 days he missed a whole markup.", False),
        ("", False),
        ("He attended the six best-attended", False),
        ("hearings (sanctuary mayors, MN fraud).", False),
        ("", False),
        ("His absence changed no outcome.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "THE RECORD", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Apr 30, 2025: the committee sent its", True),
        ("piece of the OBBBA to Budget, 22 to 21.", True),
        ("His row: blank on all 28 sheets.", True),
        ("", False),
        ("Mar 25, 2025: 0 of 26 roll calls.", False),
        ("Mar 18, 2026: 0 of 9 roll calls.", False),
        ("", False),
        ("Absent at 5 of 12 hearings, incl.", False),
        ("GAO's High Risk List, FDA, AI, and", False),
        ("the 23andMe genetic-privacy hearing.", False),
        ("", False),
        ("Hearing-day subpoena votes: 4 of 7.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "HIS WORDS, SEPT 10 (OFFICIAL PAGE AND WBEN)", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, '"I take the \'Oversight\' in serving on the House Oversight Committee seriously."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, '"Perhaps it\'s because I don\'t represent the city proper... I am a member of the House Oversight Committee."', size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "Two months after the 22-21 committee vote he missed, he voted for the OBBBA on the floor (Roll Call 190).", size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'He told WBEN the housing credits "are for everyone and for every district" and the Southern Tier has "just as big of a housing need."',
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "The committee he invokes is the one whose votes he has missed most often.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: docs.house.gov recorded-vote sheets (161)  ·  govinfo hearing transcripts  ·  House Clerk EVS and MemberData", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "oversight.house.gov task-force rosters  ·  his official Facebook page, Sept 10 2026  ·  Full entry and method at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "oversight_attendance_card.png"), to_desktop=True)
