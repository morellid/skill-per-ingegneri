# costruzioni-legno-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento della progettazione
delle costruzioni di legno** (caso **non sismico**) secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 4.4**: classi di durata del carico e classi di servizio, resistenze di progetto con kmod e γM,
deformabilità (kdef) e stati limite di esercizio, verifiche agli stati limite ultimi (resistenza e
stabilità), collegamenti e robustezza.

**Non calcola** le resistenze né **esegue** le verifiche, **non dimensiona** elementi e collegamenti e
**non sostituisce** il progettista: fornisce le classi (Tab. 4.4.I/4.4.II), i coefficienti γM (Tab.
4.4.III), kmod (Tab. 4.4.IV) e kdef (Tab. 4.4.V), la relazione Xd = kmod·Xk/γM e i criteri di verifica.

## Target

Ingegneri strutturisti e progettisti che devono inquadrare la progettazione (non sismica) di strutture in
legno secondo le NTC 2018 par. 4.4.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-resistenze-progetto-legno` | Classi di durata (Tab. 4.4.I) e di servizio (Tab. 4.4.II), kmod (Tab. 4.4.IV) e γM (Tab. 4.4.III), resistenze di progetto Xd=kmod·Xk/γM (§4.4.4-4.4.6) |
| `inquadra-verifiche-slu-sle-legno` | Verifiche SLU di resistenza (km) e stabilità (kcrit, βc) e verifiche SLE (kdef, frecce L/300 e L/200) (§4.4.7, 4.4.8) |

Nucleo: **classi di durata** e **di servizio**, **resistenze di progetto** `Xd = kmod·Xk/γM` (γM, kmod),
**SLE** (kdef, frecce), **verifiche SLU** di resistenza (km) e di stabilità (kcrit, βc), collegamenti e
robustezza (§4.4).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le resistenze né **esegue** le verifiche; **non dimensiona** elementi e collegamenti.
- **Non riproduce** le proprietà dei materiali (fk, moduli elastici, kh) del **§11.7** né gli **Eurocodici**
  (UNI EN 1995).
- **Non tratta** la **progettazione sismica** (§7.7); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.4 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
