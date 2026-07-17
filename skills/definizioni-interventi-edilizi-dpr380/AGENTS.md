# AGENTS.md - definizioni-interventi-edilizi-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **qualificazione dell'intervento edilizio** secondo le
**definizioni dell'art. 3 del D.P.R. 380/2001** (Testo unico edilizia). Target:
ingegneri/architetti (progettisti, tecnici comunali) e richiedenti del titolo.

**È una skill documentale**: qualifica la categoria dell'intervento (a-f); **non
seleziona** il titolo (CILA/SCIA/PdC), **non redige** la pratica, **non applica** il
Salva Casa, non sostituisce il progettista o il Comune.

## Nota sull'area

Area **edilizia-urbanistica-catasto**. È la definizione **upstream**: distinta da
`modulistica-edilizia-unificata` (che seleziona il modulo/allegati e il titolo) e da
`permesso-costruire-dpr380` (regime del titolo). Complementare alle altre skill DPR 380
(agibilita', contributo, vigilanza/abusi).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-art-3**: DPR 380/2001, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `bac3f7b1...`; codice 001G0429). Art. 3 versione 11, idGruppo
  1, flagTipoArticolo 0, caricato via `caricaArticolo` e trascritto verbatim.

Trascrizione in `references/fonti/dpr-380-2001-art-3.md`; estratto operativo in
`references/estratti/definizioni-interventi-checklist.md`.

## Punti chiave (verificati sul testo)

- **lett. a** manutenzione ordinaria (finiture; impianti tecnologici esistenti).
- **lett. b** manutenzione straordinaria (opere anche strutturali; servizi;
  frazionamento/accorpamento senza modifica di volumetria e con originaria destinazione
  d'uso; modifiche ai prospetti per agibilita'/accesso, no immobili tutelati).
- **lett. c** restauro e risanamento conservativo (conservazione dell'organismo;
  possibile mutamento d'uso compatibile).
- **lett. d** ristrutturazione edilizia (organismo diverso; demo-ricostruzione con
  diversi sagoma/sedime salvo vincoli D.Lgs. 42/2004 e zone A DM 1444/1968; ripristino
  crollati con consistenza accertabile).
- **lett. e** nuova costruzione (non riconducibile alle altre; sottocasi e.1-e.7:
  manufatti/ampliamenti fuori sagoma; urbanizzazioni; infrastrutture; torri/tralicci;
  manufatti leggeri/roulotte stabili; pertinenze > 20% del volume; depositi/impianti
  produttivi all'aperto).
- **lett. f** ristrutturazione urbanistica (sostituzione del tessuto urbanistico).
- **c. 2** le definizioni prevalgono sugli strumenti urbanistici e i regolamenti
  edilizi.

## Convenzioni specifiche

### Cosa NON fare
- Non **scegliere il titolo** (CILA/SCIA/PdC): rinvio a `modulistica-edilizia-unificata`.
- Non **inventare** soglie: usare il **20%** del volume per le pertinenze (e.6) come da
  testo.
- Non applicare **Salva Casa/tolleranze/sanatorie** ne' valutare lo stato legittimo.

### Cosa fare
- **Qualificare** l'intervento nella categoria corretta con i criteri (volumetria,
  destinazione d'uso, sagoma/sedime, vincoli), con rinvio alla scelta del titolo e al
  Comune.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del DPR 380/2001 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere l'art. 3 (testo tra `(( ))` = modifiche successive, es. Salva Casa DL
69/2024 conv. L. 105/2024).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico comunale / esperto di diritto edilizio).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`qualifica-intervento.md`, `distingui-nuova-costruzione.md`)
- Esempi: 2 (frazionamento vs demo-ricostruzione - lett. b/d; pertinenza oltre il 20% - lett. e.6)
