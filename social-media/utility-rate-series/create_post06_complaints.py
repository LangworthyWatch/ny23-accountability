#!/usr/bin/env python3
"""Post 6: THE COMPLAINTS — +84% consumer complaints."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1350
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG = "#F5F7FA"
CARD = "#FFFFFF"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
MUTED = "#718096"
ACCENT = "#2B6CB0"
LIGHT_BORDER = "#E2E8F0"
GOLD = "#D69E2E"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 22)
f_headline = font("Arial Bold.ttf", 38)
f_big = font("Impact.ttf", 180)
f_label = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_stat_num = font("Arial Bold.ttf", 40)
f_stat_label = font("Arial.ttf", 22)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Headline
y = 100
draw.text((WIDTH // 2, y), "Consumer Complaints to", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 48), "the PSC Grew", fill=DARK, font=f_headline, anchor="mm")

# Big number
y = 220
draw.text((WIDTH // 2, y), "+84%", fill=RED, font=f_big, anchor="mt")

# Subline
y = 440
draw.text((WIDTH // 2, y), "in just 5 years (2019–2024)", fill=MUTED, font=f_label, anchor="mm")

# Arrow: complaint counts
y = 510
draw.text((WIDTH // 2, y), "24,146  →  44,538", fill=DARK, font=f_stat_num, anchor="mm")
draw.text((WIDTH // 2, y + 45), "statewide complaints per year", fill=MUTED, font=f_stat_label, anchor="mm")

# Divider
y = 600
draw.line([(100, y), (WIDTH - 100, y)], fill=LIGHT_BORDER, width=2)

# Key stats card
y = 640
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 320)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

stats = [
    ("Billing complaints specifically:", "+120%", RED),
    ("NYSEG complaints:", "+95%", RED),
    ("RG&E complaints:", "+94%", RED),
    ("", "", ""),
    ("Same parent company (Avangrid).", "", MUTED),
    ("Same 18% rate increase request.", "", RED),
]

sy = y + 25
for label, value, color in stats:
    if not label and not value:
        sy += 15
        continue
    if value:
        draw.text((100, sy), label, fill=DARK, font=f_body, anchor="lm")
        draw.text((WIDTH - 100, sy), value, fill=color, font=f_body_bold, anchor="rm")
    else:
        draw.text((WIDTH // 2, sy), label, fill=color, font=f_body_bold, anchor="mm")
    sy += 48

# Kicker
y = 1020
draw.text((WIDTH // 2, y), "People are telling regulators", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 36), "they can't afford their bills.", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 85), "The utilities keep filing for more.", fill=GOLD, font=f_body_bold, anchor="mm")

# Source
y = 1185
draw.text((WIDTH // 2, y), "Source: PSC consumer complaint data, 2019–2024", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post06_complaints.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
