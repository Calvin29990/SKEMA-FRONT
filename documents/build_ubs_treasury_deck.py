from pathlib import Path
import math
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT_PPTX=ROOT/'ubs-treasury-risk-presentation.pptx'
OUT_PDF=ROOT/'ubs-treasury-risk-presentation.pdf'
W,H=1280,720
BG='0A0E12'; PANEL='141A20'; PANEL2='10161B'; RED='E31B34'; WHITE='E9EEF2'; MUTED='93A0AB'; GRID='303A44'; GREEN='32C48D'; AMBER='F0A23A'; BLUE='4AA3DF'; SOFT='202932'; DEEP='0D1217'
UBS_LOGO=ASSETS/'ubs-logo-dark.png'; SKEMA_LOGO=ASSETS/'skema-logo.png'

class Scene:
    def __init__(self, number, source=''):
        self.number=number; self.source=source; self.ops=[]
    def rect(self,x,y,w,h,fill=PANEL,stroke=None,sw=1): self.ops.append(('rect',x,y,w,h,fill,stroke,sw))
    def line(self,x1,y1,x2,y2,color=GRID,sw=1,dash=False): self.ops.append(('line',x1,y1,x2,y2,color,sw,dash))
    def text(self,x,y,w,h,text,size=20,color=WHITE,bold=False,align='left',font='Aptos',leading=1.18): self.ops.append(('text',x,y,w,h,str(text),size,color,bold,align,font,leading,None))
    def circle(self,cx,cy,r,fill,stroke=None,sw=1): self.ops.append(('circle',cx,cy,r,fill,stroke,sw))
    def poly(self,pts,color=WHITE,sw=2): self.ops.append(('poly',pts,color,sw,None))
    def image(self,path,x,y,w,h): self.ops.append(('image',str(path),x,y,w,h))
    def base(self,title,kicker,source):
        self.rect(0,0,W,H,BG); self.rect(0,0,W,4,RED)
        self.image(UBS_LOGO,40,13,126,45)
        self.image(SKEMA_LOGO,1190,12,43,44)
        self.text(190,25,930,20,kicker.upper(),10,RED,True)
        self.text(44,76,1185,43,title,26,WHITE,True)
        self.line(44,131,1236,131,GRID,1)
        self.line(44,678,1236,678,GRID,1)
        self.text(44,686,1150,18,source,8,MUTED,False)
    def label(self,x,y,w,text,color=RED,size=10): self.text(x,y,w,17,text.upper(),size,color,True)
    def card(self,x,y,w,h,title='',accent=RED,fill=PANEL):
        self.rect(x,y,w,h,fill,GRID,1)
        if title:self.text(x+16,y+12,w-32,19,title.upper(),10,accent,True)

def add_scene(prs,sc):
    slide=prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid(); slide.background.fill.fore_color.rgb=RGBColor.from_string(BG)
    for op in sc.ops:
        t=op[0]
        if t=='rect':
            _,x,y,w,h,fill,stroke,sw=op
            sh=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x/96), Inches(y/96), Inches(w/96), Inches(h/96))
            if fill: sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(fill)
            else: sh.fill.background()
            sh.line.color.rgb=RGBColor.from_string(stroke or fill or BG); sh.line.width=Pt(sw)
        elif t=='line':
            _,x1,y1,x2,y2,color,sw,dash=op
            sh=slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1/96), Inches(y1/96), Inches(x2/96), Inches(y2/96))
            sh.line.color.rgb=RGBColor.from_string(color); sh.line.width=Pt(sw)
            if dash:
                try:
                    from pptx.enum.dml import MSO_LINE_DASH_STYLE
                    sh.line.dash_style=MSO_LINE_DASH_STYLE.DASH
                except Exception: pass
        elif t=='circle':
            _,cx,cy,r,fill,stroke,sw=op
            sh=slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches((cx-r)/96), Inches((cy-r)/96), Inches((2*r)/96), Inches((2*r)/96))
            sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(fill); sh.line.color.rgb=RGBColor.from_string(stroke or fill); sh.line.width=Pt(sw)
        elif t=='poly':
            _,pts,color,sw,_fill=op
            for a,b in zip(pts,pts[1:]):
                sh=slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(a[0]/96), Inches(a[1]/96), Inches(b[0]/96), Inches(b[1]/96)); sh.line.color.rgb=RGBColor.from_string(color); sh.line.width=Pt(sw)
        elif t=='text':
            _,x,y,w,h,txt,size,color,bold,align,font,leading,hyperlink=op
            tb=slide.shapes.add_textbox(Inches(x/96), Inches(y/96), Inches(w/96), Inches(h/96))
            tf=tb.text_frame; tf.clear(); tf.word_wrap=True; tf.margin_left=Pt(0); tf.margin_right=Pt(0); tf.margin_top=Pt(0); tf.margin_bottom=Pt(0); tf.vertical_anchor=MSO_ANCHOR.TOP
            for idx,line in enumerate(txt.split('\n')):
                p=tf.paragraphs[0] if idx==0 else tf.add_paragraph(); p.text=line
                p.alignment={'left':PP_ALIGN.LEFT,'center':PP_ALIGN.CENTER,'right':PP_ALIGN.RIGHT}[align]; p.space_after=Pt(0); p.space_before=Pt(0); p.line_spacing=leading
                for run in p.runs:
                    run.font.name=font; run.font.size=Pt(size*.75); run.font.bold=bold; run.font.color.rgb=RGBColor.from_string(color)
        elif t=='image':
            _,path,x,y,w,h=op
            im=Image.open(path); iw,ih=im.size; ar=iw/ih; boxar=w/h
            if ar>boxar: nw=w; nh=w/ar
            else: nh=h; nw=h*ar
            xx=x+(w-nw)/2; yy=y+(h-nh)/2
            slide.shapes.add_picture(path, Inches(xx/96), Inches(yy/96), Inches(nw/96), Inches(nh/96))
    return slide

