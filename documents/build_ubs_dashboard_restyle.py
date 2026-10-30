from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-dashboard-ubs-palette.png'
W,H=1600,900
PAGE='#F7F7F4'; INK='#25333D'; MUTED='#66737B'; RULE='#C8CDCE'
CHART='#101417'; CHART_RULE='#293238'; CHART_TEXT='#BAC3C7'; WHITE='#F3F5F5'
UBS_RED='#D71935'; GREEN='#00B386'; RED='#F04452'; AMBER='#FFB000'; CYAN='#48B8D0'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

im=Image.new('RGB',(W,H),PAGE);d=ImageDraw.Draw(im);fonts={}
def f(size,b=False,m=False):
    k=(size,b,m)
    if k not in fonts:fonts[k]=ImageFont.truetype(MONO if m else (BOLD if b else FONT),size)
    return fonts[k]
def txt(x,y,s,size=16,color=INK,b=False,anchor=None,mono=False):d.text((x,y),s,font=f(size,b,mono),fill=color,anchor=anchor)
def line(x1,y1,x2,y2,color=RULE,width=1):d.line((x1,y1,x2,y2),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)
def dashed(x1,y1,x2,y2,color,width=1,dash=7,gap=5):
    if abs(y2-y1)<1:
        x=x1
        while x<x2:d.line((x,y1,min(x+dash,x2),y2),fill=color,width=width);x+=dash+gap
    else:
        y=y1
        while y<y2:d.line((x1,y,x2,min(y+dash,y2)),fill=color,width=width);y+=dash+gap

def logo_ubs():
    imlogo=Image.open(ASSETS/'ubs-logo.png').convert('RGBA');p=imlogo.load()
    for yy in range(imlogo.height):
        for xx in range(imlogo.width):
            r,g,b,a=p[xx,yy]
            if r>246 and g>246 and b>246:p[xx,yy]=(255,255,255,0)
    imlogo.thumbnail((188,66),Image.Resampling.LANCZOS);im.paste(imlogo,(48,24),imlogo)
def logo_skema():
    imlogo=Image.open(ASSETS/'skema-logo.png').convert('RGBA');imlogo.thumbnail((74,74),Image.Resampling.LANCZOS);im.paste(imlogo,(1475,20),imlogo)

# White ExCo/Treasury Committee page with terminal-style chart inserts.
logo_ubs();logo_skema()
txt(270,28,'UBS INVESTMENT BANK  |  2011',28,INK,True)
txt(270,68,'ETF DELTA ONE / ETF TRADING  ·  CONTROL FAILURE',16,UBS_RED,True)
txt(270,98,'Treasury Committee  /  incident overview',12,MUTED)
line(48,135,1552,135,RULE,2)
txt(52,151,'THREE-PANEL RISK OVERVIEW',10,MUTED,True)
txt(1548,151,'FACTS SOURCED  ·  CONCEPTS LABELLED',10,MUTED,True,anchor='ra')

xs=[52,560,1068]; py=177; pw=480; ph=526

def panel(x,num,title,accent,sub):
    rect((x,py,x+pw,py+ph),CHART,'#5F6970',1)
    rect((x,py,x+pw,py+4),accent)
    txt(x+18,py+17,f'{num}  {title}',15,WHITE,True)
    txt(x+18,py+45,sub,8,accent,True,mono=True)
    line(x+16,py+67,x+pw-16,py+67,CHART_RULE,1)

def draw_candles(x,y,w,h,ohlc,caption,caption_color):
    # Abstract candlesticks only: no numeric axis, no dates, no implied UBS observations.
    rect((x,y,x+w,y+h),CHART,'#253038',1)
    for i in range(1,5):line(x,y+i*h/5,x+w,y+i*h/5,CHART_RULE,1)
    for i in range(1,7):line(x+i*w/7,y,x+i*w/7,y+h,CHART_RULE,1)
    step=w/len(ohlc);bw=max(8,int(step*.43))
    for i,(low,high,op,cl) in enumerate(ohlc):
        cx=x+step*(i+.5)
        col=GREEN if cl>=op else RED
        ylow=y+h*(1-low);yhigh=y+h*(1-high);yop=y+h*(1-op);ycl=y+h*(1-cl)
        line(cx,yhigh,cx,ylow,col,2)
        top=min(yop,ycl);bottom=max(yop,ycl)
        rect((int(cx-bw/2),int(top),int(cx+bw/2),max(int(top)+3,int(bottom))),col)
    txt(x,y+h+12,'SEQUENCE  →',8,CHART_TEXT,False,mono=True)
    txt(x+w,y+h+12,caption,8,caption_color,True,anchor='ra',mono=True)

