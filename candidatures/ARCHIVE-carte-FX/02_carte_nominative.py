# -*- coding: utf-8 -*-
"""
02_carte_nominative.py — carte 2 pages (A3 + A4) : 39 015 sièges cœur+contingent positionnés,
221 comptes >= 250 M$ nommés, zoom Île-de-France, page 2 = mode d'emploi.
Entrées : /tmp/univ_xy.pkl (script 01) + france-geojson-master/regions|departements-version-simplifiee.geojson
Sorties : candidatures/CARTE-2026-10-20-qui-achete-le-FX-et-ou.pdf + CARTE-2026-10-20-page1.png + page2.png
"""
import json, re, unicodedata, warnings
warnings.filterwarnings('ignore')
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.lines as mlines
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})

def norm(s):
    if s is None or isinstance(s,float): return ''
    s=str(s).strip()
    if not s or s.lower()=='nan': return ''
    s=s.replace('Œ','OE').replace('œ','oe'); s=unicodedata.normalize('NFKD',s)
    s=''.join(ch for ch in s if not unicodedata.combining(ch)); s=s.upper()
    s=re.sub(r"[’'\-]",' ',s); s=re.sub(r'[^A-Z0-9 ]',' ',s)
    return re.sub(r'\s+',' ',s).strip()

def pretty(n):
    out=[]
    for w in re.split(r'(\s+)', str(n)):
        if not w.strip(): out.append(w); continue
        parts=[p.capitalize() if len(p)>4 else p.upper() for p in w.split('-')]
        out.append('-'.join(parts))
    return ''.join(out).strip()

def fr1(x): return f"{x:.1f}".replace(".",",")

u = pd.read_pickle('/tmp/univ_xy.pkl')
SUD={'75','76','93'}; METRO={'11','24','27','28','32','44','52','53','75','76','84','93','94'}
REGIONS={'11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Fr.-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne','75':'Nouvelle-Aquitaine',
 '76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"PACA",'94':'Corse'}
ok = u[u['lon'].notna() & u['reg_code'].isin(METRO)].copy()
plot = ok[(~ok['fin']) & (ok['classe'].isin(['CŒUR','CONTINGENT']))].copy()
plot['nom_p'] = plot['nom'].map(pretty)
plot['vn'] = plot['ville'].map(norm)
print('points tracés:', len(plot))

COULEURS={'CŒUR':'#0e7a3d','CONTINGENT':'#e8a020'}
TAILLES={'>1 Md$':26,'250 M$-1 Md$':15,'100-250 M$':6.0,'25-100 M$':2.6,'5-25 M$':1.1}
rgeo=json.load(open('/tmp/france-geojson-master/regions-version-simplifiee.geojson'))
dgeo=json.load(open('/tmp/france-geojson-master/departements-version-simplifiee.geojson'))
RV={f['properties']['code']: f for f in rgeo['features']}
def region_verts(code):
    g=RV[code]['geometry']
    polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    return [np.array(p[0]) for p in polys if p and p[0]]
def verts_of(geo):
    vs=[]
    for f in geo['features']:
        g=f.get('geometry')
        if not g: continue
        polys=g.get('coordinates') if g.get('type')=='MultiPolygon' else [g.get('coordinates')]
        for poly in polys or []:
            if poly and poly[0]: vs.append(np.array(poly[0]))
    return vs
FILLS={'75':'#fdf1dc','76':'#fdf1dc','93':'#fdf1dc','11':'#e9edf2'}
def draw_france(ax):
    for code in RV:
        ax.add_collection(PolyCollection(region_verts(code), facecolor=FILLS.get(code,'#f7f7f7'),
                          edgecolor='#666666', linewidth=0.7, zorder=1))
    ax.add_collection(PolyCollection(verts_of(dgeo), facecolor='none',
                                     edgecolor='#999999', linewidth=0.22, alpha=0.5, zorder=2))
    ax.set_xlim(-5.4,10.0); ax.set_ylim(41.0,51.4)
    ax.set_aspect(1/np.cos(np.radians(46))); ax.axis('off')
def draw_points(ax, sub, mult=1.0, z0=5):
    for cl in ['CONTINGENT','CŒUR']:
        s=sub[sub['classe']==cl]
        for b,taille in TAILLES.items():
            sb=s[s['bande']==b]
            if len(sb)==0: continue
            ec='black' if b in ('>1 Md$','250 M$-1 Md$') else 'none'
            lw=0.5 if b=='>1 Md$' else (0.35 if b=='250 M$-1 Md$' else 0)
            ax.scatter(sb['lon'],sb['lat'], s=taille*mult, c=COULEURS[cl], alpha=0.6,
                       edgecolors=ec, linewidths=lw, zorder=z0+(4 if cl=='CŒUR' else 0))
def auto_labels(ax, cands, fs=5.4, tl=30):
    try:
        from adjustText import adjust_text
        texts=[ax.text(r['lon'],r['lat'],r['nom_p'][:34],fontsize=fs,zorder=30,ha='center',va='center') for _,r in cands.iterrows()]
        try:
            adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-',color='0.45',lw=0.35),
                        min_arrow_len=6, expand=(1.15,1.5), time_lim=tl)
        except TypeError:
            try: adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='-',color='0.45',lw=0.35),
                             force_text=(0.2,0.5), force_points=(0.1,0.3), lim=300)
            except TypeError: adjust_text(texts, ax=ax)
    except Exception as e:
        print('labels fallback:', e)

