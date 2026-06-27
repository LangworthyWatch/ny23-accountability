#!/usr/bin/env python3
"""Social card: cystic fibrosis NIH credit-claim. CONTRADICTION, June 27, 2026.
He met the Cystic Fibrosis Foundation and praised CF treatments; he voted twice
for the bill that same Foundation condemned for cutting Medicaid for ~40% of CF patients."""

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
f_stat    = font("Impact.ttf", 46)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 19)
f_small   = font("Arial.ttf", 18)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_src     = font("Arial.ttf", 16)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# -- Header --
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 64

# -- Verdict badge --
tag = "CONTRADICTION"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 30

# -- Topic --
draw.text((WIDTH//2, y), "Cystic Fibrosis: The Photo vs. the Vote", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# -- WHAT HE POSTED (quote box) --
claim_h = 124
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+16), "WHAT HE POSTED  ·  with the Cystic Fibrosis Foundation, Jun 26, 2026", fill=ORANGE, font=f_label_s, anchor="lm")
draw.text((76, y+50), '"…continued investment in research fuels innovation and', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+76), 'lifesaving treatments for families across the nation."', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+102), "Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")
y += claim_h + 18

# -- TWO COLUMNS: who's at stake vs. how he voted --
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 270
lx = 44
rx = lx + col_w + 16

# LEFT: the Foundation's warning
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+22), "WHO RELIES ON MEDICAID", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+96), "40%", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+166), "of people with cystic fibrosis", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+194), "CF Foundation, May 13, 2025", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+232), "It urged Congress to reject the cuts", fill=MUTED, font=f_small, anchor="mm")

# RIGHT: how he voted on the bill they condemned
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+22), "TIMES HE VOTED FOR IT", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+96), "2x", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+166), "YES on H.R. 1", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+194), "Roll Call 145  ·  Roll Call 190", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+232), "2nd vote: 2 days after they condemned it", fill=MUTED, font=f_xs_b, anchor="mm")

y += col_h + 18

# -- THE REST (3-stat strip) --
strip_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+20), "THE FULL PICTURE", fill=NAVY, font=f_label, anchor="mm")
third = (WIDTH - 88) // 3
for i, (val, l1, l2, c) in enumerate([
    ("Oct 2019", "Trikafta approved",      "before his 2023 term",     NAVY),
    ("$500M+",   "CF Foundation research",  "its own venture funding",  NAVY),
    ("$48.7B",   "NIH funding held",        "House GOP kept it ~flat",  GREEN),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+72), val, fill=c, font=f_stat, anchor="mm")
    draw.text((cx, y+108), l1, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+128), l2, fill=MUTED, font=f_xs, anchor="mm")
y += strip_h + 18

# -- Kicker --
kick_h = 96
draw.rounded_rectangle([(44, y), (WIDTH-44, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+30), "The treatments are real, and NIH funding held. The gap is coverage:",
          fill=LIGHTGRAY, font=font("Arial.ttf", 18), anchor="mm")
draw.text((WIDTH//2, y+62), "for nearly 40% of CF patients, Medicaid is what pays for them.",
          fill=WHITE, font=font("Arial Bold.ttf", 22), anchor="mm")
y += kick_h + 16

# -- Sources + URL --
draw.text((WIDTH//2, y), "Sources: Cystic Fibrosis Foundation (May 13 + Jul 1, 2025)  ·  House Clerk, Roll Call 145 + 190  ·  KFF",
          fill=MUTED, font=f_src, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-27-cystic-fibrosis-nih-credit-claim/",
          fill=NAVY, font=f_src, anchor="mm")

# -- Footer --
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/cystic_fibrosis_photo_vs_vote.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
