# -*- coding: utf-8 -*-
"""
03_carte_simplifiee.py — carte sans noms : régions métropole colorées, % sièges + % CA.
Entrée : /tmp/univ_xy.pkl (script 01) + france-geojson regions/departements.
Sorties : candidatures/CARTE-2026-10-20-gateau-regions.pdf + .png
"""
import json, warnings
warnings.filterwarnings('ignore')
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as peff
from matplotlib.collections import PolyCollection
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
u = pd.read_pickle('/tmp/univ_xy.pkl')
SUD={'75','76','93'}; METRO={'11','24','27','28','32','44','52','53','75','76','84','93','94'}
RN={'11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Franche-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne','75':'Nouvelle-Aquitaine',
 '76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"Provence-Alpes-Côte d'Azur",'94':'Corse'}
V_IDF='#0e7a3d'; V_SUD='#d98e04'; V_NEUTRE='#dfe3e8'
g = u[u['reg_code'].isin(METRO)]
TOT_N=len(g); TOT_CA=g['ca_kusd'].sum()/1e6
def kpis(code):
    s=g[g['reg_code']==code]
    return len(s), len(s)/TOT_N*100, s['ca_kusd'].sum()/1e6, s['ca_kusd'].sum()/1e6/TOT_CA*100
K={c:kpis(c) for c in RN}
sud=g[g['reg_code'].isin(SUD)]; idf=g[g['reg_code']=='11']
SUD_N=len(sud); SUD_CA=sud['ca_kusd'].sum()/1e6; IDF_N=len(idf); IDF_CA=idf['ca_kusd'].sum()/1e6
def fr1(x): return f"{x:.1f}".replace(".",",")
def fr0(x): return f"{x:,.0f}".replace(","," ")

rgeo=json.load(open('/tmp/france-geojson-master/regions-version-simplifiee.geojson'))
dgeo=json.load(open('/tmp/france-geojson-master/departements-version-simplifiee.geojson'))
RV={f['properties']['code']: f for f in rgeo['features']}
def region_verts(code):
    gg=RV[code]['geometry']
    polys=gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]
    return [np.array(p[0]) for p in polys if p and p[0]]
def large_ring(code):
    vs=region_verts(code); return max(vs, key=lambda v:(v[:,0].max()-v[:,0].min())*(v[:,1].max()-v[:,1].min()))
def centroid(code):
    v=large_ring(code)
    x=v[:,0]; y=v[:,1]
    a=0.5*np.sum(x[:-1]*y[1:]-x[1:]*y[:-1])
    cx=np.sum((x[:-1]+x[1:])*(x[:-1]*y[1:]-x[1:]*y[:-1]))/(6*a)
    cy=np.sum((y[:-1]+y[1:])*(x[:-1]*y[1:]-x[1:]*y[:-1]))/(6*a)
    return cx,cy

fig=plt.figure(figsize=(16.54,11.69), dpi=170)
ax=fig.add_axes([0.01,0.03,0.66,0.92])
FILLS={c:(V_IDF if c=='11' else (V_SUD if c in SUD else V_NEUTRE)) for c in RN}
EDGES={c:('#0b5c30' if c=='11' else ('#8a5a00' if c in SUD else '#9aa2ab')) for c in RN}
for code in RN:
    ax.add_collection(PolyCollection(region_verts(code), facecolor=FILLS[code],
        edgecolor=EDGES[code], linewidth=2.2 if code in ('11',) or code in SUD else 0.7, zorder=2, alpha=0.92))
dv=[]
for f in dgeo['features']:
    gg=f.get('geometry')
    if not gg: continue
    polys=gg.get('coordinates') if gg.get('type')=='MultiPolygon' else [gg.get('coordinates')]
    for poly in polys or []:
        if poly and poly[0]: dv.append(np.array(poly[0]))
