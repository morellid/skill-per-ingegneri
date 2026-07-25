# AGENTS.md - fascicolo-opera-manutenzione-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **coordinatore per la sicurezza in fase di progettazione (CSP)**, al **CSE** e al
**committente** per la **predisposizione**, l'**aggiornamento** e la **verifica di completezza** del **Fascicolo con le
caratteristiche dell'opera** secondo il **D.Lgs 81/2008**, **art. 91 comma 1 lett. b)**, **art. 92** e **Allegato XVI**.

**È una skill documentale per il tecnico**: inquadra la struttura e i contenuti del fascicolo; **non** lo redige al
posto del coordinatore né progetta le misure concrete (linee vita, ganci).

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Copre il **Fascicolo dell'opera** (Allegato XVI). È **distinta** da:
- `psc-piano-sicurezza-coordinamento-dlgs81` (PSC, art. 100 + Allegato XV): il fascicolo è l'altro deliverable del CSP,
  orientato alla **sicurezza degli interventi di manutenzione successivi**;
- `pos-allegato-xv-checker` (POS, Allegato XV punto 3.2);
- `coordinatori-sicurezza-cantieri-dlgs81` (ruoli/obblighi CSP/CSE, artt. 89-92).
Condivide la fonte (Testo coordinato INL del D.Lgs 81/2008) con `pos-allegato-xv-checker` e
`psc-piano-sicurezza-coordinamento-dlgs81`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-consolidato-inl-2025-01**: Testo coordinato del D.Lgs 81/2008 — Edizione gennaio 2025 (INL), SHA256
  `f593e18...` (doppio download riproducibile, stesso file usato da `pos-allegato-xv-checker` e
  `psc-piano-sicurezza-coordinamento-dlgs81`). Artt. 91-92 e Allegato XVI estratti con `pdftotext -layout` (testo
  legale in prosa; le schede sono moduli, se ne riporta la struttura). Edizione INL non ufficiale: cross-checkare su
  Normattiva/Gazzetta Ufficiale.

Trascrizione in `references/fonti/dlgs-81-2008-art-91-92-allegato-xvi.md`; estratto operativo in
`references/estratti/fascicolo-checklist.md`.

## Punti chiave (dal testo di legge)

- **Titolarità/ciclo di vita**: il **CSP predispone** il fascicolo (art. 91 c.1 lett. b); il **CSE lo adegua** (art. 92
  c.1 lett. b); il **committente lo aggiorna** nella vita dell'opera. **Non** per la **manutenzione ordinaria** (art. 3
  c.1 lett. a DPR 380). Accompagna l'opera **per tutta la sua durata di vita**.
- **Struttura (Allegato XVI)**: Cap. I descrizione opera + soggetti (scheda I); Cap. II rischi e misure per gli
  interventi successivi (schede II-1/II-2/II-3); Cap. III documentazione di supporto (schede III-1/2/3).
- **Misure in dotazione dell'opera** (incorporate — linee vita, ganci, parapetti permanenti) vs **misure ausiliarie**
  (richieste ai datori/lavoratori autonomi dei lavori successivi — ponteggi, DPI anticaduta).
- **7 elementi**: accessi; sicurezza dei luoghi; impianti alimentazione/scarico; approvvigionamento/movimentazione
  materiali; approvvigionamento/movimentazione attrezzature; igiene; interferenze e protezione dei terzi.
- **Scheda II-3**: per ciascuna misura in dotazione, info per uso in sicurezza, controllo efficienza, manutenzione
  (verifiche, interventi, **periodicità**).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il fascicolo al posto del coordinatore né **progettare** le misure concrete (linee vita/ganci —
  norme UNI di buona tecnica); non compilare le schede.
- Non trattare il **PSC** (art. 100 + Allegato XV), il **POS** (Allegato XV punto 3.2), i **ruoli** CSP/CSE (artt.
  89-92) né la **notifica preliminare** (art. 99): rinvia alle skill/norme dedicate.
- Non inventare contenuti: ogni elemento deve essere rintracciabile in
  `references/fonti/dlgs-81-2008-art-91-92-allegato-xvi.md`.

### Cosa fare
- Fornire la struttura del fascicolo (3 capitoli, schede) e la distinzione misure in dotazione/ausiliarie con i 7
  elementi, segnalando titolarità e ciclo di vita, con rinvio all'articolo/allegato.

## Aggiornamento delle fonti

D.Lgs 81/2008: se esce una nuova edizione coordinata INL o cambia l'Allegato XVI/artt. 91-92, riscaricare il PDF,
ricalcolare l'hash con doppio download e riestrarre; cross-checkare su Normattiva.

## Validatori

- Non ancora assegnato (Livello 2 con coordinatore per la sicurezza CSP/CSE abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #480)
- Task files: 2 (`inquadra-struttura-e-schede-fascicolo.md`, `imposta-misure-per-interventi-successivi.md`)
- Esempi: 2 (struttura di un fascicolo per un edificio; misure in dotazione/ausiliarie per la manutenzione della
  copertura)
