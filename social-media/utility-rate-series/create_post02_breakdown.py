#!/usr/bin/env python3
"""Post 2: THE BREAKDOWN — Horizontal bar chart of rate increase cost drivers."""

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
f_headline = font("Arial Bold.ttf", 36)
f_subhead = font("Arial.ttf", 26)
f_bar_label = font("Arial.ttf", 22)
f_bar_pct = font("Arial Bold.ttf", 24)
f_bar_amt = font("Arial.ttf", 20)
f_callout = font("Arial Bold.ttf", 26)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Headline
draw.text((WIDTH // 2, 100), "Where Your Rate Increase", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, 142), "Actually Goes", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, 190), "8 rate cases, $4.0 billion in requested increases", fill=MUTED, font=f_subhead, anchor="mm")

# Bar chart data
bars = [
    ("Infrastructure & Capital", 33.7, "$1,355M", NAVY),
    ("Operations & Maintenance", 16.7, "$672M", "#2D5A8A"),
    ("Storm Recovery", 12.5, "$504M", ACCENT),
    ("Shareholder Profit (ROE)", 10.1, "$408M", RED),
    ("Property Taxes", 8.6, "$348M", "#718096"),
    ("Depreciation", 6.0, "$242M", "#A0AEC0"),
    ("Labor & Benefits", 2.3, "$91M", "#CBD5E0"),
    ("Clean Energy Programs", 4.7, "$187M", GREEN),
]

# Drawing area
bar_left = 80
bar_max_width = 680
bar_height = 48
label_gap = 6     # gap between label and bar top
row_gap = 16      # gap between bar bottom and next label
y_start = 240
label_right = bar_left - 10

max_pct = 33.7  # scale factor

for i, (label, pct, amount, color) in enumerate(bars):
    # Label baseline sits label_gap px above the bar top
    label_y = y_start + i * (bar_height + label_gap + row_gap + 24) + 24
    bar_y = label_y + label_gap

    # Label above bar
    draw.text((bar_left, label_y), label, fill=DARK, font=f_bar_label, anchor="lb")

    # Bar
    bar_width = int((pct / max_pct) * bar_max_width)
    draw.rounded_rectangle(
        [(bar_left, bar_y), (bar_left + bar_width, bar_y + bar_height)],
        radius=6, fill=color
    )

    # Percentage inside or after bar
    pct_text = f"{pct}%"
    if bar_width > 120:
        draw.text((bar_left + bar_width - 12, bar_y + bar_height // 2),
                  pct_text, fill="#FFFFFF", font=f_bar_pct, anchor="rm")
    else:
        draw.text((bar_left + bar_width + 10, bar_y + bar_height // 2),
                  pct_text, fill=color, font=f_bar_pct, anchor="lm")

    # Amount to the right
    draw.text((WIDTH - 60, bar_y + bar_height // 2), amount, fill=MUTED, font=f_bar_amt, anchor="rm")

# Callout box
last_bar_bottom = y_start + len(bars) * (bar_height + label_gap + row_gap + 24) + 24 + label_gap + bar_height
y_callout = last_bar_bottom + 30
draw.rounded_rectangle(
    [(60, y_callout), (WIDTH - 60, y_callout + 120)],
    radius=12, fill="#FFF5F5", outline=RED, width=2
)
draw.text((WIDTH // 2, y_callout + 35),
          "The thing politicians talk about most", fill=DARK, font=f_callout, anchor="mm")
draw.text((WIDTH // 2, y_callout + 75),
          "is the smallest bar on the chart.", fill=RED, font=f_callout, anchor="mm")

# Source
y_src = y_callout + 140
draw.text((WIDTH // 2, y_src), "Source: PSC rate case filings (dps.ny.gov)", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y_src + 26), "All data downloadable at langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer bar
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post02_breakdown.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
