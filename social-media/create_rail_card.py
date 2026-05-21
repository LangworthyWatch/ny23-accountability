#!/usr/bin/env python3
"""Social card: High Speed Rail / Missing Context — May 14, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
AMBER   = "#B7791F"   # MISSING CONTEXT colour
AMBER_BG = "#FFFFF0"
AMBER_BD = "#F6E05E"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"
GOLD    = "#D69E2E"
STEEL   = "#2B6CB0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 24)
f_tag     = font("Arial Bold.ttf", 22)
f_topic   = font("Arial Bold.ttf", 34)
f_label   = font("Arial Bold.ttf", 22)
f_claim   = font("Arial.ttf", 27)
f_claim_b = font("Arial Bold.ttf", 27)
f_big     = font("Impact.ttf", 96)
f_sub     = font("Arial.ttf", 23)
f_sub_b   = font("Arial Bold.ttf", 23)
f_small   = font("Arial.ttf", 20)
f_footer  = font("Arial Bold.ttf", 22)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 52)], fill=NAVY)
draw.text((WIDTH//2, 26), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 74

# ── Verdict badge ──
tag = "MISSING CONTEXT"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+14
tx = (WIDTH-tw)//2
draw.rounded_rectangle([(tx, y), (tx+tw, y+th)], radius=5, fill=AMBER)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 12

draw.text((WIDTH//2, y), "Infrastructure", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# ── What he said ──
box_h = 136
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill=AMBER_BG, outline=AMBER_BD, width=2)
draw.text((76, y+14), "HE SAID — May 14, 2026", fill=AMBER, font=f_label, anchor="lm")
draw.text((76, y+44), '"Honored to deliver the keynote address', fill=DARK, font=f_claim)
draw.text((76, y+78), 'at the U.S. High Speed Rail Conference."', fill=DARK, font=f_claim)
y += box_h + 20

# ── What he left out ──
draw.text((WIDTH//2, y), "WHAT THE POST LEFT OUT", fill=MUTED,
          font=font("Arial Bold.ttf", 20), anchor="mm")
y += 28
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 20

# ── Two-column facts ──
mid = WIDTH // 2
col_w = 460

# Left box
lbox_h = 200
draw.rounded_rectangle([(30, y), (30+col_w, y+lbox_h)], radius=8,
                        fill="#EBF8FF", outline="#90CDF4", width=2)
draw.text((30+col_w//2, y+18), "Rail conference keynote", fill=STEEL,
          font=font("Arial Bold.ttf", 20), anchor="mm")
draw.text((30+col_w//2, y+52), "celebrating America's", fill=DARK,
          font=f_sub_b, anchor="mm")
draw.text((30+col_w//2, y+82), "high-speed rail future", fill=DARK,
          font=f_sub_b, anchor="mm")
draw.text((30+col_w//2, y+120), "May 14, 2026", fill=MUTED,
          font=f_sub, anchor="mm")

# Right box
rx = WIDTH - 30 - col_w
draw.rounded_rectangle([(rx, y), (rx+col_w, y+lbox_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+18), "His party's FY2026 budget",
          fill="#C53030", font=font("Arial Bold.ttf", 20), anchor="mm")
draw.text((rx+col_w//2, y+52), "cuts Amtrak to", fill=DARK,
          font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+82), "$2.3 billion", fill="#C53030",
          font=font("Impact.ttf", 58), anchor="mm")
draw.text((rx+col_w//2, y+130), "$127M below request", fill=MUTED,
          font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+158), "$1.77B below FY2025 transit", fill=MUTED,
          font=f_small, anchor="mm")

y += lbox_h + 20
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# ── Also ──
draw.text((WIDTH//2, y), "His own rail bill (H.R. 3548, 119th Congress)?",
          fill=DARK, font=f_sub_b, anchor="mm")
y += 30
draw.text((WIDTH//2, y), "A tort liability reform bill. Not a rail investment.", fill=MUTED,
          font=f_sub, anchor="mm")
y += 40

draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

draw.text((WIDTH//2, y), "Source: House Appropriations THUD Subcommittee  ·  congress.gov H.R. 3548",
          fill=MUTED, font=f_small, anchor="mm")
y += 24
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-14-high-speed-rail-infrastructure-missing-context",
          fill=MUTED, font=f_small, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-28), "langworthywatch.org  ·  NY-23 Accountability", fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/rail_missing_context.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
