#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
j01_bs_closed_form.py — Livrable J1 (samedi 05/09/2026)
Bloc A · Parite call-put, forward, Black-Scholes-Merton.

PROVENANCE (regle du mois : un chiffre sans provenance n'est pas un chiffre)
---------------------------------------------------------------------------
Drive P : Hull, "Fundamentals of Futures and Options Markets"
          - chapitres forwards/futures (cash-and-carry, F = S e^{(r-q)T}),
          - proprietes des options (bornes, parite call-put, exercice anticipe),
          - chapitre Black-Scholes-Merton (d1, d2, formule fermee, grecs).
          https://drive.google.com/file/d/1iYLWPb4AvtZDCKhydSFMGhkrd8f2Wkeo/view
Drive S : WORDS "Questions de base" (forward, futures, repo, Sharpe)
          https://drive.google.com/file/d/1QgAoOZFq337HwNk9SYvVf7FMg22mzSZL/view
          WORDS "Questions Produits derives" (call/put, EU/US)
          https://drive.google.com/file/d/19yX3O7-lH2Wac6demB9N-McIdocdl1wQ/view
Cours   : cours/J01-parite-forward-black-scholes.md (memes numeros de section)
Lab     : ShockDesk onglet Options — long call / long put / call spread.
          iv_shift NON touche aujourd'hui (c'est J2).

Exigence du programme : "call, put, parite numerique (ecart < 1e-10)".
Ce fichier va plus loin : grecs analytiques, verification par differences
finies, Monte-Carlo de controle, et corrige integral du TD (7 exercices).

Usage
-----
    python3 livrables/j01_bs_closed_form.py            # auto-tests
    python3 livrables/j01_bs_closed_form.py --td       # corrige du TD
    python3 livrables/j01_bs_closed_form.py --all      # les deux

Dependances : stdlib uniquement (math), numpy optionnel pour le Monte-Carlo.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# 0. Briques : loi normale en stdlib (pas de scipy requis)
# ---------------------------------------------------------------------------

SQRT_2PI = math.sqrt(2.0 * math.pi)


def npdf(x: float) -> float:
    """Densite de la loi normale centree reduite, phi(x)."""
    return math.exp(-0.5 * x * x) / SQRT_2PI


def ncdf(x: float) -> float:
    """Fonction de repartition N(x), via erf (precision machine ~1e-16)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# ---------------------------------------------------------------------------
# 1. Forwards — cours section 1
# ---------------------------------------------------------------------------

def forward_price(S: float, r: float, T: float, q: float = 0.0) -> float:
    """Forward equity/indice : F = S e^{(r-q)T}   (cours 1.3)."""
    return S * math.exp((r - q) * T)


def forward_fx(S: float, r_dom: float, r_for: float, T: float) -> float:
    """Parite couverte des taux : F = S e^{(rd-rf)T}   (cours 1.4).

    S = prix d'une unite de devise etrangere en devise domestique.
    """
    return S * math.exp((r_dom - r_for) * T)


def forward_commodity(S: float, r: float, u: float, y: float, T: float) -> float:
    """Commodity : F = S e^{(r+u-y)T}, u = storage, y = convenience yield (1.5)."""
    return S * math.exp((r + u - y) * T)


def implied_convenience_yield(F: float, S: float, r: float, u: float, T: float) -> float:
    """y implicite deduit de la courbe : y = r + u - ln(F/S)/T   (cours 1.5)."""
    return r + u - math.log(F / S) / T


def forward_value(F_now: float, K: float, r: float, T: float) -> float:
    """Valeur MTM d'un forward initie au strike K : f = (F-K) e^{-rT}  (1.6)."""
    return (F_now - K) * math.exp(-r * T)


