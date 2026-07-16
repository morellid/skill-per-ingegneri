# AGENTS.md - esercizio-controllo-impianti-termici-dpr74

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale ai criteri di **esercizio, conduzione, controllo e manutenzione** degli
**impianti termici** per la climatizzazione (invernale ed estiva), secondo il **D.P.R. 16 aprile
2013, n. 74** (attuativo del D.Lgs. 192/2005): temperature massime, limiti di esercizio per zona
climatica, responsabile/terzo responsabile, controllo/manutenzione, controllo di efficienza
energetica (RCEE). Target: ingegneri termotecnici, responsabili di impianto, ditte di
manutenzione, amministratori di condominio.

**E' una skill documentale**: inquadra criteri e adempimenti; **non riproduce i modelli RCEE**
(Allegato A) ne' il libretto di impianto (DM 10/2/2014), non esegue controllo/manutenzione e non
sostituisce il manutentore abilitato ne' l'ispezione dell'autorita' competente.

## Nota sull'area e sulla complementarita'

Area **energia-incentivi** (efficienza energetica, attuativo del D.Lgs. 192/2005). Complementare
a `trasmittanza-termica-opache-dm2015` (involucro opaco) e `diagnosi-energetica-dlgs102`
(diagnosi energetica delle imprese): questa copre l'**esercizio/manutenzione** degli impianti
termici.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-74-2013**: D.P.R. 16 aprile 2013, n. 74, indice Normattiva pinnato `!vig=2026-07-16`
  (hash `13aa0ad0...`, codice 13G00114). Artt. 3-8 via `caricaArticolo`, trascritti verbatim.

Trascrizione in `references/fonti/dpr-74-2013.md`; estratto in
`references/estratti/impianti-termici-checklist.md`.

## Punti chiave (verificati sul testo)

- **Temperature** (art. 3): invernale **18C+2** (industriale/artigianale) / **20C+2** (altri);
  estiva **>= 26C-2**.
- **Limiti di esercizio** (art. 4): zone A-F (ore/g e periodi); deroghe con **ordinanza del
  sindaco** (art. 5).
- **Responsabili** (art. 6): responsabile dell'impianto e terzo responsabile; delega NON ammessa
  per unita' residenziali singole senza locale tecnico dedicato; impianti non conformi solo con
  incarico di messa a norma.
- **Controllo/manutenzione** (art. 7): ditte abilitate **DM 37/2008**, periodicita' delle
  istruzioni installatore/fabbricante.
- **Efficienza energetica** (art. 8): impianti invernali **> 10 kW** / estivi **> 12 kW**; **RCEE**
  (Allegato A); casi (prima messa in esercizio, sostituzione generatore).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre i campi dei modelli RCEE** (Allegato A) ne' il **libretto di impianto** (DM
  10/2/2014): rinviare agli atti. Non inventare la periodicita' puntuale dei controlli.
- Non **eseguire** controllo/manutenzione ne' redigere il RCEE.
- Non trattare come esaustiva la disciplina: la parte di dettaglio (periodicita', catasto
  impianti, bollino) e' anche **regionale**.

### Cosa fare
- Verificare temperature/limiti per zona, individuare i responsabili e impostare
  controllo/manutenzione e controllo di efficienza energetica con RCEE.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 74/2013 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli articoli; verificare gli aggiornamenti del DM 10/2/2014 (libretto/RCEE) e la
disciplina regionale.

## Validatori

- Non ancora assegnato (Livello 2 con termotecnico / manutentore abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #255)
- Task files: 2 (`verifica-limiti-esercizio.md`, `imposta-controllo-manutenzione.md`)
- Esempi: 2 (riscaldamento zona E; terzo responsabile in condominio/unita' singola)
