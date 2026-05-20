#!/usr/bin/env python3
"""Post 4: THE SQUEEZE — $3.36/month vs $21.53/month."""

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
f_big_green = font("Impact.ttf", 140)
f_big_red = font("Impact.ttf", 120)
f_unit = font("Impact.ttf", 50)
f_label = font("Arial Bold.ttf", 28)
f_body = font("Arial.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 28)
f_source = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Top brand bar
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

# --- Green section: clean energy surcharge ---
y = 100
draw.text((WIDTH // 2, y), "The clean energy surcharge", fill=MUTED, font=f_label, anchor="mm")
draw.text((WIDTH // 2, y + 40), "on your electric bill:", fill=MUTED, font=f_label, anchor="mm")

y = 210
num_x = WIDTH // 2 - 60
draw.text((num_x, y), "$3.36", fill=GREEN, font=f_big_green, anchor="mt")
bbox = draw.textbbox((num_x, y), "$3.36", font=f_big_green, anchor="mt")
draw.text((bbox[2] + 8, bbox[3]), "/mo", fill=GREEN, font=f_unit, anchor="lb")

y = 380
draw.text((WIDTH // 2, y), "System Benefits Charge — funds efficiency,", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 36), "low-income assistance, and renewables.", fill=DARK, font=f_body, anchor="mm")

# --- Divider with "vs" ---
y = 480
draw.line([(80, y), (WIDTH - 80, y)], fill=LIGHT_BORDER, width=3)
draw.rounded_rectangle([((WIDTH - 60) // 2, y - 20), ((WIDTH + 60) // 2, y + 20)],
                        radius=10, fill=BG, outline=LIGHT_BORDER, width=2)
draw.text((WIDTH // 2, y), "vs", fill=MUTED, font=f_label, anchor="mm")

# --- Red section: NYSEG increase ---
y = 520
draw.text((WIDTH // 2, y), "What NYSEG's 18.4% increase", fill=MUTED, font=f_label, anchor="mm")
draw.text((WIDTH // 2, y + 40), "would add to your bill:", fill=MUTED, font=f_label, anchor="mm")

y = 630
num_x = WIDTH // 2 - 70
draw.text((num_x, y), "$21.53", fill=RED, font=f_big_red, anchor="mt")
bbox = draw.textbbox((num_x, y), "$21.53", font=f_big_red, anchor="mt")
draw.text((bbox[2] + 8, bbox[3]), "/mo", fill=RED, font=f_unit, anchor="lb")

y = 780
draw.text((WIDTH // 2, y), "Infrastructure, operations, shareholder profit,", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 36), "storm recovery, property taxes.", fill=DARK, font=f_body, anchor="mm")

# --- Callout ---
y = 880
draw.rounded_rectangle(
    [(60, y), (WIDTH - 60, y + 140)],
    radius=12, fill="#FFFFF0", outline=GOLD, width=2
)
draw.text((WIDTH // 2, y + 40), "If you eliminated the clean energy surcharge:", fill=DARK, font=f_body, anchor="mm")
draw.text((WIDTH // 2, y + 80), "you'd save $3.36/month.", fill=GREEN, font=f_body_bold, anchor="mm")
draw.text((WIDTH // 2, y + 115), "NYSEG's pending increase would cost $21.53/month.", fill=RED, font=f_body, anchor="mm")

# Source
y = 1120
draw.text((WIDTH // 2, y), "Source: PSC rate case 25-E-0375 (NYSEG)", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 24), "langworthywatch.org", fill=MUTED, font=f_source, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post04_monthly.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
