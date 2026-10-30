from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-event-context-map.png'
W,H=1600,900
PAPER='#F7F7F4'; INK='#24323B'; MUTED='#68757C'; RULE='#C8CDCE'
PANEL='#101519'; PANEL_RULE='#303A40'
MAP_WATER='#F9FAF7'; MAP_LAND='#ECEFE8'; MAP_FOCUS='#E3E9E2'; MAP_COAST='#BEC8C0'; MAP_GRID='#E8ECE7'
UBS_RED='#D71935'; CS_BLUE='#0A4B70'; JPM_BLUE='#15558A'; SG_RED='#C8002B'; BARINGS_GOLD='#74602C'; WHITE='#FFFFFF'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts={}
def f(size,b=False,m=False,serif=False):
    key=(size,b,m,serif)
    if key not in fonts:fonts[key]=ImageFont.truetype(SERIF if serif else (MONO if m else (BOLD if b else FONT)),size)
    return fonts[key]
def text(x,y,s,size=16,color=INK,b=False,anchor=None,mono=False,serif=False):
    d.text((x,y),s,font=f(size,b,mono,serif),fill=color,anchor=anchor)
def line(x1,y1,x2,y2,color=RULE,width=1):d.line((x1,y1,x2,y2),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)
def tint(hexcolor,amount=0.90):
    h=hexcolor.lstrip('#');rgb=tuple(int(h[i:i+2],16) for i in (0,2,4))
    return tuple(round(c*(1-amount)+255*amount) for c in rgb)
def crop_logo(path,remove_white=False):
    im=(path.copy() if isinstance(path,Image.Image) else Image.open(path)).convert('RGBA');p=im.load()
    if remove_white:
        for yy in range(im.height):
            for xx in range(im.width):
                r,g,b,a=p[xx,yy]
                if r>245 and g>245 and b>245:p[xx,yy]=(r,g,b,0)
    alpha=im.getchannel('A')
    bbox=alpha.point(lambda a:255 if a>12 else 0).getbbox()
    if bbox:im=im.crop(bbox)
    return im
def fit(im,maxw,maxh):
    ratio=min(maxw/im.width,maxh/im.height)
    return im.resize((max(1,round(im.width*ratio)),max(1,round(im.height*ratio))),Image.Resampling.LANCZOS)

im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im)
# UBS header identity (reuse existing logo asset; remove white only in memory).
ubs_header=crop_logo(ASSETS/'ubs-logo.png',True);ubs_header.thumbnail((188,66),Image.Resampling.LANCZOS);im.paste(ubs_header,(48,23),ubs_header)
sk=Image.open(ASSETS/'skema-logo.png').convert('RGBA');sk.thumbnail((74,74),Image.Resampling.LANCZOS);im.paste(sk,(1475,18),sk)
text(270,27,'WHY THE UBS EVENT MATTERS',28,INK,True)
text(270,68,'Contextualising the 2011 UBS trading loss within European banking incidents',14,UBS_RED,True)
text(270,98,'Treasury risk context  /  selected loss events',11,MUTED)
line(48,133,1552,133,RULE,2)

# Source logos. Barings Bank had a heraldic crest rather than a modern corporate logo;
# use an explicit historical wordmark label instead of the unrelated current Barings LLC mark.
logos={
 'CS':crop_logo(ASSETS/'credit-suisse-logo.png'),
 'JPM':crop_logo(ASSETS/'jpmorgan-chase-logo.png'),
 'SG':crop_logo(ASSETS/'societe-generale-logo.png'),
 'UBS':crop_logo(ASSETS/'ubs-logo.png',True),
}
barings=Image.new('RGBA',(460,100),(255,255,255,0));bd=ImageDraw.Draw(barings)
bd.text((8,3),'BARINGS',font=f(68,True,serif=True),fill=BARINGS_GOLD)
logos['BARINGS']=crop_logo(barings)

# Map panel: retain the Western-Europe outline and institutional layout, but zoom to the three hubs.
mx,my,mw,mh=50,155,940,540
rect((mx,my,mx+mw,my+mh),MAP_WATER,'#D2DAD4',1)
map_base=im.copy()
lon0,lon1=-8.0,15.5;lat0,lat1=43.0,55.5
def xy(lon,lat):return (mx+(lon-lon0)/(lon1-lon0)*mw,my+(lat1-lat)/(lat1-lat0)*mh)
# low-contrast gridlines, as a terminal-map cue but softer than the dark version
for lon in [-5,0,5,10,15]:line(xy(lon,50)[0],my,xy(lon,50)[0],my+mh,MAP_GRID,1)
for lat in [45,50,55]:line(mx,xy(0,lat)[1],mx+mw,xy(0,lat)[1],MAP_GRID,1)
with open(ASSETS/'natural-earth-50m-western-europe-context.geojson',encoding='utf-8') as fp:geo=json.load(fp)
geometries={feature['properties']['name']:feature['geometry'] for feature in geo['features']}
def draw_country(name,fill,stroke=MAP_COAST,width=1):
    geom=geometries[name];polys=geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
    for polygon in polys:
        ring=polygon[0];xs=[q[0] for q in ring];ys=[q[1] for q in ring]
        if max(xs)<lon0 or min(xs)>lon1 or max(ys)<lat0 or min(ys)>lat1:continue
        pts=[xy(lon,lat) for lon,lat in ring]
        d.polygon(pts,fill=fill)
        d.line(pts+[pts[0]],fill=stroke,width=width,joint='curve')
