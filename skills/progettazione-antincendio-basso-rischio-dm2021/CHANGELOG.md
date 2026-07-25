# CHANGELOG - progettazione-antincendio-basso-rischio-dm2021

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #484)
- Prima versione della skill di supporto documentale per la **progettazione, realizzazione ed esercizio della sicurezza
  antincendio nei luoghi di lavoro** secondo il **D.M. 3 settembre 2021** (attuativo dell'**art. 46 c. 3 lett. a) punti
  1 e 2 del D.Lgs 81/2008**), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.M. 3 settembre 2021** — GU Serie Generale n. 259 del 29/10/2021 — SHA256
    ed6c9c91b8340150535b690a53390114f17289c8a5255c8a2e22501f3b3027ec (doppio download riproducibile).
  - Decreto (artt. 1-5) e Allegato I estratti con `pdftotext -layout`; **costanti numeriche verificate a immagine** con
    `pdftoppm -r 150` (pdftotext perde i segni di disuguaglianza), pagine PDF 14/17/18/20 (GU pp. 10/13/14/16),
    trascritti in `references/fonti/dm-3-9-2021-progettazione-antincendio.md`.
- Estratto operativo `references/estratti/progettazione-antincendio-checklist.md`.
- Due task: `inquadra-applicabilita-e-rischio.md` e `imposta-strategia-antincendio.md`.
- Due esempi: verifica di applicabilità del minicodice per un ufficio; strategia esodo/estintori per un laboratorio.

### Contenuto ancorato al testo
- Applicabilità (artt. 1-3): luoghi di lavoro art. 62 D.Lgs 81 esclusi i cantieri; valutazione del rischio incendio
  parte specifica del DVR (art. 2 + art. 17); tre casi (art. 3): RTV applicabile; luoghi a basso rischio → Allegato I
  (minicodice); altrimenti Codice PI D.M. 3/8/2015 (per il basso rischio ammesso anche il Codice PI). Requisiti di
  basso rischio (All. I 1.2): attività non soggetta (non in Allegato I DPR 151/2011) e senza RTV, con affollamento ≤ 100
  occupanti, superficie lorda ≤ 1000 m², piani tra -5 e 24 m, assenza di materiali combustibili significativi (qf > 900
  MJ/m²), sostanze/miscele pericolose e lavorazioni pericolose significative. Strategia antincendio (All. I 4):
  compartimentazione; esodo (densità 0,7 persone/m², ≥ 2 vie indipendenti, corridoio cieco Lcc ≤ 30 m o ≤ 45 m con IRAI
  A,B,D,L,C o altezza media ≥ 5 m, Les ≤ 60 m, altezza vie 2 m, larghezza percorso ≥ 900 mm con varchi ≥ 800/700/600 mm,
  porte per > 25 occupanti nel senso esodo + UNI EN 1125); GSA; controllo dell'incendio (estintori ≥ 13A, ≥ 6 kg/6 litri,
  distanza max 30 m, classe B ≥ 89 B, rete idranti UNI 10779/EN 12845 livello 1); rivelazione e allarme (IRAI funzioni
  B/D/L/C + A, UNI 9795); controllo fumi e calore; operatività antincendio (mezzi soccorso ≤ 50 m); sicurezza impianti
  tecnologici (disattivabili). Entrata in vigore 29/10/2022 (art. 5); abrogato D.M. 10/3/1998 (art. 4).

### Scope e limiti
- Non progetta/dimensiona le misure al posto del tecnico né firma elaborati; non riproduce il Codice PI (D.M. 3/8/2015)
  né le norme UNI citate (diritto d'autore). Non è la gestione dell'emergenza (D.M. 2/9/2021) né il controllo/
  manutenzione dei sistemi (D.M. 1/9/2021).

### Note di sviluppo
- Terzo dei tre decreti antincendio del settembre 2021; distinta da `piano-emergenza-antincendio-dm2021` (D.M. 2/9),
  `controllo-manutenzione-antincendio-dm2021` (D.M. 1/9), `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR
  151/2011) e `carico-incendio-classe-resistenza-dm` (D.M. 9/3/2007). Validazione Livello 2 con professionista
  antincendio / RSPP abilitato.
