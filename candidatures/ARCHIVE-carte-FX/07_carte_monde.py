# -*- coding: utf-8 -*-
"""07_carte_monde.py — « QUI EST CLIENT DE QUI » MONDE (hors France) — modèle comptable étendu.
Même méthode que la carte France : relations client→prestataire FX publiquement prouvées
(URL + citation + date dans la feuille CAS-MONDE du classeur ORBIS). Base = preuves publiques
nommées ; absence de preuve ≠ absence de prestataire ; les % mesurent la VISIBILITÉ publique,
pas la part réelle. 21/10/2026.
Layout : monde (dots numérotés) + ZOOM EUROPE (12 relations lisibles) + panneau droit.
Sorties : candidatures/CARTE-2026-10-21-monde-attributions-FX.png + .pdf"""
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as peff
import matplotlib.patches as mpatches

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
GEO=json.load(open('/tmp/world-geo-json-master/countries.geo.json'))
KX=0.85
RED='#c0392b'; ORANGE='#e67e22'; GREY='#8a939b'; BLUE='#2d5aa7'
HALO=[peff.withStroke(linewidth=2.2,foreground='white',alpha=0.92)]

# n, client, prestataire, lon, lat, couleur, note (zoom EU), (dx,dy,ha) label zoom, (dx,dy,ha) label monde
EU=[
 ( 1,'Arsenal','Airwallex',-0.11,51.52,ORANGE,'partenaire finance officiel (09/2026)',(-0.75,-1.35,'right'),None),
 ( 2,'Aston Villa','Ebury',-1.89,52.51,ORANGE,'Official FX Partner, CFO témoigne',(-0.95,0.95,'right'),None),
 ( 3,'Manchester City','Corpay',-2.20,53.48,ORANGE,'Official FX Partner (08/2024)',(-0.95,0.55,'right'),None),
 ( 4,'Newcastle','Corpay',-1.62,54.98,ORANGE,'Official FX Partner pluriannuel (10/2026)',(0.95,-0.30,'left'),None),
 ( 5,'Bird','Airwallex',4.90,52.37,RED,'remplace >20 banques (switch explicite)',(0.95,-0.85,'left'),None),
 ( 6,'Profine','Kantox',7.15,50.81,GREY,'SAP intégré ; frais FX −60 %',(0.95,0.30,'left'),None),
 ( 7,'AERTiCKET','Kantox',13.40,52.52,GREY,'micro-hedging + API ERP',(0.75,0.60,'left'),None),
 ( 8,'Bank WIR','Amnis',7.59,47.56,BLUE,'banque régionale — canal blanc',(0.95,-0.30,'left'),None),
 ( 9,'FIG','Corpay',6.63,46.52,ORANGE,'Official FX Payments Supplier (02/2025)',(-0.95,-0.45,'right'),None),
 (10,'CD Leganés','Ebury',-3.76,40.33,ORANGE,'« coûts réduits de façon tangible » (DF)',(0.65,0.65,'left'),None),
 (11,'Dulevo','Kantox',10.33,44.80,GREY,'micro-hedging USD via ERP',(0.85,-0.55,'left'),None),
 (12,'TransferGalaxy','Corpay',18.07,59.33,GREY,'comptes multidevises nominatifs',(0.85,-0.15,'left'),None),
]
WORLD=[
 (13,'Nubank','Wise',-46.63,-23.55,BLUE,'',(1.6,-2.4,'left'),(1.6,-2.4,'left')),
 (14,'Dalstrong','Airwallex',-79.38,43.65,GREY,'',(2.0,0.9,'left'),(2.0,0.9,'left')),
 (15,'Univ. of Denver','Convera',-104.99,39.74,GREY,'',(1.8,-2.6,'left'),(1.8,-2.6,'left')),
 (16,'Betcris','Convera',-84.09,9.93,GREY,'',(1.8,-0.9,'left'),(1.8,-0.9,'left')),
 (17,'ZA Bank','Wise',114.17,22.32,BLUE,'',(0.8,2.6,'left'),(0.8,2.6,'left')),
 (18,'SHEIN','Airwallex',103.85,1.29,GREY,'',(2.1,0.5,'left'),(2.1,0.5,'left')),
 (19,'Bank Mandiri','Wise',106.85,-6.21,BLUE,'',(0.9,-3.0,'left'),(0.9,-3.0,'left')),
 (20,'Qantas','Airwallex',151.21,-33.87,GREY,'',(-1.6,-1.6,'right'),(-1.6,-1.6,'right')),
]
N=len(EU)+len(WORLD)

