# Det. ACN 379907/2025 - Allegati 3 e 4 - Incidenti significativi di base

> Fonti:
> - **D.Lgs. 138/2024 art. 25 co. 4** (definizione legale di "incidente significativo")
> - **Determinazione ACN n. 379907/2025 - Allegato 3** (incidenti significativi di base per soggetti importanti)
> - **Determinazione ACN n. 379907/2025 - Allegato 4** (incidenti significativi di base per soggetti essenziali)
> - **Determinazione ACN n. 379907/2025 - Art. 6 co. 2** (soglie quantitative aggiuntive solo per operatori telco)
>
> Catalogati in `sources.yaml` come `acn-det-379907-allegato-3`, `acn-det-379907-allegato-4`, `acn-det-379907-2025`.
> Data consultazione: 2026-04-29.

## Definizione legale (art. 25 co. 4 D.Lgs. 138/2024)

Un incidente e' considerato significativo se:
- **lett. a)** ha causato o e' in grado di causare una grave perturbazione operativa dei servizi o perdite finanziarie per il soggetto interessato;
- **lett. b)** ha avuto ripercussioni o e' idoneo a provocare ripercussioni su altre persone fisiche o giuridiche causando perdite materiali o immateriali considerevoli.

Anche **uno solo** dei due criteri attiva l'obbligo di notifica al CSIRT Italia.

## Allegato 3 (soggetti importanti) - testo verbatim

> **ALLEGATO 3 - Incidenti significativi di base per i soggetti importanti**
>
> | Codice | Descrizione |
> |--------|-------------|
> | **IS-1** | Il soggetto NIS ha evidenza della perdita di riservatezza, verso l'esterno, di dati digitali di sua proprieta' o sui quali esercita il controllo, anche parziale. |
> | **IS-2** | Il soggetto NIS ha evidenza della perdita di integrita', con impatto verso l'esterno, di dati digitali di sua proprieta' o sui quali esercita il controllo, anche parziale. |
> | **IS-3** | Il soggetto NIS ha evidenza della violazione dei livelli di servizio attesi dei suoi servizi e/o delle sue attivita', sulla base dei livelli di servizio atteso (SL) stabiliti ai sensi della misura DE.CM-01. |

## Allegato 4 (soggetti essenziali) - testo verbatim

> **ALLEGATO 4 - Incidenti significativi di base per i soggetti essenziali**
>
> | Codice | Descrizione |
> |--------|-------------|
> | **IS-1** | Il soggetto NIS ha evidenza della perdita di riservatezza, verso l'esterno, di dati digitali di sua proprieta' o sui quali esercita il controllo, anche parziale. |
> | **IS-2** | Il soggetto NIS ha evidenza della perdita di integrita', con impatto verso l'esterno, di dati digitali di sua proprieta' o sui quali esercita il controllo, anche parziale. |
> | **IS-3** | Il soggetto NIS ha evidenza della violazione dei livelli di servizio attesi dei suoi servizi e/o delle sue attivita', sulla base dei livelli di servizio atteso (SL) definiti ai sensi della misura DE.CM-01. |
> | **IS-4** | Il soggetto NIS ha evidenza, anche sulla base dei parametri quali-quantitativi definiti ai sensi della misura DE.CM-01, dell'accesso, non autorizzato o con abuso dei privilegi concessi, a dati digitali di sua proprieta' o sui quali esercita il controllo, anche parziale. |

**Differenze chiave**:
- Soggetti **importanti**: 3 codici (IS-1, IS-2, IS-3).
- Soggetti **essenziali**: 4 codici (IS-1, IS-2, IS-3, IS-4 = accesso non autorizzato/abuso privilegi).

## Soglie quale-quantitative

I codici IS-3 (violazione SL) e IS-4 (accesso non autorizzato) rinviano alle soglie definite dal soggetto stesso ai sensi della misura **DE.CM-01** (monitoraggio continuo) degli Allegati 1 e 2 della determinazione. **L'ACN non fissa soglie generali quantitative** (es. ore di indisponibilita' o numero di utenti) per la generalita' dei soggetti NIS, lasciando al soggetto la calibrazione in base al proprio contesto.

