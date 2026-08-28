#!/usr/bin/env python3
"""Social card: NYCBS oncology money and the biosimilars bill.

Anchored to content/fact-checks/2026-08-28-nycbs-oncology-money-biosimilars-bill.md
(verdict: DOCUMENTED PATTERN). Published Aug 28, 2026.

Hero is the 15 days. Green left = the fair reading, which is unusually strong
here (FDA first, bipartisan, broad support) and gets the concede-first slot.
Red right = the money and the dates. Strip = the three-entry pattern.
No allegation of exchange anywhere; the kicker is about disclosure.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(56, "DOCUMENTED PATTERN")
y = c.title(y, 'The Donors Are on Long Island. The Bill Is in His Name.', size=30)
y = c.subtitle(y + 6, 'A cancer network with no location in NY-23, its PAC, and H.R. 9661. From FEC filings; no exchange is alleged.', size=14)
y = c.divider(y + 10)

# ---- hero ---------------------------------------------------------------
hero_h = 130
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 2 + hero_h / 2, "15 days", size=52, impact=True, fill=RED, anchor="mm")
c.text(312, y + 40, "between the PAC's third $5,000 check (June 29)", size=16, bold=True, fill=DARK, anchor="lm")
c.text(312, y + 66, "and his biosimilars bill (July 14, 2026).", size=16, bold=True, fill=DARK, anchor="lm")
c.text(312, y + 98, "Total from the network's doctors and PAC across three cycles: $55,137.", size=12, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 356
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "THE FAIR READING IS STRONG", size=15, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 54, "and it comes first", size=13, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 106, "FDA FIRST", size=42, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 158, "The FDA announced this exact policy", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 182, "nine months before his bill.", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 214, "Rand Paul's identical Senate bill", size=14, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 236, "predates it by fifteen months.", size=14, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 258, "His co-lead is a Democratic physician.", size=14, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 288, "Insurers, employers, pharmacists and", size=13, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 308, "Roswell Park endorse it. No organized", size=13, fill=MUTED, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "THE MONEY AND THE DATES", size=15, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 54, "from FEC bulk filings", size=13, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 106, "$55,137", size=46, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 158, "56 gifts from the network's doctors", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 182, "in three tight same-week waves,", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 206, "plus $15,000 from its leaders' PAC.", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 238, "The CEO's two largest personal gifts:", size=14, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 260, "May 2026, two months before the bill.", size=14, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 292, "Part of a ~$2.4 million program aimed at", size=13, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 312, "health policymakers of both parties.", size=13, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 328, "opposition to the bill was found.", size=13, fill=MUTED, anchor="mm")
y = top + col_h + 14

# ---- strip: the pattern -------------------------------------------------
strip_h = 128
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "THIRD DOCUMENTED INSTANCE OF THE SAME GAP", size=14, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, l1, l2) in enumerate([
        ("Seneca Nation", "$10,100, then a jurisdiction bill.", "Release named neither"),
        ("Chemical industry", "$95,900 in ads; his bill carries", "their FTC ask. Ad names no bill section"),
        ("Oncology network", "$55,137, then a biosimilars bill.", "Release names seven endorsers, no donors")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 52, val, size=19, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 78, l1, size=12, fill=DARK, anchor="mm")
    c.text(cx, y + 96, l2, size=12, fill=DARK, anchor="mm")
y += strip_h + 12

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "The bill may well be good policy. No deal is alleged, and the giving is lawful and disclosed.",
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 62, "The press release gets the policy case. Only the FEC database gets the donors.", size=16, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14

c.text(c.w / 2, y, "Sources: FEC bulk files itcont and itpas2 (memo entries and refunds excluded)  ·  FEC C00785014  ·  govinfo BILLSTATUS", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "FDA, Oct 29, 2025  ·  Politico, Oct 28, 2024  ·  Senate LDA  ·  nycancer.com  ·  Full row-level data on the entry", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nycbs_biosimilars_card.png"), to_desktop=True)