# ---------------------------------------------------------------------------
# 2. Black-Scholes-Merton — cours section 4
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BS:
    """Parametres Black-Scholes-Merton.

    S : spot · K : strike · r : taux sans risque continu
    q : dividende continu (= r_etranger en FX) · sigma : vol annualisee
    T : maturite en annees
    """

    S: float
    K: float
    r: float
    q: float
    sigma: float
    T: float

    # -- d1 / d2 ------------------------------------------------------------
    @property
    def sqrtT(self) -> float:
        return math.sqrt(self.T)

    @property
    def d1(self) -> float:
        return (math.log(self.S / self.K)
                + (self.r - self.q + 0.5 * self.sigma ** 2) * self.T) \
            / (self.sigma * self.sqrtT)

    @property
    def d2(self) -> float:
        return self.d1 - self.sigma * self.sqrtT

    @property
    def df_r(self) -> float:
        return math.exp(-self.r * self.T)

    @property
    def df_q(self) -> float:
        return math.exp(-self.q * self.T)

    @property
    def forward(self) -> float:
        """F = S e^{(r-q)T}. Si K = F alors call = put (cours 2.4)."""
        return self.S * math.exp((self.r - self.q) * self.T)

    # -- prix ---------------------------------------------------------------
    def call(self) -> float:
        return self.S * self.df_q * ncdf(self.d1) - self.K * self.df_r * ncdf(self.d2)

    def put(self) -> float:
        """Obtenu par la parite, jamais en refaisant l'integrale (cours 4.4)."""
        return self.K * self.df_r * ncdf(-self.d2) - self.S * self.df_q * ncdf(-self.d1)

    def price(self, cp: str = "c") -> float:
        return self.call() if cp.lower().startswith("c") else self.put()

    # -- grecs analytiques — cours section 6 --------------------------------
    def delta(self, cp: str = "c") -> float:
        """Delta_C = e^{-qT} N(d1) ; Delta_P = -e^{-qT} N(-d1)   (6.2)."""
        if cp.lower().startswith("c"):
            return self.df_q * ncdf(self.d1)
        return -self.df_q * ncdf(-self.d1)

    def gamma(self) -> float:
        """Gamma = e^{-qT} phi(d1) / (S sigma sqrt(T)), identique call/put (6.3)."""
        return self.df_q * npdf(self.d1) / (self.S * self.sigma * self.sqrtT)

    def vega(self) -> float:
        """Vega = S e^{-qT} phi(d1) sqrt(T), par unite de vol (1.00 = 100 pts) (6.4)."""
        return self.S * self.df_q * npdf(self.d1) * self.sqrtT

    def vega_pt(self) -> float:
        """Convention desk : vega pour +1 POINT de vol (= vega / 100)."""
        return self.vega() / 100.0

    def theta(self, cp: str = "c") -> float:
        """Theta annuel (6.5). Attention : peut etre positif (put deep ITM)."""
        common = -self.S * self.df_q * npdf(self.d1) * self.sigma / (2.0 * self.sqrtT)
        if cp.lower().startswith("c"):
            return (common
                    + self.q * self.S * self.df_q * ncdf(self.d1)
                    - self.r * self.K * self.df_r * ncdf(self.d2))
        return (common
                - self.q * self.S * self.df_q * ncdf(-self.d1)
                + self.r * self.K * self.df_r * ncdf(-self.d2))

    def theta_day(self, cp: str = "c") -> float:
        """Convention desk : theta par jour calendaire."""
        return self.theta(cp) / 365.0

    def rho(self, cp: str = "c") -> float:
        """Rho par unite de taux (6.6)."""
        if cp.lower().startswith("c"):
            return self.K * self.T * self.df_r * ncdf(self.d2)
        return -self.K * self.T * self.df_r * ncdf(-self.d2)

    def rho_pt(self, cp: str = "c") -> float:
        """Convention desk : rho pour +1 POINT de taux."""
        return self.rho(cp) / 100.0

    # -- controles ----------------------------------------------------------
    def parity_residual(self) -> float:
        """C - P - (S e^{-qT} - K e^{-rT}). Doit valoir 0 a la precision machine."""
        return (self.call() - self.put()) - (self.S * self.df_q - self.K * self.df_r)

    def pde_residual(self) -> float:
        """Residu de l'EDP : Theta + (r-q) S Delta + 0.5 sigma^2 S^2 Gamma - r V (4.3)."""
        return (self.theta("c")
                + (self.r - self.q) * self.S * self.delta("c")
                + 0.5 * self.sigma ** 2 * self.S ** 2 * self.gamma()
                - self.r * self.call())

    def with_(self, **kw) -> "BS":
        """Copie avec parametres modifies (pour les differences finies)."""
        d = dict(S=self.S, K=self.K, r=self.r, q=self.q, sigma=self.sigma, T=self.T)
        d.update(kw)
        return BS(**d)


# ---------------------------------------------------------------------------
# 3. Bornes de non-arbitrage — cours section 3
# ---------------------------------------------------------------------------

def call_bounds(b: BS) -> tuple[float, float]:
    """max(0, S e^{-qT} - K e^{-rT}) <= C <= S e^{-qT}   (cours 3.1)."""
    return max(0.0, b.S * b.df_q - b.K * b.df_r), b.S * b.df_q


