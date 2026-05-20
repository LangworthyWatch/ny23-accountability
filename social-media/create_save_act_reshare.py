#!/usr/bin/env python3
"""SAVE Act reshare graphic — bright Instagram-optimized, 1080x1350."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1350
FONT_DIR = "/System/Library/Fonts/Supplemental/"

# Bright social media palette (matches utility series)
BG = "#F5F7FA"
CARD = "#FFFFFF"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
GREEN = "#38A169"
GOLD = "#D69E2E"
MUTED = "#718096"
ACCENT = "#2B6CB0"
LIGHT_RED = "#FFF5F5"
LIGHT_GREEN = "#F0FFF4"
LIGHT_GOLD = "#FFFFF0"
BORDER = "#E2E8F0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 22)
f_tag = font("Arial Bold.ttf", 16)
f_big = font("Impact.ttf", 140)
f_big2 = font("Impact.ttf", 72)
f_headline = font("Arial Bold.ttf", 36)
f_subhead = font("Arial Bold.ttf", 26)
f_body = font("Arial.ttf", 24)
f_body_bold = font("Arial Bold.ttf", 24)
f_small = font("Arial.ttf", 20)
f_small_bold = font("Arial Bold.ttf", 20)
f_source = font("Arial.ttf", 17)
f_footer = font("Arial Bold.ttf", 20)
f_verdict = font("Arial Bold.ttf", 22)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header bar ──
draw.rectangle([(0, 0), (WIDTH, 50)], fill=NAVY)
draw.text((WIDTH // 2, 25), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

y = 75

# ── Category tag ──
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
draw.text((WIDTH // 2, y), "The SAVE Act", fill=NAVY, font=f_headline, anchor="mm")
y += 38
draw.text((WIDTH // 2, y), "Verdict: MISLEADING", fill=RED, font=f_verdict, anchor="mm")
y += 80

# ── Big number ──
draw.text((WIDTH // 2, y), "~100", fill=RED, font=f_big, anchor="mm")
y += 110
draw.text((WIDTH // 2, y), "documented cases of noncitizen voting", fill=DARK, font=f_body, anchor="mm")
y += 30
draw.text((WIDTH // 2, y), "over 20+ years, out of billions of ballots cast", fill=MUTED, font=f_body, anchor="mm")
y += 16
draw.text((WIDTH // 2, y + 20), "Source: Heritage Foundation Election Fraud Database", fill=MUTED, font=f_small, anchor="mm")

y += 55

# ── Divider ──
draw.line([(80, y), (WIDTH - 80, y)], fill=BORDER, width=1)
y += 20

# ── VS comparison ──
draw.text((WIDTH // 2, y), "vs.", fill=MUTED, font=f_subhead, anchor="mm")
y += 38

draw.text((WIDTH // 2, y + 10), "21 Million", fill=NAVY, font=f_big2, anchor="mm")
y += 70
draw.text((WIDTH // 2, y), "U.S. citizens who lack readily accessible", fill=DARK, font=f_body, anchor="mm")
y += 30
draw.text((WIDTH // 2, y), "proof-of-citizenship documents", fill=DARK, font=f_body, anchor="mm")
y += 16
draw.text((WIDTH // 2, y + 20), "Source: Brennan Center for Justice", fill=MUTED, font=f_small, anchor="mm")

y += 55

# ── Divider ──
draw.line([(80, y), (WIDTH - 80, y)], fill=BORDER, width=1)
y += 25

# ── Impact cards ──
# Card 1: Who gets blocked
card_left = 60
card_right = WIDTH - 60
card_w = card_right - card_left

card1_h = 195
draw.rounded_rectangle([(card_left, y), (card_right, y + card1_h)],
                        radius=10, fill=LIGHT_RED, outline="#FEB2B2", width=1)

draw.text((card_left + 20, y + 14), "WHO GETS BLOCKED", fill=RED, font=f_small_bold)

impacts = [
    ("Elderly voters:", "23.3% of Tioga County is 65+ — inconsistent vital records"),
    ("Rural voters:", "Limited DMV access across NY-23 counties"),
    ("Low-income voters:", "Passport costs $165; birth certificate replacements $10-$50"),
]

iy = y + 44
for label, detail in impacts:
    draw.text((card_left + 25, iy), label, fill=DARK, font=f_small_bold)
    draw.text((card_left + 25, iy + 24), detail, fill=MUTED, font=f_small)
    iy += 50

y += card1_h + 15

# Card 2: What it actually does
draw.rounded_rectangle([(card_left, y), (card_right, y + 105)],
                        radius=10, fill=LIGHT_GOLD, outline="#ECC94B", width=1)

draw.text((card_left + 20, y + 15), "WHAT THE SAVE ACT DOES NOT ADDRESS", fill=GOLD, font=f_small_bold)

missing = "Cybersecurity, ballot chain-of-custody, voting machine\nsecurity, election infrastructure funding"
draw.text((card_left + 25, y + 45), missing, fill=DARK, font=f_small)

y += 125

# ── Key stat callout ──
draw.text((WIDTH // 2, y + 10), "Noncitizen voting is already illegal.", fill=DARK, font=f_subhead, anchor="mm")
y += 40
draw.text((WIDTH // 2, y), "Up to 5 years in prison + deportation.", fill=DARK, font=f_body, anchor="mm")
y += 28
draw.text((WIDTH // 2, y), "Federal law since 1996.", fill=MUTED, font=f_body, anchor="mm")

y += 50

# ── Source line ──
draw.text((WIDTH // 2, y), "Sources: Heritage Foundation, Cato Institute, Brennan Center,", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 22), "Pew Research, Congress.gov, U.S. Census Bureau", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 44), "Full fact-check: langworthywatch.org/fact-checks/", fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y + 66), "2026-02-10-save-act-voter-id", fill=MUTED, font=f_source, anchor="mm")

# ── Footer bar ──
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/save_act_reshare.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
