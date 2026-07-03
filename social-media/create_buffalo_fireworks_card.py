#!/usr/bin/env python3
"""Social card: Buffalo July 4 fireworks + Somali flag. The claim vs. what the
city actually said. MISLEADING, July 2, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"
WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()

f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16)
f_tile_h=font("Arial Bold.ttf",19); f_sub=font("Arial.ttf",18); f_small=font("Arial.ttf",17)
f_body=font("Arial.ttf",16); f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)

# Brand bar
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64

# Verdict badge
tag="MISLEADING"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26

draw.text((WIDTH//2,y),"Fireworks, a Flag, and a Missing Launch Site",fill=NAVY,font=f_topic,anchor="mm"); y+=34
draw.text((WIDTH//2,y),"The claim: no fireworks site + a Somali flag = 'a choice about what they value.'",
          fill=MUTED,font=font("Arial.ttf",16),anchor="mm"); y+=16
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# Claim box
claim_h=128
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+16),"WHAT HE SAID  ·  Facebook posts, July 1, 2026",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+48),'"The decision to cancel fireworks ... while raising the Somali',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+74),'flag has everything to do with THAT and nothing to do with logistics."',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+102),"Rep. Nick Langworthy (NY-23)",fill=MUTED,font=f_small,anchor="lm")
y+=claim_h+16

# "THE RECORD" 2x2 grid
draw.text((WIDTH//2,y+2),"WHAT THE CITY ACTUALLY SAID",fill=NAVY,font=f_label,anchor="mm"); y+=24

tiles=[
    ("A FLAGPOLE ISN'T A LAUNCH SITE", GREEN, [
        "The city said no downtown spot could clear a",
        "safe fireworks fallout zone near City Hall. A",
        "flag uses a pole that is already there."]),
    ("THE FLAG-RAISING WAS ROUTINE", NAVY, [
        "An annual event by the nonprofit Heal Intl,",
        "4+ years running. The same poles fly Ukraine,",
        "Ireland, Greece, Puerto Rico, and more."]),
    ("NOTHING WAS 'CANCELED'", ORANGE, [
        "Buffalo has not held a city July 4 show since",
        "2015. Ryan was trying to ADD one downtown;",
        "the vendor and sponsor were already lined up."]),
    ("AMERICA 250 FIREWORKS ARE ON", GREEN, [
        "Buffalo and Erie County are marking the 250th",
        "with fireworks Aug. 2 at Canalside, launched",
        "from a barge on the river."]),
]
col_w=(WIDTH-44*2-16)//2; tile_h=176; lx=44; rx=lx+col_w+16
fills={GREEN:("#EBF8F0","#9AE6B4"),NAVY:("#EDF2F7","#CBD5E0"),ORANGE:("#FFFAF0","#F6AD55"),RED:("#FFF5F5","#FEB2B2")}
for i,(head,color,lines) in enumerate(tiles):
    row,coln=divmod(i,2)
    tx=lx if coln==0 else rx
    ty=y+row*(tile_h+14)
    fill,outline=fills[color]
    draw.rounded_rectangle([(tx,ty),(tx+col_w,ty+tile_h)],radius=8,fill=fill,outline=outline,width=2)
    draw.text((tx+22,ty+22),head,fill=color,font=f_tile_h,anchor="lm")
    ly=ty+58
    for ln in lines:
        draw.text((tx+22,ly),ln,fill=DARK,font=f_body,anchor="lm"); ly+=26
y+=tile_h*2+14+18

# Kicker
kick_h=92
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+30),"The choice was never fireworks vs. no fireworks. It was an added downtown show",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+60),"vs. the barge show already booked for August. The 250th is still being celebrated.",
          fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+14

draw.text((WIDTH//2,y),"Sources: Spectrum News  ·  Buffalo Toronto Public Media  ·  Buffalo News  ·  WGRZ",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-02-buffalo-fireworks-somali-flag/",
          fill=NAVY,font=f_src,anchor="mm")

# Footer bar
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/buffalo_fireworks_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
