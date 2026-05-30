#!/usr/bin/env python3
"""Social card: Drug-pricing reform claim — MISLEADING — May 30, 2026."""

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
TRUMP   = "#2B6CB0"   # blue for Trump program
IRA     = "#553C9A"   # purple for IRA

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand   = font("Arial Bold.ttf", 22)
f_tag     = font("Arial Bold.ttf", 20)
f_topic   = font("Arial Bold.ttf", 32)
f_label   = font("Arial Bold.ttf", 18)
f_label_s = font("Arial Bold.ttf", 14)
f_big     = font("Impact.ttf", 64)
f_stat    = font("Impact.ttf", 44)
f_sub_b   = font("Arial Bold.ttf", 20)
f_sub     = font("Arial.ttf", 19)
f_small   = font("Arial.ttf", 17)
f_xs      = font("Arial.ttf", 14)
f_xs_b    = font("Arial Bold.ttf", 14)
f_quote   = font("Arial.ttf", 17)
f_quote_b = font("Arial Bold.ttf", 17)
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
tag = "MISLEADING"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                        fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 10

# ── Topic ──
draw.text((WIDTH//2, y), "Healthcare / Drug Pricing", fill=NAVY, font=f_topic, anchor="mm")
y += 42
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 14

# ── THE CLAIM BOX ──
claim_h = 168
draw.rounded_rectangle([(44, y), (WIDTH-44, y+claim_h)], radius=8,
                        fill="#FFFAF0", outline="#F6AD55", width=2)
draw.text((76, y+14), "THE CLAIM — Facebook, May 29, 2026", fill=ORANGE, font=f_label, anchor="lm")
draw.text((76, y+46), "“Reforming healthcare means putting patients first and the", fill=DARK, font=f_quote, anchor="lm")
draw.text((76, y+70), "results are ", fill=DARK, font=f_quote, anchor="lm")
draw.text((158, y+70), "already underway", fill=DARK, font=f_quote_b, anchor="lm")
draw.text((297, y+70), ": more than 600 generics added,", fill=DARK, font=f_quote, anchor="lm")
draw.text((76, y+94), "direct discounts, and Medicare savings of 44%. That’s", fill=DARK, font=f_quote, anchor="lm")
draw.text((76, y+118), "$12 billion in savings on 15 major drugs.”", fill=DARK, font=f_quote, anchor="lm")
draw.text((76, y+144), "— Rep. Nick Langworthy (NY-23)", fill=MUTED, font=f_small, anchor="lm")

y += claim_h + 14

# ── BREAKDOWN: THREE COLUMNS ──
col_w = 320
col_gap = 14
col_total = col_w * 3 + col_gap * 2
col_x0 = (WIDTH - col_total) // 2
col_h = 270

# Column 1: 600 generics → Trump initiative
c1x = col_x0
draw.rounded_rectangle([(c1x, y), (c1x+col_w, y+col_h)], radius=8,
                        fill="#EBF4FF", outline="#90CDF4", width=2)
draw.text((c1x+col_w//2, y+16), "“600 GENERICS”", fill=TRUMP, font=f_label_s, anchor="mm")
draw.text((c1x+col_w//2, y+66), "600+", fill=TRUMP, font=f_big, anchor="mm")
draw.text((c1x+col_w//2, y+120), "generic medicines listed", fill=DARK, font=f_small, anchor="mm")
draw.text((c1x+col_w//2, y+142), "at discounted prices", fill=DARK, font=f_small, anchor="mm")
draw.line([(c1x+24, y+168), (c1x+col_w-24, y+168)], fill="#90CDF4", width=1)
draw.text((c1x+col_w//2, y+188), "ACTUAL SOURCE:", fill=MUTED, font=f_xs_b, anchor="mm")
draw.text((c1x+col_w//2, y+212), "TrumpRx.gov", fill=TRUMP, font=f_sub_b, anchor="mm")
draw.text((c1x+col_w//2, y+236), "Trump admin executive", fill=DARK, font=f_xs, anchor="mm")
draw.text((c1x+col_w//2, y+254), "initiative, May 18, 2026", fill=DARK, font=f_xs, anchor="mm")

# Column 2: 44% / $12B / 15 drugs → IRA Round 2
c2x = c1x + col_w + col_gap
draw.rounded_rectangle([(c2x, y), (c2x+col_w, y+col_h)], radius=8,
                        fill="#FAF5FF", outline="#B794F4", width=2)
draw.text((c2x+col_w//2, y+16), "“44% / $12B / 15 DRUGS”", fill=IRA, font=f_label_s, anchor="mm")
draw.text((c2x+col_w//2, y+66), "$12B", fill=IRA, font=f_big, anchor="mm")
draw.text((c2x+col_w//2, y+120), "44% average savings on", fill=DARK, font=f_small, anchor="mm")
draw.text((c2x+col_w//2, y+142), "15 negotiated drugs", fill=DARK, font=f_small, anchor="mm")
draw.line([(c2x+24, y+168), (c2x+col_w-24, y+168)], fill="#B794F4", width=1)
draw.text((c2x+col_w//2, y+188), "ACTUAL SOURCE:", fill=MUTED, font=f_xs_b, anchor="mm")
draw.text((c2x+col_w//2, y+212), "IRA §11001, Round 2", fill=IRA, font=f_sub_b, anchor="mm")
draw.text((c2x+col_w//2, y+236), "every House Republican", fill=DARK, font=f_xs, anchor="mm")
draw.text((c2x+col_w//2, y+254), "voted NO on the IRA", fill=DARK, font=f_xs, anchor="mm")

# Column 3: "Already underway" → Jan 1, 2027
c3x = c2x + col_w + col_gap
draw.rounded_rectangle([(c3x, y), (c3x+col_w, y+col_h)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((c3x+col_w//2, y+16), "“ALREADY UNDERWAY”", fill=RED, font=f_label_s, anchor="mm")
draw.text((c3x+col_w//2, y+66), "Jan 1", fill=RED, font=f_big, anchor="mm")
draw.text((c3x+col_w//2, y+118), "2027", fill=RED, font=f_stat, anchor="mm")
draw.line([(c3x+24, y+168), (c3x+col_w-24, y+168)], fill="#FEB2B2", width=1)
draw.text((c3x+col_w//2, y+188), "ACTUAL TIMING:", fill=MUTED, font=f_xs_b, anchor="mm")
draw.text((c3x+col_w//2, y+212), "Not yet in effect", fill=RED, font=f_sub_b, anchor="mm")
draw.text((c3x+col_w//2, y+236), "Round 2 prices take effect", fill=DARK, font=f_xs, anchor="mm")
draw.text((c3x+col_w//2, y+254), "January 1, 2027", fill=DARK, font=f_xs, anchor="mm")

y += col_h + 14

# ── OBBBA §71203 BOX — what Langworthy DID vote on ──
obbba_h = 130
draw.rounded_rectangle([(44, y), (WIDTH-44, y+obbba_h)], radius=8,
                        fill="#FFF5F5", outline="#FC8181", width=2)
draw.text((76, y+14), "WHAT LANGWORTHY DID VOTE ON — OBBBA §71203", fill=RED, font=f_label, anchor="lm")
draw.text((188, y+obbba_h//2+10), "−$8.8B", fill=RED, font=f_big, anchor="mm")

vx = 372
draw.text((vx, y+44), "ORPHAN Cures Act provision", fill=DARK, font=f_sub_b, anchor="lm")
draw.text((vx, y+68), "Expanded orphan-drug carve-out from negotiation", fill=DARK, font=f_sub, anchor="lm")
draw.text((vx, y+90), "CBO: −$8.8 billion in future Medicare drug-negotiation", fill=MUTED, font=f_small, anchor="lm")
draw.text((vx, y+108), "savings over 10 years · Roll Call 190, July 3, 2025", fill=MUTED, font=f_small, anchor="lm")

y += obbba_h + 14

# ── TIMELINE STRIP ──
tl_h = 86
draw.rounded_rectangle([(44, y), (WIDTH-44, y+tl_h)], radius=6,
                        fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+11), "THE SEQUENCE", fill=NAVY, font=font("Arial Bold.ttf", 14), anchor="mm")

evts = [
    ("Aug 2022",   "IRA passes —",        "Langworthy not yet in Congress"),
    ("Jul 2025",   "Langworthy votes YES", "OBBBA §71203 (−$8.8B future savings)"),
    ("May 2026",   "Posts the claim —",    "“results already underway”"),
    ("Jan 2027",   "Round 2 prices take effect", "(the $12B / 44% / 15 drugs)"),
]
ew = (WIDTH - 88) // 4
for i, (dt, line1, line2) in enumerate(evts):
    ex = 44 + i * ew + ew // 2
    color = IRA if i == 0 else RED if i == 1 else ORANGE if i == 2 else GREEN
    draw.text((ex, y+30), dt, fill=color, font=font("Arial Bold.ttf", 13), anchor="mm")
    draw.text((ex, y+50), line1, fill=DARK, font=font("Arial Bold.ttf", 12), anchor="mm")
    draw.text((ex, y+68), line2, fill=MUTED, font=font("Arial.ttf", 11), anchor="mm")
    if i < 3:
        ax = 44 + (i + 1) * ew
        draw.text((ax, y+tl_h//2+8), "→", fill=MUTED, font=font("Arial Bold.ttf", 16), anchor="mm")

y += tl_h + 12

# ── CAVEAT ──
cav_h = 72
draw.rounded_rectangle([(44, y), (WIDTH-44, y+cav_h)], radius=6,
                        fill="#FFFAF0", outline="#F6AD55", width=1)
draw.text((WIDTH//2, y+20), "The dollar figures are real — but the post conflates a Trump executive program",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+44), "with IRA outcomes and calls savings effective Jan 2027 “already underway.”",
          fill=MUTED, font=f_note, anchor="mm")
y += cav_h + 12

# ── Sources ──
draw.text((WIDTH//2, y), "Sources: CMS  ·  KFF  ·  CBO  ·  P.L. 117-169 §11001  ·  P.L. 119-21 §71203",
          fill=MUTED, font=f_small, anchor="mm")
y += 22
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-05-30-drug-pricing-reform-claim/",
          fill=NAVY, font=f_small, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/drug_pricing_misleading.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