for name in ['Portugal','Spain','Ireland','Belgium','Netherlands','Germany','Denmark','Czechia','Slovakia','Slovenia','Poland','Hungary','Italy','Austria','Luxembourg']:
    if name in geometries:draw_country(name,MAP_LAND,MAP_COAST,1)
for name in ['United Kingdom','France','Switzerland']:
    draw_country(name,MAP_FOCUS,'#B5C2B8',1)

# Event values (USD equivalents used solely to size circles). Circle area ∝ loss.
loss_usd={'CS':5.5,'JPM':6.2,'SG':4.9*1.4663,'UBS':2.3,'BARINGS':1.4}
rmax=64.0
radii={k:rmax*(v/max(loss_usd.values()))**0.5 for k,v in loss_usd.items()}
city={'London':xy(-0.12,51.51),'Paris':xy(2.35,48.86),'Zurich':xy(8.54,47.38)}
lx,ly=city['London'];px,py=city['Paris'];zx,zy=city['Zurich']
events={
 'JPM':(lx+18,ly-24,radii['JPM'],JPM_BLUE,'#E7EFF7','2012'),
 'BARINGS':(lx-72,ly+43,radii['BARINGS'],BARINGS_GOLD,'#F1EEE4','1995'),
 'SG':(px,py,radii['SG'],SG_RED,'#F8E8EA','2008'),
 'CS':(zx+49,zy-15,radii['CS'],CS_BLUE,'#E7EFF2','2021'),
 'UBS':(zx-49,zy+25,radii['UBS'],UBS_RED,'#F8E6E9','2011'),
}
# Thin leaders from exact city locations to offset markers in the crowded London / Zurich clusters.
for key,hub in [('JPM',city['London']),('BARINGS',city['London']),('SG',city['Paris']),('CS',city['Zurich']),('UBS',city['Zurich'])]:
    cx,cy,r,brand,fill,year=events[key];hx,hy=hub
    if abs(cx-hx)+abs(cy-hy)>1:line(hx,hy,cx,cy,'#738189',1)
# Proportional circles with bank logos and years.
for key in ['BARINGS','JPM','SG','CS','UBS']:
    cx,cy,r,brand,fill,year=events[key]
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=fill,outline=brand,width=3 if key=='UBS' else 2)
    max_logo_w=max(34,2*r-16);max_logo_h=max(9,int(r*.54))
    mark=fit(logos[key],max_logo_w,max_logo_h)
    im.paste(mark,(round(cx-mark.width/2),round(cy-mark.height/2-3)),mark)
    d=ImageDraw.Draw(im)
    text(cx,cy+r*.47,year,8,brand,True,anchor='mm',mono=True)
# City labels / hub dots.
for name,(hx,hy) in city.items():
    d.ellipse((hx-3.5,hy-3.5,hx+3.5,hy+3.5),fill=INK,outline=WHITE,width=1)
text(lx+8,ly+8,'LONDON',8,INK,True)
text(px+68,py+3,'PARIS',8,INK,True)
text(zx+10,zy+64,'ZURICH',8,INK,True)
# Number callouts on the map use each institution's brand color.
text(events['JPM'][0]-80,events['JPM'][1]-radii['JPM']-17,'USD 6.2bn',10,JPM_BLUE,True)
text(events['BARINGS'][0]-57,events['BARINGS'][1]+radii['BARINGS']+9,'~USD 1.4bn',9,BARINGS_GOLD,True)
text(events['SG'][0]-45,events['SG'][1]+radii['SG']+13,'EUR 4.9bn',10,SG_RED,True)
text(events['CS'][0]+radii['CS']+7,events['CS'][1]-9,'USD 5.5bn',10,CS_BLUE,True)
text(events['UBS'][0]-48,events['UBS'][1]+radii['UBS']+10,'USD 2.3bn',10,UBS_RED,True)
# Subtle incident tags, matching the example map's local labels.
text(lx-167,ly+74,'BARINGS · LEESON¹',7,BARINGS_GOLD,True)
text(events['JPM'][0]-70,events['JPM'][1]-radii['JPM']-32,'JPMORGAN · LONDON WHALE',7,JPM_BLUE,True)
text(events['SG'][0]-70,events['SG'][1]-radii['SG']-18,'SOCIÉTÉ GÉNÉRALE · KERVIEL',7,SG_RED,True)
text(events['CS'][0]-64,events['CS'][1]-radii['CS']-18,'CREDIT SUISSE · ARCHEGOS',7,CS_BLUE,True)
text(events['UBS'][0]-38,events['UBS'][1]-radii['UBS']-17,'UBS · 2011',7,UBS_RED,True)
# Map header strip and scale description.
rect((mx+1,my+1,mx+mw-1,my+35),MAP_WATER)
text(mx+18,my+14,'EUROPEAN FINANCIAL HUBS',9,MUTED,True)
text(mx+mw-18,my+14,'CIRCLE AREA ∝ USD-EQUIVALENT LOSS',8,MUTED,True,anchor='ra',mono=True)
# Clip geographic data and markers to the map frame.
clip=Image.new('L',(W,H),0);ImageDraw.Draw(clip).rectangle((mx,my,mx+mw,my+mh),fill=255)
im=Image.composite(im,map_base,clip);d=ImageDraw.Draw(im)
rect((mx,my,mx+mw,my+mh),None,'#D2DAD4',1)

