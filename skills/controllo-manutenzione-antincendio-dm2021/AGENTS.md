# AGENTS.md - controllo-manutenzione-antincendio-dm2021

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale a **RSPP, datore di lavoro, tecnico antincendio e manutentore** per il **controllo e la
manutenzione degli impianti, attrezzature ed altri sistemi di sicurezza antincendio** nei luoghi di lavoro, secondo il
**D.M. 1° settembre 2021** (attuativo dell'**art. 46 c. 3 lett. a) punto 3 del D.Lgs 81/2008**), in vigore dal
**25 settembre 2022**.

**È una skill documentale per il tecnico**: imposta il registro dei controlli, distingue i livelli di attività e collega
i sistemi alle norme UNI di riferimento; **non** fissa le periodicità puntuali e **non** rilascia la qualifica dei
manutentori.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Copre il **D.M. 1/9/2021** (controllo e manutenzione). È **distinta** da:
- `piano-emergenza-antincendio-dm2021` (D.M. 2/9/2021, gestione emergenza e piano di emergenza);
- `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR 151/2011, procedimenti e SCIA antincendio);
- `carico-incendio-classe-resistenza-dm` (D.M. 9/3/2007, carico d'incendio e classe di resistenza al fuoco);
- `resistenza-fuoco-strutture-ntc` (requisiti strutturali di resistenza al fuoco).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-1-9-2021-gu230**: D.M. 1° settembre 2021, GU Serie Generale n. 230 del 25/09/2021, PDF ufficiale Gazzetta
  Ufficiale, SHA256 `560643c7...` (doppio download riproducibile). Decreto e Allegati I-II estratti con
  `pdftotext -layout` (impaginazione a due colonne ricomposta a mano). Testo di legge liberamente riproducibile
  (art. 5 L. 633/1941).

Trascrizione in `references/fonti/dm-1-9-2021-controllo-manutenzione-antincendio.md`; estratto operativo in
`references/estratti/controllo-manutenzione-checklist.md`.

## Punti chiave (dal testo del decreto)

- **Tre livelli (art. 1)**: **sorveglianza** (controlli visivi, anche del lavoratore istruito), **controllo periodico**
  (verifica funzionalità con frequenza non superiore a quella indicata), **manutenzione** (mantenere in efficienza).
- **Registro dei controlli (All. I punto 1)**: predisposto dal **datore di lavoro**; annota controlli periodici e
  interventi di manutenzione; cadenze da norme/specifiche/manuale; **aggiornato e disponibile per gli organi di
  controllo**.
- **Norme UNI di riferimento (All. I, Tabella 1)**: es. estintori UNI 9994-1; reti idranti UNI 10779/EN 671-3/EN 12845;
  sprinkler UNI EN 12845; IRAI UNI 11224; EVAC UNI ISO 7240-19 o CEN/TS 54-32; evacuazione fumo e calore UNI 9494-3;
  ecc. Presunzione di conformità ma applicazione volontaria (art. 3 c.2).
- **Tecnici manutentori qualificati (art. 4 + All. II)**: manutenzione e controllo periodico eseguiti da tecnici
  qualificati (formazione + valutazione + attestazione VVF); qualifica valida su tutto il territorio nazionale. Regime
  transitorio: chi ha ≥3 anni di attività alla data di entrata in vigore è esonerato dal corso ma non dalla valutazione.
- **Entrata in vigore/abrogazioni**: in vigore dal 25/9/2022 (art. 6); abrogati art. 3 c.1 lett. e), art. 4 e allegato
  VI del D.M. 10/3/1998 (art. 5).

## Convenzioni specifiche

### Cosa NON fare
- Non **fissare le periodicità puntuali** dei controlli (es. estintori ogni 6 mesi): stanno nelle **norme UNI di
  prodotto** (Tabella 1), soggette a diritto d'autore e non trascritte. Rimanda alla UNI pertinente.
- Non **rilasciare/attestare** la qualifica del manutentore (è del Corpo nazionale dei vigili del fuoco).
- Non estendere l'obbligo di **qualifica** alla sorveglianza (che spetta al lavoratore istruito).
- Non trattare la **gestione dell'emergenza** (D.M. 2/9/2021), la **progettazione** (D.M. 3/9/2021), il **DPR 151/2011**
  né il **carico d'incendio** (D.M. 9/3/2007): rinvia alle skill/norme dedicate.
- Non inventare valori o norme: ogni elemento deve essere rintracciabile in
  `references/fonti/dm-1-9-2021-controllo-manutenzione-antincendio.md`.

### Cosa fare
- Fornire la struttura del registro dei controlli, la distinzione sorveglianza/controllo periodico/manutenzione e la
  mappatura sistema→norma UNI (Tabella 1), con rinvio all'articolo/allegato del decreto.

## Aggiornamento delle fonti

D.M. 1/9/2021: se il decreto è modificato o la Tabella 1 aggiornata, riscaricare il PDF della GU, ricalcolare l'hash con
doppio download e riestrarre; cross-checkare su Gazzetta Ufficiale/Normattiva.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico antincendio / professionista antincendio ex D.Lgs 139/2006 abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #482)
- Task files: 2 (`inquadra-registro-e-livelli-controllo.md`, `verifica-qualificazione-manutentori.md`)
- Esempi: 2 (registro dei controlli per un'attività; periodicità/norma di riferimento e verifica del manutentore)
