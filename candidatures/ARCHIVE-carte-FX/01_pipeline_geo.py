# -*- coding: utf-8 -*-
"""
01_pipeline_geo.py — construit /tmp/univ_xy.pkl : univers Orbis 64 646 (>=5 M€ FR actives)
enrichi région 2016 / département / commune INSEE / lon-lat, classes FX, tranches CA.
Entrées à placer dans /tmp (voir README.md) : final_basez.xlsb, exp1950.xlsx, o3.xlsx,
decoupage-administratif-master/ (Etalab), france-geojson-master/communes-version-simplifiee.geojson
Exécution : PYTHONPATH=/tmp/pydeps python3 01_pipeline_geo.py   (~1 min)
"""
import json, zipfile, unicodedata, re, warnings
warnings.filterwarnings('ignore')
import pandas as pd, numpy as np
MIN='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts><fills count="1"><fill><patternFill patternType="none"/></fill></fills><borders count="1"><border/></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs></styleSheet>'
for src,dst in [('/tmp/exp1950.xlsx','/tmp/exp1950f.xlsx'),('/tmp/o3.xlsx','/tmp/o3f.xlsx')]:
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as zout:
        for it in zin.namelist():
            zout.writestr(it, MIN if it=='xl/styles.xml' else zin.read(it))
REGIONS={'01':'Guadeloupe','02':'Martinique','03':'Guyane','04':'La Réunion','06':'Mayotte',
 '11':'Île-de-France','24':'Centre-Val de Loire','27':'Bourgogne-Franche-Comté','28':'Normandie',
 '32':'Hauts-de-France','44':'Grand Est','52':'Pays de la Loire','53':'Bretagne',
 '75':'Nouvelle-Aquitaine','76':'Occitanie','84':'Auvergne-Rhône-Alpes','93':"Provence-Alpes-Côte d'Azur",'94':'Corse','COM':'Outre-mer (COM)'}
METRO={'11','24','27','28','32','44','52','53','75','76','84','93','94'}
OLD2NEW={'ALSACE':'44','AQUITAINE':'75','AUVERGNE':'84','BASSE NORMANDIE':'28','BOURGOGNE':'27','BRETAGNE':'53','CENTRE':'24','CHAMPAGNE ARDENNE':'44','CORSE':'94','FRANCHE COMTE':'27','HAUTE NORMANDIE':'28','ILE DE FRANCE':'11','LANGUEDOC ROUSSILLON':'76','LIMOUSIN':'75','LORRAINE':'44','MIDI PYRENEES':'76','NORD PAS DE CALAIS':'32',"PROVENCE ALPES COTE D AZUR":'93','PACA':'93','PAYS DE LA LOIRE':'52','PICARDIE':'32','POITOU CHARENTES':'75','RHONE ALPES':'84','GUADELOUPE':'01','MARTINIQUE':'02','GUYANE':'03','LA REUNION':'04','MAYOTTE':'06'}
ALIAS={'OULLINS':'69','ERAGNY':'95','CHERVES RICHEMONT':'16','SAUZE VAUSSAIS':'79','OISSEL':'76','HESDIN':'62','LOUHANS':'71','CUGAND':'85','ETAUX':'74','LE MERLERAULT':'61','MAY SUR ORNE':'14','JUGON LES LACS COMMUNE NOUVELLE':'22','NEUSSARGUES EN PINATELLE':'15','LAMBRES':'62','BIANS LES USIERS':'25','CRANSAC':'12','THOIRAS':'30','ROUGEMONTIERS':'27','ST YBARD':'19','ST POMPONT':'24','PLUDUNO':'22','STE HERMINE':'85','PAPEETE':'COM','PAPEETE TAHITI':'COM','PUNAAUIA':'COM','NOUMEA':'COM','NOUMEA NOUVELLE CALEDONIE':'COM','75116 PARIS':'75','ALICANTE VALENCIAN COMMUNITY':'ETR'}
def norm(s):
    if s is None or isinstance(s,float): return ''
    s=str(s).strip()
    if not s or s.lower()=='nan': return ''
    s=s.replace('Œ','OE').replace('œ','oe').replace('Æ','AE').replace('æ','ae')
    s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.upper(); s=re.sub(r"[’'\-]",' ',s); s=re.sub(r'[^A-Z0-9 ]',' ',s)
    s=re.sub(r'\bCEDEX\b.*$','',s); return re.sub(r'\s+',' ',s).strip()
