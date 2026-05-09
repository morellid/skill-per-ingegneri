#!/usr/bin/env python3
"""Cedimento edometrico per compressione monodimensionale - SLE NTC 2018 par. 6.2.4.

Riferimenti normativi e tecnici:
  - DM 17/01/2018 (NTC 2018) par. 6.2.2 (analisi interazione terreno-fondazione),
    par. 6.2.4 (verifiche agli stati limite di esercizio - cedimenti)
  - Circolare MIT n. 7 del 21/01/2019 par. C6.2

NTC fornisce il framework SLE (limiti di cedimento ammissibili, scelta del
metodo di calcolo) ma non riproduce la formula chiusa: la skill applica
la formulazione classica della meccanica dei terreni (compressione
monodimensionale, Terzaghi 1925, Skempton 1944), ampiamente trattata nei
testi standard di geotecnica (Lancellotta "Geotecnica", Cestari, Colombo).

Caso coperto: singolo strato omogeneo con tensione media iniziale
sigma_0', preconsolidazione sigma_p', incremento Delta sigma_v' uniforme,
parametri edometrici Cc (indice di compressione, ramo NC) e Cr (indice
di ricompressione, ramo OC).

Formula a tratti:
  caso OC (sigma_f' <= sigma_p'):
      Delta h = h0/(1+e0) * Cr * log10(sigma_f'/sigma_0')
  caso NC (sigma_0' >= sigma_p'):
      Delta h = h0/(1+e0) * Cc * log10(sigma_f'/sigma_0')
  caso transizione (sigma_0' < sigma_p' < sigma_f'):
      Delta h = h0/(1+e0) * [Cr * log10(sigma_p'/sigma_0')
                             + Cc * log10(sigma_f'/sigma_p')]

Output deterministico, formule chiuse. La skill NON sostituisce la
relazione geotecnica del progettista firmatario: il metodo edometrico
e' una stima di pre-dimensionamento; per cedimenti differenziali, strati
multipli, scarichi a profondita', consolidazione 2D/3D o terreni
strutturati il progettista deve usare metodi specifici.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


def _finite(value: Any, field_name: str) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name}: valore non numerico") from exc
    if not math.isfinite(x):
        raise ValueError(f"{field_name}: valore non finito")
    return x


def _positive(value: float, field_name: str) -> float:
    if value <= 0:
        raise ValueError(f"{field_name}: deve essere positivo, ricevuto {value}")
    return value


def _non_negative(value: float, field_name: str) -> float:
    if value < 0:
        raise ValueError(f"{field_name}: non puo' essere negativo, ricevuto {value}")
    return value


def ocr(sigma_p: float, sigma_0: float) -> float:
    """OCR = sigma_p' / sigma_0' (Over-Consolidation Ratio)."""
    sigma_p = _positive(_finite(sigma_p, "sigma_p"), "sigma_p")
    sigma_0 = _positive(_finite(sigma_0, "sigma_0"), "sigma_0")
    return sigma_p / sigma_0


def cedimento_oc(h0: float, e0: float, c_r: float, sigma_0: float, sigma_f: float) -> float:
    """Cedimento ramo over-consolidato (sigma_f <= sigma_p): formula con Cr.

    Delta h = h0/(1+e0) * Cr * log10(sigma_f/sigma_0)
    """
    h0 = _positive(_finite(h0, "h0"), "h0")
    e0 = _positive(_finite(e0, "e0"), "e0")
    c_r = _positive(_finite(c_r, "Cr"), "Cr")
    sigma_0 = _positive(_finite(sigma_0, "sigma_0"), "sigma_0")
    sigma_f = _positive(_finite(sigma_f, "sigma_f"), "sigma_f")
    if sigma_f < sigma_0:
        raise ValueError(
            f"sigma_f = {sigma_f} kPa < sigma_0 = {sigma_0} kPa: la skill assume incremento "
            "di tensione non negativo (compressione). Per scarichi (rebound) la formula non si applica."
        )
    return h0 / (1.0 + e0) * c_r * math.log10(sigma_f / sigma_0)


def cedimento_nc(h0: float, e0: float, c_c: float, sigma_0: float, sigma_f: float) -> float:
    """Cedimento ramo normalmente consolidato (sigma_0 >= sigma_p): formula con Cc.

    Delta h = h0/(1+e0) * Cc * log10(sigma_f/sigma_0)
    """
    h0 = _positive(_finite(h0, "h0"), "h0")
    e0 = _positive(_finite(e0, "e0"), "e0")
    c_c = _positive(_finite(c_c, "Cc"), "Cc")
    sigma_0 = _positive(_finite(sigma_0, "sigma_0"), "sigma_0")
    sigma_f = _positive(_finite(sigma_f, "sigma_f"), "sigma_f")
    if sigma_f < sigma_0:
        raise ValueError(
            f"sigma_f = {sigma_f} kPa < sigma_0 = {sigma_0} kPa: la skill assume incremento "
            "di tensione non negativo (compressione)."
        )
    return h0 / (1.0 + e0) * c_c * math.log10(sigma_f / sigma_0)


@dataclass(frozen=True)
class RisultatoCedimento:
    # Input
    h0: float
    e0: float
    c_c: float
    c_r: float
    sigma_0: float
    sigma_p: float
    delta_sigma: float
    # Derivati
    sigma_f: float
    ocr: float
    ramo: str               # "OC" / "NC" / "transizione"
    # Output
    delta_h_oc_m: float     # contributo OC (zero se NC, parziale se transizione)
    delta_h_nc_m: float     # contributo NC (zero se OC, parziale se transizione)
    delta_h_m: float        # cedimento totale in m
    delta_h_mm: float       # cedimento totale in mm
    epsilon_media: float    # Delta h / h0
    avvertenze: List[str] = field(default_factory=list)
    riferimenti: List[str] = field(default_factory=list)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "input": {
                "h0_m": self.h0,
                "e0": self.e0,
                "Cc": self.c_c,
                "Cr": self.c_r,
                "sigma_0_kPa": self.sigma_0,
                "sigma_p_kPa": self.sigma_p,
                "delta_sigma_kPa": self.delta_sigma,
            },
            "derivati": {
                "sigma_f_kPa": round(self.sigma_f, 6),
                "OCR": round(self.ocr, 6),
                "ramo": self.ramo,
            },
            "output": {
                "delta_h_oc_m": round(self.delta_h_oc_m, 9),
                "delta_h_nc_m": round(self.delta_h_nc_m, 9),
                "delta_h_m": round(self.delta_h_m, 9),
                "delta_h_mm": round(self.delta_h_mm, 6),
                "epsilon_media": round(self.epsilon_media, 9),
                "avvertenze": list(self.avvertenze),
            },
            "riferimenti": list(self.riferimenti),
        }


def calcola_cedimento(
    h0: float,
    e0: float,
    c_c: float,
    c_r: float,
    sigma_0: float,
    sigma_p: float,
    delta_sigma: float,
) -> RisultatoCedimento:
    """Cedimento edometrico Delta h per singolo strato omogeneo.

    Parametri:
      - h0: spessore iniziale dello strato compressibile (m)
      - e0: indice dei vuoti iniziale (-)
      - Cc: indice di compressione, ramo vergine NC (-)
      - Cr: indice di ricompressione, ramo OC (-)
      - sigma_0: tensione efficace verticale media iniziale (kPa)
      - sigma_p: tensione efficace di preconsolidazione (kPa); deve essere >= sigma_0 (OCR >= 1)
      - delta_sigma: incremento tensione efficace verticale media (kPa); >= 0 (compressione)

    Output: contributi OC e NC, cedimento totale in m e mm, deformazione media,
    OCR, ramo (OC / NC / transizione), avvertenze e riferimenti.
    """
    h0 = _positive(_finite(h0, "h0"), "h0")
    e0 = _positive(_finite(e0, "e0"), "e0")
    c_c = _positive(_finite(c_c, "Cc"), "Cc")
    c_r = _positive(_finite(c_r, "Cr"), "Cr")
    sigma_0 = _positive(_finite(sigma_0, "sigma_0"), "sigma_0")
    sigma_p = _positive(_finite(sigma_p, "sigma_p"), "sigma_p")
    delta_sigma = _non_negative(_finite(delta_sigma, "delta_sigma"), "delta_sigma")

    if c_r > c_c:
        raise ValueError(
            f"Cr = {c_r} > Cc = {c_c}: il ramo di ricompressione deve avere indice "
            "minore o uguale al ramo vergine. Verificare i parametri edometrici."
        )
    if sigma_p < sigma_0:
        raise ValueError(
            f"sigma_p = {sigma_p} kPa < sigma_0 = {sigma_0} kPa: OCR < 1 non e' "
            "fisicamente ammissibile (preconsolidazione non puo' essere inferiore "
            "alla tensione attuale). Verificare i dati edometrici."
        )

    sigma_f = sigma_0 + delta_sigma
    ocr_value = sigma_p / sigma_0

    avvertenze: List[str] = []
    if delta_sigma == 0.0:
        avvertenze.append(
            "delta_sigma = 0: nessun incremento di tensione, cedimento atteso = 0."
        )

    # Determinazione ramo e calcolo a tratti
    if sigma_f <= sigma_p:
        # interamente OC
        ramo = "OC"
        d_oc = cedimento_oc(h0, e0, c_r, sigma_0, sigma_f)
        d_nc = 0.0
    elif sigma_0 >= sigma_p:
        # interamente NC (sigma_p == sigma_0 e sigma_f > sigma_0)
        ramo = "NC"
        d_oc = 0.0
        d_nc = cedimento_nc(h0, e0, c_c, sigma_0, sigma_f)
    else:
        # transizione: parte OC fino a sigma_p, poi NC fino a sigma_f
        ramo = "transizione"
        d_oc = cedimento_oc(h0, e0, c_r, sigma_0, sigma_p)
        d_nc = cedimento_nc(h0, e0, c_c, sigma_p, sigma_f)

    d_tot = d_oc + d_nc
    epsilon = d_tot / h0
    if epsilon > 0.10:
        avvertenze.append(
            f"deformazione media epsilon = {epsilon:.3f} > 10%: il metodo edometrico "
            "monodimensionale e' una stima; per deformazioni cosi' elevate il progettista "
            "deve valutare metodi non lineari (modulo edometrico variabile, consolidazione "
            "incrementale) e/o validare con prove edometriche specifiche."
        )

    riferimenti = [
        "NTC 2018 par. 6.2.2 - analisi dell'interazione terreno-fondazione",
        "NTC 2018 par. 6.2.4 - verifiche agli SLE: cedimenti ammissibili",
        "Circ. 7/2019 par. C6.2 - commento applicativo",
        "Formulazione classica meccanica dei terreni (Terzaghi 1925, Skempton 1944)",
        "Lancellotta R., 'Geotecnica' (riferimento didattico standard)",
    ]

    return RisultatoCedimento(
        h0=h0, e0=e0, c_c=c_c, c_r=c_r,
        sigma_0=sigma_0, sigma_p=sigma_p, delta_sigma=delta_sigma,
        sigma_f=sigma_f, ocr=ocr_value, ramo=ramo,
        delta_h_oc_m=d_oc, delta_h_nc_m=d_nc,
        delta_h_m=d_tot, delta_h_mm=d_tot * 1000.0,
        epsilon_media=epsilon,
        avvertenze=avvertenze,
        riferimenti=riferimenti,
    )


def _load_input(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("input JSON deve essere un oggetto")
    return data


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-json", required=True)
    args = parser.parse_args(argv)
    try:
        data = _load_input(args.input_json)
        risultato = calcola_cedimento(
            h0=data["h0"],
            e0=data["e0"],
            c_c=data["Cc"],
            c_r=data["Cr"],
            sigma_0=data["sigma_0"],
            sigma_p=data["sigma_p"],
            delta_sigma=data["delta_sigma"],
        )
        print(json.dumps(risultato.as_dict(), indent=2, ensure_ascii=False))
    except KeyError as exc:
        print(f"ERRORE: campo mancante nel JSON: {exc}", file=sys.stderr)
        return 2
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERRORE: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
