# CHANGELOG - standard-urbanistici-distanze-dm1444

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #450)
- Prima versione della skill di supporto al **tecnico** (geometra, ingegnere, architetto, urbanista) per
  l'**inquadramento dei limiti inderogabili** del **DM 2 aprile 1968 n. 1444** (zone territoriali omogenee,
  standard urbanistici, densità, altezze e distanze), nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **DM 2 aprile 1968 n. 1444** - PDF della G.U. Serie Generale n. 97 del 16 aprile 1968 - SHA256:
    418cbdf7a24fa96bc77992f0504feb0c0defaec1593518d9e8aa3e62091562c8 (doppio download riproducibile dallo
    stesso URL eli della Gazzetta Ufficiale).
  - Il PDF è una scansione GURITEL (immagine): gli articoli 1-10 sono stati letti renderizzando le pagine in
    immagine (`pdftoppm -r 150 -png`, pagine PDF 24-26) e trascritti verbatim in
    `references/fonti/dm-1444-1968.md` (testo originario del 1968).
- Estratto operativo `references/estratti/standard-urbanistici-checklist.md`.
- Due task: `classifica-zone-omogenee-standard.md` e `verifica-densita-altezza-distanze.md`.
- Due esempi: classificazione di una zona e computo degli standard (18 mq/abitante); verifica della distanza
  minima tra fabbricati (art. 9).

### Contenuto ancorato al testo
- Zone territoriali omogenee (art. 2): A storiche/di pregio; B edificate (parziali se coperto ≥ 12,5% e
  densità > 1,5 mc/mq); C nuovi complessi; D industriali; E agricole; F attrezzature di interesse generale.
  Standard residenziali (art. 3): 18 mq/ab (4,50 istruzione + 2,00 interesse comune + 9,00 verde/sport + 2,50
  parcheggi); 25 mq/ab superficie lorda. Quantità per zona (art. 4): A/B doppio computo; C 18 mq (o 12 mq, di
  cui 4 scuole, per comuni ≤ 10.000 ab.); E 6 mq; F 1,5 + 1 + 15 mq/ab. Produttivi (art. 5): D ≥ 10%;
  commerciale/direzionale 80 mq ogni 100 mq. Densità edilizia (art. 7): A ≤ 50% media e ≤ 5 mc/mq; B 7/6/5
  mc/mq (comuni > 200.000 / 200.000-50.000 / < 50.000 ab.); E 0,03 mc/mq. Altezze (art. 8) per zone. Distanze
  (art. 9): 10 m tra pareti finestrate (nuovi edifici); zone C ≥ altezza del fabbricato più alto (anche una
  parete finestrata se sviluppo > 12 m); strade interposte: larghezza sede + 5 / 7,50 / 10 m per lato (strade
  < 7 / 7-15 / > 15 m).

### Scope e limiti
- Non redige lo strumento urbanistico né esegue il dimensionamento del piano; non riproduce le articolazioni
  regionali/comunali né le modifiche normative successive e la giurisprudenza (in particolare sull'art. 9); non
  tratta le distanze del codice civile (artt. 873-907). Non sostituisce il pianificatore né il progettista.

### Note di sviluppo
- Distinta da `distanze-legali-costruzioni-cc` (codice civile, diritto privato): il DM 1444/1968 fissa limiti
  di natura pubblicistica ai fini urbanistici. Fonte GURITEL letta via immagine. La trascrizione è del testo
  originario del 1968. Validazione Livello 2 con urbanista/tecnico comunale.
