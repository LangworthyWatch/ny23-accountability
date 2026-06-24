#!/usr/bin/env python3
"""Social card: Scaffold Law cost pitch vs. the worker-safety law it omits. MISSING CONTEXT, June 24, 2026."""

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
LIGHTGRAY = "#A0AEC0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except Exception:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 20)
f_label_s = font("Arial Bold.ttf", 16)
f_big     = font("Impact.ttf", 88)
f_stat    = font("Impact.ttf", 46)
f_sub_b   = font("Arial Bold.ttf", 21)
f_sub     = font("Arial.ttf", 19)
f_small   = font("Arial.ttf", 18)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_src     = font("Arial.ttf", 16)
f_footer  = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 64

# ── Verdict badge ──
tag = "MISSING CONTEXT"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 12

# ── Topic ──
draw.text((WIDTH//2, y), "Scaffold Law: Cost Pitch vs. Safety Law", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 18

# ── WHAT HE SAID (quote box) ──
claim_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+16), "WHAT HE SAID  ·  Facebook, June 16, 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+50), '"It causes costs to skyrocket. Families pay the price', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+76), 'through higher housing costs, pricier infrastructure,', fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+102), "and wasted tax dollars. I'm fighting to end it.\"", fill=DARK, font=f_sub, anchor="lm")
draw.text((76, y+130), "Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")
y += claim_h + 16

# ── TWO COLUMNS: how he frames it vs. what he leaves out ──
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 262
lx = 44
rx = lx + col_w + 16

# LEFT: the cost framing
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+22), "HOW HE FRAMES IT", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+92), "$785M", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+160), "added to public construction a year", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+188), "industry estimate (BTEA)", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+226), "plus 'higher housing costs' and taxes", fill=MUTED, font=f_small, anchor="mm")

# RIGHT: what the post leaves out
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+22), "WHAT HE LEAVES OUT", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+92), "74", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+160), "NY construction workers died, 2023", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+188), "highest in a decade  ·  NYCOSH", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+226), "falls are the leading cause of these deaths", fill=MUTED, font=f_small, anchor="mm")

y += col_h + 16

# ── THE CONTEXT THE POST SKIPS (3-stat strip) ──
strip_h = 150
draw.rounded_rectangle([(44, y), (WIDTH-44, y+strip_h)], radius=8,
                        fill="#EDF2F7", outline=BORDER, width=2)
draw.text((WIDTH//2, y+20), "THE CONTEXT THE POST SKIPS", fill=NAVY, font=f_label, anchor="mm")
third = (WIDTH - 88) // 3
for i, (val, l1, l2, c) in enumerate([
    ("1885",      "a worker fall-protection law", "NY Labor Law 240, not a cost line", NAVY),
    ("5 GOP",     "cosponsors (Tenney, Stefanik)", "still stuck in House Judiciary",   NAVY),
    ("Sept 2026", "the federal highway-bill window", "industry wants the repeal attached", ORANGE),
]):
    cx = 44 + i * third + third // 2
    draw.text((cx, y+72), val, fill=c, font=f_stat, anchor="mm")
    draw.text((cx, y+108), l1, fill=DARK, font=f_xs_b, anchor="mm")
    draw.text((cx, y+128), l2, fill=MUTED, font=f_xs, anchor="mm")
y += strip_h + 16

# ── Kicker ──
kick_h = 96
draw.rounded_rectangle([(44, y), (WIDTH-44, y+kick_h)], radius=8, fill=NAVY)
draw.text((WIDTH//2, y+30), "He calls a 140-year-old worker-safety law 'outdated.'",
          fill=LIGHTGRAY, font=font("Arial.ttf", 18), anchor="mm")
draw.text((WIDTH//2, y+62), "The repeal is pitched on cost, with the safety tradeoff left unsaid.",
          fill=WHITE, font=font("Arial Bold.ttf", 21), anchor="mm")
y += kick_h + 14

# ── Sources + URL ──
draw.text((WIDTH//2, y), "Sources: NYCOSH  ·  BTEA / Washington Examiner  ·  congress.gov (H.R. 3548)  ·  NY State of Politics",
          fill=MUTED, font=f_src, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-24-scaffold-law-surface-transportation-reauthorization/",
          fill=NAVY, font=f_src, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/scaffold_cost_vs_safety.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
