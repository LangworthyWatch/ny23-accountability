#!/usr/bin/env python3
"""Educational card: what "age verification" actually collects (data extraction),
why the open internet + data privacy matter, anchored to the NY-23 record.
Companion to 2026-06-30-kids-act-online-safety. Light house style, 1080x1080."""

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
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_num=font("Impact.ttf",54)
f_sub_b=font("Arial Bold.ttf",20); f_sub=font("Arial.ttf",18); f_small=font("Arial.ttf",17)
f_xs=font("Arial.ttf",15); f_xs_b=font("Arial Bold.ttf",15); f_src=font("Arial.ttf",15)
f_footer=font("Arial Bold.ttf",20); f_arrow=font("Arial Bold.ttf",18)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)

# Header
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=66

# Badge (explainer, not a verdict)
tag="WHY IT MATTERS"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26

# Title
draw.text((WIDTH//2,y),"What 'Age Verification' Actually Collects",fill=NAVY,font=f_topic,anchor="mm"); y+=42
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=18

# Intro framing box
intro_h=86
draw.rounded_rectangle([(44,y),(WIDTH-44,y+intro_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((WIDTH//2,y+30),"Checking your age online is not a yes-or-no gate.",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((WIDTH//2,y+58),"To prove it, a private company has to collect something from you.",fill=DARK,font=f_sub,anchor="mm")
y+=intro_h+18

# Three-step "data extraction" flow
draw.text((WIDTH//2,y),"HOW DATA EXTRACTION WORKS",fill=NAVY,font=f_label,anchor="mm"); y+=30
col_w=(WIDTH-44*2-2*14)//3; step_h=212
steps=[
    ("1","You hand it over","A government ID upload","or a biometric face scan",NAVY),
    ("2","A vendor holds it","Stored under company terms,","not strong public-law rules",ORANGE),
    ("3","It can travel","Breached, retained, or","reused beyond the check",RED),
]
for i,(n,t1,s1,s2,c) in enumerate(steps):
    x=44+i*(col_w+14)
    draw.rounded_rectangle([(x,y),(x+col_w,y+step_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
    draw.text((x+col_w//2,y+44),n,fill=c,font=f_num,anchor="mm")
    draw.line([(x+30,y+84),(x+col_w-30,y+84)],fill=BORDER,width=1)
    draw.text((x+col_w//2,y+114),t1,fill=DARK,font=f_sub_b,anchor="mm")
    draw.text((x+col_w//2,y+150),s1,fill=MUTED,font=f_xs,anchor="mm")
    draw.text((x+col_w//2,y+172),s2,fill=MUTED,font=f_xs,anchor="mm")
# arrows between
for i in range(2):
    ax=44+(i+1)*col_w+i*14+7
    draw.text((ax,y+44),">",fill=LIGHTGRAY,font=f_num,anchor="mm")
y+=step_h+18

# Open internet stake (navy)
oi_h=110
draw.rounded_rectangle([(44,y),(WIDTH-44,y+oi_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+24),"WHAT'S AT STAKE: THE OPEN INTERNET",fill=GOLD,font=f_label_s,anchor="mm")
draw.text((WIDTH//2,y+56),"Using the internet without first proving who you are protects",fill="#CBD5E0",font=f_small,anchor="mm")
draw.text((WIDTH//2,y+82),"survivors, whistleblowers, patients, and everyday privacy.",fill=WHITE,font=f_sub_b,anchor="mm")
y+=oi_h+18

# NY-23 record (local hook)
rec_h=134
draw.rounded_rectangle([(44,y),(WIDTH-44,y+rec_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((76,y+22),"THE NY-23 RECORD  ·  Rep. Nick Langworthy",fill=RED,font=f_label_s,anchor="lm")
draw.text((76,y+52),"Voted YEA on the KIDS Act, which pushes age checks (Roll Call 228)",fill=DARK,font=f_small,anchor="lm")
draw.text((76,y+84),"Cosponsors the SECURE Data Act: no right to sue over your data,",fill=DARK,font=f_small,anchor="lm")
draw.text((76,y+108),"and it preempts stronger state privacy law",fill=DARK,font=f_small,anchor="lm")
y+=rec_h

# Kicker (navy)
kick_h=92
draw.rounded_rectangle([(44,y+8),(WIDTH-44,y+8+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+8+34),"Privacy is not about having something to hide.",fill=LIGHTGRAY,font=f_small,anchor="mm")
draw.text((WIDTH//2,y+8+64),"It is about who controls your data once you hand it over.",fill=WHITE,font=f_sub_b,anchor="mm")
y+=8+kick_h+14

# Sources + URL
draw.text((WIDTH//2,y),"Sources: H.R. 8413 text (GovInfo)  ·  EFF  ·  Cato Institute  ·  House Clerk (Roll Call 228)",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-06-30-kids-act-online-safety/",
          fill=NAVY,font=f_src,anchor="mm")

# Footer
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/data_extraction_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
