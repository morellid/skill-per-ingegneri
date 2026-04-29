# NTC 2018 - par. 2.4 (vita nominale, classi d'uso, vita di riferimento)

> Estratto strutturato da DM 17/01/2018, Suppl. Ord. n. 8 alla GU n. 42 del 20/02/2018. Testo di pubblico dominio.
> Consultato: 2026-04-29. Hash della fonte: vedi `sources.yaml` (id: `ntc2018-dm-17-01-2018`).

## par. 2.4.1 - Vita nominale di progetto V_N

La vita nominale di progetto V_N di un'opera strutturale e' il numero di anni nel quale e' previsto che l'opera, purche' soggetta alla manutenzione ordinaria, debba poter essere usata per lo scopo al quale e' destinata.

Valori minimi (Tab. 2.4.I, riassunto):

| Tipo di costruzione | V_N minima [anni] |
|---|---|
| 1. Costruzioni temporanee e provvisorie | <= 10 |
| 2. Costruzioni con livelli di prestazione ordinari | >= 50 |
| 3. Costruzioni con livelli di prestazione elevati | >= 100 |

## par. 2.4.2 - Classi d'uso

In presenza di azioni sismiche, con riferimento alle conseguenze di una interruzione di operativita' o di un eventuale collasso, le costruzioni sono suddivise in 4 classi d'uso (sintesi):

- **Classe I**: costruzioni con presenza solo occasionale di persone, edifici agricoli.
- **Classe II**: costruzioni con normali affollamenti, senza contenuti pericolosi e senza funzioni pubbliche e sociali essenziali. Industrie con attivita' non pericolose. Ponti, opere infrastrutturali, reti viarie non ricadenti in classe d'uso III o IV, reti ferroviarie la cui interruzione non provochi situazioni di emergenza. Dighe il cui collasso non provochi conseguenze rilevanti.
- **Classe III**: costruzioni con affollamenti significativi. Industrie con attivita' pericolose per l'ambiente. Reti viarie extraurbane non ricadenti in classe d'uso IV. Ponti e reti ferroviarie la cui interruzione provochi situazioni di emergenza. Dighe rilevanti per le conseguenze di un loro eventuale collasso.
- **Classe IV**: costruzioni con funzioni pubbliche o strategiche importanti, anche con riferimento alla gestione della protezione civile in caso di calamita'. Industrie con attivita' particolarmente pericolose per l'ambiente. Reti viarie di tipo A o B di cui al D.M. 5/11/2001 n. 6792, e di tipo C quando appartenenti ad itinerari di collegamento tra capoluoghi di provincia non altresi' serviti da strade di tipo A o B. Ponti e reti ferroviarie di importanza critica per il mantenimento delle vie di comunicazione, particolarmente dopo un evento sismico. Dighe connesse al funzionamento di acquedotti e a impianti di produzione di energia elettrica.

## par. 2.4.3 - Periodo di riferimento V_R

Le azioni sismiche sulla costruzione vengono valutate in relazione ad un periodo di riferimento V_R che si ricava, per ciascun tipo di costruzione, moltiplicandone la vita nominale di progetto V_N per il coefficiente d'uso C_U:

> **V_R = V_N * C_U**     (eq. 2.4.1)

Il valore del coefficiente d'uso C_U e' definito, al variare della classe d'uso, come mostrato nella Tab. 2.4.II.

| Classe d'uso | I   | II  | III | IV  |
|--------------|-----|-----|-----|-----|
| Coeff. C_U   | 0.7 | 1.0 | 1.5 | 2.0 |

> "Se V_R risulta inferiore a 35 anni, si assume comunque V_R = 35 anni."

## Note di applicazione (rilevanti per la skill)

1. Il prodotto V_N * C_U e' la base del calcolo dei tempi di ritorno T_R nel paragrafo 3.2.1.
2. Il clamp a 35 anni e' applicato anche dal modulo Python `tasks/lib/spettro.py` nella funzione `vita_riferimento`.
3. La classificazione operativa della classe d'uso e' responsabilita' del progettista in coordinamento con il committente; la skill richiede solo il valore I/II/III/IV.
