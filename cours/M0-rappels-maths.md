# M0 — Rappels maths pour le J1
### Annexe à lire *avant* (ou pendant) le cours J1 · dimanche 06/09/2026

> **À qui ça s'adresse.** À toi ce matin : les maths sont rouillées, et une
> ligne comme
> $\lim_{m\to\infty}(1+\frac{r}{m})^{mT}=e^{rT}$
> passe pour de la magie. Ce n'est pas de la magie, et ce n'est pas grave.
> **Être rouillé n'est pas être nul** : les outils reviennent en quelques
> heures si on les reprend dans le bon ordre.

**Ce que cette annexe n'est pas :** un cours de maths. Il n'y a **que** ce qui
sert au J1, rien de plus. Huit modules courts, chacun sur le même patron :

> **① À quoi ça sert dans J1** → **② Le rappel** → **③ Un exemple traité** →
> **④ 2 ou 3 micro-exercices** (corrigés en fin de module)

**Durée visée : 2 h**, crayon en main. Tu **fais** les exercices, tu ne les lis
pas. Un module = 12 à 15 min. Si un module passe tout seul, saute directement
à ses exercices et va au suivant.

> **~90 exercices corrigés**, organisés en séries :
> **Série A** = mécanique pure · **Série B** = application · **Série C/D** =
> sens financier et réflexe d'entretien.
> Les corrigés sont **repliés** (clique sur « Corrigés ») : cherche d'abord,
> ouvre ensuite. Un exercice regardé sans être cherché ne débloque aucun
> réflexe.

**Règle du jour :** on ne cherche pas la rigueur d'un cours de licence. On
cherche à **savoir manipuler**. Un trader n'a jamais démontré le théorème
central limite ; il sait quand s'en servir.

| Module | Sujet | Débloque dans J1 |
|---|---|---|
| M1 | Exponentielle et logarithme | forwards, actualisation, §1 entier |
| M2 | Dérivées : les 6 qui servent | grecs, §6 |
| M3 | **Approximations locales (DL)** | la formule de ta capture, l'approx ATM |
| M4 | **La limite $(1+r/m)^{mT}\to e^{rT}$, lentement** | §0.1 |
| M5 | Loi normale : $\phi$ et $N$ | $N(d_1)$, $N(d_2)$, §4–5 |
| M6 | Somme d'exponentielles / complétion du carré | la démo de BS, §4.4 |
| M7 | Log-normale et le fameux $-\sigma^2/2$ | §4.2 |
| M8 | Dérivées partielles et règle de la chaîne | Itô, l'EDP, §4.3 |

---

## M1 — Exponentielle et logarithme

### ① À quoi ça sert
**Partout.** $F=Se^{(r-q)T}$, l'actualisation $e^{-rT}$, le $\ln(S/K)$ de
$d_1$. Si ce module est solide, la moitié du J1 devient mécanique.

### ② Le rappel

$e\approx2{,}718$. L'exponentielle transforme **les additions en
multiplications**, le log fait l'inverse. C'est tout.

| Règle | Formule | En clair |
|---|---|---|
| Produit | $e^a\cdot e^b=e^{a+b}$ | on **additionne** les exposants |
| Quotient | $e^a/e^b=e^{a-b}$ | on soustrait |
| Inverse | $e^{-a}=1/e^{a}$ | le signe moins = diviser |
| Neutre | $e^0=1$ | taux nul ou durée nulle ⇒ rien ne bouge |
| Log du produit | $\ln(ab)=\ln a+\ln b$ | |
| Log du quotient | $\ln(a/b)=\ln a-\ln b$ | c'est le $\ln(S/K)$ de $d_1$ |
| Puissance | $\ln(a^n)=n\ln a$ | |
| Réciproques | $\ln(e^x)=x$ et $e^{\ln x}=x$ | l'un défait l'autre |

**Les trois seuls repères numériques à retenir :**
$$\ln 2\approx0{,}69\qquad e\approx2{,}72\qquad e^{0{,}05}\approx1{,}051$$

**Le réflexe finance :** pour de **petits** taux, $e^x\approx1+x$.
Donc $e^{0{,}03}\approx1{,}03$ : capitaliser à 3 % ≈ multiplier par 1,03.
C'est faux à 0,05 % près, et **ça suffit pour un ordre de grandeur en oral**.

### ③ Exemple traité
**Énoncé.** Actualiser 100 sur 6 mois à 4 % continu.
$$100\,e^{-0{,}04\times0{,}5}=100\,e^{-0{,}02}\approx100\times(1-0{,}02)=98$$
Valeur exacte : $\mathbf{98{,}0199}$. L'approximation donne 98 : **erreur de 2
centimes**, obtenue de tête. C'est exactement le nombre du TD, exercice 1.

### ④ Micro-exercices

**Série A — mécanique** (30 s chacun)

1. Simplifier $e^{rT}\cdot e^{-qT}$.
2. Simplifier $\dfrac{e^{0{,}06}}{e^{0{,}02}}$.
3. Simplifier $e^{\ln 7}$ puis $\ln(e^{-3})$.
4. Écrire $\ln\left(\dfrac{100}{105}\right)$ comme une différence de logs. Signe ? Pourquoi ?
5. Développer $\ln(S_0e^{rT})$.

**Série B — calcul mental** (approximation $e^x\approx1+x$)

6. $e^{-0{,}01}$ (vraie valeur $0{,}990050$).
7. $e^{0{,}03}$ (vraie valeur $1{,}030455$).
8. Actualiser $100$ sur 1 an à 6 % continu (vraie valeur $94{,}18$).

**Série C — réflexe finance**

9.  Si $F=Se^{(r-q)T}$, isoler $r-q$.
10. Un forward cote 2 % au-dessus du spot sur 6 mois. Que vaut $r-q$ ?
11. Combien de temps faut-il pour doubler un capital à 5 % continu ? *(Indice : $\ln2\approx0{,}69$.)*

<details><summary><b>Corrigés M1</b></summary>

**1.** $e^{rT}e^{-qT}=e^{rT-qT}=e^{(r-q)T}$. **C'est littéralement la formule
du forward** : capitaliser au taux $r$, « décapitaliser » du dividende $q$.

**2.** $e^{0{,}06-0{,}02}=e^{0{,}04}$ ($=1{,}0408$).

**3.** $e^{\ln 7}=7$ et $\ln(e^{-3})=-3$. Les deux fonctions se défont
mutuellement — c'est leur seule raison d'être ensemble.

**4.** $\ln 100-\ln 105$. **Négatif**, car $100<105$ : le log d'un nombre
inférieur à 1 est négatif. Dans $d_1$, ça traduit « je suis **sous** le
strike », donc l'option est OTM. Valeur : $-0{,}0488$ — le premier chiffre de
l'exercice 5 du TD.

**5.** $\ln S_0+\ln(e^{rT})=\ln S_0+rT$. **Retiens cette forme :** c'est
exactement le numérateur de $d_1$ qui se construit comme ça.

**6.** $\approx1-0{,}01=0{,}99$. Erreur : $5\times10^{-5}$.

