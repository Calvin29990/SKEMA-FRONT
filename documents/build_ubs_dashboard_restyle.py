from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
SOURCE=ASSETS/'ubs-dashboard-reference.png'
OUT=ROOT/'ubs-dashboard-ubs-palette.png'
W,H=1600,900
BG='#F7F7F4'; INK='#25333D'; MUTED='#66737B'; RULE='#C8CDCE'; UBS_RED='#D71935'; UBS_GOLD='#D69A36'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

im=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(im)
fonts={}
def f(n,b=False):
    key=(n,b)
    if key not in fonts:fonts[key]=ImageFont.truetype(BOLD if b else FONT,n)
    return fonts[key]
def text(x,y,s,n=16,color=INK,b=False,anchor=None):d.text((x,y),s,font=f(n,b),fill=color,anchor=anchor)

# Preserve the user-supplied chart panels pixel-for-pixel. Only the page around them is redesigned.
source=Image.open(SOURCE).convert('RGB')
regions=[(18,80,333,520),(344,80,658,520),(669,80,983,520)]
# White ExCo/Treasury Committee masthead.
ubs=Image.open(ASSETS/'ubs-logo.png').convert('RGBA')
pix=ubs.load()
for yy in range(ubs.height):
    for xx in range(ubs.width):
        r,g,b,a=pix[xx,yy]
        if r>246 and g>246 and b>246:pix[xx,yy]=(255,255,255,0)
ubs.thumbnail((188,66),Image.Resampling.LANCZOS)
im.paste(ubs,(48,25),ubs)
skema=Image.open(ASSETS/'skema-logo.png').convert('RGBA')
skema.thumbnail((74,74),Image.Resampling.LANCZOS)
im.paste(skema,(1476,20),skema)
text(270,28,'UBS INVESTMENT BANK  |  2011',28,INK,True)
text(270,68,'ETF DELTA ONE DESK  ·  RISK ESCALATION',16,UBS_RED,True)
text(270,98,'Treasury Committee  /  operational risk, hidden exposure and controls',12,MUTED)
d.line((48,135,1552,135),fill=RULE,width=2)
text(52,151,'REFERENCE CHARTS  ·  PRESERVED UNCHANGED',10,MUTED,True)
text(1548,151,'UBS  ×  SKEMA',10,INK,True,anchor='ra')

# The original three terminal panels (including all Japanese candlesticks, legends, axes,
# labels, and linework) are pasted without edits, recoloring, redrawing, or data changes.
boxes=[(64,177,474,664),(563,177,474,664),(1062,177,474,664)]
for region,box in zip(regions,boxes):
    crop=source.crop(region)
    crop=crop.resize((box[2],box[3]),Image.Resampling.LANCZOS)
    im.paste(crop,(box[0],box[1]))

# Committee note remains outside the unmodified chart images.
d.line((52,861,1548,861),fill=RULE,width=1)
text(54,873,'Charts reproduced exactly from the supplied image. Figures and series are not independently validated.',9,MUTED)

im.save(OUT)
print(OUT)