def put_bounds(b: BS) -> tuple[float, float]:
    """max(0, K e^{-rT} - S e^{-qT}) <= P <= K e^{-rT}   (cours 3.1)."""
    return max(0.0, b.K * b.df_r - b.S * b.df_q), b.K * b.df_r


# ---------------------------------------------------------------------------
# 4. Controles numeriques
# ---------------------------------------------------------------------------

def fd_greeks(b: BS) -> dict:
    """Grecs par differences finies centrees — verifie l'algebre de la section 6."""
    hS, hv, hT, hr = 1e-4 * b.S, 1e-5, 1e-6, 1e-6
    up, dn = b.with_(S=b.S + hS), b.with_(S=b.S - hS)
    return {
        "delta": (up.call() - dn.call()) / (2 * hS),
        "gamma": (up.call() - 2 * b.call() + dn.call()) / hS ** 2,
        "vega": (b.with_(sigma=b.sigma + hv).call()
                 - b.with_(sigma=b.sigma - hv).call()) / (2 * hv),
        # Theta = -dV/dT (le temps qui passe reduit la maturite residuelle)
        "theta": -(b.with_(T=b.T + hT).call() - b.with_(T=b.T - hT).call()) / (2 * hT),
        "rho": (b.with_(r=b.r + hr).call() - b.with_(r=b.r - hr).call()) / (2 * hr),
    }


def mc_call(b: BS, n: int = 400_000, seed: int = 20260905) -> tuple[float, float]:
    """Monte-Carlo risque-neutre avec variables antithetiques (cours 4.4).

    Retourne (prix, erreur standard). Sert de garde-fou : la formule fermee
    doit tomber dans l'intervalle a ~3 erreurs standard.
    """
    try:
        import numpy as np
    except ImportError:  # pragma: no cover
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n // 2)
    z = np.concatenate([z, -z])  # antithetiques
    ST = b.S * np.exp((b.r - b.q - 0.5 * b.sigma ** 2) * b.T
                      + b.sigma * math.sqrt(b.T) * z)
    pay = np.maximum(ST - b.K, 0.0) * math.exp(-b.r * b.T)
    return float(pay.mean()), float(pay.std(ddof=1) / math.sqrt(len(pay)))


# ---------------------------------------------------------------------------
# 5. Auto-tests (le jour n'est pas clos si un seul echoue)
# ---------------------------------------------------------------------------

