# AGENTS.md - contabilizzazione-calore-dlgs102

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento degli obblighi di **contabilizzazione del
calore** e di **ripartizione delle spese** negli edifici/condomini con impianto
centralizzato o teleriscaldamento, secondo il **D.Lgs. 102/2014, art. 9, comma 5** (e
commi 5-bis/5-ter/5-quater). Target: ingegneri/termotecnici e amministratori di
condominio.

**È una skill documentale**: inquadra obblighi e criteri; **non calcola** i millesimi
termici né le quote (UNI 10200/EN 15459), **non redige** la relazione tecnica o la
tabella di ripartizione, non sostituisce il progettista/termotecnico o l'amministratore.

## Nota sull'area

Area **energia-incentivi**. Complementare a `diagnosi-energetica-dlgs102` (art. 8, stesso
decreto) e alle skill sugli impianti termici (DPR 74/2013): questa copre la
**contabilizzazione del calore** e la **ripartizione delle spese** (art. 9 c. 5).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-102-2014-art-9**: D.Lgs. 102/2014, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `a98de115...`; codice 14G00113). Art. 9 versione 8, idGruppo
  2, flagTipoArticolo 0, caricato via `caricaArticolo` e trascritto verbatim.

Trascrizione in `references/fonti/dlgs-102-2014-art-9.md`; estratto operativo in
`references/estratti/contabilizzazione-calore-checklist.md`.

## Punti chiave (verificati sul testo)

- **c. 5 lett. a**: contatore di fornitura allo scambiatore/punto di fornitura
  dell'edificio (obbligo dal 30/6/2017, a cura degli esercenti l'attivita' di misura).
- **c. 5 lett. b**: sotto-contatori per unita' immobiliare (a cura del proprietario) ove
  tecnicamente possibile ed efficiente in termini di costi (UNI EN 15459); esenzioni in
  relazione tecnica del progettista/tecnico abilitato.
- **c. 5 lett. c**: in alternativa, sistemi di termoregolazione e contabilizzazione
  individuali (ripartitori) per corpo scaldante, salvo inefficienza (UNI EN 15459).
- **c. 5 lett. d**: ripartizione con **quota >= 50%** ai prelievi volontari; quota
  residua per millesimi/mq/mc/potenze (UNI 10200); prima stagione ai soli millesimi;
  facoltativa per edifici gia' provvisti.
- **c. 5-bis**: lettura da remoto (dispositivi post 25/10/2020; tutti entro 1/1/2027).
- **c. 5-ter**: nessuna deroga alle lett. b)/c) per le nuove costruzioni.
- **c. 5-quater**: guida ENEA per differenze di fabbisogno per mq > 50%.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** millesimi termici, quote o efficienza in termini di costi (UNI
  10200, UNI EN 15459).
- Non **inventare** soglie: usare **>= 50%** ai prelievi volontari e le date (30/6/2017,
  1/1/2027) come da testo.
- Non **redigere** la relazione tecnica o la tabella di ripartizione.

### Cosa fare
- **Individuare** gli obblighi (contatore/sotto-contatori/ripartitori) e i presupposti
  di esenzione, e **impostare** lo schema di ripartizione, con rinvio al termotecnico e
  all'amministratore.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 102/2014 pinnato a nuovo `!vig=` (nuovo
hash) e rileggere l'art. 9 (testo tra `(( ))` = modifiche successive). Le norme tecniche
UNI 10200 e UNI EN 15459 sono citate, non riprodotte (a pagamento).

## Validatori

- Non ancora assegnato (Livello 2 con termotecnico / amministratore di condominio).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`verifica-obbligo-contabilizzazione.md`, `imposta-ripartizione-spese.md`)
- Esempi: 2 (obbligo ed esenzione con ripartitori - art. 9 c. 5 a-c; ripartizione spese quota >= 50% - art. 9 c. 5 d)
