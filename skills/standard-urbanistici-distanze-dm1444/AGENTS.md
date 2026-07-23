# AGENTS.md - standard-urbanistici-distanze-dm1444

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (geometra, ingegnere, architetto, urbanista) per l'**inquadramento dei
limiti inderogabili** del **DM 2 aprile 1968 n. 1444**: zone territoriali omogenee (art. 2), standard
urbanistici (artt. 3-5), limiti di densità edilizia (art. 7), altezza (art. 8) e distanza tra i fabbricati
(art. 9). Target: professionisti dell'urbanistica e dell'edilizia (formazione/revisione strumenti urbanistici;
verifica di conformità urbanistica).

**È una skill documentale per il tecnico**: fornisce la classificazione delle zone, gli standard, le densità,
le altezze e le distanze del **testo originario** del 1968; **non** redige lo strumento urbanistico né
riproduce le articolazioni regionali/comunali o le modifiche successive.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Copre i **limiti inderogabili di natura pubblicistica** (zone, standard,
densità, altezze, distanze) del DM 1444/1968. È **distinta** da `distanze-legali-costruzioni-cc` (codice
civile artt. 873-907, **diritto privato**): il DM 1444/1968 fissa limiti cogenti ai fini della formazione
degli strumenti urbanistici. Restano fuori scope: la redazione del piano, le articolazioni regionali/comunali,
le modifiche normative successive e l'interpretazione giurisprudenziale (in particolare sull'art. 9).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-1444-1968**: PDF della G.U. Serie Generale n. 97 del 16/4/1968 (DM 2 aprile 1968 n. 1444), SHA256
  `418cbdf7...` (doppio download riproducibile dallo stesso URL eli). Scansione **GURITEL**: `pdftotext` non
  estrae testo utile; gli articoli 1-10 sono stati letti renderizzando le pagine in immagine (`pdftoppm -r
  150`, pagine PDF 24-26) e trascritti verbatim.

Trascrizione in `references/fonti/dm-1444-1968.md`; estratto operativo in
`references/estratti/standard-urbanistici-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **Zone** (art. 2): A/B/C/D/E/F; B parziale se coperto ≥ 12,5% e densità > 1,5 mc/mq.
- **Standard** (art. 3): 18 mq/ab (4,50 + 2,00 + 9,00 + 2,50); 25 mq/ab superficie lorda.
- **Per zona** (art. 4): A/B doppio; C 18 (o 12, 4 scuole, ≤ 10.000 ab); E 6; F 1,5+1+15 mq/ab. Produttivi
  (art. 5): D ≥ 10%; commerciale 80/100 mq.
- **Densità** (art. 7): A ≤ 5 mc/mq; B 7/6/5 mc/mq; E 0,03 mc/mq. Altezze (art. 8) per zone.
- **Distanze** (art. 9): 10 m tra pareti finestrate; C ≥ altezza; strade +5/+7,50/+10 m per lato.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** lo strumento urbanistico né eseguire il dimensionamento del piano.
- Non **riprodurre** le articolazioni regionali/comunali, le modifiche successive o la giurisprudenza; non
  trattare le distanze del **codice civile** (→ skill artt. 873-907).

### Cosa fare
- Fornire zone, standard, densità, altezze e distanze del DM 1444/1968 (testo originario), sempre con rinvio
  all'articolo.

## Aggiornamento delle fonti

DM: se il PDF GU cambia (nuova scansione) riscaricare, ricalcolare l'hash con doppio download e rileggere via
immagine (GURITEL). Verificare le costanti (12,5% e 1,5 mc/mq art. 2; 18 mq/ab art. 3; 5/6/7 e 0,03 mc/mq
art. 7; 10 m e +5/+7,50/+10 m art. 9). Attenzione: la fonte è il **testo originario 1968**; eventuali
aggiornamenti normativi vanno segnalati come contesto, non riscritti nel testo.

## Validatori

- Non ancora assegnato (Livello 2 con urbanista/tecnico comunale).

## Stato attuale

- Versione: 0.1.0-alpha (closes #450)
- Task files: 2 (`classifica-zone-omogenee-standard.md`, `verifica-densita-altezza-distanze.md`)
- Esempi: 2 (classificazione di una zona e computo standard 18 mq/ab; verifica della distanza minima tra
  fabbricati, art. 9)
