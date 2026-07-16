# AGENTS.md - prevenzione-incendi-attivita-procedimenti-dpr151

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale per stabilire se un'attivita' e' **soggetta ai controlli di prevenzione
incendi** e in quale **categoria (A/B/C)** dell'**Allegato I**, e per impostare i
**procedimenti** del **Comando dei Vigili del fuoco** (valutazione progetto, SCIA, controlli,
CPI, rinnovo, deroghe) secondo il **D.P.R. 1 agosto 2011, n. 151**. Target: ingegneri,
professionisti antincendio, tecnici SUAP/VV.F.

**E' una skill documentale**: inquadra ambito, categorie e procedimenti; **non riproduce la
classificazione puntuale** di ogni attivita', non redige progetto/SCIA/asseverazioni, non
riproduce le regole tecniche (DM 3/8/2015) e non sostituisce il Comando VV.F.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare a `piano-emergenza-antincendio-dm2021`
(gestione dell'emergenza, DM 2/9/2021) e ad `atex-luoghi-lavoro-dlgs81`: questa copre
l'**assoggettabilita' e i procedimenti VV.F.** del D.P.R. 151/2011.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-151-2011**: D.P.R. 1 agosto 2011, n. 151, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `a254e203...`; codice 011G0193). Articoli e Allegato I caricati via
  `caricaArticolo` e trascritti verbatim: art. 2 (attivita' soggette, categorie A/B/C), art.
  3 (valutazione progetti B/C), art. 4 (SCIA e controlli, CPI), art. 5 (rinnovo periodico),
  art. 6 (obblighi in esercizio), art. 7 (deroghe); Allegato I (intestazione + estratto).

Trascrizione in `references/fonti/dpr-151-2011.md`; estratto operativo in
`references/estratti/prevenzione-incendi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 2**: attivita' soggette nell'**Allegato I**, categorie **A/B/C** (per dimensione,
  settore, regole tecniche, pubblica incolumita').
- **Art. 3** (B e C): esame del progetto, pronuncia del Comando **entro 60 gg** (integrazioni
  entro 30 gg).
- **Art. 4**: **SCIA** prima dell'esercizio; **A/B** visite tecniche entro **60 gg** (anche a
  campione), conformazione entro **45 gg**; **C** visite tecniche entro 60 gg + **CPI entro
  15 gg**.
- **Art. 5**: rinnovo periodico **ogni 5 anni** (10 anni per le attivita' **6, 7, 8, 64, 71,
  72, 77**).
- **Art. 6**: obblighi di mantenimento in efficienza in esercizio.
- **Art. 7**: **deroga** al Comando -> Direzione regionale (parere entro 30 gg).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre la classificazione puntuale** (categoria A/B/C) di ogni attivita':
  rinviare all'Allegato I (tabella grafica, resa testuale non allineata sulle colonne).
- Non **redigere** il progetto antincendio, la SCIA ne' le asseverazioni.
- Non **riprodurre le regole tecniche** (DM 3/8/2015 - Codice di prevenzione incendi, RTV).

### Cosa fare
- Verificare assoggettabilita' e categoria (Allegato I) e impostare i procedimenti VV.F. con
  i relativi termini.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 151/2011 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere artt. 2-7 e l'Allegato I, verificando eventuali modifiche dell'elenco delle
attivita' e delle categorie.

## Validatori

- Non ancora assegnato (Livello 2 con professionista antincendio / funzionario VV.F.).

## Stato attuale

- Versione: 0.1.0-alpha (closes #251)
- Task files: 2 (`classifica-attivita-categoria.md`, `imposta-procedimento-vvf.md`)
- Esempi: 2 (autorimessa - categoria e procedimento; rinnovo quinquennale e deroga)