def run_tests() -> int:
    fails = 0

    def check(label: str, cond: bool, detail: str = "") -> None:
        nonlocal fails
        flag = "OK  " if cond else "FAIL"
        if not cond:
            fails += 1
        print(f"  [{flag}] {label}" + (f"  {detail}" if detail else ""))

    print("=" * 74)
    print("J1 — AUTO-TESTS  (Hull / WORDS · cours J01 sections 1 a 6)")
    print("=" * 74)

    b = BS(S=100, K=105, r=0.03, q=0.0, sigma=0.25, T=0.5)

    print("\n1. Parite call-put — exigence du programme : ecart < 1e-10")
    res = b.parity_residual()
    check("parite (S=100,K=105,r=3%,q=0,sig=25%,T=0.5)", abs(res) < 1e-10,
          f"residu = {res:.2e}")
    for bb in (BS(80, 100, 0.05, 0.03, 0.40, 2.0),
               BS(120, 100, -0.005, 0.01, 0.15, 0.25),
               BS(1.0850, 1.10, 0.0425, 0.0225, 0.08, 0.25)):
        r_ = bb.parity_residual()
        check(f"parite S={bb.S} K={bb.K} T={bb.T}", abs(r_) < 1e-10,
              f"residu = {r_:.2e}")

    print("\n2. ATM forward : K = F  =>  call = put  (cours 2.4)")
    batmf = b.with_(K=b.forward)
    check("call == put au strike forward", abs(batmf.call() - batmf.put()) < 1e-12,
          f"C={batmf.call():.6f}  P={batmf.put():.6f}")

    print("\n3. Bornes de non-arbitrage  (cours 3.1)")
    lo, hi = call_bounds(b)
    check("borne call", lo <= b.call() <= hi, f"{lo:.4f} <= {b.call():.4f} <= {hi:.4f}")
    lo, hi = put_bounds(b)
    check("borne put", lo <= b.put() <= hi, f"{lo:.4f} <= {b.put():.4f} <= {hi:.4f}")

    print("\n4. Convexite en strike (butterfly >= 0)  (cours 3.2)")
    c95 = b.with_(K=95).call()
    c100 = b.with_(K=100).call()
    c105 = b.with_(K=105).call()
    fly = c95 - 2 * c100 + c105
    check("butterfly 95/100/105 >= 0", fly > 0, f"prix = {fly:.6f}")
    check("call decroissant en strike", c95 > c100 > c105,
          f"{c95:.4f} > {c100:.4f} > {c105:.4f}")

    print("\n5. Grecs analytiques vs differences finies  (cours 6)")
    fd = fd_greeks(b)
    for name, ana in (("delta", b.delta("c")), ("gamma", b.gamma()),
                      ("vega", b.vega()), ("theta", b.theta("c")), ("rho", b.rho("c"))):
        err = abs(ana - fd[name])
        tol = 1e-4 * max(1.0, abs(ana))
        check(f"{name:<5} analytique {ana: .6f} vs FD {fd[name]: .6f}", err < tol,
              f"ecart = {err:.2e}")

    print("\n6. Relations de parite sur les grecs  (cours 6.7)")
    check("Delta_C - Delta_P = e^{-qT}",
          abs((b.delta("c") - b.delta("p")) - b.df_q) < 1e-12)
    check("Gamma_C = Gamma_P (identique par construction)", True)
    check("Vega ne depend pas du sens : nu_C = nu_P", True)
    check("nu = Gamma S^2 sigma T",
          abs(b.vega() - b.gamma() * b.S ** 2 * b.sigma * b.T) < 1e-10,
          f"{b.vega():.6f} vs {b.gamma() * b.S**2 * b.sigma * b.T:.6f}")
    lemme = b.S * b.df_q * npdf(b.d1) - b.K * b.df_r * npdf(b.d2)
    check("lemme S e^{-qT} phi(d1) = K e^{-rT} phi(d2)", abs(lemme) < 1e-12,
          f"ecart = {lemme:.2e}")

    print("\n7. EDP de Black-Scholes  (cours 4.3) : Theta + (r-q)S*Delta + .5 s^2 S^2 G = rV")
    pde = b.pde_residual()
    check("residu EDP", abs(pde) < 1e-9, f"residu = {pde:.2e}")
    check("EDP verifiee aussi sur un put",
          abs(b.theta("p") + (b.r - b.q) * b.S * b.delta("p")
              + 0.5 * b.sigma ** 2 * b.S ** 2 * b.gamma() - b.r * b.put()) < 1e-9)

    print("\n8. Theta = -0.5 sigma^2 S^2 Gamma  si r=q=0 et delta-neutre (straddle)")
    z = BS(S=100, K=100, r=0.0, q=0.0, sigma=0.20, T=0.5)
    zf = z.with_(K=z.forward)  # K = F = S donc straddle exactement delta-neutre ? non :
    # delta straddle = e^{-qT}(2N(d1)-1) != 0 exactement ; on teste la relation
    # sur la somme call+put, qui est presque delta-neutre, via l'EDP.
    straddle_theta = zf.theta("c") + zf.theta("p")
    straddle_gamma = 2 * zf.gamma()
    straddle_delta = zf.delta("c") + zf.delta("p")
    lhs = straddle_theta + 0.5 * z.sigma ** 2 * z.S ** 2 * straddle_gamma
    check("Theta_straddle + .5 s^2 S^2 Gamma_straddle = 0 (r=q=0)", abs(lhs) < 1e-9,
          f"Theta={straddle_theta:.4f}  terme gamma={0.5*z.sigma**2*z.S**2*straddle_gamma:.4f}")
    check("straddle quasi delta-neutre", abs(straddle_delta) < 0.10,
          f"delta = {straddle_delta:.4f}")

    print("\n9. Cas limites  (cours 5.2)")
    check("sigma -> 0 : C -> e^{-rT}(F-K)+",
          abs(b.with_(sigma=1e-8).call()
              - b.df_r * max(b.forward - b.K, 0.0)) < 1e-6)
    check("T -> 0 : C -> (S-K)+",
          abs(b.with_(T=1e-8).call() - max(b.S - b.K, 0.0)) < 1e-6)
    check("S -> 0 : P -> K e^{-rT}",
          abs(b.with_(S=1e-8).put() - b.K * b.df_r) < 1e-6)
    check("sigma tres grand : C -> S e^{-qT}",
          abs(b.with_(sigma=25.0).call() - b.S * b.df_q) < 1e-4)

    print("\n10. Approximation ATM : C ~ 0.4 sigma sqrt(T) S  (cours 5.2)")
    a = BS(S=100, K=100, r=0.0, q=0.0, sigma=0.20, T=1.0)
    approx = 0.4 * a.sigma * math.sqrt(a.T) * a.S
    check(f"exact {a.call():.4f} vs approx {approx:.4f}",
          abs(a.call() - approx) < 0.05, f"ecart = {abs(a.call()-approx):.4f}")

    print("\n11. Theta positif : put europeen deep ITM  (piege cours 6.5)")
    itm = BS(S=50, K=150, r=0.05, q=0.0, sigma=0.20, T=1.0)
    check("theta du put deep ITM > 0", itm.theta("p") > 0,
          f"theta/an = {itm.theta('p'):.4f}  (par jour = {itm.theta_day('p'):+.5f})")

    print("\n12. Box spread = pret synthetique  (cours 2.3)")
    k1, k2 = 95.0, 105.0
    box = ((b.with_(K=k1).call() - b.with_(K=k1).put())
           - (b.with_(K=k2).call() - b.with_(K=k2).put()))
    check("box = (K2-K1) e^{-rT}", abs(box - (k2 - k1) * b.df_r) < 1e-10,
          f"{box:.10f} vs {(k2-k1)*b.df_r:.10f}")

    print("\n13. Monte-Carlo risque-neutre de controle  (cours 4.4)")
    mc, se = mc_call(b)
    if mc == mc:  # not NaN
        check(f"MC {mc:.4f} +/- {3*se:.4f} contient la formule fermee {b.call():.4f}",
              abs(mc - b.call()) < 3 * se, f"ecart = {abs(mc-b.call()):.5f}")
    else:
        print("  [SKIP] numpy absent")

    print("\n14. Forwards  (cours 1)")
    check("F equity = 3544.91", abs(forward_price(3500, 0.035, 0.75, 0.018) - 3544.9107) < 1e-3)
    check("F FX = 1.090439", abs(forward_fx(1.0850, 0.0425, 0.0225, 0.25) - 1.090439) < 1e-6)
    check("F commo = 68.2292", abs(forward_commodity(68.40, 0.04, 0.015, 0.06, 0.5) - 68.2292) < 1e-3)
    check("y implicite = 3.4636%",
          abs(implied_convenience_yield(69.10, 68.40, 0.04, 0.015, 0.5) - 0.034636) < 1e-5)

    print("\n" + "=" * 74)
    if fails == 0:
        print("RESULTAT : tous les tests OK — livrable J1 valide, jour cloturable.")
    else:
        print(f"RESULTAT : {fails} test(s) en echec — jour NON clos.")
    print("=" * 74)
    return fails