**7.** $\approx1{,}03$. Exact $1{,}030455$, erreur $4{,}5\times10^{-4}$.

**8.** $100e^{-0{,}06}\approx100(1-0{,}06)=94$. Exact $94{,}18$. De tête, à
18 centimes près.

**9.** $\frac{F}{S}=e^{(r-q)T}$, donc $\ln\frac{F}{S}=(r-q)T$, donc
$$r-q=\frac{1}{T}\ln\frac{F}{S}.$$
**Tu viens de retrouver seul la formule du convenience yield implicite**
(exercice 4 du TD) : on lit un taux dans une courbe en prenant un log.

**10.** $r-q=\frac{1}{0{,}5}\ln(1{,}02)=2\times0{,}0198=0{,}0396$, soit
**3,96 %**. Note que ce n'est pas 4 % : $\ln(1{,}02)\ne0{,}02$ exactement.

**11.** Il faut $e^{rT}=2$, donc $T=\frac{\ln2}{r}=\frac{0{,}69}{0{,}05}$,
soit environ **13,9 ans**. C'est la **« règle de 70 »** utilisée en salle :
$70/5=14$ ans.
</details>

---

## M2 — Dérivées : les six qui servent

### ① À quoi ça sert
Un grec **est** une dérivée. Delta = dérivée du prix par rapport au spot,
gamma = dérivée du delta. Pas de dérivées ⇒ pas de grecs.

### ② Le rappel

**L'idée en une phrase :** la dérivée $f'(x)$, c'est **de combien $f$ bouge
quand $x$ bouge d'une toute petite unité**. C'est une *sensibilité*. Un desk
ne dit jamais « dérivée », il dit « sensi ». Même chose.

| Fonction | Dérivée | Note |
|---|---|---|
| $x^n$ | $nx^{n-1}$ | |
| $e^{x}$ | $e^{x}$ | elle est sa propre dérivée |
| $e^{ax}$ | $a\,e^{ax}$ | le **$a$ descend** |
| $\ln x$ | $1/x$ | |
| $\sqrt x=x^{1/2}$ | $\frac{1}{2\sqrt x}$ | sert pour $\sqrt T$ |
| $f(g(x))$ | $f'(g(x))\cdot g'(x)$ | **règle de la chaîne** |

**Produit :** $(uv)'=u'v+uv'$.

**La règle de la chaîne, en français :** « je dérive l'extérieur, **puis** je
multiplie par la dérivée de l'intérieur ». C'est l'outil qu'on utilise le plus
en §6.

### ③ Exemple traité
**Énoncé.** Dériver $f(T)=e^{-rT}$ par rapport à $T$.
Extérieur : $e^{u}$, dérivée $e^{u}$. Intérieur : $u=-rT$, dérivée $-r$.
$$f'(T)=e^{-rT}\times(-r)=-r\,e^{-rT}$$
**Lecture :** le facteur d'actualisation **décroît** quand la maturité
s'allonge (signe négatif), et d'autant plus vite que le taux est élevé.

### ④ Micro-exercices

**Série A — dérivées directes**

1. $f(S)=S^2$
2. $f(S)=\ln(S/K)$, $K$ constant
3. $f(T)=\sigma\sqrt T$
4. $f(x)=e^{-x}$

**Série B — règle de la chaîne** (dériver l'extérieur, puis multiplier par la dérivée de l'intérieur)

5. $f(T)=e^{-rT}$ par rapport à $T$
6. $f(T)=e^{(r-q)T}$ par rapport à $T$
7. $\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ par rapport à $x$
8. $f(S)=e^{-q T}\ln S$ par rapport à $S$

**Série C — lecture financière**

9.  $V(T)=Ke^{-rT}$. Signe de $V'(T)$ ? Sens économique ?
10. Le payoff d'un forward est $f(S)=S-K$. Que vaut $\frac{df}{dS}$ ?
    Pourquoi dit-on qu'un forward a un **delta de 1** ?
11. Pourquoi la dérivée de $\sqrt T$ « explose » quand $T\to0$, et quel grec
    cela concerne-t-il ?

<details><summary><b>Corrigés M2</b></summary>

**1.** $2S$.

**2.** $\ln(S/K)=\ln S-\ln K$ (M1) ; $\ln K$ est une **constante**, dérivée
nulle. Donc $\boxed{1/S}$.

**3.** $\sigma T^{1/2}$, donc
$\sigma\cdot\frac12T^{-1/2}=\boxed{\dfrac{\sigma}{2\sqrt T}}$.

