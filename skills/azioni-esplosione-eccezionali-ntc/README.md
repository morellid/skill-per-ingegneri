# azioni-esplosione-eccezionali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle azioni
eccezionali da esplosione** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 3.6.2 (Esplosioni)**:
classificazione, modellazione (pressioni statiche equivalenti) e criteri di progettazione.

**Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi e **non sostituisce** il
progettista: fornisce le categorie (Tab. 3.6.I), le pressioni equivalenti (formule [3.6.5a]/[3.6.5b], vincolo
[3.6.6], elementi chiave 20 kN/m²) e i criteri.

## Target

Ingegneri strutturisti che devono definire le azioni da esplosione per la verifica di strutture in ambienti a
rischio secondo le NTC 2018 par. 3.6.2.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classificazione-modellazione-esplosioni` | Classificazione (Tab. 3.6.I) e modellazione: Cat. 2 con pannelli di sfogo (pd = max di [3.6.5a]/[3.6.5b], vincolo [3.6.6], elementi chiave 20 kN/m²) (§3.6.2.2-3.6.2.3) |
| `inquadra-criteri-progettazione-esplosioni` | Criteri di progettazione: danni localizzati accettabili, misure di protezione (superfici collassabili, giunti, prevenzione crolli) (§3.6.2.4) |

Nucleo: **classificazione** (categorie 1/2/3), **pressione statica equivalente** (Cat. 2 con pannelli di sfogo,
pd = max di [3.6.5a]/[3.6.5b], vincolo 0,05 ≤ Av/V ≤ 0,15; elementi chiave 20 kN/m²) e **criteri di
progettazione** (§3.6.2).

## Relazione con altre skill

- Completa la famiglia delle **azioni eccezionali** (§3.6) con `resistenza-fuoco-strutture-ntc` (§3.6.1) e
  `azioni-urto-eccezionali-ntc` (§3.6.3). Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim (operatori delle formule verificati sull'immagine del PDF).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non svolge** i **modelli teorici** delle onde di pressione né gli **studi di Categoria 3**; **non** tratta
  le **esplosioni esterne**.
- **Non tratta** l'**incendio** (§3.6.1, skill `resistenza-fuoco-strutture-ntc`) né gli **urti** (§3.6.3, skill
  `azioni-urto-eccezionali-ntc`).

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.6.2 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
