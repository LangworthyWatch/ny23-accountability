#!/usr/bin/env python3
"""Social card: H.R. 5517 Northern Border Security Enhancement and Review Act.
The framing ('Enforcement', 'protected on all fronts') vs. what the bill text
requires (reports, strategy, briefings, metrics), against the GAO staffing finding.
MISSING CONTEXT, July 6, 2026."""

from lib.card import Card, NAVY, RED, GREEN, GOLD, ORANGE, DARK, MUTED, WHITE, LIGHTGRAY, BORDER

c = Card(scale=2)
c.brand_bar()

y = c.badge(62, "MISSING CONTEXT")
y = c.title(y, "A Reporting Bill, an Enforcement Label", size=30)
y = c.subtitle(y + 2, "He calls it the 'Security and Enforcement Act.'", size=17)
y = c.subtitle(y + 4, "Its real name is the 'Enhancement and Review Act.'", size=17)
y = c.divider(y + 10)

# --- his post (claim box) ---
claim_h = 108
c.panel(44, y, c.w - 44, y + claim_h, fill="#FFFAF0", outline="#F6AD55")
c.text(72, y + 20, "HIS FACEBOOK POST  ·  JULY 2026", size=16, bold=True, fill=ORANGE)
c.text(72, y + 52, '"My Northern Border Security and Enforcement Act', size=18, fill=DARK)
c.text(72, y + 80, 'will ensure we are protected on all fronts."', size=18, fill=DARK)
y += claim_h + 18

# --- two columns: what's promised vs. what the text requires ---
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 292
lx = 44
rx = lx + col_w + 16

# left: the framing (green)
c.panel(lx, y, lx + col_w, y + col_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(lx + col_w / 2, y + 24, "WHAT'S PROMISED", size=19, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, y + 46, "the pitch", size=14, fill=MUTED, anchor="mm")
c.bullets(lx + 24, y + 86, [
    "'Protected on all fronts'",
    "Border secured vs. cartels",
    "Branded as 'Enforcement'",
    "Sounds like boots and agents",
], accent=GREEN, step=44, size=16)

# right: what the bill actually requires (red)
c.panel(rx, y, rx + col_w, y + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, y + 24, "WHAT THE TEXT REQUIRES", size=19, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, y + 46, "H.R. 5517, every provision", size=14, fill=MUTED, anchor="mm")
c.bullets(rx + 24, y + 86, [
    "A DHS threat analysis (a report)",
    "A written strategy update",
    "Classified briefings to Congress",
    "New effectiveness metrics",
    "No agents. No funding.",
], accent=RED, step=40, size=16)
y += col_h + 18

# --- the watchdog stat strip ---
strip_h = 108
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(72, y + 22, "THE WATCHDOG THE POST CITES (GAO, JUNE 2026) FOUND:", size=17, bold=True, fill=NAVY)
c.text(150, y + 68, "6%", size=52, impact=True, fill=RED, anchor="mm")
c.text(228, y + 58, "fewer Border Patrol agents on the northern", size=17, fill=DARK)
c.text(228, y + 84, "border, 2019 to 2024. H.R. 5517 adds none.", size=17, fill=DARK)
y += strip_h + 16

# --- kicker: the fair point ---
c.kicker(y, "To be fair, the bill answers one of the GAO's three recommendations (the AMO metrics).",
         "It skips the other two, including the staffing gap the watchdog documented.", h=92)
y += 92 + 16

c.text(c.w / 2, y, "Sources: H.R. 5517 (119th Cong.)  ·  GAO-26-109195  ·  Langworthy press release",
       size=15, fill=MUTED, anchor="mm")
y += 24
c.text(c.w / 2, y, "langworthywatch.org/fact-checks/2026-07-06-northern-border-security-review-act/",
       size=14, fill=NAVY, anchor="mm")

c.footer_bar()
c.save("/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/northern_border_card.png")
