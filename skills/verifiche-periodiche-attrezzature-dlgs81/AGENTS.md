# AGENTS.md - verifiche-periodiche-attrezzature-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al regime dei **controlli** e delle **verifiche periodiche** delle
**attrezzature di lavoro** (apparecchi di sollevamento, gru, ponti mobili sviluppabili,
generatori di vapore, recipienti/insiemi a pressione), secondo l'**art. 71 e l'Allegato VII
del D.Lgs. 9 aprile 2008, n. 81**. Target: ingegneri, datori di lavoro, RSPP, responsabili
della manutenzione.

**E' una skill documentale**: distingue i due regimi e imposta gli adempimenti; **non esegue**
le verifiche/controlli, **non redige** i verbali, **non riproduce** l'Allegato VII.

## Nota sull'area e sulla complementarita'

Area **impianti-macchine-prodotti**. Complementare e distinta da
`verifiche-periodiche-ascensori-dpr162` (ascensori), `verifiche-messa-a-terra-dpr462` (impianti
di terra) e `ped-classificazione-conformita` (conformita' PED): questa copre le **verifiche
periodiche delle attrezzature soggette** (Allegato VII) in esercizio.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-art71-allegatoVII**: D.Lgs. 9 aprile 2008, n. 81, pagina indice Normattiva
  pinnata a `!vig=2026-07-16` (hash `d8991985...`; codice 008G0104). Art. 71 (versione 6,
  idGruppo 15) caricato via `caricaArticolo` e trascritto verbatim; Allegato VII e' in formato
  grafico (trascritta la sola parte testuale disponibile, nota di aggiornamento).

Trascrizione in `references/fonti/dlgs-81-2008-art71-allegatoVII.md`; estratto operativo in
`references/estratti/verifiche-attrezzature-checklist.md`.

## Punti chiave (verificati sul testo)

- **Controlli** (c. 8-10): iniziale/periodici/straordinari da **persona competente**; risultati
  scritti **conservati almeno 3 anni**; documento dell'ultimo controllo per l'uso fuori sede.
- **Verifiche periodiche** (c. 11): solo attrezzature **Allegato VII**; **prima verifica INAIL
  entro 45 giorni**, poi soggetti abilitati; **successive** ASL/ARPA o soggetti abilitati;
  **oneri e verbali a carico del datore**.
- **Soggetti privati abilitati** (c. 12): incaricati di pubblico servizio. **Modalita'** e
  **abilitazione** con **DM 11 aprile 2011** (c. 13); **VVF** (c. 13-bis); **elenco** aggiornato
  con decreto (c. 14).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre l'Allegato VII** (elenco/periodicita', formato grafico): rinviare all'atto e
  al **DM 11/4/2011**.
- Non **eseguire** verifiche/controlli ne' redigere verbali; non sostituire INAIL/ASL/ARPA/soggetti abilitati.
- Non inventare **frequenze** (annuale/biennale/triennale) non presenti nel testo Normattiva:
  citare solo cio' che e' rintracciabile (es. la nota di aggiornamento L. 34/2026).

### Cosa fare
- Distinguere il regime (soli controlli vs anche verifiche periodiche Allegato VII) e impostare
  soggetti/termini/oneri della prima verifica e delle successive.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 71; verificare le modifiche all'**elenco dell'Allegato VII** (aggiornato con
decreto ex c. 14; es. L. 34/2026, che ha inserito le piattaforme di lavoro fuori strada per
operazioni in frutteto - verifica triennale).

## Validatori

- Non ancora assegnato (Livello 2 con esperto di sicurezza / verificatore abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #266)
- Task files: 2 (`inquadra-regime-attrezzatura.md`, `imposta-verifiche-periodiche.md`)
- Esempi: 2 (gru a torre soggetta a verifiche Allegato VII; trapano da banco - soli controlli)
