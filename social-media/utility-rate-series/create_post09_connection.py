#!/usr/bin/env python3
"""Post 9: THE CONNECTION — Avangrid donated to Langworthy while requesting rate hike."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1350
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG = "#F5F7FA"
CARD = "#FFFFFF"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
GREEN = "#38A169"
GOLD = "#D69E2E"
MUTED = "#718096"
ACCENT = "#2B6CB0"
LIGHT_BORDER = "#E2E8F0"
LIGHT_RED = "#FFF5F5"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 22)
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 36)
f_subhead = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_entity = font("Arial Bold.ttf", 30)
f_amount = font("Impact.ttf", 52)
f_detail = font("Arial.ttf", 22)
f_arrow_big = font("Arial Bold.ttf", 48)
f_kicker = font("Arial Bold.ttf", 28)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Tag
y = 82
tag = "FOLLOW THE MONEY"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle([((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
                        radius=6, fill=GOLD)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF", font=f_tag, anchor="mm")

# Headline
y = 140
draw.text((WIDTH // 2, y), "The Utility Requesting", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 46), "Your Rate Increase", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 92), "Donated to Your Congressman", fill=RED, font=f_headline, anchor="mm")

# --- Flow diagram ---
# Box 1: Avangrid
y = 290
draw.rounded_rectangle(
    [(100, y), (WIDTH - 100, y + 110)],
    radius=12, fill=NAVY
)
draw.text((WIDTH // 2, y + 30), "Avangrid Inc.", fill="#FFFFFF", font=f_entity, anchor="mm")
draw.text((WIDTH // 2, y + 65), "Parent company of NYSEG", fill="#A0C4E8", font=f_detail, anchor="mm")
draw.text((WIDTH // 2, y + 90), "Requesting 18.4% rate increase in NY-23", fill="#FFD700", font=f_detail, anchor="mm")

# Arrow
y = 405
draw.text((WIDTH // 2, y), "↓", fill=GOLD, font=f_arrow_big, anchor="mm")

# Amount
y = 445
draw.text((WIDTH // 2, y), "$1,500", fill=GOLD, font=f_amount, anchor="mt")
draw.text((WIDTH // 2, y + 60), "campaign donation", fill=MUTED, font=f_detail, anchor="mm")

# Arrow
y = 525
draw.text((WIDTH // 2, y), "↓", fill=GOLD, font=f_arrow_big, anchor="mm")

# Box 2: Langworthy
y = 560
draw.rounded_rectangle(
    [(100, y), (WIDTH - 100, y + 110)],
    radius=12, fill="#4A5568"
)
draw.text((WIDTH // 2, y + 30), "Langworthy for Congress", fill="#FFFFFF", font=f_entity, anchor="mm")
draw.text((WIDTH // 2, y + 65), "Rep. Nick Langworthy (R, NY-23)", fill="#FFD0D0", font=f_detail, anchor="mm")
draw.text((WIDTH // 2, y + 90), "FEC Committee C00817932", fill="#FFD0D0", font=f_detail, anchor="mm")

# Divider
y = 710
draw.line([(80, y), (WIDTH - 80, y)], fill=LIGHT_BORDER, width=2)

# Context card
y = 740
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 175)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

items = [
    ("Langworthy says:", "\"Clean energy makes bills unaffordable\"", DARK),
    ("Clean energy's actual share:", "4.7% of NYSEG's rate request", GREEN),
    ("Langworthy's position on the rate case:", "(silence)", RED),
]

iy = y + 20
for label, value, color in items:
    draw.text((100, iy), label, fill=MUTED, font=f_detail, anchor="lm")
    draw.text((100, iy + 26), value, fill=color, font=f_body_bold, anchor="lm")
    iy += 56

# Kicker
y = 990
draw.text((WIDTH // 2, y), "Langworthy has not publicly commented", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 40), "on the pending rate case.", fill=DARK, font=f_body, anchor="mm")

# Source
y = 1100
draw.text((WIDTH // 2, y), "Source: FEC individual contributions (fec.gov)", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "Committee C00817932 | PSC case 25-E-0375", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 48), "Full investigation: langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post09_connection.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
