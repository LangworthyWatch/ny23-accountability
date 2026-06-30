#!/usr/bin/env python3
"""Social card: Corning convergence, DOCUMENTED PATTERN, June 2026.
Lobbying -> OBBBA credits -> vote -> donations -> office move. A sequence, not a quid pro quo."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_sub_head=font("Arial.ttf",17); f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16)
f_stat=font("Impact.ttf",46); f_rowlabel=font("Arial Bold.ttf",23); f_rowsub=font("Arial.ttf",17)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62
tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+24
draw.text((WIDTH//2,y),"The Company in the District: Corning + Langworthy",fill=NAVY,font=f_topic,anchor="mm"); y+=38
draw.text((WIDTH//2,y),"A sequence in the public record. Not proof of a connection, and not a quid pro quo.",
          fill=MUTED,font=f_sub_head,anchor="mm"); y+=26
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# -- sequence panel --
rows=[
    ("$700K+","Lobbied on the bill","2025 disclosures name the reconciliation bill",NAVY),
    ("35%","Its chip credit, raised from 25%","OBBBA also kept Corning's solar (45X) credit",GREEN),
    ("YES","Langworthy's vote on it","Roll Call 190; he called it 'a generational win'",RED),
    ("$65,775","From 62 Corning employees","CEO to engineers, most of it after the vote",RED),
    ("2026","Then the office moved to Elmira","into Chemung County, where much of the workforce lives",NAVY),
]
rh=104; panel_top=y; panel_h=rh*len(rows)+16
draw.rounded_rectangle([(44,panel_top),(WIDTH-44,panel_top+panel_h)],radius=10,fill=WHITE,outline=BORDER,width=2)
ry=panel_top+8
for i,(stat,label,sub,c) in enumerate(rows):
    if i>0: draw.line([(72,ry),(WIDTH-72,ry)],fill="#EDF2F7",width=2)
    draw.text((182,ry+rh//2),stat,fill=c,font=f_stat,anchor="mm")
    draw.line([(330,ry+22),(330,ry+rh-22)],fill=BORDER,width=2)
    draw.text((356,ry+40),label,fill=DARK,font=f_rowlabel,anchor="lm")
    draw.text((356,ry+72),sub,fill=MUTED,font=f_rowsub,anchor="lm")
    ry+=rh
y=panel_top+panel_h+16

# -- Kicker --
kick_h=88
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+28),"A company lobbied, the member voted, its employees gave, and the office moved closer.",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+58),"Public records show the sequence. They cannot show why, and this page claims no quid pro quo.",
          fill=WHITE,font=font("Arial Bold.ttf",17),anchor="mm")
y+=kick_h+14
draw.text((WIDTH//2,y),"Sources: FEC bulk files  ·  Senate lobbying disclosures  ·  P.L. 119-21  ·  House Clerk (Roll Call 190)",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-05-29-corning-manufacturing-credits-obbba/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/corning_convergence_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
