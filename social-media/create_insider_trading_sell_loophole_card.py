#!/usr/bin/env python3
"""Card: Langworthy's own video says members "shouldn't run from a briefing
to their broker" while touting H.R. 7008 (Stop Insider Trading Act). The bill
bans new stock PURCHASES but does not ban SELLING - only requires 7-14 days'
public notice before a sale. Rep. Neguse (D-CO) raised exactly this gap at the
July 20, 2026 Rules Committee hearing. MISLEADING. House style, 1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "MISLEADING")
y = c.title(y, "“Shouldn’t Run From a Briefing to a Broker.”", size=29)
y = c.subtitle(y + 6, "His own video, touting a bill that doesn’t ban selling on one.", size=16)
y = c.divider(y + 20)

# ---- two panels: his words vs the bill's mechanics ----
ph = 356
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2
py = y + 14

c.panel(lx0, py, lx1, py + ph, fill="#F7FAFC", outline=NAVY)
c.text(lc, py + 36, "HIS OWN WORDS", size=19, bold=True, fill=NAVY, anchor="mm")
c.text(lc, py + 58, "Facebook video, July 21, 2026", size=14, fill=MUTED, anchor="mm")
quotes_l = [
    "“I’m not a millionaire, and",
    "I don’t trade stocks.”",
    "",
    "“Public service, not cashing",
    "in on insider tips.”",
    "",
    "“Members shouldn’t run",
    "from a briefing to their",
    "broker.”",
]
yy = py + 104
for line in quotes_l:
    if line:
        c.text(lc, yy, line, size=17, fill=DARK, anchor="mm")
    yy += 27

c.panel(rx0, py, rx1, py + ph, fill="#FFF5F5", outline=RED)
c.text(rc, py + 36, "WHAT HIS BILL DOES", size=19, bold=True, fill=RED, anchor="mm")
c.text(rc, py + 58, "H.R. 7008, Stop Insider Trading Act", size=14, fill=MUTED, anchor="mm")
rows_r = [
    "Bans members, spouses,",
    "kids from BUYING new",
    "individual stock.",
    "",
    "Selling is NOT banned:",
    "just 7–14 days’ public",
    "notice before the sale.",
]
yy = py + 104
for line in rows_r:
    if line:
        c.text(rc, yy, line, size=17, fill=DARK, anchor="mm")
    yy += 27

y = py + ph + 34

# ---- Neguse callout strip ----
strip_h = 116
c.panel(44, y, c.w - 44, y + strip_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 36, "REP. JOE NEGUSE (D-CO), RULES COMMITTEE, JULY 20, 2026", size=15, bold=True, fill="#744210", anchor="mm")
c.text(c.w / 2, y + 80, "“It does not ban the selling.”", size=23, bold=True, fill=DARK, anchor="mm")
y += strip_h + 32

y = c.kicker(y,
         "Buying on a tip: banned under the bill he’s touting.",
         "Selling on one: still legal, with 7–14 days’ notice.",
         h=104)
y += 26
c.text(c.w / 2, y, "Sources: facebook.com/RepLangworthy · H.R. 7008 text, Rules Committee · Rules Cmte. hearing, 7/20/26",
       size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save("social-media/insider_trading_sell_loophole_card.png", to_desktop=True)
