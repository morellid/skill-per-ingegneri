# AGENTS.md - piano-emergenza-antincendio-dm2021

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**obbligo e alla struttura del piano di emergenza ed evacuazione**
nei luoghi di lavoro, ai sensi dell'**art. 46 D.Lgs 81/2008** e del **DM 2 settembre 2021**
(gestione della sicurezza antincendio in esercizio ed in emergenza). Target: datori di
lavoro, RSPP, tecnici antincendio.

**E' una skill documentale**: inquadra obbligo, soglie e struttura; **non esegue la
valutazione del rischio incendio**, non riproduce integralmente gli allegati e non
certifica il piano.

## Area di catalogo

`sicurezza-lavoro-cantieri`. Complementare a `dvr-generico` (le misure di emergenza, se il
piano non e' obbligatorio, confluiscono nel DVR) e alle skill impiantistiche antincendio.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-art46**: D.Lgs. 81/2008 art. 46, indice Normattiva pinnato `!vig=2026-07-16`
  (hash d8991985...; codice 008G0104), articolo via caricaArticolo.
- **dm-2-9-2021**: DM 2/9/2021, pagina ELI di Gazzetta Ufficiale (riferimento solo-online,
  `sha256: null`, `binary_path: null`; codice 21A05748, GU SG n. 237 del 4/10/2021). Artt.
  1-8 letti via caricaArticolo e trascritti verbatim.

Trascrizioni in `references/fonti/piano-emergenza.md`; estratto in
`references/estratti/piano-emergenza-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 46 D.Lgs 81/2008**: prevenzione incendi (c.1-2), delega ai decreti per i criteri
  di gestione emergenze e per il servizio antincendio (c.3), regime transitorio DM 10/3/1998
  (c.4).
- **DM 2/9/2021 art. 2 c.2**: il piano di emergenza e' obbligatorio se: **>= 10 lavoratori**;
  **oppure** luogo aperto al pubblico con **> 50 persone** contemporanee; **oppure** attivita'
  dell'Allegato I DPR 151/2011. (Condizioni **alternative**.)
- **Art. 2 c.4**: sotto soglia, niente piano ma misure di emergenza nel DVR (o procedure
  standardizzate art. 29 c.5).
- **Art. 2 c.3**: contenuti del piano (misure di emergenza + nominativi addetti).
- **Artt. 4-5**: designazione addetti (all'esito della valutazione del rischio incendio) e
  loro formazione/aggiornamento (allegato III).
- **Art. 7-8**: transitorie (sostituisce DM 10/3/1998), entrata in vigore 4/10/2022.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire la valutazione del rischio incendio** (presupposto).
- Non **riprodurre integralmente** gli allegati I-II-III del D.M.
- Non **certificare** il piano ne' sostituire il progetto antincendio (DM 3/9/2021) o le
  pratiche VV.F. (DPR 151/2011).

### Cosa fare
- Determinare l'obbligo del piano (soglie art. 2 c.2) o le misure nel DVR (c.4); impostare
  contenuti del piano e designazione/formazione addetti (artt. 2 c.3, 4, 5).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 46. GU: rileggere il DM 2/9/2021 (codice 21A05748) via caricaArticolo;
verificare eventuali modifiche/allegati.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico antincendio / RSPP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #242)
- Task files: 2 (`determina-obbligo-piano.md`, `struttura-piano-e-addetti.md`)
- Esempi: 2 (ufficio 8 dipendenti - non obbligatorio; negozio al pubblico > 50 persone -
  obbligatorio nonostante < 10 lavoratori)
