# -*- coding: utf-8 -*-
"""
05_carte_modele_parts.py — MODÈLE COMPTABLE SPÉCULATIF (demande utilisateur du 21/10)
Hypothèse volontairement irréaliste, posée par le commanditaire :
  (H1) les relations prestataire↔client publiquement documentées = 100 % des clients ;
  (H2 « silence = vierge » ÉCARTÉE le 21/10 : cadrage rejeté — on présente le su, pas l'insu.)
Sorties : candidatures/CARTE-2026-10-21-modele-parts-FX.pdf + .png
Périphérie inchangée : carte = exercice pédagogique de lecture en sales FX.
"""
import json, warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as peff
from matplotlib.collections import PolyCollection

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
rgeo=json.load(open('/tmp/france-geojson-master/regions-version-simplifiee.geojson'))
dgeo=json.load(open('/tmp/france-geojson-master/departements-version-simplifiee.geojson'))

# ---------- modèle comptable ----------
# Base stricte : 7 relations clientes FR publiquement nommées
#   Kantox (filiale BNPP 07/2023) : Théa, Fareva, HMY, AnimalBox = 4
#   iBanFirst : Guard Industrie, Mobile Club, Bensimon = 3
#   + extensions v2 (VeryChic, Aurlane, Snetor, Chrono Carpe) et v3 : GT Company → Moneycorp
#   + v4 : OL + Stade de Reims → Ebury (contrats FX clubs affichés 2025) ; TFC/OM exclus (hors univers Orbis)
STRICT = {'Kantox (BNP Paribas)':4,'iBanFirst':3}
ELARGI = {'Groupe BNP Paribas (Kantox 4 + direct 1)':5,'iBanFirst':3}
NAMED_FR = 15                      # entreprises FR distinctes nommées publiquement (comptées dans le modèle)
ELIGIBLES = 64646 + 2316251        # univers Orbis ≥5M€ + requête <5M€
PCT_VIERGE = (1 - NAMED_FR/ELIGIBLES)*100

RED='#c0392b'; ORANGE='#e67e22'; GREY='#8a939b'; BLUE='#2456a0'
V_IDF='#0e7a3d'; V_SUD='#d98e04'; V_NEUTRE='#e9edf2'
SUD={'75','76','93'}
RN={'11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Franche-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne','75':'Nouvelle-Aquitaine',
 '76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"Provence-Alpes-Côte d'Azur",'94':'Corse'}
RV={f['properties']['code']:f for f in rgeo['features']}
def region_verts(code):
    gg=RV[code]['geometry']; polys=gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]
    return [np.array(p[0]) for p in polys if p and p[0]]

# pins: (num, lon, lat, couleur, texte court)
PX,PY=2.35,48.86
PINS=[
 (1, PX+0.75,PY+0.95, RED,   'Bensimon'),
 (2, PX+1.10,PY+0.70, RED,   'Amaris'),
 (3, PX+2.10,PY+0.85, ORANGE,'Mobile Club'),
 (4, PX+1.15,PY+0.08, GREY,  'AnimalBox'),
 (5, PX+1.10,PY-0.50, BLUE,  'LBP×Ebury'),
 (6, PX+0.72,PY-0.60, BLUE,  'EH×iBanFirst'),
 (7, PX-0.60,PY-0.95, BLUE,  'Kantox↦BNPP'),
 (8, 3.087+0.30,45.777-0.15, ORANGE,'Théa (Clermont-F.)'),
 (9, 4.94+0.30,45.70+0.12,  GREY,  'Guard (Lyon)'),
 (10,4.833+0.30,45.067-0.10,GREY,  'Fareva (Tournon)'),
 (11,1.065-0.30,47.79+0.20, GREY,  'HMY (Vendôme)'),
 (12,PX+1.55,PY+1.25, GREY,  'VeryChic'),
 (13,PX-0.50,PY+1.40, GREY,  'Aurlane'),
 (14,PX-1.60,PY+0.90, GREY,  'Snetor'),
 (15,PX+0.45,PY-0.28, GREY,  'GT Company'),
 (16,4.95,45.32,    ORANGE,'OL'),
 (17,4.03,49.26,    ORANGE,'Stade de Reims'),
]

fig=plt.figure(figsize=(16.54,11.69), dpi=170)
ax=fig.add_axes([0.005,0.03,0.565,0.90])
for code in RN:
    fc=V_IDF if code=='11' else (V_SUD if code in SUD else V_NEUTRE)
    ec='#9aa2ab'
    ax.add_collection(PolyCollection(region_verts(code),facecolor=fc,edgecolor=ec,
        linewidth=1.4 if code=='11' or code in SUD else 0.7,zorder=2,alpha=0.85))
