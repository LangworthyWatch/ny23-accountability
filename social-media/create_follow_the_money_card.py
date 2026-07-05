#!/usr/bin/env python3
"""Social card: Follow the Money — donor -> aligned action (documented sequences).
DOCUMENTED PATTERN. Rendered at 2x for smooth text."""

from PIL import Image, ImageDraw, ImageFont

SS=2
W,H=1080*SS,1080*SS
FONT_DIR="/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; RED="#9B2C2C"; GOLD="#D69E2E"
MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; CARD="#FFFFFF"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s*SS)
    except Exception: return ImageFont.load_default()

f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_title=font("Arial Bold.ttf",34)
f_sub=font("Arial.ttf",17); f_amt=font("Impact.ttf",46); f_donor=font("Arial Bold.ttf",16)
f_then=font("Arial Bold.ttf",15); f_act=font("Arial.ttf",16); f_src=font("Arial.ttf",15); f_foot=font("Arial Bold.ttf",20)

img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
d.rectangle([(0,0),(W,48*SS)],fill=NAVY)
d.text((W//2,24*SS),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64*SS

tag="DOCUMENTED PATTERN"; tb=d.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28*SS,tb[3]-tb[1]+12*SS
d.rounded_rectangle([((W-tw)//2,y),((W+tw)//2,y+th)],radius=5*SS,fill="#744210",outline=GOLD,width=2*SS)
d.text((W//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+24*SS

d.text((W//2,y),"Follow the Money",fill=NAVY,font=f_title,anchor="mm"); y+=32*SS
d.text((W//2,y),"What his donors gave, and what his votes did next.",fill=MUTED,font=f_sub,anchor="mm"); y+=16*SS
d.line([(60*SS,y),(W-60*SS,y)],fill=BORDER,width=2*SS); y+=14*SS

rows=[
 ("$68,700",["Nursing-home operator","Benjamin Landa"],
   ["Voted to block the first federal nursing-","home staffing rule until 2034. 50+ of his","106 facilities fall below that standard."]),
 ("$65,775",["62 Corning employees","(incl. the CEO and CFO)"],
   ["The law he voted for preserved the tax","credits that benefit Corning's plants;","much of the money came after the vote."]),
 ("$10,100",["The Seneca Nation"],
   ["Introduced a bill removing New York's civil","jurisdiction over Seneca lands, affecting","their gaming and business operations."]),
 ("$16,500",["Homebuilders' PAC","(NAHB BUILD-PAC)"],
   ["Named him \"Defender of Housing\"; he backs","their push to preempt local energy rules."]),
]

rh=150*SS; gap=12*SS; lx=44*SS; rw=W-44*SS
for amt,donor,act in rows:
    d.rounded_rectangle([(lx,y),(rw,y+rh)],radius=8*SS,fill=CARD,outline=BORDER,width=2*SS)
    # left: amount + donor
    d.text((lx+34*SS,y+34*SS),amt,fill=NAVY,font=f_amt,anchor="lm")
    dy=y+72*SS
    for line in donor:
        d.text((lx+34*SS,dy),line,fill=DARK,font=f_donor,anchor="lm"); dy+=24*SS
    # divider
    dvx=lx+350*SS
    d.line([(dvx,y+22*SS),(dvx,y+rh-22*SS)],fill=BORDER,width=2*SS)
    # right: THEN + action
    d.text((dvx+28*SS,y+30*SS),"→ THEN",fill=RED,font=f_then,anchor="lm")
    ay=y+58*SS
    for line in act:
        d.text((dvx+28*SS,ay),line,fill=DARK,font=f_act,anchor="lm"); ay+=27*SS
    y+=rh+gap

y+=6*SS
d.text((W//2,y),"Documented sequences in the public record. Not proof of a deal.",
       fill=MUTED,font=font("Arial.ttf",16),anchor="mm"); y+=26*SS
d.text((W//2,y),"Sources: FEC filings + the House record.  ·  langworthywatch.org",
       fill=NAVY,font=f_src,anchor="mm")

d.rectangle([(0,H-50*SS),(W,H)],fill=NAVY)
d.text((W//2,H-25*SS),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_foot,anchor="mm")

img=img.resize((1080,1080),Image.LANCZOS)
out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/follow_the_money_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
