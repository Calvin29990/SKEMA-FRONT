# -*- coding: utf-8 -*-
"""09_carte_clients_et_ecosystemes_V6.py — CARTE 08 FIGÉE + COUCHE « ÉCOSYSTÈMES FX CACHÉS » (mission V6).
Demande user 21/10 : « donne la carte et choisis des couleurs ou autre truc pour rendre cela visuel »
→ on AJOUTE aux clients FX nommés (couleurs prestataires, inchangées) des PASTILLES sectorielles
blanches cerclées de couleur + libellés colorés = les écosystèmes V6 géolocalisables (dossier
DOSSIER-2026-10-21-ecosystemes-FX-caches-V6.md : 22 découvertes, 10 secteurs, sources datées).
Canaux nationaux non ponctuels (experts-comptables, DAF, Team France Export…) = carton légende, pas de pastille.
Entrées : /tmp/univ_xy.pkl (script 01) + france-geojson.
Sorties : candidatures/CARTE-2026-10-21-marche-FX-et-ecosystemes-V6.png + .pdf"""
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
plot['nom_p']=plot['nom'].map(pretty); plot['nom_n']=plot['nom'].map(norm)

VI='#7d3ac1'; V='#0e7a3d'; BL='#2d5aa7'; RO='#c0392b'; TL='#0e8c8c'; MG='#d81b8f'
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

# ---------- clients FX colorés : IDENTIQUE CARTE 08 FIGÉE ----------
DROP=('THEA','FAREVA','HMY','VERYCHIC','SNETOR','AURLANE','OLYMPIQUE LYONNAIS','STADE DE REIMS','GT COMPANY','AMARIS FRANCE')
def dropmask(df):
    m=pd.Series(False,index=df.index)
    for k in DROP: m=m|df['nom_n'].str.contains(k,regex=False,na=False)
    return m
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
        nom,c,x,y,tx,ty=row[:6]
        ax.scatter([x],[y],s=46,facecolor=c,edgecolor='white',linewidth=1.0,zorder=40)
        ax.annotate(nom,xy=(x,y),xytext=(tx,ty),fontsize=fs,fontweight='bold',color=c,zorder=41,
                    ha='center',va='center',arrowprops=dict(arrowstyle='-',color=c,lw=0.7,alpha=0.75),
                    path_effects=HALO)

# ---------- NOUVELLE COUCHE : écosystèmes FX cachés (mission V6, 21/10/2026) ----------
# SECTEUR : couleur, marqueur — pastilles BLANCHES cerclées (distinction visuelle des points-marché pleins)
SEC={'VOILE':('#0e9db8','D'),'AÉRO':('#1f77b4','^'),'BIOTECH':('#4caf50','h'),'AGRO':('#8d5b2d','X'),
     'GBP':('#5d6d7e','s'),'JV':('#e377c2','*'),'CINÉ':('#d62728','v'),'FEST':('#ff7f0e','o'),
     'SALONS':('#00695c','s'),'ESPORT':('#2962ff','p'),'STARTUPS':('#f9a825','>'),'ÉCOLES':('#ad1457','D'),
     'GOLF':('#8bc34a','H'),'M&A':('#1a237e','P')}
# ancres : (secteur, x, y, libellé, tx, ty) — pastille grande + libellé fléché
ANC=[('AÉRO',1.444,43.604,"TOULOUSE · AÉRO\nsupply chain USD",1.00,42.72),
     ('AÉRO',-2.21,47.27,"ST-NAZAIRE aéro",-3.42,46.52),
     ('BIOTECH',5.73,45.15,"GRENOBLE/MEYLAN\nbiotech·pharma",6.28,44.58),
     ('AGRO',-1.68,48.11,"AGRO OUEST\n4,9 Md€ export",-3.9,47.02),
     ('GBP',2.38,51.02,"DUNKERQUE\ncouloir GBP £",0.72,50.28),
     ('VOILE',-1.78,46.50,"VOILE — PME sponsors\ncourse au large",-4.42,45.52),
     ('JV',3.88,43.61,"MONTPELLIER\nJEUX VIDÉO · 95 % export",2.82,42.66),
     ('CINÉ',0.11,49.49,"LE HAVRE\nexport audiovisuel",-1.62,49.86),
     ('FEST',-1.28,47.09,"CLISSON · HELLFEST\nfestivals cachets intl",-2.25,46.28),
     ('SALONS',4.78,45.62,"LYON · GL EVENTS\nsalons internationaux",4.32,44.90),
     ('M&A',3.06,50.64,"LILLE\nM&A transfrontalier",4.18,50.30),
     ('GOLF',6.59,46.40,"ÉVIAN\ngolf · 9,1 M$",6.78,47.10),
     ('ÉCOLES',7.06,43.78,"SOPHIA · campus écoles\ncash-flows en devises",6.02,43.02)]
