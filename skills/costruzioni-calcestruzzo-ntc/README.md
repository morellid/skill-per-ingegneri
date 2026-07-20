# costruzioni-calcestruzzo-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
delle costruzioni di calcestruzzo** (c.a., c.a.p., non armato; caso **non sismico**) secondo le **NTC 2018**
(D.M. 17 gennaio 2018), **paragrafo 4.1**: classi di resistenza, resistenze di progetto e coefficienti
parziali, diagrammi di calcolo, verifiche agli stati limite ultimi e di esercizio.

**Non calcola** le resistenze né **esegue** le verifiche, **non dimensiona** né **arma** gli elementi e
**non sostituisce** il progettista: fornisce le classi (Tab. 4.1.I), i coefficienti γc/γs, le resistenze di
progetto (fcd, fctd, fyd), i diagrammi di calcolo e i criteri di verifica.

## Target

Ingegneri strutturisti e progettisti che devono inquadrare la progettazione (non sismica) di strutture in
cemento armato secondo le NTC 2018 par. 4.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-resistenze-progetto-ca` | Classi di resistenza (Tab. 4.1.I), coefficienti γc/γs e resistenze di progetto fcd/fctd/fyd con i diagrammi di calcolo (§4.1, 4.1.2.1) |
| `inquadra-verifiche-slu-sle-ca` | Verifiche SLU (pressoflessione, taglio, torsione, punzonamento) e SLE (fessurazione w1/w2/w3, limitazione tensioni) (§4.1.2.2-3) |

Nucleo: **classi di resistenza** (Tab. 4.1.I), **resistenze di progetto** fcd = αcc·fck/γc, fctd, fyd =
fyk/γs, **diagrammi di calcolo** (εc2, εcu), **verifiche SLU** (pressoflessione, taglio, torsione) e **SLE**
(fessurazione, limitazione delle tensioni) (§4.1).

## Relazione con altre skill

- **Complementare** (inquadramento documentale) al code-driven `predimensionamento-flessione-ca-ntc`
  (predimensionamento a flessione).
- Completa la famiglia "costruzioni di X" con `costruzioni-acciaio-ntc` (§4.2), `costruzioni-legno-ntc`
  (§4.4) e `costruzioni-muratura-ntc` (§4.5).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le resistenze né **esegue** le verifiche; **non dimensiona** né **arma** gli elementi.
- **Non riproduce** le proprietà dei materiali (fck, fctk, fyk, moduli) dei **§11.2/11.3** né gli
  **Eurocodici** (UNI EN 1992).
- **Non tratta** la **progettazione sismica** (§7.4) né i **calcestruzzi speciali** (leggeri §4.1.12,
  fibrorinforzati §11.2.12); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 4.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
