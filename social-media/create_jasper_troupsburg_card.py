#!/usr/bin/env python3
"""Social card: Jasper-Troupsburg $60.5M FEMA award — MOSTLY TRUE — June 10, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
GREEN   = "#276749"
ORANGE  = "#C05621"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
GOLD    = "#D69E2E"
WHITE   = "#FFFFFF"
BLUE    = "#2B6CB0"


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except Exception:
        return ImageFont.load_default()


f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 22)
f_quote   = font("Arial.ttf", 26)
f_quote_b = font("Arial Bold.ttf", 26)
f_stat    = font("Impact.ttf", 56)
f_sub     = font("Arial.ttf", 19)
f_sub_b   = font("Arial Bold.ttf", 19)
f_track   = font("Arial Bold.ttf", 16)
f_xs      = font("Arial.ttf", 15)
f_xs_b    = font("Arial Bold.ttf", 15)
f_arrow   = font("Arial Bold.ttf", 17)
f_footer  = font("Arial Bold.ttf", 19)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 56

# ── Verdict badge ──
tag = "MOSTLY TRUE"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+24, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill=GREEN)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "FEMA / Jasper-Troupsburg Schools", fill=NAVY, font=f_topic, anchor="mm")
y += 38
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── HE SAID box ──
box_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+14), "HE SAID — Facebook post, June 9, 2026", fill=GREEN, font=f_label, anchor="lm")
draw.text((WIDTH//2, y+58), '"Proud to have helped secure $60.5 million in', fill=DARK, font=f_quote_b, anchor="mm")
draw.text((WIDTH//2, y+88), '@fema funds to rebuild Jasper-Troupsburg schools."', fill=DARK, font=f_quote_b, anchor="mm")
y += box_h + 10

draw.text((WIDTH//2, y), "▼  WHAT THE RECORD SHOWS  ▼", fill=MUTED, font=f_arrow, anchor="mm")
y += 28

# ── TWO-TRACK comparison ──
col_w = 474
gap   = 12
lx    = 44
rx    = lx + col_w + gap
track_h = 286

# Track 1 — what checks out
draw.rounded_rectangle([(lx, y), (lx+col_w, y+track_h)], radius=8,
                        fill="#EBF4FB", outline="#90CDF4", width=2)
draw.text((lx+col_w//2, y+14), "WHAT CHECKS OUT", fill=BLUE, font=f_track, anchor="mm")
draw.text((lx+col_w//2, y+38), "The award and the advocacy", fill=BLUE, font=f_sub_b, anchor="mm")
draw.line([(lx+24, y+60), (lx+col_w-24, y+60)], fill="#90CDF4", width=1)
draw.text((lx+col_w//2, y+84), "$60,493,661 through FEMA Public", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+102), "Assistance — 90% of a $67.2M rebuild", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+128), "Campus flooded twice: Tropical Storm", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+146), "Fred (2021), then Debby (2024) mid-repair", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+172), 'Superintendent, by name: "steadfast', fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+190), 'support and advocacy throughout"', fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+216), "He also cosponsored the bipartisan", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+234), "FEMA Act (Jan 2026)", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+262), '"Helped secure" is careful phrasing.', fill=BLUE, font=f_xs_b, anchor="mm")

# Track 2 — the fuller picture
draw.rounded_rectangle([(rx, y), (rx+col_w, y+track_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((rx+col_w//2, y+14), "THE FULLER PICTURE", fill=ORANGE, font=f_track, anchor="mm")
draw.text((rx+col_w//2, y+38), "What the post leaves out", fill=ORANGE, font=f_sub_b, anchor="mm")
draw.line([(rx+24, y+60), (rx+col_w-24, y+60)], fill="#F6AD55", width=1)
draw.text((rx+col_w//2, y+84), "Once FEMA approves the project, the", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+102), "money flows by statute — no member", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+120), "of Congress directs a PA award", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+146), "Schumer announced the SAME award:", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+164), '"SCHUMER SECURES $60 MILLION"', fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+190), "The superintendent credited BOTH", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+208), "offices; neither release names the other", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+234), "Two solo victory laps, one award", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+262), "Advocacy: real. Shared. Statutory.", fill=ORANGE, font=f_xs_b, anchor="mm")

y += track_h + 12

# ── Stat strip ──
strip_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+18), "THE PROGRAM BEHIND THIS AWARD IS NOW ON THE TABLE", fill=GOLD, font=f_track, anchor="mm")
draw.text((WIDTH//2, y+62), "90% COST SHARE", fill=WHITE, font=f_stat, anchor="mm")
draw.text((WIDTH//2, y+96), "is what the current FEMA Public Assistance Program paid here", fill="#CBD5E0", font=f_xs, anchor="mm")
draw.text((WIDTH//2, y+116),
          "The May 7 FEMA Review Council report proposes replacing it with fixed block grants to states",
          fill="#CBD5E0", font=f_xs_b, anchor="mm")
y += strip_h + 14

# ── Bottom-line callout ──
bl_h = 168
draw.rounded_rectangle([(44, y), (WIDTH-44, y+bl_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((WIDTH//2, y+22), "THE BOTTOM LINE", fill=ORANGE, font=f_label, anchor="mm")
draw.line([(180, y+44), (WIDTH-180, y+44)], fill="#F6AD55", width=1)
draw.text((WIDTH//2, y+72), "This claim mostly holds up. The open question:", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+104), "does he support the FEMA restructuring that would", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+136), "change how the next award like this works?", fill=DARK, font=f_quote, anchor="mm")
y += bl_h + 12

# ── On-the-record line ──
draw.text((WIDTH//2, y+10),
          "Sources: FEMA / district announcements, Schumer office releases, FEMA Review Council final report.",
          fill=MUTED, font=f_sub_b, anchor="mm")
y += 36

# ── Footer ──
draw.rectangle([(0, HEIGHT-48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 24),
          "Full fact-check: langworthywatch.org/fact-checks/2026-06-10-jasper-troupsburg-fema-award/",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/jasper_troupsburg_fema_award.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
