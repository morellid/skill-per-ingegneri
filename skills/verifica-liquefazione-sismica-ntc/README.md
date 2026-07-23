# verifica-liquefazione-sismica-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico da completare)

Skill di **supporto documentale** al **progettista geotecnico / strutturale** per l'**inquadramento della
verifica di stabilità del sito nei confronti della liquefazione** in condizioni sismiche secondo le **NTC
2018** (D.M. 17 gennaio 2018), **paragrafo 7.11.3.4**: generalità/definizione, condizioni di esclusione della
verifica e metodi di analisi (coefficiente di sicurezza).

**Non calcola** il coefficiente di sicurezza (CRR/CSR: metodi storico-empirici da letteratura e prove) né
**progetta** gli interventi di consolidamento e **non sostituisce** il progettista: fornisce la definizione
del fenomeno, le quattro condizioni di esclusione e la struttura della verifica. È **distinta** dalle skill
sulla stabilità dei pendii (§6.3) e sulle verifiche geotecniche SLU (§6.2.4).

## Target

Ingegneri geotecnici e strutturisti che, nella relazione geotecnica per un sito sismico, devono stabilire se
la verifica a liquefazione è necessaria e come impostarla secondo le NTC 2018 par. 7.11.3.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `valuta-esclusione-verifica-liquefazione` | Verifica se ricorre almeno una delle 4 condizioni di esclusione (§7.11.3.4.2), con definizione e conseguenze (§7.11.3.4.1) |
| `inquadra-metodo-coefficiente-sicurezza` | Inquadra i metodi di analisi quando nessuna condizione è soddisfatta: coefficiente di sicurezza = resistenza/sollecitazione (§7.11.3.4.3) |

Nucleo: **definizione** della liquefazione, **condizioni di esclusione** (a_max < 0,1 g; falda > 15 m;
(N₁)₆₀ > 30 o q_c1N > 180 a 100 kPa; granulometria fuori Fig. 7.11.1) e **coefficiente di sicurezza** = resistenza
disponibile / sollecitazione indotta dal terremoto di progetto (§7.11.3.4).

## Relazione con altre skill

- Copre la **verifica alla liquefazione** (§7.11.3.4). È **distinta** da `stabilita-pendii-naturali-ntc`
  (§6.3) e `verifiche-geotecniche-slu-ntc` (§6.2.4); si appoggia a `categorie-sottosuolo-topografiche-ntc`
  (§3.2.2) e `spettro-risposta-ntc` (§3.2.3) per l'azione sismica. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.11.3.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 284-285.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** il coefficiente di sicurezza alla liquefazione (rapporti **CRR/CSR**, correlazioni con
  **(N₁)₆₀ / q_c1N**, magnitudo): metodi di letteratura e prove, non nelle NTC.
- **Non progetta** gli **interventi di consolidamento** né le fondazioni profonde; non valuta la riduzione di
  capacità portante o gli incrementi nei pali.
- **Non tratta** la **stabilità dei pendii** sismica (§7.11.3.5) o statica (§6.3), né l'azione sismica di
  dettaglio (§3.2.3) e le categorie di sottosuolo (§3.2.2).

**La skill è un supporto documentale: non sostituisce il progettista geotecnico né la lettura del par. 7.11.3.4 delle NTC 2018 e delle metodologie di verifica alla liquefazione adottate.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
