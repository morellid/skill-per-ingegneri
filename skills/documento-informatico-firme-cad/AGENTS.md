# AGENTS.md - documento-informatico-firme-cad

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **valore giuridico del documento informatico** e delle **firme
elettroniche** secondo il **Codice dell'amministrazione digitale** (D.Lgs. 82/2005), artt. **20,
21, 24**. Target: ingegneri e professionisti che firmano digitalmente elaborati, depositano atti
telematici, gestiscono PEC/documenti in formato digitale.

**E' una skill documentale**: inquadra valore probatorio e tipi di firma; **non appone/verifica**
firme, **non valuta** la validita' del singolo atto, non sostituisce professionista, notaio ne'
giudice.

## Nota sull'area e sulla complementarita'

Area **software-dati-cybersecurity**. Complementare e distinta da `riuso-software-pa-cad69` (CAD
artt. 68-69, riuso software): questa copre il **documento informatico e le firme** (CAD artt.
20-24). Utile anche a chi opera con deposito telematico e firme su elaborati tecnici.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cad-artt-20-21-24**: D.Lgs. 82/2005 (CAD), pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `5e75c6b9...`; codice 005G0104). Artt. 20 (idGruppo 4, v5), 21
  (idGruppo 4, v6), 24 (idGruppo 5, v3) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/cad-artt-20-21-24.md`; estratto operativo in
`references/estratti/documento-informatico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 20**: documento informatico soddisfa la **forma scritta** e ha l'**efficacia art. 2702
  c.c.** con firma digitale/qualificata/avanzata o processo con requisiti AgID (art. 71);
  altrimenti **liberamente valutabile**; **presunzione** di riconducibilita' al titolare (c. 1-ter).
- **Art. 21**: scritture private **art. 1350 nn. 1-12 c.c.** a **pena di nullita'** con firma
  qualificata/digitale; atto pubblico informatico (c. 2-bis/2-ter).
- **Art. 24**: firma digitale **univoca**; sostituisce sigilli/timbri; **certificato qualificato**
  non scaduto/revocato/sospeso; firma su certificato revocato = **mancata sottoscrizione** (c. 4-bis).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre** le **Linee guida AgID** (art. 71) ne' l'**eIDAS** (Reg. UE 910/2014):
  rinviarvi (regole tecniche).
- Non **apporre/verificare** firme ne' valutare la validita' del singolo atto.
- Non inventare requisiti tecnici non presenti nel testo degli artt. 20/21/24.

### Cosa fare
- Inquadrare il **valore giuridico** del documento (forma scritta / art. 2702 c.c. / libera
  valutazione) sul **tipo di firma** e i **requisiti del certificato**; segnalare gli **atti
  nulli** senza firma qualificata/digitale.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del CAD pinnato a nuovo `!vig=` (nuovo hash) e rileggere artt.
20/21/24, verificando le modifiche (il CAD e' molto modificato; commi abrogati e blocchi (( ))).

## Validatori

- Non ancora assegnato (Livello 2 con esperto di diritto dell'informatica / notaio).

## Stato attuale

- Versione: 0.1.0-alpha (closes #270)
- Task files: 2 (`valuta-valore-documento.md`, `inquadra-firma-atto.md`)
- Esempi: 2 (relazione tecnica firmata digitalmente; e-mail semplice come documento informatico)
