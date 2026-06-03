#!/usr/bin/env python3
"""Social card: Grape belt / Refresco — MISSING CONTEXT — June 2, 2026."""

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

f_brand  = font("Arial Bold.ttf", 22)
f_tag    = font("Arial Bold.ttf", 20)
f_topic  = font("Arial Bold.ttf", 32)
f_label  = font("Arial Bold.ttf", 18)
f_label_s= font("Arial Bold.ttf", 14)
f_big    = font("Impact.ttf", 78)
f_stat   = font("Impact.ttf", 48)
f_sub_b  = font("Arial Bold.ttf", 20)
f_sub    = font("Arial.ttf", 18)
f_small  = font("Arial.ttf", 16)
f_xs     = font("Arial.ttf", 14)
f_xs_b   = font("Arial Bold.ttf", 14)
f_note_b = font("Arial Bold.ttf", 17)
f_note   = font("Arial.ttf", 17)
f_footer = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH//2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62
# Verdict badge
tag = "MISSING CONTEXT"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 10

draw.text((WIDTH//2, y), "Agriculture / Grape Belt", fill=NAVY, font=f_topic, anchor="mm")
y += 42
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# THE SHOCK BOX
shock_h = 132
draw.rounded_rectangle([(44, y), (WIDTH-44, y+shock_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+14), "THE SHOCK — REFRESCO CANCELLATION, MARCH 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((220, y+shock_h//2+10), "126", fill=ORANGE, font=f_big, anchor="mm")
draw.text((WIDTH-220, y+shock_h//2+10), "2,600", fill=ORANGE, font=f_big, anchor="mm")
draw.text((220, y+shock_h-22), "growers affected", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((WIDTH-220, y+shock_h-22), "acres of contracts canceled", fill=DARK, font=f_sub_b, anchor="mm")
y += shock_h + 16

# TWO-PANEL COMPARISON
col_w = (WIDTH - 44*2 - 16) // 2
col_h = 322
lx = 44
rx = lx + col_w + 16

# LEFT — Pre-Refresco federal action
draw.rounded_rectangle([(lx, y), (lx+col_w, y+col_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((lx+col_w//2, y+18), "JANUARY 2026 — PRE-REFRESCO", fill=GREEN, font=f_label_s, anchor="mm")
draw.text((lx+col_w//2, y+76), "$20M", fill=GREEN, font=f_big, anchor="mm")
draw.text((lx+col_w//2, y+138), "USDA Section 32 buy", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((lx+col_w//2, y+162), "Concord grape juice for", fill=DARK, font=f_sub, anchor="mm")
draw.text((lx+col_w//2, y+184), "school lunches + food banks", fill=DARK, font=f_sub, anchor="mm")
draw.line([(lx+24, y+212), (lx+col_w-24, y+212)], fill="#9AE6B4", width=1)
draw.text((lx+col_w//2, y+232), "WHAT HE DID:", fill=MUTED, font=f_xs_b, anchor="mm")
draw.text((lx+col_w//2, y+254), "→ Letter to USDA Sec. Rollins", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+274), "→ Press release on the buy", fill=DARK, font=f_xs, anchor="mm")
draw.text((lx+col_w//2, y+294), "→ Grape Research Act intro", fill=DARK, font=f_xs, anchor="mm")

# RIGHT — Post-Refresco
draw.rounded_rectangle([(rx, y), (rx+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((rx+col_w//2, y+18), "MARCH 2026 — POST-REFRESCO", fill=RED, font=f_label_s, anchor="mm")
draw.text((rx+col_w//2, y+76), "0", fill=RED, font=f_big, anchor="mm")
draw.text((rx+col_w//2, y+138), "new federal actions", fill=DARK, font=f_sub_b, anchor="mm")
draw.text((rx+col_w//2, y+162), "Press appearances only —", fill=DARK, font=f_sub, anchor="mm")
draw.text((rx+col_w//2, y+184), "the buyer-exit problem is new", fill=DARK, font=f_sub, anchor="mm")
draw.line([(rx+24, y+212), (rx+col_w-24, y+212)], fill="#FEB2B2", width=1)
draw.text((rx+col_w//2, y+232), "WHAT'S MISSING:", fill=MUTED, font=f_xs_b, anchor="mm")
draw.text((rx+col_w//2, y+254), "—  No new letter to USDA", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+274), "—  No second Section 32 ask", fill=DARK, font=f_xs, anchor="mm")
draw.text((rx+col_w//2, y+294), "—  No processor-risk bill / hearing", fill=DARK, font=f_xs, anchor="mm")

y += col_h + 16

# COUNTY-LEVEL MITIGATION FOOTNOTE
cav_h = 92
draw.rounded_rectangle([(44, y), (WIDTH-44, y+cav_h)], radius=6,
                        fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+20), "The only concrete post-Refresco mitigation is the CCIDA's $200K loan to",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+44), "WMC Grape Juice LLC in Westfield (May 2026, November 2026 target start).",
          fill=DARK, font=f_note, anchor="mm")
draw.text((WIDTH//2, y+68), "That is a county-level action, not federal.",
          fill=MUTED, font=f_note_b, anchor="mm")
y += cav_h + 14

# Sources + URL
draw.text((WIDTH//2, y), "Sources: USDA AMS  ·  langworthy.house.gov  ·  Post-Journal  ·  WGRZ  ·  WENY",
          fill=MUTED, font=f_small, anchor="mm")
y += 24
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-02-grape-belt-refresco-federal-response/",
          fill=NAVY, font=f_small, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/grape_belt_refresco.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