p = plot[(plot['ca_kusd']>=250000) & (plot['reg_code']!='11')].copy()
p['cx']=(p['lon']/0.50).astype(int); p['cy']=(p['lat']/0.34).astype(int)
lab=(p.sort_values('ca_kusd',ascending=False).drop_duplicates(['cx','cy']))
must = plot[(plot['ca_kusd']>=8e6) & (plot['reg_code']!='11')]
lab = pd.concat([lab, must]).drop_duplicates('idx').sort_values('ca_kusd',ascending=False).head(230)
print('labels carte:', len(lab))
def ville_count(*villes):
    vn=[norm(v) for v in villes]
    return int(plot['vn'].isin(vn).sum())
N_MARS=ville_count('MARSEILLE'); N_TLS=ville_count('TOULOUSE'); N_BDX=ville_count('BORDEAUX','MERIGNAC')
N_MPL=ville_count('MONTPELLIER'); N_NICE=ville_count('NICE'); N_PERP=ville_count('PERPIGNAN'); N_AIX=ville_count('AIX EN PROVENCE')
print('villes:', N_MARS,N_TLS,N_BDX,N_MPL,N_NICE,N_PERP,N_AIX)

g=u[u['reg_code'].isin(METRO)]
sud=g[g['reg_code'].isin(SUD)]
SUD_N=len(sud); SUD_CA=sud['ca_kusd'].sum()/1e6
SUD_COEUR=int(g.loc[g['reg_code'].isin(SUD) & (g['classe']=='CŒUR'),'nom'].count())
IDF_N=int((g['reg_code']=='11').sum()); IDF_CA=g.loc[g['reg_code']=='11','ca_kusd'].sum()/1e6
GEO_N=len(g); GEO_CA=g['ca_kusd'].sum()/1e6
SUD_PCT=SUD_N/GEO_N*100; IDF_PCT=IDF_N/GEO_N*100; IDF_CAPCT=IDF_CA/GEO_CA*100
gm=u[u['reg_code'].notna() & ~u['reg_code'].isin(['ETR','COM'])]
P_IDF=int(((gm['reg_code']=='11')&(gm['ca_kusd']>=250000)).sum())
P_SUD=int((gm['reg_code'].isin(SUD)&(gm['ca_kusd']>=250000)).sum())
P_75=int(((gm['reg_code']=='75')&(gm['ca_kusd']>=250000)).sum())
P_76=int(((gm['reg_code']=='76')&(gm['ca_kusd']>=250000)).sum())
P_93=int(((gm['reg_code']=='93')&(gm['ca_kusd']>=250000)).sum())
GEO_ALL=int((u['reg_code'].notna()&~u['reg_code'].isin(['ETR'])).sum())

fig = plt.figure(figsize=(16.54,11.69), dpi=170)
ax = fig.add_axes([0.015,0.05,0.70,0.885])
draw_france(ax); draw_points(ax, plot); auto_labels(ax, lab)
villes_info=[((5.38,43.28),f"Marseille · {N_MARS}"),((1.44,43.60),f"Toulouse · {N_TLS}"),
 ((-0.62,44.86),f"Bordeaux + Mérignac · {N_BDX}"),((3.88,43.62),f"Montpellier · {N_MPL}"),
 ((7.27,43.71),f"Nice · {N_NICE}"),((5.44,43.53),f"Aix · {N_AIX}"),((2.90,42.69),f"Perpignan · {N_PERP}")]
