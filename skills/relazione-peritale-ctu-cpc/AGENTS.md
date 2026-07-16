# AGENTS.md - relazione-peritale-ctu-cpc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto alla **strutturazione della relazione peritale** e allo **svolgimento delle
operazioni** del **consulente tecnico d'ufficio (CTU)** nel **processo civile**, ai
sensi degli **artt. 191-201 c.p.c.**, con inquadramento del CTU **nell'albo** (D.M.
109/2023). Target: ingegneri nominati CTU (o aspiranti tali).

**E' una skill procedurale/documentale di dominio forense**: struttura la relazione,
i quesiti e il verbale; **non fornisce il contenuto tecnico/di merito** della perizia
e non sostituisce le direttive del giudice.

## Nota sull'area di catalogo

Skill nell'area **forense** (CTU & ingegneria forense), aggiunta ad `areas.yaml` su
indicazione esplicita del maintainer. L'area comprende `compensi-ctu-dpr115` (#42) e
questa (#41), in deroga consapevole alla soglia di 3 skill indicata in `areas.yaml`.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **cpc-191-201**: Codice di procedura civile (R.D. 1443/1940), artt. 191-201, pagina
  indice Normattiva pinnata a `!vig=2026-07-16` (hash 7a53e745...; codice 040U1443).
  Articoli caricati via AJAX (caricaArticolo, idGruppo=28) e trascritti verbatim in
  `references/fonti/codice-procedura-civile-artt-191-201.md`.
- **dm-109-2023**: D.M. Giustizia 4/8/2023 n. 109 (albo CTU), pagina ELI di Gazzetta
  Ufficiale (riferimento solo-online, `sha256: null`, `binary_path: null`, come altre
  voci `/eli/id/.../sg` del repo). Testo letto via `caricaArticolo` e trascritto
  verbatim in `references/fonti/dm-109-2023.md` (artt. 1-12 + settori categoria
  INGEGNERIA dell'Allegato A).

Estratto operativo: `references/estratti/struttura-relazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Nomina e quesiti** (art. 191): ordinanza ex art. 183 c. 4; il giudice formula i
  quesiti. Piu' consulenti solo per grave necessita' o se la legge lo prevede.
- **Astensione/ricusazione** (art. 192): denuncia/istanza almeno 3 giorni prima
  dell'udienza di comparizione.
- **Giuramento** (art. 193): in udienza o con **dichiarazione a firma digitale**; con
  lo stesso provvedimento il giudice fissa i **termini dell'art. 195, terzo comma**.
- **Attivita'** (art. 194): indagini, chiarimenti alle parti, informazioni da terzi,
  piante/calchi/rilievi (se autorizzati); **intervento di parti e CTP**.
- **Verbale e relazione** (art. 195): scansione **bozza alle parti -> osservazioni
  delle parti -> deposito** di relazione + osservazioni + **sintetica valutazione**.
- **Rinnovazione/sostituzione** (196); **camera di consiglio** (197); **esame
  contabile e conciliazione** (198-199, titolo esecutivo al verbale); **mancata
  conciliazione** (200); **CTP** (201).
- **Albo CTU** (D.M. 109/2023): categorie e **settori di specializzazione** (art. 3,
  Allegato A); **requisiti** e **domanda** di iscrizione (artt. 4-5); mantenimento
  (art. 6).

## Convenzioni specifiche

### Cosa NON fare
- Non **fornire contenuti tecnici/di merito** della perizia (rilievi, calcoli,
  conclusioni): fuori scope.
- Non trattare la **perizia penale** (c.p.p.) ne' la **liquidazione del compenso**
  (vedi skill `compensi-ctu-dpr115`).
- Non riprodurre come "verbatim" l'**intera tabella dell'Allegato A** del D.M.
  109/2023 (celle a capo multi-riga): solo i settori della categoria INGEGNERIA sono
  trascritti verbatim; per le altre categorie si rinvia all'Allegato A.

### Cosa fare
- Impostare indice della relazione, scansione dei termini (art. 195) e struttura del
  verbale (art. 194), citando gli articoli.
- Inquadrare categoria/settore e requisiti di iscrizione del CTU (D.M. 109/2023).

## Aggiornamento delle fonti

Normattiva: riscaricare la pagina indice del c.p.c. pinnata a un nuovo `!vig=` (nuovo
hash) e rileggere gli artt. 191-201 (attenzione ai numeri di versione per articolo).
D.M. 109/2023: verificare eventuali modifiche del regolamento e degli allegati su GU.

## Validatori

- Non ancora assegnato (Livello 2 con CTU/avvocato esperto di processo civile).

## Stato attuale

- Versione: 0.1.0-alpha (closes #41)
- Task files: 2 (`struttura-relazione.md`, `verbale-operazioni-peritali.md`)
- Esempi: 2 (nomina/quesiti/termini con giuramento a firma digitale; verbale del
  sopralluogo con CTP presenti)
