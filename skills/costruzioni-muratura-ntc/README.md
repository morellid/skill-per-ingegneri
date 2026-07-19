# costruzioni-muratura-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
delle costruzioni in muratura** (caso **non sismico**) secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 4.5**: materiali e categorie degli elementi, organizzazione strutturale, resistenze di progetto
e coefficienti parziali, verifiche agli stati limite e verifiche semplificate, muratura armata.

**Non calcola** le resistenze né **esegue** le verifiche, **non dimensiona** la muratura e **non
sostituisce** il progettista: fornisce la classificazione degli elementi (Tab. 4.5.I), i coefficienti γM
(Tab. 4.5.II), Φ (Tab. 4.5.III) e ρ (Tab. 4.5.IV) e i criteri di verifica.

## Target

Ingegneri strutturisti e progettisti che devono inquadrare la progettazione (non sismica) di edifici in
muratura portante secondo le NTC 2018 par. 4.5.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-resistenze-muratura` | Classificazione elementi (Tab. 4.5.I), caratteristiche meccaniche e resistenze di progetto con γM (Tab. 4.5.II) (§4.5.2, 4.5.3, 4.5.6.1) |
| `inquadra-organizzazione-verifiche-muratura` | Organizzazione strutturale, spessori e snellezza, verifiche SLU e verifiche semplificate (§4.5.4, 4.5.6.2, 4.5.6.4) |

Nucleo: **classificazione** degli elementi per foratura (Tab. 4.5.I), **categoria** I/II, **spessori
minimi** e **snellezza** (§4.5.4), **resistenze di progetto** fd/fvd e coefficiente **γM** (Tab. 4.5.II),
**verifiche SLU** con metodo semplificato (Φ, ρ, eccentricità), **verifiche semplificate** (γM = 4,2) e
**muratura armata** (§4.5.7).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.5** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le resistenze né **esegue** le verifiche; **non dimensiona** la muratura.
- **Non tratta** la **progettazione sismica** (§7.8) né la **Tab. 7.8.II**, la **resistenza al fuoco**
  (§4.5.11), il **cap. 11.10** (materiali) né gli **Eurocodici** (§4.6).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.5 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