**4.** $-e^{-x}$ (le $-1$ de l'intérieur descend).

**5.** Extérieur $e^u\to e^u$ ; intérieur $u=-rT\to-r$. Donc
$\boxed{-re^{-rT}}$.

**6.** $(r-q)e^{(r-q)T}$. **C'est la pente de la courbe de forward** : si
$r>q$ elle monte (contango), si $r<q$ elle descend.

**7.** Extérieur $e^u$ (dérivée $e^u$), intérieur $u=-x^2/2$ (dérivée $-x$) :
$$\phi'(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\times(-x)=\boxed{-x\,\phi(x)}$$
Jolie propriété : la dérivée de la densité normale, c'est elle-même fois $-x$.

**8.** $e^{-qT}$ est une constante vis-à-vis de $S$ : $\boxed{e^{-qT}/S}$.

**9.** $V'(T)=-rKe^{-rT}<0$. **Négatif** : plus l'échéance est lointaine, moins
la valeur actuelle du strike est élevée. C'est le cœur du $\rho$ (§6.6).

**10.** $\frac{df}{dS}=1$. Un forward bouge **exactement** comme le
sous-jacent : delta $=1$, gamma $=0$ (pas de convexité). C'est le repère
auquel on compare toutes les options.

**11.** $\frac{d}{dT}\sqrt T=\frac{1}{2\sqrt T}\to+\infty$ quand $T\to0$.
**C'est le theta** : la valeur temps ne s'écoule pas linéairement, elle
s'effondre en accéléré dans les derniers jours. Voilà pourquoi on ne garde pas
des options ATM très courtes quand on est acheteur.
</details>

---

## M3 — Approximations locales (développements limités)

> **C'est le module de ta capture d'écran.** Prends‑le lentement, tout le
> reste en découle.

### ① À quoi ça sert
À remplacer une fonction compliquée par une **droite** (ou une parabole) quand
on regarde de très près. C'est ce qui permet : la limite $e^{rT}$, l'approx du
call ATM $0{,}4\sigma\sqrt T S$, et le lemme d'Itô lui‑même.

### ② Le rappel — l'idée avant les formules

Zoome sur une courbe lisse, très fort, autour d'un point. **Elle ressemble à
une droite.** C'est tout ce qu'est un développement limité : *près de zéro,
je remplace la courbe par sa tangente*. Si je veux plus de précision,
j'ajoute un terme en $x^2$ (une parabole).

**Les trois DL du J1** (valables quand $x$ est **petit**, disons $|x|<0{,}1$) :

$$e^{x}\approx1+x\qquad \ln(1+x)\approx x\qquad \sqrt{1+x}\approx1+\frac{x}{2}$$

Et avec le terme suivant, si on veut être plus précis :
$$e^{x}\approx1+x+\frac{x^2}{2}\qquad\ln(1+x)\approx x-\frac{x^2}{2}$$

**Vérifions que ce n'est pas du bluff** — $x=0{,}1$ (déjà « grand ») :

| | valeur exacte | $1+x$ | $1+x+\frac{x^2}{2}$ |
|---|---|---|---|
| $e^{0,1}$ | $1{,}105171$ | $1{,}1$ | $1{,}105$ |
| $\ln(1{,}1)$ | $0{,}095310$ | $0{,}1$ | $0{,}095$ |

Et pour $x=0{,}01$ :

| | exact | $1+x$ |
|---|---|---|
| $e^{0,01}$ | $1{,}0100502$ | $1{,}01$ |
| $\ln(1{,}01)$ | $0{,}0099503$ | $0{,}01$ |

**Conclusion :** plus $x$ est petit, plus l'approximation est bonne — et
l'erreur diminue **beaucoup** plus vite que $x$ (elle est en $x^2$). Quand tu
divises $x$ par 10, l'erreur est divisée par 100.

### ③ Que veut dire $O(1/m)$ ?

C'est **la seule notation intimidante de ta capture**, et elle ne dit rien de
plus que :

> « il reste des bricoles, et ces bricoles sont au plus de la taille de
> $1/m$ ; donc quand $m$ devient énorme, elles tendent vers zéro et je les
> jette. »

$O(\cdot)$ = « **un reste de l'ordre de** ». Rien à calculer. C'est une
façon d'écrire « et du menu fretin qui disparaît ». Quand tu lis
$O(1/m)$ dans une preuve, tu peux littéralement lire **« + poussière »**.

### ④ Micro-exercices

**Série A — appliquer les trois DL**

1. $e^{0{,}02}$ (exact $1{,}020201$)
2. $e^{-0{,}02}$ (exact $0{,}980199$)
3. $\ln(1{,}05)$ (exact $0{,}048790$)
4. $\ln(0{,}98)$ (exact $-0{,}020203$)
5. $\sqrt{1{,}04}$ (exact $1{,}019804$)

**Série B — ordre 2, quand l'ordre 1 ne suffit plus**

6. Recalculer $e^{0{,}05}$ avec $1+x$ puis avec $1+x+\frac{x^2}{2}$.
   Exact : $1{,}051271$. Que gagne-t-on ?
7. Pourquoi l'erreur de $e^x\approx1+x$ est-elle divisée par ~100 quand on
   divise $x$ par 10 ?

**Série C — le réflexe qui sert vraiment**

8.  Une action baisse de 2 % puis remonte de 2 %. Est-on revenu au départ ?
9.  Même question avec $\pm5$ %, puis $\pm10$ %. Que remarque-t-on ?
10. Que signifie $O(1/m)$ dans une preuve ? Faut-il le calculer ?

<details><summary><b>Corrigés M3</b></summary>

**1.** $1{,}02$ contre $1{,}020201$ : erreur $2\times10^{-4}$, soit **2 points
de base**. Négligeable pour un ordre de grandeur oral.

**2.** $0{,}98$ contre $0{,}980199$ : erreur $2\times10^{-4}$.

**3.** $\approx0{,}05$, exact $0{,}048790$. **C'est le fameux « 5 % annuel
= 4,88 % en continu ».** Un taux continu est toujours **un peu plus petit** que
le taux simple équivalent, parce qu'il capitalise plus souvent.

**4.** $\ln(1+x)$ avec $x=-0{,}02$ : $\approx-0{,}02$, exact $-0{,}020203$.
L'approximation marche aussi pour les $x$ **négatifs**.

**5.** $1+\frac{0{,}04}{2}=1{,}02$, exact $1{,}019804$. Erreur $2\times10^{-4}$.

**6.** Ordre 1 : $1{,}05$ (erreur $1{,}3\times10^{-3}$).
Ordre 2 : $1+0{,}05+0{,}00125=1{,}05125$ (erreur $2\times10^{-5}$).
**On gagne un facteur ~60.** Le terme en $x^2$ vaut la peine dès que
$x>0{,}05$.

**7.** Parce que l'erreur est de l'ordre de $\frac{x^2}{2}$. Si $x$ est divisé
par 10, alors $x^2$ est divisé par **100**. C'est toute la puissance des DL :
plus on regarde de près, plus la droite est une bonne approximation, et **très
vite**.

**8.** Non. Le facteur total est
$$(1-0{,}02)(1+0{,}02)=1-0{,}02^2=0{,}9996$$
On a **perdu 0,04 %**.

**9.** $\pm5$ % : $0{,}9975$ (−0,25 %). $\pm10$ % : $0{,}99$ (−1 %).
**Le coût est en carré de l'amplitude** : doubler la volatilité quadruple la
perte. C'est le *volatility drag*. **Tu viens de toucher du doigt pourquoi la
moyenne dépasse la médiane** en log-normale : c'est le $-\sigma^2/2$ du
module M7.

**10.** Ça veut dire « il reste des bricoles au plus de la taille de $1/m$,
qui tendent vers zéro ». **Rien à calculer.** Lis-le « + poussière ».
</details>

---

## M4 — La limite $(1+r/m)^{mT}\to e^{rT}$, refaite lentement

> C'est **exactement** la formule de ta capture. On la reprend en 5 étapes, et
> on commence par la comprendre **sans aucun calcul**.

### ① D'abord, le sens — zéro maths

Je place 100 € à 5 % pendant 1 an.

- Versé **1 fois** en fin d'année : $100\times1{,}05=105{,}000$
- Versé **2 fois** (2,5 % par semestre) : $100\times1{,}025^2=105{,}0625$ — un
  peu plus, car les intérêts du 1er semestre produisent eux‑mêmes des intérêts
- **12 fois** (mensuel) : $105{,}116$
- **365 fois** (quotidien) : $105{,}1267$
- **8 760 fois** (horaire) : $105{,}12710$
- **En continu** : $100\,e^{0{,}05}=105{,}12711$

**Regarde la colonne : ça converge.** Découper toujours plus finement ne fait
pas exploser le résultat, ça **plafonne**. Cette limite s'appelle $e^{0,05}$.
Voilà tout ce que dit la formule. Le reste, c'est de la plomberie.

### ② La plomberie, étape par étape

On veut $\lim_{m\to\infty}\left(1+\frac{r}{m}\right)^{mT}$.

**Étape 1 — passer au log.** Une puissance est pénible à manipuler ; un log la
transforme en produit (M1). On pose $A_m=\left(1+\frac{r}{m}\right)^{mT}$ :
$$\ln A_m=mT\cdot\ln\left(1+\frac{r}{m}\right)$$

**Étape 2 — l'ingrédient clé.** $m$ devient énorme, donc $\frac{r}{m}$ devient
**minuscule**. Or pour $x$ petit, $\ln(1+x)\approx x$ (M3) ! Ici $x=\frac{r}{m}$ :
$$\ln\left(1+\frac{r}{m}\right)\approx\frac{r}{m}$$

**Étape 3 — remplacer.**
$$\ln A_m\approx mT\times\frac{r}{m}=rT$$
**Le $m$ se simplifie.** C'est tout le tour de passe‑passe : le $m$ qui
multiplie annule le $m$ qui divise.

**Étape 4 — le reste.** L'approximation de l'étape 2 n'est pas exacte : il
reste des poussières, notées $O(1/m)$. Multipliées par $mT$, elles restent de
taille $\sim T/m\to0$. **Donc elles disparaissent.**

**Étape 5 — revenir de l'autre côté du log.** Si $\ln A_m\to rT$, alors
$$A_m\to e^{rT}.\qquad\blacksquare$$

### ③ Contrôle numérique
Avec $r=5\%$, $T=1$ : l'écart entre le mensuel ($1{,}051162$) et le continu
($1{,}051271$) vaut $1{,}1\times10^{-4}$. La théorie prédit un reste de l'ordre
de $\frac{r^2T}{2m}=\frac{0{,}0025}{24}=1{,}04\times10^{-4}$. **Ça colle.**

### ④ Micro-exercices

**Série A — comprendre la convergence**

1. Sans calculatrice, ordonner : $\left(1+\frac{0{,}06}{2}\right)^2$,
   $e^{0{,}06}$, $1{,}06$.
2. Avec $r=4$ %, calculer $(1+r/m)^m$ pour $m=1,2,4$. Puis comparer à
   $e^{0{,}04}=1{,}040811$.
3. Dans l'étape 3 de la démonstration, pourquoi est-il crucial que le $m$
   se simplifie ?

**Série B — refaire la preuve soi-même**

4. Écris les 5 étapes de mémoire, sans regarder. *(Passer au log → …)*
5. À quelle étape utilise-t-on le module M3 ? Quelle approximation
   exactement ?

**Série C — conversions de taux (question d'entretien classique)**

6. Convertir 6 % **semestriel** en taux continu.
   *(Formule : $r_c=m\ln(1+r_m/m)$.)*
7. Convertir 8 % **trimestriel** en taux continu.
8. Convertir 5 % **continu** en taux **mensuel** équivalent.
   *(Formule : $r_m=m(e^{r_c/m}-1)$.)*
9. Un taux continu est-il toujours au-dessus ou en dessous du taux composé
   équivalent ? Pourquoi ?

<details><summary><b>Corrigés M4</b></summary>

**1.** $1{,}06<1{,}0609<1{,}061837$, soit
$$1{,}06\;<\;\left(1+\tfrac{0{,}06}{2}\right)^2\;<\;e^{0{,}06}$$
**Règle générale :** plus on capitalise souvent, plus on finit haut. Le continu
est la **borne supérieure**.

**2.** $m=1\to1{,}040000$ · $m=2\to1{,}040400$ · $m=4\to1{,}040604$ ·
continu $\to1{,}040811$. **Ça monte et ça plafonne** — exactement le tableau
du §0.1 du cours.

**3.** Parce que sinon la limite serait $0$ ou $+\infty$. C'est l'équilibre
exact entre « le taux par période tend vers 0 » et « le nombre de périodes tend
vers l'infini » qui produit un résultat **fini**. Deux effets opposés qui se
compensent : c'est ça, une forme indéterminée $1^\infty$.

**4.** ① Passer au log (casse la puissance) ② $\ln(1+x)\approx x$ car
$x=r/m$ est minuscule ③ $mT\times\frac{r}{m}=rT$, **le $m$ se simplifie**
④ le reste $O(1/m)$ tend vers 0 ⑤ repasser à l'exponentielle : $e^{rT}$.

**5.** À l'**étape 2**, avec $\ln(1+x)\approx x$ appliqué à $x=\frac{r}{m}$.
C'est le seul endroit où l'on approxime — et l'approximation devient exacte à
la limite.

**6.** $r_c=2\ln(1{,}03)=2\times0{,}029559=0{,}0591$, soit **5,91 %**.
Inférieur à 6 %, cohérent.

**7.** $r_c=4\ln(1{,}02)=4\times0{,}019803=0{,}0792$, soit **7,92 %**.

**8.** $r_m=12(e^{0{,}05/12}-1)=12\times0{,}0041754=0{,}0501$, soit
**5,01 %**. Le taux mensuel équivalent est légèrement **au-dessus** du continu.

**9.** **Toujours en dessous.** Le continu capitalise le plus souvent
possible, donc pour atteindre le même capital final il lui faut un taux
affiché plus petit. Formulation d'entretien : *« le taux continu est le taux
équivalent le plus faible, parce que c'est la capitalisation la plus
fréquente »*.
</details>

---

## M5 — La loi normale : $\phi$ et $N$

### ① À quoi ça sert
$N(d_1)$ et $N(d_2)$ **sont** la formule de Black-Scholes. Si tu sais lire ces
deux symboles, la formule cesse d'être un hiéroglyphe.

### ② Le rappel

Deux objets, à ne jamais confondre.

**$\phi(x)$ — la densité** (« la cloche ») :
$$\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$$
C'est la **hauteur** de la courbe en cloche au point $x$. Maximale en $0$ où
elle vaut $\phi(0)=\frac{1}{\sqrt{2\pi}}\approx\mathbf{0{,}3989}$ — retiens
**« 0,4 »**, c'est le $0{,}4$ de l'approximation du call ATM (§5.2 du cours !).

**$N(x)$ — la fonction de répartition** (« l'aire cumulée ») :
$$N(x)=\mathbb P(Z\le x)=\text{aire sous la cloche à gauche de }x$$
C'est une **probabilité** : toujours entre 0 et 1, toujours croissante.

**Le lien :** $N$ est la primitive de $\phi$ ; autrement dit $N'(x)=\phi(x)$.
*Accumuler la hauteur donne l'aire.*

**Les valeurs à connaître :**

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $1{,}645$ | $1{,}96$ | $2$ |
|---|---|---|---|---|---|---|---|
| $N(x)$ | $0{,}023$ | $0{,}159$ | $\mathbf{0{,}5}$ | $0{,}841$ | $0{,}95$ | $0{,}975$ | $0{,}977$ |

**La symétrie, indispensable :**
$$\boxed{N(-x)=1-N(x)}$$
**Preuve visuelle.** la cloche est symétrique, donc l'aire à gauche de $-x$
égale l'aire à droite de $+x$, qui vaut $1-N(x)$. C'est **exactement** ce qui
transforme la formule du call en celle du put (§4.4 du cours).

**Approximation près de zéro** (utile en mental math) :
$$N(x)\approx0{,}5+0{,}4\,x\quad\text{pour }|x|<0{,}3$$

### ③ Exemple traité
**Énoncé.** Dans l'exercice 5 du TD, $d_2=-0{,}2795$. Que vaut $N(d_2)$ et que signifie-t-il ?
$N(-0{,}2795)=\mathbf{0{,}3899}$.
Approximation : $0{,}5-0{,}4\times0{,}2795=0{,}388$ — à un millième près, de tête.
**Sens :** il y a environ **39 % de probabilité (risque-neutre) que l'option
finisse dans la monnaie.** Cohérent : le strike 105 est au-dessus du spot 100,
donc moins d'une chance sur deux.

### ④ Micro-exercices

**Série A — lire la table**

1. Que vaut $N(0)$ ? Pourquoi, sans calcul ?
2. Sachant $N(1)=0{,}841$, calculer $N(-1)$.
3. Sachant $N(1{,}5)=0{,}933$, calculer $N(-1{,}5)$.
4. Que vaut $N(-2)$ sachant $N(2)=0{,}977$ ?

**Série B — distinguer $\phi$ et $N$**

5. $\phi$ peut-elle dépasser 1 ? Et $N$ ?
6. Où $\phi$ est-elle maximale, et que vaut ce maximum ?
7. Quel est le lien mathématique entre $\phi$ et $N$ ?
8. $N$ est-elle croissante ou décroissante ? Pourquoi, en une phrase ?

**Série C — mental math** (approx $N(x)\approx0{,}5+0{,}4x$)

9.  Estimer $N(0{,}2)$ (exact $0{,}579260$).
10. Estimer $N(-0{,}25)$ (exact $0{,}401294$).
11. Estimer $N(0{,}1)$ (exact $0{,}539828$).

**Série D — sens financier**

12. Dans le TD, $d_2=-0{,}2795$ donne $N(d_2)=0{,}39$. Interprète ce nombre.
13. Une option a $N(d_2)=0{,}5$. Où se situe le strike ?
14. Pourquoi a-t-on **toujours** $N(d_1)>N(d_2)$ ?

<details><summary><b>Corrigés M5</b></summary>

**1.** $N(0)=\mathbf{0{,}5}$. La cloche est symétrique autour de 0 : la moitié
de l'aire est à gauche. Concrètement, une option **au strike forward** a ~50 %
de finir ITM — c'est le §2.4 du cours ($C=P$ à l'ATM forward).

**2.** $N(-1)=1-0{,}841=\mathbf{0{,}159}$.

**3.** $N(-1{,}5)=1-0{,}933=\mathbf{0{,}067}$.

**4.** $N(-2)=1-0{,}977=\mathbf{0{,}023}$. Retiens ces deux-là : **2 % à
2 écarts-types**, c'est le repère des queues de distribution (et de la VaR 99 %,
vu au J21).

**5.** $\phi$ **oui** (c'est une hauteur, pas une probabilité — pour une
normale très resserrée elle dépasse largement 1). $N$ **non, jamais** : c'est
une probabilité, plafonnée à 1.

**6.** En $x=0$, où elle vaut $\frac{1}{\sqrt{2\pi}}\approx\mathbf{0{,}3989}$.
**Retiens « 0,4 »** : c'est le $0{,}4$ de l'approximation du call ATM.

**7.** $N$ est la **primitive** de $\phi$ : $N'(x)=\phi(x)$. Accumuler la
hauteur donne l'aire.

**8.** **Croissante**, toujours. En avançant vers la droite on ne fait
qu'ajouter de l'aire (et $\phi>0$ partout).

**9.** $0{,}5+0{,}4\times0{,}2=\mathbf{0{,}58}$. Exact $0{,}5793$ : erreur de
7 dix-millièmes, de tête.

**10.** $0{,}5-0{,}4\times0{,}25=\mathbf{0{,}40}$. Exact $0{,}4013$.

**11.** $0{,}5+0{,}04=\mathbf{0{,}54}$. Exact $0{,}5398$.

**12.** **Environ 39 % de probabilité (risque-neutre) que l'option finisse
dans la monnaie.** Cohérent : le strike 105 est au-dessus du spot 100, donc
moins d'une chance sur deux.

**13.** Au **strike forward** ($K=F$), puisque $N(0)=0{,}5$ signifie $d_2=0$.

**14.** Parce que $d_1=d_2+\sigma\sqrt T$ et que $\sigma\sqrt T>0$ : $d_1$ est
strictement à droite de $d_2$, et $N$ est croissante. Économiquement, $N(d_1)$
pondère par la **valeur** du sous-jacent, et les scénarios d'exercice sont
justement ceux où $S$ est élevé.
</details>

---

## M6 — Somme d'exponentielles et complétion du carré

### ① À quoi ça sert
**Uniquement** à comprendre l'étape 5 de la démonstration de Black-Scholes
(§4.4), celle où $N(d_1)$ apparaît « par magie ». C'est le seul passage
calculatoire dur du J1 — et c'est un simple exercice de collège déguisé.

### ② Le rappel

**Compléter le carré**, c'est réécrire $z^2+bz$ sous la forme
$(z+\tfrac{b}{2})^2-\tfrac{b^2}{4}$. Rien de plus. Tu l'as fait au lycée pour
résoudre les équations du second degré.

Dans la démo de BS, on rencontre l'exposant
$$-\frac{z^2}{2}+sz$$
On factorise par $-\frac12$ :
$$-\frac{z^2}{2}+sz=-\frac12\left(z^2-2sz\right)$$
Puis on complète : $z^2-2sz=(z-s)^2-s^2$. Donc
$$-\frac12\left[(z-s)^2-s^2\right]=\boxed{-\frac{(z-s)^2}{2}+\frac{s^2}{2}}$$

**Pourquoi c'est utile.** À gauche, l'exposant contient un $z$ « en trop ». À
droite, on a **la même cloche, simplement décalée de $s$**, multipliée par une
constante $e^{s^2/2}$ qui sort de l'intégrale.

**En une phrase, ce que fait cette astuce dans BS :**
> Multiplier une gaussienne par $e^{sz}$, c'est **déplacer son centre de $s$**
> (et récupérer un facteur constant au passage).

C'est *toute* la raison pour laquelle la borne d'intégration passe de $-d_2$ à
$-d_2-s$, c'est-à-dire pourquoi le second terme fait apparaître
$$d_1=d_2+\sigma\sqrt T.$$

### ③ Exemple traité
**Énoncé.** Vérifier l'identité avec $z=1$ et $s=0{,}3$.
Gauche : $-\frac{1}{2}+0{,}3=-0{,}2$.
Droite : $-\frac{(1-0{,}3)^2}{2}+\frac{0{,}09}{2}=-0{,}245+0{,}045=-0{,}2$. ✔

### ④ Micro-exercices

**Série A — mécanique du carré**

1. Compléter le carré dans $z^2+4z$.
2. Compléter le carré dans $z^2+6z$.
3. Compléter le carré dans $z^2-2sz$ (cas général de la démo).

**Série B — la forme utilisée dans Black-Scholes**

4. Réécrire $-\frac{z^2}{2}+2z$ sous la forme $-\frac{(z-a)^2}{2}+c$.
5. Réécrire $-\frac{z^2}{2}+sz$ (cas général). Vérifier avec $z=2$, $s=0{,}5$.
6. Dans $-\frac{(z-s)^2}{2}+\frac{s^2}{2}$, lequel des deux termes **sort de
   l'intégrale** ? Pourquoi ?

**Série C — sens dans la démonstration**

7. En une phrase : que fait $e^{sz}$ à une cloche gaussienne ?
8. Dans la démo BS, $s=\sigma\sqrt T$. De combien la cloche est-elle décalée,
   et quel objet du cours cela fait-il apparaître ?
9. Pourquoi la borne d'intégration passe-t-elle de $-d_2$ à $-d_2-s$ ?

<details><summary><b>Corrigés M6</b></summary>

**1.** $(z+2)^2-4$.

**2.** $(z+3)^2-9$.

**3.** $(z-s)^2-s^2$. **C'est la seule ligne d'algèbre à retenir** de tout ce
module.

**4.** $-\frac12(z^2-4z)=-\frac12[(z-2)^2-4]=-\frac{(z-2)^2}{2}+2$.
Donc $a=2$, $c=2$.

**5.**
$$-\frac12(z^2-2sz)=-\frac12\left[(z-s)^2-s^2\right]=-\frac{(z-s)^2}{2}+\frac{s^2}{2}$$
Vérification $z=2$, $s=0{,}5$ : gauche $=-2+1=-1$ ;
droite $=-\frac{2{,}25}{2}+0{,}125=-1$. ✔

**6.** Le terme $\frac{s^2}{2}$ : c'est une **constante** (il ne contient pas
$z$), donc $e^{s^2/2}$ sort de l'intégrale. Le terme $-\frac{(z-s)^2}{2}$
reste dedans et redonne **une cloche complète**, simplement recentrée en $s$ —
donc son intégrale vaut de nouveau 1 (à la borne près).

