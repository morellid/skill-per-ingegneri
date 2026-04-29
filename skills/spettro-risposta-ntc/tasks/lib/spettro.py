"""
Spettro di risposta elastico NTC 2018 par. 3.2 - componente orizzontale.

Implementa formule chiuse di:
- NTC 2018 par. 2.4 (vita di riferimento V_R)
- NTC 2018 par. 3.2.1 (probabilita' di superamento P_VR per stato limite, Tab. 3.2.I)
- NTC 2018 par. 3.2.3.2.1 (parametri costruttivi S, eta, TB, TC, TD e ordinate Se(T))
- NTC 2018 Allegato A (interpolazione logaritmica sul reticolo di 9 TR di riferimento)

Riferimenti puntuali ai paragrafi sono nelle docstring delle singole funzioni.

NB: la skill non incorpora il reticolo INGV. L'utente fornisce ag, F0, Tc*
per i 9 TR di riferimento {30, 50, 72, 101, 140, 201, 475, 975, 2475} anni
al sito di interesse, ricavati dal servizio INGV o dal foglio Excel CSLP.

NB v0.1.0-alpha: la test suite copre solo consistenza interna delle
formule (vedi test_spettro.py); il confronto numerico vs foglio CSLP su
casi reali (validazione di campo) e' prerequisito del release stabile e
non e' ancora stato eseguito.

Uso CLI:
    python3 spettro.py --tr-riferimento params.json \\
            --vn 50 --classe-uso II \\
            --cat-sottosuolo C --cat-topografica T1 \\
            --stato-limite SLV \\
            --tabula 0:4:0.05

Vedi --help per opzioni complete.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import Iterable


# --- Costanti normative (NTC 2018) ---------------------------------------

# Tabella 3.2.I NTC 2018: probabilita' di superamento P_VR nel periodo di
# riferimento V_R per ciascuno stato limite.
P_VR: dict[str, float] = {
    "SLO": 0.81,
    "SLD": 0.63,
    "SLV": 0.10,
    "SLC": 0.05,
}

# par. 2.4.3 NTC: coefficiente d'uso C_U per classe d'uso (Tab. 2.4.II).
C_U: dict[str, float] = {
    "I": 0.7,
    "II": 1.0,
    "III": 1.5,
    "IV": 2.0,
}

# Tabella 3.2.IV NTC: categoria topografica -> ST in sommita' del rilievo.
S_T: dict[str, float] = {
    "T1": 1.0,
    "T2": 1.2,
    "T3": 1.2,
    "T4": 1.4,
}

# Allegato A NTC: 9 TR di riferimento del reticolo INGV [anni].
TR_RIFERIMENTO: tuple[int, ...] = (30, 50, 72, 101, 140, 201, 475, 975, 2475)


# --- Strutture dati ------------------------------------------------------


def _assert_finito(nome: str, valore: float) -> float:
    """Valida che `valore` sia un numero reale finito (no NaN/inf, no bool, no string).

    Restituisce il valore come float in caso di successo, solleva ValueError
    altrimenti. Usato da entry point pubblici (vita_riferimento, coeff_eta,
    Se_T, CLI) per garantire fail-closed su input non-finiti, coerentemente
    con la validazione vettoriale di ParametriRiferimento.__post_init__.
    """
    if isinstance(valore, bool) or not isinstance(valore, (int, float)):
        raise ValueError(f"{nome}: atteso numero reale, ricevuto {valore!r}")
    if not math.isfinite(valore):
        raise ValueError(f"{nome}: atteso valore finito, ricevuto {valore!r} (NaN o inf)")
    return float(valore)


@dataclass
class ParametriRiferimento:
    """Parametri di pericolosita' al sito per i 9 TR di riferimento.

    Ogni lista ha lunghezza 9, allineata con TR_RIFERIMENTO.

    ag: accelerazione orizzontale massima al sito su sottosuolo rigido [g]
    F0: valore massimo del fattore di amplificazione spettrale [adim.]
    Tc_star: periodo di inizio del tratto a velocita' costante dello
             spettro orizzontale di riferimento [s]
    """

    ag: list[float]
    F0: list[float]
    Tc_star: list[float]

    def __post_init__(self) -> None:
        # Range di sanita' usati come hint nei messaggi d'errore (non vincoli rigidi).
        # ag in g (frazione di g): un sito italiano sta tipicamente in [0.001, 1.0].
        # F0 e' adimensionale, range tipico [2.0, 3.5].
        # Tc* in secondi, range tipico [0.10, 0.60].
        hints: dict[str, str] = {
            "ag": "ag e' atteso in g (frazione di g, non m/s^2): tipico in [0.001, 1.0]",
            "F0": "F0 e' adimensionale, tipico in [2.0, 3.5]",
            "Tc_star": "Tc* in [s], tipico in [0.10, 0.60]",
        }
        for nome, valori in (("ag", self.ag), ("F0", self.F0), ("Tc_star", self.Tc_star)):
            if len(valori) != len(TR_RIFERIMENTO):
                raise ValueError(
                    f"{nome}: attesi {len(TR_RIFERIMENTO)} valori (uno per TR di "
                    f"riferimento {list(TR_RIFERIMENTO)}), ricevuti {len(valori)}"
                )
            for k, v in enumerate(valori):
                if not isinstance(v, (int, float)) or isinstance(v, bool):
                    raise ValueError(
                        f"{nome}[{k}] (TR={TR_RIFERIMENTO[k]} anni): valore non "
                        f"numerico {v!r}. {hints[nome]}."
                    )
                if not math.isfinite(v):
                    raise ValueError(
                        f"{nome}[{k}] (TR={TR_RIFERIMENTO[k]} anni): valore non "
                        f"finito {v!r} (NaN o inf). {hints[nome]}."
                    )
                if v <= 0.0:
                    raise ValueError(
                        f"{nome}[{k}] (TR={TR_RIFERIMENTO[k]} anni): atteso "
                        f"strettamente positivo, ricevuto {v!r}. {hints[nome]}."
                    )


@dataclass
class ParametriSpettro:
    """Parametri costruttivi dello spettro per uno stato limite."""

    stato_limite: str
    TR: float
    ag: float  # [g]
    F0: float
    Tc_star: float  # [s]
    cat_sottosuolo: str
    cat_topografica: str
    SS: float
    ST: float
    S: float  # = SS * ST
    CC: float
    eta: float
    TB: float  # [s]
    TC: float  # [s]
    TD: float  # [s]


@dataclass
class OrdinataSpettro:
    """Ordinata Se(T) tabulata."""

    T: float  # [s]
    Se: float  # [g]
    ramo: str  # uno fra: "0-TB", "TB-TC", "TC-TD", "TD-inf"


@dataclass
class RisultatoSpettro:
    """Output completo del calcolo per uno stato limite."""

    parametri: ParametriSpettro
    ordinate: list[OrdinataSpettro] = field(default_factory=list)


# --- Calcolo TR e probabilita' di superamento ----------------------------


def vita_riferimento(vn_anni: float, classe_uso: str) -> float:
    """V_R = V_N * C_U  (NTC par. 2.4.3, eq. 2.4.1).

    V_R minima 35 anni e' applicata sotto come prescritto da par. 2.4.3.
    """
    vn_anni = _assert_finito("Vita nominale V_N", vn_anni)
    if vn_anni <= 0:
        raise ValueError("Vita nominale V_N deve essere positiva")
    cu = classe_uso.upper() if isinstance(classe_uso, str) else classe_uso
    if cu not in C_U:
        raise ValueError(f"Classe d'uso {classe_uso!r} non valida (attesa: {list(C_U)})")
    vr = vn_anni * C_U[cu]
    # par. 2.4.3 NTC: "se V_R risulta inferiore a 35 anni, si assume comunque V_R = 35 anni".
    return max(vr, 35.0)


def tempo_ritorno(vita_riferimento_anni: float, p_vr: float) -> float:
    """T_R = - V_R / ln(1 - P_VR)  (NTC par. 3.2.1, eq. 3.2.0).

    Inverso della relazione P_VR = 1 - exp(-V_R/T_R).
    """
    if not 0.0 < p_vr < 1.0:
        raise ValueError("P_VR deve essere in (0, 1)")
    return -vita_riferimento_anni / math.log(1.0 - p_vr)


def tempi_ritorno_per_stati_limite(
    vn_anni: float, classe_uso: str
) -> dict[str, float]:
    """Calcola TR per i 4 stati limite dati VN e classe d'uso."""
    vr = vita_riferimento(vn_anni, classe_uso)
    return {sl: tempo_ritorno(vr, p) for sl, p in P_VR.items()}


