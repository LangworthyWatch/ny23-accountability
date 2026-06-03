#!/usr/bin/env python3
"""Social card: RHTP $212M — MISSING CONTEXT — June 2, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
GREEN   = "#276749"
RED     = "#E53E3E"
ORANGE  = "#C05621"
GOLD    = "#D69E2E"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"
PURPLE  = "#553C9A"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 18)
f_label_s = font("Arial Bold.ttf", 14)
f_huge    = font("Impact.ttf", 96)
f_big     = font("Impact.ttf", 72)
f_stat    = font("Impact.ttf", 48)
f_sub_b   = font("Arial Bold.ttf", 20)
f_sub     = font("Arial.ttf", 18)
f_small   = font("Arial.ttf", 16)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_note_b  = font("Arial Bold.ttf", 17)
f_note    = font("Arial.ttf", 17)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH//2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62
tag = "MISSING CONTEXT"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 10

draw.text((WIDTH//2, y), "Rural Health Transformation Program", fill=NAVY, font=f_topic, anchor="mm")
y += 42
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# CLAIM BOX
claim_h = 100
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+14), "THE CLAIM — Press release, Dec 30, 2025", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+46), '"New York will receive $212 million in funding to strengthen our rural', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+70), 'hospitals and healthcare systems…"', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+90), "— Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")

y += claim_h + 14

# TWO-PANEL — the award vs the cut
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 224
lx = 44
rx = lx + col_w + 16

# LEFT — the award
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+18), "THE AWARD — NY YEAR 1", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+80), "$212M", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+140), "Rural Health Transformation Program", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+164), "5-year fund · ends FY2030", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+190), "12th-largest state award", fill=MUTED, font=f_small, anchor="mm")

# RIGHT — the cut
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+18), "THE CUT — SAME BILL", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+80), "$137B", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+140), "Rural Medicaid cut, 10 years", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+164), "Same OBBBA bill, Roll Call 190", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+190), "Langworthy voted YES", fill=MUTED, font=f_small, anchor="mm")

y += col_h + 14

# OFFSET MATH STRIP
strip_h = 130
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+18), "THE OFFSET MATH (per KFF)", fill=NAVY, font=f_label, anchor="mm")

third = (WIDTH - 88) // 3
for i, (val, label1, label2) in enumerate([
    ("37%", "of rural Medicaid cuts", "the $50B RHTP offsets"),
    ("64%", "of those Medicaid cuts hit", "AFTER FY2030, when RHTP ends"),
    ("8", "at-risk hospitals in NY-23", "most of any NY district (FPI)"),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+62), val, fill=RED, font=f_stat, anchor="mm")
    draw.text((cx, y+96), label1, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+114), label2, fill=MUTED, font=f_xs, anchor="mm")

y += strip_h + 14

# WHAT'S MISSING
miss_h = 74
draw.rounded_rectangle([(44, y), (WIDTH-44, y+miss_h)], radius=6,
                        fill="#FFFAF0", outline="#F6AD55", width=1)
draw.text((WIDTH//2, y+20), "The press release omits the offset math AND",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+46), "names no NY-23 facility recipient (none announced as of Jun 2, 2026).",
          fill=MUTED, font=f_note, anchor="mm")
y += miss_h + 12

# Sources + URL
draw.text((WIDTH//2, y), "Sources: CMS  ·  NY DOH  ·  KFF  ·  Fiscal Policy Institute  ·  Roll Call 190",
          fill=MUTED, font=f_small, anchor="mm")
y += 22
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-02-rural-health-transformation-212m/",
          fill=NAVY, font=f_small, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/rhtp_212m_offset.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