FONT_REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FONT_BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DeckSans',FONT_REG)); pdfmetrics.registerFont(TTFont('DeckSansBold',FONT_BOLD))
def pdf_render(scenes):
    c=pdfcanvas.Canvas(str(OUT_PDF),pagesize=(W*.75,H*.75),pageCompression=1); c.setTitle('UBS 2011 Treasury Committee Briefing')
    for sc in scenes:
        for op in sc.ops:
            t=op[0]
            if t=='rect':
                _,x,y,w,h,fill,stroke,sw=op
                if fill:c.setFillColor(HexColor('#'+fill))
                if stroke:c.setStrokeColor(HexColor('#'+stroke)); c.setLineWidth(sw*.75)
                c.rect(x*.75,(H-y-h)*.75,w*.75,h*.75,fill=1 if fill else 0,stroke=1 if stroke else 0)
            elif t=='line':
                _,x1,y1,x2,y2,col,sw,dash=op; c.setStrokeColor(HexColor('#'+col)); c.setLineWidth(sw*.75); c.setDash(3,2) if dash else c.setDash(); c.line(x1*.75,(H-y1)*.75,x2*.75,(H-y2)*.75); c.setDash()
            elif t=='circle':
                _,cx,cy,r,fill,stroke,sw=op
                if fill:c.setFillColor(HexColor('#'+fill))
                if stroke:c.setStrokeColor(HexColor('#'+stroke)); c.setLineWidth(sw*.75)
                c.circle(cx*.75,(H-cy)*.75,r*.75,fill=1 if fill else 0,stroke=1 if stroke else 0)
            elif t=='poly':
                _,pts,col,sw,_=op; c.setStrokeColor(HexColor('#'+col)); c.setLineWidth(sw*.75); p=c.beginPath(); p.moveTo(pts[0][0]*.75,(H-pts[0][1])*.75)
                for x,y in pts[1:]:p.lineTo(x*.75,(H-y)*.75)
                c.drawPath(p,stroke=1,fill=0)
            elif t=='text':
                _,x,y,w,h,txt,size,col,bold,align,font,leading,url=op; fontname='DeckSansBold' if bold else 'DeckSans'; fontsize=size*.75; maxw=w*.75; out=[]
                for para in txt.split('\n'):
                    words=para.split(); cur=''
                    for word in words:
                        test=(cur+' '+word).strip()
                        if pdfmetrics.stringWidth(test,fontname,fontsize)>maxw and cur:out.append(cur); cur=word
                        else:cur=test
                    out.append(cur)
                lineh=fontsize*leading; start_y=(H-y)*.75-fontsize; c.setFillColor(HexColor('#'+col)); c.setFont(fontname,fontsize)
                for i,line in enumerate(out):
                    yy=start_y-i*lineh
                    if align=='center':c.drawCentredString((x+w/2)*.75,yy,line)
                    elif align=='right':c.drawRightString((x+w)*.75,yy,line)
                    else:c.drawString(x*.75,yy,line)
            elif t=='image':
                _,path,x,y,w,h=op; c.drawImage(path,x*.75,(H-y-h)*.75,w*.75,h*.75,preserveAspectRatio=True,anchor='c',mask='auto')
        c.showPage()
    c.save()

scenes=[]
def new(title,kicker,source):
    s=Scene(len(scenes)+1,source); s.base(title,kicker,source); scenes.append(s); return s