# --- Interpolazione logaritmica sui TR di riferimento --------------------


def _interpola_log(
    tr_target: float,
    tr_riferimento: Iterable[float],
    valori: Iterable[float],
) -> float:
    """Interpolazione logaritmica di un parametro p su TR.

    log(p) = log(p_k) + (log(p_{k+1}) - log(p_k)) *
                        (log(T*/T_k) / log(T_{k+1}/T_k))

    Procedura prescritta da NTC Allegato A e ripresa da Circolare 7/2019
    Appendice C3.2.

    Per ag, F0, Tc* tutti i valori sono positivi e monotonia non
    necessariamente assicurata; l'interpolazione log-log e' comunque
    quella adottata dal foglio CSLP.
    """
    tr_lst = list(tr_riferimento)
    val_lst = list(valori)
    if len(tr_lst) != len(val_lst):
        raise ValueError("Liste di TR e valori devono avere la stessa lunghezza")
    if not tr_lst:
        raise ValueError("Lista TR di riferimento vuota")

    # Range del reticolo: NTC raccomanda TR in [30, 2475] per costruzioni ordinarie.
    if tr_target < tr_lst[0] or tr_target > tr_lst[-1]:
        raise ValueError(
            f"TR target {tr_target:.1f} anni e' fuori dal reticolo di riferimento "
            f"[{tr_lst[0]}, {tr_lst[-1]}]: estrapolazione non eseguita "
            f"(NTC Allegato A)."
        )

    # Esatto match
    for i, tr_i in enumerate(tr_lst):
        if math.isclose(tr_i, tr_target, rel_tol=1e-9, abs_tol=1e-9):
            return val_lst[i]

    # Trova bracket
    for i in range(len(tr_lst) - 1):
        t_lo, t_hi = tr_lst[i], tr_lst[i + 1]
        if t_lo < tr_target < t_hi:
            v_lo, v_hi = val_lst[i], val_lst[i + 1]
            if v_lo <= 0 or v_hi <= 0:
                raise ValueError("Interpolazione log richiede valori positivi")
            log_v = (
                math.log(v_lo)
                + (math.log(v_hi) - math.log(v_lo))
                * math.log(tr_target / t_lo)
                / math.log(t_hi / t_lo)
            )
            return math.exp(log_v)

    # Non dovremmo arrivare qui dato il check su range
    raise AssertionError("bracket non trovato pur essendo in range")


