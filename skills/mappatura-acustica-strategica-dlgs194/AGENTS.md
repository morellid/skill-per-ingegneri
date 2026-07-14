# AGENTS.md - mappatura-acustica-strategica-dlgs194

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi di **mappatura acustica strategica** e **piani
d'azione** contro il rumore ambientale ai sensi del D.Lgs. 194/2005 (attuazione
della direttiva 2002/49/CE - END). Target: enti locali/regioni, gestori di
infrastrutture di trasporto, ingegneri e consulenti acustici/ambientali.

**E' una skill documentale**: non produce mappe/piani, non esegue modellazione
acustica, non riproduce gli allegati tecnici.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-194-2005**: D.Lgs. 19/8/2005 n. 194, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile 02f5432f...,
  pattern della skill aua-dpr59-dossier). Articoli 1-11 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dlgs-194-2005.md`.

Estratto operativo: `references/estratti/mappatura-acustica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Soglie** (art. 2): agglomerato **> 100.000 ab.**; aeroporto **> 50.000
  movimenti/anno**; asse ferroviario **> 30.000 treni/anno**; asse stradale **>
  3.000.000 veicoli/anno**. Prima tornata (art. 3 c. 1): agglomerati > 250.000;
  strade > 6.000.000; ferrovie > 60.000.
- **Soggetti** (artt. 3-4): autorita' regionale per gli agglomerati; gestori per
  le infrastrutture; Ministero dell'ambiente per le infrastrutture nazionali/
  multiregionali.
- **Deliverable**: mappa acustica strategica/mappatura (art. 3, all. 4, dati all.
  6) e piano d'azione (art. 4, all. 5).
- **Scadenze quinquennali**: mappe 30/6/2007 -> 30/6/2017 -> 31/3/2022 -> ogni 5
  anni; piani 18/7/2008 -> 18/7/2018 -> 18/4/2024 -> ogni 5 anni; riesame mappe
  almeno ogni 5 anni; riesame piani per sviluppi sostanziali.
- **Descrittori** Lden/Lnight (art. 5, all. 1); metodi (art. 6, all. 2-3;
  CNOSSOS-EU dir. (UE) 2015/996 a livello UE, non riprodotto).
- **Informazione del pubblico** (art. 8): accessibilita' (D.Lgs. 195/2005); avviso
  pubblico e **45 giorni** di osservazioni per i piani.
- **Sanzioni** (art. 11): fino a **180.000 euro/mese di ritardo** per mappe/piani
  mancanti; 2.000-12.000 (requisiti minimi); 5.000-30.000 (comunicazioni).

## Convenzioni specifiche

### Cosa NON fare
- Non produrre mappe/piani ne' eseguire la modellazione acustica (Lden/Lnight).
- Non riprodurre gli allegati 1-6 (contenuto tecnico esteso, in parte immagini):
  citarli come esistenza e oggetto.
- Non citare "a memoria" le soglie/scadenze: citare sempre l'articolo (artt.
  1-11).
- Non confondere la soglia della prima tornata con quella a regime.
- Non confondere il D.Lgs. 194/2005 (rumore strategico) con la L. 447/1995
  (inquinamento acustico ordinario): distinguere e rinviare.

### Cosa fare
- Citare l'articolo preciso per ogni soglia/scadenza/adempimento.
- Distinguere soggetto obbligato per tipo di elemento.
- Segnalare le sanzioni dell'art. 11.
- Chiudere con il rinvio all'autorita' competente e al tecnico acustico.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati (art. 4 e' in vigore dal 30-12-2022).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con tecnico acustico / ente
  competente).

## Stato attuale

- Versione: 0.1.0-alpha (closes #40)
- Task files: 2 (`diagnosi-applicabilita.md`, `checklist-adempimenti.md`)
- Esempi: 2 (agglomerato 150.000 ab. - soggetto; asse stradale 2 mln veicoli/anno
  - sotto soglia)
