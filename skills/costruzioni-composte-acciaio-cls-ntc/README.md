# costruzioni-composte-acciaio-cls-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
delle costruzioni composte di acciaio-calcestruzzo** (travi con soletta collaborante, colonne composte; caso
**non sismico**) secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 4.3**: materiali e coefficienti
parziali, classificazione delle sezioni, resistenza delle sezioni composte, sistema di connessione a taglio
e colonne composte.

**Non calcola** le resistenze né **esegue** le verifiche, **non dimensiona** la sezione né la connessione e
**non sostituisce** il progettista: fornisce i coefficienti (γC/γA/γS/γV), i criteri di classificazione, i
metodi di calcolo del momento resistente e le formule dei connettori (PRd,a, PRd,c).

## Target

Ingegneri strutturisti e progettisti che devono inquadrare la progettazione (non sismica) di strutture
composte acciaio-calcestruzzo secondo le NTC 2018 par. 4.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-sezioni-composte` | Coefficienti (γC/γA/γS/γV), classificazione delle sezioni e resistenza a flessione (elastico/plastico/elasto-plastico) (§4.3.2-4.3.4.2) |
| `inquadra-connessione-taglio-composte` | Grado di connessione K e resistenza dei pioli (PRd,a/PRd,c), con riduzioni per lamiera grecata (§4.3.4.3) |

Nucleo: **coefficienti parziali** (γC = 1,5, γA = 1,05, γS = 1,15, γV = 1,25), **classificazione** delle
sezioni composte, **resistenza a flessione** (elastico/plastico/elasto-plastico), **connessione a taglio**
(pioli con testa, PRd,a/PRd,c) e **colonne composte** (§4.3).

## Relazione con altre skill

- **Completa** la famiglia "costruzioni di X" con `costruzioni-calcestruzzo-ntc` (§4.1),
  `costruzioni-acciaio-ntc` (§4.2), `costruzioni-legno-ntc` (§4.4) e `costruzioni-muratura-ntc` (§4.5). Il
  §4.3 rinvia ai §4.1 e §4.2 per quanto non specificato.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le resistenze né **esegue** le verifiche; **non dimensiona** la sezione né la connessione.
- **Non riproduce** le **Fig. 4.3.3/4.3.4** né la **Tab. 4.3.II** (figure/tabella figurata → norma/EC4) né i
  materiali dei **§11.2/11.3** né gli **Eurocodici** (UNI EN 1994).
- **Non tratta** la **progettazione sismica** (§7.6); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 4.3 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