def parametri_al_TR(
    tr_target: float, riferimento: ParametriRiferimento
) -> tuple[float, float, float]:
    """Restituisce (ag, F0, Tc*) interpolati al TR target."""
    ag = _interpola_log(tr_target, TR_RIFERIMENTO, riferimento.ag)
    f0 = _interpola_log(tr_target, TR_RIFERIMENTO, riferimento.F0)
    tcs = _interpola_log(tr_target, TR_RIFERIMENTO, riferimento.Tc_star)
    return ag, f0, tcs


# --- Coefficienti SS, CC e periodi TB, TC, TD ----------------------------


def coeff_SS(cat_sottosuolo: str, ag_g: float, F0: float) -> float:
    """Coefficiente di amplificazione stratigrafica SS (NTC Tab. 3.2.IV).

    ag_g: ag espresso in unita' di g (adimensionale).
    Per cat. A: SS = 1.0.
    Per cat. B/C/D/E: formula con clamp ai limiti di tabella.
    Per cat. S1/S2: NTC par. 3.2.2 prescrive analisi specifiche di risposta
    sismica locale -> errore esplicito.
    """
    cat = cat_sottosuolo.upper()
    fa = F0 * ag_g  # F_0 * ag/g
    if cat == "A":
        return 1.0
    if cat == "B":
        return min(1.20, max(1.00, 1.40 - 0.40 * fa))
    if cat == "C":
        return min(1.50, max(1.00, 1.70 - 0.60 * fa))
    if cat == "D":
        return min(1.80, max(0.90, 2.40 - 1.50 * fa))
    if cat == "E":
        return min(1.60, max(1.00, 2.00 - 1.10 * fa))
    if cat in {"S1", "S2"}:
        raise ValueError(
            f"Categoria di sottosuolo {cat}: NTC par. 3.2.2 prescrive analisi "
            "specifiche di risposta sismica locale. Calcolo non eseguibile con "
            "questa skill."
        )
    raise ValueError(f"Categoria di sottosuolo {cat!r} non riconosciuta")


