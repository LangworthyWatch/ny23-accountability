#!/usr/bin/env python3
"""Post 7: THE MACHINE — $75.7M in lobbying."""

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

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 22)
f_headline = font("Arial Bold.ttf", 38)
f_big = font("Impact.ttf", 110)
f_big_unit = font("Impact.ttf", 60)
f_label = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 24)
f_body_bold = font("Arial Bold.ttf", 24)
f_company = font("Arial Bold.ttf", 24)
f_amount = font("Arial Bold.ttf", 24)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Headline
y = 95
draw.text((WIDTH // 2, y), "Energy Sector Lobbying", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 46), "in Albany (2015-2024)", fill=MUTED, font=f_label, anchor="mm")

# Big number
y = 200
draw.text((WIDTH // 2 - 50, y), "$75.7", fill=NAVY, font=f_big, anchor="mt")
bbox_big = draw.textbbox((WIDTH // 2 - 50, y), "$75.7", font=f_big, anchor="mt")
draw.text((bbox_big[2] + 5, bbox_big[3]), "M", fill=NAVY, font=f_big_unit, anchor="lb")

# Sub-stat
y = 340
draw.rounded_rectangle(
    [(100, y), (WIDTH - 100, y + 55)],
    radius=8, fill="#FFF5F5", outline=RED, width=1
)
draw.text((WIDTH // 2, y + 27), "87.7% ($62.9M) on rate-case-related policy", fill=RED, font=f_body_bold, anchor="mm")

# Trend
y = 425
draw.text((WIDTH // 2, y), "Annual spend nearly tripled:", fill=MUTED, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 35), "$3.4M (2011)  →  $8.4M (2024)", fill=DARK, font=f_body_bold, anchor="mm")

# Divider
y = 500
draw.line([(80, y), (WIDTH - 80, y)], fill=LIGHT_BORDER, width=2)

# Top spenders table
y = 530
draw.text((WIDTH // 2, y), "Top Lobbying Spenders", fill=DARK, font=f_label, anchor="mm")

spenders = [
    ("Business Council of NYS", "$8.91M"),
    ("Entergy Corp", "$5.58M"),
    ("National Grid", "$5.50M"),
    ("NRG Energy", "$4.72M"),
    ("Avangrid (NYSEG+RG&E)", "$4.65M"),
    ("Consolidated Edison", "$4.06M"),
]

sy = y + 45
for company, amount in spenders:
    draw.text((90, sy), company, fill=DARK, font=f_company, anchor="lm")
    draw.text((WIDTH - 90, sy), amount, fill=ACCENT, font=f_amount, anchor="rm")
    sy += 48

# Divider
y = sy + 10
draw.line([(80, y), (WIDTH - 80, y)], fill=LIGHT_BORDER, width=2)

# Key context
y += 20
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 120)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)
draw.text((WIDTH // 2, y + 30), "All 7 PSC commissioners who approve rates", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 60), "are appointed by Governor + confirmed by Senate.", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 92), "1,754 lobbying filings. 7 commissioners.", fill=GOLD, font=f_body_bold, anchor="mm")

# Source
y += 150
draw.text((WIDTH // 2, y), "Source: COELIG/JCOPE lobbying disclosures (public records)", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post07_lobbying.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
