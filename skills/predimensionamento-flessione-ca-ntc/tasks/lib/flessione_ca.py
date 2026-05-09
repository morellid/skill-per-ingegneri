#!/usr/bin/env python3
"""Pre-dimensionamento sezione c.a. SLU flessione semplice NTC 2018 par. 4.1.2.1.

Riferimenti normativi:
  - DM 17/01/2018 (NTC 2018) par. 4.1.2.1 - resistenze e diagrammi tensione/deformazione
  - DM 17/01/2018 (NTC 2018) par. 4.1.2.3.4.2 - flessione semplice SLU
  - Circolare MIT n. 7 del 21/01/2019 - C4.1.2

Implementa il calcolo di MRd per sezione rettangolare in c.a. con sola
armatura tesa (singolarmente armata). Usa il diagramma stress-block
rettangolare equivalente (eta = 1, lambda = 0.8 per fck <= 50 MPa).

Output deterministico, tutte le formule sono chiuse. La skill e' di
PRE-DIMENSIONAMENTO: non sostituisce verifica completa con software di
calcolo strutturale, non gestisce sezioni doppiamente armate, non gestisce
calcestruzzi ad alta resistenza fck > 50 MPa, non gestisce flessione
deviata o pressoflessione.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# Costanti NTC 2018 par. 4.1.2.1
ALPHA_CC_DEFAULT = 0.85
GAMMA_C_DEFAULT = 1.5
GAMMA_S_DEFAULT = 1.15
ES_DEFAULT = 200000.0          # MPa, modulo elastico acciaio (par. 4.1.2.1.1.2)
EPS_CU_DEFAULT = 0.0035        # 3.5 per mille, fck <= 50 MPa (Classe 1)
LAMBDA_SB = 0.8                # stress-block: profondita' equivalente
ETA_SB = 1.0                   # stress-block: tensione costante (fck <= 50 MPa)
FCK_MAX_CLASSE_1 = 50.0        # MPa, oltre richiede formulazione diversa (NTC eq. 4.1.10-4.1.11)
ZETA_LIM_DUTTILITA = 0.45      # x/d <= 0.45 raccomandato per duttilita' (Circ 7/2019 C4.1.2)


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


def resistenza_calcestruzzo_fcd(
    fck: float, alpha_cc: float = ALPHA_CC_DEFAULT, gamma_c: float = GAMMA_C_DEFAULT
) -> float:
    """fcd = alpha_cc * fck / gamma_c (NTC eq. 4.1.4)."""
    fck = _positive(_finite(fck, "fck"), "fck")
    if fck > FCK_MAX_CLASSE_1:
        raise ValueError(
            f"fck = {fck} MPa > {FCK_MAX_CLASSE_1} MPa: la skill copre solo classi <= C50/60 "
            "(stress-block con eta=1, lambda=0.8). Per fck > 50 MPa NTC eq. 4.1.10-4.1.11 "
            "richiede eta < 1 e lambda < 0.8: fuori scope."
        )
    alpha_cc = _positive(_finite(alpha_cc, "alpha_cc"), "alpha_cc")
    gamma_c = _positive(_finite(gamma_c, "gamma_c"), "gamma_c")
    return alpha_cc * fck / gamma_c


def resistenza_acciaio_fyd(fyk: float, gamma_s: float = GAMMA_S_DEFAULT) -> float:
    """fyd = fyk / gamma_s (NTC par. 4.1.2.1.1.3)."""
    fyk = _positive(_finite(fyk, "fyk"), "fyk")
    gamma_s = _positive(_finite(gamma_s, "gamma_s"), "gamma_s")
    return fyk / gamma_s


def deformazione_snervamento_eyd(fyd: float, e_s: float = ES_DEFAULT) -> float:
    """eps_yd = fyd / Es."""
    fyd = _positive(_finite(fyd, "fyd"), "fyd")
    e_s = _positive(_finite(e_s, "Es"), "Es")
    return fyd / e_s


def asse_neutro_x(
    a_s: float, fyd: float, b: float, fcd: float, lambda_sb: float = LAMBDA_SB
) -> float:
    """Profondita' asse neutro x, da equilibrio Cc = T (assunzione acciaio snervato).

    lambda_sb * b * x * fcd = a_s * fyd
    ->  x = (a_s * fyd) / (lambda_sb * b * fcd)
    """
    a_s = _positive(_finite(a_s, "As"), "As")
    fyd = _positive(_finite(fyd, "fyd"), "fyd")
    b = _positive(_finite(b, "b"), "b")
    fcd = _positive(_finite(fcd, "fcd"), "fcd")
    lambda_sb = _positive(_finite(lambda_sb, "lambda_sb"), "lambda_sb")
    return (a_s * fyd) / (lambda_sb * b * fcd)


def deformazione_acciaio_eps_s(
    x: float, d: float, eps_cu: float = EPS_CU_DEFAULT
) -> float:
    """Deformazione acciaio teso eps_s = eps_cu * (d - x) / x (compatibilita' piana sezione)."""
    x = _positive(_finite(x, "x"), "x")
    d = _positive(_finite(d, "d"), "d")
    eps_cu = _positive(_finite(eps_cu, "eps_cu"), "eps_cu")
    if x >= d:
        # asse neutro fuori dalla sezione tesa: configurazione patologica
        raise ValueError(
            f"x = {x} mm >= d = {d} mm: asse neutro oltre l'armatura tesa, "
            "sezione gravemente sovra-armata. Aumentare b o h, ridurre As, "
            "o passare a sezione doppiamente armata (fuori scope skill)."
        )
    return eps_cu * (d - x) / x


@dataclass(frozen=True)
class RisultatoFlessione:
    # Input
    b: float
    h: float
    d: float
    a_s: float
    fck: float
    fyk: float
    alpha_cc: float
    gamma_c: float
    gamma_s: float
    eps_cu: float
    e_s_modulo: float
    # Materiali
    fcd: float
    fyd: float
    eps_yd: float
    # Geometria interna
    x: float
    zeta: float           # x/d
    eps_s: float
    z: float              # braccio leva = d - 0.4 x (eta * x con eta = 0.4 per stress-block)
    # Output
    m_rd_Nmm: float
    duttile_snervamento: bool      # eps_s >= eps_yd
    duttile_zeta_limite: bool      # x/d <= ZETA_LIM
    avvertenze: List[str] = field(default_factory=list)
    riferimenti: List[str] = field(default_factory=list)

    @property
    def m_rd_kNm(self) -> float:
        return self.m_rd_Nmm / 1.0e6

    def as_dict(self) -> Dict[str, Any]:
        return {
            "input": {
                "b_mm": self.b,
                "h_mm": self.h,
                "d_mm": self.d,
                "As_mm2": self.a_s,
                "fck_MPa": self.fck,
                "fyk_MPa": self.fyk,
                "alpha_cc": self.alpha_cc,
                "gamma_c": self.gamma_c,
                "gamma_s": self.gamma_s,
                "eps_cu": self.eps_cu,
                "Es_MPa": self.e_s_modulo,
            },
            "materiali": {
                "fcd_MPa": round(self.fcd, 6),
                "fyd_MPa": round(self.fyd, 6),
                "eps_yd": round(self.eps_yd, 6),
            },
            "geometria_interna": {
                "x_mm": round(self.x, 6),
                "zeta_x_su_d": round(self.zeta, 6),
                "eps_s": round(self.eps_s, 6),
                "z_braccio_leva_mm": round(self.z, 6),
            },
            "output": {
                "M_Rd_Nmm": round(self.m_rd_Nmm, 6),
                "M_Rd_kNm": round(self.m_rd_kNm, 6),
                "duttile_snervamento_acciaio": self.duttile_snervamento,
                "duttile_zeta_limite_0_45": self.duttile_zeta_limite,
                "avvertenze": list(self.avvertenze),
            },
            "riferimenti_ntc": list(self.riferimenti),
        }


def calcola_m_rd(
    b: float,
    h: float,
    d: float,
    a_s: float,
    fck: float,
    fyk: float,
    alpha_cc: float = ALPHA_CC_DEFAULT,
    gamma_c: float = GAMMA_C_DEFAULT,
    gamma_s: float = GAMMA_S_DEFAULT,
    e_s: float = ES_DEFAULT,
    eps_cu: float = EPS_CU_DEFAULT,
) -> RisultatoFlessione:
    """Momento resistente MRd di sezione rettangolare in c.a. singolarmente armata.

    Ipotesi:
      - sezione rettangolare b x h
      - sola armatura tesa A_s a quota d dal lembo compresso
      - calcestruzzo Classe 1 (fck <= 50 MPa)
      - stress-block rettangolare equivalente: lambda = 0.8, eta = 1
      - eps_cu = 0.0035 (NTC fck <= 50 MPa)

    Riferimenti:
      - NTC 2018 par. 4.1.2.1 (resistenze, diagramma stress-block)
      - NTC 2018 par. 4.1.2.3.4.2 (flessione semplice)
      - Circ. 7/2019 par. C4.1.2 (commento)
    """
    b = _positive(_finite(b, "b"), "b")
    h = _positive(_finite(h, "h"), "h")
    d = _positive(_finite(d, "d"), "d")
    a_s = _positive(_finite(a_s, "As"), "As")
    if d > h:
        raise ValueError(f"d = {d} > h = {h}: l'altezza utile non puo' superare l'altezza totale")
    fck = _positive(_finite(fck, "fck"), "fck")
    fyk = _positive(_finite(fyk, "fyk"), "fyk")
    fcd = resistenza_calcestruzzo_fcd(fck, alpha_cc=alpha_cc, gamma_c=gamma_c)
    fyd = resistenza_acciaio_fyd(fyk, gamma_s=gamma_s)
    eps_yd = deformazione_snervamento_eyd(fyd, e_s=e_s)

    x = asse_neutro_x(a_s, fyd, b, fcd)
    eps_s = deformazione_acciaio_eps_s(x, d, eps_cu=eps_cu)
    zeta = x / d

    duttile_snervamento = eps_s >= eps_yd
    duttile_zeta = zeta <= ZETA_LIM_DUTTILITA

    z = d - 0.4 * x
    if duttile_snervamento:
        m_rd = a_s * fyd * z
    else:
        # Sezione sovra-armata: l'acciaio non snerva al collasso. La formula con
        # sigma_s = fyd sovrastima la resistenza. Calcolo conservativo: usa
        # sigma_s = Es * eps_s (acciaio in regime elastico) ricalcolando x per
        # nuova condizione di equilibrio. Per semplicita' ed evitare iterazioni
        # implicite, in v0.1 si rifiuta il calcolo con avvertenza esplicita.
        raise ValueError(
            f"Sezione sovra-armata: eps_s = {eps_s:.6f} < eps_yd = {eps_yd:.6f}, "
            "l'acciaio non snerva al collasso. La formula M_Rd = As * fyd * z "
            "non si applica. Aumentare b/h o ridurre As, oppure passare a calcolo "
            "iterativo con sigma_s elastico (fuori scope skill v0.1)."
        )

    avvertenze: List[str] = []
    if not duttile_zeta:
        avvertenze.append(
            f"x/d = {zeta:.3f} > {ZETA_LIM_DUTTILITA} (limite raccomandato Circ. 7/2019 "
            "C4.1.2 per duttilita' adeguata): sezione poco duttile, ammessa per casi "
            "non sismici, ma sconsigliata. Aumentare b o h, oppure passare a sezione "
            "doppiamente armata."
        )

    riferimenti = [
        "NTC 2018 par. 4.1.2.1 - resistenze di progetto fcd, fyd",
        "NTC 2018 par. 4.1.2.1.1 - diagramma stress-block (eta=1, lambda=0.8 per fck <= 50 MPa)",
        "NTC 2018 par. 4.1.2.3.4.2 - flessione semplice SLU",
        "NTC 2018 par. 4.1.2.1.1.2 - acciaio: Es = 200000 MPa, eps_yd = fyd/Es",
        "Circ. 7/2019 par. C4.1.2 - commento applicativo, raccomandazione x/d <= 0.45",
    ]

    return RisultatoFlessione(
        b=b, h=h, d=d, a_s=a_s, fck=fck, fyk=fyk,
        alpha_cc=alpha_cc, gamma_c=gamma_c, gamma_s=gamma_s,
        eps_cu=eps_cu, e_s_modulo=e_s,
        fcd=fcd, fyd=fyd, eps_yd=eps_yd,
        x=x, zeta=zeta, eps_s=eps_s, z=z,
        m_rd_Nmm=m_rd,
        duttile_snervamento=duttile_snervamento,
        duttile_zeta_limite=duttile_zeta,
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
        risultato = calcola_m_rd(
            b=data["b"],
            h=data["h"],
            d=data["d"],
            a_s=data["As"],
            fck=data["fck"],
            fyk=data["fyk"],
            alpha_cc=data.get("alpha_cc", ALPHA_CC_DEFAULT),
            gamma_c=data.get("gamma_c", GAMMA_C_DEFAULT),
            gamma_s=data.get("gamma_s", GAMMA_S_DEFAULT),
            e_s=data.get("Es", ES_DEFAULT),
            eps_cu=data.get("eps_cu", EPS_CU_DEFAULT),
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
