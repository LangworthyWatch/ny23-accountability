#!/usr/bin/env python3
"""Social card: Corning convergence, DOCUMENTED PATTERN, June 2026.
Three threads in the public record: the law, the money, the office move. Not a quid pro quo."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_num=font("Impact.ttf",72)
f_sub_b=font("Arial Bold.ttf",22); f_sub=font("Arial.ttf",18); f_small=font("Arial.ttf",17)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62
tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill=NAVY,outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+22
draw.text((WIDTH//2,y),"Corning Inc.: The Law, the Money, the Office",fill=NAVY,font=f_topic,anchor="mm"); y+=38
draw.text((WIDTH//2,y),"Three threads in the public record, in sequence.",fill=MUTED,font=font("Arial.ttf",17),anchor="mm"); y+=24
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

bands=[
    ("1","THE LAW",NAVY,
     "OBBBA kept Corning's 45X solar credit and raised its chip credit 25% to 35%.",
     "He voted Yes on the bill (Roll Call 190) and called it a generational win."),
    ("2","THE MONEY",NAVY,
     "62 Corning employees, from the CEO to engineers, gave $65,775.",
     "Most of it arrived in the months after the vote."),
    ("3","THE OFFICE",NAVY,
     "His district office moved from Corning (Steuben) to Elmira (Chemung),",
     "the county where much of Corning's workforce, and several donors, live."),
]
bh=166; gap=16
for num,label,c,l1,l2 in bands:
    draw.rounded_rectangle([(44,y),(WIDTH-44,y+bh)],radius=10,fill="#EDF2F7",outline=BORDER,width=2)
    draw.text((104,y+bh//2),num,fill=c,font=f_num,anchor="mm")
    draw.line([(168,y+26),(168,y+bh-26)],fill="#CBD5E0",width=2)
    tx=192
    draw.text((tx,y+38),label,fill=NAVY,font=f_label_s,anchor="lm")
    draw.text((tx,y+82),l1,fill=DARK,font=f_sub_b,anchor="lm")
    draw.text((tx,y+120),l2,fill=MUTED,font=f_sub,anchor="lm")
    y+=bh+gap
y+=2

kick_h=104
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+30),"Not proof of a deal. A documented sequence: a company lobbied, a member voted,",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+58),"its people donated, the office moved closer. Public records can't resolve why;",
          fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
draw.text((WIDTH//2,y+82),"readers can weigh the pattern.",fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+14
draw.text((WIDTH//2,y),"Sources: FEC bulk files  ·  Senate lobbying disclosures  ·  P.L. 119-21  ·  clerk.house.gov",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-05-29-corning-manufacturing-credits-obbba/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/corning_pattern_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
