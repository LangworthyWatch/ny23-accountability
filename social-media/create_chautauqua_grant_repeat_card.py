#!/usr/bin/env python3
"""Card: the same $1M SAMHSA children's mental-health grant for Chautauqua
County, announced by Langworthy twice, 1,037 days apart (Sept 2023, July
2026), in nearly identical language. MISSING CONTEXT. Stat-first layout
(matches beagle_count_contrast_card / shared_earmarks_card precedent: lead
with a big glanceable number, not quote-dense panels). House style, 1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "MISSING CONTEXT")
y = c.title(y, "The Same $1M Grant, Announced Twice.", size=30)
y = c.subtitle(y + 6, "1,037 days apart, nearly the same sentence.", size=16)
y = c.divider(y + 20)

# ---- hero stat: the day gap, not a wall of quotes ----
c.text(c.w / 2, y + 22, "DAYS BETWEEN TWO ANNOUNCEMENTS OF THE SAME GRANT", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 120, "1,037", size=110, impact=True, fill=RED, anchor="mm")
c.text(c.w / 2, y + 192, "Sept. 13, 2023  →  July 16, 2026", size=16, fill=MUTED, anchor="mm")
y += 224

# ---- two compact quote panels ----
ph = 190
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2
py = y

c.panel(lx0, py, lx1, py + ph, fill="#F7FAFC", outline=NAVY)
c.text(lc, py + 26, "SEPT. 13, 2023", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(lc, py + 46, "County press release", size=12, fill=MUTED, anchor="mm")
for i, line in enumerate([
    "“I’m pleased to announce",
    "this significant grant...",
    "for our community’s",
    "mental health services.”",
]):
    c.text(lc, py + 82 + i * 26, line, size=15, fill=DARK, anchor="mm")

c.panel(rx0, py, rx1, py + ph, fill="#F7FAFC", outline=NAVY)
c.text(rc, py + 26, "JULY 16, 2026", size=16, bold=True, fill=NAVY, anchor="mm")
c.text(rc, py + 46, "House.gov press release", size=12, fill=MUTED, anchor="mm")
for i, line in enumerate([
    "“...this $1 million",
    "investment will help",
    "ensure children... receive",
    "timely, comprehensive care.”",
]):
    c.text(rc, py + 82 + i * 26, line, size=15, fill=DARK, anchor="mm")

y = py + ph + 30

# ---- same-facts strip ----
strip_h = 110
c.panel(44, y, c.w - 44, y + strip_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 36, "SAME PROGRAM  ·  SAME $1,000,000  ·  SAME COUNTY DEPARTMENT", size=17, bold=True, fill="#744210", anchor="mm")
c.text(c.w / 2, y + 76, "SAMHSA selects the recipient. A member of Congress doesn’t pick the winner.", size=16, fill=DARK, anchor="mm")
y += strip_h + 30

y = c.kicker(y,
         "He voted Aye on H.R. 1 (Roll Call 190): about $900B cut from Medicaid.",
         "Medicaid funds most of the children’s behavioral care this grant supplements.",
         h=110)
y += 26
c.text(c.w / 2, y, "Sources: langworthy.house.gov · Chautauqua Co. Dept. of Mental Hygiene · SAMHSA · House Clerk Roll Call 190",
       size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save("social-media/chautauqua_grant_repeat_card.png", to_desktop=True)