**7.** **Ça la décale de $s$** (et ça produit un facteur constant
$e^{s^2/2}$). Rien d'autre.

**8.** Décalage de $\sigma\sqrt T$. Cela transforme $d_2$ en
$d_2+\sigma\sqrt T=\mathbf{d_1}$. **C'est l'origine exacte de $N(d_1)$** dans
la formule — et la raison pour laquelle $d_1>d_2$ toujours.

**9.** Parce qu'on pose $u=z-s$ pour retrouver une cloche centrée. Si $z$
part de $-d_2$, alors $u$ part de $-d_2-s$. **La borne suit le changement de
variable**, c'est tout.
</details>

---

## M7 — La log-normale et le fameux $-\sigma^2/2$

### ① À quoi ça sert
À comprendre pourquoi $S_T$ ne peut pas devenir négatif, et d'où sort ce
$-\frac{\sigma^2}{2}$ qui traîne dans tout le cours (§4.2) et dans $d_1,d_2$.

### ② Le rappel

**Définition.** $X$ est **log-normale** si $\ln X$ est normale. Autrement dit :
la normale décrit les **rendements en log**, la log-normale décrit **le prix**.

**Deux conséquences immédiates :**
1. $X=e^{(\text{quelque chose de normal})}>0$ : **un prix reste positif.** C'est
   la raison n°1 de ce choix de modèle.
