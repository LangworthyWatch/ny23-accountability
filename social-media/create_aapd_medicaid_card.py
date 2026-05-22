#!/usr/bin/env python3
"""Social card: AAPD / Medicaid + SSI bedroom rule CONTRADICTION — updated May 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
RED     = "#E53E3E"
GREEN   = "#276749"
ORANGE  = "#C05621"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
GOLD    = "#D69E2E"
WHITE   = "#FFFFFF"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_verdict = font("Arial Bold.ttf", 34)
f_label   = font("Arial Bold.ttf", 22)
f_quote   = font("Arial.ttf", 26)
f_quote_b = font("Arial Bold.ttf", 26)
f_stat    = font("Impact.ttf", 72)
f_sub     = font("Arial.ttf", 21)
f_sub_b   = font("Arial Bold.ttf", 21)
f_source  = font("Arial.ttf", 18)
f_footer  = font("Arial Bold.ttf", 21)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62

# ── Verdict badge ──
tag = "CONTRADICTION"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+24, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill=RED)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "Disability & Medicaid", fill=NAVY, font=f_verdict, anchor="mm")
y += 40
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# ── HIS PROMISE ──
box_h = 148
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+14), "HE SAID — May 18, 2026", fill=GREEN, font=f_label, anchor="lm")
draw.text((76, y+42), '"I\'ll keep working to protect critical', fill=DARK, font=f_quote)
draw.text((76, y+72), 'support systems and improve opportunities', fill=DARK, font=f_quote)
draw.text((76, y+102), 'for disabled Americans."', fill=DARK, font=f_quote)
y += box_h + 12

draw.text((WIDTH//2, y), "▼  WHAT WAS ALREADY HAPPENING  ▼", fill=MUTED,
          font=font("Arial Bold.ttf", 17), anchor="mm")
y += 28

# ── TWO-TRACK layout ──
col_w = 474
gap   = 12
lx    = 44
rx    = lx + col_w + gap
track_h = 218

# Track 1 — Medicaid vote
draw.rounded_rectangle([(lx, y), (lx+col_w, y+track_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((lx+col_w//2, y+14), "TRACK 1", fill=RED, font=font("Arial Bold.ttf", 16), anchor="mm")
draw.text((lx+col_w//2, y+36), "Medicaid vote", fill=RED, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+60), "Roll Call 190  ·  July 3, 2025", fill=DARK, font=font("Arial.ttf", 17), anchor="mm")
draw.text((lx+col_w//2, y+80), "YEA", fill=RED, font=font("Arial Bold.ttf", 22), anchor="mm")
draw.text((lx+col_w//2, y+122), "$840B", fill=RED, font=f_stat, anchor="mm")
draw.text((lx+col_w//2, y+170), "in Medicaid cuts", fill=MUTED, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+192), "10M lose coverage", fill=MUTED, font=font("Arial.ttf", 17), anchor="mm")

# Track 2 — SSI bedroom rule
draw.rounded_rectangle([(rx, y), (rx+col_w, y+track_h)], radius=8,
                        fill="#FFFAF0", outline="#FBD38D", width=2)
draw.text((rx+col_w//2, y+14), "TRACK 2", fill=ORANGE, font=font("Arial Bold.ttf", 16), anchor="mm")
draw.text((rx+col_w//2, y+36), "SSI bedroom rule", fill=ORANGE, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+60), "Proposed Apr 29, 2026", fill=DARK, font=font("Arial.ttf", 17), anchor="mm")
draw.text((rx+col_w//2, y+80), "18 days before meeting", fill=DARK, font=font("Arial Bold.ttf", 17), anchor="mm")
draw.text((rx+col_w//2, y+122), "−$330/mo", fill=ORANGE, font=f_stat, anchor="mm")
draw.text((rx+col_w//2, y+170), "for 400,000 disabled", fill=MUTED, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+192), "adults living at home", fill=MUTED, font=font("Arial.ttf", 17), anchor="mm")

y += track_h + 12

# ── Silence note ──
sil_h = 44
draw.rounded_rectangle([(44, y), (WIDTH-44, y+sil_h)], radius=6,
                        fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+sil_h//2),
          "Langworthy has made no public statement on the SSI bedroom rule.",
          fill=DARK, font=f_sub_b, anchor="mm")
y += sil_h + 14

# ── AAPD navy box ──
f_aapd_q = font("Arial Bold.ttf", 28)
f_aapd_l = font("Arial.ttf", 19)
aapd_h = 190
draw.rounded_rectangle([(44, y), (WIDTH-44, y+aapd_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+18), "AAPD President & CEO Maria Town — on the same law:",
          fill="#A0AEC0", font=f_aapd_l, anchor="mm")
draw.text((WIDTH//2, y+60), '"This Is A Devastating Day for Disabled Americans."',
          fill=WHITE, font=f_aapd_q, anchor="mm")
draw.text((WIDTH//2, y+100), "— AAPD press release, July 3, 2025", fill=GOLD, font=f_aapd_l, anchor="mm")
draw.text((WIDTH//2, y+130), "The same organization whose reps he posed with on May 18.",
          fill="#718096", font=f_aapd_l, anchor="mm")
y += aapd_h + 14

# ── Sources ──
draw.text((WIDTH//2, y),
          "Sources: CBO pub. 61510  ·  Roll Call 190  ·  ProPublica Apr 29, 2026  ·  AAPD",
          fill=MUTED, font=f_source, anchor="mm")
y += 22
draw.text((WIDTH//2, y),
          "langworthywatch.org/fact-checks/2026-05-18-aapd-medicaid-disability-contradiction",
          fill=MUTED, font=f_source, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/aapd_medicaid_contradiction.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