# 1. Normal activity: only symbolic candlesticks, explicitly not scaled or historical.
x=xs[0];panel(x,'01','NORMAL TRADING ACTIVITY',GREEN,'CONCEPTUAL REPRESENTATION  /  NOT TO SCALE')
normal=[(.44,.59,.49,.54),(.47,.63,.54,.60),(.49,.66,.60,.55),(.45,.62,.55,.58),(.48,.65,.58,.63),(.53,.69,.63,.59),(.50,.67,.59,.65),(.55,.71,.65,.68),(.56,.73,.68,.62),(.51,.68,.62,.66),(.55,.72,.66,.70),(.58,.74,.70,.67)]
draw_candles(x+35,py+105,pw-70,245,normal,'SYMBOLIC',GREEN)
line(x+18,py+401,x+pw-18,py+401,CHART_RULE,1)
txt(x+18,py+419,'Routine trading activity',11,WHITE,True)
txt(x+18,py+443,'Illustrative candle marks; no UBS daily P&L series.',9,CHART_TEXT)
txt(x+18,py+476,'No numerical scale or limit shown.',8,AMBER,True,mono=True)

# 2. Hidden exposure accumulation: conceptual sequence, no invented metrics or time series.
x=xs[1];panel(x,'02','HIDDEN EXPOSURE ACCUMULATION',AMBER,'ILLUSTRATIVE RISK ESCALATION FRAMEWORK')
hidden=[(.12,.26,.18,.22),(.16,.32,.22,.29),(.21,.38,.29,.24),(.25,.45,.24,.41),(.33,.55,.41,.49),(.40,.63,.49,.45),(.43,.70,.45,.64),(.54,.77,.64,.70),(.61,.87,.70,.66),(.65,.93,.66,.84),(.74,.98,.84,.91),(.79,1.0,.91,.96)]
draw_candles(x+35,py+105,pw-70,245,hidden,'CONCEPTUAL',AMBER)
# qualitative annotations only, no internal threshold or percentages
line(x+18,py+401,x+pw-18,py+401,CHART_RULE,1)
txt(x+18,py+419,'Hidden positions evade routine visibility',10,WHITE,True)
txt(x+18,py+443,'Control gaps delay reconciliation and escalation.',9,CHART_TEXT)
txt(x+18,py+476,'Conceptual sequence  ·  not to scale',8,AMBER,True,mono=True)

# 3. UBS 2011 facts only; no invented monthly exposure chart.
x=xs[2];panel(x,'03','UBS 2011 LOSS EVENT',UBS_RED,'CONFIRMED PUBLIC FACTS  /  NO MONTHLY SERIES')
# loss callout
rect((x+18,py+91,x+pw-18,py+191),'#1B2226','#39454C',1)
txt(x+34,py+107,'UNAUTHORIZED TRADING LOSS',9,CHART_TEXT,True,mono=True)
txt(x+34,py+132,'USD 2.3bn',27,UBS_RED,True)
txt(x+pw-34,py+157,'FINAL REPORTED LOSS',8,CHART_TEXT,False,anchor='ra',mono=True)
# fact table
facts=[('TRADER','Kweku Adoboli'),('ACTIVITY','Delta One / ETF trading'),('REVEALED','September 2011'),('CONTROL ISSUE','Hidden positions; control failures')]
for i,(label,value) in enumerate(facts):
    yy=py+219+i*57
    line(x+20,yy+42,x+pw-20,yy+42,CHART_RULE,1)
    txt(x+24,yy,label,8,CHART_TEXT,True,mono=True)
    txt(x+24,yy+18,value,12,WHITE,True)
# limited source note within panel
txt(x+22,py+472,'LOSS FIGURE IS PUBLISHED; EXPOSURE SERIES NOT SHOWN.',8,AMBER,True,mono=True)

# Two-sentence executive takeaway, per user wording.
line(52,733,1548,733,RULE,1)
txt(54,750,'EXECUTIVE SUMMARY',10,UBS_RED,True)
txt(54,773,'The 2011 UBS incident illustrates how operational control weaknesses can evolve into material financial losses.',13,INK,True)
txt(54,796,'For Treasury, the key concern is the translation of trading losses into funding and liquidity pressures.',13,INK,True)
txt(54,846,'Panels 1–2 are conceptual, not UBS historical observations. No unsupported exposure percentages or monthly P&L are displayed.',9,MUTED)
txt(54,868,'Sources: FINMA UBS investigation summary (2012); FCA Final Notice (2012); UBS 2011 disclosures.',9,MUTED)
txt(1546,868,'UBS  ×  SKEMA',9,INK,True,anchor='ra')

im.save(OUT)
print(OUT)
