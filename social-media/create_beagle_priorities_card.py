#!/usr/bin/env python3
"""Social card: Beagle posts vs district issues — DOCUMENTED PATTERN — May 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
PURPLE  = "#553C9A"
RED     = "#E53E3E"
GREEN   = "#276749"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"
GOLD    = "#D69E2E"
LIGHT   = "#EDF2F7"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand  = font("Arial Bold.ttf", 22)
f_tag    = font("Arial Bold.ttf", 20)
f_topic  = font("Arial Bold.ttf", 30)
f_big    = font("Impact.ttf", 160)
f_big2   = font("Impact.ttf", 160)
f_label  = font("Arial Bold.ttf", 22)
f_sub    = font("Arial.ttf", 21)
f_sub_b  = font("Arial Bold.ttf", 21)
f_small  = font("Arial.ttf", 19)
f_footer = font("Arial Bold.ttf", 21)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH//2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62

# ── Verdict badge ──
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+24, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill=PURPLE)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 10

draw.text((WIDTH//2, y), "May 2026 — What He Posted About", fill=NAVY, font=f_topic, anchor="mm")
y += 42
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# ── Two column comparison ──
col_w = 470
gap   = 16
lx    = 32
rx    = lx + col_w + gap

# LEFT — beagles
col_h = 420
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=10,
                        fill="#EBF8F0", outline="#9AE6B4", width=3)
draw.text((lx+col_w//2, y+20), "Wisconsin Beagles", fill=GREEN,
          font=font("Arial Bold.ttf", 24), anchor="mm")
draw.line([(lx+20, y+46), (lx+col_w-20, y+46)], fill="#9AE6B4", width=1)
draw.text((lx+col_w//2, y+150), "17", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+292), "posts since May 1", fill=GREEN,
          font=font("Arial Bold.ttf", 28), anchor="mm")
draw.text((lx+col_w//2, y+330), "A Wisconsin facility.", fill=MUTED, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+356), "Not in his district.", fill=MUTED, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+382), "He didn't free them.", fill=MUTED, font=f_sub, anchor="mm")

# RIGHT — district issues
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=10,
                        fill="#FFF5F5", outline="#FEB2B2", width=3)
draw.text((rx+col_w//2, y+20), "His District", fill=RED,
          font=font("Arial Bold.ttf", 24), anchor="mm")
draw.line([(rx+20, y+46), (rx+col_w-20, y+46)], fill="#FEB2B2", width=1)
draw.text((rx+col_w//2, y+150), "0", fill=RED, font=f_big2, anchor="mm")
draw.text((rx+col_w//2, y+292), "posts about:", fill=RED,
          font=font("Arial Bold.ttf", 28), anchor="mm")
draw.text((rx+col_w//2, y+330), "8 hospitals at risk of closing", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+356), "Most of any NY district", fill=MUTED, font=font("Arial.ttf", 18), anchor="mm")
draw.text((rx+col_w//2, y+382), "$840B Medicaid cuts he voted for", fill=DARK, font=font("Arial.ttf", 18), anchor="mm")

y += col_h + 16

# ── The kicker ──
kick_h = 80
draw.rounded_rectangle([(32, y), (WIDTH-32, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+20), "He said hospital closure warnings were", fill="#A0AEC0",
          font=font("Arial.ttf", 20), anchor="mm")
draw.text((WIDTH//2, y+50), '"pure fiction."', fill=WHITE,
          font=font("Arial Bold.ttf", 30), anchor="mm")
y += kick_h + 14

# ── Sub stats row ──
draw.rounded_rectangle([(32, y), (WIDTH-32, y+88)], radius=8, fill=LIGHT)
third = (WIDTH - 64) // 3
for i, (num, label) in enumerate([
    ("8", "hospitals at risk\nin NY-23"),
    ("$840B", "Medicaid cut\nhe voted for"),
    ("400K", "disabled people\nthreatened by SSI rule"),
]):
    cx = 32 + third*i + third//2
    draw.text((cx, y+18), num, fill=RED, font=font("Impact.ttf", 38), anchor="mm")
    for j, line in enumerate(label.split("\n")):
        draw.text((cx, y+50+j*18), line, fill=MUTED, font=font("Arial.ttf", 15), anchor="mm")
y += 88 + 12

# ── Source ──
draw.text((WIDTH//2, y), "Sources: Fiscal Policy Institute  ·  CBO pub. 61510  ·  ProPublica Apr 29, 2026",
          fill=MUTED, font=font("Arial.ttf", 17), anchor="mm")
y += 22
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-22-beagle-posts-credit-claiming-distraction",
          fill=MUTED, font=font("Arial.ttf", 17), anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-24), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/beagle_priorities_pattern.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