# 1 — Europe map and proportional losses
s=new('A map of four defining trading-loss events','EUROPE · LOSS COMPARISON','Sources: [1]–[4]. Bubble area uses approximate nominal USD equivalents at event dates; not inflation-adjusted.')
s.rect(46,148,845,496,DEEP,GRID,1)
# Schematic European coastline and country boundaries, deliberately non-geographic-detail
coast=[(186,227),(225,202),(272,198),(304,181),(339,187),(364,204),(398,196),(425,211),(456,202),(492,218),(525,211),(554,224),(587,218),(618,235),(648,229),(679,245),(709,252),(742,270),(768,291),(766,314),(741,323),(723,340),(733,361),(713,382),(695,391),(682,415),(654,420),(632,407),(613,387),(592,392),(572,382),(552,398),(531,390),(511,376),(490,384),(470,369),(450,366),(432,377),(408,369),(390,353),(370,349),(354,333),(332,327),(315,311),(294,308),(278,292),(260,285),(249,267),(263,253),(280,245),(293,229),(279,216),(299,203)]
s.poly(coast+[coast[0]],GRID,1)
# Scandinavia, UK, Ireland, Iceland, Italy and Iberia outlines
for pts in [ [(559,218),(570,189),(586,162),(606,149),(620,160),(618,185),(607,212),(601,241),(590,264),(577,251),(581,229),(570,218),(559,218)], [(377,244),(389,231),(401,234),(405,246),(400,258),(406,270),(399,283),(403,294),(395,304),(388,293),(384,281),(377,271),(382,258),(377,244)], [(361,257),(370,252),(374,259),(370,270),(363,271),(359,265),(361,257)], [(201,211),(215,205),(226,209),(222,218),(208,220),(201,211)], [(468,361),(482,367),(497,371),(508,383),(505,402),(499,425),(489,438),(481,419),(478,399),(469,386),(468,361)], [(414,370),(431,379),(447,389),(442,404),(424,407),(408,398),(398,386),(402,376),(414,370)] ]:s.poly(pts+[pts[0]],GRID,1)
# city names and event marks
s.circle(397,278,2,WHITE); s.text(368,306,70,16,'LONDON',8,MUTED,True)
s.circle(466,350,2,WHITE); s.text(420,389,55,16,'PARIS',8,MUTED,True)
s.circle(546,344,2,WHITE); s.text(517,421,65,16,'ZURICH',8,MUTED,True)
# bubble area proportional to approx USD loss values: Barings 1.3, UBS 2.3, CS 5.5, SocGen 7.2
bubbles=[(389,269,17,'5B6670','BARINGS'),(474,340,40,'5B6670','SOCIÉTÉ GÉNÉRALE'),(581,342,35,'5B6670','CREDIT SUISSE'),(619,391,23,RED,'UBS')]
for x,y,r,col,_ in bubbles:s.circle(x,y,r,col,WHITE if col!=RED else RED,1)
# location leaders and text labels
s.line(389,252,340,218,MUTED,1);s.text(95,174,260,38,'BARINGS · LONDON\nGBP 827m unreported by 27 Feb',10,WHITE,True,leading=1.25)
s.line(487,310,526,254,MUTED,1);s.text(506,177,300,42,'SOCIÉTÉ GÉNÉRALE · PARIS\nEUR 4.9bn net loss ≈ USD 7.2bn',10,WHITE,True,leading=1.25)
s.line(600,316,643,277,MUTED,1);s.text(647,244,228,39,'CREDIT SUISSE · ZURICH\nUSD 5.5bn Archegos loss',10,WHITE,True,leading=1.25)
s.line(628,411,671,456,MUTED,1);s.text(636,464,222,44,'UBS · ZURICH\nUSD 2.3bn final trading loss',10,RED,True,leading=1.25)
s.text(70,602,790,23,'Barings close-out loss: GBP 927m incl. closure costs. Archegos was counterparty default—not rogue trading.',8,MUTED,False)
# right takeaway panel
s.card(916,148,318,496,'EXECUTIVE TAKEAWAY',RED)
s.text(941,191,263,141,'UBS 2011 became one of the largest unauthorized trading losses in European banking.',23,WHITE,True,leading=1.17)
s.line(941,358,1208,358,GRID,1)
s.text(941,379,260,18,'APPROXIMATE USD LOSS SCALE · USD bn',9,MUTED,True)
for yy,lab,val,col in [(415,'SocGen','7.2','5B6670'),(451,'Credit Suisse','5.5','5B6670'),(487,'UBS','2.3',RED),(523,'Barings','1.3','5B6670')]:
    s.text(941,yy,110,18,lab,10,WHITE,True); s.rect(1050,yy+2,120*float(val)/7.2,11,col,None,0); s.text(1175,yy-1,40,18,'$'+val,9,WHITE,True,'right')