fig=plt.figure(figsize=(16.54,11.69), dpi=150)
fig.text(0.008,0.978,"MARCHÉ FX MONDIAL — RELATIONS CLIENTS PUBLIQUEMENT PROUVÉES (HORS FRANCE)",fontsize=13.5,fontweight='bold')
fig.text(0.008,0.9545,"20 relations · sources publiques (CP, presse, case studies) avec URL + citation + date au classeur ORBIS, feuille CAS-MONDE · 21/10/2026",
         fontsize=8.6,color='#475263')

# ---------- carte monde (dots numérotés + labels hors Europe) ----------
ax=fig.add_axes([0.005,0.405,0.630,0.520])
def draw_countries(a):
    for feat in GEO['features']:
        if feat['properties'].get('name')=='Antarctica': continue
        geom=feat['geometry']; polys=geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
        for poly in polys:
            for ring in poly[:1]:
                xs=[pt[0]*KX for pt in ring]; ys=[pt[1] for pt in ring]
                a.fill(xs,ys,color='#e9eef5',edgecolor='white',linewidth=0.35,zorder=1)
draw_countries(ax)
ax.set_xlim(-106*KX,155*KX); ax.set_ylim(-42,68); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(mpatches.Rectangle((-11.5*KX,36),(26.5+11.5)*KX,27.5,fill=False,edgecolor='#7d8aa0',
             linewidth=1.1,linestyle=(0,(4,3)),zorder=4))
ax.text(-11.5*KX,64.6,"EUROPE — 12 relations → zoom en bas à gauche",fontsize=8.2,color='#55606e',style='italic',path_effects=HALO)
for n,cli,prov,lon,lat,c,note,_,_ in EU:
    x,y=lon*KX,lat
    ax.scatter([x],[y],s=120,facecolor=c,edgecolor='white',linewidth=1.1,zorder=5)
    ax.text(x,y,str(n),fontsize=5.6,color='white',ha='center',va='center',zorder=6,fontweight='bold')
for n,cli,prov,lon,lat,c,note,_,(dx,dy,ha) in WORLD:
    x,y=lon*KX,lat
    ax.scatter([x],[y],s=150,facecolor=c,edgecolor='white',linewidth=1.3,zorder=5)
    ax.text(x,y,str(n),fontsize=6.8,color='white',ha='center',va='center',zorder=6,fontweight='bold')
    ax.text(x+dx,y+dy,f"{n} {cli}",fontsize=8.6,fontweight='bold',color='#232a31',ha=ha,va='center',zorder=6,path_effects=HALO)
    ax.text(x+dx,y+dy-1.7,f"→ {prov}",fontsize=7.6,color=c if c!=GREY else '#5d646b',ha=ha,va='center',zorder=6,fontweight='bold',path_effects=HALO)

