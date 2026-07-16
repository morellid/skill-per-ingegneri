# AGENTS.md - duvri-interferenze-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli **obblighi del committente negli appalti/contratti d'opera** e
alla redazione del **DUVRI** (Documento Unico di Valutazione dei Rischi da Interferenze)
ai sensi dell'**art. 26 D.Lgs 81/2008**. Target: datori di lavoro committenti, RSPP,
consulenti sicurezza.

**E' una skill documentale**: inquadra obblighi, esclusioni e contenuti; **non valuta i
rischi specifici** dell'appaltatore, **non quantifica i costi** e **non copre i cantieri
Titolo IV**.

## Area di catalogo

`sicurezza-lavoro-cantieri`. Complementare a `dvr-generico` (art. 28-29, DVR del datore di
lavoro) e a `pos-allegato-xv-checker` (cantieri Titolo IV, PSC/POS): l'art. 26 riguarda gli
appalti "interni" NON cantiere.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-art26**: D.Lgs. 81/2008 art. 26, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash d8991985...; codice 008G0104). Articolo caricato via AJAX
  (caricaArticolo, idGruppo=3) e trascritto verbatim in
  `references/fonti/dlgs-81-art-26.md`. Estratto in
  `references/estratti/duvri-checklist.md`.

## Punti chiave (verificati sul testo)

- **c.1**: verifica idoneita' tecnico-professionale (certificato camerale +
  autocertificazione art. 47 DPR 445/2000); informazione sui rischi specifici e sulle
  misure di emergenza.
- **c.2**: cooperazione e coordinamento tra i datori di lavoro (compresi subappaltatori).
- **c.3**: il committente elabora il **DUVRI** (misure per eliminare/ridurre i rischi da
  interferenza), allegato al contratto e aggiornato; accesso RLS/OO.SS.; NON riguarda i
  rischi specifici propri dell'appaltatore; alternativa dell'incaricato nei settori a
  basso rischio (art. 29 c.6-ter).
- **c.3-bis**: esclusioni (servizi intellettuali, mere forniture, <= 5 uomini-giorno) salvo
  rischi cancerogeni/biologici/esplosione/particolari.
- **c.5**: costi delle misure da interferenza, **non soggetti a ribasso** (nei pubblici,
  quantificati dalla stazione appaltante).
- **c.8**: tessera di riconoscimento; responsabilita' solidale committente/appaltatore.

## Convenzioni specifiche

### Cosa NON fare
- Non **valutare i rischi specifici** dell'appaltatore (restano nel suo DVR).
- Non **quantificare** i costi della sicurezza.
- Non trattare i **cantieri edili Titolo IV** (PSC/POS -> `pos-allegato-xv-checker`).
- Non confondere il DUVRI (art. 26) con il **DVR** del datore di lavoro (art. 28-29 ->
  `dvr-generico`).

### Cosa fare
- Impostare verifica idoneita' e informazione (c.1), cooperazione/coordinamento (c.2), la
  determinazione "DUVRI dovuto/non dovuto" e i contenuti (c.3, 3-bis), i costi (c.5).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs 81/2008 pinnato a un nuovo `!vig=` (nuovo hash)
e rileggere l'art. 26 (attenzione alle versioni per articolo e agli aggiornamenti).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP / esperto sicurezza sul lavoro).

## Stato attuale

- Versione: 0.1.0-alpha (closes #241)
- Task files: 2 (`verifica-idoneita-e-informazione.md`, `imposta-duvri.md`)
- Esempi: 2 (pulizie in stabilimento - DUVRI dovuto; mera fornitura - esclusione e limite)
