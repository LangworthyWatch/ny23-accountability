#!/usr/bin/env python3
"""Social card: SECURE Data Act / Big Brother contradiction — June 6, 2026."""

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
    except Exception:
        return ImageFont.load_default()


f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 22)
f_quote   = font("Arial.ttf", 26)
f_quote_b = font("Arial Bold.ttf", 26)
f_stat    = font("Impact.ttf", 56)
f_stat_s  = font("Impact.ttf", 44)
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

y = 62

# ── Verdict badge ──
tag = "CONTRADICTION"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+24, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5, fill=RED)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "Privacy / Surveillance", fill=NAVY, font=f_topic, anchor="mm")
y += 38
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── HE SAID box ──
box_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+14), "HE SAID — Facebook post, April 30, 2026", fill=GREEN, font=f_label, anchor="lm")
draw.text((WIDTH//2, y+58), '"Big Brother has no place spying on you', fill=DARK, font=f_quote_b, anchor="mm")
draw.text((WIDTH//2, y+88), 'behind the wheel."', fill=DARK, font=f_quote_b, anchor="mm")
y += box_h + 10

draw.text((WIDTH//2, y), "▼  WHAT HE DID — IN THE SAME 9 DAYS  ▼", fill=MUTED, font=f_arrow, anchor="mm")
y += 28

# ── TWO-TRACK comparison ──
col_w = 474
gap   = 12
lx    = 44
rx    = lx + col_w + gap
track_h = 286

# Track 1 — H.R. 8413 cosponsor (April 21)
draw.rounded_rectangle([(lx, y), (lx+col_w, y+track_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((lx+col_w//2, y+14), "APRIL 21 — COSPONSORED", fill=RED, font=f_track, anchor="mm")
draw.text((lx+col_w//2, y+38), "H.R. 8413 SECURE Data Act", fill=RED, font=f_sub_b, anchor="mm")
draw.line([(lx+24, y+60), (lx+col_w-24, y+60)], fill="#FEB2B2", width=1)
draw.text((lx+col_w//2, y+82), "Federal corporate surveillance", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+114), "→ Preempts NY's pending", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+132), "    data-broker delete law (S9088A)", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+158), "→ NO right for you to sue", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+176), "    a company for data misuse", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+202), "→ Sec. of Commerce", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+220), "    approves industry \"codes of conduct\"", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+250), "57 industry trade groups", fill=RED, font=f_xs_b, anchor="mm")
draw.text((lx+col_w//2, y+268), "signed the support letter", fill=RED, font=f_xs_b, anchor="mm")

# Track 2 — FISA 702 vote (April 30)
draw.rounded_rectangle([(rx, y), (rx+col_w, y+track_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+14), "APRIL 30 — VOTED YEA", fill=RED, font=f_track, anchor="mm")
draw.text((rx+col_w//2, y+38), "FISA 702 extension", fill=RED, font=f_sub_b, anchor="mm")
draw.line([(rx+24, y+60), (rx+col_w-24, y+60)], fill="#FEB2B2", width=1)
draw.text((rx+col_w//2, y+82), "Federal government surveillance", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+114), "→ Roll Call 155", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+132), "    Passed 261-111, signed same day", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+158), "→ FBI can search Americans'", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+176), "    communications without a warrant", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+202), "→ Roughly 200,000 warrantless", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+220), "    searches/year of US data", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+250), "Same day as the post.", fill=RED, font=f_xs_b, anchor="mm")
draw.text((rx+col_w//2, y+268), "FISA renewed without warrant rule.", fill=RED, font=f_xs_b, anchor="mm")

y += track_h + 12

# ── Donor strip ──
donor_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+donor_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+18), "DONOR FOOTPRINT — PACS WHOSE ORGS SIGNED THE H.R. 8413 LETTER",
          fill=GOLD, font=f_track, anchor="mm")
# Big number
draw.text((WIDTH//2, y+62), "$270,500", fill=WHITE, font=f_stat, anchor="mm")
draw.text((WIDTH//2, y+96), "across 21 PACs — 2024 + 2026 cycles", fill="#CBD5E0", font=f_xs, anchor="mm")
draw.text((WIDTH//2, y+116),
          "Telecom $121K  ·  Retail/Franchise $77K  ·  Oil/Energy $61K  ·  Big Tech direct $3.5K",
          fill="#CBD5E0", font=f_xs_b, anchor="mm")
y += donor_h + 14

# ── Bottom-line callout ──
bl_h = 168
draw.rounded_rectangle([(44, y), (WIDTH-44, y+bl_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((WIDTH//2, y+22), "THE PATTERN", fill=ORANGE, font=f_label, anchor="mm")
draw.line([(180, y+44), (WIDTH-180, y+44)], fill="#F6AD55", width=1)
draw.text((WIDTH//2, y+72), 'He posts about being against "Big Brother."', fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+104), "He cosponsors federal corporate surveillance.", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+136), "He votes for federal government surveillance.", fill=DARK, font=f_quote, anchor="mm")
y += bl_h + 12

# ── On-the-record line ──
draw.text((WIDTH//2, y+10),
          "Fourth federal preemption initiative since February 2026.",
          fill=MUTED, font=f_sub_b, anchor="mm")
y += 36

# ── Footer ──
draw.rectangle([(0, HEIGHT-48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 24),
          "Full fact-check: langworthywatch.org/fact-checks/2026-06-06-langworthy-secure-data-act-hr8413/",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/secure_data_act_contradiction.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