def coeff_CC(cat_sottosuolo: str, Tc_star: float) -> float:
    """Coefficiente CC per il calcolo di TC (NTC Tab. 3.2.IV).

    Tc_star in [s].
    """
    cat = cat_sottosuolo.upper()
    if cat == "A":
        return 1.00
    if cat == "B":
        return 1.10 * Tc_star ** (-0.20)
    if cat == "C":
        return 1.05 * Tc_star ** (-0.33)
    if cat == "D":
        return 1.25 * Tc_star ** (-0.50)
    if cat == "E":
        return 1.15 * Tc_star ** (-0.40)
    if cat in {"S1", "S2"}:
        raise ValueError(
            f"Categoria di sottosuolo {cat}: analisi specifiche richieste "
            "(NTC par. 3.2.2)."
        )
    raise ValueError(f"Categoria di sottosuolo {cat!r} non riconosciuta")


def coeff_eta(xi_percento: float) -> float:
    """Fattore di alterazione dello smorzamento viscoso (NTC eq. 3.2.6).

    eta = sqrt(10 / (5 + xi)) >= 0.55, dove xi in %.
    Per xi = 5 -> eta = 1.0.
    """
    xi_percento = _assert_finito("xi (smorzamento %)", xi_percento)
    if xi_percento < 0:
        raise ValueError("xi (smorzamento %) deve essere >= 0")
    eta = math.sqrt(10.0 / (5.0 + xi_percento))
    return max(eta, 0.55)


def periodi_caratteristici(
    Tc_star: float, ag_g: float, cat_sottosuolo: str
) -> tuple[float, float, float, float]:
    """Restituisce (CC, TB, TC, TD).

    NTC eq. 3.2.7-3.2.8:
    TC = CC * Tc_star
    TB = TC / 3
    TD = 4 * ag_g + 1.6   [s]
    """
    cc = coeff_CC(cat_sottosuolo, Tc_star)
    tc = cc * Tc_star
    tb = tc / 3.0
    td = 4.0 * ag_g + 1.6
    return cc, tb, tc, td


# --- Spettro elastico orizzontale Se(T) ---------------------------------


