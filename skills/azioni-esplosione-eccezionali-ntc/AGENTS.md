# AGENTS.md - azioni-esplosione-eccezionali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle azioni eccezionali da
esplosione** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.2 (Esplosioni)**: classificazione,
modellazione (pressioni statiche equivalenti) e criteri di progettazione. Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce le categorie (Tab. 3.6.I), le pressioni equivalenti
(formule [3.6.5a]/[3.6.5b], vincolo [3.6.6], elementi chiave 20 kN/m²) e i criteri; **non calcola** le
sollecitazioni e **non dimensiona/verifica** gli elementi.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Completa la famiglia delle **azioni eccezionali** (§3.6) insieme a
`resistenza-fuoco-strutture-ntc` (§3.6.1 Incendio) e `azioni-urto-eccezionali-ntc` (§3.6.3 Urti). Condivide con
le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: il calcolo
delle sollecitazioni e le verifiche, i modelli teorici delle onde di pressione, gli studi di Categoria 3 e le
esplosioni esterne.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-3-6-2**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 3.6.2 estratto con `pdftotext -layout` (pagina GU 65) e trascritto verbatim; **gli operatori delle
  formule [3.6.5a]/[3.6.5b] sono stati verificati sull'immagine del PDF** (pdftoppm), perché pdftotext li rende
  come spazi.

Trascrizione in `references/fonti/ntc2018-par-3-6-2.md`; estratto operativo in
`references/estratti/azioni-esplosione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Classificazione** (Tab. 3.6.I): categorie 1/2/3.
- **Cat. 2** (pannelli di sfogo): pd = max fra pd = 3 + pv [3.6.5a] e pd = 3 + pv/2 + 0,04/(Av/V)² [3.6.5b];
  vincolo 0,05 m⁻¹ ≤ Av/V ≤ 0,15 m⁻¹ [3.6.6]; V ≤ 1000 m³; elementi chiave pd = 20 kN/m² da ogni direzione.
- **Cat. 1**: nessuna verifica. **Cat. 3**: studi più approfonditi.
- **Criteri** (§3.6.2.4): danni localizzati accettabili; superfici collassabili, giunti, prevenzione crolli.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le sollecitazioni né **dimensionare/verificare** gli elementi o i sistemi di protezione;
  non **scegliere** la categoria di azione al posto del progettista.
- Non **svolgere** i modelli teorici delle onde di pressione né gli studi di Categoria 3; non **trattare** le
  esplosioni esterne, l'incendio (§3.6.1) né gli urti (§3.6.3, skill dedicate).
- **ATTENZIONE agli operatori**: pdftotext perde i "+"; verificare sempre sull'immagine del PDF prima di
  scrivere le formule [3.6.5a]/[3.6.5b].

### Cosa fare
- Fornire categorie, pressioni statiche equivalenti (formule [3.6.5a]/[3.6.5b], [3.6.6], 20 kN/m²) e criteri,
  sempre con rinvio al paragrafo/tabella/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 3.6.2. Riverificare gli operatori delle formule [3.6.5a]/[3.6.5b] sull'immagine,
il vincolo [3.6.6] e il valore degli elementi chiave (20 kN/m²).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #407)
- Task files: 2 (`inquadra-classificazione-modellazione-esplosioni.md`, `inquadra-criteri-progettazione-esplosioni.md`)
- Esempi: 2 (pd in ambiente con pannelli di sfogo, pv=3/Av/V=0,10/V=500; pressione 20 kN/m² sugli elementi
  chiave)
