# AGENTS.md - vigilanza-sanzioni-abusi-edilizi-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **regime repressivo degli abusi edilizi**: vigilanza, sospensione dei lavori,
ordine di demolizione e acquisizione gratuita, ristrutturazione abusiva, parziale difformità, sanzioni
penali, secondo il **D.P.R. 6 giugno 2001, n. 380** (T.U. Edilizia), Titolo IV, artt. 27, 31, 33, 34,
44. Target: ingegneri, tecnici, operatori SUE.

**È una skill documentale**: inquadra il regime e i termini; **non adotta** i provvedimenti, **non
quantifica** le sanzioni, **non tratta** la sanatoria (artt. 36/36-bis), non sostituisce Comune/SUE,
tecnico o legale.

## Nota sull'area e complementarità

Area **edilizia-urbanistica-catasto**. Copre il lato **sanzionatorio**; complementare e distinta da
`modulistica-edilizia-unificata` (regime edilizio e **sanatoria** art. 36/36-bis, Salva Casa),
`contributo-costruzione-dpr380` (onerosità), `segnalazione-agibilita-dpr380` (agibilità) e
`denuncia-opere-strutturali-l1086` (strutture). La **sanatoria** NON è oggetto di questa skill.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-artt-27-31-33-34-44**: D.P.R. 6 giugno 2001, n. 380, pagina indice Normattiva pinnata
  a `!vig=2026-07-17` (hash `bac3f7b1...`; codice 001G0429). Artt. 27 (grp8, v3), 31 (grp9, v8), 33
  (grp9, v4), 34 (grp9, v8), 44 (grp9, v5) via `caricaArticolo`, trascritti verbatim.

Trascrizione in `references/fonti/dpr-380-2001-artt-27-31-33-34-44.md`; estratto operativo in
`references/estratti/abusi-edilizi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 27**: vigilanza; sospensione lavori, provvedimenti entro **45 gg**, sequestro entro **15 gg**;
  demolizione d'ufficio in aree vincolate (Soprintendente, **180 gg**).
- **Art. 31**: assenza/totale difformità/variazioni essenziali; ingiunzione, **90 gg** (proroga **240
  gg**), **acquisizione gratuita** (area **≤ 10 volte** sup. utile abusiva), **sanzione 2.000-20.000
  euro**, demolizione a spese, ordine del giudice ex art. 44.
- **Art. 33**: ristrutturazione abusiva → demolizione o **doppio dell'aumento di valore**; contributo
  dovuto.
- **Art. 34**: parziale difformità → demolizione o **triplo del costo di produzione/valore venale** se
  la demolizione pregiudica la parte conforme.
- **Art. 44**: sanzioni penali (ammenda fino a 10.329 euro; arresto fino a 2 anni + ammenda
  5.164-51.645 euro; lottizzazione abusiva e confisca).

## Convenzioni specifiche

### Cosa NON fare
- Non **adottare** i provvedimenti (ordinanze/ingiunzioni) né eseguire notifiche/acquisizioni.
- Non **quantificare** le sanzioni (doppio/triplo, importi) né determinare il valore venale.
- Non **trattare** la **sanatoria** (artt. 36/36-bis) o le tolleranze (art. 34-bis): rinviare a
  `modulistica-edilizia-unificata`.

### Cosa fare
- **Classificare** l'abuso e la misura (31/33/34); **ricostruire** vigilanza e termini (27); segnalare
  la **rilevanza penale** (44).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 380/2001 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 27, 31, 33, 34, 44 (testo tra `(( ))`; modifiche anche del Salva Casa - DL 69/2024).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico/ufficio abusi o legale amministrativista).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-abuso-misura.md`, `ricostruisci-vigilanza-termini.md`)
- Esempi: 2 (abuso in assenza di permesso - artt. 27/31; parziale difformità - art. 34)