s.text(941,574,264,42,'Approximate historical FX conversions; nominal amounts only.',9,MUTED,False)
s.text(46,650,846,14,'Group CEO briefing · Supervisor Jamil Chaftar · Diouf · Minang · Métayer · Abou-Tayeh',8,MUTED)

# 2 — Bloomberg dashboard
s=new('Control dashboard: activity, hidden exposure and UBS facts','CONTROL DASHBOARD · SIGNALS, NOT FALSE PRECISION','UBS facts: [4] FINMA / [5] FCA. Panels 1–2 are illustrative normalized profiles, not historical UBS time series.')
cols=[46,449,852]; pw=382
for x,title,sub in [(cols[0],'01  CONTROLLED ACTIVITY','Illustrative normalized risk index'),(cols[1],'02  EXPOSURE BUILDS','Illustrative hidden exposure index'),(cols[2],'03  UBS · SOURCED FACTS','Peak futures notionals / final loss')]:
    s.card(x,151,pw,488,title,RED)
    s.text(x+18,179,pw-36,20,sub,9,MUTED,False)
# chart 1
x0,y0,w,h=cols[0]+45,230,300,255
for k in range(5):
    yy=y0+k*h/4;s.line(x0,yy,x0+w,yy,GRID,1,True);s.text(x0-31,yy-7,25,14,str(100-k*25),8,MUTED,False,'right')
s.line(x0,y0+h,x0+w,y0+h,GRID,1);s.line(x0,y0+h*.28,x0+w,y0+h*.28,AMBER,1,True)
data=[28,33,37,45,48,43,50,54,58,52,47,40]
pts=[]
for i,v in enumerate(data):pts.append((x0+i*w/(len(data)-1),y0+h*(1-v/100)))
s.poly(pts,BLUE,3);s.text(x0+5,y0+h*.28-19,150,15,'CONTROL LIMIT',8,AMBER,True)
s.circle(pts[-1][0],pts[-1][1],5,BLUE)
s.text(cols[0]+20,503,340,43,'Normal controls keep activity below limit; exceptions trigger review.',11,WHITE,True)
s.rect(cols[0]+20,565,96,24,'113126',GREEN,1);s.text(cols[0]+22,568,92,17,'GREEN · NORMAL',8,GREEN,True,'center')
s.rect(cols[0]+126,565,104,24,'302719',AMBER,1);s.text(cols[0]+128,568,100,17,'AMBER · WATCH',8,AMBER,True,'center')
s.rect(cols[0]+240,565,118,24,'32191E',RED,1);s.text(cols[0]+242,568,114,17,'RED · CRITICAL',8,RED,True,'center')
# chart 2
x1=cols[1]+45;y1=230
for k in range(5):
    yy=y1+k*h/4;s.line(x1,yy,x1+w,yy,GRID,1,True)
s.line(x1,y1+h,x1+w,y1+h,GRID,1);s.line(x1,y1+h*.25,x1+w,y1+h*.25,AMBER,1,True)
vis=[30,32,35,34,39,42,44,46,45,48,49,47];hid=[12,16,19,24,30,36,42,50,58,69,84,97]
for arr,col in [(vis,GREEN),(hid,RED)]:s.poly([(x1+i*w/(len(arr)-1),y1+h*(1-v/100)) for i,v in enumerate(arr)],col,3)
s.text(x1+4,y1+h*.25-19,180,15,'ESCALATION TRIGGER',8,AMBER,True)
s.text(cols[1]+20,503,342,43,'When hidden exposure diverges from reported activity, controls are already late.',11,WHITE,True)
s.line(cols[1]+24,567,cols[1]+57,567,GREEN,3);s.text(cols[1]+64,559,103,18,'Reported activity',9,MUTED)
s.line(cols[1]+186,567,cols[1]+219,567,RED,3);s.text(cols[1]+226,559,131,18,'Hidden exposure',9,MUTED)
# sourced actuals, no invented time series
s.text(cols[2]+22,219,340,17,'PEAK GROSS FUTURES POSITIONS',9,MUTED,True)
chartx=cols[2]+56; base=447; scale=12.7
for val,label,dt,col,cx in [(12.1,'LONG','8 AUG',BLUE,chartx+61),(8.5,'SHORT','15 SEP',AMBER,chartx+190)]:
    bh=val*scale;s.rect(cx,base-bh,74,bh,col,None,0);s.text(cx-5,base-bh-25,84,20,f'${val}bn',13,WHITE,True,'center');s.text(cx-2,base+11,78,17,label,9,WHITE,True,'center');s.text(cx-2,base+29,78,16,dt,8,MUTED,False,'center')
