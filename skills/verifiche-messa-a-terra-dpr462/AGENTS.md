# AGENTS.md - verifiche-messa-a-terra-dpr462

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli adempimenti del **DPR 462/2001**: denuncia e verifiche
(a campione, prima verifica, periodiche) degli impianti elettrici di messa a
terra, dei dispositivi contro le scariche atmosferiche e degli impianti in
luoghi con pericolo di esplosione, **nei luoghi di lavoro**. Target: datori di
lavoro, periti/ingegneri elettrotecnici, RSPP, consulenti sicurezza, installatori.

**E' una skill documentale**: non definisce regole tecniche di impianto (CEI),
non calcola, non fornisce tariffe, non calcola le date delle scadenze.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-462-2001**: D.P.R. 22/10/2001 n. 462, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile 08a5a8c...,
  pattern della skill aua-dpr59-dossier). Articoli 1-10 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dpr-462-2001.md`.

Estratto operativo: `references/estratti/verifiche-messa-a-terra-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 1): tre impianti nei luoghi di lavoro (messa a terra;
  scariche atmosferiche; luoghi con pericolo di esplosione). Obbligato: il datore
  di lavoro.
- **Periodicita' verifiche periodiche**: **5 anni** (messa a terra/scariche
  ordinari, art. 4 c. 1); **2 anni** per cantieri, locali ad uso medico, ambienti
  a maggior rischio in caso di incendio (art. 4 c. 1) e per luoghi con pericolo di
  esplosione (art. 6 c. 1).
- **Messa in esercizio** (art. 2/5): dichiarazione di conformita' dell'installatore
  (= omologazione per messa a terra/scariche); denuncia **entro 30 giorni** a
  **INAIL e ASL/ARPA** (art. 2) o ad **ASL/ARPA** (art. 5); prima verifica a
  campione INAIL (art. 3) o omologazione ASL/ARPA (art. 5 c. 4).
- **Soggetti verificatori** (art. 4 c. 2 / art. 6 c. 2): ASL/ARPA o organismi
  abilitati (MISE/MIMIT), criteri UNI CEI; rilascio di **verbale** da conservare.
- **Art. 7-bis** (dal 1-3-2020): banca dati INAIL; comunicazione del nominativo
  dell'organismo all'INAIL; quota 5% della tariffa; tariffe decreto ISPESL 7/7/2005.
- **Variazioni** (art. 8): cessazione, modifiche sostanziali, trasferimento -> a
  INAIL e ASL/ARPA.
- **Nota storica**: ISPESL confluito nell'INAIL (DL 78/2010).

## Convenzioni specifiche

### Cosa NON fare
- Non definire regole tecniche di impianto (CEI 64-8, CEI EN 62305, ATEX) ne'
  calcolare parametri: il DPR rinvia alle norme UNI CEI (non riprodotte).
- Non fornire importi di tariffe (decreto ISPESL 7/7/2005, non trascritto).
- Non confondere i due binari: messa a terra/scariche (artt. 2-4, prima verifica
  INAIL a campione) vs luoghi con pericolo di esplosione (artt. 5-6, omologazione
  ASL/ARPA).
- Non applicare la periodicita' quinquennale senza controllare le eccezioni
  biennali (cantieri, locali medici, rischio incendio, esplosione).
- Non calcolare le date concrete delle scadenze al posto dell'utente.
- Non citare "ISPESL" senza precisare che oggi le funzioni sono dell'INAIL.

### Cosa fare
- Citare l'articolo preciso (art. 1-8, 7-bis) per ogni obbligo/periodicita'.
- Applicare la regola di decisione della periodicita' con la condizione che la
  determina.
- Ricordare la comunicazione INAIL (art. 7-bis) e le comunicazioni di variazione
  (art. 8).
- Chiudere con il rinvio agli obblighi del datore di lavoro e ai soggetti
  competenti.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati (l'art. 7-bis e' in vigore dal 1-3-2020).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con perito elettrotecnico / RSPP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #59)
- Task files: 2 (`diagnosi-adempimenti.md`, `checklist-adempimenti.md`)
- Esempi: 2 (messa a terra in ambiente a maggior rischio incendio -> biennale;
  impianto in luogo con pericolo di esplosione -> artt. 5-6)