2. La distribution est **asymétrique** : queue longue à droite (une action peut
   faire ×10, elle ne peut pas faire −200 %).

**Le résultat central** (celui qui produit le $-\sigma^2/2$) :
$$\boxed{\mathbb E\left[e^{Y}\right]=e^{\;\mathbb E[Y]+\frac12\mathrm{Var}(Y)}}
\qquad\text{pour }Y\text{ normale}$$

**Traduction :** l'espérance d'une exponentielle **n'est pas** l'exponentielle
de l'espérance. Il y a un **bonus** $+\frac12\mathrm{Var}$, dû à la convexité de
$e^x$ (inégalité de Jensen). Plus c'est volatil, plus la moyenne est tirée vers
le haut par les scénarios extrêmes.

**Application au GBM.** On veut que le prix moyen croisse à $\mu$, c'est-à-dire
$\mathbb E[S_T]=S_0e^{\mu T}$. On écrit
$S_T=S_0e^{Y}$ avec $Y$ normale de variance $\sigma^2T$. D'après la formule :
$$\mathbb E[S_T]=S_0\,e^{\mathbb E[Y]+\frac12\sigma^2T}$$
Pour que ça donne $S_0e^{\mu T}$, il faut **obligatoirement**
$$\mathbb E[Y]=\mu T-\frac{\sigma^2}{2}T
\quad\Longrightarrow\quad\boxed{\;\mathbb E[\ln S_T]=\ln S_0+\left(\mu-\frac{\sigma^2}{2}\right)T\;}$$