s.line(cols[2]+27,base,cols[2]+354,base,GRID,1)
s.rect(cols[2]+22,510,338,67,'32191E',RED,1);s.text(cols[2]+39,521,293,19,'FINAL TRADING LOSS · USD 2.3bn',12,RED,True);s.text(cols[2]+39,545,295,20,'Positions shown are gross notional, not P&L.',9,WHITE)
s.text(cols[2]+22,590,340,30,'No synthetic UBS time series shown.',9,MUTED,False)

# 3 — transmission diagram
s=new('How a trading position becomes a Treasury cash problem','CASH TRANSMISSION · BUY SIDE TO SELL SIDE','Simplified process based on [4]–[5]. Funding needs depend on settlement timing, margin and collateral—not P&L alone.')
# buy/sell side at top
s.card(55,157,320,86,'BUY SIDE',BLUE);s.text(74,190,280,35,'Asset managers · funds · institutional clients',11,WHITE,True)
s.card(424,157,394,86,'SELL SIDE · UBS INVESTMENT BANK',RED);s.text(444,190,348,35,'Client facilitation · ETF / Delta One desk',11,WHITE,True)
s.line(375,201,424,201,WHITE,2);s.poly([(424,201),(414,195),(414,207),(424,201)],WHITE,2)
# five operational stages
stage_x=[55,291,527,763,999]
labels=[('01','CLIENT ORDER','Buy / sell request'),('02','ETF / DELTA ONE','Position built'),('03','TRADING BOOK','Hedge / futures'),('04','SETTLEMENT','Margin / collateral'),('05','TREASURY','Cash by entity / currency')]
for idx,(x,(num,head,body)) in enumerate(zip(stage_x,labels)):
    color=RED if idx in (2,3) else BLUE if idx==0 else WHITE
    s.card(x,302,204,111,head,color)
    s.circle(x+24,338,13,RED if idx in (2,3) else SOFT,color,1)
    s.text(x+16,331,16,18,num,8,WHITE,True,'center')
    s.text(x+18,359,168,20,body,10,WHITE,True)
    if idx<4:
        ax=x+204;s.line(ax,356,ax+32,356,RED if idx in (1,2,3) else MUTED,2);s.poly([(ax+32,356),(ax+23,350),(ax+23,362),(ax+32,356)],RED if idx in (1,2,3) else MUTED,2)
# pressure chain row
s.text(57,443,1140,17,'FAILURE TRANSMISSION · ONE HIDDEN POSITION CAN CREATE MULTIPLE CASH CALLS',9,RED,True)
chain=[('HIDDEN POSITION','Exposure not visible'),('MARK-TO-MARKET','Loss recognized'),('MARGIN / SETTLEMENT','Cash due by cutoff'),('COLLATERAL LOCK-UP','Liquidity unavailable'),('FUNDING GAP','Treasury action required')]
for idx,(x,(head,body)) in enumerate(zip(stage_x,chain)):
    s.rect(x,476,204,103,'25171C' if idx>=1 else PANEL,RED if idx>=1 else GRID,1)
    s.text(x+14,491,176,19,head,9,RED if idx>=1 else WHITE,True)
    s.text(x+14,521,176,39,body,10,WHITE,False,leading=1.2)
    if idx<4:
        ax=x+204;s.line(ax,528,ax+32,528,RED,2);s.poly([(ax+32,528),(ax+23,522),(ax+23,534),(ax+32,528)],RED,2)
s.text(58,604,1150,35,'P&L is an accounting outcome; liquidity is cash available at the right entity, currency and time.',13,WHITE,True)

# 4 — Timeline
s=new('Discovery was sudden; the exposure had accumulated over years','EXECUTIVE TIMELINE · 2010–SEPTEMBER 2011','Sources: [4] FINMA; [5] FCA; [6] UBS 2011 disclosures. Notional positions are not losses.')
# timeline spine
s.line(94,343,1180,343,GRID,3)
items=[
 (108,'2010','CONCEALMENT','Fictitious / offsetting entries obscure positions; controls fail to reconcile.'),
 (365,'8 AUG 2011','LONG PEAK','Long futures peak at USD 12.1bn; gross notional, not P&L.'),
 (660,'15 SEP 2011','SHORT PEAK','Short futures reach USD 8.5bn; gross notional, not P&L.'),
 (928,'14 SEP 2011','DISCOVERY','Trading loss found; initial estimate about USD 2bn.'),
 (1155,'18 SEP 2011','RISK COVERED','Risk covered by 18 Sep; exposure no longer open.')]
