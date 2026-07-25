# AGENTS.md - progettazione-antincendio-basso-rischio-dm2021

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale a **RSPP, progettista antincendio e datore di lavoro** per la **progettazione, realizzazione ed
esercizio della sicurezza antincendio nei luoghi di lavoro** secondo il **D.M. 3 settembre 2021** (attuativo dell'**art.
46 c. 3 lett. a) punti 1 e 2 del D.Lgs 81/2008**), in vigore dal **29 ottobre 2022**.

**È una skill documentale per il tecnico**: inquadra applicabilità, valutazione del rischio e strategia antincendio;
**non** progetta/dimensiona le misure e **non** riproduce il Codice PI (D.M. 3/8/2015) né le norme UNI.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Copre il **D.M. 3/9/2021** (progettazione). È il **terzo** dei tre decreti
antincendio del settembre 2021; complementare e **distinta** da:
- `piano-emergenza-antincendio-dm2021` (D.M. 2/9/2021, gestione emergenza e piano di emergenza);
- `controllo-manutenzione-antincendio-dm2021` (D.M. 1/9/2021, controllo e manutenzione dei sistemi);
- `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR 151/2011, procedimenti e SCIA antincendio);
- `carico-incendio-classe-resistenza-dm` (D.M. 9/3/2007, carico d'incendio) e `resistenza-fuoco-strutture-ntc`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-3-9-2021-gu259**: D.M. 3 settembre 2021, GU Serie Generale n. 259 del 29/10/2021, PDF ufficiale Gazzetta
  Ufficiale, SHA256 `ed6c9c91...` (doppio download riproducibile). Decreto (artt. 1-5) e Allegato I estratti con
  `pdftotext -layout`; **costanti numeriche verificate a immagine** con `pdftoppm -r 150` (pdftotext perde i segni di
  disuguaglianza). Testo di legge liberamente riproducibile (art. 5 L. 633/1941).

Trascrizione in `references/fonti/dm-3-9-2021-progettazione-antincendio.md`; estratto operativo in
`references/estratti/progettazione-antincendio-checklist.md`.

## Punti chiave (dal testo del decreto)

- **Applicabilità (art. 1-3)**: luoghi di lavoro (art. 62 D.Lgs 81), esclusi i cantieri. Valutazione del rischio
  incendio **parte del DVR** (art. 2). Tre casi (art. 3): RTV → quella; **basso rischio → Allegato I**; altrimenti →
  **Codice PI D.M. 3/8/2015** (per il basso rischio è comunque ammesso il Codice PI).
- **Requisiti di basso rischio (All. I 1.2, TUTTI)**: non soggetta + no RTV; affollamento **≤ 100**; superficie **≤ 1000
  m²**; piani **-5/+24 m**; no combustibili significativi (**qf > 900 MJ/m²**); no sostanze pericolose significative; no
  lavorazioni pericolose.
- **Strategia antincendio (All. I 4)**: compartimentazione; esodo (**≥ 2 vie**, **Lcc ≤ 30/45 m**, **Les ≤ 60 m**,
  larghezze **≥ 900/800/700/600 mm**, densità **0,7 pers/m²**, porte **> 25 occ.** UNI EN 1125); GSA; controllo
  dell'incendio (estintori **≥ 13A**, **≥ 6 kg/6 l**, **max 30 m**, classe B **≥ 89 B**; idranti UNI 10779/EN 12845 liv.
  1); rivelazione/allarme (IRAI **B,D,L,C**+A, UNI 9795); controllo fumi/calore; operatività (**≤ 50 m**); impianti
  tecnologici (disattivabili).
- **Entrata in vigore/abrogazioni**: dal 29/10/2022 (art. 5); abrogato D.M. 10/3/1998 (art. 4).

## Convenzioni specifiche

### Cosa NON fare
- Non **progettare/dimensionare** le misure al posto del tecnico né firmare elaborati.
- Non applicare i parametri del minicodice a luoghi **non a basso rischio** (in tal caso Codice PI o RTV).
- Non riprodurre il **Codice PI (D.M. 3/8/2015)** né le **norme UNI** citate (diritto d'autore): rinviare ad essi.
- Non trattare la **gestione dell'emergenza** (D.M. 2/9/2021) né il **controllo/manutenzione** (D.M. 1/9/2021).
- Non inventare valori: ogni costante deve essere rintracciabile in
  `references/fonti/dm-3-9-2021-progettazione-antincendio.md` (verificata a immagine).

### Cosa fare
- Aiutare a decidere quale corpo di regole si applica e a impostare la strategia antincendio con i parametri corretti,
  citando articolo/punto dell'Allegato I.

## Aggiornamento delle fonti

D.M. 3/9/2021: se il decreto o l'Allegato I cambiano, riscaricare il PDF della GU, ricalcolare l'hash con doppio
download, riestrarre e **riverificare a immagine** le costanti; cross-checkare su Gazzetta Ufficiale.

## Validatori

- Non ancora assegnato (Livello 2 con professionista antincendio ex D.Lgs 139/2006 / RSPP abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #484)
- Task files: 2 (`inquadra-applicabilita-e-rischio.md`, `imposta-strategia-antincendio.md`)
- Esempi: 2 (verifica di applicabilità del minicodice per un ufficio; strategia esodo/estintori per un laboratorio)