dv=[]
for f in dgeo['features']:
    gg=f['geometry']; polys=gg['coordinates'] if gg['type']=='MultiPolygon' else [gg['coordinates']]
    dv+=[np.array(p[0]) for p in polys if p and p[0]]
ax.add_collection(PolyCollection(dv,facecolor='none',edgecolor='white',linewidth=0.3,zorder=3))
for num,x,y,c,_ in PINS:
    ax.scatter([x],[y],s=560,facecolor=c,edgecolor='white',linewidth=1.8,zorder=6)
    ax.text(x,y,str(num),color='white',fontsize=10.5,fontweight='bold',ha='center',va='center',zorder=7)
    if c!=BLUE:
        ax.text(x+0.12,y-0.02,_,fontsize=7.3,color='#333',zorder=7,
                path_effects=[peff.withStroke(linewidth=2,foreground='white',alpha=0.9)])
ax.scatter([PX],[PY],s=200,facecolor='#222',edgecolor='white',linewidth=1.4,zorder=5,marker='*')
ax.text(PX-0.72,PY+0.40,'Paris',fontsize=9.5,fontweight='bold',
        path_effects=[peff.withStroke(linewidth=2.4,foreground='white',alpha=0.9)])
ax.set_xlim(-5.6,10.2); ax.set_ylim(41.0,51.6); ax.set_aspect('equal'); ax.axis('off')

# ---------- panneau droit ----------
rx=0.585
fig.text(rx,0.955,"« QUI EST CLIENT DE QUI » — MODÈLE COMPTABLE",fontsize=15.5,fontweight='bold')
fig.text(rx,0.934,"Hypothèses (demandées) : H1 = cas publiquement nommés = 100 % des clients",
         fontsize=8.8,color='#444')
fig.text(rx,0.919,"Base = preuves publiques nommées ; absence de preuve ≠ absence de prestataire.",fontsize=8.8,color='#444')

fig.text(rx,0.893,"PARTS PUBLIQUES (modèle)",fontsize=12,fontweight='bold')
tbl=[('Groupe BNP Paribas (Kantox 6 + Amaris 1)','7 / 15','46,7 %'),
     ('iBanFirst (5 clients FR nommés)','5 / 15','33,3 %'),
     ('Ebury (Santander) — OL + Stade de Reims (+ canaux)','2 / 15','13,3 %'),
     ('Moneycorp (GT Company — cas bilatéral)','1 / 15','6,7 %'),
     ('Corpay ex-AFEX (TFC nommé, hors univers)','0 / 15','0 % *'),
     ('J.P. Morgan · Barclays · HSBC · SG · CA CIB','0 FR publié','0 % *'),
     ('Amnis · Wise · OFX · Nium · Convera · autres','0 FR publié','0 % *')]
ay=0.870
for a,b,c in tbl:
    fig.text(rx,ay,a,fontsize=9.6)
    fig.text(rx+0.255,ay,b,fontsize=9.6,fontweight='bold')
    fig.text(rx+0.315,ay,c,fontsize=9.6,fontweight='bold',color=('#0e7a3d' if '%' in c and c!='0 % *' else '#a33'))
    ay-=0.020
ay-=0.004
fig.text(rx,ay,"* 0 % publié ≠ 0 % réel — c'est exactement le piège du modèle (voir cadre rouge).",
        fontsize=8.4,style='italic',color='#666')
fig.text(rx,ay-0.022,"Base stricte sans Amaris : BNPP-Kantox 42,9 % · iBanFirst 35,7 % · Ebury 14,3 % · Moneycorp 7,1 % (14 rel.).",
        fontsize=8.4,style='italic',color='#666')

fig.text(rx,0.688,"PROFIL TYPE DU CLIENT (d'après les cas)",fontsize=12,fontweight='bold')
prof=[('BNP Paribas / Kantox','ETI→grand groupe (3,8–862 M$) ; trésorerie assise ; hedging automatisé ; multi-pays (Amaris 35 pays).'),
      ('iBanFirst','TPE/PME import/retail (achats Asie/UK) ; le public déclaré: 500 k€–50 M€ de flux/an ; seuil 200 k€/an.'),
      ('Ebury','PME 1–20 M€ ; canaux : banque magasin (LBP), courtier white-label, clubs L1 (OL, Reims).'),
      ('J.P. Morgan / Barclays','Grands comptes globalisés primés aux awards — cas confirmés hors FR (NTT DATA, Honeywell, L\u2019Oréal BR).'),
      ('Banques FR (SG, CA CIB, HSBC…)','Aucun cas FX mid-market nominatif publié en FR — présence réelle connue, preuve publique absente.')]