for i,(x,date,head,body) in enumerate(items):
    col=RED if i>=3 else AMBER if i==2 else BLUE
    s.circle(x,343,9,col,WHITE,1)
    top=169 if i%2==0 else 380
    if i%2==0:
        s.line(x,352,x,top+84,GRID,1)
    else:s.line(x,352,x,top,GRID,1)
    width=215 if i<4 else 190; xx=max(52,min(1210-width,x-width/2))
    s.rect(xx,top,width,117,PANEL,GRID,1)
    s.text(xx+12,top+10,width-24,17,date,9,col,True)
    s.text(xx+12,top+33,width-24,20,head,11,WHITE,True)
    s.text(xx+12,top+59,width-24,52,body,9,MUTED,False,leading=1.18)
s.rect(56,565,1164,66,'10161B',GRID,1)
s.text(76,576,1100,18,'WHAT TREASURY KNEW AT DISCOVERY',9,RED,True)
s.text(76,599,1110,20,'Initial estimate: ~USD 2bn. UBS revised the final estimate to USD 2.3bn on 4 October.',11,WHITE,True)

# 5 — central liquidity graph
s=new('Liquidity headroom becomes the decisive control metric','CASH FORECAST · BASE, INCIDENT AND STRESS CASES','Illustrative scenario only—not UBS historical daily cash data. Assumptions and values are teaching inputs (USDm).')
# chart left
cx,cy,cw,ch=83,195,817,354
lo,hi=400,1150
for val in [400,500,600,700,800,900,1000,1100]:
    yy=cy+ch*(hi-val)/(hi-lo);s.line(cx,yy,cx+cw,yy,GRID,1,True);s.text(47,yy-7,31,14,str(val),8,MUTED,False,'right')
dates=['14 Sep','20 Sep','30 Sep','7 Oct','14 Oct','31 Oct','14 Nov','25 Nov','29 Nov','30 Nov','14 Dec']
series=[('Base case',[1000,990,985,990,985,987,984,1004,1104,1054,1024],BLUE),('UBS incident case',[1000,915,805,775,765,772,724,719,859,799,774],AMBER),('Stress case',[1000,915,805,775,765,772,724,719,759,499,474],RED)]
for i,d in enumerate(dates):
    xx=cx+i*cw/(len(dates)-1);s.line(xx,cy+ch,xx,cy+ch+5,GRID,1);s.text(xx-24,cy+ch+11,48,16,d,7,MUTED,False,'center')
buf_y=cy+ch*(hi-700)/(hi-lo);s.line(cx,buf_y,cx+cw,buf_y,WHITE,1,True);s.text(cx+4,buf_y-20,160,15,'MINIMUM BUFFER · 700',8,WHITE,True)
for name,vals,col in series:
    pts=[(cx+i*cw/(len(vals)-1),cy+ch*(hi-v)/(hi-lo)) for i,v in enumerate(vals)]
    s.poly(pts,col,3)
    for p in pts:s.circle(p[0],p[1],3,col)
# specific stress breach point
bx=cx+9*cw/10;by=cy+ch*(hi-499)/(hi-lo);s.circle(bx,by,7,RED,WHITE,1);s.line(bx,by-5,bx,by-62,RED,1)
s.rect(bx-81,by-97,166,35,'32191E',RED,1);s.text(bx-73,by-90,151,22,'30 NOV · $499m',10,RED,True,'center')
# legend and side metrics
for i,(name,_,col) in enumerate(series):
    xx=95+i*225;s.line(xx,602,xx+30,602,col,3);s.text(xx+38,594,178,18,name,9,WHITE,True)
s.card(934,157,300,482,'STRESS DECISION',RED)
s.text(956,195,251,20,'FIRST BUFFER BREACH',9,MUTED,True)
s.text(956,220,252,38,'30 Nov · USD 499m',21,RED,True)
s.text(956,276,252,19,'USD 201m below buffer',12,WHITE,True)
s.line(956,309,1210,309,GRID,1)
s.text(956,326,252,18,'MINIMUM STRESS CASH',9,MUTED,True)
s.text(956,350,252,32,'USD 474m',20,WHITE,True)
s.text(956,397,252,18,'PEAK FUNDING NEED',9,MUTED,True)
s.text(956,421,252,32,'USD 226m',20,RED,True)
s.rect(956,471,252,69,'10251D',GREEN,1);s.text(971,481,222,18,'USD 250m FACILITY · T+2',10,GREEN,True);s.text(971,505,222,25,'Draw ≥ USD 226m by 25 Nov\nfor 29 Nov cash.',9,WHITE,False,leading=1.2)
s.text(956,566,252,50,'Incident path stays above buffer; stress path breaches.',9,MUTED)

