#!/usr/bin/env python3
"""Social card: OBBBA 'largest tax cut' anniversary, MISLEADING, June 30, 2026.
Not the largest, not paid for; benefit up now, cost down later."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_big=font("Impact.ttf",78)
f_stat=font("Impact.ttf",44); f_sub_b=font("Arial Bold.ttf",21); f_sub=font("Arial.ttf",18)
f_small=font("Arial.ttf",17); f_xs=font("Arial.ttf",14); f_xs_b=font("Arial Bold.ttf",14)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64
tag="MISLEADING"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+30
draw.text((WIDTH//2,y),"The 'Largest Tax Cut in History,' by the Numbers",fill=NAVY,font=f_topic,anchor="mm"); y+=44
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=18

claim_h=124
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+16),"WHAT HE SAID  ·  Anniversary post, July 2026",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+50),'"The one-year anniversary of the LARGEST TAX CUT',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+76),'in U.S. history. Here\'s how it helped your family."',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+102),"Rep. Nick Langworthy (NY-23)",fill=MUTED,font=f_small,anchor="lm")
y+=claim_h+18

col_w=(WIDTH-44*2-16)//2; col_h=274; lx=44; rx=lx+col_w+16
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#EBF8F0",outline="#9AE6B4",width=2)
draw.text((lx+col_w//2,y+22),"TOP 10% OF HOUSEHOLDS",fill=GREEN,font=f_label_s,anchor="mm")
draw.text((lx+col_w//2,y+92),"+$13,600",fill=GREEN,font=f_big,anchor="mm")
draw.text((lx+col_w//2,y+158),"a year (CBO)",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((lx+col_w//2,y+188),"business + $15M+ estate breaks:",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+216),"permanent",fill=DARK,font=f_sub,anchor="mm")
draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+22),"BOTTOM 10% OF HOUSEHOLDS",fill=RED,font=f_label_s,anchor="mm")
draw.text((rx+col_w//2,y+92),"−$1,200",fill=RED,font=f_big,anchor="mm")
draw.text((rx+col_w//2,y+158),"a year, worse off (CBO)",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((rx+col_w//2,y+188),"after the Medicaid + SNAP",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+216),"cuts that help pay for it",fill=DARK,font=f_sub,anchor="mm")
y+=col_h+18

strip_h=150
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+20),"THE FULL PICTURE",fill=NAVY,font=f_label,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,l2,c) in enumerate([
    ("+$4.1T","added to the debt","$5.5T if extended",NAVY),
    ("6th","largest since 1940","1.40% of GDP",RED),
    ("2028","worker breaks expire","business breaks: permanent",GREEN),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+72),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+108),l1,fill=DARK,font=f_xs_b,anchor="mm")
    draw.text((cx,y+128),l2,fill=MUTED,font=f_xs,anchor="mm")
y+=strip_h+18

kick_h=96
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+30),"Not the largest in history. Not paid for. The temporary breaks go to workers;",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+62),"the permanent ones go to capital. The people who gain least pay twice.",
          fill=WHITE,font=font("Arial Bold.ttf",20),anchor="mm")
y+=kick_h+16
draw.text((WIDTH//2,y),"Sources: CBO  ·  Joint Committee on Taxation  ·  Tax Foundation  ·  CRFB  ·  Penn Wharton",
          fill=MUTED,font=f_src,anchor="mm"); y+=26
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-06-30-largest-tax-cut-anniversary/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/tax_cut_deficit_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
