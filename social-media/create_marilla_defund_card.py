#!/usr/bin/env python3
"""Social card: Marilla apprehensions / "voted to defund" claim — June 10, 2026."""

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
draw.text((WIDTH//2, y), "Border Patrol Funding / Marilla", fill=NAVY, font=f_topic, anchor="mm")
y += 38
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── HE SAID box ──
box_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y+14), "HE SAID — Facebook post, June 10, 2026 (sharing the Marilla story)", fill=GREEN, font=f_label, anchor="lm")
draw.text((WIDTH//2, y+58), '"While Democrats yet again voted to defund them,', fill=DARK, font=f_quote_b, anchor="mm")
draw.text((WIDTH//2, y+88), 'we are ensuring our law enforcement has the resources..."', fill=DARK, font=f_quote_b, anchor="mm")
y += box_h + 10

draw.text((WIDTH//2, y), "▼  THE TIMELINE THE POST SKIPS  ▼", fill=MUTED, font=f_arrow, anchor="mm")
y += 28

# ── TWO-TRACK comparison ──
col_w = 474
gap   = 12
lx    = 44
rx    = lx + col_w + gap
track_h = 286

# Track 1 — what was funded, and when
draw.rounded_rectangle([(lx, y), (lx+col_w, y+track_h)], radius=8,
                        fill="#EBF4FB", outline="#90CDF4", width=2)
draw.text((lx+col_w//2, y+14), "WHAT WAS FUNDED, AND WHEN", fill=BLUE, font=f_track, anchor="mm")
draw.text((lx+col_w//2, y+38), "The operation came first", fill=BLUE, font=f_sub_b, anchor="mm")
draw.line([(lx+24, y+60), (lx+col_w-24, y+60)], fill="#90CDF4", width=1)
draw.text((lx+col_w//2, y+84), "Apr 30 — DHS funding becomes law", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+102), "(P.L. 119-86; Senate passed it by voice vote)", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+128), "June 8 — Border Patrol agents and a CBP", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+146), "helicopter apprehend 15 people in Marilla", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+172), "The agents, the helicopter, the operation:", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+190), "all paid for by already-enacted funding", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+216), "Erie County Sheriff: responded to a 911", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+234), "call; not a joint operation, no custody", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+262), "Funded. Operating. On the record.", fill=BLUE, font=f_xs_b, anchor="mm")

# Track 2 — the vote he means
draw.rounded_rectangle([(rx, y), (rx+col_w, y+track_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((rx+col_w//2, y+14), "THE VOTE HE MEANS", fill=ORANGE, font=f_track, anchor="mm")
draw.text((rx+col_w//2, y+38), "Came the NEXT day", fill=ORANGE, font=f_sub_b, anchor="mm")
draw.line([(rx+24, y+60), (rx+col_w-24, y+60)], fill="#F6AD55", width=1)
draw.text((rx+col_w//2, y+84), "June 9 — S. 2, the Secure America Act:", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+102), "$70 BILLION in NEW supplemental funding", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+128), "Roll Call 214: 214-212", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+146), "(R 214-0, D 0-211)", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+172), "Democrats' condition: warrants, body", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+190), "cameras, mask limits — after Minneapolis", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+216), "June 10 — signed into law;", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+234), "the post goes up hours later", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+262), "A no on an increase, not a defunding.", fill=ORANGE, font=f_xs_b, anchor="mm")

y += track_h + 12

# ── Stat strip ──
strip_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+18), "THE OPERATION HE CITES AS PROOF OF \"DEFUNDING\" HAPPENED", fill=GOLD, font=f_track, anchor="mm")
draw.text((WIDTH//2, y+62), "1 DAY BEFORE THE VOTE", fill=WHITE, font=f_stat, anchor="mm")
draw.text((WIDTH//2, y+96), "June 8 operation  ·  June 9 vote  ·  June 10 signing and post", fill="#CBD5E0", font=f_xs, anchor="mm")
draw.text((WIDTH//2, y+116),
          "Under DHS appropriations enacted April 30 — which the Senate passed by voice vote",
          fill="#CBD5E0", font=f_xs_b, anchor="mm")
y += strip_h + 14

# ── Bottom-line callout ──
bl_h = 168
draw.rounded_rectangle([(44, y), (WIDTH-44, y+bl_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((WIDTH//2, y+22), "THE BOTTOM LINE", fill=ORANGE, font=f_label, anchor="mm")
draw.line([(180, y+44), (WIDTH-180, y+44)], fill="#F6AD55", width=1)
draw.text((WIDTH//2, y+72), "Voting against a $70 billion increase is not", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+104), "removing existing funding. The Marilla operation", fill=DARK, font=f_quote, anchor="mm")
draw.text((WIDTH//2, y+136), "is proof the funding was there.", fill=DARK, font=f_quote, anchor="mm")
y += bl_h + 12

# ── On-the-record line ──
draw.text((WIDTH//2, y+10),
          "Sources: House Clerk roll calls, Congress.gov, P.L. 119-86, WKBW, CBS News, PBS NewsHour.",
          fill=MUTED, font=f_sub_b, anchor="mm")
y += 36

# ── Footer ──
draw.rectangle([(0, HEIGHT-48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 24),
          "Full fact-check: langworthywatch.org/fact-checks/2026-06-10-marilla-defund-claim/",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/marilla_defund_claim.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
