#!/usr/bin/env python3
"""Carichi atmosferici NTC 2018 par. 3.3 (vento) e 3.4 (neve) - code-driven.

Riferimenti normativi:
  - DM 17/01/2018 (NTC 2018) par. 3.3 (azioni del vento) e par. 3.4 (azioni della neve)
  - Circolare MIT n. 7 del 21/01/2019 - C3.3 e C3.4

La skill non incorpora la mappa zone vento (Tab. 3.3.I) e si limita a richiedere
i parametri zonali (v_b_0, a_0, k_s) all'utente, analogamente a come la skill
spettro-risposta-ntc richiede i parametri di pericolosita' sismica al sito.

Per la neve i parametri zonali sono integralmente codificati come da formule
(3.4.1)-(3.4.4) NTC 2018 par. 3.4.2.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


RHO_ARIA = 1.25  # kg/m3, NTC par. 3.3.6


CATEGORIE_ESPOSIZIONE = {
    "I":   {"k_r": 0.17, "z_0": 0.01, "z_min": 2.0},
    "II":  {"k_r": 0.19, "z_0": 0.05, "z_min": 4.0},
    "III": {"k_r": 0.20, "z_0": 0.10, "z_min": 5.0},
    "IV":  {"k_r": 0.22, "z_0": 0.30, "z_min": 8.0},
    "V":   {"k_r": 0.23, "z_0": 0.70, "z_min": 12.0},
}


CLASSI_ESPOSIZIONE_NEVE = {
    "battuta_dai_venti": 0.9,
    "normale": 1.0,
    "riparata": 1.1,
}


ZONE_NEVE = ("I-Alpina", "I-Mediterranea", "II", "III")


def _finite(value: Any, field_name: str) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name}: valore non numerico") from exc
    if not math.isfinite(x):
        raise ValueError(f"{field_name}: valore non finito")
    return x


# ---------------------------------------------------------------------------
# VENTO (par. 3.3 NTC 2018)
# ---------------------------------------------------------------------------

def velocita_riferimento_vb(v_b_0: float, a_0: float, k_s: float, a_s: float) -> float:
    """Velocita' di riferimento v_b in m/s, NTC eq. 3.3.2.

    v_b = v_b_0                                     se a_s <= a_0
    v_b = v_b_0 * (1 + k_s * (a_s/a_0 - 1))         se a_0 < a_s <= 1500 m

    Per a_s > 1500 m la norma rinvia a indagini specifiche (NTC par. 3.3.2);
    il modulo solleva ValueError.
    """
    v_b_0 = _finite(v_b_0, "v_b_0")
    a_0 = _finite(a_0, "a_0")
    k_s = _finite(k_s, "k_s")
    a_s = _finite(a_s, "a_s")
    if v_b_0 <= 0:
        raise ValueError("v_b_0 deve essere positivo")
    if a_0 <= 0:
        raise ValueError("a_0 deve essere positivo")
    if a_s < 0:
        raise ValueError("a_s (altitudine sito) non puo' essere negativa")
    if a_s > 1500:
        raise ValueError(
            "a_s > 1500 m: NTC par. 3.3.2 richiede indagine specifica, fuori scope skill"
        )
    if a_s <= a_0:
        return v_b_0
    return v_b_0 * (1.0 + k_s * (a_s / a_0 - 1.0))


def coefficiente_ritorno_cr(t_r_anni: float) -> float:
    """Coefficiente di ritorno c_r per T_R != 50 anni, NTC eq. 3.3.3.

    c_r = 0.75 * sqrt(1 - 0.2 * ln(-ln(1 - 1/T_R)))   per T_R != 50 anni
    Per T_R = 50 anni c_r = 1.

    Validita': 5 <= T_R <= 500 anni (intervallo coerente con NTC par. 3.3.4).
    """
    t_r_anni = _finite(t_r_anni, "t_r_anni")
    if t_r_anni <= 1:
        raise ValueError("T_R deve essere > 1 anno")
    if t_r_anni < 5 or t_r_anni > 500:
        raise ValueError(
            "T_R fuori intervallo 5-500 anni: NTC par. 3.3.4 limita la formula 3.3.3"
        )
    if abs(t_r_anni - 50.0) < 1e-9:
        return 1.0
    arg = 1.0 - 1.0 / t_r_anni
    inner = -math.log(arg)
    return 0.75 * math.sqrt(1.0 - 0.2 * math.log(inner))


def velocita_progetto_vr(v_b: float, c_r: float) -> float:
    """v_r = c_r * v_b (m/s), NTC par. 3.3.3."""
    v_b = _finite(v_b, "v_b")
    c_r = _finite(c_r, "c_r")
    if v_b <= 0 or c_r <= 0:
        raise ValueError("v_b e c_r devono essere positivi")
    return c_r * v_b


def pressione_cinetica_qr(v_r: float) -> float:
    """Pressione cinetica di riferimento q_r in N/m^2, NTC eq. 3.3.4.

    q_r = 0.5 * rho * v_r^2   con rho = 1.25 kg/m^3
    """
    v_r = _finite(v_r, "v_r")
    if v_r <= 0:
        raise ValueError("v_r deve essere positivo")
    return 0.5 * RHO_ARIA * v_r * v_r


def coefficiente_esposizione_ce(
    z: float, categoria: str, c_t: float = 1.0
) -> float:
    """c_e(z) per categoria di esposizione I-V, NTC eq. 3.3.5.

    c_e(z) = k_r^2 * c_t * ln(z/z_0) * [7 + c_t * ln(z/z_0)]   per z >= z_min
    c_e(z) = c_e(z_min)                                          per z < z_min
    """
    z = _finite(z, "z")
    c_t = _finite(c_t, "c_t")
    if z <= 0:
        raise ValueError("z (quota di riferimento) deve essere positiva")
    if c_t <= 0:
        raise ValueError("c_t deve essere positivo")
    cat = (categoria or "").strip().upper()
    if cat not in CATEGORIE_ESPOSIZIONE:
        raise ValueError(
            f"categoria esposizione '{categoria}' non valida: usare I/II/III/IV/V"
        )
    p = CATEGORIE_ESPOSIZIONE[cat]
    z_eff = max(z, p["z_min"])
    ln_ratio = math.log(z_eff / p["z_0"])
    return p["k_r"] ** 2 * c_t * ln_ratio * (7.0 + c_t * ln_ratio)


@dataclass(frozen=True)
class RisultatoVento:
    v_b_0: float
    a_0: float
    k_s: float
    a_s: float
    v_b: float
    t_r_anni: float
    c_r: float
    v_r: float
    q_r: float
    categoria_esposizione: str
    z: float
    c_t: float
    c_e: float
    c_p: float
    c_d: float
    p: float
    riferimenti: List[str] = field(default_factory=list)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "input": {
                "v_b_0_m_s": self.v_b_0,
                "a_0_m": self.a_0,
                "k_s": self.k_s,
                "a_s_m": self.a_s,
                "t_r_anni": self.t_r_anni,
                "categoria_esposizione": self.categoria_esposizione,
                "z_m": self.z,
                "c_t": self.c_t,
                "c_p": self.c_p,
                "c_d": self.c_d,
            },
            "intermedi": {
                "v_b_m_s": round(self.v_b, 4),
                "c_r": round(self.c_r, 6),
                "v_r_m_s": round(self.v_r, 4),
                "q_r_N_m2": round(self.q_r, 4),
                "c_e": round(self.c_e, 6),
            },
            "output": {
                "p_N_m2": round(self.p, 4),
                "p_kN_m2": round(self.p / 1000.0, 6),
            },
            "riferimenti_ntc": self.riferimenti,
        }


def calcola_pressione_vento(
    v_b_0: float,
    a_0: float,
    k_s: float,
    a_s: float,
    categoria_esposizione: str,
    z: float,
    c_p: float,
    c_d: float = 1.0,
    c_t: float = 1.0,
    t_r_anni: float = 50.0,
) -> RisultatoVento:
    """Calcola la pressione del vento p su un elemento, NTC eq. 3.3.1.

    p = q_r * c_e * c_p * c_d
    """
    v_b = velocita_riferimento_vb(v_b_0, a_0, k_s, a_s)
    c_r = coefficiente_ritorno_cr(t_r_anni)
    v_r = velocita_progetto_vr(v_b, c_r)
    q_r = pressione_cinetica_qr(v_r)
    c_e = coefficiente_esposizione_ce(z, categoria_esposizione, c_t=c_t)
    c_p = _finite(c_p, "c_p")
    c_d = _finite(c_d, "c_d")
    if c_d <= 0:
        raise ValueError("c_d deve essere positivo")
    p = q_r * c_e * c_p * c_d
    return RisultatoVento(
        v_b_0=v_b_0,
        a_0=a_0,
        k_s=k_s,
        a_s=a_s,
        v_b=v_b,
        t_r_anni=t_r_anni,
        c_r=c_r,
        v_r=v_r,
        q_r=q_r,
        categoria_esposizione=(categoria_esposizione or "").strip().upper(),
        z=z,
        c_t=c_t,
        c_e=c_e,
        c_p=c_p,
        c_d=c_d,
        p=p,
        riferimenti=[
            "NTC 2018 par. 3.3.1 - eq. 3.3.1 p = q_r * c_e * c_p * c_d",
            "NTC 2018 par. 3.3.2 - eq. 3.3.2 v_b in funzione di a_s vs a_0",
            "NTC 2018 par. 3.3.4 - eq. 3.3.3-3.3.4 c_r e q_r",
            "NTC 2018 par. 3.3.7 - eq. 3.3.5 c_e(z), Tab. 3.3.II categorie I-V",
        ],
    )


# ---------------------------------------------------------------------------
# NEVE (par. 3.4 NTC 2018)
# ---------------------------------------------------------------------------

def carico_neve_al_suolo_qsk(zona: str, a_s: float) -> float:
    """Valore caratteristico q_sk in kN/m^2, NTC par. 3.4.2 eq. 3.4.1-3.4.4.

    Zona I-Alpina:
        a_s <= 200 m: q_sk = 1.50
        a_s >  200 m: q_sk = 1.39 * [1 + (a_s/728)^2]
    Zona I-Mediterranea:
        a_s <= 200 m: q_sk = 1.50
        a_s >  200 m: q_sk = 1.35 * [1 + (a_s/602)^2]
    Zona II:
        a_s <= 200 m: q_sk = 1.00
        a_s >  200 m: q_sk = 0.85 * [1 + (a_s/481)^2]
    Zona III:
        a_s <= 200 m: q_sk = 0.60
        a_s >  200 m: q_sk = 0.51 * [1 + (a_s/481)^2]
    """
    a_s = _finite(a_s, "a_s")
    if a_s < 0:
        raise ValueError("a_s (altitudine sito) non puo' essere negativa")
    z = (zona or "").strip()
    if z not in ZONE_NEVE:
        raise ValueError(
            f"zona neve '{zona}' non valida: usare una di {ZONE_NEVE}"
        )
    if a_s <= 200.0:
        return {"I-Alpina": 1.50, "I-Mediterranea": 1.50, "II": 1.00, "III": 0.60}[z]
    if z == "I-Alpina":
        return 1.39 * (1.0 + (a_s / 728.0) ** 2)
    if z == "I-Mediterranea":
        return 1.35 * (1.0 + (a_s / 602.0) ** 2)
    if z == "II":
        return 0.85 * (1.0 + (a_s / 481.0) ** 2)
    return 0.51 * (1.0 + (a_s / 481.0) ** 2)


def coefficiente_forma_mu1(alpha_deg: float) -> float:
    """Coefficiente di forma mu_1 per copertura ad una/due falde, NTC par. 3.4.5.2.1.

    0 <=  alpha <= 30:   mu_1 = 0.8
    30 < alpha <  60:   mu_1 = 0.8 * (60 - alpha) / 30
    alpha >= 60:         mu_1 = 0
    """
    alpha_deg = _finite(alpha_deg, "alpha_deg")
    if alpha_deg < 0 or alpha_deg > 90:
        raise ValueError("alpha_deg deve essere in [0, 90]")
    if alpha_deg <= 30.0:
        return 0.8
    if alpha_deg < 60.0:
        return 0.8 * (60.0 - alpha_deg) / 30.0
    return 0.0


def coefficiente_esposizione_neve_ce(classe: str) -> float:
    """c_E per la neve, NTC Tab. 3.4.I.

    battuta_dai_venti -> 0.9
    normale           -> 1.0
    riparata          -> 1.1
    """
    key = (classe or "").strip().lower().replace(" ", "_").replace("-", "_")
    if key not in CLASSI_ESPOSIZIONE_NEVE:
        raise ValueError(
            f"classe esposizione neve '{classe}' non valida: "
            f"usare una di {sorted(CLASSI_ESPOSIZIONE_NEVE)}"
        )
    return CLASSI_ESPOSIZIONE_NEVE[key]


@dataclass(frozen=True)
class RisultatoNeve:
    zona: str
    a_s: float
    q_sk: float
    alpha_deg: float
    mu_1: float
    classe_esposizione: str
    c_E: float
    c_t: float
    q_s: float
    riferimenti: List[str] = field(default_factory=list)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "input": {
                "zona": self.zona,
                "a_s_m": self.a_s,
                "alpha_deg": self.alpha_deg,
                "classe_esposizione": self.classe_esposizione,
                "c_t": self.c_t,
            },
            "intermedi": {
                "q_sk_kN_m2": round(self.q_sk, 6),
                "mu_1": round(self.mu_1, 6),
                "c_E": round(self.c_E, 6),
            },
            "output": {
                "q_s_kN_m2": round(self.q_s, 6),
            },
            "riferimenti_ntc": self.riferimenti,
        }


def calcola_carico_neve(
    zona: str,
    a_s: float,
    alpha_deg: float,
    classe_esposizione: str = "normale",
    c_t: float = 1.0,
) -> RisultatoNeve:
    """Carico neve sulla copertura q_s in kN/m^2, NTC eq. 3.4.1.

    q_s = mu_1 * q_sk * c_E * c_t
    """
    q_sk = carico_neve_al_suolo_qsk(zona, a_s)
    mu_1 = coefficiente_forma_mu1(alpha_deg)
    c_E = coefficiente_esposizione_neve_ce(classe_esposizione)
    c_t = _finite(c_t, "c_t")
    if c_t <= 0:
        raise ValueError("c_t deve essere positivo")
    q_s = mu_1 * q_sk * c_E * c_t
    return RisultatoNeve(
        zona=zona.strip(),
        a_s=a_s,
        q_sk=q_sk,
        alpha_deg=alpha_deg,
        mu_1=mu_1,
        classe_esposizione=(classe_esposizione or "").strip().lower(),
        c_E=c_E,
        c_t=c_t,
        q_s=q_s,
        riferimenti=[
            "NTC 2018 par. 3.4.1 - eq. 3.4.1 q_s = mu_1 * q_sk * c_E * c_t",
            "NTC 2018 par. 3.4.2 - eq. 3.4.1-3.4.4 q_sk per zona e altitudine",
            "NTC 2018 par. 3.4.5.2.1 - mu_1 per copertura a 1-2 falde",
            "NTC 2018 par. 3.4.3 - Tab. 3.4.I c_E topografia",
        ],
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _load_input(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("input JSON deve essere un oggetto")
    return data


def _run_vento(data: Dict[str, Any]) -> Dict[str, Any]:
    res = calcola_pressione_vento(
        v_b_0=data["v_b_0"],
        a_0=data["a_0"],
        k_s=data["k_s"],
        a_s=data["a_s"],
        categoria_esposizione=data["categoria_esposizione"],
        z=data["z"],
        c_p=data["c_p"],
        c_d=data.get("c_d", 1.0),
        c_t=data.get("c_t", 1.0),
        t_r_anni=data.get("t_r_anni", 50.0),
    )
    return res.as_dict()


def _run_neve(data: Dict[str, Any]) -> Dict[str, Any]:
    res = calcola_carico_neve(
        zona=data["zona"],
        a_s=data["a_s"],
        alpha_deg=data["alpha_deg"],
        classe_esposizione=data.get("classe_esposizione", "normale"),
        c_t=data.get("c_t", 1.0),
    )
    return res.as_dict()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_v = sub.add_parser("vento", help="Pressione vento (NTC par. 3.3)")
    p_v.add_argument("--input-json", required=True)
    p_n = sub.add_parser("neve", help="Carico neve (NTC par. 3.4)")
    p_n.add_argument("--input-json", required=True)
    args = parser.parse_args(argv)
    try:
        data = _load_input(args.input_json)
        if args.cmd == "vento":
            out = _run_vento(data)
        else:
            out = _run_neve(data)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    except KeyError as exc:
        print(f"ERRORE: campo mancante nel JSON: {exc}", file=sys.stderr)
        return 2
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERRORE: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