for (x,y),txt in villes_info:
    ax.annotate(txt, xy=(x,y), xytext=(x,y-0.60), fontsize=7.5, ha='center', fontweight='bold',
                color='#7a4a00', zorder=40,
                bbox=dict(boxstyle='round,pad=0.28', fc='white', ec='#c9a25e', lw=0.7, alpha=0.95))
ax.text(0.015,0.035,f"GRAND SUD — Nouvelle-Aquitaine + Occitanie + PACA\n{SUD_N:,} sièges mesurés ({fr1(SUD_PCT)} %) · ~13 200 projetés\ndont {SUD_COEUR:,} cœur FX mesurés · {SUD_CA:.0f} Md$ de CA mesuré".replace(","," "),
        transform=ax.transAxes, fontsize=9.5, fontweight='bold', color='#6b3d00', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='#fdf1dc', ec='#c9a25e', lw=1.1))
fig.text(0.02,0.975,"QUI ACHÈTE DES PRODUITS DE CHANGE — ET OÙ", fontsize=21, fontweight='bold')
fig.text(0.02,0.952,"Sièges sociaux des sociétés françaises ≥ 5 M€ de CA — un point = une entreprise sur sa commune INSEE — les noms = comptes ≥ 250 M$ (meilleur par zone ; l'Île-de-France est nommée dans le zoom)",
         fontsize=10.5, color='#333')
fig.text(0.02,0.030,f"64 646 sociétés ≥ 5 M€ (Orbis, 20/10/2026) — 61 199 hors financières — {GEO_ALL:,} géolocalisées (70,9 % ; ≥99 % dès 25 M$) — {len(plot):,} points cœur+contingent tracés sur cette carte — Île-de-France : {fr1(IDF_PCT)} % des sièges, {fr1(IDF_CAPCT)} % du CA.".replace(","," "),
         fontsize=6.8, color='#555')
fig.text(0.02,0.014,"CŒUR = flux de change récurrents par construction · CONTINGENT = flux épisodiques · hors cible (DOMESTIQUE + financières) : non tracé, cf. page 2 §2 · étude académique personnelle — aucune donnée client.",
         fontsize=6.8, color='#555')
lx=0.735
fig.text(lx,0.925,"LÉGENDE", fontsize=11, fontweight='bold')
axleg=fig.add_axes([lx,0.845,0.25,0.075]); axleg.axis('off')
leg=[mlines.Line2D([],[],marker='o',ls='',markersize=7,markerfacecolor=COULEURS['CŒUR'],markeredgecolor='none',alpha=0.7),
     mlines.Line2D([],[],marker='o',ls='',markersize=7,markerfacecolor=COULEURS['CONTINGENT'],markeredgecolor='none',alpha=0.7),
     mlines.Line2D([],[],marker='o',ls='',markersize=9,markerfacecolor='white',markeredgecolor='black')]
axleg.legend(leg,["CŒUR — 24 862 points (flux récurrents)","CONTINGENT — flux épisodiques","≥ 250 M$ — couche prestige, nommée"],
             loc='lower left', frameon=False, fontsize=8.2, handletextpad=0.4, borderaxespad=0.2, labelspacing=0.35)
fig.text(lx,0.840,"Taille des points = tranche de CA (5-25 M$ → >1 Md$)", fontsize=7.2, color='#333')
fig.text(lx,0.826,"Compteurs villes = sièges cœur+contingent localisés.", fontsize=7.2, color='#333')
axidf=fig.add_axes([lx,0.375,0.25,0.435])
axidf.set_xlim(1.25,3.80); axidf.set_ylim(47.95,49.40)
axidf.set_aspect(1/np.cos(np.radians(48.7)))
for code in ['11','24','27','28','44','52','84']:
    axidf.add_collection(PolyCollection(region_verts(code),facecolor=FILLS.get(code,'#f3f3f3'),edgecolor='#888',linewidth=0.6,zorder=1))