# pins mineurs : même secteur, plus petits, sans libellé
MIN=[('AÉRO',2.03,44.61),('AÉRO',0.08,43.23),
     ('VOILE',-3.37,47.75),('VOILE',-2.00,48.66),('VOILE',-1.15,46.16),
     ('JV',-0.58,44.84),('CINÉ',7.02,43.50),('SALONS',7.10,43.62),
     ('FEST',-3.57,48.28),('FEST',6.86,47.64),
     ('M&A',7.75,48.58),('M&A',-0.42,44.98),('ÉCOLES',2.70,48.40)]
# zoom IDF : ancres + mineurs
ANC_Z=[('ESPORT',2.32,48.856,"ESPORT Paris\nprize money USD",1.70,48.97),
       ('SALONS',2.51,48.97,"VILLEPINTE\nsalons intls",2.02,49.28),
       ('STARTUPS',2.373,48.834,"STARTUPS\nStation F",3.12,48.52)]
MIN_Z=[('GOLF',2.03,48.754),('SALONS',2.29,48.832)]
def eco_layer(ax, anc, mins, fs=7.0, z=45):
    for sec,x,y in mins:
        c,m=SEC[sec]; sz=38 if m!='*' else 62
        ax.scatter([x],[y],s=sz,marker=m,facecolor='white',edgecolor=c,linewidth=1.3,zorder=z)
    for sec,x,y,lab,tx,ty in anc:
        c,m=SEC[sec]; sz=95 if m!='*' else 150
        ax.scatter([x],[y],s=sz,marker=m,facecolor='white',edgecolor=c,linewidth=2.0,zorder=z+1)
        ax.annotate(lab,xy=(x,y),xytext=(tx,ty),fontsize=fs,fontweight='bold',color=c,zorder=z+2,
                    ha='center',va='center',linespacing=1.15,
                    arrowprops=dict(arrowstyle='-',color=c,lw=0.8,alpha=0.7),path_effects=HALO)

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

fig=plt.figure(figsize=(18.5,11.69), dpi=170)
ax=fig.add_axes([0.008,0.045,0.615,0.89])
draw_france(ax); draw_points(ax,plot); auto_labels(ax,lab)
fx_labels(ax,FX_MAIN)
eco_layer(ax,ANC,MIN)
ax.annotate("Île-de-France :\n8 clients FX + 3 écosystèmes\n→ panneau ZOOM",xy=(2.6,48.9),xytext=(5.1,47.42),
            fontsize=8.2,fontweight='bold',color='#444',zorder=41,ha='left',
            arrowprops=dict(arrowstyle='-|>',color='#777',lw=0.8),
            bbox=dict(boxstyle='round,pad=0.35',fc='white',ec='#888',lw=0.8,alpha=0.95))
ax.text(0.015,0.035,f"GRAND SUD — Nouvelle-Aquitaine + Occitanie + PACA\n{SUD_N:,} sièges mesurés ({fr1(SUD_PCT)} %) · ~13 200 projetés\ndont {SUD_COEUR:,} cœur FX mesurés · {SUD_CA:.0f} Md$ de CA mesuré".replace(","," "),
        transform=ax.transAxes,fontsize=9.5,fontweight='bold',color='#6b3d00',va='bottom',
        bbox=dict(boxstyle='round,pad=0.5',fc='#fdf1dc',ec='#c9a25e',lw=1.1))
fig.text(0.02,0.976,"QUI ACHÈTE DES PRODUITS DE CHANGE — ET OÙ",fontsize=21,fontweight='bold')
fig.text(0.02,0.9605,"clients FX publiquement nommés (couleurs = prestataires)  +  ÉCOSYSTÈMES FX CACHÉS (pastilles blanches cerclées colorées)",
         fontsize=11,color='#222')
