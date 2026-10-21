# -*- coding: utf-8 -*-
"""
04_carte_simplifiee_PME.py — carte régionale de la tranche PME 3,8–5 M€ (tendance positive)
située JUSTE SOUS l'univers de la carte principale (≥ 5 M€).
Entrées : /tmp/seg5.pkl (fusion dédupliquée des exports 21_10 09_56 + 09_59, voir SEGMENT-SOUS-5ME)
          + /tmp/france-geojson-master/regions-version-simplifiee.geojson
Sorties : candidatures/CARTE-2026-10-21-gateau-regions-PME.pdf + .png
"""
import json, warnings
warnings.filterwarnings('ignore')
import numpy as np, pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as peff
from matplotlib.collections import PolyCollection

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
df = pd.read_pickle('/tmp/seg5.pkl')
df = df[df['_src']=='210956'].copy()          # tranche 3,8–5 M€ (export trié desc, propre)
DEPTO={'01':'84','03':'84','07':'84','15':'84','26':'84','38':'84','42':'84','43':'84','63':'84','69':'84','73':'84','74':'84',
'21':'27','25':'27','39':'27','58':'27','70':'27','71':'27','89':'27','90':'27','22':'53','29':'53','35':'53','56':'53',
'18':'24','28':'24','36':'24','37':'24','41':'24','45':'24','20':'94','08':'44','10':'44','51':'44','52':'44','54':'44',
'55':'44','57':'44','67':'44','68':'44','88':'44','02':'32','59':'32','60':'32','62':'32','80':'32',
'75':'11','77':'11','78':'11','91':'11','92':'11','93':'11','94':'11','95':'11','14':'28','27':'28','50':'28','61':'28','76':'28',
'44':'52','49':'52','53':'52','72':'52','85':'52','16':'75','17':'75','19':'75','23':'75','24':'75','33':'75','40':'75',
'47':'75','64':'75','79':'75','86':'75','87':'75','09':'76','11':'76','12':'76','30':'76','31':'76','32':'76','34':'76',
'46':'76','48':'76','65':'76','66':'76','81':'76','82':'76','04':'93','05':'93','06':'93','13':'93','83':'93','84':'93'}
def dep(cp):
    if not cp: return ''
    if cp[:2]=='20': return '20'
    if cp[:3] in ('971','972','973','974','976'): return '97'
    return cp[:2]
df['reg']=df.cp.map(lambda x: DEPTO.get(dep(x),''))
g=df[df.reg!='']
SUD={'75','76','93'}; RN={'11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Franche-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne','75':'Nouvelle-Aquitaine',
 '76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"Provence-Alpes-Côte d'Azur",'94':'Corse'}
V_IDF='#0e7a3d'; V_SUD='#d98e04'; V_NEUTRE='#dfe3e8'
TOT_N=len(g); TOT_CA=g.rev.sum()
def kpis(c):
    s=g[g.reg==c]; n=len(s); ca=s.rev.sum()
    return n, n/TOT_N*100, ca/1e9, ca/TOT_CA*100
K={c:kpis(c) for c in RN}
sud=g[g.reg.isin(SUD)]; idf=g[g.reg=='11']
SUD_N=len(sud); SUD_CA=sud.rev.sum(); IDF_N=len(idf); IDF_CA=idf.rev.sum()
def fr1(x): return f"{x:.1f}".replace(".",",")
def fr0(x): return f"{x:,.0f}".replace(","," ")

rgeo=json.load(open('/tmp/france-geojson-master/regions-version-simplifiee.geojson'))
dgeo=json.load(open('/tmp/france-geojson-master/departements-version-simplifiee.geojson'))
RV={f['properties']['code']: f for f in rgeo['features']}
def region_verts(code):
    gg=RV[code]['geometry']; polys=gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]
    return [np.array(p[0]) for p in polys if p and p[0]]
def large_ring(code):
    vs=region_verts(code); return max(vs,key=lambda v:(v[:,0].max()-v[:,0].min())*(v[:,1].max()-v[:,1].min()))