sub=plot[(plot['lon'].between(1.25,3.80))&(plot['lat'].between(47.95,49.40))]
draw_points(axidf, sub, mult=1.7)
top_idf=sub.sort_values('ca_kusd',ascending=False).head(24)
auto_labels(axidf, top_idf, fs=5.0, tl=30)
axidf.set_title(f"ZOOM — ÎLE-DE-FRANCE\n{IDF_N:,} sièges mesurés ({fr1(IDF_PCT)} %) · {IDF_CA:,.0f} Md$ ({fr1(IDF_CAPCT)} % du CA)".replace(","," "), fontsize=9, fontweight='bold')
axidf.set_xticks([]); axidf.set_yticks([])
for sp in axidf.spines.values(): sp.set_edgecolor('#556')
axtab=fig.add_axes([lx,0.045,0.25,0.315]); axtab.axis('off')
rec=g.groupby('reg_code').agg(n=('nom','count'), ca=('ca_kusd',lambda s:s.sum()/1e6)).reset_index().sort_values('n',ascending=False)
lines=["SIÈGES MESURÉS PAR RÉGION"," region                n   CA Md$"," "+"-"*35]
for _,r in rec.iterrows():
    nm=REGIONS.get(r['reg_code'],'?')
    flag=' <' if r['reg_code'] in SUD else '  '
    lines.append(f"{flag}{nm[:20]:<21}{int(r['n']):>6}{r['ca']:>8.0f}")
sud2=g[g['reg_code'].isin(SUD)]
lines.append(" "+"-"*35)
lines.append(f"  GRAND SUD            {len(sud2):>6}{sud2['ca_kusd'].sum()/1e6:>8.0f}")
lines.append(f"  TOTAL metropole      {len(g):>6}{g['ca_kusd'].sum()/1e6:>8.0f}")
om=u[u['reg_code'].isin({'01','02','03','04','06'})]
lines.append(f"  + Outre-mer          {len(om):>6}{om['ca_kusd'].sum()/1e6:>8.0f}")
axtab.text(0,1,"\n".join(lines),fontsize=6.8,family='DejaVu Sans Mono',va='top',transform=axtab.transAxes,linespacing=1.42)
import os
os.makedirs('/home/user/SKEMA-FRONT/candidatures', exist_ok=True)
pdf_path='/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-qui-achete-le-FX-et-ou.pdf'
pdf=PdfPages(pdf_path)
pdf.savefig(fig)
fig.savefig('/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-page1.png', dpi=190)
plt.close(fig)

fig2=plt.figure(figsize=(8.27,11.69), dpi=170)
fig2.text(0.06,0.965,"MODE D'EMPLOI DE LA CARTE — la lire, la prouver, la défendre",fontsize=15,fontweight='bold')
def bloc(titre, txt, y, ts=8.8):
    fig2.text(0.065,y,titre,fontsize=11.5,fontweight='bold',color='#0e5a2d')
    fig2.text(0.085,y-0.016,txt,fontsize=ts,va='top',linespacing=1.55)
    n=txt.count('\n')+1
    return y-0.016-n*0.0158-0.018
