#!/usr/bin/env python3
"""Trasmittanza termica U di strutture opache + verifica limiti DM 26/06/2015.

Riferimenti:
  - DM 26/06/2015 (MiSE) "requisiti minimi", GU n. 162/2015 S.O. 39
    (SHA256 b69e130f...), Allegato 1:
      par. 5.2: U <= U_limite per le porzioni di involucro riqualificate;
      Appendice B Tabelle 1-4: valori limite di U per zona climatica
        (edifici esistenti sottoposti a riqualificazione energetica);
      Appendice A Tabelle 1-4: U dell'edificio di riferimento (nuove
        costruzioni / ristrutturazioni importanti);
      Cap. 5 par. 5.2: incremento +30% dei limiti App. B in caso di
        isolamento dall'interno o in intercapedine.
  - Metodo di calcolo U = 1/R_tot (legge di Fourier): fisica tecnica di
    pubblico dominio. Il DM NON contiene ne' il metodo, ne' i lambda dei
    materiali, ne' le resistenze superficiali R_si/R_se (rinvia a UNI/TS
    11300, UNI EN ISO 6946): tali dati sono INPUT dell'utente.

Il modulo calcola U dalla stratigrafia (spessori e lambda forniti) e dalle
resistenze superficiali fornite, quindi confronta con il limite del DM per
zona climatica, tipo di struttura, regime (riqualificazione / edificio di
riferimento) e anno. Non inventa lambda ne' R_si/R_se; non calcola i ponti
termici (il limite del DM li include, il calcolo 1D no: la verifica e'
preliminare). Non sostituisce la relazione tecnica del progettista.

Unita': spessori in m, lambda in W/(m K), resistenze in m2 K/W, U in W/(m2 K).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# --- Valori limite di U [W/(m2 K)] dal DM 26/06/2015 (trascritti da PDF) ---
# Chiave: zona climatica normalizzata ("AB", "C", "D", "E", "F").
# Ogni valore: (limite 2015, limite colonna successiva).
# Appendice B - edifici esistenti sottoposti a riqualificazione energetica
#   colonna successiva = 2021 (dal 1/1/2021 per tutti gli edifici).
APP_B: Dict[str, Dict[str, Tuple[float, float]]] = {
    "parete_verticale": {  # Tabella 1 App. B
        "AB": (0.45, 0.40), "C": (0.40, 0.36), "D": (0.36, 0.32),
        "E": (0.30, 0.28), "F": (0.28, 0.26),
    },
    "copertura": {  # Tabella 2 App. B
        "AB": (0.34, 0.32), "C": (0.34, 0.32), "D": (0.28, 0.26),
        "E": (0.26, 0.24), "F": (0.24, 0.22),
    },
    "pavimento": {  # Tabella 3 App. B
        "AB": (0.48, 0.42), "C": (0.42, 0.38), "D": (0.36, 0.32),
        "E": (0.31, 0.29), "F": (0.30, 0.28),
    },
    "chiusura_trasparente": {  # Tabella 4 App. B (con infissi)
        "AB": (3.20, 3.00), "C": (2.40, 2.00), "D": (2.10, 1.80),
        "E": (1.90, 1.40), "F": (1.70, 1.00),
    },
}
# Appendice A - edificio di riferimento (nuove costruzioni / ristrutt. importanti)
#   colonna successiva = 2019 (edifici pubblici) / 2021 (altri).
APP_A: Dict[str, Dict[str, Tuple[float, float]]] = {
    "parete_verticale": {  # Tabella 1 App. A
        "AB": (0.45, 0.43), "C": (0.38, 0.34), "D": (0.34, 0.29),
        "E": (0.30, 0.26), "F": (0.28, 0.24),
    },
    "copertura": {  # Tabella 2 App. A
        "AB": (0.38, 0.35), "C": (0.36, 0.33), "D": (0.30, 0.26),
        "E": (0.25, 0.22), "F": (0.23, 0.20),
    },
    "pavimento": {  # Tabella 3 App. A
        "AB": (0.46, 0.44), "C": (0.40, 0.38), "D": (0.32, 0.29),
        "E": (0.30, 0.26), "F": (0.28, 0.24),
    },
    "chiusura_trasparente": {  # Tabella 4 App. A (con infissi)
        "AB": (3.20, 3.00), "C": (2.40, 2.20), "D": (2.00, 1.80),
        "E": (1.80, 1.40), "F": (1.50, 1.10),
    },
}

TIPI = ("parete_verticale", "copertura", "pavimento", "chiusura_trasparente")
REGIMI = ("riqualificazione", "edificio_riferimento")
ANNI = ("2015", "2021")
INCREMENTO_ISOLAMENTO_INTERNO = 0.30  # +30% App. B (Cap. 5 par. 5.2 DM 2015)


def _norm_zona(zona: Any) -> str:
    z = str(zona).strip().upper().replace(" ", "")
    if z in ("A", "B", "AB", "AEB", "AB"):
        return "AB"
    if z in ("C", "D", "E", "F"):
        return z
    raise ValueError(
        f"zona climatica '{zona}' non valida: attese A, B, C, D, E, F "
        "(A e B condividono lo stesso limite)"
    )


def _finite(value: Any, name: str, positive: bool = True) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name}: valore non numerico") from exc
    if not math.isfinite(x):
        raise ValueError(f"{name}: valore non finito")
    if positive and x <= 0.0:
        raise ValueError(f"{name}: deve essere > 0")
    return x


@dataclass
class Strato:
    nome: str
    spessore_m: float
    lambda_w_mk: float

    @property
    def resistenza(self) -> float:
        return self.spessore_m / self.lambda_w_mk


@dataclass
class Risultato:
    U_W_m2K: float
    R_tot: float
    R_si: float
    R_se: float
    R_strati: float
    strati: List[Dict[str, Any]]
    zona: str
    tipo: str
    regime: str
    anno: str
    U_limite_base: float
    U_limite_applicato: float
    incremento_applicato: bool
    verifica_soddisfatta: bool
    avvertenze: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "U_W_m2K": round(self.U_W_m2K, 4),
            "R_tot_m2K_W": round(self.R_tot, 4),
            "dettaglio_resistenze": {
                "R_si": round(self.R_si, 4),
                "R_strati": round(self.R_strati, 4),
                "R_se": round(self.R_se, 4),
            },
            "strati": self.strati,
            "zona_climatica": self.zona,
            "tipo_struttura": self.tipo,
            "regime": self.regime,
            "anno_limite": self.anno,
            "U_limite_base_W_m2K": round(self.U_limite_base, 4),
            "U_limite_applicato_W_m2K": round(self.U_limite_applicato, 4),
            "incremento_30pct_isolamento_interno": self.incremento_applicato,
            "verifica_U_minore_uguale_limite": self.verifica_soddisfatta,
            "avvertenze": self.avvertenze,
        }


def calcola_trasmittanza(
    strati: List[Strato],
    R_si: Any,
    R_se: Any,
    zona: Any,
    tipo: str = "parete_verticale",
    regime: str = "riqualificazione",
    anno: str = "2021",
    isolamento_interno_o_intercapedine: bool = False,
    verso_ambiente_non_climatizzato: bool = False,
    controterra: bool = False,
) -> Risultato:
    """Calcola U e verifica il limite DM 26/06/2015.

    Rifiuta (ValueError) input incompleti/non validi: nessuno strato, lambda o
    spessore non positivi, R_si/R_se mancanti, zona/tipo/regime/anno non validi.
    """
    if tipo not in TIPI:
        raise ValueError(f"tipo '{tipo}' non valido: attesi {TIPI}")
    if regime not in REGIMI:
        raise ValueError(f"regime '{regime}' non valido: attesi {REGIMI}")
    if str(anno) not in ANNI:
        raise ValueError(f"anno '{anno}' non valido: attesi {ANNI}")
    anno = str(anno)

    rsi = _finite(R_si, "R_si", positive=True)
    rse = _finite(R_se, "R_se", positive=True)

    if tipo == "chiusura_trasparente":
        raise ValueError(
            "tipo 'chiusura_trasparente': la U dei serramenti non si calcola per "
            "stratigrafia (dipende da telaio, vetro, distanziatore: UNI EN ISO "
            "10077). Questa skill calcola solo strutture opache stratificate; per "
            "i serramenti usare la Uw dichiarata dal produttore e confrontarla con "
            "la Tabella 4 del DM 26/06/2015."
        )

    if not strati:
        raise ValueError("nessuno strato fornito: la stratigrafia e' obbligatoria")

    dettaglio: List[Dict[str, Any]] = []
    r_strati = 0.0
    for i, s in enumerate(strati):
        _finite(s.spessore_m, f"strato[{i}].spessore_m", positive=True)
        _finite(s.lambda_w_mk, f"strato[{i}].lambda_w_mk", positive=True)
        r = s.resistenza
        r_strati += r
        dettaglio.append({
            "nome": s.nome,
            "spessore_m": s.spessore_m,
            "lambda_W_mK": s.lambda_w_mk,
            "R_m2K_W": round(r, 4),
        })

    r_tot = rsi + r_strati + rse
    u = 1.0 / r_tot

    tabella = APP_B if regime == "riqualificazione" else APP_A
    z = _norm_zona(zona)
    idx = 0 if anno == "2015" else 1
    u_lim_base = tabella[tipo][z][idx]

    incremento = False
    u_lim = u_lim_base
    if isolamento_interno_o_intercapedine:
        if regime != "riqualificazione":
            raise ValueError(
                "l'incremento +30% (isolamento interno/intercapedine) si applica "
                "solo ai limiti dell'Appendice B (regime 'riqualificazione')"
            )
        u_lim = u_lim_base * (1.0 + INCREMENTO_ISOLAMENTO_INTERNO)
        incremento = True

    avvertenze: List[str] = [
        "Il valore limite del DM include l'effetto dei ponti termici (App. B/A); "
        "questa U e' calcolata in regime monodimensionale e NON include i ponti "
        "termici: la verifica e' PRELIMINARE. La verifica completa richiede il "
        "calcolo dei ponti termici (UNI EN ISO 14683/10211).",
        "lambda dei materiali e resistenze superficiali R_si/R_se sono dati "
        "forniti dall'utente (schede tecniche / UNI EN ISO 6946): il modulo non "
        "li verifica ne' li stima.",
        "La skill non sostituisce la relazione tecnica ex art. 8 c. 1 D.Lgs. "
        "192/2005 firmata dal progettista.",
    ]
    if verso_ambiente_non_climatizzato:
        avvertenze.append(
            "Struttura verso ambiente non climatizzato: il DM richiede di dividere "
            "la U per il fattore di correzione dello scambio termico (UNI/TS "
            "11300-1) prima del confronto col limite. Questo modulo NON applica "
            "tale fattore: il confronto qui e' cautelativo/indicativo."
        )
    if controterra:
        avvertenze.append(
            "Struttura controterra: il DM richiede il confronto con la "
            "trasmittanza equivalente (UNI EN ISO 13370), non con la U 1D. Il "
            "confronto qui e' indicativo."
        )

    return Risultato(
        U_W_m2K=u,
        R_tot=r_tot,
        R_si=rsi,
        R_se=rse,
        R_strati=r_strati,
        strati=dettaglio,
        zona=z,
        tipo=tipo,
        regime=regime,
        anno=anno,
        U_limite_base=u_lim_base,
        U_limite_applicato=u_lim,
        incremento_applicato=incremento,
        verifica_soddisfatta=(u <= u_lim + 1e-9),
        avvertenze=avvertenze,
    )


def _parse_strati(raw: List[str]) -> List[Strato]:
    strati: List[Strato] = []
    for j, item in enumerate(raw):
        parts = item.split(":")
        if len(parts) == 3:
            nome, sp, lam = parts
        elif len(parts) == 2:
            nome, sp, lam = f"strato_{j+1}", parts[0], parts[1]
        else:
            raise ValueError(
                f"strato '{item}' non valido: usa 'nome:spessore_m:lambda' "
                "oppure 'spessore_m:lambda'"
            )
        strati.append(Strato(nome=nome, spessore_m=float(sp), lambda_w_mk=float(lam)))
    return strati


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Calcolo U strutture opache + verifica limiti DM 26/06/2015",
    )
    p.add_argument(
        "--strato", action="append", default=[], metavar="nome:spessore_m:lambda",
        help="strato (ripetibile), dall'interno all'esterno; es. mattone:0.25:0.72",
    )
    p.add_argument("--rsi", required=True, type=float, help="resistenza superficiale interna [m2K/W] (UNI EN ISO 6946)")
    p.add_argument("--rse", required=True, type=float, help="resistenza superficiale esterna [m2K/W] (UNI EN ISO 6946)")
    p.add_argument("--zona", required=True, help="zona climatica: A/B/C/D/E/F")
    p.add_argument("--tipo", default="parete_verticale", choices=list(TIPI))
    p.add_argument("--regime", default="riqualificazione", choices=list(REGIMI))
    p.add_argument("--anno", default="2021", choices=list(ANNI))
    p.add_argument("--isolamento-interno", action="store_true", help="isolamento dall'interno o in intercapedine (+30%% limiti App. B)")
    p.add_argument("--verso-non-climatizzato", action="store_true")
    p.add_argument("--controterra", action="store_true")
    args = p.parse_args(argv)

    try:
        strati = _parse_strati(args.strato)
        res = calcola_trasmittanza(
            strati=strati, R_si=args.rsi, R_se=args.rse, zona=args.zona,
            tipo=args.tipo, regime=args.regime, anno=args.anno,
            isolamento_interno_o_intercapedine=args.isolamento_interno,
            verso_ambiente_non_climatizzato=args.verso_non_climatizzato,
            controterra=args.controterra,
        )
    except ValueError as exc:
        print(json.dumps({"errore": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps(res.to_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
