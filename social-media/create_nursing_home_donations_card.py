#!/usr/bin/env python3
"""Social card: Nursing home donations / staffing vote — DOCUMENTED PATTERN — May 28, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
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

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 20)
f_big     = font("Impact.ttf", 78)
f_stat    = font("Impact.ttf", 60)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 20)
f_small   = font("Arial.ttf", 18)
f_seq_n   = font("Impact.ttf", 22)
f_seq     = font("Arial Bold.ttf", 16)
f_seq_s   = font("Arial.ttf", 15)
f_note_b  = font("Arial Bold.ttf", 17)
f_note    = font("Arial.ttf", 17)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62

# ── Verdict badge ──
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "Nursing Homes & Campaign Finance", fill=NAVY, font=f_topic, anchor="mm")
y += 44
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── MONEY BOX ──
money_h = 185
draw.rounded_rectangle([(44, y), (WIDTH-44, y+money_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+16), "THE MONEY — FEC BULK FILINGS", fill=GREEN, font=f_label, anchor="lm")
draw.text((240, y+money_h//2+12), "$60,000", fill=GREEN, font=f_big, anchor="mm")

rx = 490
draw.text((rx, y+38), "Benjamin + Judy Landa", fill=DARK, font=f_sub_b, anchor="lm")
draw.text((rx, y+64), "Lawrence, NY — nursing home operator", fill=MUTED, font=f_small, anchor="lm")
draw.text((rx, y+86), "106 facilities across 10 states", fill=MUTED, font=f_small, anchor="lm")
draw.line([(rx, y+104), (WIDTH-56, y+104)], fill="#9AE6B4", width=1)
draw.text((rx, y+118), "All contributed 2022–2025", fill=DARK, font=f_sub_b, anchor="lm")
draw.text((rx, y+142), "every dollar before the vote", fill=DARK, font=f_sub, anchor="lm")
draw.text((rx, y+163), "$25,000 in March 2025 — 3 months prior", fill=ORANGE, font=f_small, anchor="lm")

y += money_h + 16

# ── VOTE BOX ──
vote_h = 126
draw.rounded_rectangle([(44, y), (WIDTH-44, y+vote_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((76, y+16), "THE VOTE — Roll Call 190 · July 3, 2025", fill=RED, font=f_label, anchor="lm")
draw.text((178, y+vote_h//2+12), "YES", fill=RED, font=f_stat, anchor="mm")

vx = 288
draw.text((vx, y+36), "One Big Beautiful Bill Act · §71111", fill=DARK, font=f_sub_b, anchor="lm")
draw.text((vx, y+62), "Blocked CMS nursing home staffing rule until 2034", fill=DARK, font=f_sub, anchor="lm")
draw.text((vx, y+86), "CMS RIA: ~$43B cost to operators that won't be required", fill=MUTED, font=f_small, anchor="lm")
draw.text((vx, y+106), "UPenn est: ~13,000 preventable deaths/year", fill=MUTED, font=f_small, anchor="lm")

y += vote_h + 16

# ── SEQUENCE STRIP ──
seq_h = 88
draw.rounded_rectangle([(44, y), (WIDTH-44, y+seq_h)], radius=6,
                        fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+10), "THE SEQUENCE", fill=NAVY, font=font("Arial Bold.ttf", 15), anchor="mm")

s_w = (WIDTH - 88 - 32) // 3
s_gap = 16
s1x = 60
s2x = s1x + s_w + s_gap
s3x = s2x + s_w + s_gap

for sx, num, line1, line2, color in [
    (s1x, "1", "2022–2025", "Landa donates $60K", GREEN),
    (s2x, "2", "July 3, 2025", "Langworthy votes YES", RED),
    (s3x, "3", "Dec. 3, 2025", "CMS formally repeals rule", ORANGE),
]:
    mx = sx + s_w // 2
    draw.text((mx, y+28), line1, fill=color, font=f_seq, anchor="mm")
    draw.text((mx, y+48), line2, fill=DARK, font=f_seq, anchor="mm")
    draw.text((mx, y+66), "(rule void Feb 2, 2026)" if num == "3" else "", fill=MUTED, font=f_seq_s, anchor="mm")
    if num in ("1", "2"):
        ax = sx + s_w + s_gap // 2
        draw.text((ax, y+seq_h//2), "→", fill=MUTED, font=font("Arial Bold.ttf", 22), anchor="mm")

y += seq_h + 16

# ── FACILITIES — TWO COLUMNS ──
col_w = 474
gap   = 12
lx    = 44
rx_col = lx + col_w + gap
fac_h = 196

draw.rounded_rectangle([(lx, y), (lx+col_w, y+fac_h)], radius=8,
                        fill="#FFF5F0", outline="#FBD38D", width=2)
draw.text((lx+col_w//2, y+16), "STAFFING (106 FACILITIES)", fill=ORANGE, font=font("Arial Bold.ttf", 17), anchor="mm")
draw.text((lx+col_w//2, y+56), "55%", fill=ORANGE, font=f_stat, anchor="mm")
draw.text((lx+col_w//2, y+106), "fall below the RN floor", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+130), "the vote blocked", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+154), "61% have poor staffing rating (1–2 star)", fill=MUTED, font=f_small, anchor="mm")

draw.rounded_rectangle([(rx_col, y), (rx_col+col_w, y+fac_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx_col+col_w//2, y+16), "CMS ABUSE ICON", fill=RED, font=font("Arial Bold.ttf", 17), anchor="mm")
draw.text((rx_col+col_w//2, y+56), "106/106", fill=RED, font=f_stat, anchor="mm")
draw.text((rx_col+col_w//2, y+106), "every facility in the network", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx_col+col_w//2, y+130), "carries CMS's abuse icon", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx_col+col_w//2, y+154), "$3.85M in total civil monetary penalties", fill=MUTED, font=f_small, anchor="mm")

y += fac_h + 16

# ── CAVEAT BOX ──
cav_h = 100
draw.rounded_rectangle([(44, y), (WIDTH-44, y+cav_h)], radius=6,
                        fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+22), "We can't prove a connection between these donations and this vote.",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+48), "Contributions from nursing home operators to members who vote on nursing",
          fill=MUTED, font=f_note, anchor="mm")
draw.text((WIDTH//2, y+68), "home policy are legal and routine. The pattern is documented below.",
          fill=MUTED, font=f_note, anchor="mm")
y += cav_h + 18

# ── Sources ──
draw.text((WIDTH//2, y), "Sources: FEC bulk files  ·  CMS Care Compare Apr 2026  ·  clerk.house.gov Roll Call 190",
          fill=MUTED, font=f_small, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-28-nursing-home-staffing-donations/",
          fill=NAVY, font=f_small, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/nursing_home_donations_pattern.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