fig.text(0.02,0.9470,"écosystèmes = secteurs où naît le besoin FX avant les banques — mission V6 : 22 découvertes, 10 secteurs, sources datées au dossier + classeur",
         fontsize=9,color='#555')
fig.text(0.02,0.0315,f"Sièges sociaux ≥ 5 M€ de CA (Orbis, 20/10/2026) — un point = une entreprise — noms NOIRS = comptes ≥ 250 M$ — noms EN COULEUR = relations client→prestataire FX prouvées (18). Île-de-France : {fr1(IDF_PCT)} % des sièges, {fr1(IDF_CAPCT)} % du CA.",
         fontsize=7.4,color='#555')
fig.text(0.02,0.0215,"Relations FX en couleur : URL + citation + date au classeur ORBIS (ATTRIBUTIONS-FX). MAGENTA nom = changement de fournisseur publié. Vert = CŒUR, orange = CONTINGENT. Carte nominative — usage restreint · étude académique.",
         fontsize=7.3,color='#444')
fig.text(0.02,0.0120,"V6 (21/10/2026) : pastilles = écosystèmes géolocalisés, chacun sourcé et daté (dossier DOSSIER-2026-10-21-ecosystemes-FX-caches-V6.md + feuille ECOSYSTEMES-V6 du classeur). Canaux nationaux non localisables (experts-comptables multidevises, DAF externalisés, Team France Export, capitales French Tech, business clubs de stades, avocats desks) : carton à droite, sans pastille.",
         fontsize=7.0,color='#666')
fig.text(0.02,0.0005,"Balayage sport au 21/10/2026 : foot = 5 partenariats FX corporate publiés (4 Ebury · 1 Corpay) ; rugby TOP 14 · hand LNH · basket LNB · voile : aucun partenariat FX publié. ² OM · AS Monaco · TFC : hors univers Orbis (< 5 M€ / hors France), tracés à la demande.",
         fontsize=6.8,color='#666',va='baseline')

lx=0.645
# ---- bloc légende V6 ----
fig.text(lx,0.968,"ÉCOSYSTÈMES FX CACHÉS — MISSION V6",fontsize=11.5,fontweight='bold')
fig.text(lx,0.9555,"pastille blanche cerclée + libellé coloré = cluster géolocalisé · P1 = priorité haute · détail + sources : dossier + classeur",
         fontsize=6.6,color='#555')
rows=[('VOILE','course au large — PME sponsors · Sables · Lorient · St-Malo · La Rochelle','P1'),
      ('AÉRO','supply chain USD (Boeing 1er client export) · Toulouse · Figeac · Tarbes · St-Nazaire','P1'),
      ('BIOTECH','pharma Lyonbiopôle ~230 PME · Lyon · Grenoble/Meylan · Clermont','P1'),
      ('AGRO','Ouest export 4,9 Md€ · Valorial Rennes · Bretagne · Pays de la Loire','P1'),
      ('GBP','couloir UK 12 rot./j Douvres · Dunkerque · Calais · Lille','P2'),
      ('JV','jeux vidéo ~95 % vendu à l’étranger · Montpellier · Bordeaux','P1'),
      ('FEST','festivals cachets artistes intl · Clisson · Carhaix · Belfort','P1'),
      ('SALONS','organisateurs internationaux · GL events Lyon · Paris · Cannes','P1'),
      ('CINÉ','audiovisuel ventes export 282,7 M€ · Le Havre · Cannes · Paris','P2'),
      ('ESPORT','prize money USD · Paris — banques présentes, FX absent','P2'),
      ('STARTUPS','SaaS facturation USD · Station F + capitales French Tech','P2'),
      ('ÉCOLES','campus hors zone euro · SKEMA Raleigh · ESSEC Rabat · INSEAD','P2'),
      ('GOLF','dotations USD sur sol FR · Évian 9,1 M$ · Golf National','P2'),
      ('M&A','boutiques small/mid-cap · Lille · Strasbourg · Bordeaux','P1')]
