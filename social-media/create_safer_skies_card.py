#!/usr/bin/env python3
"""Social card: "pass my Safer Skies Act" after the Flydubai cockpit attack vs. what H.R. 2353 actually does.

Anchored to content/fact-checks/2026-09-30-safer-skies-act-flydubai.md (verdict: MISLEADING).

Hero is the mismatch in one line. Left column is the fair reading. Right column is the bill's text and
status. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"Pass My Safer Skies Act." The Attacker Was the Pilot. His Bill Screens Passengers.', size=27)
y = c.subtitle(y + 6, 'Sept 30, 2026: his post on the Flydubai cockpit stabbing, and what H.R. 2353 says in its own text.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 46, "0 provisions", size=40, impact=True, fill=RED, anchor="mm")
c.text(170, y + 88, "in his bill about pilots,", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(170, y + 106, "crew or cockpit access", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, 'His post: "pass my Safer Skies Act to ensure our planes can never', size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, 'again be used as a weapon of terror."', size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "The event: a Flydubai pilot stabbed his co-pilot at the controls, Dubai to", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "Tel Aviv. Passengers stormed the cockpit. 174 aboard. 14,125 feet in 29 seconds.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 352
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The loophole his bill closes is real:", True),
        ("scheduled charters that sell seats", True),
        ("and skip TSA checkpoints.", True),
        ("", False),
        ("It is bipartisan: 52 cosponsors,", False),
        ("26 Republicans and 26 Democrats.", False),
        ("He chairs the Aviation Safety Caucus.", False),
        ("", False),
        ('"Terrorist attack" tracks what', False),
        ("Israel's defense minister said that", False),
        ("morning, without details.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT H.R. 2353 ACTUALLY DOES", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Puts U.S. public-charter passengers", True),
        ("through TSA checkpoint screening.", True),
        ("That is the whole bill.", True),
        ("", False),
        ("Nothing on pilots, crew vetting,", False),
        ("cockpit access or foreign carriers.", False),
        ("", False),
        ("Referred to a Homeland Security", False),
        ("subcommittee Mar 26, 2025.", False),
        ("No hearing, no markup, in 18 months.", False),
        ("House is out until Nov 9.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "THE MOTIVE, AS OF THE DAY HE POSTED", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, 'Flydubai: "the underlying reasons and motives behind this event are unknown and remain subject to a formal investigation."', size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, 'Israel\'s PM spokesperson: "there is a strong opinion" it was terror, "but we can\'t be sure until we debrief everybody."', size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, 'Aviation security consultant Philip Baum: "the insider threat is probably the greatest threat to civil aviation nowadays."', size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "The danger came from inside the cockpit. His bill is about the line passengers stand in before a charter flight.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "A real bill for a real gap. Not the gap on that plane.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: H.R. 2353 text and status (govinfo)  ·  his Aug 5 2024 release  ·  NBC, NPR, Al Jazeera, CBC, Sept 30 2026  ·  Flightradar24 via NBC", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "safer_skies_card.png"), to_desktop=True)