# Dark right-side data panel preserves the Bloomberg-style executive layout.
rx,ry,rw,rh=1015,155,535,540
rect((rx,ry,rx+rw,ry+rh),PANEL,'#465158',1);rect((rx,ry,rx+rw,ry+4),UBS_RED)
text(rx+23,ry+20,'SELECTED MAJOR TRADING LOSS EVENTS',14,WHITE,True)
text(rx+23,ry+48,'Headline loss · reported currency',9,'#A8B2B7')
text(rx+rw-23,ry+48,'SOURCE',7,'#89959B',True,anchor='ra',mono=True)
line(rx+22,ry+70,rx+rw-22,ry+70,PANEL_RULE,1)

def panel_logo(key,width,height):
    mark=fit(logos[key],width,height)
    return mark

def event_row(y,key,name,event,value,source):
    global d
    d=ImageDraw.Draw(im)
    brand=events[key][3]
    if key=='UBS':
        rect((rx+13,y-5,rx+rw-13,y+42),'#25171B');rect((rx+13,y-5,rx+17,y+42),UBS_RED)
    d.rounded_rectangle((rx+23,y-1,rx+132,y+30),radius=4,fill='#F3F4F1')
    mark=panel_logo(key,99,22)
    im.paste(mark,(rx+28,y+3),mark)
    # Refresh drawing handle after paste (paste mutates im, draw remains valid).
    d=ImageDraw.Draw(im)
    text(rx+143,y,name,10,WHITE if key=='UBS' else '#D5DBDD',True)
    text(rx+143,y+18,event,8,'#89959B')
    text(rx+rw-52,y+5,value,11,brand,True,anchor='ra',mono=True)
    text(rx+rw-25,y+8,source,7,'#96A1A6',True,anchor='ra',mono=True)
    if key!='UBS':line(rx+24,y+43,rx+rw-22,y+43,PANEL_RULE,1)

event_row(ry+83,'CS','Credit Suisse (2021)','Archegos · prime brokerage','USD 5.5bn','[2]')
event_row(ry+132,'JPM','JPMorgan (2012)','London Whale · CIO portfolio','USD 6.2bn','[3]')
event_row(ry+181,'SG','Société Générale (2008)','Kerviel · unauthorised positions','EUR 4.9bn','[4]')
event_row(ry+230,'UBS','UBS (2011)','ETF / Delta One · unauthorised','USD 2.3bn','[1]')
event_row(ry+279,'BARINGS','Barings (1995)','Leeson · concealed positions','USD 1.4bn','[5]')
line(rx+22,ry+334,rx+rw-22,ry+334,PANEL_RULE,1)
rect((rx+23,ry+351,rx+109,ry+375),UBS_RED)
text(rx+66,ry+356,'UBS 2011',9,WHITE,True,anchor='mm',mono=True)
text(rx+123,ry+352,'One of the largest unauthorized trading losses',10,WHITE,True)
text(rx+123,ry+369,'recorded by a major European banking institution.',10,WHITE,True)
text(rx+23,ry+399,'Events differ; circle area tracks USD-equivalent loss.',8,'#A4AEB3')
text(rx+23,ry+439,'¹ Leeson traded in Singapore; London marks Barings HQ.',7,'#89959B')
text(rx+23,ry+453,'EUR conversion: ECB reference, 24 Jan 2008 (€1 = USD 1.4663) [6].',7,'#89959B')

# Executive takeaway, same UBS footer identity.
line(48,728,1552,728,RULE,1)
text(52,746,'TREASURY LENS',9,UBS_RED,True)
text(52,768,'Delta One control failure: capital headroom, funding confidence and liquidity readiness.',16,INK,True)
text(52,806,'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5] · ECB FX [6].',8,MUTED)
text(52,826,'Loss values are approximate headline impacts; accounting bases differ. Barings USD equivalent is approximate.',7,MUTED)
text(1548,826,'DOCUMENTATION: documents/ubs-event-context-map-sources.md',7,MUTED,False,anchor='ra')
im.save(OUT)
print(OUT)
