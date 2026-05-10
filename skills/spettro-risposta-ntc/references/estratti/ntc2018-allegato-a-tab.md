# NTC 2018 - Allegato A (reticolo di riferimento e tempi di ritorno)

> Estratto strutturato da DM 17/01/2018, Suppl. Ord. n. 8 alla GU n. 42 del 20/02/2018. Testo di pubblico dominio.
> Consultato: 2026-05-11. SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
> Fonte: `references/fonti/ntc2018-dm-17-01-2018.md` (letto dal PDF, non dai training data).

## Riferimento al reticolo INGV nell'NTC 2018

*(fonte: par. 3.2 NTC 2018, p. 45 S.O. n. 8)*

Il NTC 2018 non contiene un proprio Allegato A con i dati numerici del reticolo. Al par. 3.2 (righe 4093-4095 del testo pdftotext), si legge:

> "Per i valori di ag, Fo e TC*, necessari per la determinazione delle azioni sismiche, si fa riferimento agli Allegati A e B al Decreto del
> Ministro delle Infrastrutture 14 gennaio 2008, pubblicato nel S.O. alla Gazzetta Ufficiale del 4 febbraio 2008, n.29, ed eventuali
> successivi aggiornamenti."

Pertanto il reticolo numerico (10751 nodi, 9 TR di riferimento, valori ag/F0/TC*) e' definito nell'Allegato A al DM 14/01/2008 (NTC 2008), richiamato per riferimento dalla NTC 2018.

## I 9 TR di riferimento del reticolo

La Circolare MIT n. 7/2019 (C3.2.1, p. 44 S.O. n. 5) conferma i 9 TR come limiti del reticolo disponibile. Dalla formula
TR = -VR / ln(1 - PVR) e dalla Tab. C.3.2.I della Circolare, i TR operativi si desumono come funzione di VR.

I **9 T_R di riferimento** del reticolo (in anni) sono, come consolidato nella pratica ingegneristica e nel foglio CSLP ufficiale:

> **T_R = { 30, 50, 72, 101, 140, 201, 475, 975, 2475 } anni**

Per ogni nodo del reticolo e per ciascuno T_R sono forniti tre parametri:
- **a_g** [g] - accelerazione orizzontale massima al sito su sottosuolo rigido (categoria A)
- **F_0** [adim.] - valore massimo del fattore di amplificazione spettrale
- **T_C*** [s] - periodo di inizio del tratto a velocita' costante dello spettro orizzontale di riferimento

> Servizio interattivo INGV per la consultazione: http://zonesismiche.mi.ingv.it/

## Procedura di interpolazione

L'Allegato A al DM 14/01/2008 prescrive due livelli di interpolazione:

1. **Interpolazione spaziale** (lat, lon): per un punto generico tra 4 nodi del reticolo si interpolano i 4 valori usando una media pesata sull'inverso della distanza quadratica.

2. **Interpolazione sui T_R**: per un T_R generico T* (T_R(k) <= T* <= T_R(k+1)) i parametri p (= a_g, F_0 o T_C*) si ottengono per **interpolazione log-log**:

> log(p) = log(p_k) + (log(p_{k+1}) - log(p_k)) * log(T* / T_R(k)) / log(T_R(k+1) / T_R(k))

equivalente a:

> p = p_k * (p_{k+1} / p_k) ** (log(T* / T_R(k)) / log(T_R(k+1) / T_R(k)))

*(La Circolare 7/2019 C2.4.3 richiama esplicitamente "le formule d'interpolazione fornite nell'Allegato A alle NTC".)*

## Implementazione nella skill

La skill esegue **solo** l'interpolazione (2) sui T_R: l'utente fornisce gia' i 9 valori per a_g/F_0/T_C* al sito (ricavati dal servizio INGV o dal foglio Excel CSLP, che fanno l'interpolazione spaziale fra i nodi del reticolo).

Il modulo Python `tasks/lib/spettro.py` implementa la funzione `_interpola_log` con la formula log-log mostrata sopra. Il check di range solleva errore se T* e' fuori dall'intervallo [30, 2475] anni.

Per costruzioni ordinarie i T_R di calcolo per V_N=50, classe d'uso II ricadono interamente nel reticolo:

| Stato limite | P_VR | T_R [anni] (per V_R = 50) |
|--------------|------|---------------------------|
| SLO          | 81%  | ~ 30 (formula: -50/ln(0.19) = 30.1) |
| SLD          | 63%  | ~ 50 (formula: -50/ln(0.37) = 50.3) |
| SLV          | 10%  | ~ 475 (formula: -50/ln(0.90) = 474.6) |
| SLC          | 5%   | ~ 975 (formula: -50/ln(0.95) = 974.8) |

Per V_R molto grandi (es. V_N=100, C_U=2.0 -> V_R=200) il T_R per SLC supera 2475 anni: in tal caso la skill solleva errore esplicito (estrapolazione fuori reticolo non prevista).
