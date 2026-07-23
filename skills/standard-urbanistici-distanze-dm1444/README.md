# standard-urbanistici-distanze-dm1444

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con urbanista/tecnico comunale da completare)

Skill di **supporto documentale** al **tecnico** (geometra, ingegnere, architetto, urbanista) per
l'**inquadramento dei limiti inderogabili** del **DM 2 aprile 1968 n. 1444**: zone territoriali omogenee,
standard urbanistici, densità edilizia, altezze e distanze tra i fabbricati.

**Non redige** lo strumento urbanistico né **riproduce** le articolazioni regionali/comunali o le modifiche
successive, e **non sostituisce** il pianificatore/progettista: inquadra il **testo originario** del 1968. È
**distinta** da `distanze-legali-costruzioni-cc` (codice civile artt. 873-907, diritto privato).

## Target

Professionisti dell'urbanistica e dell'edilizia che, nella formazione/revisione degli strumenti urbanistici o
nella verifica di conformità urbanistica, devono applicare i limiti del DM 1444/1968.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-zone-omogenee-standard` | Classificazione delle zone territoriali omogenee (art. 2) e computo degli standard urbanistici per zona (artt. 3-5) |
| `verifica-densita-altezza-distanze` | Limiti inderogabili di densità edilizia (art. 7), altezza (art. 8) e distanza tra i fabbricati (art. 9) |

Nucleo: **zone A-F** (art. 2), **standard 18 mq/abitante** (art. 3: 4,50 + 2,00 + 9,00 + 2,50), quantità per
zona (art. 4) e produttivi (art. 5), **densità** (art. 7: A ≤ 5, B 7/6/5, E 0,03 mc/mq), **altezze** (art. 8) e
**distanze** (art. 9: **10 m tra pareti finestrate**; strade + 5/7,50/10 m per lato).

## Relazione con altre skill

- Copre i **limiti inderogabili di natura pubblicistica** (urbanistica) del DM 1444/1968. È **distinta** da
  `distanze-legali-costruzioni-cc` (codice civile, diritto privato) e complementare alle skill DPR 380/2001
  (titoli edilizi, agibilità).

## Fonti consultate

- **DM 2 aprile 1968 n. 1444** - **G.U. Serie Generale n. 97 del 16/4/1968** (PDF Gazzetta Ufficiale, SHA256
  `418cbdf7...`). Scansione **GURITEL**: gli articoli 1-10 sono stati letti renderizzando le pagine in immagine
  (`pdftoppm`, pagine PDF 24-26) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** lo strumento urbanistico né esegue il dimensionamento del piano.
- **Non riproduce** le **articolazioni regionali/comunali** né le **modifiche normative successive** e
  l'interpretazione giurisprudenziale (in particolare sull'art. 9): la fonte è il **testo originario** del 1968.
- **Non tratta** le distanze del **codice civile** (artt. 873-907, → skill `distanze-legali-costruzioni-cc`);
  **non** sostituisce il pianificatore né il progettista.

**La skill è un supporto documentale: non sostituisce il pianificatore né il progettista, né la lettura del DM 1444/1968, degli strumenti urbanistici vigenti e delle norme regionali/comunali applicabili.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