ax.add_collection(PolyCollection(dv, facecolor='none', edgecolor='white', linewidth=0.6, alpha=0.8, zorder=3))
ax.set_xlim(-5.5,10.2); ax.set_ylim(41.0,51.4); ax.set_aspect(1/np.cos(np.radians(46))); ax.axis('off')

OFF={'53':(-0.6,0.25),'28':(0.1,0.55),'24':(-0.15,0),'27':(0.25,-0.05),'94':(0,0.55),'52':(-0.3,0),'84':(0.15,0.1),'32':(0,-0.05),'44':(0.15,0.05)}
SHORT={'93':'PACA'}
for code,(n,pn,ca,pc) in K.items():
    if code=='11':
        cx,cy=centroid('11')
        ax.annotate(f"Île-de-France\n{fr0(n)} sièges · {fr1(pn)} %\n{fr0(ca)} Md$ · {fr1(pc)} %",
            xy=(cx,cy), xytext=(3.35,49.82), ha='center', fontsize=10.5, fontweight='bold', color='#0b5c30', zorder=8,
            arrowprops=dict(arrowstyle='-', color='#0b5c30', lw=1.1),
            bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='#0b5c30', lw=1.4, alpha=0.96),
            linespacing=1.35)
        continue
    cx,cy=centroid(code); dx,dy=OFF.get(code,(0,0)); x,y=cx+dx,cy+dy
    big = code in SUD
    col_txt = 'white' if big else '#2b2f33'
    fs1 = 11.0 if big else 8.6
    halo=[peff.withStroke(linewidth=3,foreground='#8a5a00',alpha=0.5)] if big else None
    kw=dict(path_effects=halo) if halo else {}
    ax.text(x,y+0.16,SHORT.get(code,RN[code]),ha='center',fontsize=fs1+1.2,fontweight='bold',color=col_txt,zorder=6,**kw)
    ax.text(x,y-0.12,f"{fr0(n)} sièges · {fr1(pn)} %",ha='center',fontsize=fs1,color=col_txt,zorder=6,**kw)
    ax.text(x,y-0.44,f"{fr0(ca)} Md$ · {fr1(pc)} %",ha='center',fontsize=fs1,color=col_txt,zorder=6,**kw)

fig.text(0.02,0.975,"LE MARCHÉ CORPORATE FRANÇAIS — SIÈGES SOCIAUX ≥ 5 M€ : LE GÂTEAU EN DEUX VUES",
         fontsize=20, fontweight='bold')
fig.text(0.02,0.952,"Univers Orbis 64 646 sociétés (actives, France, derniers comptes) — 61 199 hors financières — 45 837 géolocalisées (70,9 %) — chaque région : nombre de sièges (%) et CA cumulé (%) — aucune entreprise nommée",
         fontsize=10.5, color='#333')

# ------- colonne droite : 2 panneaux + barres 100 % -------
RX=0.690
def panel(y, h, fc, ec, title, lines, tcol):
    fig.patches.append(FancyBboxPatch((RX,y),0.298,h, transform=fig.transFigure,
        boxstyle="round,pad=0.006,rounding_size=0.010", fc=fc, ec=ec, lw=1.6, zorder=4))
    fig.text(RX+0.014,y+h-0.030,title,fontsize=12,fontweight='bold',color=tcol,zorder=6)
    yy=y+h-0.062
    for t,fs,fw in lines:
        fig.text(RX+0.014,yy,t,fontsize=fs,fontweight=fw,color='#1c1c1c',zorder=6)
        yy-=0.033
idf_n_pct=IDF_N/TOT_N*100; idf_ca_pct=IDF_CA/TOT_CA*100
sud_n_pct=SUD_N/TOT_N*100; sud_ca_pct=SUD_CA/TOT_CA*100
panel(0.625,0.20,'#e8f4ec',V_IDF,"ÎLE-DE-FRANCE",
      [(f"{fr1(idf_ca_pct)} % du CA — {fr0(IDF_CA)} Md$",12.5,'bold'),
       (f"{fr1(idf_n_pct)} % des sièges — {fr0(IDF_N)} sociétés",11,'normal'),
       ("1er territoire : panels de toutes les banques",9.5,'normal'),
       ("(effet maisons-mères de groupes cotés)",9.5,'normal')], V_IDF)