SRC='/tmp/decoupage-administratif-master/sources/'
from collections import defaultdict
cog=pd.read_csv(SRC+'communes.csv',dtype=str)
cog=cog[cog['TYPECOM'].isin(['COM','ARM'])]
pop=pd.read_csv(SRC+'donnees_communes.csv',sep=';',dtype=str)
popd={'75056':2113705,'69123':522250,'13055':870731}
for _,r in pop.iterrows():
    try: popd[r['COM']]=int(float(r['PTOT']))
    except Exception: pass
cog['pop']=cog['COM'].map(popd).fillna(0).astype(int)
cand=defaultdict(list)
for _,r in cog.iterrows():
    for k in {norm(r['LIBELLE']),norm(r['NCCENR']),norm(r['NCC'])}:
        if k: cand[k].append((r['pop'],r['REG'],r['DEP'],r['COM']))
geo={}
for k,lst in cand.items():
    lst.sort(reverse=True); ba=lst[0]
    metro=[x for x in lst if x[1] in METRO]
    pool=metro if metro and metro[0][0]>=0.05*max(ba[0],1) else lst
    geo[k]=pool[0]
drops=pd.read_csv(SRC+'departements.csv',dtype=str).set_index('DEP')
DEP2REG=drops['REG'].to_dict()
PLM={'PARIS':(2113705,'11','75','75056'),'LYON':(522250,'84','69','69123'),'MARSEILLE':(870731,'93','13','13055')}
re_plm=re.compile(r'^(PARIS|LYON|MARSEILLE)\s+(0?\d{1,2})(E)?( ARRONDISSEMENT)?$')
def expand_st(v):
    v=re.sub(r'\bST\b','SAINT',v); return re.sub(r'\bSTE\b','SAINTE',v)
def lookup(vn):
    if not vn: return None
    if vn in geo: return geo[vn]
    m=re_plm.match(vn)
    if m: return PLM[m.group(1)]
    v2=expand_st(vn)
    if v2 in geo: return geo[v2]
    m=re_plm.match(v2)
    if m: return PLM[m.group(1)]
    w=vn.split()
    while len(w)>1:
        w=w[:-1]; k=' '.join(w)
        if k in geo and geo[k][0]>=3000: return geo[k]
        k2=expand_st(k)
        if k2 in geo and geo[k2][0]>=3000: return geo[k2]
    return None
df=pd.read_excel('/tmp/final_basez.xlsb',sheet_name='Résultats',engine='pyxlsb')
c=df.columns
d=df[df[c[1]].notna()].copy().reset_index(drop=True)
d.columns=['idx','nom','inactive','quoted','branch','owndata','woco','iso','nace','consol','annee','ca_meur','effectifs','web','web1','cp_add','region_add','tel_add','email_dirig','maj_adresse','ville','ville_add']
d['ville_n']=d['ville'].map(norm); d['nom_n']=d['nom'].map(norm)
res=d['ville_n'].map(lookup)
d['reg_code']=res.map(lambda x:x[1] if x else None)
d['dep']=res.map(lambda x:x[2] if x else None)
d['com']=res.map(lambda x:x[3] if x else None)
malias=d['reg_code'].isna() & d['ville_n'].ne('')
for ville,dep in ALIAS.items():
    sel=malias & (d['ville_n']==ville)
    if dep in ('ETR','COM'): d.loc[sel,'reg_code']=dep
    else: d.loc[sel,'reg_code']=DEP2REG.get(dep); d.loc[sel,'dep']=dep
print('BASEZ:', d['reg_code'].notna().sum(),'/',len(d))
CORE=set(range(1,4))|set(range(5,34))|{46,51,52}|set(range(58,64))|set(range(69,76))|{77,79}
CONT=set(range(35,40))|set(range(41,44))|{45,47,49,50,55,56,65,66,80,81,82}
def classe(div):
    if div in CORE: return 'CŒUR'
    if div in CONT: return 'CONTINGENT'
    return 'DOMESTIQUE'
o3=pd.read_excel('/tmp/o3f.xlsx',sheet_name='Résultats')
o3['nom_n']=o3.iloc[:,1].map(norm)
NEW_NORM={}
for k,v in REGIONS.items():
    n=norm(v)
    if n: NEW_NORM[n]=k
def reg_from_o3(v):
    n=norm(v)
    if not n: return None
    if n in NEW_NORM: return NEW_NORM[n]
    if n in OLD2NEW: return OLD2NEW[n]
    if n.isdigit() and n.zfill(2) in REGIONS: return n.zfill(2)
    return None
