#!/usr/bin/env python3
"""Kentucky nursing-home joint fundraising committee, entry 2026-10-31-kentucky-nursing-home-joint-fundraising-committee
(DOCUMENTED PATTERN). v2: three-stage flow (who gave -> the vehicle -> who received, by role). Figures from FEC files 1932018,
1957130, 1961860; CMS Care Compare Oct 2026; retained under research/sources/prospect-nursing-home-2026-10-30/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN  ·  NOV 2, 2026")
y = c.title(y, "$150,800 From Six Nursing-Home Companies, in One Day,", size=28)
y = c.title(y - 2, "to the Three Men Whose Committees Oversee Nursing Homes.", size=28)
y = c.subtitle(y + 6, "The Langworthy Leadership & Accountability Fund, a joint fundraising committee, per its own FEC filings. It lived eleven weeks.", size=13.5)
y = c.divider(y + 12)

# Three-stage flow
gap = 44
inner = c.w - 44 * 2
left_w, mid_w = 330, 272
right_w = inner - left_w - mid_w - gap * 2
lx = 44
mx = lx + left_w + gap
rx = mx + mid_w + gap
top = y
flow_h = 500

# LEFT: who gave
c.panel(lx, top, lx + left_w, top + flow_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + left_w / 2, top + 28, "WHO GAVE", size=15, bold=True, fill=RED, anchor="mm")
c.text(lx + left_w / 2, top + 56, "March 19, 2026. One address:", size=12.5, fill=MUTED, anchor="mm")
c.text(lx + left_w / 2, top + 76, "300 Provider Court, Richmond, Ky.", size=12.5, bold=True, fill=DARK, anchor="mm")
donors = [("Woodland Oaks Operations", "$75,000"), ("Klondike Nursing & Rehab", "$50,000"), ("Berea Healthcare", "$6,000"),
          ("Cambridge Operations", "$6,000"), ("Cumberland KY OpCo", "$6,000"), ("Dover Manor Operations", "$6,000")]
for i, (n, a) in enumerate(donors):
    ry = top + 112 + i * 30
    c.text(lx + 18, ry, n, size=12.5, fill=DARK, anchor="lm")
    c.text(lx + left_w - 18, ry, a, size=12.5, bold=True, fill=DARK, anchor="rm")
c.rect(lx + 18, top + 300, lx + left_w - 18, top + 301, fill="#FEB2B2", outline=None)
for i, t in enumerate(["Six Kentucky nursing homes.", "Five in one chain CMS rates", "1.7 of 5 for staffing.", "Two rated one star overall."]):
    c.text(lx + left_w / 2, top + 324 + i * 24, t, size=12.5, bold=(i == 0), fill=RED if i == 0 else DARK, anchor="mm")
c.text(lx + left_w / 2, top + flow_h - 22, "(CMS Care Compare, Oct 2026)", size=10.5, fill=MUTED, anchor="mm")

# arrows
c.text(lx + left_w + gap / 2, top + flow_h / 2, "→", size=40, bold=True, fill=NAVY, anchor="mm")
c.text(mx + mid_w + gap / 2, top + flow_h / 2, "→", size=40, bold=True, fill=NAVY, anchor="mm")

# MIDDLE: the vehicle
c.panel(mx, top, mx + mid_w, top + flow_h, fill=WHITE, outline=BORDER)
c.text(mx + mid_w / 2, top + 28, "THE VEHICLE", size=15, bold=True, fill=NAVY, anchor="mm")
c.text(mx + mid_w / 2, top + 100, "$150,800", size=46, impact=True, fill=NAVY, anchor="mm")
c.text(mx + mid_w / 2, top + 140, "its only money, ever", size=13, bold=True, fill=DARK, anchor="mm")
steps = [("Jan 12", "formed with the", "three members' campaigns,", "their PACs and the NRCC"),
         ("Jan, Feb", "$0 raised", "", ""),
         ("Mar 19", "$150,800 in", "", ""),
         ("Mar 30", "split: $94,160 to the", "members and their PACs,", "$51,984 to the NRCC"),
         ("Apr 1", "termination report filed", "", "")]
ty = top + 176
for d, l1, l2, l3 in steps:
    col = RED if d == "Mar 19" else NAVY
    c.rect(mx + 24, ty - 6, mx + 34, ty + 6, fill=col, outline=None)
    c.text(mx + 46, ty, d, size=12.5, bold=True, fill=col, anchor="lm")
    c.text(mx + 118, ty, l1, size=11.5, fill=DARK, anchor="lm")
    n = 1
    for extra in (l2, l3):
        if extra:
            c.text(mx + 118, ty + 16 * n, extra, size=11.5, fill=DARK, anchor="lm"); n += 1
    ty += 22 + 16 * (n - 1) + 10
c.text(mx + mid_w / 2, top + flow_h - 22, "Eleven weeks, start to finish.", size=12.5, bold=True, fill=NAVY, anchor="mm")

# RIGHT: who received, by role
c.panel(rx, top, rx + right_w, top + flow_h, fill="#EDF2F7", outline=BORDER)
c.text(rx + right_w / 2, top + 28, "WHO RECEIVED", size=15, bold=True, fill=NAVY, anchor="mm")
c.text(rx + right_w / 2, top + 56, "March 30, 2026. By role:", size=12.5, fill=MUTED, anchor="mm")
recips = [("Chairman, Energy and Commerce", "the committee that writes Medicaid law", "Guthrie for Congress + PAC", "$31,386"),
          ("Chairman, Oversight", "the committee that investigates it", "Comer for Congress + PAC", "$31,386"),
          ("Member of both committees", "the only New Yorker in the group", "Langworthy for Congress + PAC", "$31,386")]
ry = top + 92
for role, sub, who, amt in recips:
    c.text(rx + 18, ry, role, size=13, bold=True, fill=NAVY if "both" not in role else RED, anchor="lm")
    c.text(rx + 18, ry + 18, sub, size=11, fill=MUTED, anchor="lm")
    c.text(rx + 18, ry + 36, who, size=11.5, fill=DARK, anchor="lm")
    c.text(rx + right_w - 18, ry + 18, amt, size=15, bold=True, fill=DARK, anchor="rm")
    ry += 74
c.rect(rx + 18, ry - 6, rx + right_w - 18, ry - 5, fill=BORDER, outline=None)
c.text(rx + 18, ry + 14, "NRCC", size=12.5, fill=DARK, anchor="lm")
c.text(rx + right_w - 18, ry + 14, "$51,984", size=12.5, bold=True, fill=DARK, anchor="rm")
c.text(rx + 18, ry + 34, "plus $53,000 direct from the same two LLCs that day", size=10.5, fill=MUTED, anchor="lm")
c.text(rx + right_w / 2, top + flow_h - 22, "Medicaid is nursing homes' largest payer.", size=12, bold=True, fill=NAVY, anchor="mm")
y = top + flow_h + 14

strip_h = 96
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 26, "WHAT HE HAS SAID ABOUT NURSING HOMES", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, "Oct 20: \"As a member of the Energy and Commerce Committee, I'm committed to rooting out waste, fraud, and abuse.\"", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 76, "The fraud documents his committee and CMS published this year, and his 70 press releases since Aug 2025: no mention of nursing homes.", size=12.5, bold=True, fill=RED, anchor="mm")
y += strip_h + 14

kick_h = 108
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "All of it is lawful and disclosed. Joint fundraising committees are common. No link to any vote is claimed.", size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "Six nursing-home donors. Three overseers. One day. Eleven weeks.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: FEC files 1932018, 1957130, 1961860 (docquery)  ·  fec.gov NRCC receipts  ·  CMS Care Compare provider data, Oct 2026  ·  American Prospect, Oct 30", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-10-31-kentucky-nursing-home-joint-fundraising-committee/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kentucky_jfc_card.png"), to_desktop=True)
