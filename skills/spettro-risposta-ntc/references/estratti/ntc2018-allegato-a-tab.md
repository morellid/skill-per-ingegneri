# NTC 2018 - Allegato A (reticolo di riferimento e tempi di ritorno)

> Estratto strutturato da DM 17/01/2018, Allegato A "Pericolosita' sismica". Suppl. Ord. n. 8 alla GU n. 42 del 20/02/2018. Testo di pubblico dominio.
> Consultato: 2026-04-29. Hash della fonte: vedi `sources.yaml` (id: `ntc2018-dm-17-01-2018`).

## Reticolo di riferimento

L'Allegato A definisce un reticolo di riferimento di 10751 nodi distribuiti uniformemente in latitudine e longitudine sul territorio italiano (passo ~ 0.05 grad), per ciascuno dei quali sono forniti i parametri di pericolosita' sismica relativi a 9 tempi di ritorno T_R.

I **9 T_R di riferimento** del reticolo (in anni) sono:

> **T_R(k) = { 30, 50, 72, 101, 140, 201, 475, 975, 2475 } anni**

Per ogni nodo del reticolo e per ciascuno T_R(k) sono forniti tre parametri:

- **a_g** [g] - accelerazione orizzontale massima al sito su sottosuolo rigido (categoria A)
- **F_0** [adim.] - valore massimo del fattore di amplificazione spettrale
- **T_C*** [s] - periodo di inizio del tratto a velocita' costante dello spettro orizzontale di riferimento

> Servizio interattivo INGV per la consultazione: http://zonesismiche.mi.ingv.it/

## Procedura di interpolazione

L'Allegato A prescrive due livelli di interpolazione:

1. **Interpolazione spaziale** (lat, lon): per un punto generico tra 4 nodi del reticolo si interpolano i 4 valori (uno per nodo) usando una **media pesata sull'inverso della distanza**, con pesi proporzionali a 1 / d^2 (formula esplicita nell'Appendice A delle NTC; e' una "shepard's bilinear interpolation" sul reticolo regolare).

2. **Interpolazione sui T_R**: per un T_R generico T* (T_R(k) <= T* <= T_R(k+1)) i parametri p (= a_g, F_0 o T_C*) si ottengono per **interpolazione log-log**:

> log(p) = log(p_k) + (log(p_{k+1}) - log(p_k)) * log(T* / T_R(k)) / log(T_R(k+1) / T_R(k))

equivalente a:

> p = p_k * (p_{k+1} / p_k) ** (log(T* / T_R(k)) / log(T_R(k+1) / T_R(k)))

## Implementazione nella skill

La skill esegue **solo** l'interpolazione (2) sui T_R: l'utente fornisce gia' i 9 valori per a_g/F_0/T_C* al sito (ricavati dal servizio INGV o dal foglio Excel CSLP, che fanno l'interpolazione spaziale fra i nodi del reticolo).

Il modulo Python `tasks/lib/spettro.py` implementa la funzione `_interpola_log` con la formula log-log mostrata sopra. Il check di range solleva errore se T* e' fuori dall'intervallo [30, 2475] anni.

Per costruzioni ordinarie i T_R di calcolo per V_N=50, classe d'uso II ricadono interamente nel reticolo:

| Stato limite | P_VR | T_R [anni] (per V_R = 50) |
|--------------|------|---------------------------|
| SLO          | 81%  | 30.11                     |
| SLD          | 63%  | 50.29                     |
| SLV          | 10%  | 474.56                    |
| SLC          | 5%   | 974.79                    |

Per V_R molto grandi (es. V_N=100, C_U=2.0 -> V_R=200) il T_R per SLC supera 2475 anni: in tal caso la skill solleva errore esplicito (par. NTC Allegato A: estrapolazione fuori reticolo non prevista).
