#!/usr/bin/env python3
"""Social card: Langworthy's housing-bill vote (TRUE), then Trump cancels the signing. June 24, 2026."""

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
f_big     = font("Impact.ttf", 80)
f_quote   = font("Arial Bold.ttf", 24)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 19)
f_small   = font("Arial.ttf", 18)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 15)
f_src     = font("Arial.ttf", 16)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 64

# Verdict badge
tag = "TRUE  ·  THEN STALLED"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 12

# Topic
draw.text((WIDTH//2, y), "Langworthy's Housing Bill Vote", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# WHAT HE SAID (quote box)
claim_h = 134
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+16), "WHAT HE SAID  ·  Facebook, June 24, 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+52), '"Proud to work in a bipartisan manner to deliver for', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+78), 'families and make the dream of owning a home more affordable."', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+110), "Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")
y += claim_h + 16

# TWO COLUMNS: the vote (true) vs. the holdup
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 262
lx = 44
rx = lx + col_w + 16

# LEFT: the vote, confirmed
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+22), "THE VOTE  ·  CONFIRMED", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+92), "358-32", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+158), "House passed it, June 23", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+186), "Senate 85-5  ·  veto-proof margins", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+224), "Langworthy voted YES", fill=GREEN, font=f_sub_b, anchor="mm")

# RIGHT: the holdup
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+22), "THE HOLDUP", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+92), "STALLED", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+158), "Trump canceled the signing", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+186), "won't sign until the SAVE Act passes", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+224), "not a veto  ·  bill in limbo", fill=MUTED, font=f_small, anchor="mm")

y += col_h + 16

# GOP REACTION strip (cross-aisle: Republicans objecting)
strip_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+22), "EVEN REPUBLICAN SENATORS OBJECT", fill=NAVY, font=f_label, anchor="mm")
third = (WIDTH - 88) // 3
for i, (quote, who, st) in enumerate([
    ('"Inexplicable"',   "Sen. John Cornyn",  "R-TX"),
    ('"Makes no sense"',  "Sen. Susan Collins", "R-ME"),
    ('"Hostage"',         "Sen. Thom Tillis",  "R-NC"),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+74), quote, fill=NAVY, font=f_quote, anchor="mm")
    draw.text((cx, y+106), who, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+128), st, fill=MUTED, font=f_xs, anchor="mm")
y += strip_h + 16

# Kicker
kick_h = 96
draw.rounded_rectangle([(44, y), (WIDTH-44, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+30), "Langworthy helped pass a finished, bipartisan housing bill.",
          fill=LIGHTGRAY, font=font("Arial.ttf", 18), anchor="mm")
draw.text((WIDTH//2, y+62), "The President is the one refusing to sign it.",
          fill=WHITE, font=font("Arial Bold.ttf", 22), anchor="mm")
y += kick_h + 14

# Sources + URL
draw.text((WIDTH//2, y), "Sources: House Roll Call 224  ·  Senate Roll Call 182  ·  congress.gov (H.R. 6644)  ·  NPR  ·  The Hill",
          fill=MUTED, font=f_src, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org", fill=NAVY, font=f_src, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/housing_bill_passed_stalled.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
