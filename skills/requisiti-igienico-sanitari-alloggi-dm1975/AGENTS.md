# AGENTS.md - requisiti-igienico-sanitari-alloggi-dm1975

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico** (geometra, ingegnere, architetto) per l'**inquadramento dei requisiti
igienico-sanitari minimi** dei locali di abitazione secondo il **DM 5 luglio 1975** (Ministero della sanità):
altezze minime (art. 1), superfici minime (artt. 2-3), riscaldamento (art. 4), aeroilluminazione (art. 5),
ventilazione (art. 6), servizi (art. 7) e protezione acustica (art. 8). Target: progettisti edili
(progettazione alloggi, frazionamenti/cambi di destinazione, verifica di agibilità).

**È una skill documentale per il tecnico**: fornisce i valori minimi nazionali; **non** redige il progetto né
esegue calcoli illuminotecnici/termotecnici di dettaglio, e **non** riproduce i regolamenti edilizi
regionali/comunali o le deroghe (es. recupero sottotetti).

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Copre i **requisiti igienico-sanitari minimi** degli alloggi (DM
5/7/1975), riferimento nazionale per l'abitabilità/agibilità. È **distinta** da
`requisiti-acustici-passivi-edifici-dpcm` (DPCM 5/12/1997, valori limite acustici) e da
`barriere-architettoniche-edifici-privati-dm236` (accessibilità); **complementare** a
`segnalazione-agibilita-dpr380` (procedura di agibilità). Restano fuori scope: la redazione del progetto, i
regolamenti edilizi regionali/comunali e il Regolamento Edilizio Tipo, le deroghe per il recupero dei
sottotetti/locali esistenti (leggi regionali).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-5-7-1975**: PDF della G.U. Serie Generale n. 190 del 18/7/1975 (DM 5 luglio 1975), SHA256 `3fd9f355...`
  (doppio download riproducibile dallo stesso URL eli). Scansione **GURITEL**: `pdftotext` non estrae testo
  utile; gli articoli 1-9 sono stati letti renderizzando le pagine in immagine (`pdftoppm -r 150`, pagine PDF
  12-13) e trascritti verbatim.

Trascrizione in `references/fonti/dm-5-7-1975.md`; estratto operativo in
`references/estratti/requisiti-igienico-sanitari-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **Altezze** (art. 1): 2,70 m; 2,40 m (corridoi/disimpegni/bagni/gabinetti/ripostigli); 2,55 m (comuni montani
  > 1000 m s.l.m.).
- **Superfici** (art. 2): 14 mq/ab (primi 4) + 10 mq successivi; letto 9/14 mq; soggiorno ≥ 14 mq. Monostanza
  (art. 3): 28 mq (1 pers.) / 38 mq (2 pers.).
- **Aria/luce** (artt. 4-5): 18-20 °C; FLDm ≥ 2%; superficie finestrata apribile ≥ 1/8 del pavimento.
- **Servizi** (artt. 6-7): ventilazione meccanica ove manca la naturale; bagno con vaso, bidet, vasca/doccia,
  lavabo.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il progetto né eseguire calcoli illuminotecnici/termotecnici di dettaglio.
- Non **riprodurre** i regolamenti edilizi regionali/comunali, il Regolamento Edilizio Tipo o le deroghe per il
  recupero dei sottotetti; non fornire i valori limite acustici (→ DPCM 5/12/1997) né l'accessibilità (→ DM 236/1989).

### Cosa fare
- Fornire i valori minimi (altezze, superfici, aeroilluminazione, temperatura, servizi) del DM 5/7/1975, sempre
  con rinvio all'articolo.

## Aggiornamento delle fonti

DM: se il PDF GU cambia (nuova scansione) riscaricare, ricalcolare l'hash con doppio download e rileggere via
immagine (GURITEL). Verificare le costanti (2,70/2,40/2,55 m art. 1; 14+10 e 9/14 mq art. 2; 28/38 mq art. 3;
18-20 °C art. 4; 2% e 1/8 art. 5). La fonte è il testo del 1975; eventuali norme regionali/deroghe vanno
segnalate come contesto, non riscritte.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico comunale/ASL o progettista edile).

## Stato attuale

- Versione: 0.1.0-alpha (closes #452)
- Task files: 2 (`verifica-altezze-superfici-minime.md`, `verifica-aeroilluminazione-servizi-impianti.md`)
- Esempi: 2 (verifica di altezze e superfici di un alloggio; verifica del rapporto aeroilluminante 1/8 e
  dell'altezza del bagno)
