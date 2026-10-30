from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-event-context-map.png'
W, H = 1600, 900

PAPER = '#FFFFFF'
INK = '#183448'
MUTED = '#75818A'
LAND = '#F0F2EA'
WATER = '#FFFFFF'
COAST = '#FFFFFF'
UK_FILL = '#D58B94'
FR_FILL = '#A9BDE0'
CH_FILL = '#71BBDD'
BARINGS_GOLD = '#A9842E'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
ITALIC = FONT
SERIF_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
_font_cache = {}

def font(size, bold=False, italic=False, serif=False):
    key = (size, bold, italic, serif)
    if key not in _font_cache:
        path = SERIF_BOLD if serif else (BOLD if bold else (ITALIC if italic else FONT))
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]

def text(draw, xy, value, size, color=INK, bold=False, italic=False, anchor=None):
    draw.text(xy, value, font=font(size, bold, italic), fill=color, anchor=anchor)

def load_logo(filename, remove_white=False):
    image = Image.open(ASSETS / filename).convert('RGBA')
    if remove_white:
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = pixels[x, y]
                if r > 245 and g > 245 and b > 245:
                    pixels[x, y] = (r, g, b, 0)
    alpha = image.getchannel('A')
    bbox = alpha.point(lambda a: 255 if a > 10 else 0).getbbox()
    return image.crop(bbox) if bbox else image

def fit(image, max_width, max_height):
    scale = min(max_width / image.width, max_height / image.height)
    return image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.LANCZOS)

def paste_logo(canvas, logo, center, max_size):
    """Place a clean bank mark directly on the coloured map, with a fine white halo."""
    mark = fit(logo, *max_size)
    alpha = mark.getchannel('A')
    halo_alpha = alpha.filter(ImageFilter.MaxFilter(5))
    halo = Image.new('RGBA', mark.size, (255, 255, 255, 0))
    halo.putalpha(halo_alpha)
    x = round(center[0] - mark.width / 2)
    y = round(center[1] - mark.height / 2)
    canvas.alpha_composite(halo, (x, y))
    canvas.alpha_composite(mark, (x, y))
    return mark.size

# Clean, white canvas in the editorial style of the supplied regional-map reference.
im = Image.new('RGBA', (W, H), PAPER)
d = ImageDraw.Draw(im)

# Header kept deliberately compact so the map remains the dominant visual.
d.line((0, 1, W, 1), fill='#D9E0E2', width=2)
text(d, (48, 25), 'MAJOR EUROPEAN TRADING LOSS EVENTS', 26, INK, bold=True)
text(d, (49, 62), 'Selected benchmark trading-loss events relevant to the UBS 2011 case', 14, '#B5263E', bold=True)
skema = Image.open(ASSETS / 'skema-logo.png').convert('RGBA')
skema.thumbnail((58, 58), Image.Resampling.LANCZOS)
im.alpha_composite(skema, (1492, 18))

# Stylized western-European map, with only countries tied to the selected events coloured.
mx, my, mw, mh = 42, 105, 1516, 685
lon0, lon1 = -12.0, 20.0
lat0, lat1 = 42.0, 58.0

def xy(lon, lat):
    return (mx + (lon - lon0) / (lon1 - lon0) * mw,
            my + (lat1 - lat) / (lat1 - lat0) * mh)

geo_path = ASSETS / 'natural-earth-50m-western-europe-context.geojson'
with geo_path.open(encoding='utf-8') as handle:
    geo = json.load(handle)
geometries = {feature['properties']['name']: feature['geometry'] for feature in geo['features']}

def draw_country(name, fill):
    geometry = geometries.get(name)
    if not geometry:
        return
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        ring = polygon[0]
        xs = [point[0] for point in ring]
        ys = [point[1] for point in ring]
        if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1:
            continue
        points = [xy(lon, lat) for lon, lat in ring]
        d.polygon(points, fill=fill)
        d.line(points + [points[0]], fill=COAST, width=2, joint='curve')

# Background land and fine white country borders, as in the example map.
context_countries = [
    'Portugal', 'Spain', 'Ireland', 'Belgium', 'Netherlands', 'Germany',
    'Denmark', 'Czechia', 'Slovakia', 'Slovenia', 'Poland', 'Hungary',
    'Italy', 'Austria', 'Luxembourg'
]
for country in context_countries:
    draw_country(country, LAND)
draw_country('United Kingdom', UK_FILL)
draw_country('France', FR_FILL)
draw_country('Switzerland', CH_FILL)

# Bank marks are placed directly on their highlighted countries (no pins, circles or leader lines).
logos = {
    'JPM': load_logo('jpmorgan-chase-logo.png'),
    'SG': load_logo('societe-generale-logo.png'),
    'UBS': load_logo('ubs-logo.png', remove_white=True),
    'CS': load_logo('credit-suisse-logo.png'),
}
barings = Image.new('RGBA', (460, 100), (255, 255, 255, 0))
ImageDraw.Draw(barings).text((8, 3), 'BARINGS', font=font(68, bold=True, serif=True), fill=BARINGS_GOLD)
barings = barings.crop(barings.getchannel('A').getbbox())
logos['BARINGS'] = barings

# UK — two events, offset within the country to keep each wordmark and value readable.
paste_logo(im, logos['JPM'], (653, 357), (150, 39))
d = ImageDraw.Draw(im)
text(d, (637, 386), 'USD 6.2bn', 20, INK, bold=True)
text(d, (638, 413), 'London Whale · 2012', 11, MUTED, italic=True)

paste_logo(im, logos['BARINGS'], (526, 425), (126, 29))
d = ImageDraw.Draw(im)
text(d, (473, 449), '~USD 1.4bn', 18, INK, bold=True)
text(d, (474, 475), 'Barings · 1995', 11, MUTED, italic=True)

# France — Société Générale / Kerviel.
paste_logo(im, logos['SG'], (732, 500), (132, 43))
d = ImageDraw.Draw(im)
text(d, (677, 535), 'EUR 4.9bn', 20, INK, bold=True)
text(d, (678, 562), 'Société Générale · 2008', 11, MUTED, italic=True)

# Switzerland — both institution marks identify the Zurich hub; amounts sit beside each mark.
paste_logo(im, logos['CS'], (1008, 544), (128, 31))
d = ImageDraw.Draw(im)
text(d, (1090, 546), 'USD 5.5bn', 19, INK, bold=True)
text(d, (1091, 571), 'Credit Suisse · 2021', 10, MUTED, italic=True)

paste_logo(im, logos['UBS'], (936, 589), (82, 42))
d = ImageDraw.Draw(im)
text(d, (755, 583), 'USD 2.3bn', 19, INK, bold=True)
text(d, (756, 609), 'UBS · 2011', 10, MUTED, italic=True)

# Minimal footer: exact requested takeaway plus sourcing / location caveats.
d.line((48, 806, 1552, 806), fill='#D9E0E2', width=1)
text(d, (52, 818), 'EXECUTIVE TAKEAWAY', 8, '#B5263E', bold=True)
text(d, (52, 835), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 10, INK, bold=True)
text(d, (52, 862), 'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5] · ECB FX [6].', 7, MUTED)
text(d, (1548, 862), 'Bases shown: Barings—London; UBS & Credit Suisse—Zurich; Société Générale—Paris. UBS desk & JPMorgan event—London; Leeson traded in Singapore.', 7, MUTED, italic=True, anchor='ra')

im.convert('RGB').save(OUT)
print(OUT)