**Le $-\sigma^2/2$ n'est donc pas un ajustement arbitraire : c'est le prix à
payer pour que la moyenne reste $\mu$.**

**Moyenne vs médiane :**
$$\mathbb E[S_T]=S_0e^{\mu T}\qquad\text{médiane}(S_T)=S_0e^{(\mu-\frac{\sigma^2}{2})T}$$
La moyenne est **au-dessus** de la médiane. C'est le *volatility drag* que tu as
déjà rencontré en **M3.3** (−2 % puis +2 % ⇒ perte de 0,04 %).

### ③ Exemple traité
**Énoncé.** $S_0=100$, $\mu=10$ %, $\sigma=30$ %, $T=1$ an.
- Moyenne : $100e^{0{,}10}=\mathbf{110{,}52}$
- Médiane : $100e^{0{,}10-0{,}045}=100e^{0{,}055}=\mathbf{105{,}65}$

Écart : **4,86**. Plus d'une chance sur deux de finir **sous** la moyenne. Le
« rendement moyen » est trompeur — c'est le genre de remarque qui fait bonne
impression en entretien.

### ④ Micro-exercices

**Série A — comprendre le choix du modèle**

1. Pourquoi ne modélise-t-on pas $S_T$ directement par une normale ?
2. Quelle quantité est normale dans le modèle : le prix, ou autre chose ?
3. Une log-normale est-elle symétrique ? De quel côté est la queue longue ?

**Série B — le $-\sigma^2/2$**

4. Avec $\sigma=20$ %, $T=1$ : de combien la médiane est-elle sous la
   moyenne (en %) ?
5. Même question avec $\sigma=40$ %. Le résultat double-t-il ?
6. Si $\sigma\to0$, que devient l'écart moyenne/médiane ? Cohérent ?
7. D'où vient exactement le $-\frac{\sigma^2}{2}$ ? *(Une phrase.)*

**Série C — application chiffrée**

8. $S_0=50$, $\mu=6$ %, $\sigma=40$ %, $T=2$. Calculer moyenne et médiane.
9. Relie ce module à l'exercice 9 du module M3. Quel est le lien ?

<details><summary><b>Corrigés M7</b></summary>

**1.** Une normale prend des valeurs **négatives** avec probabilité non nulle.
Un prix négatif n'a pas de sens (hors WTI avril 2020, précisément parce que le
**stockage physique** avait saturé — l'exception qui confirme la règle, et qui
relie au module commodities du §1.5).

**2.** **Le log du prix**, $\ln S_T$. D'où le nom « log-normale » : c'est le
log qui est normal.

