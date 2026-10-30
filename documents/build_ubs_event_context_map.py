from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-event-context-map.png'
W,H=1600,900
PAPER='#F7F7F4'; INK='#24323B'; MUTED='#68757C'; RULE='#C8CDCE'
PANEL='#101519'; PANEL_RULE='#303A40'
MAP_WATER='#F8F9F6'; MAP_LAND='#E9EDE6'; MAP_COAST='#BFC9C1'
UBS_RED='#D71935'; CS_BLUE='#2B628E'; JPM_BLUE='#287BAE'; SG_RED='#B5213D'; BARINGS_GOLD='#B19347'; WHITE='#FFFFFF'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts={}
def f(size,b=False,m=False,serif=False):
    k=(size,b,m,serif)
    if k not in fonts:fonts[k]=ImageFont.truetype(SERIF if serif else (MONO if m else (BOLD if b else FONT)),size)
    return fonts[k]
def text(x,y,s,size=16,color=INK,b=False,anchor=None,mono=False,serif=False):
    d.text((x,y),s,font=f(size,b,mono,serif),fill=color,anchor=anchor)
def line(x1,y1,x2,y2,color=RULE,width=1):d.line((x1,y1,x2,y2),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)
def rounded(box,fill,outline=None,width=1,radius=5):d.rounded_rectangle(box,radius=radius,fill=fill,outline=outline,width=width)
def crop_logo(path,remove_white=False):
    im=(path.copy() if isinstance(path,Image.Image) else Image.open(path)).convert('RGBA');p=im.load()
    if remove_white:
        for yy in range(im.height):
            for xx in range(im.width):
                r,g,b,a=p[xx,yy]
                if r>245 and g>245 and b>245:p[xx,yy]=(r,g,b,0)
    bbox=im.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox()
    return im.crop(bbox) if bbox else im
def fit(im,maxw,maxh):
    ratio=min(maxw/im.width,maxh/im.height)
    return im.resize((max(1,round(im.width*ratio)),max(1,round(im.height*ratio))),Image.Resampling.LANCZOS)

im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im)
# Established UBS header identity.
mark=crop_logo(ASSETS/'ubs-logo.png',True);mark.thumbnail((188,66),Image.Resampling.LANCZOS);im.paste(mark,(48,23),mark)
sk=Image.open(ASSETS/'skema-logo.png').convert('RGBA');sk.thumbnail((74,74),Image.Resampling.LANCZOS);im.paste(sk,(1475,18),sk)
text(270,27,'WHY THE UBS EVENT MATTERS',28,INK,True)
text(270,68,'Contextualising the 2011 UBS trading loss within European banking incidents',14,UBS_RED,True)
text(270,98,'Treasury risk context  /  selected loss events',11,MUTED)
line(48,133,1552,133,RULE,2)

# Identity marks. Barings Bank historically used a crest; this is a custom period-neutral wordmark.
logos={
 'CS':crop_logo(ASSETS/'credit-suisse-logo.png'),
 'JPM':crop_logo(ASSETS/'jpmorgan-chase-logo.png'),
 'SG':crop_logo(ASSETS/'societe-generale-logo.png'),
 'UBS':crop_logo(ASSETS/'ubs-logo.png',True),
}
barings=Image.new('RGBA',(460,100),(255,255,255,0));bd=ImageDraw.Draw(barings)
bd.text((8,3),'BARINGS',font=f(68,True,serif=True),fill=BARINGS_GOLD)
logos['BARINGS']=crop_logo(barings)
brand={'CS':CS_BLUE,'JPM':JPM_BLUE,'SG':SG_RED,'UBS':UBS_RED,'BARINGS':BARINGS_GOLD}

