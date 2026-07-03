#!/usr/bin/env python3
"""Social card: HR 9237 — the Rules vote that kept the 'Star Act without the cuts'
amendment off the floor. DOCUMENTED PATTERN, July 3, 2026."""

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
f_colh=font("Arial Bold.ttf",18); f_big=font("Impact.ttf",54); f_sub=font("Arial.ttf",18)
f_small=font("Arial.ttf",17); f_body=font("Arial.ttf",16); f_src=font("Arial.ttf",15)
f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)

draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64

tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+24

draw.text((WIDTH//2,y),"The Star Act, Without the Cuts",fill=NAVY,font=f_topic,anchor="mm"); y+=34
draw.text((WIDTH//2,y),"A recorded chance on the Rules Committee, and how he voted.",
          fill=MUTED,font=font("Arial.ttf",16),anchor="mm"); y+=16
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# the bill context box
ctx_h=126
draw.rounded_rectangle([(44,y),(WIDTH-44,y+ctx_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((76,y+16),"THE BILL  ·  H.R. 9237",fill=NAVY,font=f_label_s,anchor="lm")
draw.text((76,y+44),"Real expansions (caregiver, student vets, catastrophically disabled),",fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+70),"paid for by cutting FUTURE disability comp for sleep apnea + tinnitus.",fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+98),"Existing ratings protected. VFW, DAV, and IAVA oppose it.",fill=MUTED,font=f_small,anchor="lm")
y+=ctx_h+16

# two vote boxes
col_w=(WIDTH-44*2-16)//2; col_h=214; lx=44; rx=lx+col_w+16
# 369
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((lx+col_w//2,y+20),"RECORD VOTE 369",fill=RED,font=f_colh,anchor="mm")
draw.text((lx+col_w//2,y+68),"NO",fill=RED,font=f_big,anchor="mm")
draw.text((lx+col_w//2,y+118),"on the amendment to pass",fill=DARK,font=f_body,anchor="mm")
draw.text((lx+col_w//2,y+140),"the Major Richard Star Act",fill=DARK,font=f_body,anchor="mm")
draw.text((lx+col_w//2,y+162),"WITHOUT the cuts.",fill=DARK,font=font("Arial Bold.ttf",16),anchor="mm")
draw.text((lx+col_w//2,y+186),"Kept off the floor (4-8).",fill=MUTED,font=font("Arial.ttf",14),anchor="mm")
# 373
draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+20),"RECORD VOTE 373",fill=RED,font=f_colh,anchor="mm")
draw.text((rx+col_w//2,y+68),"YES",fill=RED,font=f_big,anchor="mm")
draw.text((rx+col_w//2,y+118),"to report the CLOSED rule",fill=DARK,font=f_body,anchor="mm")
draw.text((rx+col_w//2,y+140),"that barred all floor",fill=DARK,font=f_body,anchor="mm")
draw.text((rx+col_w//2,y+162),"amendments to the bill.",fill=DARK,font=font("Arial Bold.ttf",16),anchor="mm")
draw.text((rx+col_w//2,y+186),"Adopted (8-4).",fill=MUTED,font=font("Arial.ttf",14),anchor="mm")
y+=col_h+16

# kicker
kick_h=94
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+30),"A clean chance to deliver the benefit everyone praises without the cut the",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+62),"veterans' groups oppose. He voted to keep it off the table.",
          fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+12

# accuracy note
draw.text((WIDTH//2,y),"(The \"misleading veterans\" post was the House VA Committee GOP's, not Langworthy's.",
          fill=MUTED,font=font("Arial.ttf",13),anchor="mm"); y+=18
draw.text((WIDTH//2,y),"This documents his Rules Committee vote.)",fill=MUTED,font=font("Arial.ttf",13),anchor="mm"); y+=22

draw.text((WIDTH//2,y),"Source: House Rules Committee report (H. Rept. 119-707)",fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-03-hr9237-rules-vote-veterans-benefit-cuts/",
          fill=NAVY,font=font("Arial.ttf",13),anchor="mm")

draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/hr9237_rules_vote_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