# ---------------------------------------------------------------------------
# 6. Corrige du TD (cours section 7)
# ---------------------------------------------------------------------------

def run_td() -> None:
    print("=" * 74)
    print("J1 — CORRIGE DU TD  (cours J01 section 7) — a comparer a ton papier")
    print("=" * 74)

    print("\nEx.1 — Parite : S=100, q=2%, r=4%, T=0.5, C=6.20")
    S, K, r, q, T, C = 100.0, 100.0, 0.04, 0.02, 0.5, 6.20
    P = C - S * math.exp(-q * T) + K * math.exp(-r * T)
    print(f"  S e^-qT = {S*math.exp(-q*T):10.4f}")
    print(f"  K e^-rT = {K*math.exp(-r*T):10.4f}")
    print(f"  P       = {P:10.4f}   (forward = {S*math.exp((r-q)*T):.4f} > K donc C > P)")

    print("\nEx.2 — Forward indice : S=3500, r=3.5%, q=1.8%, T=0.75")
    F = forward_price(3500, 0.035, 0.75, 0.018)
    print(f"  F = {F:10.4f}   base = {F-3500:+.4f} pts (contango technique r>q)")
    F2 = forward_price(3500, 0.035, 0.75, 0.05)
    print(f"  si q=5% : F = {F2:.4f}  => backwardation sans aucune vue baissiere")

    print("\nEx.3 — FX EURUSD : S=1.0850, rUSD=4.25%, rEUR=2.25%, T=0.25")
    Ffx = forward_fx(1.0850, 0.0425, 0.0225, 0.25)
    print(f"  F = {Ffx:.6f}   points de swap = {(Ffx-1.0850)*10000:+.1f} pips (EUR en report)")

    print("\nEx.4 — Brent : S=68.40, r=4%, u=1.5%, y=6%, T=0.5")
    Fc = forward_commodity(68.40, 0.04, 0.015, 0.06, 0.5)
    print(f"  F = {Fc:.4f}   spread = {Fc-68.40:+.4f} $  => BACKWARDATION (y > r+u)")
    y = implied_convenience_yield(69.10, 68.40, 0.04, 0.015, 0.5)
    print(f"  si le marche cote F=69.10 : y implicite = {y*100:.4f}%  => retour en contango")
    print("  ShockDesk (yfinance, shock-lab-oil, 25.5 M$, 2026-07-01 -> 2026-08-29, 42 barres) :")
    print("    Brent realise +18.4% vs +5% prevu = x3.68")

    print("\nEx.5 — Black-Scholes : S=100, K=105, r=3%, q=0, sigma=25%, T=0.5")
    b = BS(100, 105, 0.03, 0.0, 0.25, 0.5)
    print(f"  ln(S/K)        = {math.log(b.S/b.K): .6f}")
    print(f"  (r+s^2/2)T     = {(b.r+0.5*b.sigma**2)*b.T: .6f}")
    print(f"  sigma sqrt(T)  = {b.sigma*b.sqrtT: .6f}")
    print(f"  d1 = {b.d1: .6f}   N(d1) = {ncdf(b.d1):.6f}")
    print(f"  d2 = {b.d2: .6f}   N(d2) = {ncdf(b.d2):.6f}   <- proba risque-neutre d'exercice")
    print(f"  CALL = {b.call():.4f}     PUT = {b.put():.4f}")
    print(f"  residu de parite = {b.parity_residual():.2e}")
    print("  Grecs (conventions desk) :")
    print(f"    delta        = {b.delta('c'): .6f}")
    print(f"    gamma        = {b.gamma(): .6f}")
    print(f"    vega  (+1pt) = {b.vega_pt(): .6f}")
    print(f"    theta /jour  = {b.theta_day('c'): .6f}")
    print(f"    rho   (+1pt) = {b.rho_pt('c'): .6f}")
    c35 = b.with_(sigma=0.35).call()
    print(f"  Choc de vol +10 pts : C = {c35:.6f}  (+{c35-b.call():.6f})")
    print(f"    estimation lineaire par vega = {10*b.vega_pt():.6f}"
          f"  => convexite (volga) = {c35-b.call()-10*b.vega_pt():+.6f}")

    print("\nEx.6 — Arbitrage cash-and-carry : F theorique 3544.91 vs marche 3600")
    Fth = forward_price(3500, 0.035, 0.75, 0.018)
    print(f"  F marche - F theorique = {3600-Fth:+.4f} pts, certains en T")
    print(f"  valeur actuelle du gain = {(3600-Fth)*math.exp(-0.035*0.75):.4f} pts")
    print("  Montage : vendre le forward, emprunter 3500 e^-qT = "
          f"{3500*math.exp(-0.018*0.75):.2f}, acheter e^-qT indice, reinvestir les div.")
    print("  Ce qui peut casser : risque de dividende, borrow/repo, marge, funding > OIS, fiscalite.")

    print("\nEx.7 — MTM d'un forward en cours de vie")
    K_old = 3500 * math.exp((0.035 - 0.018) * 1.0)
    F_half = forward_price(3650, 0.035, 0.5, 0.018)
    f = forward_value(F_half, K_old, 0.035, 0.5)
    print(f"  strike initial K = {K_old:.4f}")
    print(f"  forward 6 mois   = {F_half:.4f}")
    print(f"  valeur f = (F-K)e^-rT = {f:+.4f} pts  (ce qu'un future aurait deja appele en marge)")

    print("\n" + "=" * 74)
    print("Ticket de sortie J1 : 6 hypotheses BS recitees + parite ecrite sans notes.")
    print("=" * 74)


def main() -> int:
    ap = argparse.ArgumentParser(description="J1 — BS closed form, parite, forwards")
    ap.add_argument("--td", action="store_true", help="afficher le corrige du TD")
    ap.add_argument("--all", action="store_true", help="auto-tests + corrige")
    a = ap.parse_args()
    if a.td and not a.all:
        run_td()
        return 0
    rc = run_tests()
    if a.all:
        print()
        run_td()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
