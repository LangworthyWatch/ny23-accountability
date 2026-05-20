#!/usr/bin/env python3
"""Post 3: THE GAP — CEO Pay +64% vs Your Rates +42%."""

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
f_headline = font("Arial Bold.ttf", 40)
f_big = font("Impact.ttf", 130)
f_label = font("Arial Bold.ttf", 30)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_detail = font("Arial.ttf", 22)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Tag
y = 85
tag = "2015–2024"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle([((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
                        radius=6, fill=MUTED)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF", font=f_tag, anchor="mm")

# Headline
y = 150
draw.text((WIDTH // 2, y), "CEO Pay vs. Your Bill", fill=DARK, font=f_headline, anchor="mm")

# --- CEO section ---
y = 240
draw.text((WIDTH // 2, y), "CEO Compensation", fill=MUTED, font=f_label, anchor="mm")
draw.text((WIDTH // 2, y), "CEO Compensation", fill=MUTED, font=f_label, anchor="mm")
y = 280
draw.text((WIDTH // 2, y), "+64%", fill=RED, font=f_big, anchor="mt")
y = 420
draw.text((WIDTH // 2, y), "$28.5M → $46.8M (top 3 utility CEOs)", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 38), "National Grid CEO specifically: +78.6%", fill=RED, font=f_body_bold, anchor="mm")

# --- Divider ---
y = 510
draw.line([(120, y), (WIDTH - 120, y)], fill=LIGHT_BORDER, width=3)
draw.text((WIDTH // 2, y), " vs ", fill=MUTED, font=f_label, anchor="mm")

# --- Consumer section ---
y = 550
draw.text((WIDTH // 2, y), "Your Electricity Rate", fill=MUTED, font=f_label, anchor="mm")
y = 590
draw.text((WIDTH // 2, y), "+42%", fill=NAVY, font=f_big, anchor="mt")
y = 730
draw.text((WIDTH // 2, y), "17.7¢ → 25.1¢ per kWh (NY residential avg)", fill=DARK, font=f_body, anchor="mm")

# --- Evidence card ---
y = 810
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 240)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

evidence = [
    ("Shareholder dividends (2015–2024):", "$36.8 BILLION", RED),
    ("Clean energy surcharge (same period):", "$7.0 billion", GREEN),
    ("Ratio:", "5.3x more to shareholders", GOLD),
]
ey = y + 30
for label, value, color in evidence:
    draw.text((100, ey), label, fill=MUTED, font=f_detail, anchor="lm")
    draw.text((WIDTH - 100, ey), value, fill=color, font=f_body_bold, anchor="rm")
    ey += 65

# Source
y = 1120
draw.text((WIDTH // 2, y), "Source: SEC proxy statements, FERC Form 1, EIA", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 26), "Full analysis: langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post03_ceo_gap.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
