#!/usr/bin/env python3
"""Social card: "You spoke. I listened." — responsiveness asymmetry — DOCUMENTED PATTERN — June 24, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG     = "#F5F7FA"
NAVY   = "#1E3A5F"
DARK   = "#1A202C"
GREEN  = "#276749"
RED    = "#E53E3E"
ORANGE = "#C05621"
GOLD   = "#D69E2E"
MUTED  = "#718096"
BORDER = "#E2E8F0"
WHITE  = "#FFFFFF"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand  = font("Arial Bold.ttf", 22)
f_tag    = font("Arial Bold.ttf", 20)
f_topic  = font("Arial Bold.ttf", 40)
f_sub    = font("Arial.ttf", 20)
f_label  = font("Arial Bold.ttf", 19)
f_body   = font("Arial.ttf", 20)
f_bodyb  = font("Arial Bold.ttf", 20)
f_small  = font("Arial.ttf", 15)
f_smallb = font("Arial Bold.ttf", 15)
f_bullet = font("Arial.ttf", 19)
f_arrow  = font("Arial Bold.ttf", 22)
f_note_b = font("Arial Bold.ttf", 18)
f_note   = font("Arial.ttf", 17)
f_src    = font("Arial.ttf", 17)
f_footer = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH//2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62
# Badge
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")

# Topic
draw.text((WIDTH//2, 132), '"You spoke. I listened."', fill=NAVY, font=f_topic, anchor="mm")
draw.text((WIDTH//2, 172), "What it takes to get Rep. Langworthy's attention", fill=MUTED, font=f_sub, anchor="mm")
draw.line([(60, 196), (WIDTH-60, 196)], fill=BORDER, width=2)

# GREEN box — what got an answer
gy = 208
draw.rounded_rectangle([(44, gy), (WIDTH-44, gy+150)], radius=8, fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, gy+22), "ANSWERED IN DAYS, IN PERSON", fill=GREEN, font=f_label, anchor="lm")
draw.text((76, gy+54), "Animal-welfare advocates asked him to look into Marshall Farms.", fill=DARK, font=f_body, anchor="lm")
draw.text((76, gy+82), "He visited the site himself and released video.", fill=DARK, font=f_body, anchor="lm")
draw.text((76, gy+114), "Ridglan Farms: Wisconsin.    Marshall Farms: North Rose (NY-24, Rep. Tenney).", fill=MUTED, font=f_small, anchor="lm")
draw.text((76, gy+134), "Neither is in NY-23.", fill=ORANGE, font=f_smallb, anchor="lm")

# RED box — still waiting
ry = gy + 150 + 16
rh = 300
draw.rounded_rectangle([(44, ry), (WIDTH-44, ry+rh)], radius=8, fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((WIDTH//2, ry+24), "STILL WAITING IN NY-23", fill=RED, font=f_label, anchor="mm")
bullets = [
    "No in-person town hall in over three years",
    "Constituent mail answered with form letters",
    "(one reply arrived 6 days after the bill became law)",
    "8 hospitals at risk of closure, the most in New York",
    "Chautauqua County layoffs; a Springville nursing home closing",
    "No posts about any of it",
]
by = ry + 56
for i, b in enumerate(bullets):
    indent = (i == 2)  # continuation line of bullet 2
    if not indent:
        draw.text((78, by), "→", fill=RED, font=f_arrow, anchor="lm")
    draw.text((112 if not indent else 134, by), b, fill=DARK, font=f_bullet, anchor="lm")
    by += 40

# Closer box
cy = ry + rh + 16
ch = 90
draw.rounded_rectangle([(44, cy), (WIDTH-44, cy+ch)], radius=6, fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, cy+30), "Caring about animals is good. So is answering the people you represent.", fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, cy+58), "What does a NY-23 constituent have to do to get the same response?", fill=MUTED, font=f_note, anchor="mm")

# Sources + URL
sy = cy + ch + 22
draw.text((WIDTH//2, sy), "Sources: Langworthy Facebook (May 12, 2026)  ·  NY-23 constituent-access & correspondence records",
          fill=MUTED, font=f_src, anchor="mm")
draw.text((WIDTH//2, sy+26), "langworthywatch.org/fact-checks/2026-05-22-beagle-posts-credit-claiming-distraction/",
          fill=NAVY, font=f_src, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability", fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/responsiveness_you_spoke.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
