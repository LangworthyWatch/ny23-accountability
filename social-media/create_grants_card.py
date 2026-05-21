#!/usr/bin/env python3
"""Social card: Federal Grants Credit-Claiming — DOCUMENTED PATTERN — May 20, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
PURPLE  = "#553C9A"   # DOCUMENTED PATTERN colour
PURPLE_BG = "#FAF5FF"
PURPLE_BD = "#D6BCFA"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"
GOLD    = "#D69E2E"
GREEN   = "#276749"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 24)
f_tag     = font("Arial Bold.ttf", 22)
f_topic   = font("Arial Bold.ttf", 34)
f_label   = font("Arial Bold.ttf", 22)
f_claim   = font("Arial.ttf", 26)
f_claim_b = font("Arial Bold.ttf", 26)
f_big     = font("Impact.ttf", 120)
f_big2    = font("Impact.ttf", 72)
f_sub     = font("Arial.ttf", 22)
f_sub_b   = font("Arial Bold.ttf", 22)
f_small   = font("Arial.ttf", 19)
f_footer  = font("Arial Bold.ttf", 22)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 52)], fill=NAVY)
draw.text((WIDTH//2, 26), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 74

# ── Verdict badge ──
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+14
tx = (WIDTH-tw)//2
draw.rounded_rectangle([(tx, y), (tx+tw, y+th)], radius=5, fill=PURPLE)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 12

draw.text((WIDTH//2, y), "Federal Funding", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# ── The week ──
box_h = 116
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill=PURPLE_BG, outline=PURPLE_BD, width=2)
draw.text((WIDTH//2, y+20), "4 announcements in 7 days — May 13–20, 2026", fill=PURPLE,
          font=f_label, anchor="mm")
draw.text((WIDTH//2, y+56), '"I\'m proud to deliver for my district."', fill=DARK,
          font=font("Arial.ttf", 28), anchor="mm")
draw.text((WIDTH//2, y+88), '"I will always fight to ensure our fair share."', fill=DARK,
          font=font("Arial.ttf", 24), anchor="mm")
y += box_h + 18

# ── The number ──
num_box_h = 148
draw.rounded_rectangle([(44, y), (WIDTH-44, y+num_box_h)], radius=8,
                        fill=PURPLE_BG, outline=PURPLE_BD, width=2)
draw.text((WIDTH//2, y+16), "Total announced:", fill=MUTED, font=f_sub_b, anchor="mm")
draw.text((WIDTH//2, y+90), "$16.6M", fill=PURPLE, font=f_big, anchor="mm")
y += num_box_h + 16

# ── What they actually are ──
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

draw.text((WIDTH//2, y), "What these grants actually are:", fill=DARK,
          font=f_sub_b, anchor="mm")
y += 32

grants = [
    ("$3.2M water",   "USDA Rural Development formula grant"),
    ("$7.7M health",  "HHS/SAMHSA community grant"),
    ("$5.7M airport", "FAA Airport Improvement Program formula"),
]
row_h = 52
for label, desc in grants:
    draw.rounded_rectangle([(44, y), (WIDTH-44, y+row_h-4)], radius=6,
                            fill=WHITE, outline=BORDER, width=1)
    draw.text((70, y+row_h//2-2), label, fill=PURPLE, font=f_sub_b, anchor="lm")
    draw.text((260, y+row_h//2-2), desc, fill=MUTED, font=f_sub, anchor="lm")
    y += row_h + 4

y += 8
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

draw.text((WIDTH//2, y), "Formula grants. Not earmarks. Applied for by towns.",
          fill=DARK, font=f_sub_b, anchor="mm")
y += 32
draw.text((WIDTH//2, y), "6th documented instance of this pattern in this tracker.",
          fill=MUTED, font=f_sub, anchor="mm")
y += 36

draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

draw.text((WIDTH//2, y), "Sources: USDA Rural Development  ·  FAA AIP  ·  Observer Today",
          fill=MUTED, font=f_small, anchor="mm")
y += 22
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-20-federal-grants-credit-claiming-may2026",
          fill=MUTED, font=f_small, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-28), "langworthywatch.org  ·  NY-23 Accountability", fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/grants_credit_claiming_pattern.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
