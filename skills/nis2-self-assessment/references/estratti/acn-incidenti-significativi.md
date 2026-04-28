# Det. ACN - Incidenti significativi di base (D.Lgs. 138/2024 art. 25 + ACN)

> Fonti combinate:
> - D.Lgs. 138/2024 art. 25 co. 4 (definizione legale di "incidente significativo").
> - Determinazione ACN n. 164179/2025 e successiva Determinazione ACN n. 379907/2025 (in vigore dal 15/01/2026): definizioni operative degli "incidenti significativi di base" per soggetti importanti (Allegato 3) ed essenziali (Allegato 4).
> - Catalogate in `sources.yaml` come `acn-det-164179-2025`.
> Data consultazione: 2026-04-29.
>
> **Avvertenza**: gli elenchi degli "incidenti significativi di base" e le soglie quantitative sono pubblicati negli allegati 3 (importanti) e 4 (essenziali) della determinazione ACN. Questo file fornisce la struttura concettuale + la definizione legale di art. 25 co. 4. Per i valori numerici puntuali e l'elenco settoriale completo dei trigger di notifica, fare riferimento agli allegati ufficiali ACN.

## Definizione legale (art. 25 co. 4 D.Lgs. 138/2024)

Un incidente e' considerato significativo se:
- **lett. a)** ha causato o e' in grado di causare una grave perturbazione operativa dei servizi o perdite finanziarie per il soggetto interessato;
- **lett. b)** ha avuto ripercussioni o e' idoneo a provocare ripercussioni su altre persone fisiche o giuridiche causando perdite materiali o immateriali considerevoli.

Anche **uno solo** dei due criteri attiva l'obbligo di notifica.

## Categorie tipiche di incidente significativo (per ambito ACN)

La Determinazione ACN definisce le **soglie quantitative** che identificano un incidente come "significativo di base". Le categorie tipiche includono:

### A. Indisponibilita' del servizio
- Indisponibilita' totale o parziale di un servizio rilevante per un periodo che supera una soglia di durata (es. > 1h per servizi critici, > N ore per altri).
- Numero di destinatari del servizio coinvolti che supera una soglia (es. > 10.000 utenti, > 1% del bacino di utenza).

### B. Compromissione confidenzialita' / integrita'
- Esfiltrazione o accesso non autorizzato a dati con caratteristiche di criticita' (es. dati personali su scala, segreti industriali, credenziali privilegiate).
- Modifica non autorizzata di dati che incide sul servizio.

### C. Compromissione di account/identita'
- Compromissione di un numero di account utente o privilegiati superiore a soglia.
- Compromissione di account amministrativi o di servizio critici.

### D. Compromissione di asset critici
- Compromissione di un asset rilevante (server di produzione, database principale, controller di dominio).
- Compromissione di sistemi di controllo industriale (ICS/OT) per soggetti dei settori energia, acqua, trasporti, sanita'.

### E. Cifratura malevola (ransomware)
- Cifratura di dati su sistemi rilevanti, anche parziale.

### F. Impatto economico
- Perdite finanziarie dirette o indirette superiori a una soglia (es. > 500.000 EUR o > X% del fatturato).

### G. Impatto su persone
- Conseguenze su salute, sicurezza fisica o diritti fondamentali di persone (settori sanita', trasporti, sicurezza pubblica).

### H. Impatto transfrontaliero
- Servizi forniti in piu' Stati membri UE coinvolti.

## Differenza essenziali vs importanti

Le soglie sono **piu' basse per i soggetti essenziali** (notifica scatta prima) e **piu' alte per gli importanti**. Per esempio (illustrativo, non verbatim):

| Tipo trigger | Soggetto importante | Soggetto essenziale |
|--------------|---------------------|----------------------|
| Indisponibilita' servizio | > 4 ore | > 1 ora |
| Numero utenti coinvolti | > 5% bacino | > 1% bacino |
| Perdita finanziaria | > 1M EUR | > 500.000 EUR |

I valori esatti sono nella determinazione ACN (allegati 3 e 4 della Det. 379907/2025).

## Tempistiche di notifica (richiamo art. 25)

Vedi `dlgs-138-2024-incident-art25.md` per il dettaglio. In sintesi:

| Step | Termine |
|------|---------|
| Pre-notifica | 24 ore dalla conoscenza |
| Notifica | 72 ore dalla conoscenza |
| Relazione finale | 1 mese dalla notifica |
| Comunicazione ai destinatari | Senza ingiustificato ritardo, sentito CSIRT |

## Coordinamento con altre notifiche

- **GDPR**: parallelizzata, NON sostituita. Notifica al Garante entro 72h se ci sono dati personali (art. 33 GDPR).
- **PSNC** (DL 105/2019): la notifica PSNC, se effettuata da un soggetto anche NIS, **assolve** anche all'obbligo NIS2 (art. 1 co. 8 DL 105/2019, come modificato dall'art. 44 D.Lgs. 138/2024).
- **DORA**: per le entita' DORA-eligible, la notifica DORA prevale sulla NIS2 per i settori 3 e 4 dell'Allegato I.
- **eIDAS**: per i prestatori di servizi fiduciari rimangono gli obblighi del Reg. UE 910/2014 art. 19, ma in coordinamento con la notifica NIS2 (art. 25 co. 6 prevede deroga 24h).

## Procedura di notifica al CSIRT Italia

Canale ufficiale: piattaforma digitale dell'Agenzia per la Cybersicurezza Nazionale. Modalita' tecniche stabilite con determinazione ACN ai sensi dell'art. 25 co. 12 (procedure semplificate) e dell'art. 7 co. 6 (modalita' della piattaforma).

Per il "punto di contatto NIS" registrato in piattaforma (art. 7 co. 1 lett. c) e il suo sostituto (art. 7 co. 4 lett. d), l'organizzazione deve garantire reperibilita' continuativa per la trasmissione della pre-notifica entro 24 ore.
