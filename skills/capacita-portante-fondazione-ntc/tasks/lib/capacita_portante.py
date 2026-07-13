#!/usr/bin/env python3
"""Capacita' portante fondazioni superficiali - FHWA NHI-06-089 par. 8.4 + NTC 2018 par. 6.4.2.1.

Riferimenti:
  - FHWA NHI-06-089 "Soils and Foundations - Reference Manual Volume II"
    (U.S. DOT, dicembre 2006, pubblico dominio), par. 8.4:
      eq. [8-2] Nq = e^(pi*tan phi) * tan^2(45+phi/2)
      eq. [8-3] Nc = (Nq-1)*cot(phi) per phi>0; [8-4] Nc = 5,14 per phi=0
      eq. [8-5] Ngamma = 2*(Nq+1)*tan(phi)
      eq. [8-6] forma generale con fattori correttivi (qui: base e piano
        campagna orizzontali, carico verticale)
      eq. [8-7..8-9] dimensioni efficaci B' = B-2eB, L' = L-2eL, A' = B'L'
      Table 8-4 fattori di forma; Table 8-5 falda (Cwq, Cwgamma, con
        interpolazione); Table 8-6 dq (default conservativo 1,0)
  - NTC 2018 par. 6.4.2.1 + Tab. 6.4.I: verifica GEO carico limite in
    Approccio 2 (A1+M1+R3), gamma_R = 2,3; Tab. 6.2.II: M1 = 1,0 (parametri
    di progetto = caratteristici); cap. 12: uso di altri codici
    internazionali sotto responsabilita' del progettista.

Convenzioni: kPa, kN/m3, m; angoli in gradi. Il modulo calcola qult, la
resistenza di progetto q_Rd = qult/gamma_R e R_d = q_Rd*A', e confronta con
Ed se fornito. Casi fuori ambito (carico inclinato, base inclinata, pendio,
terreni stratificati, rottura locale/punzonamento, sisma) NON sono
implementati: vengono rifiutati o segnalati. Non sostituisce il calcolo
geotecnico del progettista.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

GAMMA_R_CARICO_LIMITE = 2.3   # Tab. 6.4.I NTC 2018 (R3)
STRIP_RATIO = 10.0            # L/B >= 10: nastro (FHWA 8.4.3.1)
ECC_LIMITE_TERRENO = 1.0 / 6.0  # e < B/6 su terreno (FHWA 8.4.3.1)


def _finite(value: Any, name: str, positive: bool = True, nonneg: bool = False) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: valore non numerico") from exc
    if not math.isfinite(x):
        raise ValueError(f"{name}: valore non finito")
    if positive and x <= 0.0:
        raise ValueError(f"{name}: deve essere > 0")
    if nonneg and x < 0.0:
        raise ValueError(f"{name}: deve essere >= 0")
    return x


def fattori_capacita(phi_deg: float) -> Dict[str, float]:
    """Nc, Nq, Ngamma da eq. [8-2][8-3][8-4][8-5] FHWA (espressioni AASHTO)."""
    phi = _finite(phi_deg, "phi (gradi)", positive=False, nonneg=True)
    if phi >= 60.0:
        raise ValueError("phi >= 60 gradi: fuori dal dominio pratico della formulazione")
    r = math.radians(phi)
    nq = math.exp(math.pi * math.tan(r)) * math.tan(math.radians(45.0 + phi / 2.0)) ** 2
    nc = 2.0 + math.pi if phi == 0.0 else (nq - 1.0) / math.tan(r)
    ngamma = 2.0 * (nq + 1.0) * math.tan(r)
    return {"Nc": nc, "Nq": nq, "Ngamma": ngamma}


def fattori_forma(phi_deg: float, b_eff: float, l_eff: float,
                  nc: float, nq: float) -> Dict[str, float]:
    """Table 8-4 FHWA. Applicati se L/B < 10 (nastro: tutti 1)."""
    if l_eff / b_eff >= STRIP_RATIO:
        return {"sc": 1.0, "sq": 1.0, "sgamma": 1.0}
    rapporto = b_eff / l_eff
    if phi_deg == 0.0:
        return {"sc": 1.0 + rapporto / 5.0, "sq": 1.0, "sgamma": 1.0}
    r = math.radians(phi_deg)
    return {
        "sc": 1.0 + rapporto * (nq / nc),
        "sq": 1.0 + rapporto * math.tan(r),
        "sgamma": 1.0 - 0.4 * rapporto,
    }


def fattori_falda(dw: Optional[float], df: float, b_eff: float) -> Dict[str, float]:
    """Table 8-5 FHWA con interpolazione lineare (DW dal piano campagna)."""
    soglia = 1.5 * b_eff + df
    if dw is None:
        return {"Cwq": 1.0, "Cwgamma": 1.0, "DW_soglia_no_effetto": soglia}
    w = _finite(dw, "DW (profondita' falda dal p.c., m)", positive=False, nonneg=True)
    if w >= soglia:
        cwq, cwg = 1.0, 1.0
    elif w <= df:
        # Cwq: 0,5 (DW=0) -> 1,0 (DW=Df); Cwgamma costante 0,5 fino a Df
        cwq = 0.5 + 0.5 * (w / df) if df > 0 else 1.0
        cwg = 0.5
    else:
        cwq = 1.0
        cwg = 0.5 + 0.5 * (w - df) / (soglia - df)
    return {"Cwq": cwq, "Cwgamma": cwg, "DW_soglia_no_effetto": soglia}


@dataclass
class Risultato:
    qult_kpa: float
    q_rd_kpa: float
    r_d_kn: float
    dettaglio: Dict[str, Any]
    avvertenze: List[str] = field(default_factory=list)
    esito_ed: Optional[bool] = None


def capacita_portante(
    B: float,
    L: Optional[float],
    Df: float,
    gamma_sotto: float,
    condizione: str,
    c: float = 0.0,
    phi: float = 0.0,
    gamma_sopra: Optional[float] = None,
    q_appl: float = 0.0,
    eB: float = 0.0,
    eL: float = 0.0,
    DW: Optional[float] = None,
    dq: float = 1.0,
    Ed_kn: Optional[float] = None,
) -> Risultato:
    """Carico limite (FHWA 8.4) e resistenza di progetto NTC (gamma_R = 2,3).

    B, L [m] (L assente -> nastro); Df [m]; pesi [kN/m3]; c/cu [kPa];
    phi [gradi]; q_appl [kPa]; eB/eL [m]; DW [m dal piano campagna];
    Ed [kN] = componente normale della risultante di progetto (A1).
    """
    b = _finite(B, "B (m)")
    df = _finite(Df, "Df (m)", positive=False, nonneg=True)
    g_sotto = _finite(gamma_sotto, "gamma_sotto (kN/m3)")
    g_sopra = g_sotto if gamma_sopra is None else _finite(gamma_sopra, "gamma_sopra (kN/m3)")
    qa = _finite(q_appl, "q_appl (kPa)", positive=False, nonneg=True)
    dq_v = _finite(dq, "dq", positive=True)
    e_b = _finite(eB, "eB (m)", positive=False, nonneg=True)
    e_l = _finite(eL, "eL (m)", positive=False, nonneg=True)

    avv: List[str] = []

    if condizione == "non-drenata":
        if phi not in (0, 0.0):
            raise ValueError("condizione non-drenata: phi deve essere 0 (c = cu)")
        c_v = _finite(c, "cu (kPa)")
        phi_v = 0.0
    elif condizione == "drenata":
        phi_v = _finite(phi, "phi (gradi)", positive=False, nonneg=True)
        c_v = _finite(c, "c' (kPa)", positive=False, nonneg=True)
        if phi_v == 0.0 and c_v == 0.0:
            raise ValueError("condizione drenata: fornire phi' > 0 e/o c' > 0")
    else:
        raise ValueError("condizione: usare 'drenata' o 'non-drenata'")

    # geometria: nastro o rettangolare; dimensioni efficaci (eq. 8-7..8-9)
    if L is None:
        if e_l > 0:
            raise ValueError("eL richiede L (fondazione rettangolare)")
        nastro = True
        l_v = STRIP_RATIO * b  # solo per i rapporti; A' per metro non usato
    else:
        l_v = _finite(L, "L (m)")
        if l_v < b:
            raise ValueError("L < B: per convenzione B e' la dimensione minore")
        nastro = l_v / b >= STRIP_RATIO

    # limiti di eccentricita' su terreno (FHWA 8.4.3.1): e < dim/6
    if e_b >= b * ECC_LIMITE_TERRENO or (L is not None and e_l >= l_v * ECC_LIMITE_TERRENO):
        raise ValueError(
            "eccentricita' oltre il limite di 1/6 della dimensione (fondazione "
            "su terreno, FHWA 8.4.3.1): 'the footing should be resized'. "
            "Ridimensionare la fondazione; la skill non calcola oltre il limite."
        )
    b_eff = b - 2.0 * e_b
    l_eff = l_v - 2.0 * e_l

    fat = fattori_capacita(phi_v)
    forma = fattori_forma(phi_v, b_eff, l_eff, fat["Nc"], fat["Nq"])
    falda = fattori_falda(DW, df, b_eff)

    if dq_v != 1.0:
        avv.append(
            "dq diverso da 1,0 fornito dall'utente: la Table 8-6 FHWA lo "
            "ammette solo con rinterro granulare compattato di qualita' e "
            "permanente, e con terreni sopra il piano di posa competenti "
            "quanto quelli sottostanti; altrimenti dq = 1,0 (omissione "
            "conservativa). Responsabilita' del progettista."
        )
    if DW is None:
        avv.append(
            f"DW non fornita: assunta falda profonda (DW >= 1,5B+Df = "
            f"{falda['DW_soglia_no_effetto']:.2f} m dal p.c., Table 8-5). "
            "Verificare."
        )

    # eq. [8-6] con base e piano campagna orizzontali, carico verticale;
    # sovraccarico secondo la nota all'eq. 8-6: (qa + gamma_a*Df*dq)
    termine_c = c_v * fat["Nc"] * forma["sc"]
    termine_q = (qa + g_sopra * df * dq_v) * fat["Nq"] * falda["Cwq"] * forma["sq"]
    termine_g = 0.5 * g_sotto * b_eff * fat["Ngamma"] * falda["Cwgamma"] * forma["sgamma"]
    qult = termine_c + termine_q + termine_g

    q_rd = qult / GAMMA_R_CARICO_LIMITE
    a_eff = b_eff * l_eff if L is not None else b_eff * 1.0  # per metro se nastro
    r_d = q_rd * a_eff

    avv.extend([
        "Verifica NTC: Approccio 2 (A1+M1+R3), gamma_R = 2,3 (Tab. 6.4.I "
        "carico limite); parametri geotecnici caratteristici = di progetto "
        "(M1 = 1,0, Tab. 6.2.II). Ed = componente NORMALE della risultante "
        "di progetto con coefficienti A1 (Tab. 6.2.I), a carico dell'utente.",
        "Formulazione del carico limite da FHWA NHI-06-089 par. 8.4, usata "
        "come altro codice internazionale ex cap. 12 NTC 2018: livelli di "
        "sicurezza coerenti sotto la responsabilita' del progettista.",
        "Ipotesi della formulazione: terreno omogeneo, rottura generale, "
        "base e piano campagna orizzontali, carico verticale (eventualmente "
        "eccentrico). Fuori ambito: carico inclinato, base inclinata, "
        "pendio, terreni stratificati, rottura locale/punzonamento, azioni "
        "sismiche (NTC 7.11.5.3.1), scorrimento (gamma_R = 1,1) e "
        "stabilita' globale.",
    ])
    if L is None:
        avv.append("Fondazione a nastro: R_d espressa per metro di sviluppo (A' = B' x 1 m).")

    ris = Risultato(
        qult_kpa=qult,
        q_rd_kpa=q_rd,
        r_d_kn=r_d,
        dettaglio={
            "condizione": condizione,
            "nastro_L_su_B_maggiore_uguale_10": nastro,
            "B_eff_m": round(b_eff, 4),
            "L_eff_m": None if L is None else round(l_eff, 4),
            "A_eff_m2": round(a_eff, 4),
            "fattori_N": {k: round(v, 3) for k, v in fat.items()},
            "fattori_forma": {k: round(v, 4) for k, v in forma.items()},
            "fattori_falda": {k: round(v, 4) for k, v in falda.items() if k != "DW_soglia_no_effetto"},
            "dq": dq_v,
            "termini_kpa": {
                "coesione": round(termine_c, 2),
                "sovraccarico": round(termine_q, 2),
                "peso": round(termine_g, 2),
            },
            "gamma_R": GAMMA_R_CARICO_LIMITE,
        },
        avvertenze=avv,
    )
    if Ed_kn is not None:
        ed = _finite(Ed_kn, "Ed (kN)")
        ris.esito_ed = ed <= r_d
        ris.dettaglio["Ed_kn"] = ed
        if not ris.esito_ed:
            ris.avvertenze.append(
                "Ed > Rd: la condizione [6.2.1] NON e' soddisfatta per il "
                "carico limite. Rivedere geometria/piano di posa o parametri "
                "con il progettista."
            )
    return ris


def _to_json(ris: Risultato) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "formulazione": (
            "FHWA NHI-06-089 par. 8.4 (eq. 8-2..8-6, Tab. 8-4/8-5), codice "
            "internazionale ex cap. 12 NTC 2018; verifica NTC 6.4.2.1 "
            "Approccio 2 con gamma_R = 2,3 (Tab. 6.4.I)"
        ),
        "qult_kPa": round(ris.qult_kpa, 2),
        "q_Rd_kPa": round(ris.q_rd_kpa, 2),
        "R_d_kN": round(ris.r_d_kn, 2),
        "dettaglio": ris.dettaglio,
        "avvertenze": ris.avvertenze,
    }
    if ris.esito_ed is not None:
        out["Ed_minore_uguale_Rd"] = ris.esito_ed
    return out


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Capacita' portante fondazione superficiale (FHWA NHI-06-089 "
            "par. 8.4 + NTC 6.4.2.1). Output JSON su stdout."
        )
    )
    ap.add_argument("--b", type=float, required=True, help="B, lato minore [m]")
    ap.add_argument("--l", type=float, help="L [m]; assente = nastro")
    ap.add_argument("--df", type=float, required=True, help="profondita' piano di posa [m]")
    ap.add_argument("--gamma", type=float, required=True, help="peso unita' volume sotto il piano di posa [kN/m3]")
    ap.add_argument("--gamma-sopra", type=float, help="peso unita' volume sopra il piano di posa [kN/m3] (default = gamma)")
    ap.add_argument("--condizione", required=True, choices=["drenata", "non-drenata"])
    ap.add_argument("--c", type=float, default=0.0, help="c' o cu [kPa]")
    ap.add_argument("--phi", type=float, default=0.0, help="phi' [gradi] (0 se non drenata)")
    ap.add_argument("--q-appl", type=float, default=0.0, help="sovraccarico applicato al piano di posa [kPa]")
    ap.add_argument("--eb", type=float, default=0.0, help="eccentricita' in direzione B [m]")
    ap.add_argument("--el", type=float, default=0.0, help="eccentricita' in direzione L [m]")
    ap.add_argument("--dw", type=float, help="profondita' falda dal piano campagna [m]")
    ap.add_argument("--dq", type=float, default=1.0, help="fattore di approfondimento (Table 8-6; default 1,0)")
    ap.add_argument("--ed", type=float, help="Ed [kN], componente normale della risultante di progetto (A1)")
    args = ap.parse_args(argv)

    try:
        ris = capacita_portante(
            B=args.b, L=args.l, Df=args.df, gamma_sotto=args.gamma,
            condizione=args.condizione, c=args.c, phi=args.phi,
            gamma_sopra=args.gamma_sopra, q_appl=args.q_appl,
            eB=args.eb, eL=args.el, DW=args.dw, dq=args.dq, Ed_kn=args.ed,
        )
    except ValueError as exc:
        print(json.dumps({"errore": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(_to_json(ris), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
