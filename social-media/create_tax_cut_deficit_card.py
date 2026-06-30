#!/usr/bin/env python3
"""Social card: OBBBA 'largest tax cut' anniversary, MISLEADING, June 30, 2026.
Deficit as the big central hero; the cost shifts down (poor now) and forward (future taxpayers)."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16)
f_hero=font("Impact.ttf",138); f_stat=font("Impact.ttf",52); f_sub_b=font("Arial Bold.ttf",22)
f_sub=font("Arial.ttf",18); f_small=font("Arial.ttf",17); f_xs=font("Arial.ttf",14)
f_xs_b=font("Arial Bold.ttf",15); f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64
tag="MISLEADING"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26
draw.text((WIDTH//2,y),"The 'Largest Tax Cut in History,' by the Deficit",fill=NAVY,font=f_topic,anchor="mm"); y+=42
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# -- WHAT HE SAID --
claim_h=104
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+14),"WHAT HE SAID  ·  Anniversary post, July 2026",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+46),'"The LARGEST TAX CUT in U.S. history. Here\'s how it helped your family."',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+78),"Rep. Nick Langworthy (NY-23)",fill=MUTED,font=f_small,anchor="lm")
y+=claim_h+18

# -- HERO: the deficit, large and central --
hero_h=252
draw.rounded_rectangle([(44,y),(WIDTH-44,y+hero_h)],radius=10,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((WIDTH//2,y+30),"WHAT THE POST LEAVES OUT: IT ISN'T PAID FOR",fill=RED,font=f_label_s,anchor="mm")
draw.text((WIDTH//2,y+112),"+$4.1T",fill=RED,font=f_hero,anchor="mm")
draw.text((WIDTH//2,y+200),"added to a debt already past $39 trillion",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((WIDTH//2,y+230),"near 130% of GDP  ·  $5.5 trillion more if the 2028 breaks are extended",
          fill=MUTED,font=f_small,anchor="mm")
y+=hero_h+18

# -- WHERE THE COST SHIFTS --
strip_h=176
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+22),"WHO GAINS, AND WHO PAYS",fill=NAVY,font=f_label,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,l2,c) in enumerate([
    ("+$13,600","top 10%, per year","gains now (CBO)",GREEN),
    ("−$1,200","bottom 10%, per year","worse off, no tax cut (CBO)",RED),
    ("$4.1T","future taxpayers","inherit the debt, later",NAVY),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+86),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+126),l1,fill=DARK,font=f_xs_b,anchor="mm")
    draw.text((cx,y+148),l2,fill=MUTED,font=f_xs,anchor="mm")
y+=strip_h+16

# -- Kicker --
kick_h=92
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+28),"Sold as a family tax cut. For the lowest-income households it wasn't one at all:",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+60),"after the Medicaid and SNAP cuts that pay for it, they come out behind, not ahead.",
          fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+14
draw.text((WIDTH//2,y),"Sources: CBO  ·  Joint Committee on Taxation  ·  Tax Foundation  ·  CRFB  ·  Penn Wharton",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-06-30-largest-tax-cut-anniversary/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/tax_cut_deficit_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
