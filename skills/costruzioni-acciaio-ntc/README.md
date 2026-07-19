# costruzioni-acciaio-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
delle costruzioni di acciaio** (caso **non sismico**) secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 4.2**: materiali, classificazione delle sezioni, coefficienti parziali, resistenze di progetto
e verifiche agli stati limite ultimi (resistenza e stabilità delle membrature).

**Non calcola** le resistenze né **esegue** le verifiche, **non dimensiona** membrature e collegamenti e
**non sostituisce** il progettista: fornisce i materiali (S235-S460, Tab. 4.2.I/II), le classi di sezione
(1-4), i coefficienti γM (Tab. 4.2.VII), la relazione Rd = Rk/γM e i criteri di verifica.

## Target

Ingegneri strutturisti e progettisti che devono inquadrare la progettazione (non sismica) di strutture in
acciaio secondo le NTC 2018 par. 4.2.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classe-sezione-resistenze-acciaio` | Materiali (S235-S460, Tab. 4.2.I/II), classe di sezione (1-4), γM (Tab. 4.2.VII) e resistenze di progetto SLU (§4.2.1, 4.2.3.1, 4.2.4.1) |
| `inquadra-stabilita-analisi-acciaio` | Metodo di analisi (α_cr) e verifiche di stabilità delle membrature (Nb,Rd, χ, λ̄, svergolamento) (§4.2.3, 4.2.4.1.3) |

Nucleo: **materiali** (gradi, fyk/ftk), **classi di sezione** (1-4), **coefficienti γM** (Tab. 4.2.VII),
**resistenze di progetto** SLU (trazione, compressione, flessione, taglio) e **verifiche di stabilità**
(aste compresse e travi inflesse) (§4.2).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.2** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le resistenze né **esegue** le verifiche; **non dimensiona** membrature e collegamenti.
- **Non riproduce** le **Tab. 4.2.III-V** (b/t) né la **Tab. 4.2.VIII** (curve di instabilità), che nel PDF
  sono figure: vanno lette sulla norma o su **UNI EN 1993** (EC3).
- **Non riproduce** i materiali del **§11.3.4** né gli Eurocodici; **non tratta** la **progettazione
  sismica** (§7.5); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.2 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
