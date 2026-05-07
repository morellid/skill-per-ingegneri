# AGENTS.md - valutazione-cem-srb-art-87-cce

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill di supporto al tecnico/ingegnere che predispone o revisiona la pratica autorizzativa di una infrastruttura per impianto radioelettrico (SRB GSM/UMTS/LTE/5G NR FR1, ripetitore, ponte radio, rete a radiofrequenza in banda 100 kHz - 300 GHz) ai sensi dell'**art. 87 D.Lgs. 1 agosto 2003 n. 259** (Codice delle comunicazioni elettroniche - CCE), comprensiva della **valutazione predittiva CEM** allegata, redatta ai limiti del **DPCM 8 luglio 2003** con modelli predittivi conformi alla **norma CEI 211-7**. Target: ingegnere TLC, tecnico operatore, consulente CEM, validatore ARPA-side.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **D.Lgs. 259/2003 - Codice comunicazioni elettroniche, testo MIMIT** (id `dlgs-259-2003-cce-mimit`) - sha256 `476b36ffc3bf045cefadb0a6c53e6b3ab58844946c6e05c4ac6487f632c5e9d8`. Riflette il testo aggiornato fino al 2013-2014.
- **DPCM 8 luglio 2003 - limiti CEM 100 kHz - 300 GHz** (id `dpcm-8-7-2003-cem`) - sha256 `362144b32d12e0bd473f87b7a47364ed325ef0a8465285b703e38661cd32bb83`. Pubblicato in GU Serie Generale n. 199 del 28 agosto 2003. Tabelle 1, 2, 3 Allegato B in formato immagine, NON estraibili come testo.
- **L. 22 febbraio 2001 n. 36 - legge quadro CEM** (id `legge-36-2001-quadro-cem`) - sha256 `7e705e7fc62b91a4b7296ffd714b2d3df5379615f9bc436337f957744d309f3f`. Testo solo come immagine in GU; usata strutturalmente, non quotata.

Estratti in `references/estratti/`:
- `dlgs-259-2003-art-87.md` - art. 87 commi 1-10 + 3-bis con sintesi operativa.
- `dpcm-8-7-2003-limiti-cem.md` - DPCM 8/7/2003 art. 1-7 + rinvio strutturale ad Allegati A, B, C.

## Articoli e punti chiave (citare puntualmente)

- **art. 87 c. 1 D.Lgs. 259/2003**: autorizzazione Ente locale + accertamento di compatibilita' a cura ARPA/APPA ex art. 14 L. 36/2001.
- **art. 87 c. 2**: istanza all'Ente locale; indicazione del responsabile del procedimento.
- **art. 87 c. 3**: Modello A Allegato 13; modelli predittivi conformi alla CEI; **SCIA Modello B Allegato 13 per impianti UMTS od altre con potenza singola antenna <= 20 W**.
- **art. 87 c. 3-bis**: regime speciale GSM-R ferroviario (fuori scope skill).
- **art. 87 c. 4**: trasmissione contestuale ad ARPA + pronuncia ARPA entro 30 giorni.
- **art. 87 c. 5**: una sola richiesta integrazioni entro 15 giorni; sospensione termine c. 9.
- **art. 87 c. 6, 7**: conferenza di servizi, pronuncia entro 30 giorni dalla 1a convocazione, sostituisce gli atti delle singole Amministrazioni.
- **art. 87 c. 8**: dissenso qualificato (ambiente/salute/patrimonio storico-artistico) -> rimessione al Consiglio dei Ministri.
- **art. 87 c. 9**: silenzio-assenso a 90 giorni dalla presentazione (salvo c. 8).
- **art. 87 c. 10**: realizzazione opere entro 12 mesi a pena di decadenza.
- **DPCM 8/7/2003 art. 3 c. 1** + Tabella 1 Allegato B: limiti di esposizione.
- **DPCM 8/7/2003 art. 3 c. 2** + Tabella 2 Allegato B: valori di attenzione (ambienti con permanenza >= 4 ore + pertinenze fruibili).
- **DPCM 8/7/2003 art. 3 c. 3** + **art. 4 c. 1 ultima parte**: mediazione su 6 minuti e su sezione verticale del corpo umano.
- **DPCM 8/7/2003 art. 4** + Tabella 3 Allegato B: obiettivi di qualita' (aree intensamente frequentate all'aperto).
- **DPCM 8/7/2003 art. 5** + Allegato C: somma dei contributi normalizzati < 1 (esposizioni multiple).
- **DPCM 8/7/2003 art. 6**: tecniche secondo norma CEI 211-7.

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre numeri delle Tabelle 1, 2, 3 Allegato B DPCM 8/7/2003: sono pubblicate come immagine in GU; rinviare strutturalmente alla riga di tabella applicabile.
- Non calcolare valori predetti di E (V/m), H (A/m), S (W/m^2): non e' compito della skill.
- Non confondere le tre famiglie di soglie: **limite di esposizione** (sempre), **valore di attenzione** (ambienti >= 4 h), **obiettivo di qualita'** (aree intensamente frequentate all'aperto).
- Non dare per vigente il testo della fonte MIMIT (2013-2014): rinviare sempre a Normattiva per modifiche post-2014 (D.L. 76/2020 conv. L. 120/2020, D.Lgs. 8 novembre 2021 n. 207).
- Non includere automaticamente impianti radar / esposizioni pulsate (DPCM dedicato, non DPCM 8/7/2003).
- Non gestire reti GSM-R ferroviarie (regime speciale art. 87 c. 3-bis).
- Non sostituire il parere tecnico ARPA (art. 87 c. 4).

### Cosa fare
- Citare sempre comma + articolo del D.Lgs. 259/2003 e del DPCM 8/7/2003.
- Distinguere sempre Modello A vs. Modello B in base alla potenza singola antenna <= 20 W.
- Per il co-siting, esigere il calcolo cumulativo ex DPCM art. 5 + Allegato C.
- Per la mediazione, esigere dichiarazione esplicita "6 minuti / sezione verticale del corpo umano".
- In presenza di scuole/ospedali nel volume di rispetto: segnalare rischio di dissenso qualificato art. 87 c. 8.
- Includere sempre nel report finale il rinvio al testo vigente su Normattiva.
- Mantenere il disclaimer di responsabilita' professionale.

## Validatori

- Da identificare per Livello 2 validation (ingegnere CEM ARPA-side o tecnico operatore mobile diverso dall'autore della skill).

## Stato attuale

- Versione: vedi `CHANGELOG.md` (0.1.0-alpha).
- Validazione: Livello 1 (validate.sh + adversarial review automatica).
- Task files: `check-completezza-istanza.md`, `mappa-iter-procedurale.md`, `checklist-relazione-cem.md`.
- Esempi: 1 conforme (`srb-lte-30w-conforme`) + 1 problematico (`srb-5g-bozza-incompleta`).