**3.** **Non, asymétrique.** Queue longue **à droite** : une action peut faire
×10, elle ne peut pas faire −200 %. Le plancher à zéro comprime la gauche.

**4.** $\frac{\sigma^2}{2}=\frac{0{,}04}{2}=0{,}02$, soit **2 %**.

**5.** $\frac{0{,}16}{2}=0{,}08$, soit **8 %**. **Non, ça quadruple** — l'effet est
en $\sigma^2$, pas en $\sigma$. Même logique qu'en M3 : le drag est quadratique.

**6.** L'écart tend vers **0**. Cohérent : sans volatilité il n'y a qu'un seul
scénario, donc moyenne = médiane. **Toute la différence vient du risque.**

**7.** De $\mathbb E[e^Y]=e^{\mathbb E Y+\frac12\mathrm{Var}Y}$ : c'est la
correction nécessaire pour que le prix **moyen** croisse bien à $\mu$.

**8.** Moyenne $=50e^{0{,}12}=\mathbf{56{,}37}$.
Médiane $=50e^{(0{,}06-0{,}08)\times2}=50e^{-0{,}04}=\mathbf{48{,}04}$.
**Remarque importante :** la médiane est **sous le prix initial** alors que le
drift est positif. Avec $\sigma=40$ %, plus d'une fois sur deux l'action est en
perte au bout de 2 ans, alors même que son espérance monte. C'est le genre de
constat qui fait très bonne impression en entretien.

**9.** C'est **le même phénomène**. En M3, $-2$ % puis $+2$ % laisse
$1-0{,}02^2$ : la perte est en carré de l'amplitude. Ici, le $-\frac{\sigma^2}{2}$
est cette même perte, exprimée en continu. **Volatility drag dans les deux
cas.**
</details>

---

## M8 — Dérivées partielles et règle de la chaîne

### ① À quoi ça sert
Le prix d'une option dépend de **plusieurs** variables à la fois ($S$, $t$,
$\sigma$, $r$). Chaque grec est une dérivée **par rapport à une seule**, les
autres gelées. C'est le langage de l'EDP (§4.3).

### ② Le rappel

**Dérivée partielle** $\frac{\partial V}{\partial S}$ : je dérive par rapport à
$S$ **en traitant $t$, $\sigma$, $r$ comme des constantes**. Le symbole rond
$\partial$ ne dit rien d'autre que « il y a d'autres variables, je les gèle ».

**Le dictionnaire grecs ↔ dérivées** — à lire de gauche à droite :

| Grec | Notation | En français |
|---|---|---|
| $\Delta$ | $\frac{\partial V}{\partial S}$ | sensibilité au **spot** |
| $\Gamma$ | $\frac{\partial^2V}{\partial S^2}$ | sensibilité **du delta** au spot |
| $\nu$ (véga) | $\frac{\partial V}{\partial\sigma}$ | sensibilité à la **vol** |
| $\Theta$ | $\frac{\partial V}{\partial t}$ | sensibilité au **temps** |
| $\rho$ | $\frac{\partial V}{\partial r}$ | sensibilité au **taux** |

**Une fois ce tableau lu, l'EDP de Black-Scholes**
$$\frac{\partial V}{\partial t}+(r-q)S\frac{\partial V}{\partial S}
+\frac12\sigma^2S^2\frac{\partial^2V}{\partial S^2}=rV$$
**se lit en français :**
$$\Theta+(r-q)S\Delta+\tfrac12\sigma^2S^2\Gamma=rV$$
> « L'usure du temps, plus le portage de ma position en delta, plus le gain de
> convexité apporté par le gamma, doit rapporter exactement le taux sans
> risque. »

Ce n'est plus une équation aux dérivées partielles : c'est une **phrase de
trader**. Et c'est la ligne la plus rentable du J1.

### ③ Exemple traité
**Énoncé.** Soit $V=S^2t$. Calculer les trois dérivées partielles.
- $\frac{\partial V}{\partial S}=2St$ ($t$ gelé)
- $\frac{\partial^2V}{\partial S^2}=2t$
- $\frac{\partial V}{\partial t}=S^2$ ($S$ gelé)

### ④ Micro-exercices

**Série A — calculer des partielles**

1. $V=S^2t$. Calculer $\frac{\partial V}{\partial S}$,
   $\frac{\partial^2V}{\partial S^2}$, $\frac{\partial V}{\partial t}$.
2. $V=e^{-rT}K$. Calculer $\frac{\partial V}{\partial r}$. Signe ? Sens
   économique ?
3. $V=Se^{-qT}$. Calculer $\frac{\partial V}{\partial S}$ et
   $\frac{\partial V}{\partial q}$.
4. $V=3S^2\sigma$. Calculer $\frac{\partial V}{\partial\sigma}$.

**Série B — traduire grec ↔ dérivée**

5. Écris $\Delta$, $\Gamma$, $\nu$, $\Theta$, $\rho$ en notation dérivée
   partielle, de mémoire.
6. Quel grec est une dérivée **seconde** ? Qu'est-ce que ça implique sur le
   signe pour un acheteur d'option ?
7. $\Gamma$ est la dérivée de quoi par rapport à quoi ? Donne les **deux**
   formulations.

**Série C — lire l'EDP comme une phrase**

8. Si $\Gamma>0$, que dit le terme $\frac12\sigma^2S^2\Gamma$ sur le signe
   de $\Theta$ (cas $r=0$, $\Delta=0$) ?
9. Traduis en français : $\Theta+(r-q)S\Delta+\frac12\sigma^2S^2\Gamma=rV$.
10. Pourquoi le véga s'écrit-il $\partial V/\partial\sigma$ alors que
    $\sigma$ est censée être **constante** dans BS ?
11. Un forward a $\Gamma=0$. Que devient l'EDP pour lui, et est-ce cohérent ?

<details><summary><b>Corrigés M8</b></summary>

**1.** $\frac{\partial V}{\partial S}=2St$ ($t$ gelé) ·
$\frac{\partial^2V}{\partial S^2}=2t$ ·
$\frac{\partial V}{\partial t}=S^2$ ($S$ gelé).

**2.** $\frac{\partial V}{\partial r}=-TKe^{-rT}<0$. **Négatif** : si les taux
montent, la valeur actuelle du strike baisse. C'est exactement le $\rho$
négatif du **put** (§6.6). Avec $K=100$, $T=2$, $r=3$ % : $-188{,}35$.

**3.** $\frac{\partial V}{\partial S}=e^{-qT}$ et
$\frac{\partial V}{\partial q}=-TSe^{-qT}<0$. Plus le dividende est élevé,
moins le forward vaut.

**4.** $3S^2$ ($S$ gelé).

**5.** $\Delta=\frac{\partial V}{\partial S}$ ·
$\Gamma=\frac{\partial^2V}{\partial S^2}$ ·
$\nu=\frac{\partial V}{\partial\sigma}$ ·
$\Theta=\frac{\partial V}{\partial t}$ ·
$\rho=\frac{\partial V}{\partial r}$.

