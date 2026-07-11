# AGENTS.md - relazione-geologica-geotecnica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Verifica documentale (completezza e coerenza) della relazione geologica e
della relazione geotecnica richieste dalle NTC 2018 (DM 17/01/2018, cap. 6)
e dalla Circolare applicativa 7/2019, piu' la stesura dell'indice commentato
di una relazione geotecnica. Target: ingegneri civili progettisti, geologi,
collaudatori statici.

## Fonti autoritative

Catalogate in `references/sources.yaml`, trascritte in `references/fonti/`:

- **NTC 2018** (DM 17/01/2018, GU n. 42/2018 SO n. 8) - sha256
  `dda1e397...05a46` - parr. 6.1-6.2.6
- **Circolare C.S.LL.PP. 7/2019** (GU n. 35/2019 SO n. 5) - sha256
  `f7c3b8d1...aed7c` - C6 intro, C6.2-C6.2.4.3, C9.1 lett. g, C10.1

Estratti operativi in `references/estratti/`:
- `ntc2018-cap6-relazioni.md` - obblighi, definizioni, verifiche (DM)
- `circ-7-2019-c6-relazioni.md` - contenuti delle due relazioni (Circolare)
- `circ-7-2019-c9-c10-ruoli-elaborati.md` - ruoli, firme, elaborati

## Punti normativi chiave

- **NTC par. 6.1.2**: obbligo delle due relazioni; contenuto minimo della
  relazione geotecnica.
- **NTC par. 6.2.1**: modello geologico; relazione geologica parte
  integrante del progetto.
- **NTC par. 6.2.2**: volume significativo, modello geotecnico, valori
  caratteristici; responsabilita' del progettista; laboratori ex art. 59
  DPR 380/2001; deroga per opere di modesta rilevanza.
- **NTC parr. 6.2.4-6.2.6**: verifiche SLU/SLE, metodo osservazionale,
  monitoraggio (programma illustrato nella relazione geotecnica).
- **Circ. C6.2.1**: sei aspetti e elaborati grafici della relazione
  geologica; nota 1 su ruoli e distinzione tra indagini.
- **Circ. C6.2.2.5**: dodici contenuti indicativi e corredo della relazione
  geotecnica.
- **Circ. C9.1 lett. g**: relazione geologica "redatta da un Geologo",
  geotecnica "redatta dal Progettista", certificati di laboratorio.
- **Circ. C10.1**: relazioni specialistiche; modello strutturale "correlato
  con quello geotecnico" nella relazione di calcolo.

## Convenzioni specifiche

### Cosa NON fare
- Non eseguire o rifare calcoli geotecnici (portanza, cedimenti,
  stabilita'): NTC parr. 6.3-6.11 sono fuori scope e non trascritti.
- Non citare valori dei coefficienti parziali (Tabb. 6.2.I-6.2.III NTC):
  non sono trascritti nelle fonti della skill.
- Non trattare l'elenco C6.2.2.5 come obbligatorio: e' dichiarato
  indicativo e modulato su fase e tipo di opera.
- Non attribuire alla Circolare valore cogente pari al DM: e' strumento
  applicativo.

### Cosa fare
- Citare sempre il paragrafo preciso (es. "NTC par. 6.2.2", "Circ. C6.2.2.5"),
  mai "le NTC" in generale.
- Distinguere gli esiti: assenza di contenuto minimo del DM (par. 6.1.2) =
  carenza; assenza di voce indicativa della Circolare = da motivare.
- Chiudere ogni output con il rinvio al professionista firmatario.

## Validatori

- Nessuno identificato per Livello 2 (da individuare: ingegnere geotecnico
  o geologo terzo rispetto all'autore).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha)
- Validazione: Livello 1 (self-check + review adversariale)
- Task files: check-relazione-geologica, check-relazione-geotecnica,
  check-coerenza-geologica-geotecnica, draft-struttura-relazione-geotecnica
- Esempi: 1 conforme + 1 problematico
