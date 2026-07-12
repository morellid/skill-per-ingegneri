#!/usr/bin/env python3
"""Cedimento di consolidazione primaria - FHWA NHI-06-088 par. 7.5.2 (ex cap. 12 NTC 2018).

Riferimenti:
  - FHWA NHI-06-088 "Soils and Foundations - Reference Manual Volume I"
    (U.S. DOT, dicembre 2006, pubblico dominio), par. 7.5.2:
      eq. [7-2] NC:  Sc = sum( Cc/(1+e0) * H0 * log10(pf/p0) )
      eq. [7-4] OC (pf > pc): S = sum( H0/(1+e0) * (Cr*log10(pc/p0) + Cc*log10(pf/pc)) )
      eq. [7-6] UC (pc < p0): S = sum( H0/(1+e0) * (Cc*log10(p0/pc) + Cc*log10(pf/p0)) )
  - NTC 2018 cap. 12: uso di "altri codici internazionali" per quanto non
    trattato dalla norma, sotto responsabilita' del progettista.
  - NTC 2018 par. 6.2.4.3: quadro SLE (Ed <= Cd), sovraordinato al calcolo.

Convenzioni:
  - tensioni in kPa (o qualunque unita' coerente: nelle equazioni compaiono
    solo rapporti), spessori in m, cedimenti restituiti in m e mm;
  - ogni strato e' un sublayer con tensioni riferite al suo centro e
    proprieta' costanti (FHWA 7.5.2.2);
  - il caso OC con pf <= pc NON e' coperto dalle equazioni trascritte
    (le eq. 7-4/7-5 valgono per pf > pc): il modulo lo rifiuta;
  - il caso OCR < 1 e' accettato SOLO se dichiarato esplicitamente come
    sottoconsolidazione reale (sottoconsolidato=True): in assenza di
    dichiarazione viene rifiutato come probabile errore nei dati.

Output deterministico. Il modulo calcola il solo cedimento di consolidazione
PRIMARIA: niente decorso nel tempo, niente compressione secondaria, niente
diffusione delle tensioni (delta_p e' un input). Non sostituisce il calcolo
geotecnico del progettista.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

OCR_TOL = 1e-9  # tolleranza numerica per pc ~= p0 (caso NC)


def _finite_pos(value: Any, name: str) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: valore non numerico") from exc
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name}: deve essere un numero finito > 0")
    return x


def _finite_nonneg(value: Any, name: str) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: valore non numerico") from exc
    if not math.isfinite(x) or x < 0.0:
        raise ValueError(f"{name}: deve essere un numero finito >= 0")
    return x


@dataclass
class RisultatoStrato:
    caso: str                 # "NC" | "OC" | "UC"
    equazione: str            # "[7-2]" | "[7-4]" | "[7-6]"
    s_m: float
    ocr: float
    sigma_f: float
    dettaglio: Dict[str, float]
    avvertenze: List[str] = field(default_factory=list)


def cedimento_strato(
    h0: float,
    e0: float,
    Cc: float,
    sigma_0: float,
    delta_sigma: float,
    sigma_p: Optional[float] = None,
    Cr: Optional[float] = None,
    sottoconsolidato: bool = False,
) -> RisultatoStrato:
    """Cedimento di consolidazione primaria di un singolo strato/sublayer.

    h0 [m], e0 [-], Cc [-], Cr [-], tensioni [kPa o unita' coerente], al
    centro dello strato. sigma_p assente -> NC (pc = p0, FHWA 7.5.2).
    """
    h = _finite_pos(h0, "h0 (spessore, m)")
    e = _finite_nonneg(e0, "e0 (indice dei vuoti)")
    cc = _finite_pos(Cc, "Cc (indice di compressione)")
    p0 = _finite_pos(sigma_0, "sigma_0 (tensione efficace iniziale)")
    dp = _finite_pos(delta_sigma, "delta_sigma (incremento di tensione)")
    pf = p0 + dp

    pc = p0 if sigma_p is None else _finite_pos(sigma_p, "sigma_p (preconsolidazione)")
    ocr = pc / p0
    avv: List[str] = []

    if abs(ocr - 1.0) <= OCR_TOL:
        # NC - eq. [7-2]
        s = cc / (1.0 + e) * h * math.log10(pf / p0)
        ris = RisultatoStrato(
            caso="NC",
            equazione="[7-2]",
            s_m=s,
            ocr=1.0,
            sigma_f=pf,
            dettaglio={"termine_NC_m": s},
        )
    elif ocr > 1.0:
        # OC - eq. [7-4], valida per pf > pc
        if pf <= pc:
            raise ValueError(
                "caso OC con sigma_f <= sigma_p: le equazioni trascritte "
                "dalla fonte (FHWA 7-4/7-5) valgono per pf > pc; il caso in "
                "cui il carico finale resta sotto la preconsolidazione non "
                "e' coperto dalla skill. Rinvio al progettista/alla fonte."
            )
        if Cr is None:
            raise ValueError(
                "caso OC (OCR > 1): richiesto Cr (indice di ricompressione) "
                "per il ramo pc/p0 dell'eq. 7-4"
            )
        cr = _finite_pos(Cr, "Cr (indice di ricompressione)")
        if cr > cc:
            avv.append(
                "Cr > Cc: l'indice di ricompressione dichiarato supera "
                "quello di compressione vergine; verificare i dati "
                "edometrici."
            )
        t_oc = h / (1.0 + e) * cr * math.log10(pc / p0)
        t_nc = h / (1.0 + e) * cc * math.log10(pf / pc)
        ris = RisultatoStrato(
            caso="OC",
            equazione="[7-4]",
            s_m=t_oc + t_nc,
            ocr=ocr,
            sigma_f=pf,
            dettaglio={"termine_ricompressione_m": t_oc, "termine_vergine_m": t_nc},
            avvertenze=avv,
        )
    else:
        # OCR < 1
        if not sottoconsolidato:
            raise ValueError(
                "OCR < 1 (sigma_p < sigma_0): o i dati edometrici sono "
                "errati (verificare sigma_p, unita' di misura, scambio di "
                "colonne) oppure il terreno e' realmente sottoconsolidato "
                "(consolidazione ancora in corso, FHWA 7.5.2.3). In "
                "quest'ultimo caso rieseguire dichiarando esplicitamente "
                "sottoconsolidato=True (CLI: --sottoconsolidato)."
            )
        t_corr = h / (1.0 + e) * cc * math.log10(p0 / pc)
        t_add = h / (1.0 + e) * cc * math.log10(pf / p0)
        avv.append(
            "Terreno dichiarato sottoconsolidato (OCR < 1): il primo "
            "termine dell'eq. 7-6 e' la consolidazione ancora in corso "
            "sotto il carico esistente; se ignorata, il cedimento totale "
            "verrebbe sottostimato (FHWA 7.5.2.3). La condizione di "
            "sottoconsolidazione deve essere giustificata dal progettista."
        )
        ris = RisultatoStrato(
            caso="UC",
            equazione="[7-6]",
            s_m=t_corr + t_add,
            ocr=ocr,
            sigma_f=pf,
            dettaglio={"termine_in_corso_m": t_corr, "termine_incremento_m": t_add},
            avvertenze=avv,
        )
    return ris


def cedimento_multistrato(
    strati: List[Dict[str, Any]],
    sottoconsolidato: bool = False,
) -> Dict[str, Any]:
    """Somma i contributi di n strati/sublayer (FHWA 7.5.2.2: S = somma)."""
    if not strati:
        raise ValueError("strati: fornire almeno uno strato")
    out_strati: List[Dict[str, Any]] = []
    totale = 0.0
    avvertenze_globali = [
        "Tensioni riferite al CENTRO di ciascuno strato/sublayer, "
        "proprieta' costanti nel sublayer (FHWA 7.5.2.2). Spessori tipici "
        "dei sublayer 1,5-3 m.",
        "Il modulo calcola il solo cedimento di consolidazione primaria: "
        "decorso nel tempo (FHWA 7.5.3) e compressione secondaria (FHWA "
        "7.5.4) sono fuori ambito.",
        "delta_sigma (diffusione delle tensioni) e' un input del "
        "progettista: la skill non lo calcola.",
        "Quadro NTC sovraordinato: confrontare il risultato con il limite "
        "Cd dichiarato dal progetto (NTC 6.2.4.3, Ed <= Cd [6.2.7]); l'uso "
        "del codice internazionale FHWA avviene ai sensi del cap. 12 NTC "
        "sotto la responsabilita' del progettista.",
    ]
    for i, strato in enumerate(strati, start=1):
        ris = cedimento_strato(
            h0=strato.get("h0"),
            e0=strato.get("e0"),
            Cc=strato.get("Cc"),
            sigma_0=strato.get("sigma_0"),
            delta_sigma=strato.get("delta_sigma"),
            sigma_p=strato.get("sigma_p"),
            Cr=strato.get("Cr"),
            sottoconsolidato=bool(strato.get("sottoconsolidato", sottoconsolidato)),
        )
        totale += ris.s_m
        out_strati.append(
            {
                "strato": i,
                "caso": ris.caso,
                "equazione_FHWA": ris.equazione,
                "OCR": round(ris.ocr, 4),
                "sigma_f": round(ris.sigma_f, 4),
                "S_m": round(ris.s_m, 6),
                "S_mm": round(ris.s_m * 1000.0, 1),
                "epsilon_media": round(ris.s_m / float(strato["h0"]), 6),
                "dettaglio_m": {k: round(v, 6) for k, v in ris.dettaglio.items()},
                "avvertenze": ris.avvertenze,
            }
        )
    return {
        "formulazione": (
            "FHWA NHI-06-088 par. 7.5.2 (eq. 7-2/7-4/7-6), codice "
            "internazionale ex cap. 12 NTC 2018"
        ),
        "S_totale_m": round(totale, 6),
        "S_totale_mm": round(totale * 1000.0, 1),
        "strati": out_strati,
        "avvertenze": avvertenze_globali,
    }


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Cedimento di consolidazione primaria (FHWA NHI-06-088 par. "
            "7.5.2, ex cap. 12 NTC 2018). Output JSON su stdout. "
            "Singolo strato con i flag, oppure --json per multistrato."
        )
    )
    ap.add_argument("--json", help="file JSON con {\"strati\": [...]} per il multistrato")
    ap.add_argument("--h0", type=float, help="spessore strato [m]")
    ap.add_argument("--e0", type=float, help="indice dei vuoti iniziale")
    ap.add_argument("--cc", type=float, help="indice di compressione Cc")
    ap.add_argument("--cr", type=float, help="indice di ricompressione Cr (caso OC)")
    ap.add_argument("--sigma0", type=float, help="tensione efficace iniziale al centro [kPa]")
    ap.add_argument("--sigmap", type=float, help="tensione di preconsolidazione [kPa]")
    ap.add_argument("--dsigma", type=float, help="incremento di tensione [kPa]")
    ap.add_argument(
        "--sottoconsolidato",
        action="store_true",
        help="dichiara sottoconsolidazione reale (abilita eq. 7-6 per OCR < 1)",
    )
    args = ap.parse_args(argv)

    try:
        if args.json:
            with open(args.json, encoding="utf-8") as fh:
                data = json.load(fh)
            out = cedimento_multistrato(
                data["strati"], sottoconsolidato=bool(data.get("sottoconsolidato", False))
            )
        else:
            strato = {
                "h0": args.h0,
                "e0": args.e0,
                "Cc": args.cc,
                "Cr": args.cr,
                "sigma_0": args.sigma0,
                "sigma_p": args.sigmap,
                "delta_sigma": args.dsigma,
                "sottoconsolidato": args.sottoconsolidato,
            }
            out = cedimento_multistrato([strato])
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"errore": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