# Map panel; retain the UBS European outline and zoom on London, Paris and Zurich.
mx,my,mw,mh=50,155,940,540
rect((mx,my,mx+mw,my+mh),MAP_WATER,'#D2DAD4',1)
map_base=im.copy()
lon0,lon1=-8.0,15.5;lat0,lat1=43.0,55.5
def xy(lon,lat):return (mx+(lon-lon0)/(lon1-lon0)*mw,my+(lat1-lat)/(lat1-lat0)*mh)
# Gentle grid and contextual land, so the map is not left blank.
for lon in [-5,0,5,10,15]:line(xy(lon,50)[0],my,xy(lon,50)[0],my+mh,'#E5EAE4',1)
for lat in [45,50,55]:line(mx,xy(0,lat)[1],mx+mw,xy(0,lat)[1],'#E5EAE4',1)
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
# Colour the host regions like the reference map; the label chips identify institutions and events.
draw_country('United Kingdom',JPM_BLUE,WHITE,2)
draw_country('France',SG_RED,WHITE,2)
draw_country('Switzerland',CS_BLUE,WHITE,2)
# Distinct non-circular hub patches for the second London and Zurich institutions.
def geo_patch(points,fill,outline=WHITE,width=2):
    pts=[xy(lon,lat) for lon,lat in points]
    d.polygon(pts,fill=fill)
    d.line(pts+[pts[0]],fill=outline,width=width,joint='curve')
# London / Barings: gold angular hub patch within the blue UK region.
geo_patch([(-1.15,52.05),(-0.18,52.18),(0.75,51.88),(0.86,51.20),(0.13,50.82),(-0.86,51.02)],BARINGS_GOLD)
# Zurich / UBS: bright-red angular patch over the blue Swiss host region.
geo_patch([(7.48,47.72),(8.22,47.82),(9.08,47.58),(9.32,46.98),(8.70,46.72),(7.88,46.88),(7.42,47.25)],UBS_RED)

# Hub positions and square city points (no proportional circles).
city={'London':xy(-0.12,51.51),'Paris':xy(2.35,48.86),'Zurich':xy(8.54,47.38)}
lx,ly=city['London'];px,py=city['Paris'];zx,zy=city['Zurich']
# City labels in white over the coloured host-country fills.
d.text((lx+10,ly+9),'LONDON',font=f(8,True),fill=WHITE,stroke_width=1,stroke_fill=JPM_BLUE)
d.text((px+77,py-4),'PARIS',font=f(8,True),fill=WHITE,stroke_width=1,stroke_fill=SG_RED)
d.text((zx+9,zy+54),'ZURICH',font=f(8,True),fill=WHITE,stroke_width=1,stroke_fill=CS_BLUE)

# Flat logo chips echo the club-map reference. Values use each institution's brand colour.
def logo_chip(key,x,y,w,h):
    rounded((x,y,x+w,y+h),WHITE,brand[key],1,4)
    logo=fit(logos[key],w-12,h-8)
    im.paste(logo,(round(x+(w-logo.width)/2),round(y+(h-logo.height)/2)),logo)
    global d;d=ImageDraw.Draw(im)
def amount(x,y,value,key,size=10):
    box=d.textbbox((0,0),value,font=f(size,True))
    tw=box[2]-box[0];th=box[3]-box[1]
    rounded((x-4,y-3,x+tw+7,y+th+4),WHITE,brand[key],1,4)
    text(x,y,value,size,brand[key],True)
def leader(start,end,key):
    x1,y1=start;x2,y2=end
    line(x1,y1,x2,y2,WHITE,4);line(x1,y1,x2,y2,brand[key],2)
