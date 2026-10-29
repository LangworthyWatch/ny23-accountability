#!/usr/bin/env python3
"""Reeves Act "strong support" post, entry 2026-10-29-reeves-act-strong-support-post (MISSING CONTEXT).
Dates from govinfo BILLSTATUS (H.R. 9401, H.R. 2598), the Clerk (RC 145, 190), CBO 61510, NPR Oct 1, LeadingAge Sept 24, NYSBOE."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  OCT 29, 2026")
y = c.title(y, "\"Strong Support\" for the Disability Bill.", size=30)
y = c.title(y - 2, "He Signed On October 22.", size=30)
y = c.subtitle(y + 6, "His page shared advocates' thanks for backing the Latonya Reeves Freedom Act. The record on when, and on what he voted for first.", size=14.5)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 385
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + col_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT THE POST SHARES", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 98, "Oct 22", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 144, "the day he cosponsored H.R. 9401", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 166, "per the House's official cosponsor record", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["Bill introduced June 23, 2026.",
                       "Rep. Lawler (R-NY) signed July 9.",
                       "8 of 11 Republicans signed by Sept 24.",
                       "Early voting opened Oct 24. Rally Oct 27.",
                       "The support is real. It is ten days old."]):
    c.text(lx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 4), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT IT LEAVES OUT", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 98, "2 votes", size=58, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 144, "for the law that cuts Medicaid $840 billion", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 166, "H.R. 1, May 22 and July 3, 2025 (CBO estimate)", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["Medicaid pays for the home- and community-",
                       "based services the Reeves Act would protect.",
                       "Six-month eligibility checks. New copays.",
                       "A provider-tax freeze that hits HCBS funding.",
                       "AAPD: \"a devastating day for disabled Americans.\""]):
    c.text(rx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 4), fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 176
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 32, "WHAT THE BILL ANSWERS, AND WHAT HE HAS SAID ABOUT IT", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 68, "June 18: the Justice Dept. said federal law does not require serving disabled people \"in the most integrated setting.\"", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 98, "Sept 23: at DOJ's own request, a federal court struck the HHS rules that said it does. The bill was filed June 23.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 134, "70 press releases, his X feed, the web: no statement by him on any of it that we could find.", size=13.5, bold=True, fill=RED, anchor="mm")
y += strip_h + 14

kick_h = 118
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 38, "Also true: he joined an SSI bill Oct 1, signed a 2023 home-health letter, and is not on the bill to abolish the Education Dept.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 76, "Still not on IDEA Full Funding. Three NY Republicans are. It has waited 18 months.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: govinfo BILLSTATUS H.R. 9401, 2540, 2598  ·  House Clerk RC 145, 190  ·  CBO 61510  ·  NPR Oct 1, 2026  ·  Texas v. Kennedy order, Sept 23  ·  WENY Oct 27", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-10-29-reeves-act-strong-support-post/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reeves_act_card.png"), to_desktop=True)