y=0.935
y=bloc("1 — CE QUE LA CARTE MONTRE",
"""Un univers mesuré, pas estimé. Univers Orbis « France, actives, CA ≥ 5 M€, derniers comptes » = 64 646 sociétés.
Hors établissements financiers (NACE 64-66) : 61 199 entreprises — le marché corporate.
Géolocalisation : ville du siège Orbis → commune INSEE → département → région (COG Etalab) :
45 837 sociétés localisées (70,9 % de l'univers ; 99,3-99,9 % sur chaque tranche ≥ 25 M$ ; la tranche 5-25 M$
est couverte à 52,9 % — plafond de 45 000 lignes de l'export Orbis, pas un trou de données).
Contrôle qualité : croisement avec un export Orbis porteur de la région native → accord 98,7 % sur 4 192 sociétés.""",y)
y=bloc("2 — QUI ACHÈTE (classes, lues sur les points) — et qui est hors cible",
"""CŒUR (vert) — flux de change récurrents par construction : négoce international (46), industrie exportatrice,
agro, transport aérien/maritime, tech, ingénierie, tourisme international → 32 994 sociétés dans l'univers.
CONTINGENT (ambre) — flux épisodiques mais réels : retail à achats importés, BTP, énergie, services… → 23 861.
DOMESTIQUE (HORS CIBLE, non tracé) — pas d'exposition structurelle : santé, éducation, immobilier local,
administrations, commerce purement domestique… → 7 791.
FINANCIÈRES K64-66 (HORS CHAMP, non tracées) — le marché des banques n'est pas la cible corporate : 3 447.
Sur la carte : 39 015 points cœur+contingent positionnés. Boîtes nommées = comptes ≥ 250 M$
(3 149 « prestige » au total, dont 935 > 1 Md$) ; en Île-de-France, les noms sont dans le zoom dédié.""",y)
txt3=(f"""Île-de-France : {IDF_N:,} sièges = {fr1(IDF_PCT)} % des entreprises localisées… mais {fr1(IDF_CAPCT)} % du CA (effet sièges de groupes).
GRAND SUD (NA + Occitanie + PACA) : {SUD_N:,} sièges mesurés = {fr1(SUD_PCT)} %, dont {SUD_COEUR:,} cœur FX ; projection prudente
du reliquat non exporté (par tranche de CA) → ≈ 13 200 sociétés, ≈ 6 500 cœur FX : un cinquième du marché.
Prestige : IDF {P_IDF} · Grand Sud {P_SUD} (NA {P_75} / PACA {P_93} / Occitanie {P_76}).
Corridors Sud (points tracés) : Marseille {N_MARS} · Toulouse {N_TLS} · Bordeaux+Mérignac {N_BDX} · Aix {N_AIX} ·
Montpellier {N_MPL} · Nice {N_NICE} · Perpignan {N_PERP}.""".replace(","," "))
y=bloc("3 — OÙ (le gâteau, mesuré)",txt3,y)
g2=u[u['reg_code'].notna() & ~u['reg_code'].isin(['ETR','COM']) & u['lon'].notna()]
top_f=g2.sort_values('ca_kusd',ascending=False).head(15)
top_s=g2[g2['reg_code'].isin(SUD)].sort_values('ca_kusd',ascending=False).head(15)
lines1=["TOP 15 — FRANCE (CA Md$)  (siège)"]
for _,r in top_f.iterrows():
    lines1.append(f"{pretty(r['nom'])[:27]:<29}{r['ca_kusd']/1e6:>8.1f} {str(r['ville'])[:16].title()}")
lines2=["TOP 15 — GRAND SUD (CA Md$)  (siège)"]
for _,r in top_s.iterrows():
    lines2.append(f"{pretty(r['nom'])[:27]:<29}{r['ca_kusd']/1e6:>8.1f} {str(r['ville'])[:16].title()}")
t1=fig2.add_axes([0.065,y-0.305,0.42,0.295]); t1.axis('off')
t1.text(0,1,"\n".join(lines1),fontsize=6.9,family='DejaVu Sans Mono',va='top',linespacing=1.5)
t2=fig2.add_axes([0.53,y-0.305,0.42,0.295]); t2.axis('off')
t2.text(0,1,"\n".join(lines2),fontsize=6.9,family='DejaVu Sans Mono',va='top',linespacing=1.5)
y=y-0.315
y=bloc("4 — LIMITES HONNÊTES (à dire avant qu'on ne les trouve)",
"""Géolocalisation à 70,9 % (plafond export 45 000 lignes) : la structure est mesurée ; la tranche 5-25 M$ du Sud
est projetée (étiquetée « ≈ »). Ville du siège ≠ ville des flux : le siège décide. Classes lues sur le code
NACE principal, par construction — la preuve de flux se fait ensuite dossier par dossier (douanes US, comptes).""",y)
y=bloc("5 — LA PHRASE (à tenir en entretien)",
"""« 64 646 sociétés françaises dépassent 5 M€ de CA ; 61 199 hors financières. J'en ai géolocalisé 45 837 — 70 %
du marché, plus de 99 % dès 25 M$. L'Île-de-France : un tiers des sièges, les deux tiers du CA, déjà couverte
par les panels de toutes les banques. Le Grand Sud : un cinquième du marché, ~13 200 sociétés, ~6 500 cœur FX
— Marseille, Toulouse, Bordeaux, Montpellier, Nice. Cette carte les montre, nommément. »""",y)
fig2.text(0.06,0.020,"Sources : Orbis (exports 19-20/10/2026, licence SKEMA) · COG Etalab (decoupage-administratif) · contours/communes : france-geojson (G. David).\nÉtude académique personnelle — démonstration méthodologique pour entretien : aucune donnée client, aucune donnée d'attribution de prestataire, aucune finalité commerciale.",
          fontsize=6.6,color='#555')
pdf.savefig(fig2)
fig2.savefig('/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-page2.png', dpi=190)
plt.close(fig2)
pdf.close()
print("PDF:", pdf_path, os.path.getsize(pdf_path))
print("PNG1:", os.path.getsize('/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-page1.png'))
print("PNG2:", os.path.getsize('/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-page2.png'))