Per IS-1 e IS-2 (perdita di riservatezza/integrita') la soglia e' qualitativa: l'evidenza di perdita "verso l'esterno" / "con impatto verso l'esterno". Non sono richieste soglie di volume di dati o di valore economico.

## Soglie quantitative aggiuntive per operatori telco (art. 6 co. 2)

**Solo per gli operatori telco** definiti dall'art. 1 lett. s) (>= 1% utenti nazionali OR >= 1.000.000 utenti, sui sistemi telco), nella definizione del livello di servizio atteso (SL) si considerano come incidenti significativi di base **almeno** i seguenti casi:

| Caso | Durata | % utenti nazionali colpiti |
|------|--------|------------------------------|
| a) | > 1 ora | > 15% |
| b) | > 2 ore | > 10% |
| c) | > 4 ore | > 5% |
| d) | > 6 ore | > 2% |
| e) | > 8 ore | > 1% |

Tabella verbatim dall'art. 6 co. 2 della determinazione. Si applica solo agli operatori telco sui sistemi telco; per gli altri sistemi e per gli altri soggetti NIS le soglie SLA sono definite internamente.

## Tempistiche di notifica (richiamo art. 25 D.Lgs. 138/2024)

Vedi `dlgs-138-2024-incident-art25.md` per il dettaglio. In sintesi:

| Step | Termine |
|------|---------|
| Pre-notifica | 24 ore dalla conoscenza |
| Notifica | 72 ore dalla conoscenza |
| Relazione finale | 1 mese dalla notifica |
| Comunicazione ai destinatari | Senza ingiustificato ritardo, sentito CSIRT |

**Nota**: la determinazione 379907/2025 fissa il termine di **9 mesi dalla comunicazione di inserimento** per l'avvio dell'**obbligo di notifica** (art. 3 co. 2). Prima di tale termine il soggetto non e' soggetto all'obbligo formale di notifica ex art. 25.

## Coordinamento con altre notifiche

- **GDPR**: parallelizzata, NON sostituita. Notifica al Garante entro 72h se ci sono dati personali (art. 33 GDPR).
- **PSNC** (DL 105/2019 art. 1 co. 8, come modificato dall'art. 44 D.Lgs. 138/2024): la notifica PSNC, se effettuata da un soggetto incluso nel perimetro che e' anche soggetto NIS, **assolve** anche all'obbligo NIS2 di notifica ex art. 25. La determinazione 379907/2025 introduce inoltre la categoria operativa "soggetti PSNC-NIS" e "sistemi PSNC" (art. 1 lett. o, p) per la gestione coordinata.
- **DORA** (Reg. UE 2022/2554): per le entita' DORA-eligible, la notifica DORA prevale sulla NIS2 per i settori 3 e 4 dell'Allegato I (art. 3 co. 14 D.Lgs. 138/2024).
- **eIDAS**: per i prestatori di servizi fiduciari rimangono gli obblighi del Reg. UE 910/2014 art. 19, ma in coordinamento con la notifica NIS2 (art. 25 co. 6 prevede deroga 24h sulla notifica art. 25 co. 5 lett. b).
- **Codice comunicazioni elettroniche**: per gli operatori telco, le soglie nazionali dell'art. 6 co. 2 della determinazione operano in coordinamento con il regime preesistente (DM 12/12/2018 - cfr. art. 6 co. 1 della determinazione).

## Procedura di notifica al CSIRT Italia

Canale ufficiale: piattaforma digitale dell'Agenzia per la Cybersicurezza Nazionale. Modalita' tecniche stabilite con determinazione ACN ai sensi dell'art. 25 co. 12 (procedure semplificate) e dell'art. 7 co. 6 (modalita' della piattaforma).

Per il "punto di contatto NIS" registrato in piattaforma (art. 7 co. 1 lett. c) e il suo sostituto (art. 7 co. 4 lett. d), l'organizzazione deve garantire reperibilita' continuativa per la trasmissione della pre-notifica entro 24 ore.
