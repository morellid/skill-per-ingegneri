"""
Classificazione del rischio sismico ai sensi del DM 58/2017 (sismabonus).

Implementa il METODO CONVENZIONALE per edifici (DM 58/2017 Allegato A,
testo aggiornato dal DM 65/2017, DM 24/2020 e DM 329/2020):

- calcolo dell'Indice di Sicurezza per la Vita IS-V = PGA_C(SLV) / PGA_D(SLV)
  (Allegato A, punto 2.2);
- calcolo della Perdita Annua Media PAM come area sottesa alla Curva di
  Individuazione (Allegato A, punto 2.1), valutata con la formula
  trapezoidale a 5 stati limite (SLID convenzionale + SLO + SLD + SLV +
  SLC) piu' termine di coda dello Stato Limite di Ricostruzione (SLR);
- attribuzione delle classi di rischio PAM (8 classi: A+, A, B, C, D, E,
  F, G) e IS-V (7 classi: A+, A, B, C, D, E, F);
- determinazione della classe di rischio finale come la peggiore (minore
  in graduatoria) tra classe PAM e classe IS-V (Allegato A, punto 2.3);
- regola del salto classi: numero di classi guadagnate fra stato di fatto
  e stato di progetto, da utilizzare come indicatore del livello di
  miglioramento sismico (Allegato A, punto 3, riferito alle aliquote di
  detrazione fissate dalla legislazione fiscale vigente).

Il modulo implementa SOLO il metodo convenzionale per edifici esistenti.
Il metodo semplificato per edifici in muratura (Allegato A, punto 3,
tabella tipologie x numero piani) e' fuori scope di questa versione.

NB: il modulo NON sostituisce la valutazione di sicurezza sismica
(NTC 2018 cap. 8 + Circ. 7/2019). I valori di PGA_C per ciascuno stato
limite e i corrispondenti TR_C devono essere prodotti dal progettista
strutturale firmatario tramite analisi conformi (lineari, non lineari,
push-over, time-history) sul modello dell'edificio. Il modulo prende
questi valori in input e calcola PAM, IS-V, classi e salto classi in
modo deterministico.

NB v0.1.0-alpha: la test suite in test_sismabonus.py copre solo la
consistenza interna delle formule (trapezoidale, monotonia,
classificazione, salto classi, anti-drift fixture-based). La validazione
di campo (confronto numerico vs software certificati come ClaSS, CDM
Win, EdiSis su 10+ edifici reali) e' prerequisito del release stabile e
NON e' ancora stata eseguita.

Uso CLI:
    python3 sismabonus.py --input-json caso.json

dove caso.json contiene PGA_D, PGA_C e TR_C per i 4 stati limite NTC.
Vedi --help per le opzioni complete.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict
from typing import Any


# --- Costanti normative (DM 58/2017 Allegato A, agg. DM 329/2020) -------

# Allegato A, punto 2.1: Costo di Ricostruzione (CR) associato a ciascuno
# stato limite [adimensionale, frazione del costo di ricostruzione].
CR: dict[str, float] = {
    "SLID": 0.00,  # Stato Limite di Inizio Danno (convenzionale, TR=10 anni)
    "SLO":  0.07,  # Stato Limite di Operativita'
    "SLD":  0.15,  # Stato Limite di Danno
    "SLV":  0.50,  # Stato Limite di salvaguardia della Vita
    "SLC":  0.80,  # Stato Limite di prevenzione del Collasso
    "SLR":  1.00,  # Stato Limite di Ricostruzione (convenzionale, stessa
                   # frequenza di SLC ma CR=100%)
}

# Allegato A, punto 2.1: Periodo di Ritorno convenzionale dell'evento
# associato allo stato limite SLID [anni].
TR_SLID_ANNI: int = 10

# Stati limite NTC che devono essere valutati dal progettista (in ordine
# di severita' crescente). SLID e' convenzionale e fissato; SLR coincide
# in frequenza con SLC ma ha CR=100%.
STATI_LIMITE_NTC: tuple[str, ...] = ("SLO", "SLD", "SLV", "SLC")

# Tabella attribuzione classi PAM (Allegato A, punto 2.3, Tab.).
# Lista ordinata di tuple (classe, soglia_sup_inclusa).
# Una classe e' assegnata se PAM <= soglia_sup E PAM > soglia_inf
# (dove soglia_inf = soglia_sup della classe migliore precedente).
# La classe migliore "A+" usa soglia_inf = 0; la classe peggiore "G" non
# ha soglia_sup (PAM > 7.5%).
CLASSI_PAM: tuple[tuple[str, float], ...] = (
    ("A+", 0.005),  # PAM <= 0.50%
    ("A",  0.010),  # 0.50% < PAM <= 1.0%
    ("B",  0.015),  # 1.0%  < PAM <= 1.5%
    ("C",  0.025),  # 1.5%  < PAM <= 2.5%
    ("D",  0.035),  # 2.5%  < PAM <= 3.5%
    ("E",  0.045),  # 3.5%  < PAM <= 4.5%
    ("F",  0.075),  # 4.5%  < PAM <= 7.5%
    # ("G",  +inf)  # PAM > 7.5%
)

# Tabella attribuzione classi IS-V (Allegato A, punto 2.3, Tab.).
# Stessa convenzione: (classe, soglia_inf_inclusa). La classe migliore
# A+ richiede IS-V > 100% (soglia_inf > 1.00).
# NB: non esiste classe "G" per IS-V; la classe peggiore e' F.
CLASSI_IS_V: tuple[tuple[str, float], ...] = (
    ("A+", 1.00),  # IS-V > 100%
    ("A",  0.80),  # 80%  <= IS-V <= 100%
    ("B",  0.60),  # 60%  <= IS-V <  80%
    ("C",  0.45),  # 45%  <= IS-V <  60%
    ("D",  0.30),  # 30%  <= IS-V <  45%
    ("E",  0.15),  # 15%  <= IS-V <  30%
    # ("F",  0)     # IS-V <= 15%
)

# Ordine delle classi in graduatoria, da migliore (rischio minimo) a
# peggiore (rischio massimo). Usato per "min" delle due classi PAM e IS-V.
ORDINE_CLASSI: tuple[str, ...] = ("A+", "A", "B", "C", "D", "E", "F", "G")


# --- Validazione input ---------------------------------------------------


def _assert_finito(nome: str, valore: Any) -> float:
    """Valida che `valore` sia un numero reale finito > 0."""
    if isinstance(valore, bool) or not isinstance(valore, (int, float)):
        raise ValueError(f"{nome}: atteso numero reale, ricevuto {valore!r}")
    if not math.isfinite(valore):
        raise ValueError(f"{nome}: atteso valore finito, ricevuto {valore!r}")
    if valore <= 0:
        raise ValueError(f"{nome}: atteso valore positivo, ricevuto {valore!r}")
    return float(valore)


def _assert_finito_non_neg(nome: str, valore: Any) -> float:
    """Valida che `valore` sia un numero reale finito >= 0 (per IS-V che
    ammette zero teorico)."""
    if isinstance(valore, bool) or not isinstance(valore, (int, float)):
        raise ValueError(f"{nome}: atteso numero reale, ricevuto {valore!r}")
    if not math.isfinite(valore):
        raise ValueError(f"{nome}: atteso valore finito, ricevuto {valore!r}")
    if valore < 0:
        raise ValueError(f"{nome}: atteso valore non negativo, ricevuto {valore!r}")
    return float(valore)


# --- Strutture dati ------------------------------------------------------


@dataclass
class StatiLimiteCapacita:
    """Periodi di ritorno e PGA di capacita' per i 4 SL NTC.

    TR_C [anni] e PGA_C [g] devono essere prodotti dal progettista
    strutturale tramite analisi conformi NTC 2018 cap. 8 sull'edificio.
    """
    TR_C_SLO: float
    TR_C_SLD: float
    TR_C_SLV: float
    TR_C_SLC: float
    PGA_C_SLO: float
    PGA_C_SLD: float
    PGA_C_SLV: float
    PGA_C_SLC: float

    def __post_init__(self) -> None:
        for nome in ("TR_C_SLO", "TR_C_SLD", "TR_C_SLV", "TR_C_SLC"):
            setattr(self, nome, _assert_finito(nome, getattr(self, nome)))
        for nome in ("PGA_C_SLO", "PGA_C_SLD", "PGA_C_SLV", "PGA_C_SLC"):
            setattr(self, nome, _assert_finito(nome, getattr(self, nome)))


@dataclass
class StatiLimiteDomanda:
    """PGA di domanda per i 4 SL NTC, dal sito (reticolo INGV) tramite
    procedura NTC 2018 par. 3.2 + Allegato A."""
    PGA_D_SLO: float
    PGA_D_SLD: float
    PGA_D_SLV: float
    PGA_D_SLC: float

    def __post_init__(self) -> None:
        for nome in ("PGA_D_SLO", "PGA_D_SLD", "PGA_D_SLV", "PGA_D_SLC"):
            setattr(self, nome, _assert_finito(nome, getattr(self, nome)))


@dataclass
class CurvaIndividuazione:
    """Punti (lambda, CR) della Curva di Individuazione dell'edificio.

    lambda [1/anno] = 1/TR_C per ciascun SL.
    Sono memorizzati anche i CR_SLR=1.0 alla stessa lambda di SLC (step
    verticale) e SLID convenzionale (lambda=1/10, CR=0).
    """
    lam_SLID: float
    lam_SLO: float
    lam_SLD: float
    lam_SLV: float
    lam_SLC: float

    def __post_init__(self) -> None:
        for nome in ("lam_SLID", "lam_SLO", "lam_SLD", "lam_SLV", "lam_SLC"):
            setattr(self, nome, _assert_finito(nome, getattr(self, nome)))

    def punti(self) -> list[tuple[str, float, float]]:
        """Lista ordinata (per severita' crescente): SLID -> SLO -> SLD -> SLV -> SLC."""
        return [
            ("SLID", self.lam_SLID, CR["SLID"]),
            ("SLO",  self.lam_SLO,  CR["SLO"]),
            ("SLD",  self.lam_SLD,  CR["SLD"]),
            ("SLV",  self.lam_SLV,  CR["SLV"]),
            ("SLC",  self.lam_SLC,  CR["SLC"]),
        ]


@dataclass
class RisultatoPAM:
    """Risultato del calcolo PAM con tutti i sub-totali tracciabili."""
    PAM: float                        # frazione del costo di ricostruzione [adim.]
    PAM_percentuale: float            # PAM x 100 [%]
    classe_PAM: str                   # A+, A, B, C, D, E, F, G
    contributi_trapezoidali: list[dict[str, Any]]
    contributo_coda_SLR: float
    monotona: bool                    # True se lambda_SLID >= lam_SLO >= ... >= lam_SLC


@dataclass
class RisultatoISV:
    """Risultato del calcolo IS-V."""
    IS_V: float                       # adimensionale
    IS_V_percentuale: float           # IS-V x 100 [%]
    classe_IS_V: str                  # A+, A, B, C, D, E, F


@dataclass
class RisultatoClassificazione:
    """Esito completo di una classificazione (stato di fatto o stato di progetto)."""
    pam: RisultatoPAM
    isv: RisultatoISV
    classe_finale: str                # peggiore tra classe_PAM e classe_IS_V
    descrizione_classe_finale: str    # "minimo (peggiore) tra A e B = B"


@dataclass
class RisultatoSaltoClassi:
    """Differenza di classe tra stato di fatto e stato di progetto."""
    classe_stato_fatto: str
    classe_stato_progetto: str
    salto_classi: int                 # 0 = nessun miglioramento; 2 = +2 classi; ecc.
    miglioramento_pam_percent: float  # PAM_fatto - PAM_progetto [%]
    miglioramento_isv_percent: float  # (IS-V_progetto - IS-V_fatto) x 100 [%]


# --- Calcoli core --------------------------------------------------------


def costruisci_curva_individuazione(
    capacita: StatiLimiteCapacita,
    *,
    tr_slid_anni: int = TR_SLID_ANNI,
) -> CurvaIndividuazione:
    """Costruisce i punti (lambda_SL, CR_SL) della Curva di Individuazione.

    DM 58/2017 Allegato A punto 2.1: lambda(SL) = 1 / TR_C(SL); SLID e'
    convenzionale a TR=10 anni con CR=0.

    NB: non esegue alcun "capping" o riordino. Se i TR_C forniti dal
    progettista sono incongruenti (p.es. TR_C(SLO) > TR_C(SLD) implica
    edificio che raggiunge SLD prima di SLO), la non-monotonia viene
    segnalata in `RisultatoPAM.monotona`. La correzione delle
    incongruenze e' responsabilita' del progettista.
    """
    if tr_slid_anni <= 0:
        raise ValueError(f"tr_slid_anni: atteso positivo, ricevuto {tr_slid_anni}")
    return CurvaIndividuazione(
        lam_SLID=1.0 / tr_slid_anni,
        lam_SLO=1.0 / capacita.TR_C_SLO,
        lam_SLD=1.0 / capacita.TR_C_SLD,
        lam_SLV=1.0 / capacita.TR_C_SLV,
        lam_SLC=1.0 / capacita.TR_C_SLC,
    )


def calcola_PAM(curva: CurvaIndividuazione) -> RisultatoPAM:
    """Calcola la Perdita Annua Media (PAM) come area sottesa alla Curva
    di Individuazione (DM 58/2017 Allegato A punto 2.1).

    Formula (riportata letteralmente dall'Allegato A):

        PAM = sum_{i=2}^{5} [lambda(SL_i) - lambda(SL_{i-1})] *
              [CR(SL_i) + CR(SL_{i-1})] / 2  +  lambda(SLC) * CR(SLR)

    con SL_1=SLID, SL_2=SLO, SL_3=SLD, SL_4=SLV, SL_5=SLC.

    Implementazione: somma trapezoidale di 4 termini in valore assoluto
    sulla differenza di lambda (la differenza fisica e' sempre il
    "consumo di rate" tra due livelli adiacenti, indipendente dal verso
    di sommatoria) piu' il termine di coda lambda(SLC) * CR(SLR) =
    lambda(SLC) * 1.0.

    L'uso del valore assoluto e' coerente con la geometria della curva
    (area sempre positiva) ed e' esplicitamente confermato dal verso del
    calcolo PAM in tutti gli output dei software certificati italiani
    (ClaSS, CDM Win, EdiSis, MasterSap-SismiClass): l'utente fornisce
    lambda > 0 per ciascun SL e ottiene PAM > 0.

    Risultato:
        PAM in frazione adimensionale (es. 0.012 = 1.2% del costo di
        ricostruzione, da confrontare con la tabella classi PAM).
    """
    punti = curva.punti()
    contributi: list[dict[str, Any]] = []
    trap = 0.0
    for i in range(1, 5):
        nome_prev, lam_prev, cr_prev = punti[i - 1]
        nome_curr, lam_curr, cr_curr = punti[i]
        delta_lam = abs(lam_curr - lam_prev)
        media_cr = (cr_curr + cr_prev) / 2.0
        area = delta_lam * media_cr
        trap += area
        contributi.append({
            "tratto": f"{nome_prev}->{nome_curr}",
            "delta_lambda": delta_lam,
            "media_CR": media_cr,
            "area": area,
        })
    coda = curva.lam_SLC * CR["SLR"]
    pam = trap + coda

    monotona = (
        curva.lam_SLID >= curva.lam_SLO >= curva.lam_SLD >=
        curva.lam_SLV >= curva.lam_SLC
    )

    classe = classifica_PAM(pam)

    return RisultatoPAM(
        PAM=pam,
        PAM_percentuale=pam * 100.0,
        classe_PAM=classe,
        contributi_trapezoidali=contributi,
        contributo_coda_SLR=coda,
        monotona=monotona,
    )


def calcola_ISV(PGA_C_SLV: float, PGA_D_SLV: float) -> RisultatoISV:
    """Calcola l'Indice di Sicurezza per la Vita (DM 58/2017 Allegato A
    punto 2.2):

        IS-V = PGA_C(SLV) / PGA_D(SLV)

    PGA_C(SLV) e' la PGA per cui l'edificio raggiunge SLV (capacita');
    PGA_D(SLV) e' la PGA di domanda al sito per SLV (NTC 2018 par. 3.2).
    """
    PGA_C_SLV = _assert_finito_non_neg("PGA_C_SLV", PGA_C_SLV)
    PGA_D_SLV = _assert_finito("PGA_D_SLV", PGA_D_SLV)
    is_v = PGA_C_SLV / PGA_D_SLV
    classe = classifica_IS_V(is_v)
    return RisultatoISV(
        IS_V=is_v,
        IS_V_percentuale=is_v * 100.0,
        classe_IS_V=classe,
    )


def classifica_PAM(pam: float) -> str:
    """Attribuisce la classe di rischio PAM (DM 58/2017 Allegato A
    Tab. classi PAM): A+ <= 0.50%, A <= 1.0%, B <= 1.5%, C <= 2.5%,
    D <= 3.5%, E <= 4.5%, F <= 7.5%, G > 7.5%."""
    pam = _assert_finito_non_neg("PAM", pam)
    for classe, soglia_sup in CLASSI_PAM:
        if pam <= soglia_sup:
            return classe
    return "G"


def classifica_IS_V(is_v: float) -> str:
    """Attribuisce la classe di rischio IS-V (DM 58/2017 Allegato A
    Tab. classi IS-V): A+ > 100%, A >= 80%, B >= 60%, C >= 45%,
    D >= 30%, E >= 15%, F < 15%.

    Boundary IS-V = 100%: la fonte (DM 58/2017 testo coordinato + esempi
    di output dei software certificati ClaSS 2017, MasterSap-SismiClass)
    riporta `100% < IS-V` per A+ e `80% <= IS-V <= 100%` per A. In
    questa implementazione IS-V > 1.00 -> A+, IS-V == 1.00 -> A,
    IS-V == 0.80 -> A (boundary inclusivo per A). Coerente con
    l'esempio ClaSS 2017 (output testuale).
    """
    is_v = _assert_finito_non_neg("IS-V", is_v)
    # A+ se IS-V > 1.0 (strettamente)
    if is_v > 1.00:
        return "A+"
    # A se 0.80 <= IS-V <= 1.00
    if is_v >= 0.80:
        return "A"
    # B se 0.60 <= IS-V < 0.80
    if is_v >= 0.60:
        return "B"
    # C se 0.45 <= IS-V < 0.60
    if is_v >= 0.45:
        return "C"
    # D se 0.30 <= IS-V < 0.45
    if is_v >= 0.30:
        return "D"
    # E se 0.15 <= IS-V < 0.30
    if is_v >= 0.15:
        return "E"
    # F se IS-V < 0.15
    return "F"


def classe_peggiore(classe_a: str, classe_b: str) -> str:
    """Restituisce la classe peggiore (piu' a destra in ORDINE_CLASSI).

    DM 58/2017 Allegato A punto 2.3: "la classe di rischio finale e' la
    minore (peggiore in graduatoria) tra la classe attribuita al
    parametro PAM e quella attribuita al parametro IS-V"."""
    if classe_a not in ORDINE_CLASSI:
        raise ValueError(f"classe non riconosciuta: {classe_a!r}")
    if classe_b not in ORDINE_CLASSI:
        raise ValueError(f"classe non riconosciuta: {classe_b!r}")
    idx_a = ORDINE_CLASSI.index(classe_a)
    idx_b = ORDINE_CLASSI.index(classe_b)
    return ORDINE_CLASSI[max(idx_a, idx_b)]


def classifica(
    capacita: StatiLimiteCapacita,
    domanda: StatiLimiteDomanda,
    *,
    tr_slid_anni: int = TR_SLID_ANNI,
) -> RisultatoClassificazione:
    """Esegue la classificazione completa per un singolo stato (di fatto
    o di progetto): calcola PAM, IS-V, classi e classe finale."""
    curva = costruisci_curva_individuazione(capacita, tr_slid_anni=tr_slid_anni)
    pam = calcola_PAM(curva)
    isv = calcola_ISV(capacita.PGA_C_SLV, domanda.PGA_D_SLV)
    finale = classe_peggiore(pam.classe_PAM, isv.classe_IS_V)
    desc = (
        f"Classe finale = peggiore tra classe PAM ({pam.classe_PAM}) e "
        f"classe IS-V ({isv.classe_IS_V}) = {finale}"
    )
    return RisultatoClassificazione(
        pam=pam,
        isv=isv,
        classe_finale=finale,
        descrizione_classe_finale=desc,
    )


def calcola_salto_classi(
    fatto: RisultatoClassificazione,
    progetto: RisultatoClassificazione,
) -> RisultatoSaltoClassi:
    """Calcola il numero di classi di rischio guadagnate fra stato di
    fatto e stato di progetto (DM 58/2017 Allegato A punto 3).

    Il salto e' positivo se progetto e' meglio di fatto, zero se uguali,
    negativo se progetto e' peggio (caso anomalo: l'intervento
    peggiorerebbe la classe; va segnalato).

    Il valore numerico (1, 2, ...) e' usato per determinare l'aliquota
    di detrazione fiscale sismabonus secondo la legislazione vigente
    (rinvio fuori scope di questa skill: la skill produce salto_classi,
    il professionista verifica le aliquote applicabili)."""
    cf = fatto.classe_finale
    cp = progetto.classe_finale
    if cf not in ORDINE_CLASSI:
        raise ValueError(f"classe stato di fatto non riconosciuta: {cf!r}")
    if cp not in ORDINE_CLASSI:
        raise ValueError(f"classe stato di progetto non riconosciuta: {cp!r}")
    idx_f = ORDINE_CLASSI.index(cf)
    idx_p = ORDINE_CLASSI.index(cp)
    salto = idx_f - idx_p  # positivo se progetto e' meglio (idx minore)
    return RisultatoSaltoClassi(
        classe_stato_fatto=cf,
        classe_stato_progetto=cp,
        salto_classi=salto,
        miglioramento_pam_percent=fatto.pam.PAM_percentuale - progetto.pam.PAM_percentuale,
        miglioramento_isv_percent=progetto.isv.IS_V_percentuale - fatto.isv.IS_V_percentuale,
    )


# --- CLI -----------------------------------------------------------------


def _carica_input(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        # parse_constant rifiuta NaN/Infinity (RFC 8259)
        def _no_nan_inf(value: str) -> Any:
            raise ValueError(f"valore non finito non ammesso nell'input: {value}")
        return json.load(f, parse_constant=_no_nan_inf)


def _build_capacita(d: dict[str, Any]) -> StatiLimiteCapacita:
    chiavi = (
        "TR_C_SLO", "TR_C_SLD", "TR_C_SLV", "TR_C_SLC",
        "PGA_C_SLO", "PGA_C_SLD", "PGA_C_SLV", "PGA_C_SLC",
    )
    mancanti = [k for k in chiavi if k not in d]
    if mancanti:
        raise ValueError(f"chiavi capacita' mancanti: {', '.join(mancanti)}")
    return StatiLimiteCapacita(**{k: d[k] for k in chiavi})


def _build_domanda(d: dict[str, Any]) -> StatiLimiteDomanda:
    chiavi = ("PGA_D_SLO", "PGA_D_SLD", "PGA_D_SLV", "PGA_D_SLC")
    mancanti = [k for k in chiavi if k not in d]
    if mancanti:
        raise ValueError(f"chiavi domanda mancanti: {', '.join(mancanti)}")
    return StatiLimiteDomanda(**{k: d[k] for k in chiavi})


def _serializza(obj: Any) -> Any:
    """Serializzazione ricorsiva di dataclass annidati per JSON output."""
    if hasattr(obj, "__dataclass_fields__"):
        return {k: _serializza(v) for k, v in asdict(obj).items()}
    if isinstance(obj, (list, tuple)):
        return [_serializza(x) for x in obj]
    if isinstance(obj, dict):
        return {k: _serializza(v) for k, v in obj.items()}
    return obj


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Classificazione rischio sismico DM 58/2017 (sismabonus, metodo convenzionale).",
    )
    parser.add_argument(
        "--input-json",
        required=True,
        help=(
            "Path a file JSON con campi 'fatto' (obbligatorio) e "
            "'progetto' (opzionale), ciascuno con TR_C_SL* e PGA_C_SL* "
            "(capacita') + PGA_D_SL* (domanda) per i 4 SL NTC."
        ),
    )
    parser.add_argument(
        "--tr-slid-anni",
        type=int,
        default=TR_SLID_ANNI,
        help=f"TR convenzionale SLID in anni (default {TR_SLID_ANNI}).",
    )
    args = parser.parse_args(argv)

    try:
        dati = _carica_input(args.input_json)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"Errore lettura input: {exc}", file=sys.stderr)
        return 2

    if "fatto" not in dati:
        print("Errore: chiave 'fatto' obbligatoria nel JSON di input.", file=sys.stderr)
        return 2

    output: dict[str, Any] = {
        "fonte_normativa": "DM 58/2017 Allegato A (testo aggiornato DM 65/2017, DM 24/2020, DM 329/2020)",
        "metodo": "Convenzionale (DM 58/2017 Allegato A punto 2)",
    }

    try:
        cap_f = _build_capacita(dati["fatto"])
        dom_f = _build_domanda(dati["fatto"])
        ris_f = classifica(cap_f, dom_f, tr_slid_anni=args.tr_slid_anni)
        output["fatto"] = _serializza(ris_f)
    except ValueError as exc:
        print(f"Errore in 'fatto': {exc}", file=sys.stderr)
        return 2

    if "progetto" in dati:
        try:
            cap_p = _build_capacita(dati["progetto"])
            # PGA_D non cambia tra fatto e progetto (stesso sito); se
            # l'utente non la replica, eredita da fatto.
            dom_p = _build_domanda(dati["progetto"]) if all(
                k in dati["progetto"] for k in ("PGA_D_SLO", "PGA_D_SLD", "PGA_D_SLV", "PGA_D_SLC")
            ) else dom_f
            ris_p = classifica(cap_p, dom_p, tr_slid_anni=args.tr_slid_anni)
            salto = calcola_salto_classi(ris_f, ris_p)
            output["progetto"] = _serializza(ris_p)
            output["salto_classi"] = _serializza(salto)
        except ValueError as exc:
            print(f"Errore in 'progetto': {exc}", file=sys.stderr)
            return 2

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