panel(0.395,0.20,'#fdf1dc',V_SUD,"GRAND SUD — NA · OCCITANIE · PACA",
      [(f"{fr1(sud_n_pct)} % des sièges — {fr0(SUD_N)} sociétés",12.5,'bold'),
       (f"{fr1(sud_ca_pct)} % du CA — {fr0(SUD_CA)} Md$",11,'normal'),
       ("≈ 13 200 sociétés projetées (estimation étalonnée)",9.5,'normal'),
       ("2e territoire : cibles nombreuses, panels moins denses",9.5,'normal')], '#7a4a00')
rest_n_pct=100-idf_n_pct-sud_n_pct; rest_ca_pct=100-idf_ca_pct-sud_ca_pct
panel(0.285,0.085,'#f2f3f5','#9aa2ab',"RESTE DE LA MÉTROPOLE (10 régions)",
      [(f"{fr1(rest_n_pct)} % des sièges · {fr1(rest_ca_pct)} % du CA",11,'bold')], '#4a4f55')

axb1=fig.add_axes([RX+0.014,0.215,0.27,0.024])
axb2=fig.add_axes([RX+0.014,0.158,0.27,0.024])
def bar100(ax, parts, title):
    left=0
    for frac,col,lbl in parts:
        ax.barh([0], [frac], left=left, color=col, edgecolor='white', height=0.9)
        if frac>7:
            tc='white' if col!=V_NEUTRE else '#333'
            ax.text(left+frac/2,0,lbl,ha='center',va='center',fontsize=8.5,fontweight='bold',color=tc)
        left+=frac
    ax.set_xlim(0,100); ax.set_ylim(-0.55,0.55); ax.axis('off'); ax.set_title(title,fontsize=9.5,loc='left',fontweight='bold')
bar100(axb2,[(idf_n_pct,V_IDF,f"IDF {fr1(idf_n_pct)} %"),(sud_n_pct,V_SUD,f"Sud {fr1(sud_n_pct)} %"),(rest_n_pct,V_NEUTRE,f"reste {fr1(rest_n_pct)} %")],"PART DES SIÈGES")
bar100(axb1,[(idf_ca_pct,V_IDF,f"IDF {fr1(idf_ca_pct)} %"),(sud_ca_pct,V_SUD,f"Sud {fr1(sud_ca_pct)} %"),(rest_ca_pct,V_NEUTRE,f"reste {fr1(rest_ca_pct)} %")],"PART DU CA")

fig.text(RX+0.014,0.108,"Lecture : 1/3 des sièges, 2/3 du CA en Île-de-France (effet maisons-mères).",fontsize=8.6,color='#333')
fig.text(RX+0.014,0.090,"Le Sud aligne un cinquième des sièges pour 9,0 % du CA.",fontsize=8.6,color='#333')
fig.text(0.02,0.012,f"URLs sources : Orbis (exports 19-20/10/2026, licence SKEMA) · COG Etalab · france-geojson (G. David) — étude académique personnelle, aucune donnée client — + Outre-mer : 764 sièges mesurés ({fr0(u[u['reg_code'].isin({'01','02','03','04','06'})]['ca_kusd'].sum()/1e6)} Md$), hors carte.",
         fontsize=6.8,color='#555')
import os
out1='/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-gateau-regions.pdf'
out2='/home/user/SKEMA-FRONT/candidatures/CARTE-2026-10-20-gateau-regions.png'
fig.savefig(out1,dpi=170); fig.savefig(out2,dpi=190)
print('PDF:',os.path.getsize(out1),'PNG:',os.path.getsize(out2))
print('IDF',idf_n_pct,idf_ca_pct,'SUD',sud_n_pct,sud_ca_pct,'RESTE',rest_n_pct,rest_ca_pct)
