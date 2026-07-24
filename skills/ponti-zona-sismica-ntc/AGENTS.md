# AGENTS.md - ponti-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle regole generali** dei ponti in
zona sismica secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.9**: campo di applicazione (§7.9.1),
criteri generali di progettazione dissipativo/non dissipativo (§7.9.2), valori del fattore di comportamento
q0/νk/λ(α) e regolarità KR (§7.9.2.1), modello strutturale e requisiti dell'analisi statica lineare
(§7.9.3-7.9.4.1). Target: ingegneri strutturisti/infrastrutturali che progettano ponti a pile e travate in zona
sismica.

**È una skill documentale per il tecnico**: fornisce criteri, fattore di comportamento e requisiti dell'analisi;
**non** esegue le verifiche (duttilità/resistenza delle pile) né progetta i dettagli costruttivi.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre le **regole generali per i ponti in zona sismica** (§7.9). È **distinta**
dalle skill sui **carichi da traffico** dei ponti (`azioni-traffico-ponti-stradali-ntc` §5.1.3,
`azioni-traffico-ponti-ferroviari-ntc` §5.2.2, azioni **statiche**) e da `fattore-comportamento-q-sismica-ntc`
(§7.3.1, framework **generale** del fattore q per gli **edifici**): il §7.9 tratta la progettazione sismica
specifica dei ponti (dissipazione nelle pile, q0/νk, regolarità KR, analisi). Condivide con le altre skill NTC la
stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: le verifiche di duttilità/
resistenza, i metodi di analisi non lineare e i dettagli costruttivi (§§ 7.9.4-7.9.6).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-9**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.9 (pagine PDF 269-271) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r 150`)
  per q0, νk, λ(α), la formula [7.9.1] e KR/[7.9.2].

Trascrizione in `references/fonti/ntc2018-par-7-9.md`; estratto operativo in
`references/estratti/ponti-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.9.1**: ponti a **pile e travate** (continue/appoggiate); pile a **fusto unico**; q0 da Tab. 7.3.II.
- **§7.9.2**: non dissipativo (Cap. 4) o dissipativo (**dissipazione limitata alle pile**, inelastico flessionale,
  no rottura per taglio); pali **/1,5**, CD "B" per **10 diametri**; copriferri **0,35%**; impalcato/appoggi/
  fondazioni/spalle **elastici**.
- **§7.9.2.1**: **q0 = 1,0** (non diss.); dissipativo q0 (Tab. 7.3.II), **λ(α)=1 se α≥3 / (α/3)^0,5 se 3>α≥1**;
  c.a. **νk = NEd/(Ac·fck) ≤ 0,3**, max **0,6**, [7.9.1]; regolarità **r̃<2 → KR=1 / r̃≥2 → KR=2/r̃** [7.9.2];
  irregolari **q=1,5** (fino a **3,5** con analisi non lineare).
- **§7.9.3-7.9.4.1**: ecc. accidentale **0,03·dim. impalcato**; moti rigidi per **φ>20°** o **B/L>2,0**; statica
  lineare se massa efficace pila **≤ 1/5** massa impalcato ed eccentricità **≤ 5%**.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche di duttilità/resistenza delle pile e dei dispositivi né i metodi di analisi non
  lineare (§§ 7.9.4-7.9.6); non calcolare il q0 numerico (Tab. 7.3.II).
- Non **progettare** i dettagli costruttivi (§7.9.6); non trattare i carichi da traffico statici (§§ 5.1.3/5.2.2,
  → skill dedicate) né il framework del fattore q per gli edifici (§7.3.1, → skill dedicata).

### Cosa fare
- Fornire campo di applicazione, criteri dissipativo/non dissipativo, fattore di comportamento (q0/νk/λ(α)/KR) e
  requisiti dell'analisi, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.9. Verificare sull'immagine i valori (q0 1,0; νk 0,3/0,6; λ(α); [7.9.1]; KR 2/r̃; pali /1,5;
copriferri 0,35%; q 1,5/3,5; obliquità 20°/45°; B/L 2,0; massa 1/5; eccentricità 5%; ecc. accidentale 0,03).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di ponti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #460)
- Task files: 2 (`inquadra-criteri-fattore-comportamento.md`, `verifica-regolarita-requisiti-analisi.md`)
- Esempi: 2 (criteri e scelta di q0 per una pila in c.a.; regolarità KR e ammissibilità dell'analisi statica
  lineare)
