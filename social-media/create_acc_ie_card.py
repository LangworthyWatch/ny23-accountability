#!/usr/bin/env python3
"""Social card: the ACC independent expenditure and H.R. 7502.

Anchored to content/fact-checks/2026-08-26-acc-independent-expenditure-recycled-materials-act.md
(verdict: MISSING CONTEXT). NOTE: entry is draft:true pending comment requests
to both the office and ACC. DO NOT POST until it publishes - the caption URL
would 404.

Hero is the asymmetry: $95,900 is the ONLY outside money supporting him this
cycle. Green left = the ad's claims, which are accurate on their face (concede
first). Red right = the two sections the ad does not mention.
Strip is the chronology, which is the actual finding.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, 'The Only Outside Money in This Race Is $95,900 from the Chemical Industry.', size=27)
y = c.subtitle(y + 6, 'An FEC Form 5 filed Aug 21, and the bill it does not mention.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 118
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(168, y + 2 + hero_h / 2, "$95,900", size=52, impact=True, fill=RED, anchor="mm")
c.text(310, y + 40, "from the American Chemistry Council, supporting him.", size=17, bold=True, fill=DARK, anchor="lm")
c.text(310, y + 70, "The only outside money on the other side: $149.64.", size=17, bold=True, fill=DARK, anchor="lm")
c.text(310, y + 100, "ACC's full 2026 program is exactly $1,000,000. Four of its six recipients sit on Energy and Commerce.", size=12, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 348
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "WHAT THE AD SAYS", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "and it is accurate", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 118, "7 R, 5 D", size=50, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 178, "H.R. 7502 really is bipartisan.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 204, "Twelve cosponsors.", size=16, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 242, "It does prohibit unsubstantiated", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 268, "recycled content claims.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 306, "Misleading recycling labels are", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 328, "a real problem. This is real policy.", size=14, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 32, "WHAT THE AD LEAVES OUT", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 56, "two sections of the same bill", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 118, "SEC. 3", size=50, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 178, "recognizes mass balance accounting,", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 204, "the industry's standing ask to the FTC.", size=15, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 242, "Sec. 6 preempts state law", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 268, "on the same subject.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 306, "EPA rejected mass balance for its", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 328, "Safer Choice label in 2024.", size=14, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: the chronology ----------------------------------------------
strip_h = 122
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "THE CHRONOLOGY, FROM FEDERAL DISCLOSURE FORMS", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([
        ("Q3 2025", "ACC discloses lobbying on", "\"unintroduced legislation titled the"),
        ("Feb 11, 2026", "He introduces it under that", "exact name. ACC endorses it"),
        ("Aug 21, 2026", "ACC files the $95,900", "independent expenditure")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 54, val, size=21, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 80, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 98, l2, size=12, fill=DARK, anchor="mm")
c.text(44 + 0 * third + third / 2, y + 114, "Recycled Materials Attribution Act.\"", size=12, fill=DARK, anchor="mm")
c.text(44 + 1 * third + third / 2, y + 114, "the next day.", size=12, fill=DARK, anchor="mm")
c.text(44 + 2 * third + third / 2, y + 114, "supporting him.", size=12, fill=DARK, anchor="mm")
y += strip_h + 12

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 30, "No coordination is alleged. Lobbying on a draft bill is legal and routine.",
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 62, "This is the public record, in the order it happened.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: FEC Form 5 filing 2009256  ·  FEC Schedule E and bulk file itpas2  ·  Senate LDA filings, ACC Q3 2025", size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 19, "H.R. 7502 as introduced (govinfo)  ·  House Clerk MemberData.xml  ·  ProPublica  ·  Waste Dive  ·  Packaging Dive", size=12, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "acc_ie_card.png"), to_desktop=True)
