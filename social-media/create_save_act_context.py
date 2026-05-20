#!/usr/bin/env python3
"""SAVE Act reshare #3 — 83% support... until they hear the details. 1080x1080."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG = "#F5F7FA"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
GREEN = "#38A169"
MUTED = "#718096"
BORDER = "#E2E8F0"
GOLD = "#D69E2E"
LIGHT_GOLD = "#FFFFF0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 24)
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 36)
f_subhead = font("Arial Bold.ttf", 28)
f_big = font("Impact.ttf", 100)
f_body = font("Arial Bold.ttf", 24)
f_body_bold = font("Arial Bold.ttf", 24)
f_small = font("Arial Bold.ttf", 22)
f_small_bold = font("Arial Bold.ttf", 22)
f_source = font("Arial.ttf", 19)
f_footer = font("Arial Bold.ttf", 22)
f_verdict = font("Arial Bold.ttf", 24)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header bar ──
draw.rectangle([(0, 0), (WIDTH, 50)], fill=NAVY)
draw.text((WIDTH // 2, 25), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

y = 72

# ── Tag ──
tag_text = "FACT CHECK"
tag_bbox = draw.textbbox((0, 0), tag_text, font=f_tag)
tag_w = tag_bbox[2] - tag_bbox[0] + 24
tag_h = tag_bbox[3] - tag_bbox[1] + 12
tag_x = (WIDTH - tag_w) // 2
draw.rounded_rectangle([(tag_x, y), (tag_x + tag_w, y + tag_h)],
                        radius=4, fill=GOLD)
draw.text((WIDTH // 2, y + tag_h // 2), tag_text, fill="#FFFFFF", font=f_tag, anchor="mm")

y += tag_h + 14

# ── Claim quote ──
draw.text((WIDTH // 2, y), '"83% of Americans support', fill=NAVY, font=f_headline, anchor="mm")
y += 36
draw.text((WIDTH // 2, y), 'proof of citizenship to vote"', fill=NAVY, font=f_headline, anchor="mm")

y += 65

# ── Verdict ──
draw.text((WIDTH // 2, y), "TRUE", fill=GREEN, font=f_big, anchor="mm")
y += 55

draw.text((WIDTH // 2, y), "The polling is accurate.", fill=DARK, font=f_body, anchor="mm")
y += 26
draw.text((WIDTH // 2, y), "Pew Research, Gallup, and others confirm it.", fill=MUTED, font=f_body, anchor="mm")

y += 32

# ── Divider ──
draw.line([(120, y), (WIDTH - 120, y)], fill=BORDER, width=2)
y += 20

# ── Missing context card ──
draw.rounded_rectangle([(60, y), (WIDTH - 60, y + 42)],
                        radius=6, fill=GOLD, outline=GOLD, width=1)
draw.text((WIDTH // 2, y + 21), "MISSING CONTEXT", fill="#FFFFFF", font=f_subhead, anchor="mm")

y += 55

draw.text((WIDTH // 2, y), "The polls don't ask how people feel", fill=DARK, font=f_body_bold, anchor="mm")
y += 28
draw.text((WIDTH // 2, y), "when they learn the implementation details:", fill=DARK, font=f_body_bold, anchor="mm")

y += 35

# ── Impact list — clean, factual ──
card_left = 80
items = [
    ("21+ million citizens", "lack readily accessible documents"),
    ("Elderly voters", "born before standardized birth records"),
    ("Rural residents", "may travel hours for a DMV office"),
    ("Low-income citizens", "$165 passport vs. current free system"),
    ("Married women", "name changes create document mismatches"),
    ("Disaster survivors", "documents destroyed in floods or fires"),
]

for label, detail in items:
    draw.text((card_left, y), label, fill=RED, font=f_small_bold)
    label_bbox = draw.textbbox((0, 0), label, font=f_small_bold)
    label_w = label_bbox[2] - label_bbox[0]
    draw.text((card_left + label_w + 10, y), " --  " + detail, fill=MUTED, font=f_small)
    y += 36

y += 25

# ── Bottom line ──
draw.line([(150, y), (WIDTH - 150, y)], fill=BORDER, width=2)
y += 28

draw.text((WIDTH // 2, y), "This transcends party.", fill=DARK, font=f_body_bold, anchor="mm")
y += 28
draw.text((WIDTH // 2, y), "Elderly, rural, and low-income voters", fill=DARK, font=f_body_bold, anchor="mm")
y += 26
draw.text((WIDTH // 2, y), "are in every district, in both parties.", fill=DARK, font=f_body_bold, anchor="mm")

y += 30

# ── Source ──
draw.text((WIDTH // 2, y), "Sources: Pew Research, Gallup, Brennan Center, U.S. Census", fill=MUTED, font=f_source, anchor="mm")
y += 24
draw.text((WIDTH // 2, y), "Full fact-check: langworthywatch.org/fact-checks/2026-02-10-save-act-voter-id", fill=MUTED, font=f_source, anchor="mm")

# ── Footer bar ──
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/save_act_context.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
