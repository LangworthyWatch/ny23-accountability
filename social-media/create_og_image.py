#!/usr/bin/env python3
"""Create Open Graph social media preview image for LangworthyWatch.org.
Standard OG size: 1200x630. Must be readable at ~600x315 thumbnail."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630
FONT_DIR = "/System/Library/Fonts/Supplemental/"

# Site brand palette
NAVY = "#1E3A5F"
NAVY_DARK = "#152A45"
WHITE = "#FFFFFF"
ACCENT = "#2B6CB0"
LIGHT_BLUE = "#EBF4FF"
GOLD = "#D69E2E"
MUTED = "#A0AEC0"
LIGHT_GRAY = "#E2E8F0"
RED = "#E53E3E"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 52)
f_tagline = font("Arial.ttf", 26)
f_stat_num = font("Impact.ttf", 72)
f_stat_label = font("Arial.ttf", 18)
f_stat_label_bold = font("Arial Bold.ttf", 18)
f_divider_text = font("Arial Bold.ttf", 16)
f_url = font("Arial Bold.ttf", 20)
f_county = font("Arial.ttf", 16)

img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# --- Left panel: Navy background ---
panel_w = 520
draw.rectangle([(0, 0), (panel_w, HEIGHT)], fill=NAVY)

# Brand name
draw.text((50, 120), "LangworthyWatch", fill=WHITE, font=f_brand, anchor="lm")

# Accent line
draw.rectangle([(50, 155), (160, 160)], fill=GOLD)

# Tagline
draw.text((50, 190), "Fact-checking NY-23 with public data.", fill=MUTED, font=f_tagline, anchor="lm")
draw.text((50, 224), "No opinion. No party. Just sources.", fill=MUTED, font=f_tagline, anchor="lm")

# Counties listed
y = 310
draw.text((50, y), "NY-23  |  119th Congress", fill=GOLD, font=f_divider_text, anchor="lm")
y += 35
counties = "Allegany  \u00b7  Cattaraugus  \u00b7  Chautauqua  \u00b7  Chemung"
draw.text((50, y), counties, fill="#718096", font=f_county, anchor="lm")
y += 24
counties2 = "Erie  \u00b7  Schuyler  \u00b7  Steuben  \u00b7  Tioga"
draw.text((50, y), counties2, fill="#718096", font=f_county, anchor="lm")

# URL bottom
draw.text((50, HEIGHT - 50), "langworthywatch.org", fill=GOLD, font=f_url, anchor="lm")

# --- Right panel: Key stats ---
right_x = panel_w + 40
stat_center = panel_w + (WIDTH - panel_w) // 2

# Header bar
draw.rectangle([(panel_w, 0), (WIDTH, 50)], fill=LIGHT_BLUE)
draw.text((stat_center, 25), "WHAT THE DATA SHOWS", fill=ACCENT, font=f_divider_text, anchor="mm")

# 3 key stats in a column
stats = [
    ("4.7%", "of rate increases go to", "clean energy", RED),
    ("+84%", "consumer complaint", "surge (2019-2024)", NAVY),
    ("$36.8B", "shareholder dividends vs", "$7B clean energy", GOLD),
]

stat_h = 160
y_start = 75

for i, (num, line1, line2, color) in enumerate(stats):
    y = y_start + i * stat_h
    cy = y + stat_h // 2

    # Number
    draw.text((stat_center - 10, cy - 25), num, fill=color, font=f_stat_num, anchor="mm")

    # Labels
    draw.text((stat_center - 10, cy + 35), line1, fill="#4A5568", font=f_stat_label, anchor="mm")
    draw.text((stat_center - 10, cy + 57), line2, fill=color, font=f_stat_label_bold, anchor="mm")

    # Separator line (except after last)
    if i < len(stats) - 1:
        sep_y = y + stat_h - 5
        draw.line([(panel_w + 60, sep_y), (WIDTH - 60, sep_y)], fill=LIGHT_GRAY, width=1)

# Bottom bar
draw.rectangle([(panel_w, HEIGHT - 50), (WIDTH, HEIGHT)], fill=LIGHT_BLUE)
draw.text((stat_center, HEIGHT - 25), "Sources: PSC  \u00b7  EIA  \u00b7  FERC  \u00b7  FEC  \u00b7  Census",
          fill=ACCENT, font=f_county, anchor="mm")

# Save
out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/og_image_langworthywatch.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")

# Also save to static for Hugo
import shutil
static_path = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/static/images/og-image.png"
shutil.copy(out, static_path)
print(f"Copied to: {static_path}")