o3['reg_code']=o3.iloc[:,14].map(reg_from_o3)
m3=o3['reg_code'].isna()
o3.loc[m3,'reg_code']=o3.loc[m3,o3.columns[15]].map(lambda v:(lookup(norm(v)) or (0,None,None,None))[1])
def com_of(v):
    r=lookup(norm(v)); return r[3] if r else None
o3['com3']=o3.iloc[:,15].map(com_of)
print('o3:', o3['reg_code'].notna().sum(),'/',len(o3))
u=pd.read_excel('/tmp/exp1950f.xlsx',sheet_name='Résultats')
u=u[u.iloc[:,1].notna()].copy()
u.columns=['idx','nom','inactive','quoted','branch','owndata','woco','iso','nace','consol','annee','ca_kusd','effectifs']
u['nom_n']=u['nom'].map(norm)
u['ca_kusd']=pd.to_numeric(u['ca_kusd'],errors='coerce')
u['effectifs']=pd.to_numeric(u['effectifs'],errors='coerce')
u['nace']=pd.to_numeric(u['nace'],errors='coerce')
u['div']=(u['nace'].fillna(0).astype(int))//100
u['classe']=u['div'].map(classe)
u['fin']=u['div'].isin([64,65,66])
def bande(k):
    if not np.isfinite(k): return ''
    if k<25000: return '5-25 M$'
    if k<100000: return '25-100 M$'
    if k<250000: return '100-250 M$'
    if k<1000000: return '250 M$-1 Md$'
    return '>1 Md$'
u['bande']=u['ca_kusd'].map(bande)
dd=d.sort_values(['nom_n','ca_meur'],ascending=[True,False]).drop_duplicates('nom_n').set_index('nom_n')
u['reg_code']=u['nom_n'].map(dd['reg_code'])
u['dep']=u['nom_n'].map(dd['dep'])
u['com']=u['nom_n'].map(dd['com'])
u['ville']=u['nom_n'].map(dd['ville'])
u['src_geo']=np.where(u['reg_code'].notna(),'BASEZ',None)
o3d=o3.sort_values(['nom_n']).drop_duplicates('nom_n').set_index('nom_n')
mu=u['reg_code'].isna()
u.loc[mu,'reg_code']=u.loc[mu,'nom_n'].map(o3d['reg_code'])
u.loc[mu & u['reg_code'].notna(),'src_geo']='o3'
mu2=u['com'].isna() & u['reg_code'].notna()
u.loc[mu2,'com']=u.loc[mu2,'nom_n'].map(o3d['com3'])
u.loc[u['ville'].isna(),'ville']=u.loc[u['ville'].isna(),'nom_n'].map(o3d.iloc[:,15])
def ring_centroid(ring):
    a=cx=cy=0.0
    for i in range(len(ring)-1):
        p0,p1=ring[i],ring[i+1]
        t=p0[0]*p1[1]-p1[0]*p0[1]; a+=t; cx+=(p0[0]+p1[0])*t; cy+=(p0[1]+p1[1])*t
    if abs(a)<1e-12:
        xs=[p[0] for p in ring]; ys=[p[1] for p in ring]
        return (sum(xs)/len(xs),sum(ys)/len(ys),0.0)
    a*=0.5; return cx/6/a, cy/6/a, abs(a)
gj=json.load(open('/tmp/france-geojson-master/communes-version-simplifiee.geojson'))
cent={}
for ft in gj['features']:
    code=ft['properties'].get('code'); g=ft.get('geometry')
    if not code or not g: continue
    polys=g.get('coordinates') if g.get('type')=='MultiPolygon' else [g.get('coordinates')]
    best=None
    for poly in polys or []:
        if not poly or not poly[0]: continue
        c0=ring_centroid(poly[0])
        if best is None or c0[2]>best[2]: best=c0
    if best: cent[code]=(best[0],best[1])
u['lon']=u['com'].map(lambda c0: cent.get(c0,(None,None))[0] if isinstance(c0,str) else None)
u['lat']=u['com'].map(lambda c0: cent.get(c0,(None,None))[1] if isinstance(c0,str) else None)
u.to_pickle('/tmp/univ_xy.pkl')
mes=int((u['reg_code'].notna()&~u['reg_code'].isin(['ETR'])).sum())
print('univers:',len(u),'| géo mesurée:',mes,f"({mes/len(u)*100:.1f}%)",'| coords:',int(u['lon'].notna().sum()))