def Se_T(T: float, p: ParametriSpettro) -> tuple[float, str]:
    """Ordinata Se(T) per la componente orizzontale (NTC eq. 3.2.4).

    Tutti i ag, F0 sono valori al sito (gia' interpolati al TR di progetto).
    Restituisce (Se in g, etichetta del ramo).

    NTC eq. 3.2.4:
      0 <= T < TB:    Se = ag*S*eta*F0*[T/TB + 1/(eta*F0)*(1 - T/TB)]
      TB <= T < TC:   Se = ag*S*eta*F0
      TC <= T < TD:   Se = ag*S*eta*F0*(TC/T)
      TD <= T:        Se = ag*S*eta*F0*(TC*TD/T^2)
    """
    T = _assert_finito("T", T)
    if T < 0:
        raise ValueError("T deve essere >= 0")
    base = p.ag * p.S * p.eta * p.F0
    if T < p.TB:
        if p.TB == 0:
            return base, "TB-TC"
        # eq. 3.2.4 ramo iniziale (lineare crescente da ag*S a ag*S*eta*F0)
        se = base * (T / p.TB + 1.0 / (p.eta * p.F0) * (1.0 - T / p.TB))
        return se, "0-TB"
    if T < p.TC:
        return base, "TB-TC"
    if T < p.TD:
        return base * (p.TC / T), "TC-TD"
    return base * (p.TC * p.TD / (T * T)), "TD-inf"


# --- Pipeline completa --------------------------------------------------


def calcola_parametri(
    stato_limite: str,
    vn_anni: float,
    classe_uso: str,
    cat_sottosuolo: str,
    cat_topografica: str,
    riferimento: ParametriRiferimento,
    xi_percento: float = 5.0,
) -> ParametriSpettro:
    """Pipeline: VN/CU -> TR -> ag,F0,Tc* -> S, eta, TB, TC, TD."""
    sl = stato_limite.upper()
    if sl not in P_VR:
        raise ValueError(f"Stato limite {sl!r} non valido (attesi: {list(P_VR)})")
    vr = vita_riferimento(vn_anni, classe_uso)
    tr = tempo_ritorno(vr, P_VR[sl])
    ag, f0, tcs = parametri_al_TR(tr, riferimento)
    ss = coeff_SS(cat_sottosuolo, ag, f0)
    if cat_topografica.upper() not in S_T:
        raise ValueError(
            f"Categoria topografica {cat_topografica!r} non valida (attesi: {list(S_T)})"
        )
    st = S_T[cat_topografica.upper()]
    s = ss * st
    cc, tb, tc, td = periodi_caratteristici(tcs, ag, cat_sottosuolo)
    eta = coeff_eta(xi_percento)
    return ParametriSpettro(
        stato_limite=sl,
        TR=tr,
        ag=ag,
        F0=f0,
        Tc_star=tcs,
        cat_sottosuolo=cat_sottosuolo.upper(),
        cat_topografica=cat_topografica.upper(),
        SS=ss,
        ST=st,
        S=s,
        CC=cc,
        eta=eta,
        TB=tb,
        TC=tc,
        TD=td,
    )


def tabula_spettro(
    parametri: ParametriSpettro, periodi: Iterable[float]
) -> list[OrdinataSpettro]:
    """Tabula Se(T) sui periodi richiesti."""
    out: list[OrdinataSpettro] = []
    for t in periodi:
        se, ramo = Se_T(t, parametri)
        out.append(OrdinataSpettro(T=t, Se=se, ramo=ramo))
    return out


# --- I/O parametri di riferimento ---------------------------------------


def _reject_nan_inf(token: str) -> float:
    """Hook per json.load: rifiuta i token JSON non standard NaN/Infinity/-Infinity.

    JSON standard (RFC 8259) non ammette questi token; il parser di Python li
    accetta di default. Per evitare che NaN/inf si propaghino silenziosamente
    nel calcolo dello spettro, li rifiutiamo a livello di I/O.
    """
    raise ValueError(
        f"token JSON non ammesso: {token!r}. RFC 8259 non consente "
        f"NaN/Infinity/-Infinity; passa un numero finito."
    )


