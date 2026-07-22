# AGENTS.md - criteri-modellazione-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento dei criteri di modellazione della
struttura e dell'azione sismica** ai fini della progettazione sismica secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 7.2.6**. Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce i criteri di modellazione (modello 3D, rigidezza fessurata,
orizzontamenti rigidi, elementi non strutturali, eccentricità accidentale, limiti per RSL/ITS); **non costruisce**
il modello, **non esegue** l'analisi e **non determina** q.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `regolarita-strutturale-sismica-ntc` (§7.2.1),
`spostamenti-interpiano-sld-ntc` (§7.3.6.1), `periodo-proprio-t1-ntc` (§7.3.3.2) e `spettro-risposta-ntc` (§3.2).
E' **distinta**: nessuna di queste tratta i criteri di modellazione del §7.2.6. Condivide con le altre skill NTC
la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope i metodi di analisi (§7.3), la
risposta sismica locale (§3.2.3.6) e le fondazioni miste (§6.4.3).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-2-6**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.2.6 estratto con `pdftotext -layout` (pp. GU 214-215) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-7-2-6.md`; estratto operativo in
`references/estratti/modellazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Struttura** (§7.2.6): modello **tridimensionale**; leggi costitutive **elastiche** per comportamento non
  dissipativo o dissipativo con q; **rigidezza fessurata** riducibile **sino al 50%** di quella non fessurata
  (muratura, c.a., acciaio-cls); **orizzontamenti infinitamente rigidi** se c.a., latero-cemento con soletta c.a.
  >= 40 mm o mista con soletta c.a. >= 50 mm con connettori a taglio; **elementi non strutturali** non
  collaboranti (tamponature, tramezzi) **solo in massa** (rigidezza/resistenza solo se effetti negativi).
- **Azione sismica** (§7.2.6): forze statiche equivalenti, spettri o storie temporali; con **RSL/interazione
  terreno-struttura** lo spettro (5% smorzamento) **>= 70%** di quello per sottosuolo A e taglio/normale alla
  fondazione **>= 70%** di quello a base fissa; divieto di storie temporali artificiali (§3.2.3.6); **eccentricità
  accidentale** **>= 0,05** x dimensione media perpendicolare all'azione, **costante** su tutti gli
  orizzontamenti.

## Convenzioni specifiche

### Cosa NON fare
- Non **costruire** il modello ne' **eseguire** l'analisi (§7.3); non **determinare** q.
- Non **trattare** la risposta sismica locale (§3.2.3.6) ne' le fondazioni miste (§6.4.3).

### Cosa fare
- Fornire i criteri di modellazione (struttura e azione sismica) con le costanti (50%, 40/50 mm, 70%, 0,05),
  sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 7.2.6. Verificare le costanti (rigidezza fessurata sino al 50%; solette 40/50
mm; limiti 70% con 5% di smorzamento; eccentricità accidentale >= 0,05 della dimensione media).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #423)
- Task files: 2 (`inquadra-modellazione-struttura.md`, `inquadra-modellazione-azione-sismica.md`)
- Esempi: 2 (rigidezza fessurata e orizzontamenti di un telaio in c.a.; eccentricità accidentale di un edificio
  rettangolare)
