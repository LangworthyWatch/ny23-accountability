#!/usr/bin/env python3
"""Post 10: THE CTA — Read the full investigation."""

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
f_headline = font("Arial Bold.ttf", 42)
f_subhead = font("Arial Bold.ttf", 30)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_stat_num = font("Impact.ttf", 56)
f_stat_label = font("Arial.ttf", 22)
f_url = font("Arial Bold.ttf", 24)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Headline
y = 110
draw.text((WIDTH // 2, y), "Data. Sources.", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 55), "No Opinion.", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 115), "Judge for yourself.", fill=ACCENT, font=f_subhead, anchor="mm")

# --- Stats grid (2x2) ---
y = 310
grid = [
    ("4.7%", "clean energy share\nof rate increases", RED),
    ("49.7%", "above national\naverage", NAVY),
    ("+84%", "complaint surge\n(2019–2024)", RED),
    ("$36.8B", "shareholder dividends\nvs $7B clean energy", GOLD),
]

cell_w = (WIDTH - 120) // 2
cell_h = 170

for i, (num, label, color) in enumerate(grid):
    col = i % 2
    row = i // 2
    cx = 60 + col * cell_w + cell_w // 2
    cy = y + row * (cell_h + 20) + cell_h // 2

    # Card background
    x1 = 60 + col * cell_w + (10 if col == 1 else 0)
    x2 = x1 + cell_w - (10 if col == 0 else 0)
    y1 = y + row * (cell_h + 20)
    y2 = y1 + cell_h
    draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=12, fill=CARD, outline=LIGHT_BORDER, width=1)

    # Number
    draw.text((cx, y1 + 30), num, fill=color, font=f_stat_num, anchor="mt")

    # Label (multiline)
    label_lines = label.split("\n")
    for li, line in enumerate(label_lines):
        draw.text((cx, y1 + 100 + li * 28), line, fill=MUTED, font=f_stat_label, anchor="mm")

# --- What's included ---
y = 720
draw.text((WIDTH // 2, y), "The full investigation includes:", fill=DARK, font=f_subhead, anchor="mm")

items = [
    "6 interactive data charts",
    "4 downloadable CSV datasets",
    "Every source linked (PSC, EIA, FERC, SEC, Census)",
    "No paywalls, no ads, no party affiliation",
]

iy = y + 50
for item in items:
    draw.text((120, iy), "→", fill=ACCENT, font=f_body_bold, anchor="lm")
    draw.text((160, iy), item, fill=DARK, font=f_body, anchor="lm")
    iy += 44

# --- URL card ---
y = 960
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 130)],
    radius=12, fill=NAVY
)
draw.text((WIDTH // 2, y + 40), "Who's really driving your electric bill?", fill="#FFFFFF", font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 85), "langworthywatch.org", fill=GOLD, font=f_subhead, anchor="mm")

# --- Share line ---
y = 1130
draw.text((WIDTH // 2, y), "Share if you think your neighbors", fill=MUTED, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 36), "should see this data.", fill=ACCENT, font=f_body_bold, anchor="mm")

# Source
y = 1220
draw.text((WIDTH // 2, y), "All data from public government sources", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post10_cta.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
