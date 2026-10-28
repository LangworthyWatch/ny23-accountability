#!/usr/bin/env python3
"""Epstein / Oversight, Oct 28, 2026 update to 2026-01-14-epstein-files-discharge-petition (MISSING CONTEXT).
Every figure is from the committee's transcripts, its Sept 15 vote sheet and transcript, the Clerk, govinfo and his press index."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  UPDATED OCT 28, 2026")
y = c.title(y, "The Epstein Investigation Kept Going.", size=30)
y = c.title(y - 8, "He Kept Not Being in the Room.", size=30)
y = c.subtitle(y + 6, "He sits on the House Oversight Committee. Its own transcripts and vote sheets, July through October 2026.", size=15)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 392
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 30, "WITNESS INTERVIEWS", size=16, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 98, "1 of 12", size=58, impact=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 144, "attendance rosters list him", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 166, "Aug 2025 to Jul 2026, per the transcripts", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["Present for Bill Clinton (Feb 27).",
                       "Not listed for Barr, Waitt, Noel, Bondi,",
                       "Lutnick, Gates, Groff, Leon Black,",
                       "Doug Band, Ruemmler or Jes Staley.",
                       "Four more rosters released since July. None."]):
    c.text(lx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 4), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#EDF2F7", outline=BORDER)
c.text(rx + col_w / 2, top + 30, "THE ONE ENFORCEMENT VOTE", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 98, "No response", size=44, impact=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 144, "Sept 15: hold Leon Black in contempt", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 166, "Committee vote 41 to 0. His row: blank.", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["\"The Clerk. Mr. Langworthy? [No response.]\"",
                       "Same afternoon, the House Clerk records",
                       "him on floor votes at 4:46, 4:54 and 5:27.",
                       "The markup ran 5:12 to 5:32.",
                       "The next day the full House agreed, no roll call."]):
    c.text(rx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 0), fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 176
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 32, "WHAT HE HAS SAID ABOUT ANY OF IT", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 68, "His chairman, Sept 3: \"I've asked Blanche numerous times to come in.\" The Attorney General still has not.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 98, "Not a cosponsor of the chairman's Epstein survivor bill (4 Republicans are). No public hearing for survivors yet.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 134, "70 press releases since Aug 2025, the Oct 6 debate, the Sept 1 tele-town hall: not one word on Epstein.", size=13.5, bold=True, fill=RED, anchor="mm")
y += strip_h + 14

kick_h = 118
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 38, "Five other Republicans also missed the contempt vote, and no member attends every interview. This is not one absence.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 76, "It is fifteen months, twelve rosters, one vote sheet, and silence.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: Oversight Committee transcripts (Present lists)  ·  Sept 15, 2026 vote sheet and markup transcript (docs.house.gov)  ·  House Clerk roll calls 298-307  ·  govinfo H.R. 10389  ·  Politico Sept 3", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-01-14-epstein-files-discharge-petition/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "epstein_oversight_card.png"), to_desktop=True)
