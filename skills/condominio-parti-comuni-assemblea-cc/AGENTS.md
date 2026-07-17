# AGENTS.md - condominio-parti-comuni-assemblea-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **condominio negli edifici**: parti comuni, innovazioni (ordinarie/agevolate) e
costituzione dell'assemblea con quorum e maggioranze delle deliberazioni, secondo il **Codice civile,
artt. 1117, 1120, 1136**. Target: ingegneri/architetti (progettisti di interventi su parti comuni,
amministratori, CTU condominiali).

**È una skill documentale**: inquadra parti comuni, innovazioni e maggioranze; **non redige** verbali/
delibere, **non valuta** validità/impugnazione (art. 1137), non tratta le tabelle millesimali, non
sostituisce l'amministratore, il legale o il giudice.

## Nota sull'area

Area **forense** (diritto civile). Complementare a `responsabilita-appaltatore-rovina-cc` (art. 1669,
rovina/gravi difetti) e alle skill CTU (`relazione-peritale-ctu-cpc`, `compensi-ctu-dpr115`): questa
copre il **condominio** (parti comuni, innovazioni, assemblea).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cc-artt-1117-1120-1136**: Codice civile (R.D. 262/1942), pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `f817bc32...`; codice 042U0262). Artt. 1117 (v2), 1120 (v4), 1136 (v4),
  idGruppo 140, flagTipoArticolo 2, caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/cc-artt-1117-1120-1136.md`; estratto operativo in
`references/estratti/condominio-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 1117**: parti comuni (n. 1 strutture/facciate/scale/cortili; n. 2 parcheggi/locali servizi; n.
  3 impianti centralizzati fino al punto di diramazione/utenza), salvo titolo contrario.
- **Art. 1120**: innovazioni ordinarie (2/3 del valore, 5° comma 1136) e agevolate (metà del valore, 2°
  comma 1136); convocazione entro 30 gg su richiesta di un condomino; divieti (stabilità/sicurezza/
  decoro/inservibilità).
- **Art. 1136**: quorum costitutivi/deliberativi (1ª conv. 2/3 valore + maggioranza partecipanti; 2ª
  conv. 1/3 e 1/3); maggioranze qualificate del 2° comma (nomina/revoca amministratore, liti,
  ricostruzione, innovazioni agevolate); innovazioni ordinarie 2/3 (5° comma); convocazione di tutti;
  verbale.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** convocazioni/verbali/delibere né compilare le **tabelle millesimali**.
- Non **valutare** validità/impugnazione (art. 1137) né la ripartizione delle spese (artt. 1123-1126).
- Non inventare **quorum** (usare 2/3, 1/2, 1/3 del valore come da art. 1136).

### Cosa fare
- **Individuare** le parti comuni, **classificare** l'innovazione con la maggioranza, **verificare** i
  quorum, con rinvio al legale per la validità.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del Codice civile pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 1117, 1120, 1136 (testo tra `(( ))`; riforma L. 220/2012).

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista/amministratore di condominio).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-parti-innovazione.md`, `verifica-quorum-assemblea.md`)
- Esempi: 2 (quorum nomina amministratore - art. 1136; innovazioni agevolate cappotto/fotovoltaico - art. 1120)
