#!/usr/bin/env python3
"""SAVE Act reshare #2 — Who gets blocked from voting. 1080x1080 square."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG = "#F5F7FA"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
MUTED = "#718096"
BORDER = "#E2E8F0"
LIGHT_RED = "#FFF5F5"
GOLD = "#D69E2E"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 24)
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 38)
f_subhead = font("Arial Bold.ttf", 30)
f_big = font("Impact.ttf", 86)
f_body = font("Arial Bold.ttf", 26)
f_body_bold = font("Arial Bold.ttf", 26)
f_small = font("Arial Bold.ttf", 22)
f_small_bold = font("Arial Bold.ttf", 22)
f_source = font("Arial.ttf", 19)
f_footer = font("Arial Bold.ttf", 22)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header bar ──
draw.rectangle([(0, 0), (WIDTH, 50)], fill=NAVY)
draw.text((WIDTH // 2, 25), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

y = 75

# ── Tag ──
tag_text = "FACT CHECK"
tag_bbox = draw.textbbox((0, 0), tag_text, font=f_tag)
tag_w = tag_bbox[2] - tag_bbox[0] + 24
tag_h = tag_bbox[3] - tag_bbox[1] + 12
tag_x = (WIDTH - tag_w) // 2
draw.rounded_rectangle([(tag_x, y), (tag_x + tag_w, y + tag_h)],
                        radius=4, fill=RED)
draw.text((WIDTH // 2, y + tag_h // 2), tag_text, fill="#FFFFFF", font=f_tag, anchor="mm")

y += tag_h + 18

# ── Title ──
draw.text((WIDTH // 2, y), "Who the SAVE Act", fill=NAVY, font=f_headline, anchor="mm")
y += 38
draw.text((WIDTH // 2, y), "Actually Blocks", fill=RED, font=f_headline, anchor="mm")

y += 55

# ── Three rows: icon-style stat blocks ──
card_left = 60
card_right = WIDTH - 60
card_w = card_right - card_left

groups = [
    {
        'number': '23.3%',
        'color': RED,
        'label': 'of Tioga County residents are 65+',
        'detail': 'Many born before standardized birth records.',
        'detail2': 'Inconsistent vital records across rural counties.',
    },
    {
        'number': '$165',
        'color': NAVY,
        'label': 'cost of a passport',
        'detail': 'Birth certificate replacement: $10-$50.',
        'detail2': 'Current system: free attestation under penalty of perjury.',
    },
    {
        'number': '0',
        'color': RED,
        'label': 'DMV offices open on weekends in NY-23',
        'detail': 'Allegany, Schuyler, and Tioga counties:',
        'detail2': 'one DMV office each, weekday hours only.',
    },
]

for group in groups:
    # Card background
    draw.rounded_rectangle([(card_left, y), (card_right, y + 130)],
                            radius=10, fill="#FFFFFF", outline=BORDER, width=1)

    # Big number on the left
    draw.text((card_left + 30, y + 35), group['number'],
              fill=group['color'], font=f_big, anchor="lm")

    # Get width of number to position text after it
    num_bbox = draw.textbbox((0, 0), group['number'], font=f_big)
    num_w = num_bbox[2] - num_bbox[0]
    text_x = card_left + 40 + num_w

    # Label and detail to the right
    draw.text((text_x, y + 18), group['label'],
              fill=DARK, font=f_body_bold, anchor="lm")
    draw.text((text_x, y + 50), group['detail'],
              fill=MUTED, font=f_small, anchor="lm")
    draw.text((text_x, y + 74), group['detail2'],
              fill=MUTED, font=f_small, anchor="lm")

    y += 145

# ── Bottom callout ──
y += 5
draw.line([(120, y), (WIDTH - 120, y)], fill=BORDER, width=2)
y += 25

draw.text((WIDTH // 2, y), "The SAVE Act shifts the burden from", fill=DARK, font=f_body, anchor="mm")
y += 30
draw.text((WIDTH // 2, y), "enforcement to individual voters.", fill=DARK, font=f_body, anchor="mm")
y += 38
draw.text((WIDTH // 2, y), "It costs voters $10-$165. The current", fill=MUTED, font=f_small, anchor="mm")
y += 24
draw.text((WIDTH // 2, y), "system costs $0 and carries criminal penalties.", fill=MUTED, font=f_small, anchor="mm")

y += 40

# ── Source ──
draw.text((WIDTH // 2, y), "Sources: Brennan Center, U.S. Census, Tioga County data", fill=MUTED, font=f_source, anchor="mm")
y += 22
draw.text((WIDTH // 2, y), "Full fact-check: langworthywatch.org/fact-checks/2026-02-10-save-act-voter-id", fill=MUTED, font=f_source, anchor="mm")

# ── Footer bar ──
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/save_act_impact.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
