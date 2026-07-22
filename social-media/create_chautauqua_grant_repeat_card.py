#!/usr/bin/env python3
"""Card: the same $1M SAMHSA children's mental-health grant for Chautauqua
County, announced by Langworthy twice, nearly three years apart (Sept 2023,
July 2026), in nearly identical language. MISSING CONTEXT. House style,
1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "MISSING CONTEXT")
y = c.title(y, "The Same $1M Grant, Announced Twice.", size=30)
y = c.subtitle(y + 6, "September 2023 and July 2026. Nearly identical words, same program.", size=16)
y = c.divider(y + 34)

# ---- two panels: 2023 vs 2026 announcement ----
ph = 380
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2
py = y + 14

c.panel(lx0, py, lx1, py + ph, fill="#F7FAFC", outline=NAVY)
c.text(lc, py + 34, "SEPTEMBER 13, 2023", size=18, bold=True, fill=NAVY, anchor="mm")
c.text(lc, py + 56, "County press release", size=13, fill=MUTED, anchor="mm")
lines_l = [
    "“I’m pleased to",
    "announce this",
    "significant grant to",
    "provide needed",
    "resources for our",
    "community’s mental",
    "health services.”",
]
yy = py + 110
for line in lines_l:
    c.text(lc, yy, line, size=17, fill=DARK, anchor="mm")
    yy += 27

c.panel(rx0, py, rx1, py + ph, fill="#F7FAFC", outline=NAVY)
c.text(rc, py + 34, "JULY 16, 2026", size=18, bold=True, fill=NAVY, anchor="mm")
c.text(rc, py + 56, "House.gov press release", size=13, fill=MUTED, anchor="mm")
lines_r = [
    "“Every child deserves",
    "access to the mental",
    "health care... this",
    "$1 million investment",
    "will help ensure",
    "children... receive",
    "timely, comprehensive care.”",
]
yy = py + 110
for line in lines_r:
    c.text(rc, yy, line, size=17, fill=DARK, anchor="mm")
    yy += 27

y = py + ph + 34

# ---- same-facts strip ----
strip_h = 116
c.panel(44, y, c.w - 44, y + strip_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 38, "SAME PROGRAM  ·  SAME $1,000,000  ·  SAME COUNTY DEPARTMENT", size=17, bold=True, fill="#744210", anchor="mm")
c.text(c.w / 2, y + 80, "SAMHSA selects the recipient. A member of Congress doesn’t pick the winner.", size=17, fill=DARK, anchor="mm")
y += strip_h + 32

y = c.kicker(y,
         "He voted Aye on H.R. 1 (Roll Call 190): about $900B cut from Medicaid.",
         "Medicaid funds most of the children’s behavioral care this grant supplements.",
         h=112)
y += 26
c.text(c.w / 2, y, "Sources: langworthy.house.gov · Chautauqua Co. Dept. of Mental Hygiene · SAMHSA · House Clerk Roll Call 190",
       size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save("social-media/chautauqua_grant_repeat_card.png", to_desktop=True)