**6.** Le **gamma**. Une dérivée seconde mesure la **courbure** : pour un
acheteur d'option elle est **positive** (payoff convexe), et c'est précisément
ce qu'il paie via le theta.

**7.** Dérivée **seconde du prix** par rapport au spot, ou dérivée
**première du delta** par rapport au spot. Les deux formulations sont
attendues en entretien.

**8.** L'EDP devient $\Theta+\frac12\sigma^2S^2\Gamma=0$, donc
$$\Theta=-\tfrac12\sigma^2S^2\Gamma<0.$$
**Long gamma ⇒ theta négatif.** Tu viens de redémontrer seul « le theta est le
loyer du gamma » (§4.3, étape 5).

**9.** « L'usure du temps, plus le portage de ma position en delta, plus le
gain de convexité apporté par le gamma, doit rapporter exactement le taux sans
risque. » **Si tu sais dire cette phrase, tu as compris le J1.**

**10.** Excellente question, et c'est **une incohérence assumée du modèle**. BS
suppose $\sigma$ constante, donc en toute rigueur le véga devrait être nul.
On s'en sert quand même comme mesure de sensibilité au paramètre choisi.
**C'est exactement ce que dit la phrase du cours** : « Black-Scholes est faux
mais universel, c'est un dictionnaire prix ↔ vol ». Si un intervieweur pose
cette question, il teste si tu récites ou si tu comprends.

**11.** Avec $\Gamma=0$ et $V=S-Ke^{-rT}$, l'EDP se réduit à
$\Theta+(r-q)S\Delta=rV$. **Cohérent :** un forward n'a pas de convexité, donc
aucun loyer de gamma à payer — il ne « perd » rien avec le temps, il ne fait
que porter.
</details>

---

# Exercice de synthèse — reconstruire $d_1$ et $d_2$

> **Le seul exercice qui mobilise les 8 modules d'un coup.** Fais-le au crayon.
> Si tu le réussis, tu peux ouvrir le §4 du J1 sans crainte.

On donne $S_0=100$, $K=105$, $r=3$ %, $q=0$, $\sigma=25$ %, $T=0{,}5$.

1. Calculer $\ln(S_0/K)$. *(module M1)*
2. Calculer $\sigma\sqrt T$. *(M2 pour la racine)*
3. Calculer $\left(r-q+\frac{\sigma^2}{2}\right)T$. *(M7 pour le $\sigma^2/2$)*
4. En déduire $d_1$, puis $d_2=d_1-\sigma\sqrt T$.
5. Estimer $N(d_1)$ et $N(d_2)$ avec $N(x)\approx0{,}5+0{,}4x$. *(M5)*
6. Sans calculer le prix : $N(d_1)$ doit-il être plus grand ou plus petit que
   $N(d_2)$ ? Pourquoi ? *(M6)*
7. L'option est-elle ITM ou OTM ? Cohérent avec $N(d_2)<0{,}5$ ?

<details><summary><b>Corrigé de la synthèse</b></summary>

**1.** $\ln(100/105)=\ln100-\ln105=-0{,}048790$. **Négatif** car on est sous
le strike.

**2.** $0{,}25\times\sqrt{0{,}5}=0{,}25\times0{,}707107=0{,}176777$.

**3.**
$$\left(0{,}03+\frac{0{,}0625}{2}\right)\times0{,}5=(0{,}03+0{,}03125)\times0{,}5=0{,}030625$$

**4.**
$$d_1=\frac{-0{,}048790+0{,}030625}{0{,}176777}=-0{,}102758$$
$$d_2=-0{,}102758-0{,}176777=-0{,}279534$$

**5.** $N(d_1)\approx0{,}5-0{,}4\times0{,}1028=0{,}459$ (exact $0{,}459078$) ;
$N(d_2)\approx0{,}5-0{,}4\times0{,}2795=0{,}388$ (exact $0{,}389917$).
**À trois millièmes près, de tête.**

**6.** Plus **grand**, toujours : $d_1=d_2+\sigma\sqrt T$ et $N$ est
croissante. C'est le décalage de la cloche du module M6.

**7.** **OTM** ($S_0=100<105=K$). Cohérent : $N(d_2)=0{,}39<0{,}5$, donc moins
d'une chance sur deux de finir dans la monnaie.

**Tu viens de reproduire à la main les étapes 1 et 2 de l'exercice 5 du TD
du J1.** Le prix ($C=5{,}5760$) n'est plus qu'une multiplication.
</details>

---

# Auto-test de sortie M0 (10 questions, 10 minutes)

Réponds sans revenir en arrière. **7/10 = tu peux attaquer le J1 sereinement.**

1. Simplifier $e^{rT}e^{-qT}$.
2. $\ln(a/b)=$ ?
3. Dérivée de $e^{-rT}$ par rapport à $T$ ?
4. $e^{0{,}03}\approx$ ? (de tête)
5. Que vaut $N(0)$ ?
6. $N(-1{,}5)$ en fonction de $N(1{,}5)$ ?
7. $\phi(0)\approx$ ? Où le retrouve-t-on dans le J1 ?
8. Pourquoi $S_T$ est-elle log-normale et non normale ?
9. D'où vient le $-\sigma^2/2$ ?
10. Traduire en français : $\Theta+\frac12\sigma^2S^2\Gamma=0$.

<details><summary><b>Corrigés de l'auto-test</b></summary>

1. $e^{(r-q)T}$ — la formule du forward.
2. $\ln a-\ln b$.
3. $-re^{-rT}$.
4. $\approx1{,}03$ (exact $1{,}0305$).
5. $0{,}5$.
6. $1-N(1{,}5)=0{,}0668$.
7. $0{,}3989\approx0{,}4$ ; c'est le $0{,}4$ de l'approximation du call ATM
   $C\approx0{,}4\,\sigma\sqrt T\,S$.
8. Parce qu'une normale peut être négative, et qu'un prix ne peut pas l'être.
   On modélise donc le **log** du prix par une normale.
9. De $\mathbb E[e^Y]=e^{\mathbb E Y+\frac12\mathrm{Var}Y}$ : c'est la correction
   nécessaire pour que le prix **moyen** croisse bien à $\mu$.
10. « Le theta est le loyer du gamma » : ce que je gagne en convexité, je le
    paie en usure du temps.
</details>

---

## Où retourner maintenant

| Si ce module t'a débloqué… | …va lire dans le cours J1 |
|---|---|
| M1, M3, M4 | **§0.1** (la formule de ta capture) puis **§1** forwards |
| M2, M8 | **§6** les grecs |
| M5 | **§5** lecture de $N(d_1)$, $N(d_2)$ |
| M6, M7 | **§4.2 et §4.4** la démonstration de BS |

**Conseil de rythme pour aujourd'hui (06/09).** Le programme dit « dimanche
off », mais tu as pris du retard sur J1 : fais **M0 (1 h 30) + §0 et §1 du
cours J1 (1 h)**. Tu clôtures J1 demain avec les §2 à §7. Tu ne perds rien :
le J2 « grecs » s'appuie sur §6, que M2 et M8 viennent de préparer.