def centroid(code):
    v=large_ring(code); x=v[:,0]; y=v[:,1]
    a=0.5*np.sum(x[:-1]*y[1:]-x[1:]*y[:-1])
    return (np.sum((x[:-1]+x[1:])*(x[:-1]*y[1:]-x[1:]*y[:-1]))/(6*a),
            np.sum((y[:-1]+y[1:])*(x[:-1]*y[1:]-x[1:]*y[:-1]))/(6*a))
LBL={'75':(-1.7,0.35),'76':(-1.25,-0.55),'93':(0.3,-0.85),'52':(0.2,-1.05),'24':(0.95,-0.75),'53':(-1.35,-0.35),'28':(-1.0,0.55),'11':(0,0.15)}

fig=plt.figure(figsize=(16.54,11.69), dpi=170)
ax=fig.add_axes([0.005,0.025,0.60,0.90])
FILLS={c:(V_IDF if c=='11' else (V_SUD if c in SUD else V_NEUTRE)) for c in RN}
EDGES={c:('#0b5c30' if c=='11' else ('#8a5a00' if c in SUD else '#9aa2ab')) for c in RN}
for code in RN:
    ax.add_collection(PolyCollection(region_verts(code), facecolor=FILLS[code],
        edgecolor=EDGES[code], linewidth=2.2 if code=='11' or code in SUD else 0.7, zorder=2, alpha=0.92))
dv=[]
for f in dgeo['features']:
    gg=f['geometry']; polys=gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]
    dv+=[np.array(p[0]) for p in polys if p and p[0]]
ax.add_collection(PolyCollection(dv, facecolor='none', edgecolor='white', linewidth=0.35, zorder=3))
for code,name in RN.items():
    n,pn,ca,pca=K[code]
    cx,cy=centroid(code)
    dx,dy=LBL.get(code,(0,0))
    txt=f"{name}\n{fr0(n)} · {fr1(pn)} %\n{fr1(ca)} Md€ · {fr1(pca)} %"
    fw='bold' if code=='11' or code in SUD else 'normal'
    fs=10.6 if code=='11' or code in SUD else 8.8
    fc='#073d1f' if code=='11' else ('#5c3c00' if code in SUD else '#3a4049')
    ax.text(cx+dx,cy+dy,txt,ha='center',va='center',fontsize=fs,fontweight=fw,color=fc,zorder=5,
            path_effects=[peff.withStroke(linewidth=2.4,foreground='white',alpha=0.85)])
ax.set_xlim(-5.6,10.2); ax.set_ylim(41.0,51.6); ax.set_aspect('equal'); ax.axis('off')

# ---------- panneau droit ----------
rx=0.615
fig.text(rx,0.954,"TRANCHE 3,8–5 M€ EN CROISSANCE",fontsize=18,fontweight='bold')
fig.text(rx,0.928,"PME juste sous la carte principale · requête Orbis : actives × France × CA ≤ 5 M€",
         fontsize=9,color='#444')
fig.text(rx,0.912,"× tendance CA positive (LY/LY-1) — tri export par CA décroissant",
         fontsize=9,color='#444')
fig.text(rx,0.891,f"n géocodé = {fr0(TOT_N)} métropole (+147 outre-mer) · {fr1(TOT_CA/1e9)} Md€ · export 21/10 09:56",
         fontsize=8.4,color='#666')
fig.text(rx,0.877,"limite Moody's : 6 000 lignes/page (requête totale : 1 254 798 entités)",
         fontsize=8.4,color='#666')

fig.text(rx,0.845,"COMPARAISON AVEC L'UNIVERS ≥ 5 M€ (la carte)",fontsize=12,fontweight='bold')
rows=[("Sièges Île-de-France",32.9,100*IDF_N/TOT_N,"32,9 %","27,4 %"),
      ("CA Île-de-France",68.1,100*IDF_CA/TOT_CA,"68,1 %","27,4 %"),
      ("Sièges Grand Sud (NA+Occ+PACA)",20.3,100*SUD_N/TOT_N,"20,3 %","22,9 %"),
      ("CA Grand Sud",9.0,100*SUD_CA/TOT_CA,"9,0 %","22,9 %")]
