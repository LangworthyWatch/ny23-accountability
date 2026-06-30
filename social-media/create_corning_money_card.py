#!/usr/bin/env python3
"""Social card: Corning 'follow the money', DOCUMENTED PATTERN, June 2026.
Names the C-suite donors and the post-vote timing. A sequence, not a quid pro quo."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_sub_head=font("Arial.ttf",17); f_big=font("Impact.ttf",60); f_name=font("Arial Bold.ttf",22)
f_title=font("Arial.ttf",16); f_amt=font("Arial Bold.ttf",24); f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62
tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+22
draw.text((WIDTH//2,y),"Follow the Money: Corning's Leadership Gave to Langworthy",fill=NAVY,font=font("Arial Bold.ttf",27),anchor="mm"); y+=34
draw.text((WIDTH//2,y),"After he voted for a law that preserved the company's manufacturing tax credits.",
          fill=MUTED,font=f_sub_head,anchor="mm"); y+=24
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=14

# -- total band --
band_h=66
draw.rounded_rectangle([(44,y),(WIDTH-44,y+band_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((96,y+band_h//2),"$65,775",fill=RED,font=f_big,anchor="lm")
draw.text((WIDTH-96,y+22),"from 62 Corning employees, CEO to engineers",fill=DARK,font=font("Arial Bold.ttf",18),anchor="rm")
draw.text((WIDTH-96,y+46),"the largest gifts arrived Sep-Oct 2025, after the July 3 vote",fill=MUTED,font=f_title,anchor="rm")
y+=band_h+14

# -- named leadership list --
rows=[
    ("Wendell Weeks","Chairman & CEO","$5,000"),
    ("Lewis Steverson","General Counsel","$5,000"),
    ("Edward Schlesinger","Chief Financial Officer","$2,500"),
    ("Stefan Becker","SVP, Corporate Controller","$2,500"),
    ("Michelle O'Neill","VP, Government Affairs","$2,500"),
    ("Jaymin Amin","Chief Technology Officer","$1,250"),
]
panel_top=y; rh=62; panel_h=rh*len(rows)+50
draw.rounded_rectangle([(44,panel_top),(WIDTH-44,panel_top+panel_h)],radius=10,fill=WHITE,outline=BORDER,width=2)
ry=panel_top+6
for i,(name,title,amt) in enumerate(rows):
    if i>0: draw.line([(72,ry),(WIDTH-72,ry)],fill="#EDF2F7",width=2)
    draw.text((76,ry+22),name,fill=DARK,font=f_name,anchor="lm")
    draw.text((76,ry+44),title,fill=MUTED,font=f_title,anchor="lm")
    draw.text((WIDTH-76,ry+rh//2),amt,fill=RED,font=f_amt,anchor="rm")
    ry+=rh
draw.line([(72,ry),(WIDTH-72,ry)],fill="#EDF2F7",width=2)
draw.text((76,ry+25),"and 56 more Corning employees, engineers to attorneys",fill=MUTED,font=font("Arial.ttf",17),anchor="lm")
draw.text((WIDTH-76,ry+25),"= $65,775",fill=DARK,font=font("Arial Bold.ttf",18),anchor="rm")
y=panel_top+panel_h+14

# -- Kicker --
kick_h=84
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+26),"He represents Corning's hometown, so some employee giving is routine.",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+56),"Public records show the timing, not the reason. This page claims no quid pro quo.",
          fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+12
draw.text((WIDTH//2,y),"Sources: FEC bulk files (indiv24, indiv26)  ·  House Clerk Roll Call 190  ·  P.L. 119-21",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-05-29-corning-manufacturing-credits-obbba/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/corning_money_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
