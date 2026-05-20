#!/usr/bin/env python3
"""Post 5: THE BURDEN — Upstate counties pay more as share of income."""

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
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 38)
f_subhead = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_county = font("Arial Bold.ttf", 26)
f_pct = font("Impact.ttf", 48)
f_income = font("Arial.ttf", 20)
f_bar_label = font("Arial.ttf", 20)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Tag
y = 82
tag = "NY-23 DATA"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle([((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
                        radius=6, fill=RED)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF", font=f_tag, anchor="mm")

# Headline
y = 140
draw.text((WIDTH // 2, y), "Same Rate Increase.", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 48), "Different Impact.", fill=RED, font=f_headline, anchor="mm")

# Subtitle
y = 250
draw.text((WIDTH // 2, y), "Electricity cost as % of household income", fill=MUTED, font=f_body, anchor="mm")

# County comparison — horizontal bars
counties = [
    ("Bronx", 4.17, "$40,233", RED),
    ("Chautauqua", 3.02, "$46,543", RED),
    ("Steuben", 2.74, "$51,234", "#E07040"),
    ("Chemung", 2.68, "$52,640", "#E07040"),
    ("Tioga", 2.38, "$59,272", GOLD),
    ("Allegany", 2.62, "$48,795", "#E07040"),
    ("Westchester", 1.45, "$109,383", GREEN),
    ("Nassau", 1.28, "$124,832", GREEN),
]

y_start = 310
bar_left = 220
bar_max_w = 520
bar_h = 44
bar_gap = 14
max_pct = 4.5

for i, (county, pct, income, color) in enumerate(counties):
    y = y_start + i * (bar_h + bar_gap)

    # County name
    draw.text((bar_left - 15, y + bar_h // 2), county, fill=DARK, font=f_county, anchor="rm")

    # Bar
    bar_w = int((pct / max_pct) * bar_max_w)
    draw.rounded_rectangle([(bar_left, y), (bar_left + bar_w, y + bar_h)],
                            radius=6, fill=color)

    # Percentage
    if bar_w > 100:
        draw.text((bar_left + bar_w - 10, y + bar_h // 2), f"{pct}%",
                  fill="#FFFFFF", font=f_body_bold, anchor="rm")
    else:
        draw.text((bar_left + bar_w + 8, y + bar_h // 2), f"{pct}%",
                  fill=color, font=f_body_bold, anchor="lm")

    # Income label (right side)
    draw.text((WIDTH - 50, y + bar_h // 2), income, fill=MUTED, font=f_income, anchor="rm")

# Label for income column
draw.text((WIDTH - 50, y_start - 20), "Median income", fill=MUTED, font=f_income, anchor="rm")

# Divider
y = y_start + 8 * (bar_h + bar_gap) + 15
draw.line([(80, y), (WIDTH - 80, y)], fill=LIGHT_BORDER, width=2)

# Key insight card
y += 20
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 160)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

draw.text((WIDTH // 2, y + 25), "Lowest income quartile:", fill=MUTED, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 60), "2.99% of income on electricity", fill=RED, font=f_body_bold, anchor="mm")

draw.text((WIDTH // 2, y + 100), "Highest income quartile:", fill=MUTED, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 135), "1.85% of income on electricity", fill=GREEN, font=f_body_bold, anchor="mm")

# NYSEG callout
y += 185
draw.text((WIDTH // 2, y), "NYSEG territory — the poorest counties —", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 34), "gets the steepest increase: 18.4%", fill=RED, font=f_body_bold, anchor="mm")

# Source
y += 80
draw.text((WIDTH // 2, y), "Source: EIA electricity prices, Census ACS 2022", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post05_burden.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
