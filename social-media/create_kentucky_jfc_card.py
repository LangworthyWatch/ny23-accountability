#!/usr/bin/env python3
"""Kentucky nursing-home joint fundraising committee, entry 2026-10-31-kentucky-nursing-home-joint-fundraising-committee
(DOCUMENTED PATTERN). Figures from FEC files 1932018 (F1), 1957130 (termination report), 1961860 (LfC Q1 2026),
CMS Care Compare Oct 2026; retained under research/sources/prospect-nursing-home-2026-10-30/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN  ·  NOV 2, 2026")
y = c.title(y, "One Day. One Address. $150,800.", size=31)
y = c.title(y - 2, "The Fundraising Committee That Lived Eleven Weeks.", size=29)
y = c.subtitle(y + 6, "Langworthy Leadership & Accountability Fund (FEC C00934109): his campaign, the chairmen of Energy and Commerce and Oversight, their PACs, and the NRCC.", size=13)
y = c.divider(y + 12)

# Timeline strip
tl_h = 78
c.panel(44, y, c.w - 44, y + tl_h, fill=WHITE, outline=BORDER)
steps = [("JAN 12", "formed"), ("JAN, FEB", "$0 raised"), ("MAR 19", "$150,800 in"), ("MAR 30", "split seven ways"), ("APR 1", "terminated")]
sw = (c.w - 88) / len(steps)
c.rect(44 + sw / 2, y + 30, c.w - 44 - sw / 2, y + 32, fill=BORDER, outline=None)
for i, (d, lab) in enumerate(steps):
    cx = 44 + sw * i + sw / 2
    col = RED if i == 2 else NAVY
    c.rect(cx - 7, y + 24, cx + 7, y + 38, fill=col, outline=None)
    c.text(cx, y + 52, d, size=12.5, bold=True, fill=col, anchor="mm")
    c.text(cx, y + 68, lab, size=11, fill=MUTED, anchor="mm")
y += tl_h + 14

# Flow: in -> out
col_w = (c.w - 44 * 2 - 70) // 2
col_h = 340
lx = 44
rx = c.w - 44 - col_w
top = y
c.panel(lx, top, lx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 28, "IN: MARCH 19, 2026", size=15, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 84, "$150,800", size=52, impact=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 124, "every dollar from one address:", size=13, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 144, "300 Provider Court, Richmond, Kentucky", size=12.5, fill=MUTED, anchor="mm")
donors = [("Woodland Oaks Operations LLC", "$75,000"), ("Klondike Nursing & Rehabilitation", "$50,000"),
          ("Berea, Cambridge, Cumberland, Dover Manor LLCs, $6,000 each", "$24,000"),
          ("in-kind, a Fla. nursing-home manager", "$1,800")]
for i, (n, a) in enumerate(donors):
    ry = top + 180 + i * 30
    c.text(lx + 22, ry, n, size=12, fill=DARK, anchor="lm")
    c.text(lx + col_w - 22, ry, a, size=12.5, bold=True, fill=DARK, anchor="rm")
c.text(lx + col_w / 2, top + col_h - 18, "Six Kentucky nursing-home operating companies.", size=11.5, bold=True, fill=RED, anchor="mm")

# arrow
ax = lx + col_w + 35
c.text(ax, top + col_h / 2, "→", size=44, bold=True, fill=NAVY, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#EDF2F7", outline=BORDER)
c.text(rx + col_w / 2, top + 28, "OUT: MARCH 30, 2026", size=15, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 84, "7 ways", size=52, impact=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 124, "to the three members, their PACs, the NRCC", size=13, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 144, "then the committee filed to dissolve, April 1", size=12.5, fill=MUTED, anchor="mm")
outs = [("NRCC", "$51,984"), ("Langworthy for Congress", "$21,578"), ("Comer and Guthrie campaigns, each", "$21,578"),
        ("three leadership PACs (his: Circle the Wagons), each", "$9,808"), ("compliance, software, in-kind", "$4,655")]
for i, (n, a) in enumerate(outs):
    ry = top + 180 + i * 30
    c.text(rx + 22, ry, n, size=12, bold=("Langworthy" in n or "his" in n), fill=DARK, anchor="lm")
    c.text(rx + col_w - 22, ry, a, size=12.5, bold=True, fill=DARK, anchor="rm")
c.text(rx + col_w / 2, top + col_h - 18, "The NRCC took another $53,000 from the same two LLCs that day.", size=11.5, bold=True, fill=NAVY, anchor="mm")
y = top + col_h + 14

strip_h = 136
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 26, "WHO THE DONORS ARE, AND WHO OVERSEES THEM", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 54, "Six Kentucky nursing homes. Five are in one chain CMS rates 1.7 of 5 for staffing; two are rated one star overall (CMS Care Compare, Oct 2026).", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 80, "Energy and Commerce writes Medicaid law; Oversight investigates it. The chairmen of both were in the committee. He sits on both.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 108, "His Oct 20 post: \"rooting out waste, fraud, and abuse.\" The fraud documents his committee and CMS published, and his 70 releases: no mention of nursing homes.", size=12.5, bold=True, fill=RED, anchor="mm")
y += strip_h + 14

kick_h = 104
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 30, "All of it is lawful and disclosed. Joint fundraising committees are common. No link to any vote is claimed.", size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 62, "Three members whose committees oversee nursing homes. Six nursing-home donors. Eleven weeks.", size=16, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: FEC files 1932018, 1957130, 1961860 (docquery)  ·  fec.gov NRCC receipts  ·  CMS Care Compare provider data, Oct 2026  ·  American Prospect, Oct 30", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-10-31-kentucky-nursing-home-joint-fundraising-committee/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kentucky_jfc_card.png"), to_desktop=True)
