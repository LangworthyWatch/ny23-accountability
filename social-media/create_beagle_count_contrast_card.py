#!/usr/bin/env python3
"""Social card: beagle post count vs Essential Plan silence, July 1 2026.
30 beagle campaign posts (May 3 - Jun 29, manual count) vs 0 posts on 450,000 losing coverage.
DOCUMENTED PATTERN. Light house style, 1080x1080, no em dashes."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_huge=font("Impact.ttf",110)
f_stat=font("Impact.ttf",38); f_sub_b=font("Arial Bold.ttf",20); f_sub=font("Arial.ttf",17)
f_small=font("Arial.ttf",16); f_xs=font("Arial.ttf",14); f_xs_b=font("Arial Bold.ttf",14)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62

tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+24
draw.text((WIDTH//2,y),"Same Feed. Same Two Months.",fill=NAVY,font=f_topic,anchor="mm"); y+=40
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# two columns
col_w=(WIDTH-44*2-16)//2; col_h=430; lx=44; rx=lx+col_w+16
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#EBF8F0",outline="#9AE6B4",width=2)
draw.text((lx+col_w//2,y+24),"POSTS ABOUT BEAGLES",fill=GREEN,font=f_label_s,anchor="mm")
draw.text((lx+col_w//2,y+40),"May 3 to June 29",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+146),"30",fill=GREEN,font=f_huge,anchor="mm")
draw.text((lx+col_w//2,y+230),"posts, surveys, releases",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((lx+col_w//2,y+268),'"Huge rally. Save the Beagles."',fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+298),'"Marshall Farms is a torture chamber."',fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+328),'"Together, we saved the Beagles."',fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+372),"The Ridglan release he claimed was won by",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+392),"prosecutors, activists, and two nonprofits",fill=MUTED,font=f_xs,anchor="mm")

draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+24),"POSTS ABOUT YOUR HEALTH COVERAGE",fill=RED,font=f_label_s,anchor="mm")
draw.text((rx+col_w//2,y+40),"same window, same page",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+146),"0",fill=RED,font=f_huge,anchor="mm")
draw.text((rx+col_w//2,y+230),"mentions of the Essential Plan",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((rx+col_w//2,y+268),"450,000 New Yorkers lost it July 1",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+298),"under H.R. 1, the law he voted for",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+328),"(Roll Call 190, July 2025)",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+372),"About 26,000 of them are",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+392),"in Western New York",fill=MUTED,font=f_xs,anchor="mm")
y+=col_h+20

# sweep strip
strip_h=150
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+20),"JULY 1 SWEEP OF @REPLANGWORTHY  ·  232 POSTS, MID-APRIL TO JULY 1",fill=NAVY,font=f_label_s,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,c) in enumerate([
    ("232","total page posts reviewed",NAVY),
    ("0","Essential Plan or Medicaid",RED),
    ("0","in-person town halls (tele only)",RED),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+76),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+118),l1,fill=DARK,font=f_xs_b,anchor="mm")
y+=strip_h+20

# kicker
kick_h=112
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+40),"High-engagement, low-cost advocacy up front.",fill="#CBD5E0",font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+76),"The costly consequences of his own votes: unmentioned.",fill=WHITE,font=font("Arial Bold.ttf",18),anchor="mm")
y+=kick_h+20
draw.text((WIDTH//2,y),"Sources: facebook.com/RepLangworthy  ·  NY Dept. of Health  ·  Fiscal Policy Institute  ·  House Clerk",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-05-22-beagle-posts-credit-claiming-distraction/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/beagle_count_contrast_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