axc=fig.add_axes([rx,0.615,0.36,0.215]); axc.axis('off')
y=0.92
for lab,v1,v2,t1,t2 in rows:
    axc.text(0.0,y,lab,fontsize=9.4,fontweight='bold')
    axc.barh(y-0.10,0.80*v1/72,height=0.042,color='#5b7ea6',left=0.0)
    axc.text(0.80*v1/72+0.012,y-0.10,t1,fontsize=8.8,va='center',color='#2e4e6e')
    axc.barh(y-0.165,0.80*v2/72,height=0.042,color='#e0a23c',left=0.0)
    axc.text(0.80*v2/72+0.012,y-0.165,t2,fontsize=8.8,va='center',color='#7a5410')
    y-=0.235
axc.set_xlim(0,1.15); axc.set_ylim(-0.16,1.0)
axc.text(0.0,-0.12,"■ univers ≥ 5 M€",fontsize=8.2,color='#5b7ea6')
axc.text(0.24,-0.12,"■ tranche 3,8–5 M€ (croissance)",fontsize=8.2,color='#c78f2e')

fig.text(rx,0.585,"CE QUE LA COMPARAISON DIT",fontsize=12,fontweight='bold')
bullets=[
 "• Moins mégapole : IDF 33 % → 27 % des sièges sous 5 M€.",
 "• Paris dans le CA : 68 % → 27 %. La valeur se régionalise.",
 "• Grand Sud : 20 % → 23 % sièges ; 9 % → 23 % du CA tranche.",
 "• Lecture FX : les prospects 'seuil 200 k€' des fintechs sont",
 "   plus régionaux que le cœur des grandes salles — terrain",
 "   des canaux (LBP×Ebury) et des fintechs hors-Paris.",
]
fig.text(rx,0.567,"\n".join(bullets),fontsize=10,va='top',linespacing=1.5)

fig.text(rx,0.335,"GRAND SUD — DÉTAIL",fontsize=12,fontweight='bold')
gs=[(RN[c],)+K[c] for c in ['75','76','93']]
glines=[f"{nme[:18]:18s} {fr0(n):>5s} · {fr1(pn):4s} % · {fr1(ca):3s} Md€" for nme,n,pn,ca,pca in gs]
fig.text(rx,0.316,"\n".join(glines),fontsize=9.6,va='top',fontfamily='DejaVu Sans Mono',linespacing=1.75)
fig.text(rx,0.232,f"Total : {fr0(SUD_N)} sièges = {fr1(100*SUD_N/TOT_N)} % · {fr1(SUD_CA/1e9)} Md€ = {fr1(100*SUD_CA/TOT_CA)} %",
         fontsize=10.2,fontweight='bold',color='#7a5410')

fig.text(rx,0.145,"Limites & suite : couverture = 6 000 lignes sur 1 254 798 requêtés (0,5 %),",
         fontsize=8.2,color='#666')
fig.text(rx,0.129,"tranche CONTIGUË à la carte (tri descendant). Découper la requête (région/NACE)",
         fontsize=8.2,color='#666')
fig.text(rx,0.113,"pour couvrir plus. Source : Export Orbis 21_10_2026 09_56 (+09_59 = fond à 90 k€).",
         fontsize=8.2,color='#666')
fig.text(rx,0.091,"Étude académique personnelle — aucune finalité commerciale.",
         fontsize=8.2,color='#666',style='italic')

plt.savefig('candidatures/CARTE-2026-10-21-gateau-regions-PME.pdf')
plt.savefig('candidatures/CARTE-2026-10-21-gateau-regions-PME.png')
print('cartes PME écrites')
