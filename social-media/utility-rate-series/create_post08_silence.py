#!/usr/bin/env python3
"""Post 8: THE SILENCE — 18.4% NYSEG increase, Langworthy silent."""

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
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 36)
f_big = font("Impact.ttf", 160)
f_pct = font("Impact.ttf", 80)
f_label = font("Arial Bold.ttf", 28)
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
tag = "NY-23 ACCOUNTABILITY"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle([((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
                        radius=6, fill=RED)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF", font=f_tag, anchor="mm")

# Headline
y = 145
draw.text((WIDTH // 2, y), "NYSEG's Pending Rate Increase", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 46), "The Steepest in New York", fill=RED, font=f_headline, anchor="mm")

# Big number
y = 270
num_x = WIDTH // 2 - 60
draw.text((num_x, y), "18.4", fill=RED, font=f_big, anchor="mt")
bbox = draw.textbbox((num_x, y), "18.4", font=f_big, anchor="mt")
draw.text((bbox[2] + 5, bbox[3]), "%", fill=RED, font=f_pct, anchor="lb")

# Context
y = 480
draw.text((WIDTH // 2, y), "NYSEG serves most of NY-23:", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 36), "Steuben, Chemung, Tioga, Allegany, Schuyler", fill=ACCENT, font=f_body_bold, anchor="mm")

# Divider
y = 570
draw.line([(100, y), (WIDTH - 100, y)], fill=LIGHT_BORDER, width=2)

# Comparison card
y = 610
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 260)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

draw.text((WIDTH // 2, y + 30), "What Langworthy says:", fill=MUTED, font=f_detail, anchor="mm")
draw.text((WIDTH // 2, y + 65), "\"Clean energy is making your bills unaffordable\"", fill=DARK, font=f_body, anchor="mm")

draw.line([(120, y + 100), (WIDTH - 120, y + 100)], fill=LIGHT_BORDER, width=1)

draw.text((WIDTH // 2, y + 125), "What the rate filing shows:", fill=MUTED, font=f_detail, anchor="mm")

# Mini bars for visual comparison
bar_left = 120
bar_y1 = y + 160
bar_y2 = y + 210

# Infrastructure bar (33.7%)
infra_w = 420
draw.rounded_rectangle([(bar_left, bar_y1), (bar_left + infra_w, bar_y1 + 35)],
                        radius=5, fill=NAVY)
draw.text((bar_left + infra_w + 10, bar_y1 + 17), "Infrastructure 33.7%", fill=DARK, font=f_detail, anchor="lm")

# Clean energy bar (4.7%)
ce_w = int(420 * 4.7 / 33.7)
draw.rounded_rectangle([(bar_left, bar_y2), (bar_left + ce_w, bar_y2 + 35)],
                        radius=5, fill=GREEN)
draw.text((bar_left + ce_w + 10, bar_y2 + 17), "Clean energy 4.7%", fill=DARK, font=f_detail, anchor="lm")

# Kicker
y = 920
draw.text((WIDTH // 2, y), "Rep. Langworthy has not publicly", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 38), "addressed this rate case.", fill=DARK, font=f_body, anchor="mm")

# Evidence box
y = 1020
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 100)],
    radius=12, fill="#FFFFF0", outline=GOLD, width=2
)
draw.text((WIDTH // 2, y + 30), "He blames clean energy (4.7%)", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 68), "and ignores the other 95.3%.", fill=GOLD, font=f_body_bold, anchor="mm")

# Source
y = 1175
draw.text((WIDTH // 2, y), "Source: PSC case 25-E-0375, EIA, Census ACS", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "Full investigation: langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post08_silence.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
