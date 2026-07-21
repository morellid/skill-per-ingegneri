# AGENTS.md - azioni-urto-eccezionali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle azioni eccezionali da urto**
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.3 (Urti)**: classificazione, forze statiche
equivalenti e punti di applicazione per urti da traffico veicolare (sotto/sopra i ponti), ferroviario e (con
rinvio) di imbarcazioni/aeromobili. Target: ingegneri strutturisti e progettisti di ponti.

**E' una skill documentale per il tecnico**: fornisce le categorie (Tab. 3.6.II), le forze equivalenti (Tab.
3.6.III, formule [3.6.7]-[3.6.9]) e i punti/aree di applicazione; **non calcola** le sollecitazioni e **non
dimensiona/verifica** gli elementi o i sistemi di protezione.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Completa la famiglia delle **azioni eccezionali** (§3.6) insieme a
`resistenza-fuoco-strutture-ntc` (§3.6.1 Incendio). È **distinta** dalla skill `azioni-traffico-ponti-stradali-ntc`
(§5.1.3, azioni da traffico q1-q9): il §3.6.3 riguarda gli **urti accidentali** (azione eccezionale), non i
carichi da traffico ordinari. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U.
n. 42/2018). Restano fuori scope: il calcolo delle sollecitazioni e le verifiche, le analisi di rischio
(ferrovia), le procedure per imbarcazioni/aeromobili (Cap. 12) e le esplosioni (§3.6.2).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-3-6-3**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 3.6.3 estratto con `pdftotext -layout` (pp. 65-66) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-3-6-3.md`; estratto operativo in
`references/estratti/azioni-urto-checklist.md`.

## Punti chiave (verificati sul testo)

- **Classificazione** (Tab. 3.6.II): categorie 1/2/3; si applicano per categoria 2 e 3.
- **Sotto ponti** (§3.6.3.3.1): Fd,y = 0,50·Fd,x [3.6.7]; Tab. 3.6.III (1000/750/500/50/150 kN); applicazione a
  0,5 m (automobili) o 1,25 m.
- **Elementi orizzontali**: F = r·Fd,x [3.6.8], r = 1,0 fino a 5 m, 1,0→0 tra 5 e 6 m, 0 oltre 6 m.
- **Carrelli elevatori**: F = 5·W [3.6.9].
- **Sopra i ponti** (§3.6.3.3.2): 100 kN sugli elementi di sicurezza.
- **Ferroviario** (§3.6.3.4): 4000/1500 kN (d ≤ 5 m), 2000/750 kN (5 < d ≤ 15 m), 0 (d > 15 m), a 1,80 m dal
  piano del ferro.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le sollecitazioni né **dimensionare/verificare** gli elementi o i sistemi di protezione;
  non **scegliere** la categoria di azione al posto del progettista.
- Non **riprodurre** le analisi di rischio (ferrovia) né le procedure per imbarcazioni/aeromobili (Cap. 12);
  non **trattare** le esplosioni (§3.6.2) né l'incendio (§3.6.1, skill dedicata).

### Cosa fare
- Fornire categorie, forze statiche equivalenti (Tab. 3.6.III, formule [3.6.7]-[3.6.9]) e punti/aree di
  applicazione, sempre con rinvio al paragrafo/tabella/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 3.6.3. Verificare le forze (Tab. 3.6.III), il fattore r [3.6.8] e le forze
ferroviarie (4000/1500, 2000/750 kN).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista/progettista di ponti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #403)
- Task files: 2 (`inquadra-urti-traffico-veicolare.md`, `inquadra-urti-ferroviario-altri.md`)
- Esempi: 2 (urto su piedritto di cavalcavia autostradale; urto su elemento orizzontale con sottovia h=5,5 m)
