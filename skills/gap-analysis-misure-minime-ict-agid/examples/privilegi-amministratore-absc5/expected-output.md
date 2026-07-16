# Output atteso - ABSC 5 nella gap analysis

## 1. Oggetto del gruppo (verbatim dalla fonte)

- **ABSC 5 (CSC 5): Uso appropriato dei privilegi di amministratore** - "Regole,
  processi e strumenti atti ad assicurare il corretto utilizzo delle utenze privilegiate
  e dei diritti amministrativi."
- Rilevanza: nella circolare si osserva che questa classe e' salita "dal 12° al 5° posto"
  nelle SANS 20, per la sua importanza nel prevenire la scalata dei privilegi.

## 2. Come inquadrarlo nella gap analysis

- Elenca i controlli del gruppo per **ABSC_ID** (`5.y.z`), con **descrizione**,
  **Subcategory FNSC** e le colonne **Minimo/Standard/Alto**.
- Per **ciascun** controllo registra **stato di attuazione**, **evidenze** e **azioni**
  (tipici temi: censimento e limitazione delle utenze amministrative, credenziali
  dedicate, tracciamento degli accessi privilegiati).

## 3. Determinare se un controllo e' obbligatorio

- Un controllo e' **obbligatorio** per la tua amministrazione se e' marcato **"Minimo"**
  nella tabella dell'Allegato 1: il Minimo e' la **soglia sotto cui nessuna PA puo'
  scendere**.
- I controlli marcati solo **Standard** o **Alto** sono, rispettivamente, base di
  riferimento e obiettivo: obbligatori solo se l'amministrazione adotta quel livello per
  il sottoinsieme considerato.
- **Il flag esatto** (Minimo/Standard/Alto) di ogni `ABSC_ID 5.y.z` si **legge sulla
  tabella del PDF** (Allegato 1): non va desunto.

## 4. Sintesi

- ABSC 5 = corretto uso delle utenze privilegiate; controlli valutati per ABSC_ID.
- Obbligatori = quelli con flag **Minimo**; il flag si legge sul PDF.

> La skill inquadra il gruppo e il metodo; **non sostituisce** la lettura della tabella
> ABSC nel PDF ne' l'assessment tecnico dei sistemi.
