# fondazioni-pali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista / geotecnico da completare)

Skill di **supporto documentale** al **progettista strutturale e geotecnico** per l'**inquadramento delle
verifiche delle fondazioni su pali** (e delle **fondazioni miste** a platea su pali) secondo le **NTC
2018** (D.M. 17 gennaio 2018), **paragrafo 6.4.3**.

**Non calcola** le resistenze, le verifiche o i coefficienti, **non dimensiona** i pali o la palificata e
**non sostituisce** il progettista o la relazione geotecnica: inquadra stati limite, approcci progettuali,
coefficienti parziali, fattori di correlazione, controlli d'integrità e prove di carico.

## Target

Ingegneri strutturisti e geotecnici e progettisti di fondazioni profonde che devono inquadrare le
verifiche agli stati limite delle fondazioni su pali secondo le NTC 2018 par. 6.4.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifiche-slu-sle-pali` | Stati limite, approcci e combinazioni per pali e fondazioni miste, con Tab. 6.4.II e Tab. 6.4.VI (§6.4.3.1-6.4.3.4) |
| `inquadra-resistenza-caratteristica-prove` | Resistenza caratteristica con i fattori di correlazione, controlli d'integrità e prove di carico (§6.4.3.1.1, 6.4.3.6, 6.4.3.7) |

Nucleo: **SLU** dei pali con **stabilità globale** in **Approccio 1 (A2+M2+R2)** e **rimanenti** in
**Approccio 2 (A1+M1+R3)**, **Tab. 6.4.II** (γR) e **Tab. 6.4.VI** (γT), **fattori di correlazione** (Tab.
6.4.III/IV/V), **SLE**, **fondazioni miste**, **controlli d'integrità** e **prove di carico** (§6.4.3).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** resistenze, verifiche o coefficienti; **non dimensiona** i pali o la palificata.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 21/1/2019 n. 7**.
- **Non tratta** il caso **sismico** (§7.11.5.3.2) né le fondazioni superficiali (§6.4.2, skill
  `capacita-portante-fondazione-ntc`) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista strutturale/geotecnico o la
relazione geotecnica, né la lettura del par. 6.4.3 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
