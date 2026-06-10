#!/usr/bin/env python3
"""Social card: Minnesota fraud "stayed buried" / 50-state claim — June 10, 2026."""

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
tag = "MISLEADING"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+24, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill=GOLD)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "Minnesota Fraud / Oversight Committee", fill=NAVY, font=f_topic, anchor="mm")
y += 38
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── HE SAID box ──
box_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+14), "HE SAID — Facebook post, June 9, 2026", fill=GREEN, font=f_label, anchor="lm")
draw.text((WIDTH//2, y+58), '"Without our House Oversight Committee investigation,', fill=DARK, font=f_quote_b, anchor="mm")
draw.text((WIDTH//2, y+88), 'this scandal would have stayed buried."', fill=DARK, font=f_quote_b, anchor="mm")
y += box_h + 10

draw.text((WIDTH//2, y), "▼  THE DOCUMENTED TIMELINE  ▼", fill=MUTED, font=f_arrow, anchor="mm")
y += 28

# ── TWO-TRACK comparison ──
col_w = 474
gap   = 12
lx    = 44
rx    = lx + col_w + gap
track_h = 286

# Track 1 — who exposed and prosecuted it
draw.rounded_rectangle([(lx, y), (lx+col_w, y+track_h)], radius=8,
                        fill="#EBF4FB", outline="#90CDF4", width=2)
draw.text((lx+col_w//2, y+14), "EXPOSED AND PROSECUTED BY", fill=BLUE, font=f_track, anchor="mm")
draw.text((lx+col_w//2, y+38), "FBI · DOJ · Minnesota auditors", fill=BLUE, font=f_sub_b, anchor="mm")
draw.line([(lx+24, y+60), (lx+col_w-24, y+60)], fill="#90CDF4", width=1)
draw.text((lx+col_w//2, y+84), "Jan 2022 — FBI raids: search warrants", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+102), "at 26 locations across Minnesota", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+128), "Sept 2022 — DOJ charges 47 in the", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+146), "$250M scheme, national press conference", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+172), "June 2024 — state legislative auditor", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+190), "report on oversight failures", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+216), "May 2026 — ringleader sentenced to", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+234), "500 months — over 41 years in prison", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+262), "77+ indicted · 50+ convicted", fill=BLUE, font=f_xs_b, anchor="mm")

# Track 2 — the committee's timeline
draw.rounded_rectangle([(rx, y), (rx+col_w, y+track_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((rx+col_w//2, y+14), "THE COMMITTEE'S TIMELINE", fill=ORANGE, font=f_track, anchor="mm")
draw.text((rx+col_w//2, y+38), "House Oversight Committee", fill=ORANGE, font=f_sub_b, anchor="mm")
draw.line([(rx+24, y+60), (rx+col_w-24, y+60)], fill="#F6AD55", width=1)
draw.text((rx+col_w//2, y+84), "Jan 7, 2026 — first Minnesota hearing,", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+102), "four years after the FBI raids", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+128), "Mar 4, 2026 — second hearing;", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+146), "Walz and Ellison testify", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+172), "June 8, 2026 — committee report on", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+190), "what state officials knew", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+216), "Real contribution: whistleblower", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+234), "findings behind the June 8 DOJ referral", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+262), "Examined it. Didn't expose it.", fill=ORANGE, font=f_xs_b, anchor="mm")

y += track_h + 12

# ── 50-state strip ──
strip_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+18), 'HE ALSO SAID: "THIS IS A 50 STATE, COAST TO COAST EFFORT"',
          fill=GOLD, font=f_track, anchor="mm")
draw.text((WIDTH//2, y+62), "3 STATES", fill=WHITE, font=f_stat, anchor="mm")
draw.text((WIDTH//2, y+96), "on the public record: Minnesota · New York · California", fill="#CBD5E0", font=f_xs, anchor="mm")
draw.text((WIDTH//2, y+116),
          "Minnesota hearings + report  ·  NY Medicaid letter (he co-signed)  ·  CA hospice letter",
          fill="#CBD5E0", font=f_xs_b, anchor="mm")
y += strip_h + 14

# ── Bottom-line callout ──
bl_h = 168
draw.rounded_rectangle([(44, y), (WIDTH-44, y+bl_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((WIDTH//2, y+22), "THE BOTTOM LINE", fill=ORANGE, font=f_label, anchor="mm")
draw.line([(180, y+44), (WIDTH-180, y+44)], fill="#F6AD55", width=1)
draw.text((WIDTH//2, y+72), "A scandal with FBI raids at 26 locations, a national DOJ", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+104), "press conference, 50+ convictions, and a sentence of", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+136), 'over 41 years was not "buried."', fill=DARK, font=f_quote, anchor="mm")
y += bl_h + 12

# ── On-the-record line ──
draw.text((WIDTH//2, y+10),
          "Sources: DOJ and FBI press releases, House Oversight Committee publications, House records.",
          fill=MUTED, font=f_sub_b, anchor="mm")
y += 36

# ── Footer ──
draw.rectangle([(0, HEIGHT-48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 24),
          "Full fact-check: langworthywatch.org/fact-checks/2026-06-10-minnesota-fraud-50-state-claim/",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/minnesota_50state_claim.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
