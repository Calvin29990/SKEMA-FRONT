# -*- coding: utf-8 -*-
"""08_carte_clients_couleurs.py — LES CLIENTS FX PUBLIQUEMENT NOMMÉS SUR LA CARTE DU MARCHÉ.
Demande user 21/10 : fond = même carte que « Qui achète des produits de change » (points cœur/
contingent + noms prestige EN NOIR) ; les 15 relations FX prouvées = NOMS EN COULEUR par
prestataire (iBanFirst violet, BNP/Kantox vert, Ebury bleu, Moneycorp rouge). Pas plus.
Coordonnées = sièges réels dans l'univers Orbis (10/15) ; 5 hors univers (<5 M€) + Fareva
(s siège groupe hors export) positionnés sur siège public connu — notes en bas de carte.
Entrées : /tmp/univ_xy.pkl (script 01) + france-geojson.
Sorties : candidatures/CARTE-2026-10-21-clients-FX-sur-carte-marche.png + .pdf"""
import json, re, unicodedata, warnings
warnings.filterwarnings('ignore')
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import matplotlib.patheffects as peff
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
HALO=[peff.withStroke(linewidth=2.6,foreground='white',alpha=0.95)]

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

u=pd.read_pickle('/tmp/univ_xy.pkl')
SUD={'75','76','93'}; METRO={'11','24','27','28','32','44','52','53','75','76','84','93','94'}
REGIONS={'11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Fr.-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne','75':'Nouvelle-Aquitaine',
 '76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"PACA",'94':'Corse'}
ok=u[u['lon'].notna() & u['reg_code'].isin(METRO)].copy()
plot=ok[(~ok['fin']) & (ok['classe'].isin(['CŒUR','CONTINGENT']))].copy()
plot['nom_p']=plot['nom'].map(pretty); plot['nom_n']=plot['nom'].map(norm); plot['vn']=plot['ville'].map(norm)

VI='#7d3ac1'; V='#0e7a3d'; BL='#2d5aa7'; RO='#c0392b'; TL='#0e8c8c'; MG='#d81b8f'
# iBanFirst violet · BNPP/Kantox vert · Ebury bleu · Moneycorp rouge · Corpay teal · SWITCH magenta
COULEURS={'CŒUR':'#0e7a3d','CONTINGENT':'#e8a020'}
TAILLES={'>1 Md$':26,'250 M$-1 Md$':15,'100-250 M$':6.0,'25-100 M$':2.6,'5-25 M$':1.1}
rgeo=json.load(open('/tmp/france-geojson-master/regions-version-simplifiee.geojson'))
dgeo=json.load(open('/tmp/france-geojson-master/departements-version-simplifiee.geojson'))
RV={f['properties']['code']: f for f in rgeo['features']}
def region_verts(code):
    g=RV[code]['geometry']; polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
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
        ax.add_collection(PolyCollection(region_verts(code),facecolor=FILLS.get(code,'#f7f7f7'),
                          edgecolor='#666666',linewidth=0.7,zorder=1))
    ax.add_collection(PolyCollection(verts_of(dgeo),facecolor='none',
                                     edgecolor='#999999',linewidth=0.22,alpha=0.5,zorder=2))
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
            ax.scatter(sb['lon'],sb['lat'],s=taille*mult,c=COULEURS[cl],alpha=0.6,
                       edgecolors=ec,linewidths=lw,zorder=z0+(4 if cl=='CŒUR' else 0))
def auto_labels(ax,cands,fs=5.4,tl=30):
    try:
        from adjustText import adjust_text
        texts=[ax.text(r['lon'],r['lat'],r['nom_p'][:34],fontsize=fs,zorder=30,ha='center',va='center') for _,r in cands.iterrows()]
        try: adjust_text(texts,ax=ax,arrowprops=dict(arrowstyle='-',color='0.45',lw=0.35),
                         min_arrow_len=6,expand=(1.15,1.5),time_lim=tl)
        except TypeError:
            try: adjust_text(texts,ax=ax,arrowprops=dict(arrowstyle='-',color='0.45',lw=0.35),
                             force_text=(0.2,0.5),force_points=(0.1,0.3),lim=300)
            except TypeError: adjust_text(texts,ax=ax)
    except Exception as e: print('labels fallback:',e)

# ---------- clients FX à colorer ----------
# noir = je retire ces entités de la couche « prestige » pour éviter les doublons
DROP=('THEA','FAREVA','HMY','VERYCHIC','SNETOR','AURLANE','OLYMPIQUE LYONNAIS','STADE DE REIMS','GT COMPANY','AMARIS FRANCE')
def dropmask(df):
    m=pd.Series(False,index=df.index)
    for k in DROP: m=m|df['nom_n'].str.contains(k,regex=False,na=False)
    return m
# (nom affiché, couleur, x, y, tx, ty) — carte principale (hors IDF) / zoom (IDF)
FX_MAIN=[('Théa',V,3.115,45.786,2.35,46.05),('Fareva',V,4.830,45.060,4.00,44.45),
         ('HMY',V,3.589,47.850,2.42,47.50),('Amaris¹',MG,4.836,45.755,5.55,45.42),
         ('Guard Industrie',VI,4.835,45.764,3.75,45.40),('Olympique Lyonnais',BL,4.961,45.772,5.85,46.05),
         ('Stade de Reims',BL,4.060,49.295,4.55,49.85),
         ('Olympique de Marseille',BL,5.400,43.300,6.15,43.62),('AS Monaco',BL,7.420,43.740,7.95,44.12),
         ('Toulouse FC',TL,1.444,43.604,0.30,42.95)]
FX_IDF=[('Bensimon¹',MG,2.300,48.840,1.90,49.14),
        ('Mobile Club¹',MG,2.450,48.870,2.95,49.20),
        ('AnimalBox',V,2.390,48.840,3.00,49.02),('VeryChic',V,2.343,48.856,2.75,48.55),
        ('Aurlane',VI,2.343,48.856,1.80,48.60),('Snetor',V,2.255,48.898,2.38,49.28),
        ('GT Company',RO,2.771,48.873,3.72,48.92),('Chrono Carpe',VI,2.490,48.790,2.75,48.36)]
def fx_labels(ax,fx,fs=7.6):
    for row in fx:
        nom,c,x,y,tx,ty=row[:6]; sub,sc=(row[6],row[7]) if len(row)>6 else (None,None)
        ax.scatter([x],[y],s=46,facecolor=c,edgecolor='white',linewidth=1.0,zorder=40)
        ax.annotate(nom,xy=(x,y),xytext=(tx,ty),fontsize=fs,fontweight='bold',color=c,zorder=41,
                    ha='center',va='center',arrowprops=dict(arrowstyle='-',color=c,lw=0.7,alpha=0.75),
                    path_effects=HALO)
        if sub:
            ax.text(tx,ty-0.155 if fs>7 else ty-0.085,sub,fontsize=fs-1.5,color=sc,zorder=41,
                    ha='center',va='center',path_effects=HALO)

p=plot[(plot['ca_kusd']>=250000)&(plot['reg_code']!='11')&(~dropmask(plot))].copy()
p['cx']=(p['lon']/0.50).astype(int); p['cy']=(p['lat']/0.34).astype(int)
lab=(p.sort_values('ca_kusd',ascending=False).drop_duplicates(['cx','cy']))
must=plot[(plot['ca_kusd']>=8e6)&(plot['reg_code']!='11')&(~dropmask(plot))]
lab=pd.concat([lab,must]).drop_duplicates('idx').sort_values('ca_kusd',ascending=False).head(230)

g=u[u['reg_code'].isin(METRO)]
sud=g[g['reg_code'].isin(SUD)]; SUD_N=len(sud); SUD_CA=sud['ca_kusd'].sum()/1e6
SUD_COEUR=int(g.loc[g['reg_code'].isin(SUD)&(g['classe']=='CŒUR'),'nom'].count())
IDF_N=int((g['reg_code']=='11').sum()); IDF_CA=g.loc[g['reg_code']=='11','ca_kusd'].sum()/1e6
GEO_N=len(g); GEO_CA=g['ca_kusd'].sum()/1e6
SUD_PCT=SUD_N/GEO_N*100; IDF_PCT=IDF_N/GEO_N*100; IDF_CAPCT=IDF_CA/GEO_CA*100
GEO_ALL=int((u['reg_code'].notna()&~u['reg_code'].isin(['ETR'])).sum())

fig=plt.figure(figsize=(16.54,11.69), dpi=170)
ax=fig.add_axes([0.015,0.05,0.70,0.885])
draw_france(ax); draw_points(ax,plot); auto_labels(ax,lab)
fx_labels(ax,FX_MAIN)
ax.annotate("Île-de-France :\n8 clients FX nommés\n→ panneau ZOOM",xy=(2.6,48.9),xytext=(5.1,47.55),
            fontsize=8.2,fontweight='bold',color='#444',zorder=41,ha='left',
            arrowprops=dict(arrowstyle='-|>',color='#777',lw=0.8),
            bbox=dict(boxstyle='round,pad=0.35',fc='white',ec='#888',lw=0.8,alpha=0.95))
ax.text(0.015,0.035,f"GRAND SUD — Nouvelle-Aquitaine + Occitanie + PACA\n{SUD_N:,} sièges mesurés ({fr1(SUD_PCT)} %) · ~13 200 projetés\ndont {SUD_COEUR:,} cœur FX mesurés · {SUD_CA:.0f} Md$ de CA mesuré".replace(","," "),
        transform=ax.transAxes,fontsize=9.5,fontweight='bold',color='#6b3d00',va='bottom',
        bbox=dict(boxstyle='round,pad=0.5',fc='#fdf1dc',ec='#c9a25e',lw=1.1))
fig.text(0.02,0.975,"LES CLIENTS FX PUBLIQUEMENT NOMMÉS — SUR LA CARTE DU MARCHÉ",fontsize=21,fontweight='bold')
fig.text(0.02,0.952,"Sièges sociaux ≥ 5 M€ de CA (Orbis) — un point = une entreprise — les noms NOIRS = comptes ≥ 250 M$ — les noms EN COULEUR = relations client→prestataire FX prouvées publiquement (18, dont 3 clubs hors univers), colorées par prestataire",
         fontsize=10.3,color='#333')
fig.text(0.02,0.030,f"64 646 sociétés ≥ 5 M€ (Orbis, 20/10/2026) — 61 199 hors financières — {GEO_ALL:,} géolocalisées (70,9 % ; ≥99 % dès 25 M$) — {len(plot):,} points tracés — Île-de-France : {fr1(IDF_PCT)} % des sièges, {fr1(IDF_CAPCT)} % du CA.".replace(","," "),
         fontsize=6.8,color='#555')
fig.text(0.02,0.016,"Relations FX en couleur : URL + citation + date au classeur ORBIS (ATTRIBUTIONS-FX). MAGENTA = changement de fournisseur publié (3). Fareva : siège groupe Tournon (export). Vert = CŒUR, orange = CONTINGENT ; noms noirs = comptes ≥ 250 M$. Carte nominative — usage restreint · étude académique.",
         fontsize=7.6,color='#444')
fig.text(0.02,0.003,"² OM · AS Monaco (Principauté) · Toulouse FC : hors univers Orbis (club < 5 M€ / hors France), tracés à la demande. Balayage clubs L1/L2 au 21/10/2026 — PSG · Lille · Lens · Rennes · Nantes · Nice · Saint-Étienne · Montpellier · Brest · Le Havre · Auxerre · Strasbourg · Paris FC : aucun partenaire FX corporate publié ; Nice×Robinhood = sponsor retail, non retenu.",
         fontsize=7.1,color='#666')
lx=0.735
fig.text(lx,0.925,"LÉGENDE — COULEURS DES NOMS FX",fontsize=11,fontweight='bold')
leg=[('iBanFirst','Bensimon¹ · Mobile Club¹ · Guard Industrie · Aurlane · Chrono Carpe',VI,5),
     ('BNP Paribas / Kantox','Théa · Fareva · HMY · AnimalBox · VeryChic · Snetor · Amaris¹',V,7),
     ('Ebury','Olympique Lyonnais · Stade de Reims · OM² · AS Monaco²',BL,4),
     ('Corpay','Toulouse FC²',TL,1),
     ('Moneycorp','GT Company',RO,1),
     ('A CHANGÉ DE FOURNISSEUR (publié)','¹ Bensimon→iBanFirst (2019) · Mobile Club→iBanFirst (2025) · Amaris→BNPP (2017)',MG,3)]
yy=0.910
for prov,names,c,n in leg:
    fig.text(lx,yy,'■',fontsize=9.0,color=c)
    fig.text(lx+0.013,yy,f"{prov}"+(f" ({n})" if n else ''),fontsize=8.4,fontweight='bold',color=c)
    fig.text(lx+0.013,yy-0.0108,names,fontsize=6.7,color='#333')
    yy-=0.0240
axidf=fig.add_axes([lx,0.375,0.25,0.385])
axidf.set_xlim(1.55,3.85); axidf.set_ylim(48.30,49.32)
axidf.set_aspect(1/np.cos(np.radians(48.8)))
for code in ['11','24','27','28','44','52','84']:
    axidf.add_collection(PolyCollection(region_verts(code),facecolor=FILLS.get(code,'#f3f3f3'),edgecolor='#888',linewidth=0.6,zorder=1))
sub=plot[(plot['lon'].between(1.55,3.85))&(plot['lat'].between(48.30,49.32))]
draw_points(axidf,sub,mult=1.7)
top_idf=sub[(sub['ca_kusd']>=250000)&(~dropmask(sub))].sort_values('ca_kusd',ascending=False).head(20)
auto_labels(axidf,top_idf,fs=5.0,tl=30)
fx_labels(axidf,FX_IDF,fs=6.6)
axidf.set_title("ZOOM — ÎLE-DE-FRANCE : les 8 clients FX en couleur",fontsize=9.2,fontweight='bold')
axidf.set_xticks([]); axidf.set_yticks([])
for sp in axidf.spines.values(): sp.set_edgecolor('#556')
axtab=fig.add_axes([lx,0.045,0.25,0.315]); axtab.axis('off')
rec=g.groupby('reg_code').agg(n=('nom','count'),ca=('ca_kusd',lambda s:s.sum()/1e6)).reset_index().sort_values('n',ascending=False)
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
plt.savefig('candidatures/CARTE-2026-10-21-clients-FX-sur-carte-marche.png',dpi=190)
plt.savefig('candidatures/CARTE-2026-10-21-clients-FX-sur-carte-marche.pdf')
print('carte couleurs écrite — labels noirs:',len(lab),'| points:',len(plot))
