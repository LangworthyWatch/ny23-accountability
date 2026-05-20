#!/usr/bin/env python3
"""SAVE Act reshare — clean version. One contrast, one fact, one link."""

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

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand = font("Arial Bold.ttf", 24)
f_tag = font("Arial Bold.ttf", 18)
f_big = font("Impact.ttf", 170)
f_big2 = font("Impact.ttf", 110)
f_headline = font("Arial Bold.ttf", 40)
f_subhead = font("Arial Bold.ttf", 32)
f_body = font("Arial Bold.ttf", 28)
f_body_bold = font("Arial Bold.ttf", 28)
f_small = font("Arial Bold.ttf", 24)
f_source = font("Arial.ttf", 20)
f_footer = font("Arial Bold.ttf", 22)
f_verdict = font("Arial Bold.ttf", 28)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header bar ──
draw.rectangle([(0, 0), (WIDTH, 50)], fill=NAVY)
draw.text((WIDTH // 2, 25), "LANGWORTHYWATCH.ORG", fill="#FFFFFF", font=f_brand, anchor="mm")

y = 80

# ── Tag + Title ──
tag_text = "FACT CHECK"
tag_bbox = draw.textbbox((0, 0), tag_text, font=f_tag)
tag_w = tag_bbox[2] - tag_bbox[0] + 24
tag_h = tag_bbox[3] - tag_bbox[1] + 12
tag_x = (WIDTH - tag_w) // 2
draw.rounded_rectangle([(tag_x, y), (tag_x + tag_w, y + tag_h)],
                        radius=4, fill=RED)
draw.text((WIDTH // 2, y + tag_h // 2), tag_text, fill="#FFFFFF", font=f_tag, anchor="mm")

y += tag_h + 20
draw.text((WIDTH // 2, y), "The SAVE Act", fill=NAVY, font=f_headline, anchor="mm")
y += 38
draw.text((WIDTH // 2, y), "Verdict: MISLEADING", fill=RED, font=f_verdict, anchor="mm")

y += 95

# ── TOP NUMBER ──
draw.text((WIDTH // 2, y), "~100", fill=RED, font=f_big, anchor="mm")
y += 105
draw.text((WIDTH // 2, y), "documented cases of noncitizen voting", fill=DARK, font=f_body, anchor="mm")
y += 32
draw.text((WIDTH // 2, y), "over 20+ years", fill=MUTED, font=f_body, anchor="mm")
y += 28
draw.text((WIDTH // 2, y), "out of billions of ballots cast", fill=MUTED, font=f_body, anchor="mm")

y += 40

# ── VS ──
draw.line([(150, y), (WIDTH - 150, y)], fill=BORDER, width=2)
y += 22
draw.text((WIDTH // 2, y), "vs.", fill=MUTED, font=f_subhead, anchor="mm")
y += 30
draw.line([(150, y), (WIDTH - 150, y)], fill=BORDER, width=2)

y += 40

# ── BOTTOM NUMBER ──
draw.text((WIDTH // 2, y), "21 Million", fill=NAVY, font=f_big2, anchor="mm")
y += 65
draw.text((WIDTH // 2, y), "U.S. citizens who lack the documents", fill=DARK, font=f_body, anchor="mm")
y += 30
draw.text((WIDTH // 2, y), "this bill would require to vote", fill=DARK, font=f_body, anchor="mm")

y += 45

# ── Divider ──
draw.line([(150, y), (WIDTH - 150, y)], fill=BORDER, width=2)
y += 35

# ── Key fact ──
draw.text((WIDTH // 2, y), "Noncitizen voting is already illegal.", fill=DARK, font=f_subhead, anchor="mm")
y += 38
draw.text((WIDTH // 2, y), "Up to 5 years in prison + deportation.", fill=MUTED, font=f_small, anchor="mm")
y += 26
draw.text((WIDTH // 2, y), "Federal law since 1996.", fill=MUTED, font=f_small, anchor="mm")

y += 40

# ── Sources ──
draw.text((WIDTH // 2, y), "Sources: Heritage Foundation, Brennan Center, Cato Institute", fill=MUTED, font=f_source, anchor="mm")
y += 22
draw.text((WIDTH // 2, y), "Full fact-check: langworthywatch.org/fact-checks/2026-02-10-save-act-voter-id", fill=MUTED, font=f_source, anchor="mm")

# ── Footer bar ──
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org", fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/save_act_reshare.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
