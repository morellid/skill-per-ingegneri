# requisiti-igienico-sanitari-alloggi-dm1975

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico comunale/ASL o progettista edile da completare)

Skill di **supporto documentale** al **tecnico** (geometra, ingegnere, architetto) per l'**inquadramento dei
requisiti igienico-sanitari minimi** dei locali di abitazione secondo il **DM 5 luglio 1975** (Ministero della
sanità): altezze minime, superfici minime, aeroilluminazione, riscaldamento, ventilazione e servizi.

**Non redige** il progetto né esegue **calcoli illuminotecnici/termotecnici** e **non sostituisce** il
progettista: inquadra i **requisiti minimi nazionali**. È **distinta** da `requisiti-acustici-passivi-edifici-dpcm`
(valori limite acustici) e da `barriere-architettoniche-edifici-privati-dm236` (accessibilità); complementare
a `segnalazione-agibilita-dpr380`.

## Target

Progettisti edili che, nella progettazione degli alloggi, nei frazionamenti/cambi di destinazione o nella
verifica di agibilità, devono controllare i requisiti igienico-sanitari minimi (DM 5/7/1975).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-altezze-superfici-minime` | Altezza minima interna (art. 1) e superfici minime per abitante, stanze da letto, soggiorno e alloggio monostanza (artt. 2-3) |
| `verifica-aeroilluminazione-servizi-impianti` | Riscaldamento (art. 4), illuminazione/aeroilluminazione (art. 5), ventilazione (art. 6), bagno (art. 7) e protezione acustica (art. 8) |

Nucleo: **altezza minima 2,70 m** (2,40 servizi; 2,55 montani), **superfici** (14+10 mq/ab; letto 9/14;
soggiorno 14; **monostanza 28/38 mq**), **temperatura 18-20 °C**, **aeroilluminazione** (FLDm ≥ 2%; finestra ≥
1/8 del pavimento), **bagno** (vaso, bidet, vasca/doccia, lavabo).

## Relazione con altre skill

- Copre i **requisiti igienico-sanitari minimi** degli alloggi (DM 5/7/1975). **Distinta** da
  `requisiti-acustici-passivi-edifici-dpcm` (DPCM 5/12/1997) e `barriere-architettoniche-edifici-privati-dm236`;
  **complementare** a `segnalazione-agibilita-dpr380` (agibilità).

## Fonti consultate

- **DM 5 luglio 1975** - **G.U. Serie Generale n. 190 del 18/7/1975** (PDF Gazzetta Ufficiale, SHA256
  `3fd9f355...`). Scansione **GURITEL**: gli articoli 1-9 sono stati letti renderizzando le pagine in immagine
  (`pdftoppm`, pagine PDF 12-13) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il progetto né esegue calcoli illuminotecnici/termotecnici di dettaglio.
- **Non riproduce** i **regolamenti edilizi regionali/comunali**, il **Regolamento Edilizio Tipo** né le
  **deroghe** per il **recupero dei sottotetti**/locali esistenti (leggi regionali).
- **Non fornisce** i valori limite acustici (→ `requisiti-acustici-passivi-edifici-dpcm`) né l'accessibilità (→
  `barriere-architettoniche-edifici-privati-dm236`); non sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista, né la lettura del DM 5 luglio 1975 e dei regolamenti edilizi regionali/comunali applicabili.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
