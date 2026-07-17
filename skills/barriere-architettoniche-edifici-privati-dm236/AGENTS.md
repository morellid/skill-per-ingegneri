# AGENTS.md - barriere-architettoniche-edifici-privati-dm236

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **superamento delle barriere architettoniche** negli **edifici privati**
e di **edilizia residenziale pubblica**: obbligo di progettazione (L. 13/1989), livelli di
**accessibilita'/visitabilita'/adattabilita'** e criteri di progettazione (DM 236/1989). Target:
ingegneri, architetti, geometri, uffici tecnici comunali.

**E' una skill documentale**: inquadra obbligo, livelli e criteri; **non riproduce i valori
dimensionali** dell'art. 8 (in formato grafico), non redige l'asseverazione di conformita' e non
sostituisce il progettista/ufficio tecnico.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Complementare (e distinta) rispetto alle skill di
accessibilita' **digitale** (`accessibilita-siti-app-l4-2004`,
`verifica-accessibilita-dichiarazione-agid`): questa e' l'accessibilita' **fisica** degli
edifici. Non copre gli **edifici/spazi pubblici** (DPR 503/1996).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **legge-13-1989**: L. 9 gennaio 1989, n. 13, indice Normattiva pinnato `!vig=2026-07-16`
  (hash `b95aa2b5...`, codice 089G0031). Artt. 1 (obbligo/delega) e 7 (regime abilitativo).
- **dm-236-1989**: D.M. LL.PP. 14 giugno 1989, n. 236, indice Normattiva pinnato
  `!vig=2026-07-16` (hash `f72a56a4...`, codice 089G0298). Artt. 2 (definizioni), 3 (livelli e
  categorie), 4 (criteri di progettazione), 8.0 (modalita' di misura).

Trascrizione in `references/fonti/l13-dm236-1989.md`; estratto in
`references/estratti/barriere-architettoniche-checklist.md`.

## Punti chiave (verificati sul testo)

- **Obbligo** (art. 1 L. 13/1989): nuovi edifici e ristrutturazioni di interi edifici (inclusa ERP).
- **Tre livelli** (artt. 2-3 DM): **accessibilita'** (spazi esterni, parti comuni, 5% alloggi ERP,
  attivita' sociali, sedi a collocamento obbligatorio); **visitabilita'** (ogni unita' immobiliare,
  con precisazioni per residenziale/spettacoli/ristorazione); **adattabilita'** (differita).
- **Deroga ascensore**: edifici residenziali **<= 3 livelli fuori terra** (con predisposizione).
- **Criteri** (art. 4): porte, servizi igienici, scale, rampe, ascensore, corridoi, spazi di manovra.
- **Regime abilitativo** (art. 7 L. 13/1989, coordinato con DPR 380/2001).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre i valori dimensionali** dell'art. 8 (formato grafico): rinviare all'atto. Non
  inventare/stimare numeri (pendenza rampe, luce porte, cabina ascensore, spazi di manovra).
- Non **redigere** l'asseverazione/relazione di conformita'.
- Non trattare gli **edifici pubblici** (DPR 503/1996) ne' l'accessibilita' digitale.

### Cosa fare
- Individuare obbligo e livello per categoria di edificio e impostare i criteri di progettazione,
  rinviando ai valori dimensionali dell'art. 8.

## Aggiornamento delle fonti

Normattiva: riscaricare gli indici di L. 13/1989 e DM 236/1989 pinnati a nuovo `!vig=` (nuovi
hash) e rileggere gli articoli, verificando il coordinamento con il DPR 380/2001.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di accessibilita' / ufficio tecnico comunale).

## Stato attuale

- Versione: 0.1.0-alpha (closes #253)
- Task files: 2 (`individua-livello-accessibilita.md`, `imposta-criteri-progettazione.md`)
- Esempi: 2 (palazzina residenziale 3 piani; ristorante - visitabilita')
