# AGENTS.md - autorizzazione-integrata-ambientale-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**Autorizzazione Integrata Ambientale (AIA/IPPC)**: domanda, procedura di
rilascio, contenuto e condizioni (VLE su BAT), rinnovo/riesame, rispetto delle condizioni e
controlli/ispezioni, secondo il **D.Lgs. 3 aprile 2006, n. 152, Parte II, Titolo III-bis** (artt.
29-ter, 29-quater, 29-sexies, 29-octies, 29-decies). Target: ingegneri, gestori di installazioni,
consulenti ambientali.

**È una skill documentale**: inquadra procedura/contenuto/controlli; **non redige** la domanda/AIA,
**non individua** le BAT, non sostituisce il gestore, l'autorità competente o ISPRA/ARPA.

## Nota sull'area e complementarità

Area **ambiente-territorio-mobilita**. Complementare e distinta da `aua-dpr59-dossier` (AUA, impianti
**non** soggetti ad AIA), `scarichi-emissioni-dlgs152` (autorizzazioni singole residuali) e
`via-screening-sia-dlgs152` (VIA): questa copre l'**AIA** (impianti IPPC).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006-aia-titolo3bis**: D.Lgs. 3 aprile 2006, n. 152, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `c2175fe5...`; codice 006G0171). Artt. 29-ter, 29-quater, 29-sexies,
  29-octies, 29-decies (idGruppo 9) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-152-2006-aia-titolo3bis.md`; estratto operativo in
`references/estratti/aia-checklist.md`.

## Punti chiave (verificati sul testo)

- **Domanda** (art. 29-ter): contenuti a-m; relazione di riferimento per sostanze pericolose;
  completezza entro 30 gg.
- **Procedura** (art. 29-quater): avvio 30 gg, pubblicazione 15 gg, osservazioni 30 gg, conferenza di
  servizi, integrazioni ≤ 90 gg, determinazione entro **150 gg**; coordinamento con la VIA.
- **Contenuto** (art. 29-sexies): VLE su **BAT** (senza obbligo di tecnica specifica), entro i
  **BAT-AEL**; monitoraggio; deroghe motivate.
- **Riesame** (art. 29-octies): su nuove conclusioni sulle BAT; **10 anni** dal rilascio/ultimo
  riesame; gestore 30-180 gg.
- **Controlli** (art. 29-decies): ISPRA/ARPA; ispezioni 1/3 anni, 6 mesi dopo grave inosservanza;
  inosservanze → diffida/sospensione/revoca-chiusura.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la domanda/AIA né individuare le **BAT** applicabili.
- Non **riprodurre** gli **Allegati VIII/XII** (attività IPPC/soglie) né i BREF.
- Non inventare **termini** (usare 30/15/30 gg, 90 gg, 150 gg, 10 anni, 1/3 anni, 6 mesi come da testo).

### Cosa fare
- **Verificare** l'assoggettabilità (rinvio All. VIII/XII), **comporre** contenuti/timeline della
  domanda, **inquadrare** contenuto/riesame/controlli.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 152/2006 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 29-ter/quater/sexies/octies/decies (testo tra `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico ambientale / autorità competente o ARPA).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-domanda-aia.md`, `verifica-condizioni-controlli.md`)
- Esempi: 2 (domanda e procedura; controlli e inosservanze art. 29-decies)