# Hairline connectors tie flat logo plaques to the square hub points (no circles).
leader(city['London'],(lx+3,ly-61),'JPM')
leader(city['London'],(lx-116,ly+39),'BARINGS')
leader(city['Paris'],(px,py+19),'SG')
leader(city['Zurich'],(zx+102,zy-47),'CS')
leader(city['Zurich'],(zx-78,zy+43),'UBS')
# London: two events share one hub, distinguished by colour and separate angular patch / wordmark.
logo_chip('JPM',lx-61,ly-93,128,32);amount(lx-48,ly-57,'USD 6.2bn','JPM')
text(lx-52,ly-113,'JPMORGAN · LONDON WHALE',7,JPM_BLUE,True)
logo_chip('BARINGS',lx-165,ly+24,98,30);amount(lx-160,ly+58,'~USD 1.4bn','BARINGS',9)
text(lx-160,ly+78,'LEESON¹',7,BARINGS_GOLD,True)
# Paris: SocGen event
logo_chip('SG',px-67,py+20,132,32);amount(px-20,py+57,'EUR 4.9bn','SG')
text(px-59,py+5,'KERVIEL · 2008',7,SG_RED,True)
# Zurich: Credit Suisse and UBS, offset and tied to the same square hub point.
logo_chip('CS',zx+41,zy-63,126,32);amount(zx+52,zy-27,'USD 5.5bn','CS')
text(zx+47,zy-79,'CREDIT SUISSE · ARCHEGOS',7,CS_BLUE,True)
logo_chip('UBS',zx-121,zy+27,86,31);amount(zx-113,zy+62,'USD 2.3bn','UBS')
text(zx-120,zy+11,'UBS · 2011',7,UBS_RED,True)
# Map title strip and explanation of the non-circular hub colour patches.
rect((mx+1,my+1,mx+mw-1,my+35),MAP_WATER)
text(mx+18,my+14,'EUROPEAN FINANCIAL HUBS',9,MUTED,True)
text(mx+mw-18,my+14,'HUB COLOURS · REPORTED LOSS VALUES',8,MUTED,True,anchor='ra',mono=True)
# Clip map fills and logo labels to panel bounds.
clip=Image.new('L',(W,H),0);ImageDraw.Draw(clip).rectangle((mx,my,mx+mw,my+mh),fill=255)
im=Image.composite(im,map_base,clip);d=ImageDraw.Draw(im)
rect((mx,my,mx+mw,my+mh),None,'#D2DAD4',1)

# Bloomberg-style data rail with the bank marks and colour-matched values.
rx,ry,rw,rh=1015,155,535,540
rect((rx,ry,rx+rw,ry+rh),PANEL,'#465158',1);rect((rx,ry,rx+rw,ry+4),UBS_RED)
text(rx+23,ry+20,'SELECTED MAJOR TRADING LOSS EVENTS',14,WHITE,True)
text(rx+23,ry+48,'Headline loss · reported currency',9,'#A8B2B7')
text(rx+rw-23,ry+48,'SOURCE',7,'#89959B',True,anchor='ra',mono=True)
line(rx+22,ry+70,rx+rw-22,ry+70,PANEL_RULE,1)
def panel_logo(key,width,height):return fit(logos[key],width,height)
def event_row(y,key,name,event,value,source):
    global d;d=ImageDraw.Draw(im);col=brand[key]
    if key=='UBS':
        rect((rx+13,y-5,rx+rw-13,y+42),'#25171B');rect((rx+13,y-5,rx+17,y+42),UBS_RED)
    d.rounded_rectangle((rx+23,y-1,rx+132,y+30),radius=4,fill='#F3F4F1')
    mark=panel_logo(key,99,22);im.paste(mark,(rx+28,y+3),mark);d=ImageDraw.Draw(im)
    text(rx+143,y,name,10,WHITE if key=='UBS' else '#D5DBDD',True)
    text(rx+143,y+18,event,8,'#89959B')
    text(rx+rw-52,y+5,value,11,col,True,anchor='ra',mono=True)
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
text(rx+23,ry+399,'Hub fills are illustrative; event labels identify each institution.',8,'#A4AEB3')
text(rx+23,ry+439,'¹ Leeson traded in Singapore; London marks Barings HQ.',7,'#89959B')
text(rx+23,ry+453,'UBS patch: Zurich HQ; loss-making ETF / Delta One desk was London [1].',7,'#89959B')


# Executive takeaway and primary-source references.
line(48,728,1552,728,RULE,1)
text(52,746,'TREASURY LENS',9,UBS_RED,True)
text(52,768,'Delta One control failure: capital headroom, funding confidence and liquidity readiness.',16,INK,True)
text(52,806,'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5].',8,MUTED)
text(52,826,'Loss values are approximate headline impacts; accounting bases differ. Barings USD equivalent is approximate.',7,MUTED)
text(1548,826,'DOCUMENTATION: documents/ubs-event-context-map-sources.md',7,MUTED,False,anchor='ra')
im.save(OUT)
print(OUT)