# 6 — Waterfall cash flow
s=new('Cash waterfall: distinguish loss from cash settlement','ILLUSTRATIVE CASH BRIDGE · USDm','Teaching scenario, not historical UBS cash flows. Net loss is not added to settlement or collateral payments.')
# waterfall axis chart
x0,ybase=80,553; chart_h=310; scale=chart_h/2200; bars=[
 ('Opening\ncash',1000,'total',BLUE),('Cash\ninflows',1105,'up',GREEN),('Operating /\ncontractual',-1101,'down',AMBER),('Incident\nsettlements',-270,'down',RED),('Net collateral\nuse',-10,'down',RED),('Operating\ncosts',-5,'down',AMBER),('Closing\ncash',719,'total',BLUE)]
# grid 0..2200
for val in [0,500,1000,1500,2000]:
    yy=ybase-val*scale;s.line(x0,yy,886,yy,GRID,1,True);s.text(43,yy-7,31,14,str(val),8,MUTED,False,'right')
s.line(x0,ybase,886,ybase,GRID,1)
start=0;bw=70;gap=41
for i,(name,amount,kind,col) in enumerate(bars):
    x=x0+24+i*(bw+gap)
    if kind=='total':
        end=amount; top=ybase-max(start,end)*scale; height=(end)*scale; bottom=ybase
    elif kind=='up':
        end=start+amount; top=ybase-end*scale; height=amount*scale; bottom=ybase-start*scale
    else:
        end=start+amount; top=ybase-start*scale; height=(-amount)*scale; bottom=ybase-end*scale
    s.rect(x,top,bw,max(2,height),col,None,0)
    if kind!='total':
        label=f'+{amount:,}' if amount>0 else f'{amount:,}'
        s.text(x-8,top-20,bw+16,17,label,9,WHITE,True,'center')
    elif i==0:s.text(x-5,top-21,bw+10,17,f'{amount:,}',10,WHITE,True,'center')
    s.text(x-14,ybase+11,bw+28,42,name,8,WHITE,True,'center',leading=1.12)
    if i<6:s.line(x+bw,ybase-end*scale,x+bw+gap,ybase-end*scale,GRID,1,True)
    if kind=='total':start=amount
    else:start=end
# buffer marker
buffer_y=ybase-700*scale;s.line(x0,buffer_y,886,buffer_y,WHITE,1,True);s.text(724,buffer_y-19,155,17,'MINIMUM BUFFER · 700',8,WHITE,True,'right')
# side panel
s.card(932,157,302,482,'CASH CONTROL',RED)
s.text(956,199,251,20,'OPENING CASH',9,MUTED,True);s.text(956,223,250,32,'1,000',21,WHITE,True)
s.line(956,270,1207,270,GRID,1)
s.text(956,290,251,19,'CLOSING CASH',9,MUTED,True);s.text(956,315,251,32,'719',21,BLUE,True)
s.text(956,362,251,19,'BUFFER HEADROOM',9,MUTED,True);s.text(956,386,251,32,'19',21,AMBER,True)
s.rect(956,444,250,74,'10251D',GREEN,1);s.text(971,454,220,18,'RECONCILIATION',9,GREEN,True);s.text(971,477,220,31,'1,000 + 1,105 − 1,101\n− 270 − 10 − 5 = 719',10,WHITE,True,leading=1.2)
s.text(956,544,250,54,'P&L describes value lost; settlement describes cash timing. Do not double-count.',9,MUTED,False,leading=1.2)
s.text(81,622,800,22,'Period: 14–30 September · Hypothetical movements sized for liquidity teaching.',9,MUTED)

# 7 — Risk 3x3 matrix
s=new('Residual risks require clear owners and trigger-based escalation','RISK MATRIX · 3 × 3','Qualitative scoring: likelihood × impact. Residual risk after immediate controls; judgemental, not a regulatory rating.')
# matrix axes, cells
mx,my,mw,mh=307,184,669,390; cw,ch=mw/3,mh/3
colors=[['17372D','253324','3B3020'],['253324','3B3020','3A2920'],['3B3020','3A2920','3D2025']]
for r in range(3):
 for c in range(3):
    s.rect(mx+c*cw,my+r*ch,cw-4,ch-4,colors[r][c],GRID,1)
