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
- **dlgs-5-2026-allegato-iii-estratto**: D.Lgs. 9 gennaio 2026, n. 5 (RED III), PDF del fascicolo
  integrale della **GU Serie generale n. 15 del 20 gennaio 2026** (hash `3d13cb9a...`, codice
  26G00018). Scopo **deliberatamente ristretto**: solo art. 29 c. 1 lett. b) punto 2 (campo di
  applicazione dell'Allegato III), lett. c) punto 2 lett. d) (quota FER del 15%) e Sezione D punto 1
  dell'Allegato III risultante. **Estrazione**: `pdftotext` **senza** `-layout` per il corpo (due
  colonne), **con** `-layout` per le pagine "Note". La forma di URL `/eli/id/.../sg/pdf` a livello di
  singolo atto risponde 404: usare `/eli/gu/YYYY/MM/DD/<numero>/sg/pdf`.
- **dlgs-5-2026-entrata-in-vigore**: scheda Normattiva del D.Lgs. 5/2026 pinnata `!vig=2026-08-09`
  (hash `1a675001...`). Serve a **una sola informazione**: "Entrata in vigore del provvedimento:
  04/02/2026". Il PDF di Gazzetta prova che il decreto non ha un articolo di entrata in vigore ma
  **non contiene la data**: derivarla dalla vacatio ordinaria sarebbe un'affermazione normativa
  priva di fonte.

Trascrizioni in `references/fonti/dpr-74-2013.md`,
`references/fonti/dlgs-5-2026-allegato-iii-estratto.md` e
`references/fonti/dlgs-5-2026-entrata-in-vigore.md`; estratto in
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
- **Obbligo FER a monte** (D.Lgs. 5/2026, art. 29): la **ristrutturazione dell'impianto termico**
  entra nel campo di applicazione dell'Allegato III del D.Lgs. 199/2021 (Sezione A punto 1) con
  quota di copertura del **15%** della somma dei consumi per climatizzazione invernale ed estiva
  (Sezione B punto 1, lett. d). Se l'obbligo non e' assolvibile e la relazione tecnica ex art. 8 c. 1
  del D.Lgs. 192/2005 non e' dovuta, il progettista **comunica al Comune** la motivazione (Sezione D
  punto 1).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre i campi dei modelli RCEE** (Allegato A) ne' il **libretto di impianto** (DM
  10/2/2014): rinviare agli atti. Non inventare la periodicita' puntuale dei controlli.
- Non **eseguire** controllo/manutenzione ne' redigere il RCEE.
- Non trattare come esaustiva la disciplina: la parte di dettaglio (periodicita', catasto
  impianti, bollino) e' anche **regionale**.
- Non **espandere** qui la trattazione degli obblighi FER: questa skill **avverte e rinvia** a
  `relazione-tecnica-requisiti-minimi-dlgs192`. Non calcolare quote di copertura, non trattare le
  altre categorie di intervento, non riprodurre le Sezioni B punto 3, C ed E dell'Allegato III.
- Non **qualificare** l'intervento come "ristrutturazione dell'impianto termico": la definizione e'
  nel DM 26/6/2015 come modificato dal DM MASE 28/10/2025 (rinvio), non nel DPR 74/2013.
- Non **affermare come certa** la decorrenza del 3 agosto 2026: la formula "decorsi centottanta
  giorni dall'entrata in vigore del presente decreto" e' inserita nell'Allegato III del D.Lgs.
  199/2021 ed e' testualmente ambigua. Segnalare l'incertezza.
- Non **derivare per ragionamento** la data di entrata in vigore del D.Lgs. 5/2026 dalla vacatio
  ordinaria di 15 giorni: citare la scheda Normattiva registrata come fonte
  `dlgs-5-2026-entrata-in-vigore` (4 febbraio 2026).
- Non trattare l'esclusione della relazione tecnica (art. 8 c. 1 D.Lgs. 192/2005) come esonero
  dall'obbligo FER: sono piani distinti.

### Cosa fare
- Verificare temperature/limiti per zona, individuare i responsabili e impostare
  controllo/manutenzione e controllo di efficienza energetica con RCEE.
- Quando l'intervento tocca il **generatore**, segnalare la verifica FER a monte e rinviare alla
  skill dedicata.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 74/2013 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli articoli; verificare gli aggiornamenti del DM 10/2/2014 (libretto/RCEE) e la
disciplina regionale.

Allegato III del D.Lgs. 199/2021: la Sezione B punto 6 ne prevede la rideterminazione almeno
quinquennale a decorrere dal 1° gennaio 2026. Se cambia la quota del 15%, aggiornare qui **solo** il
riferimento e la cifra, lasciando la trattazione completa alla skill
`relazione-tecnica-requisiti-minimi-dlgs192`.

## Validatori

- Non ancora assegnato (Livello 2 con termotecnico / manutentore abilitato).

## Stato attuale

- Versione: 0.2.0-alpha (closes #488; iniziale #255)
- Task files: 2 (`verifica-limiti-esercizio.md`, `imposta-controllo-manutenzione.md`)
- Esempi: 2 (riscaldamento zona E; terzo responsabile in condominio/unita' singola)
