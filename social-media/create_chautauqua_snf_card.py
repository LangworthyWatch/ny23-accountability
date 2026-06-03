#!/usr/bin/env python3
"""Social card: Chautauqua SNF cluster — DOCUMENTED PATTERN — June 2, 2026."""

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
f_topic   = font("Arial Bold.ttf", 30)
f_label   = font("Arial Bold.ttf", 18)
f_label_s = font("Arial Bold.ttf", 14)
f_big     = font("Impact.ttf", 80)
f_stat    = font("Impact.ttf", 48)
f_sub_b   = font("Arial Bold.ttf", 19)
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
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 10

draw.text((WIDTH//2, y), "Chautauqua County Nursing Homes", fill=NAVY, font=f_topic, anchor="mm")
y += 42
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# THREE CLOSURES STRIP
strip_h = 158
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#FFF5F0", outline="#FBD38D", width=2)
draw.text((WIDTH//2, y+18), "THREE CHAUTAUQUA SNF CLOSURES SINCE NOV 2023", fill=ORANGE, font=f_label, anchor="mm")

ew = (WIDTH - 88) // 3
for i, (date, name, magn) in enumerate([
    ("Jan 2024", "Lutheran Social Svcs", "49 residents · 106 staff"),
    ("Oct 2025", "Absolut Care Westfield", "66 residents · 113 jobs"),
    ("Jan 2026", "Heritage Village Gerry", "<40 residents (announced)"),
]):
    ex = 44 + i * ew + ew // 2
    draw.text((ex, y+54), date, fill=ORANGE, font=f_sub_b, anchor="mm")
    draw.text((ex, y+82), name, fill=DARK, font=f_sub_b, anchor="mm")
    draw.text((ex, y+108), magn, fill=MUTED, font=f_small, anchor="mm")
    if i < 2:
        ax = 44 + (i + 1) * ew
        draw.text((ax, y+strip_h//2+12), "→", fill=MUTED, font=font("Arial Bold.ttf", 22), anchor="mm")

y += strip_h + 16

# THE KILLER STAT — Heritage Village BELOW the floor
killer_h = 158
draw.rounded_rectangle([(44, y), (WIDTH-44, y+killer_h)], radius=8,
                        fill="#FFF5F5", outline="#FC8181", width=2)
draw.text((76, y+16), "HERITAGE VILLAGE WAS BELOW THE FEDERAL FLOOR", fill=RED, font=f_label, anchor="lm")
draw.text((220, y+killer_h//2+12), "0.5", fill=RED, font=f_big, anchor="mm")
draw.text((220, y+killer_h-26), "RN hrs/resident/day", fill=DARK, font=f_sub_b, anchor="mm")

vx = 395
draw.text((vx, y+58), "Federal §71111-blocked floor: 0.55", fill=DARK, font=f_sub_b, anchor="lm")
draw.text((vx, y+82), "Total nurse hours: ~2.7–3.25 (floor: 3.48)", fill=DARK, font=f_sub, anchor="lm")
draw.text((vx, y+106), "Staffing sub-rating: 1 of 5 stars", fill=DARK, font=f_sub, anchor="lm")
draw.text((vx, y+128), "Nurse turnover 58.9% vs NY avg 40.3%", fill=MUTED, font=f_small, anchor="lm")

y += killer_h + 16

# THE VOTE + THE SILENCE
quad_h = 122
draw.rounded_rectangle([(44, y), (WIDTH-44, y+quad_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)

half = (WIDTH - 88) // 2

# LEFT — the vote
draw.text((44+half//2, y+18), "THE VOTE — Roll Call 190", fill=NAVY, font=f_label_s, anchor="mm")
draw.text((44+half//2, y+62), "YES", fill=RED, font=f_big, anchor="mm")
draw.text((44+half//2, y+108), "OBBBA §71111 — staffing rule moratorium until 2034", fill=DARK, font=f_xs, anchor="mm")

# Divider
draw.line([(44+half, y+18), (44+half, y+quad_h-18)], fill=BORDER, width=1)

# RIGHT — the silence
draw.text((44+half + half//2, y+18), "PUBLIC STATEMENTS ON THE CLOSURES", fill=NAVY, font=f_label_s, anchor="mm")
draw.text((44+half + half//2, y+62), "0", fill=RED, font=f_big, anchor="mm")
draw.text((44+half + half//2, y+108), "vs. 22+ posts about Wisconsin beagles in same window", fill=DARK, font=f_xs, anchor="mm")

y += quad_h + 14

# Caveat
cav_h = 60
draw.rounded_rectangle([(44, y), (WIDTH-44, y+cav_h)], radius=6,
                        fill="#FFFAF0", outline="#F6AD55", width=1)
draw.text((WIDTH//2, y+20), "Closures' proximate causes vary (lease, financial, census).",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+42), "What's documented is the federal floor one was failing and the §71111 vote.",
          fill=MUTED, font=f_note, anchor="mm")
y += cav_h + 12

# Sources
draw.text((WIDTH//2, y), "Sources: ProPublica  ·  CMS Care Compare  ·  NY DOH  ·  Post-Journal  ·  Roll Call 190",
          fill=MUTED, font=f_small, anchor="mm")
y += 22
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-02-chautauqua-snf-cluster/",
          fill=NAVY, font=f_small, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/chautauqua_snf_cluster.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
