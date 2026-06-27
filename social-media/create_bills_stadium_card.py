#!/usr/bin/env python3
"""Social card: Bills stadium 'for the Bills Mafia' MISLEADING, June 27, 2026.
The Mafia (taxpayers + PSL buyers) helped pay for a stadium with ~10k fewer seats."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
GREEN   = "#276749"
RED     = "#E53E3E"
ORANGE  = "#C05621"
GOLD    = "#D69E2E"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"
LIGHTGRAY = "#A0AEC0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except Exception:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 20)
f_label_s = font("Arial Bold.ttf", 16)
f_big     = font("Impact.ttf", 84)
f_stat    = font("Impact.ttf", 46)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 18)
f_small   = font("Arial.ttf", 17)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_src     = font("Arial.ttf", 15)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# -- Header --
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 64

# -- Verdict badge --
tag = "MISLEADING"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 12

# -- Topic --
draw.text((WIDTH//2, y), "Who Really Paid for the New Stadium", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# -- WHAT HE SAID (quote box) --
claim_h = 124
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+16), "WHAT HE SAID  ·  Grand opening video, Jun 23, 2026", fill=ORANGE, font=f_label_s, anchor="lm")
draw.text((76, y+50), '"This is for all of the Bills Mafia that have', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+76), 'been with this team for their whole lives."', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+102), "Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")
y += claim_h + 18

# -- TWO COLUMNS: what they paid vs. what they got --
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 274
lx = 44
rx = lx + col_w + 16

# LEFT: what fans + taxpayers paid
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+22), "WHAT FANS + TAXPAYERS PAID", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+92), "$1.1B", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+158), "into a $2.1B stadium", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+188), "$850M public + $263M in PSLs", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+228), "Owner: the PSLs 'helped finance' it", fill=MUTED, font=f_small, anchor="mm")

# RIGHT: what they got back
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+22), "WHAT THEY GOT BACK", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+92), "10,000", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+158), "fewer seats", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+188), "71,608 → 60,108 · smallest in NFL", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+228), "plus PSLs up to $50,000", fill=MUTED, font=f_small, anchor="mm")

y += col_h + 18

# -- THE FULL PICTURE (3-stat strip) --
strip_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+20), "THE FULL PICTURE", fill=NAVY, font=f_label, anchor="mm")
third = (WIDTH - 88) // 3
for i, (val, l1, l2, c) in enumerate([
    ("$850M", "public subsidy",      "state + county, 2022",   NAVY),
    ("$50K",  "top seat license",    "before a single ticket", RED),
    ("83%",   "of economists agree", "subsidies aren't worth it", GREEN),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+72), val, fill=c, font=f_stat, anchor="mm")
    draw.text((cx, y+108), l1, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+128), l2, fill=MUTED, font=f_xs, anchor="mm")
y += strip_h + 18

# -- Kicker --
kick_h = 96
draw.rounded_rectangle([(44, y), (WIDTH-44, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+30), "He cast no vote on the subsidy. But the same week he warned of",
          fill=LIGHTGRAY, font=font("Arial.ttf", 18), anchor="mm")
draw.text((WIDTH//2, y+62), "'too much public money' elsewhere, then cheered $850M of it here.",
          fill=WHITE, font=font("Arial Bold.ttf", 21), anchor="mm")
y += kick_h + 16

# -- Sources + URL --
draw.text((WIDTH//2, y), "Sources: Buffalo Bills  ·  CNY Central  ·  WKBW  ·  WHEC  ·  U. Chicago Booth (IGM)  ·  Bradbury et al. 2023",
          fill=MUTED, font=f_src, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-27-bills-stadium-public-money-mafia/",
          fill=NAVY, font=f_src, anchor="mm")

# -- Footer --
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/bills_stadium_who_paid.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
