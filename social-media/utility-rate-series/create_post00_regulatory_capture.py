#!/usr/bin/env python3
"""Post 0: WHAT IS REGULATORY CAPTURE? — Concept explainer with NY utility pipeline."""

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
LIGHT_BLUE = "#EBF4FF"
LIGHT_GOLD = "#FFFFF0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 22)
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 42)
f_subhead = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 24)
f_body_bold = font("Arial Bold.ttf", 24)
f_step_num = font("Impact.ttf", 36)
f_step_text = font("Arial Bold.ttf", 22)
f_step_detail = font("Arial.ttf", 19)
f_kicker = font("Arial Bold.ttf", 26)
f_source = font("Arial.ttf", 17)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# Tag
y = 80
tag = "EXPLAINER"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle([((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
                        radius=6, fill=ACCENT)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF", font=f_tag, anchor="mm")

# Headline
y = 130
draw.text((WIDTH // 2, y), "What Is", fill=DARK, font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 52), "Regulatory Capture?", fill=RED, font=f_headline, anchor="mm")

# Definition
y = 230
draw.text((WIDTH // 2, y), "When the agency meant to regulate", fill=MUTED, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 32), "an industry is instead controlled by it.", fill=MUTED, font=f_body, anchor="mm")

# --- Pipeline steps ---
steps = [
    ("1", "LOBBY", "$75.7M in energy sector lobbying\n87.7% on rate-case policy", NAVY, LIGHT_BLUE),
    ("2", "APPOINT", "Governor nominates, Senate confirms\nall 7 PSC commissioners who set your rates", ACCENT, LIGHT_BLUE),
    ("3", "REVOLVE", "PSC Chair previously worked at\nKeySpan Energy (now National Grid)", RED, LIGHT_RED),
    ("4", "APPROVE", "PSC approves rate increases with\nguaranteed 9% profit for shareholders", GOLD, LIGHT_GOLD),
    ("5", "PROFIT", "Shareholders received $36.8B\nCEO pay grew 64%. Your rates: 42%.", RED, LIGHT_RED),
    ("6", "BLAME", "Utilities blame \"clean energy\"\nwhich is 4.7% of the increase", NAVY, LIGHT_BLUE),
]

step_height = 105
step_gap = 12
y_start = 310
margin = 65

for i, (num, title, detail, color, bg_color) in enumerate(steps):
    y = y_start + i * (step_height + step_gap)

    # Step card
    draw.rounded_rectangle(
        [(margin, y), (WIDTH - margin, y + step_height)],
        radius=10, fill=bg_color, outline=color, width=2
    )

    # Number circle
    cx = margin + 40
    cy = y + step_height // 2
    draw.ellipse([(cx - 22, cy - 22), (cx + 22, cy + 22)], fill=color)
    draw.text((cx, cy), num, fill="#FFFFFF", font=f_step_num, anchor="mm")

    # Title
    draw.text((cx + 40, y + 18), title, fill=color, font=f_step_text, anchor="lm")

    # Detail (two lines)
    detail_lines = detail.split("\n")
    for li, line in enumerate(detail_lines):
        draw.text((cx + 40, y + 48 + li * 24), line, fill=DARK, font=f_step_detail, anchor="lm")

    # Arrow between steps
    if i < len(steps) - 1:
        arrow_y = y + step_height + step_gap // 2
        # Draw a solid triangle arrow
        cx = WIDTH // 2
        draw.polygon([(cx - 10, arrow_y - 6), (cx + 10, arrow_y - 6), (cx, arrow_y + 6)], fill=NAVY)

# Kicker
y = y_start + 6 * (step_height + step_gap) + 15
draw.text((WIDTH // 2, y), "This is how your electric bill works.", fill=DARK, font=f_kicker, anchor="mm")
draw.text((WIDTH // 2, y + 36), "Every step is documented with data.", fill=GOLD, font=f_kicker, anchor="mm")

# Source
y = y + 80
draw.text((WIDTH // 2, y), "Sources: COELIG/JCOPE lobbying, PSC bios, FERC Form 1, EIA", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 22), "Full data investigation at langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post00_regulatory_capture.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
