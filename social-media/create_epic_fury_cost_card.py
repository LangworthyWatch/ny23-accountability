#!/usr/bin/env python3
"""Social card: Operation Epic Fury cost vs. the cuts he voted for. DOCUMENTED PATTERN, June 18, 2026."""

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
f_big     = font("Impact.ttf", 88)
f_stat    = font("Impact.ttf", 48)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 19)
f_small   = font("Arial.ttf", 18)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_src     = font("Arial.ttf", 16)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 64

# ── Verdict badge ──
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 12

# ── Topic ──
draw.text((WIDTH//2, y), "Operation Epic Fury: Cost vs. Cuts", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# ── WHAT HE SAID (quote box) ──
claim_h = 124
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+16), "WHAT HE SAID  ·  Statement, Feb. 28, 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+50), '"…supportive of the Epic Fury operation. This mission is', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+76), 'about protecting our homeland."', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+102), "Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")
y += claim_h + 18

# ── TWO COLUMNS: the war he backed vs. the cut ──
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 270
lx = 44
rx = lx + col_w + 16

# LEFT: the war he championed
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+22), "THE WAR HE CHAMPIONED", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+96), "$132B", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+166), "total cost to Americans so far", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+194), "Moody's Analytics (NPR, Jun 2026)", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+232), "He called it 'protecting our homeland'", fill=MUTED, font=f_small, anchor="mm")

# RIGHT: what he voted to cut
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+22), "WHAT HE VOTED TO CUT", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+96), "$911B", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+166), "Medicaid cut, 10 years", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+194), "KFF / CBO  ·  $137B rural", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+232), "YES on H.R. 1  ·  Roll Call 190", fill=MUTED, font=f_small, anchor="mm")

y += col_h + 18

# ── THE FULL TAB (3-stat strip) ──
strip_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+20), "THE REST OF THE TAB", fill=NAVY, font=f_label, anchor="mm")
third = (WIDTH - 88) // 3
for i, (val, l1, l2, c) in enumerate([
    ("$29B",  "U.S. military cost so far", "Pentagon  ·  excl. base repairs", NAVY),
    ("$1T",   "projected long-term cost",  "Harvard / Bilmes (~$2B a day)",  NAVY),
    ("$186B", "SNAP cut, same bill",       "CBO  ·  2026-2034",              RED),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+72), val, fill=c, font=f_stat, anchor="mm")
    draw.text((cx, y+108), l1, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+128), l2, fill=MUTED, font=f_xs, anchor="mm")
y += strip_h + 18

# ── Kicker ──
kick_h = 96
draw.rounded_rectangle([(44, y), (WIDTH-44, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+30), "Separate budget streams. But the war he urged Washington to fund",
          fill=LIGHTGRAY, font=font("Arial.ttf", 18), anchor="mm")
draw.text((WIDTH//2, y+62), "is projected to cost about what he voted to cut from Medicaid.",
          fill=WHITE, font=font("Arial Bold.ttf", 22), anchor="mm")
y += kick_h + 16

# ── Sources + URL ──
draw.text((WIDTH//2, y), "Sources: Pentagon  ·  Moody's Analytics  ·  Harvard (Bilmes)  ·  CBO  ·  KFF  ·  Roll Call 190",
          fill=MUTED, font=f_src, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-18-epic-fury-cost-vs-cuts/",
          fill=NAVY, font=f_src, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/epic_fury_cost_vs_cuts.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