# ---------- ZOOM EUROPE ----------
zx=fig.add_axes([0.010,0.012,0.460,0.430])
draw_countries(zx)
zx.set_xlim(-12.0*KX,27.0*KX); zx.set_ylim(35.0,63.0); zx.set_aspect('equal')
for spine in zx.spines.values(): spine.set_edgecolor('#b7c2cf'); spine.set_linewidth(1.2)
zx.set_xticks([]); zx.set_yticks([])
zx.text(-11.0*KX,61.2,"ZOOM EUROPE — 12 des 20 relations",fontsize=10.5,fontweight='bold',path_effects=HALO)
zx.text(-11.0*KX,59.7,"même numérotation que la carte monde",fontsize=7.6,color='#55606e',style='italic',path_effects=HALO)
for n,cli,prov,lon,lat,c,note,(dx,dy,ha),_ in EU:
    x,y=lon*KX,lat
    zx.scatter([x],[y],s=190,facecolor=c,edgecolor='white',linewidth=1.4,zorder=5)
    zx.text(x,y,str(n),fontsize=7.0,color='white',ha='center',va='center',zorder=6,fontweight='bold')
    zx.text(x+dx,y+dy,f"{n} {cli} → {prov}",fontsize=8.6,fontweight='bold',color='#232a31',ha=ha,va='center',zorder=6,path_effects=HALO)
    zx.text(x+dx,y+dy-1.25,note,fontsize=7.3,color='#55606e',ha=ha,va='center',zorder=6,path_effects=HALO)

# ---------- panneau droit ----------
rx=0.648
fig.text(rx,0.978,"« QUI EST CLIENT DE QUI » — MONDE hors France",fontsize=13,fontweight='bold')
fig.text(rx,0.9565,"Pendant international de la carte France (N=15) — même méthode : URL + citation + date.",fontsize=8.7,color='#444')
fig.text(rx,0.9405,"Base = preuves publiques nommées ; absence de preuve ≠ absence de prestataire.",fontsize=8.7,color='#444')

fig.text(rx,0.913,"PARTS PUBLIQUES — MONDE (modèle)",fontsize=12,fontweight='bold')
tbl=[('Airwallex (Arsenal · Bird · Dalstrong · SHEIN · Qantas)','5 / 20','25 %'),
     ('Corpay (Man City · Newcastle · FIG · TransferGalaxy)','4 / 20','20 %'),
     ('Wise Platform (Nubank · ZA Bank · Bank Mandiri)','3 / 20','15 %'),
     ('Kantox-BNP Paribas (Profine · AERTiCKET · Dulevo)','3 / 20','15 %'),
     ('Ebury (Aston Villa · CD Leganés)','2 / 20','10 %'),
     ('Convera ex-WUBS (Univ. Denver · Betcris)','2 / 20','10 %'),
     ('Amnis (Bank WIR, canal banque régionale CH)','1 / 20','5 %')]
ay=0.892
for a,b,c in tbl:
    fig.text(rx,ay,a,fontsize=9.0); fig.text(rx+0.262,ay,b,fontsize=9.0,fontweight='bold')
    fig.text(rx+0.312,ay,c,fontsize=9.0,fontweight='bold',color='#0e7a3d')
    ay-=0.0185
fig.text(rx,ay,"0 % publié ≠ 0 % réel : J.P. Morgan (best FX payments 2026),",fontsize=8.2,style='italic',color='#666'); ay-=0.0165
fig.text(rx,ay,"Barclays (sales/forwards/options 2025), HSBC (prime brokerage, NDFs 2026)",fontsize=8.2,style='italic',color='#666'); ay-=0.0165
fig.text(rx,ay,"— primés Euromoney, zéro client FX nominatif publié.",fontsize=8.2,style='italic',color='#666'); ay-=0.024

fig.text(rx,ay,"PROFIL TYPE DU CLIENT MONDE (d’après les 20 cas)",fontsize=12,fontweight='bold'); ay-=0.021
prof=[('Airwallex','scale-ups tech/e-commerce APAC→monde ; sport (Arsenal).'),
      ('Corpay','sport mondial = visibilité (2× Prem. League, FIG) ; nordiques.'),
      ('Wise Platform','CANAL banques API — Nubank 100 M · Mandiri 23 M util. · ZA.'),
      ('Kantox-BNPP','midcaps industrielles euro connectées ERP/SAP (DE ×2, IT).'),
      ('Ebury · Convera · Amnis','clubs sport EU · éducation US (Denver) · banque CH (WIR).')]