def carica_parametri_riferimento(path: str) -> ParametriRiferimento:
    """Carica i parametri (ag, F0, Tc*) per i 9 TR da file JSON.

    Schema atteso:
    {
      "tr_anni": [30, 50, 72, 101, 140, 201, 475, 975, 2475],
      "ag_g":    [...9 valori...],
      "F0":      [...9 valori...],
      "Tc_star": [...9 valori...]
    }

    Se "tr_anni" e' presente, deve coincidere con TR_RIFERIMENTO.
    """
    with open(path, encoding="utf-8") as f:
        raw = json.load(f, parse_constant=_reject_nan_inf)
    if "tr_anni" in raw and tuple(raw["tr_anni"]) != TR_RIFERIMENTO:
        raise ValueError(
            f"tr_anni nel file deve essere {list(TR_RIFERIMENTO)}, "
            f"trovato {raw['tr_anni']}"
        )
    mancanti = [k for k in ("ag_g", "F0", "Tc_star") if k not in raw]
    if mancanti:
        raise ValueError(
            f"chiavi mancanti nel file parametri di riferimento: {mancanti}. "
            f"Schema atteso: tr_anni (opzionale), ag_g, F0, Tc_star (9 valori ciascuno)."
        )
    return ParametriRiferimento(
        ag=list(raw["ag_g"]),
        F0=list(raw["F0"]),
        Tc_star=list(raw["Tc_star"]),
    )


# --- CLI ----------------------------------------------------------------


