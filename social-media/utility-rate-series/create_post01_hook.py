#!/usr/bin/env python3
"""Post 1: THE HOOK — 4.7% clean energy share. Bright Instagram-optimized graphic."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1350
FONT_DIR = "/System/Library/Fonts/Supplemental/"

# Bright social media palette
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
f_big = font("Impact.ttf", 180)
f_pct = font("Impact.ttf", 90)
f_headline = font("Arial Bold.ttf", 38)
f_body = font("Arial.ttf", 28)
f_body_bold = font("Arial Bold.ttf", 28)
f_evidence = font("Arial.ttf", 24)
f_evidence_bold = font("Arial Bold.ttf", 24)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# --- Top brand bar ---
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# --- Category tag ---
y = 90
tag_text = "DATA INVESTIGATION"
tb = draw.textbbox((0, 0), tag_text, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
pill_x = (WIDTH - tw) // 2 - 16
draw.rounded_rectangle([(pill_x, y), (pill_x + tw + 32, y + th + 16)], radius=6, fill=ACCENT)
draw.text((WIDTH // 2, y + (th + 16) // 2), tag_text, fill="#FFFFFF", font=f_tag, anchor="mm")

# --- Big number: 4.7% ---
y = 180
num_x = WIDTH // 2 - 30
draw.text((num_x, y), "4.7", fill=RED, font=f_big, anchor="mt")
bbox = draw.textbbox((num_x, y), "4.7", font=f_big, anchor="mt")
draw.text((bbox[2] + 5, bbox[3]), "%", fill=RED, font=f_pct, anchor="lb")

# --- Headline ---
y = 430
lines = [
    "That's how much of your",
    "rate increase goes to",
    "clean energy."
]
for i, line in enumerate(lines):
    draw.text((WIDTH // 2, y + i * 48), line, fill=DARK, font=f_headline, anchor="mm")

# --- Divider ---
y = 590
draw.line([(100, y), (WIDTH - 100, y)], fill=LIGHT_BORDER, width=2)

# --- Context ---
y = 620
context_lines = [
    "We analyzed 8 utility rate case filings",
    "totaling $4.0 BILLION in increases.",
    "",
    "The real cost drivers?"
]
for i, line in enumerate(context_lines):
    if line:
        draw.text((WIDTH // 2, y + i * 40), line, fill=MUTED, font=f_body, anchor="mm")

# --- Evidence card ---
y = 790
card_margin = 60
draw.rounded_rectangle(
    [(card_margin, y), (WIDTH - card_margin, y + 260)],
    radius=12, fill=CARD, outline=LIGHT_BORDER, width=2
)

items = [
    ("Infrastructure & Capital", "33.7%", NAVY),
    ("Shareholder Profit (ROE)", "10.1%", RED),
    ("Storm Recovery", "12.5%", ACCENT),
    ("Clean Energy Programs", "4.7%", GREEN),
]

iy = y + 25
for label, pct, color in items:
    draw.text((card_margin + 30, iy), label, fill=DARK, font=f_evidence, anchor="lm")
    draw.text((WIDTH - card_margin - 30, iy), pct, fill=color, font=f_evidence_bold, anchor="rm")
    iy += 55

# --- "Which one do politicians talk about?" ---
y = 1080
draw.text((WIDTH // 2, y), "Which one do politicians talk about?", fill=GOLD, font=f_body_bold, anchor="mm")

# --- Source line ---
y = 1180
draw.text((WIDTH // 2, y), "Source: PSC rate case filings, dps.ny.gov", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 28), "8 cases analyzed, 2023–2025 | $4.0B total requested", fill=MUTED, font=f_source, anchor="mm")

# --- Footer bar ---
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

# Save
out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post01_hook_4.7pct.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
