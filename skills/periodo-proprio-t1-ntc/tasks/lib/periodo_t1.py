#!/usr/bin/env python3
"""Stima del periodo proprio T1 - NTC 2018 par. 7.3.3.2 + Circ. 7/2019 par. C7.3.3.2.

Riferimenti normativi:
  - DM 17/01/2018 (NTC 2018) par. 7.3.3.2 - formula [7.3.6]: T1 = 2*sqrt(d)
  - DM 17/01/2018 (NTC 2018) par. 2.5.3 - combinazione masse [2.5.7]
  - Circolare MIT n. 7 del 21/01/2019 par. C7.3.3.2 - formula [C7.3.2]:
    T1 = C1*H^(3/4), con C1 tabellato per tipologia strutturale

Implementa le due stime del periodo del modo di vibrare principale T1:
  - metodo "ntc" [7.3.6]: da spostamento laterale elastico d [m] del punto
    piu' alto dell'edificio sotto la combinazione [2.5.7] applicata in
    orizzontale (richiede un modello di calcolo);
  - metodo "circolare" [C7.3.2]: da altezza H [m] dal piano di fondazione e
    tipologia strutturale (prima approssimazione, senza modello).

Se fornito TC (periodo dello spettro, da calcolare a parte, ad es. con la
skill spettro-risposta-ntc), il modulo valuta anche:
  - condizione T1 <= 2,5*TC per l'analisi lineare statica (NTC 7.3.3.2;
    la condizione alternativa su TD e la regolarita' in altezza restano
    a carico del progettista);
  - coefficiente lambda per la [7.3.7]: 0,85 se T1 < 2*TC e almeno tre
    orizzontamenti, altrimenti 1,0.

Output deterministico, formule chiuse. La skill e' di STIMA PRELIMINARE:
non sostituisce l'analisi modale ne' la verifica con software di calcolo.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# Coefficienti C1 della [C7.3.2] (Circ. 7/2019 par. C7.3.3.2)
C1_TABELLA = {
    "telaio-acciaio": 0.085,
    "telaio-legno": 0.085,
    "telaio-ca": 0.075,
    "muratura": 0.050,
    "altro": 0.050,
}

# Limite di altezza per la stima [7.3.6] (NTC 2018 par. 7.3.3.2)
H_MAX_FORMULA_M = 40.0

# Moltiplicatori delle condizioni su TC (NTC 2018 par. 7.3.3.2)
FATTORE_LIMITE_ANALISI_STATICA = 2.5   # T1 <= 2,5*TC (o TD)
FATTORE_LAMBDA = 2.0                   # lambda = 0,85 se T1 < 2*TC (+ >=3 orizzontamenti)
LAMBDA_RIDOTTO = 0.85
LAMBDA_UNITARIO = 1.0
MIN_ORIZZONTAMENTI_LAMBDA = 3


def _finite_pos(value: Any, name: str) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: valore non numerico") from exc
    if not math.isfinite(x) or x <= 0.0:
        raise ValueError(f"{name}: deve essere un numero finito > 0")
    return x


@dataclass
class RisultatoT1:
    metodo: str
    formula: str
    t1_s: float
    input_effettivi: Dict[str, Any]
    avvertenze: List[str] = field(default_factory=list)
    # valorizzati solo se tc_s e' fornito
    tc_s: Optional[float] = None
    limite_analisi_statica_s: Optional[float] = None
    condizione_t1_su_tc: Optional[bool] = None
    lambda_forze: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "metodo": self.metodo,
            "formula": self.formula,
            "T1_s": round(self.t1_s, 4),
            "input": self.input_effettivi,
            "avvertenze": self.avvertenze,
        }
        if self.tc_s is not None:
            out["TC_s"] = self.tc_s
            out["limite_2_5_TC_s"] = round(self.limite_analisi_statica_s, 4)
            out["T1_entro_2_5_TC"] = self.condizione_t1_su_tc
            out["lambda_forze_7_3_7"] = self.lambda_forze
        return out


def t1_da_spostamento(d_m: float) -> float:
    """[7.3.6] NTC 2018: T1 = 2*sqrt(d), d in metri."""
    d = _finite_pos(d_m, "d (spostamento laterale elastico, m)")
    return 2.0 * math.sqrt(d)


def t1_da_altezza(h_m: float, tipologia: str) -> float:
    """[C7.3.2] Circ. 7/2019: T1 = C1*H^(3/4), H in metri dal piano di fondazione."""
    h = _finite_pos(h_m, "H (altezza dal piano di fondazione, m)")
    if tipologia not in C1_TABELLA:
        raise ValueError(
            f"tipologia '{tipologia}' non prevista: usare una tra {sorted(C1_TABELLA)}"
        )
    return C1_TABELLA[tipologia] * h ** 0.75


def _valuta_tc(
    ris: RisultatoT1,
    tc_s: Optional[float],
    n_orizzontamenti: Optional[int],
) -> None:
    if tc_s is None:
        return
    tc = _finite_pos(tc_s, "TC (s)")
    ris.tc_s = tc
    ris.limite_analisi_statica_s = FATTORE_LIMITE_ANALISI_STATICA * tc
    ris.condizione_t1_su_tc = ris.t1_s <= ris.limite_analisi_statica_s
    if not ris.condizione_t1_su_tc:
        ris.avvertenze.append(
            "T1 supera 2,5*TC: l'analisi lineare statica richiede T1 <= 2,5*TC "
            "o T1 <= TD e costruzione regolare in altezza (NTC 7.3.3.2). "
            "Verificare la condizione alternativa su TD."
        )
    if n_orizzontamenti is not None:
        n = int(n_orizzontamenti)
        if n < 1:
            raise ValueError("n_orizzontamenti: deve essere >= 1")
        if ris.t1_s < FATTORE_LAMBDA * tc and n >= MIN_ORIZZONTAMENTI_LAMBDA:
            ris.lambda_forze = LAMBDA_RIDOTTO
        else:
            ris.lambda_forze = LAMBDA_UNITARIO
    else:
        ris.avvertenze.append(
            "n_orizzontamenti non fornito: lambda della [7.3.7] non valutato "
            "(0,85 se T1 < 2*TC e almeno tre orizzontamenti, altrimenti 1,0)."
        )


def stima_t1(
    metodo: str,
    d_m: Optional[float] = None,
    h_m: Optional[float] = None,
    tipologia: Optional[str] = None,
    tc_s: Optional[float] = None,
    n_orizzontamenti: Optional[int] = None,
    massa_uniforme: Optional[bool] = None,
) -> RisultatoT1:
    """Stima T1 col metodo richiesto ('ntc' = [7.3.6], 'circolare' = [C7.3.2])."""
    if metodo == "ntc":
        if d_m is None:
            raise ValueError("metodo 'ntc' [7.3.6]: richiesto d (spostamento in m)")
        t1 = t1_da_spostamento(d_m)
        ris = RisultatoT1(
            metodo="ntc",
            formula="T1 = 2*sqrt(d)  [7.3.6] NTC 2018 par. 7.3.3.2",
            t1_s=t1,
            input_effettivi={"d_m": float(d_m)},
        )
        ris.avvertenze.append(
            "d deve essere lo spostamento laterale ELASTICO del punto piu' alto "
            "dell'edificio dovuto alla combinazione [2.5.7] "
            "(G1 + G2 + somma psi_2j*Qkj) applicata in direzione orizzontale "
            "(NTC 7.3.3.2 + 2.5.3)."
        )
    elif metodo == "circolare":
        if h_m is None or tipologia is None:
            raise ValueError(
                "metodo 'circolare' [C7.3.2]: richiesti H (m) e tipologia"
            )
        t1 = t1_da_altezza(h_m, tipologia)
        ris = RisultatoT1(
            metodo="circolare",
            formula="T1 = C1*H^(3/4)  [C7.3.2] Circ. 7/2019 par. C7.3.3.2",
            t1_s=t1,
            input_effettivi={
                "H_m": float(h_m),
                "tipologia": tipologia,
                "C1": C1_TABELLA[tipologia],
            },
        )
        ris.avvertenze.append(
            "Stima 'in via di prima approssimazione' (C7.3.3.2): la [7.3.6] "
            "delle NTC, basata sullo spostamento d, e' indicata dalla "
            "Circolare come piu' affidabile."
        )
    else:
        raise ValueError("metodo: usare 'ntc' ([7.3.6]) o 'circolare' ([C7.3.2])")

    # Limiti di applicabilita' della stima (NTC 7.3.3.2)
    if h_m is not None and float(h_m) > H_MAX_FORMULA_M:
        ris.avvertenze.append(
            f"H = {float(h_m):g} m > {H_MAX_FORMULA_M:g} m: la stima "
            "semplificata di T1 e' prevista dalle NTC per costruzioni che non "
            "superino i 40 m di altezza (NTC 7.3.3.2). Fuori da questo limite "
            "serve l'analisi modale."
        )
    if metodo == "ntc" and h_m is None:
        ris.avvertenze.append(
            "H non fornita: verificare che la costruzione non superi i 40 m "
            "(condizione della stima semplificata, NTC 7.3.3.2)."
        )
    if massa_uniforme is False:
        ris.avvertenze.append(
            "Massa dichiarata NON approssimativamente uniforme lungo "
            "l'altezza: la stima semplificata di T1 non e' applicabile "
            "(NTC 7.3.3.2). Usare l'analisi modale."
        )
    elif massa_uniforme is None:
        ris.avvertenze.append(
            "Verificare che la massa sia distribuita in modo "
            "approssimativamente uniforme lungo l'altezza (NTC 7.3.3.2)."
        )
    ris.avvertenze.append(
        "Stima preliminare: non sostituisce l'analisi modale ne' il giudizio "
        "del progettista. La regolarita' in altezza e la condizione "
        "alternativa su TD restano da verificare a parte."
    )

    _valuta_tc(ris, tc_s, n_orizzontamenti)
    return ris


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Stima T1 (NTC 2018 [7.3.6] / Circ. 7/2019 [C7.3.2]). "
            "Output JSON su stdout."
        )
    )
    ap.add_argument("--metodo", required=True, choices=["ntc", "circolare"])
    ap.add_argument("--d", type=float, help="spostamento laterale elastico d [m] (metodo ntc)")
    ap.add_argument("--h", type=float, help="altezza H dal piano di fondazione [m]")
    ap.add_argument(
        "--tipologia",
        choices=sorted(C1_TABELLA),
        help="tipologia strutturale (metodo circolare)",
    )
    ap.add_argument("--tc", type=float, help="periodo TC dello spettro [s] (opzionale)")
    ap.add_argument(
        "--orizzontamenti", type=int, help="numero di orizzontamenti (opzionale, per lambda)"
    )
    ap.add_argument(
        "--massa-uniforme",
        choices=["si", "no"],
        help="massa approssimativamente uniforme lungo l'altezza?",
    )
    args = ap.parse_args(argv)

    massa = None
    if args.massa_uniforme == "si":
        massa = True
    elif args.massa_uniforme == "no":
        massa = False

    try:
        ris = stima_t1(
            metodo=args.metodo,
            d_m=args.d,
            h_m=args.h,
            tipologia=args.tipologia,
            tc_s=args.tc,
            n_orizzontamenti=args.orizzontamenti,
            massa_uniforme=massa,
        )
    except ValueError as exc:
        print(json.dumps({"errore": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(ris.to_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
