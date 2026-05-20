#!/usr/bin/env python3
"""Generic Open Graph image for LangworthyWatch.org — works on every page."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 630
FONT_DIR = "/System/Library/Fonts/Supplemental/"

NAVY = "#1E3A5F"
WHITE = "#FFFFFF"
ACCENT = "#2B6CB0"
GOLD = "#D69E2E"
MUTED = "#A0AEC0"
LIGHT_BLUE = "#EBF4FF"
LIGHT_GRAY = "#E2E8F0"
DARK = "#1A202C"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 56)
f_tagline = font("Arial.ttf", 28)
f_section_head = font("Arial Bold.ttf", 18)
f_topic = font("Arial Bold.ttf", 22)
f_topic_detail = font("Arial.ttf", 17)
f_county = font("Arial.ttf", 16)
f_url = font("Arial Bold.ttf", 20)
f_divider = font("Arial Bold.ttf", 16)

img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# --- Left panel: Navy ---
panel_w = 540
draw.rectangle([(0, 0), (panel_w, HEIGHT)], fill=NAVY)

# Brand
draw.text((50, 110), "LangworthyWatch", fill=WHITE, font=f_brand, anchor="lm")

# Gold accent line
draw.rectangle([(50, 150), (170, 156)], fill=GOLD)

# Tagline
draw.text((50, 185), "Fact-checking NY-23 with public data.", fill=MUTED, font=f_tagline, anchor="lm")
draw.text((50, 220), "No opinion. No party. Just sources.", fill=MUTED, font=f_tagline, anchor="lm")

# District info
y = 310
draw.text((50, y), "NY-23  |  119th Congress", fill=GOLD, font=f_divider, anchor="lm")
y += 32
draw.text((50, y), "Allegany  \u00b7  Cattaraugus  \u00b7  Chautauqua  \u00b7  Chemung", fill="#718096", font=f_county, anchor="lm")
y += 22
draw.text((50, y), "Erie  \u00b7  Schuyler  \u00b7  Steuben  \u00b7  Tioga", fill="#718096", font=f_county, anchor="lm")

# URL
draw.text((50, HEIGHT - 50), "langworthywatch.org", fill=GOLD, font=f_url, anchor="lm")

# --- Right panel: What we cover ---
right_x = panel_w + 50
stat_center = panel_w + (WIDTH - panel_w) // 2

# Header
draw.rectangle([(panel_w, 0), (WIDTH, 50)], fill=LIGHT_BLUE)
draw.text((stat_center, 25), "WHAT WE TRACK", fill=ACCENT, font=f_section_head, anchor="mm")

topics = [
    ("Fact Checks", "Statements vs. voting record", "\u00b7  30+ entries with sourced verdicts"),
    ("Utility Rates", "Who's really driving your bill", "\u00b7  PSC rate case data + cost breakdown"),
    ("Campaign Finance", "Donors, lobbying, FEC filings", "\u00b7  Public records, downloadable data"),
    ("Correspondence", "Constituent letters + responses", "\u00b7  Response times and form letter tracking"),
    ("Voting Record", "Every vote, linked to Congress.gov", "\u00b7  Floor votes + committee activity"),
]

y_start = 75
topic_h = 95

for i, (title, subtitle, detail) in enumerate(topics):
    y = y_start + i * topic_h

    # Gold bullet
    draw.ellipse([(right_x, y + 12), (right_x + 10, y + 22)], fill=GOLD)

    # Title
    draw.text((right_x + 22, y + 8), title, fill=DARK, font=f_topic, anchor="lm")

    # Subtitle
    draw.text((right_x + 22, y + 38), subtitle, fill="#4A5568", font=f_topic_detail, anchor="lm")

    # Detail
    draw.text((right_x + 22, y + 60), detail, fill=MUTED, font=f_topic_detail, anchor="lm")

    # Separator
    if i < len(topics) - 1:
        sep_y = y + topic_h - 10
        draw.line([(panel_w + 40, sep_y), (WIDTH - 40, sep_y)], fill=LIGHT_GRAY, width=1)

# Bottom bar
draw.rectangle([(panel_w, HEIGHT - 50), (WIDTH, HEIGHT)], fill=LIGHT_BLUE)
draw.text((stat_center, HEIGHT - 25), "All sources linked  \u00b7  All data downloadable",
          fill=ACCENT, font=f_county, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/static/images/og-image.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