ay=0.667
for a,b in prof:
    fig.text(rx,ay,a,fontsize=9.6,fontweight='bold')
    fig.text(rx+0.185,ay,b,fontsize=9.2,va='top',wrap=True)
    ay-=0.041

fig.text(rx,0.472,"PÉRIMÈTRE DE CONNAISSANCE",fontsize=12,fontweight='bold')
fig.text(rx,0.448,f"{NAMED_FR} relations client→prestataire prouvées",fontsize=15,fontweight='bold',color='#1F3864')
fig.text(rx,0.426,"(noms + sources publiques vérifiables — feuilles URL/ATTRIBUTIONS du classeur)",fontsize=8.4,color='#666')
fig.text(rx,0.406,"Marché adressable : 64 646 PME/ETI ≥ 5 M€ (Orbis 20-21/10) — la carte mesure la",fontsize=8.8,color='#444')
fig.text(rx,0.391,"VISIBILITÉ PUBLIQUE des fintech, pas la part réelle (banques non-publiantes).",fontsize=8.8,color='#444')

fig.text(rx,0.358,"LÉGENDE DES PINS",fontsize=12,fontweight='bold')
leg=[(RED,'CHANGEMENT FORT (explicite)',['(1) Bensimon → iBanFirst (pool bancaire, 2019)  (2) Amaris → BNP Paribas unique 35 pays (ASA 2017)']),
     (ORANGE,'ADOPTION / BASCULE',['(3) Mobile Club → iBanFirst (frais banques cités, 2025) · (8) Théa → Kantox algo (manuel abandonné)','(16) OL · (17) Stade de Reims → Ebury : contrats FX clubs affichés (2025), deals groupés sponsoring']),
     (GREY,'Citation client sans signal de changement',['(4) AnimalBox (9) Guard (10) Fareva (11) HMY (12) VeryChic (14) Snetor → Kantox · (13) Aurlane → iBanFirst','(15) GT Company → Moneycorp — cas bilatéral : le client cite lui-même son prestataire']),
     (BLUE,'Événement structurel (canal / rachat)',['(5) LBP × Ebury (2021) · (6) Euler Hermes × iBanFirst (2022) · (7) Kantox rachetée par BNP Paribas (2023)'])]
ay=0.334
for c,t,ds in leg:
    fig.text(rx,ay,'■',fontsize=11,color=c)
    fig.text(rx+0.013,ay,t,fontsize=9.4,fontweight='bold')
    for i,d in enumerate(ds):
        fig.text(rx+0.013,ay-0.0175-0.0135*i,d,fontsize=8.4,color='#333')
    ay-=0.0435+0.0135*(len(ds)-1)

# cadre disclaimer rouge
import matplotlib.patches as mpatches
fig.patches.append(mpatches.Rectangle((rx-0.008,0.020),0.402,0.112,transform=fig.transFigure,
                   facecolor='#fdf1f0',edgecolor=RED,linewidth=2.2,zorder=20))
fig.text(rx+0.004,0.105,"DISCLAIMER — À LIRE AVANT TOUTE UTILISATION",fontsize=10.5,fontweight='bold',color=RED,zorder=21)
disc=["Hypothèse volontairement irréaliste, fournie par le commanditaire : « données publiques = 100 % ».",
      "Les % mesurent la VISIBILITÉ MARKETING des prestataires (qui publie ses cas), pas des parts de marché.",
      "Les banques communiquent peu leurs clients mid-market : 0 % publié peut masquer une position réelle majeure.",
      "À brandir en entretien UNIQUEMENT avec ce cadre dit à voix haute."]
dy=0.086
for dl in disc:
    fig.text(rx+0.004,dy,dl,fontsize=8.4,color='#5a1a12',zorder=21)
    dy-=0.0168

plt.savefig('candidatures/CARTE-2026-10-21-modele-parts-FX.pdf')
plt.savefig('candidatures/CARTE-2026-10-21-modele-parts-FX.png')
print('carte modèle écrite — connaissance =', NAMED_FR, 'relations prouvées')
