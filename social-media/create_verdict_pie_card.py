#!/usr/bin/env python3
"""Social card: pie chart of all 128 fact-check verdicts (normalized categories).
Rendered at 3x and downscaled for smooth pie edges."""

from PIL import Image, ImageDraw, ImageFont

SS = 3                      # supersample factor
W, H = 1080*SS, 1080*SS
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; MUTED="#718096"; WHITE="#FFFFFF"; BORDER="#E2E8F0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s*SS)
    except Exception: return ImageFont.load_default()

f_brand=font("Arial Bold.ttf",22); f_title=font("Arial Bold.ttf",34); f_sub=font("Arial.ttf",17)
f_big=font("Impact.ttf",120); f_biglbl=font("Arial Bold.ttf",18)
f_leg=font("Arial Bold.ttf",19); f_legn=font("Arial.ttf",17); f_foot=font("Arial Bold.ttf",20)
f_note=font("Arial.ttf",16)

img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

# brand bar
d.rectangle([(0,0),(W,48*SS)],fill=NAVY)
d.text((W//2,24*SS),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")

# title
d.text((W//2,86*SS),"128 Fact-Checks. Here's the Breakdown.",fill=NAVY,font=f_title,anchor="mm")
d.text((W//2,118*SS),"Every published check of Rep. Langworthy's public claims, by finding.",
       fill=MUTED,font=f_sub,anchor="mm")
d.line([(60*SS,140*SS),(W-60*SS,140*SS)],fill=BORDER,width=2*SS)

slices=[
 ("Missing context",36,"#2C5282"),
 ("Misleading",31,"#C05621"),
 ("Documented pattern",24,"#975A16"),
 ("Contradiction",14,"#9B2C2C"),
 ("False / false attribution",12,"#E53E3E"),
 ("Deflection / non-responsive / mixed",7,"#718096"),
 ("Mostly true (held up)",4,"#2F855A"),
]
total=sum(n for _,n,_ in slices)

# pie
cx,cy,r = 330*SS, 560*SS, 235*SS
box=[cx-r,cy-r,cx+r,cy+r]
ang=-90.0
for label,n,color in slices:
    sweep=n/total*360.0
    d.pieslice(box,ang,ang+sweep,fill=color)
    ang+=sweep
# donut hole for a cleaner look + center stat
hr=int(r*0.52)
d.ellipse([cx-hr,cy-hr,cx+hr,cy+hr],fill=BG)
d.text((cx,cy-20*SS),"128",fill=NAVY,font=f_big,anchor="mm")
d.text((cx,cy+52*SS),"fact-checks",fill=MUTED,font=f_biglbl,anchor="mm")

# legend (right column)
lx=650*SS; ly=210*SS; row=54*SS; sw=26*SS
for label,n,color in slices:
    d.rounded_rectangle([lx,ly,lx+sw,ly+sw],radius=4*SS,fill=color)
    pct=n/total*100
    d.text((lx+sw+16*SS, ly+2*SS), label, fill=DARK, font=f_leg, anchor="lm")
    d.text((lx+sw+16*SS, ly+24*SS), f"{n} entries  ·  {pct:.0f}%", fill=MUTED, font=f_legn, anchor="lm")
    ly+=row

# bottom callout bar
by=H-190*SS
d.rounded_rectangle([(44*SS,by),(W-44*SS,by+92*SS)],radius=8*SS,fill=NAVY)
d.text((W//2,by+30*SS),"Across 128 checks, his claims held up as accurate 4 times.",
       fill="#A0AEC0",font=font("Arial.ttf",18),anchor="mm")
d.text((W//2,by+62*SS),"The other 97% were misleading, missing key context, or contradicted by his own record.",
       fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")

d.text((W//2,H-72*SS),"Verdicts normalized from the project's standard labels. Full record and sources below.",
       fill=MUTED,font=f_note,anchor="mm")

# footer
d.rectangle([(0,H-50*SS),(W,H)],fill=NAVY)
d.text((W//2,H-25*SS),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_foot,anchor="mm")

img=img.resize((1080,1080),Image.LANCZOS)
out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/verdict_pie_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