def _parse_periodi(spec: str) -> list[float]:
    """Espande spec del tipo 'start:stop:step' in lista di periodi."""
    parti = spec.split(":")
    if len(parti) != 3:
        raise argparse.ArgumentTypeError(
            "spec periodi attesa nel formato 'start:stop:step' (es. '0:4:0.05')"
        )
    try:
        start, stop, step = (float(p) for p in parti)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"spec periodi: numero non valido ({e})")
    for nome, v in (("start", start), ("stop", stop), ("step", step)):
        if not math.isfinite(v):
            raise argparse.ArgumentTypeError(
                f"spec periodi: {nome} deve essere finito (no NaN/inf), ricevuto {v!r}"
            )
    if step <= 0:
        raise argparse.ArgumentTypeError("step deve essere > 0")
    if stop < start:
        raise argparse.ArgumentTypeError(
            f"spec periodi: stop ({stop}) deve essere >= start ({start})"
        )
    out: list[float] = []
    t = start
    # tolleranza per evitare ultimo punto fuori per arrotondamento
    while t <= stop + 1e-9:
        out.append(round(t, 6))
        t += step
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Spettro di risposta elastico orizzontale NTC 2018 par. 3.2",
        epilog=(
            "Modalita' di input: (A) --input-json punta a un singolo file con "
            "tutti i parametri (parametri_calcolo + parametri_pericolosita_sito) "
            "e gli altri flag scalari sono ignorati; (B) i flag scalari "
            "--tr-riferimento/--vn/--classe-uso/--cat-sottosuolo/--cat-topografica "
            "sono tutti richiesti, --stato-limite/--xi/--tabula opzionali."
        ),
    )
    parser.add_argument(
        "--input-json",
        default=None,
        help=(
            "File JSON con tutti i parametri di input (oggetti "
            "parametri_calcolo e parametri_pericolosita_sito). Schema: "
            "vedi examples/caso-conforme-fittizio-cu2-c-t1/input.json. "
            "Se passato, sovrascrive --tr-riferimento, --vn, --classe-uso, "
            "--cat-sottosuolo, --cat-topografica, --xi, --stato-limite, --tabula."
        ),
    )
    parser.add_argument(
        "--tr-riferimento",
        default=None,
        help=(
            "File JSON con ag_g, F0, Tc_star (9 valori ciascuno) per i TR di "
            "riferimento {30,50,72,101,140,201,475,975,2475} anni. Required "
            "in modalita' B (no --input-json)."
        ),
    )
    parser.add_argument("--vn", type=float, default=None, help="Vita nominale V_N [anni]")
    parser.add_argument(
        "--classe-uso", choices=list(C_U), default=None, help="Classe d'uso (par. 2.4.2 NTC)"
    )
    parser.add_argument(
        "--cat-sottosuolo",
        default=None,
        help="Categoria di sottosuolo: A, B, C, D, E (S1/S2 non supportate)",
    )
    parser.add_argument(
        "--cat-topografica",
        choices=list(S_T),
        default=None,
        help="Categoria topografica T1/T2/T3/T4 (Tab. 3.2.IV NTC)",
    )
    parser.add_argument(
        "--stato-limite",
        choices=list(P_VR) + ["TUTTI"],
        default=None,
        help="Stato limite: SLO, SLD, SLV, SLC, oppure TUTTI (default in modalita' B)",
    )
    parser.add_argument(
        "--xi", type=float, default=None, help="Smorzamento viscoso xi [%%] (default 5 in modalita' B)"
    )
    parser.add_argument(
        "--tabula",
        type=_parse_periodi,
        default=None,
        help="Tabula Se(T) su periodi spec 'start:stop:step' (es. '0:4:0.05')",
    )
    parser.add_argument(
        "--out-csv",
        default=None,
        help="Path CSV output con tabella Se(T). Se omesso, output a stdout.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Stampa i parametri spettro in JSON invece che testo umano",
    )

    args = parser.parse_args(argv)

    if args.input_json is not None:
        # Modalita' A: tutto da un singolo file JSON. I flag scalari sono ignorati
        # (warning silenzioso in argparse, esplicito qui solo se l'utente li passa).
        try:
            with open(args.input_json, encoding="utf-8") as f:
                full = json.load(f, parse_constant=_reject_nan_inf)
        except ValueError as e:
            parser.error(f"--input-json: parse error: {e}")
        try:
            pc = full["parametri_calcolo"]
            sito = full["parametri_pericolosita_sito"]
        except KeyError as e:
            parser.error(
                f"--input-json: chiave mancante {e!r}. Atteso schema con "
                f"'parametri_calcolo' e 'parametri_pericolosita_sito'. "
                f"Vedi examples/caso-conforme-fittizio-cu2-c-t1/input.json."
            )
        if "tr_anni" in sito and tuple(sito["tr_anni"]) != TR_RIFERIMENTO:
            parser.error(
                f"--input-json: tr_anni in parametri_pericolosita_sito deve "
                f"essere {list(TR_RIFERIMENTO)}, trovato {sito['tr_anni']}"
            )
        sito_mancanti = [k for k in ("ag_g", "F0", "Tc_star") if k not in sito]
        if sito_mancanti:
            parser.error(
                f"--input-json: parametri_pericolosita_sito: chiavi mancanti "
                f"{sito_mancanti}. Schema atteso: tr_anni (opzionale), ag_g, "
                f"F0, Tc_star (9 valori ciascuno)."
            )
        try:
            riferimento = ParametriRiferimento(
                ag=list(sito["ag_g"]),
                F0=list(sito["F0"]),
                Tc_star=list(sito["Tc_star"]),
            )
        except ValueError as e:
            parser.error(f"--input-json: parametri_pericolosita_sito non valido: {e}")
        pc_mancanti = [
            k for k in ("vn_anni", "classe_uso", "cat_sottosuolo", "cat_topografica")
            if k not in pc
        ]
        if pc_mancanti:
            parser.error(
                f"--input-json: parametri_calcolo: chiavi mancanti {pc_mancanti}."
            )
        try:
            vn = float(pc["vn_anni"])
            xi = float(pc.get("xi_percento", 5.0))
        except (TypeError, ValueError) as e:
            parser.error(
                f"--input-json: vn_anni/xi_percento devono essere numerici ({e})"
            )
        classe_uso = pc["classe_uso"]
        cat_sottosuolo = pc["cat_sottosuolo"]
        cat_topografica = pc["cat_topografica"]
        sl_list = pc.get("stati_limite")
        if sl_list is None:
            stati = list(P_VR)
        elif isinstance(sl_list, list):
            stati = [s.upper() for s in sl_list]
        else:
            parser.error(
                f"--input-json: parametri_calcolo.stati_limite deve essere "
                f"lista o omesso, trovato {type(sl_list).__name__}"
            )
        tab = pc.get("tabula_periodi")
        if tab:
            tab_mancanti = [k for k in ("start", "stop", "step") if k not in tab]
            if tab_mancanti:
                parser.error(
                    f"--input-json: parametri_calcolo.tabula_periodi: chiavi "
                    f"mancanti {tab_mancanti} (attese: start, stop, step)."
                )
            try:
                tabula = _parse_periodi(f"{tab['start']}:{tab['stop']}:{tab['step']}")
            except (argparse.ArgumentTypeError, ValueError) as e:
                parser.error(f"--input-json: tabula_periodi non valido: {e}")
        else:
            tabula = None
    else:
        # Modalita' B: flag scalari richiesti.
        missing = [
            n for n, v in (
                ("--tr-riferimento", args.tr_riferimento),
                ("--vn", args.vn),
                ("--classe-uso", args.classe_uso),
                ("--cat-sottosuolo", args.cat_sottosuolo),
                ("--cat-topografica", args.cat_topografica),
            )
            if v is None
        ]
        if missing:
            parser.error(
                f"in modalita' senza --input-json sono richiesti: {', '.join(missing)}. "
                f"Alternativa: usa --input-json puntando a un file con tutti i parametri."
            )
        try:
            riferimento = carica_parametri_riferimento(args.tr_riferimento)
        except (ValueError, KeyError) as e:
            parser.error(f"--tr-riferimento: file non valido: {e}")
        vn = args.vn
        classe_uso = args.classe_uso
        cat_sottosuolo = args.cat_sottosuolo
        cat_topografica = args.cat_topografica
        xi = 5.0 if args.xi is None else args.xi
        stato_limite = args.stato_limite or "TUTTI"
        stati = list(P_VR) if stato_limite == "TUTTI" else [stato_limite]
        tabula = args.tabula

    risultati: list[RisultatoSpettro] = []
    for sl in stati:
        try:
            p = calcola_parametri(
                sl,
                vn,
                classe_uso,
                cat_sottosuolo,
                cat_topografica,
                riferimento,
                xi_percento=xi,
            )
        except ValueError as e:
            parser.error(f"calcolo {sl} fallito: {e}")
        ordinate = tabula_spettro(p, tabula) if tabula else []
        risultati.append(RisultatoSpettro(parametri=p, ordinate=ordinate))

    if args.json:
        out = [
            {
                "parametri": asdict(r.parametri),
                "ordinate": [asdict(o) for o in r.ordinate],
            }
            for r in risultati
        ]
        json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        for r in risultati:
            p = r.parametri
            print(f"=== {p.stato_limite} ===")
            print(f"  TR        = {p.TR:>10.2f} anni")
            print(f"  ag        = {p.ag:>10.4f} g")
            print(f"  F0        = {p.F0:>10.4f}")
            print(f"  Tc*       = {p.Tc_star:>10.4f} s")
            print(f"  cat. sottosuolo = {p.cat_sottosuolo}    cat. topografica = {p.cat_topografica}")
            print(f"  SS        = {p.SS:>10.4f}    ST = {p.ST:.2f}    S = {p.S:.4f}")
            print(f"  CC        = {p.CC:>10.4f}    eta = {p.eta:.4f}")
            print(f"  TB,TC,TD  = {p.TB:.4f}, {p.TC:.4f}, {p.TD:.4f} s")
            if r.ordinate:
                print(f"  Tabella Se(T) [{len(r.ordinate)} punti]:")
                for o in r.ordinate:
                    print(f"    T = {o.T:>6.3f} s   Se = {o.Se:>9.5f} g   [{o.ramo}]")
            print()

    if args.out_csv and any(r.ordinate for r in risultati):
        with open(args.out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["stato_limite", "T_s", "Se_g", "ramo"])
            for r in risultati:
                for o in r.ordinate:
                    w.writerow([r.parametri.stato_limite, o.T, o.Se, o.ramo])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