yy=0.9455
for sec,desc,pr in rows:
    c,m=SEC[sec]
    fig.text(lx,yy,'●',fontsize=7.8,color=c)
    fig.text(lx+0.0105,yy,f"{sec}",fontsize=7.6,fontweight='bold',color=c)
    fig.text(lx+0.0820,yy,desc,fontsize=6.6,color='#333')
    if pr=='P1':
        fig.text(0.9935,yy,'P1',fontsize=6.6,fontweight='bold',color='#8a1a1a',ha='right')
    yy-=0.0130
fig.text(lx,yy+0.0035,"CANAUX NATIONAUX — non localisables (pas de pastille)",fontsize=7.4,fontweight='bold',color='#333')
fig.text(lx,yy-0.0055,"experts-comptables multidevises (détecteur n°1) · DAF externalisés · Team France Export (35 000 ent./an + dates)",
         fontsize=6.2,color='#555')
fig.text(lx,yy-0.0140,"capitales French Tech (19 capitales) · business clubs de stades (déjà prouvés : voir clubs colorés) · avocats desks intl · influence (P3)",
         fontsize=6.2,color='#555')
yy-=0.0140
# ---- légende FX (carte 08, inchangée en contenu) ----
yy0=yy-0.0200
fig.text(lx,yy0,"LÉGENDE — COULEURS DES NOMS FX",fontsize=10,fontweight='bold')
leg=[('iBanFirst','Bensimon¹ · Mobile Club¹ · Guard Industrie · Aurlane · Chrono Carpe',VI,5),
     ('BNP Paribas / Kantox','Théa · Fareva · HMY · AnimalBox · VeryChic · Snetor · Amaris¹',V,7),
     ('Ebury','Olympique Lyonnais · Stade de Reims · OM² · AS Monaco²',BL,4),
     ('Corpay','Toulouse FC²',TL,1),('Moneycorp','GT Company',RO,1),
     ('A CHANGÉ DE FOURNISSEUR (publié)','¹ Bensimon→iBanFirst · Mobile Club→iBanFirst · Amaris→BNPP',MG,3)]
yy=yy0-0.0135
for prov,names,c,n in leg:
    fig.text(lx,yy,'■',fontsize=8.6,color=c)
    fig.text(lx+0.0115,yy,f"{prov}"+(f" ({n})" if n else ''),fontsize=8.0,fontweight='bold',color=c)
    fig.text(lx+0.0115,yy-0.0092,names,fontsize=6.3,color='#333')
    yy-=0.0200
# ---- zoom IDF ----
axidf=fig.add_axes([lx,0.340,0.350,0.222])
axidf.set_xlim(1.55,3.85); axidf.set_ylim(48.30,49.32)
axidf.set_aspect(1/np.cos(np.radians(48.8)))
for code in ['11','24','27','28','44','52','84']:
    axidf.add_collection(PolyCollection(region_verts(code),facecolor=FILLS.get(code,'#f3f3f3'),edgecolor='#888',linewidth=0.6,zorder=1))
sub=plot[(plot['lon'].between(1.55,3.85))&(plot['lat'].between(48.30,49.32))]
draw_points(axidf,sub,mult=1.7)
top_idf=sub[(sub['ca_kusd']>=250000)&(~dropmask(sub))].sort_values('ca_kusd',ascending=False).head(20)
auto_labels(axidf,top_idf,fs=5.0,tl=30)
fx_labels(axidf,FX_IDF,fs=6.2)
eco_layer(axidf,ANC_Z,MIN_Z,fs=5.8)
axidf.set_title("ZOOM — ÎLE-DE-FRANCE : clients FX (couleurs) + écosystèmes V6 (pastilles)",fontsize=8.6,fontweight='bold')
axidf.set_xticks([]); axidf.set_yticks([])
for sp in axidf.spines.values(): sp.set_edgecolor('#556')
# ---- tableau régions (carte 08, inchangé) ----
axtab=fig.add_axes([lx,0.050,0.30,0.27]); axtab.axis('off')
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
plt.savefig('candidatures/CARTE-2026-10-21-marche-FX-et-ecosystemes-V6.png',dpi=190)
plt.savefig('candidatures/CARTE-2026-10-21-marche-FX-et-ecosystemes-V6.pdf')
print('carte V6 écrite — ancres:',len(ANC),'· mineurs:',len(MIN),'· zoom:',len(ANC_Z),'+',len(MIN_Z))