# axis labels
s.text(44,327,214,20,'IMPACT →',10,WHITE,True,'center')
s.text(213,191,78,21,'HIGH',9,MUTED,True,'right');s.text(213,322,78,21,'MEDIUM',9,MUTED,True,'right');s.text(213,453,78,21,'LOW',9,MUTED,True,'right')
for c,lab in enumerate(['LOW','MEDIUM','HIGH']):s.text(mx+c*cw,584,cw-3,18,lab,9,MUTED,True,'center')
s.text(mx+204,610,260,19,'LIKELIHOOD →',10,WHITE,True,'center')
# risks by likelihood columns and impact rows; label pills
risk_items=[(2,0,'P1  Hidden positions'),(2,0,'P2  Settlement / collateral'),(2,1,'P3  Funding renewal'),(1,1,'M   Market close-out'),(1,1,'C   Counterparty timing'),(1,2,'R   Confidence outflows'),(1,1,'L   Legal / regulatory')]
cell_counts={}
for col,row,label in risk_items:
    key=(col,row); n=cell_counts.get(key,0);cell_counts[key]=n+1
    xx=mx+col*cw+10; yy=my+row*ch+18+n*34
    tag_color=RED if (col==2 and row==0) else AMBER if row<2 else GREEN
    s.rect(xx,yy,cw-24,27,'141A20',tag_color,1);s.text(xx+9,yy+5,cw-42,17,label,9,WHITE,True)
# drivers / actions side
s.card(1010,157,224,487,'RISK DRIVERS',RED)
watch=[('P1 · Position risk','Repeated concealment raises likelihood; large positions raise impact.'),('P2 · Cash calls','Settlement cutoffs and collateral lock-up can reduce cash quickly.'),('P3 · Funding','Renewal gaps are plausible; entity access drives impact.'),('M / C · Market','Close-out cost and counterparty timing drive cash volatility.'),('R / L · Franchise','Confidence outflows and regulatory action amplify the shock.')]
for i,(head,body) in enumerate(watch):
    yy=204+i*78;s.text(1030,yy,184,19,head,9,RED if i<3 else AMBER,True);s.text(1030,yy+23,184,38,body,9,WHITE,False,leading=1.18)
s.text(69,630,202,25,'High impact ↑',9,MUTED,False)

# 8 — CFO recommendations, exactly three pillars
s=new('Three CFO actions protect liquidity and restore control','DECISIONS · OWNERS · TIMING','Illustrative USD 250m T+2 facility addresses the modeled USD 226m stress need—not a historical UBS facility.')
cards=[
 ('01','SECURE LIQUIDITY',RED,[('OWNER','Group Treasurer'),('BENEFIT','USD 226m stress gap funded before breach'),('DEADLINE','Mandate now; draw by 25 Nov for 29 Nov cash'),('CONSTRAINT','Fees, haircuts, eligible collateral, legal entities'),('FALLBACK','Prefund early; activate pre-cleared backup sources')]),
 ('02','RESOLVE POSITIONS & CASH',AMBER,[('OWNER','IB COO + Market Risk + Treasury'),('BENEFIT','Verified settlements; release collateral only when confirmed'),('DEADLINE','First 48 hours; reconcile cash daily'),('CONSTRAINT','Close-out cost, market impact, settlement delays'),('FALLBACK','Temporary liquidity overlay; prioritize critical payments')]),
 ('03','PREVENT RECURRENCE',BLUE,[('OWNER','CRO + IB COO; Internal Audit validates'),('BENEFIT','Reduce hidden exposures; strengthen escalation'),('DEADLINE','Interim controls now; full plan within 90 days'),('CONSTRAINT','Systems, staffing, conduct, implementation cost'),('FALLBACK','Dual approval; independent confirmation; tighter limits')])]
for i,(num,title,col,rows) in enumerate(cards):
    x=46+i*401;s.rect(x,157,382,470,PANEL,GRID,1);s.rect(x,157,382,5,col,None,0)
    s.text(x+21,178,46,31,num,21,col,True);s.text(x+76,185,281,24,title,14,WHITE,True)
    for j,(lab,val) in enumerate(rows):
        yy=235+j*72;s.text(x+22,yy,82,16,lab,8,col,True);s.text(x+22,yy+20,337,41,val,10,WHITE,True,leading=1.16)
        if j<4:s.line(x+22,yy+62,x+359,yy+62,GRID,1)
s.rect(46,642,1188,24,'32191E',RED,1);s.text(60,646,1160,17,'TREASURY DECISION: authorize facility readiness now; fund only against verified cash forecasts and defined triggers.',9,WHITE,True)

# Exactly eight executive slides; editable PPTX and matching PDF.
assert len(scenes)==8, f'Expected exactly 8 slides, got {len(scenes)}'
prs=Presentation(); prs.slide_width=Inches(W/96); prs.slide_height=Inches(H/96)
for sc in scenes:add_scene(prs,sc)
prs.core_properties.title='UBS Treasury Committee Briefing — 2011 Trading Loss'; prs.core_properties.subject='Executive liquidity and control response'; prs.core_properties.author='SKEMA'
prs.save(OUT_PPTX); pdf_render(scenes)
print(f'Created {OUT_PPTX} and {OUT_PDF} with {len(scenes)} slides.')
