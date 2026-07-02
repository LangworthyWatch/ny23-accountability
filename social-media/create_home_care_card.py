#!/usr/bin/env python3
"""Social card: HCA-NYS meeting post, July 2 2026. MISSING CONTEXT.
Fairness-first: credit column + omissions column + abuse-enforcement strip. No em dashes."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_big=font("Impact.ttf",64)
f_stat=font("Impact.ttf",34); f_sub_b=font("Arial Bold.ttf",19); f_sub=font("Arial.ttf",17)
f_small=font("Arial.ttf",16); f_xs=font("Arial.ttf",14); f_xs_b=font("Arial Bold.ttf",14)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62

tag="MISSING CONTEXT"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+22
draw.text((WIDTH//2,y),"Home Care: The Half He Tells",fill=NAVY,font=f_topic,anchor="mm"); y+=38
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

claim_h=112
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+18),"WHAT HE POSTED  ·  JULY 2, MEETING THE HOME CARE ASSOCIATION OF NYS",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+50),'"We share a common goal: protect patients while being strong stewards of',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+78),'taxpayer dollars. By working collaboratively to root out fraud, waste, and abuse..."',fill=DARK,font=f_sub,anchor="lm")
y+=claim_h+16

col_w=(WIDTH-44*2-16)//2; col_h=330; lx=44; rx=lx+col_w+16
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#EBF8F0",outline="#9AE6B4",width=2)
draw.text((lx+col_w//2,y+22),"CREDIT WHERE DUE",fill=GREEN,font=f_label_s,anchor="mm")
draw.text((lx+col_w//2,y+38),"and we say so",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+100),"2024",fill=GREEN,font=f_big,anchor="mm")
draw.text((lx+col_w//2,y+158),"he signed the bipartisan NY letter",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((lx+col_w//2,y+188),"against Medicare home care cuts",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+216),"and the association praised it",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+266),"HCA has taken no public position on",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+284),"H.R. 1; a meeting is not an endorsement",fill=MUTED,font=f_xs,anchor="mm")

draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+22),"WHAT THE POST OMITS",fill=RED,font=f_label_s,anchor="mm")
draw.text((rx+col_w//2,y+38),"the association's own numbers",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+100),"60%",fill=RED,font=f_big,anchor="mm")
draw.text((rx+col_w//2,y+158),"of NY home care agencies losing money",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((rx+col_w//2,y+188),"20% of agencies closed in five years",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+216),"200,000+ Medicaid patients unserved",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+262),"His vote (Roll Call 190) cut Medicaid ~$900B (w/ SNAP);",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+280),"1199SEIU, the healthcare workers' union: NY Republicans",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+298),"\"shamefully reneged\" on protecting Medicaid",fill=MUTED,font=f_xs,anchor="mm")
y+=col_h+16

strip_h=128
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+20),"BEHIND \"ROOT OUT ABUSE\"",fill=NAVY,font=f_label,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,l2,c) in enumerate([
    ("10 yrs","nursing home staffing rule","blocked by his own vote",RED),
    ("Rescinded","the rule, entirely","HHS, December 2025",RED),
    ("23,000","DOJ cases dropped in 2025, incl. a","nursing home abuse probe (ProPublica)",RED),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+58),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+90),l1,fill=DARK,font=f_xs_b,anchor="mm")
    draw.text((cx,y+108),l2,fill=MUTED,font=f_xs,anchor="mm")
y+=strip_h+16

kick_h=96
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+32),"The Medicare common ground is real. We say so.",fill="#CBD5E0",font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+64),"The Medicaid cut, the erosion, and the dropped abuse cases go unmentioned.",fill=WHITE,font=font("Arial Bold.ttf",17),anchor="mm")
y+=kick_h+16
draw.text((WIDTH//2,y),"Sources: House Clerk  ·  Torres release  ·  Spectrum/HCA-NYS  ·  1199SEIU  ·  ProPublica  ·  CBO",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-02-home-care-association-meeting-stewardship/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/home_care_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
