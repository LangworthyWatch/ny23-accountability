#!/usr/bin/env python3
"""Social card: HALT Act / Collins Correctional — MISLEADING — May 20, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG     = "#F5F7FA"
NAVY   = "#1E3A5F"
DARK   = "#1A202C"
ORANGE = "#C05621"   # MISLEADING colour
ORANGE_BG = "#FFFAF0"
ORANGE_BD = "#FBD38D"
MUTED  = "#718096"
BORDER = "#E2E8F0"
WHITE  = "#FFFFFF"
GOLD   = "#D69E2E"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 24)
f_tag     = font("Arial Bold.ttf", 22)
f_topic   = font("Arial Bold.ttf", 36)
f_label   = font("Arial Bold.ttf", 24)
f_claim   = font("Arial.ttf", 28)
f_claim_b = font("Arial Bold.ttf", 28)
f_big     = font("Impact.ttf", 110)
f_big_sub = font("Arial Bold.ttf", 28)
f_sub     = font("Arial.ttf", 24)
f_small   = font("Arial.ttf", 20)
f_footer  = font("Arial Bold.ttf", 22)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 52)], fill=NAVY)
draw.text((WIDTH // 2, 26), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 74

# ── Verdict badge ──
tag = "MISLEADING"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+14
tx = (WIDTH - tw) // 2
draw.rounded_rectangle([(tx, y), (tx+tw, y+th)], radius=5, fill=ORANGE)
draw.text((WIDTH//2, y+th//2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 12

# ── Topic ──
draw.text((WIDTH//2, y), "Prison Safety / HALT Act", fill=NAVY, font=f_topic, anchor="mm")
y += 48
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 20

# ── His claim box ──
box_h = 148
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box_h)], radius=8,
                        fill=ORANGE_BG, outline=ORANGE_BD, width=2)
draw.text((76, y+16), "HE CLAIMED — May 20, 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+48), '"The attack at Collins Correctional', fill=DARK, font=f_claim)
draw.text((76, y+84), 'is the result of... the HALT Act."', fill=DARK, font=f_claim)
y += box_h + 22

# ── Divider ──
draw.text((WIDTH//2, y), "THE DATA SAYS OTHERWISE", fill=MUTED, font=font("Arial Bold.ttf", 20), anchor="mm")
y += 30
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 20

# ── Fact 1 ──
box2_h = 230
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box2_h)], radius=8,
                        fill="#FFF5F0", outline="#FBD38D", width=2)
draw.text((WIDTH//2, y+18), "Staff assaults in NY prisons rose every year since", fill=DARK,
          font=f_claim_b, anchor="mm")
draw.text((WIDTH//2, y+80), "2016", fill=ORANGE, font=f_big, anchor="mm")
draw.text((WIDTH//2, y+168), "— 5 years before the HALT Act passed —", fill=MUTED,
          font=f_sub, anchor="mm")
draw.text((WIDTH//2, y+200), "The trend has nothing to do with the law.", fill=MUTED,
          font=f_sub, anchor="mm")
y += box2_h + 18

draw.line([(100, y), (WIDTH-100, y)], fill=BORDER, width=1)
y += 20

# ── Fact 2 ──
box3_h = 160
draw.rounded_rectangle([(44, y), (WIDTH-44, y+box3_h)], radius=8,
                        fill="#FFF5F0", outline="#FBD38D", width=2)
draw.text((WIDTH//2, y+20), "40% of prisoners were held in solitary", fill=DARK,
          font=f_claim_b, anchor="mm")
draw.text((WIDTH//2, y+54), "longer than the HALT Act's legal limit.", fill=DARK,
          font=f_claim_b, anchor="mm")
draw.text((WIDTH//2, y+100), "You can't blame a law that", fill=MUTED, font=f_sub, anchor="mm")
draw.text((WIDTH//2, y+128), "wasn't being followed.", fill=MUTED, font=f_sub, anchor="mm")
y += box3_h + 20

draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# ── Source ──
draw.text((WIDTH//2, y), "Source: Prison Policy Initiative, April 2025  ·  NY Correction Law § 137",
          fill=MUTED, font=f_small, anchor="mm")
y += 24
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-20-halt-act-collins-causal-claim",
          fill=MUTED, font=f_small, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-28), "langworthywatch.org  ·  NY-23 Accountability", fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/halt_act_collins_misleading.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
