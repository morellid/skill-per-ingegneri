# verifiche-geotecniche-slu-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico da completare)

Skill di **supporto documentale** al **progettista geotecnico o strutturista** per l'**inquadramento del framework
delle verifiche geotecniche agli stati limite ultimi** — approcci progettuali e coefficienti parziali — secondo le
**NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 6.2.4** (con il valore caratteristico del **§6.2.2**).

**Non esegue** le verifiche, **non** riproduce i coefficienti di resistenza R specifici di ciascuna opera
(§6.3-6.11) e **non sostituisce** il progettista: fornisce il framework (SLU EQU/STR/GEO, Approcci 1 e 2,
combinazioni A/M/R, Tab. 6.2.I e 6.2.II).

## Target

Ingegneri geotecnici e strutturisti che devono impostare le verifiche geotecniche agli SLU (fondazioni, muri,
pendii, scavi) scegliendo l'approccio progettuale e i coefficienti parziali su azioni, parametri del terreno e
resistenze secondo le NTC 2018 par. 6.2.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-approcci-progettuali-slu` | SLU EQU/STR/GEO, approcci 1 e 2, default (A1+M1+R1)+(A2+M2+R2), coefficienti sulle azioni Tab. 6.2.I (§6.2.4.1) |
| `inquadra-coefficienti-parametri-geotecnici` | Coefficienti M1/M2 sui parametri del terreno (Tab. 6.2.II), resistenza Rd e valore caratteristico (§6.2.4.1.2, 6.2.2) |

Nucleo: il framework **Ed ≤ Rd** [6.2.1] (e **Einst,d ≤ Estb,d** per EQU), gli **Approcci 1/2** con il default
**(A1+M1+R1)+(A2+M2+R2)** (R1 unitari, R2≥1) e i coefficienti parziali su **azioni** (Tab. 6.2.I) e **parametri del
terreno** (Tab. 6.2.II: tan φ'/c' 1,25, cu 1,4 in M2).

## Relazione con altre skill

- **Framework generale** applicato in dettaglio dalle skill d'opera (§6.3-6.11), che contengono i coefficienti
  **γR** specifici: `opere-sostegno-ntc`, `capacita-portante-fondazione-ntc`, `fondazioni-pali-ntc`,
  `stabilita-pendii-naturali-ntc`, `opere-materiali-sciolti-scavi-ntc`, `opere-sotterraneo-gallerie-ntc`,
  `tiranti-ancoraggio-ntc`. Complementa `relazione-geologica-geotecnica-ntc` (§6.1-6.2, contenuti della relazione)
  e `combinazioni-carico-ntc` (framework strutturale, §2.5.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.2.2 e 6.2.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; le Tab. 6.2.I e 6.2.II verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le verifiche né calcola **Ed / Rd**, la spinta o le resistenze.
- **Non riproduce** i coefficienti **γR** (gruppi R1/R2/R3) specifici di ciascuna opera (§6.3-6.11).
- **Non tratta** in dettaglio le **verifiche SLE** geotecniche (§6.2.4.2).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturista, né la lettura dei par. 6.2.2-6.2.4 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