for a,b in prof:
    fig.text(rx,ay,a,fontsize=8.8,fontweight='bold')
    fig.text(rx+0.112,ay,b,fontsize=8.0,va='center')
    ay-=0.0195
ay-=0.008

fig.text(rx,ay,"PÉRIMÈTRE DE CONNAISSANCE",fontsize=12,fontweight='bold'); ay-=0.024
fig.text(rx,ay,"20 relations prouvées hors France — 35 au total avec la France.",fontsize=9.8,fontweight='bold',color='#1F3864'); ay-=0.0185
fig.text(rx,ay,"La carte mesure la VISIBILITÉ PUBLIQUE (qui publie ses cas), pas la part réelle :",fontsize=8.3,color='#444'); ay-=0.0160
fig.text(rx,ay,"les banques traditionnelles servent le FX mid-market sans le publier.",fontsize=8.3,color='#444'); ay-=0.025

fig.text(rx,ay,"LÉGENDE DES PINS",fontsize=12,fontweight='bold'); ay-=0.023
leg=[(RED,'CHANGEMENT FORT (explicite)','n°5 Bird → Airwallex : remplace plus de 20 banques mondiales'),
     (ORANGE,'ADOPTION / PARTENARIAT AFFICHÉ','n°1 2 3 4 9 10 — sport mondial & européen (deals FX officiels datés)'),
     (GREY,'CITATION CLIENT (case study)','n°6 7 11 12 14 15 16 18 20 — témoignages nommés, sans bascule'),
     (BLUE,'CANAL BANCAIRE (API / white-label)','n°8 13 17 19 — la fintech sert les clients de la banque')]
for c,t,d in leg:
    fig.text(rx,ay,'■',fontsize=10.5,color=c); fig.text(rx+0.013,ay,t,fontsize=8.8,fontweight='bold')
    fig.text(rx+0.013,ay-0.0162,d,fontsize=8.1,color='#333')
    ay-=0.0370
ay-=0.002
fig.text(rx,ay,"France → carte dédiée (N=15 : BNPP-Kantox 46,7 % · iBanFirst 33,3 %).",fontsize=8.2,style='italic',color='#666'); ay-=0.0165
fig.text(rx,ay,"iBanFirst : aucun cas client hors France publié à ce stade de la recherche.",fontsize=8.2,style='italic',color='#666')

fig.patches.append(mpatches.Rectangle((rx-0.008,0.020),0.344,0.128,transform=fig.transFigure,
                   facecolor='#fdf1f0',edgecolor=RED,linewidth=2.0,zorder=20))
fig.text(rx+0.004,0.133,"DISCLAIMER — À LIRE AVANT TOUTE UTILISATION",fontsize=10,fontweight='bold',color=RED,zorder=21)
fig.text(rx+0.004,0.115,"Hypothèse volontairement irréaliste : « données publiques = 100 % des clients ».",fontsize=8.6,zorder=21)
fig.text(rx+0.004,0.098,"Les % mesurent la VISIBILITÉ MARKETING (qui publie ses cas), pas des parts de marché.",fontsize=8.6,zorder=21)
fig.text(rx+0.004,0.081,"Clubs sportifs = contrats FX réels mais deals groupés sponsoring — profil ≠ PME.",fontsize=8.6,zorder=21)
fig.text(rx+0.004,0.064,"0 % publié peut masquer une position réelle majeure (banques non-publiantes).",fontsize=8.6,zorder=21)
fig.text(rx+0.004,0.047,"Témoignages clients = tenu du discours fournisseur.",fontsize=8.6,zorder=21)
fig.text(rx+0.004,0.030,"À brandir en entretien UNIQUEMENT avec ce cadre dit à voix haute.",fontsize=8.6,fontweight='bold',color=RED,zorder=21)

plt.savefig('candidatures/CARTE-2026-10-21-monde-attributions-FX.png')
plt.savefig('candidatures/CARTE-2026-10-21-monde-attributions-FX.pdf')
print('carte monde v2 écrite — N =',N)
