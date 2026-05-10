# NTC 2018 - par. 2.4 (vita nominale, classi d'uso, vita di riferimento)

> Estratto strutturato da DM 17/01/2018, Suppl. Ord. n. 8 alla GU n. 42 del 20/02/2018. Testo di pubblico dominio.
> Consultato: 2026-05-10. SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
> Fonte: `references/fonti/ntc2018-dm-17-01-2018.md` (letto dal PDF, non dai training data).

## par. 2.4.1 - Vita nominale di progetto V_N

*(fonte: par. 2.4.1 NTC 2018, p. 36 S.O. n. 8)*

> La vita nominale di progetto VN di un'opera e' convenzionalmente definita come il numero di anni nel quale e' previsto che
> l'opera, purche' soggetta alla necessaria manutenzione, mantenga specifici livelli prestazionali.

Valori minimi (Tab. 2.4.I NTC 2018):

| Tipo di costruzione | V_N minima [anni] |
|---|---|
| 1. Costruzioni temporanee e provvisorie | <= 10 |
| 2. Costruzioni con livelli di prestazione ordinari | >= 50 |
| 3. Costruzioni con livelli di prestazione elevati | >= 100 |

## par. 2.4.2 - Classi d'uso

*(fonte: par. 2.4.2 NTC 2018, p. 36-37 S.O. n. 8)*

Con riferimento alle conseguenze di una interruzione di operativita' o di un eventuale collasso, le costruzioni sono suddivise in classi d'uso:

- **Classe I**: Costruzioni con presenza solo occasionale di persone, edifici agricoli.
- **Classe II**: Costruzioni il cui uso preveda normali affollamenti, senza contenuti pericolosi per l'ambiente e senza funzioni pubbliche e sociali essenziali. Industrie con attivita' non pericolose per l'ambiente. Ponti, opere infrastrutturali, reti viarie non ricadenti in Classe d'uso III o in Classe d'uso IV, reti ferroviarie la cui interruzione non provochi situazioni di emergenza. Dighe il cui collasso non provochi conseguenze rilevanti.
- **Classe III**: Costruzioni il cui uso preveda affollamenti significativi. Industrie con attivita' pericolose per l'ambiente. Reti viarie extraurbane non ricadenti in Classe d'uso IV. Ponti e reti ferroviarie la cui interruzione provochi situazioni di emergenza. Dighe rilevanti per le conseguenze di un loro eventuale collasso.
- **Classe IV**: Costruzioni con funzioni pubbliche o strategiche importanti, anche con riferimento alla gestione della protezione civile in caso di calamita'. Industrie con attivita' particolarmente pericolose per l'ambiente. Reti viarie di tipo A o B, di cui al DM 5/11/2001, n. 6792, e di tipo C quando appartenenti ad itinerari di collegamento tra capoluoghi di provincia non altresl' serviti da strade di tipo A o B. Ponti e reti ferroviarie di importanza critica per il mantenimento delle vie di comunicazione, particolarmente dopo un evento sismico. Dighe connesse al funzionamento di acquedotti e a impianti di produzione di energia elettrica.

## par. 2.4.3 - Periodo di riferimento V_R

*(fonte: par. 2.4.3 NTC 2018, p. 37 S.O. n. 8)*

> Le azioni sismiche sulle costruzioni vengono valutate in relazione ad un periodo di riferimento VR che si ricava, per ciascun tipo
> di costruzione, moltiplicandone la vita nominale di progetto VN per il coefficiente d'uso CU:
>
> V_R = V_N * C_U     (eq. [2.4.1] NTC 2018)

Il valore del coefficiente d'uso C_U e' definito, al variare della classe d'uso, come mostrato in Tab. 2.4.II NTC 2018:

| Classe d'uso | I   | II  | III | IV  |
|--------------|-----|-----|-----|-----|
| Coeff. C_U   | 0,7 | 1,0 | 1,5 | 2,0 |

> Per le costruzioni a servizio di attivita' a rischio di incidente rilevante si adotteranno valori di CU anche superiori a 2.

**NOTA critica - VR minimo di 35 anni**: Il testo NTC 2018 par. 2.4.3 NON contiene una clausola esplicita "se VR risulta inferiore a 35 anni, si assume VR = 35 anni" (tale formulazione era nella NTC 2008 par. 2.4). Il VR minimo di 35 anni emerge dalla Tabella C2.4.I della Circolare MIT n. 7/2019 (C2.4.3), che mostra che per VN <= 10 anni VR = 35 anni per qualsiasi classe d'uso. Il vincolo minimo e' quindi operativo ma la sua fonte esplicita e' la Circolare, non la NTC 2018.

## Note di applicazione (rilevanti per la skill)

1. Il prodotto V_N * C_U e' la base del calcolo dei tempi di ritorno T_R nel paragrafo 3.2.1.
2. Il vincolo V_R >= 35 anni e' applicato dal modulo Python `tasks/lib/spettro.py` nella funzione `vita_riferimento`, coerentemente con la Tab. C2.4.I della Circolare 7/2019 e con il limite inferiore del reticolo INGV.
3. La classificazione operativa della classe d'uso e' responsabilita' del progettista in coordinamento con il committente; la skill richiede solo il valore I/II/III/IV.
