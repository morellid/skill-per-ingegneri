# AGENTS.md - stabilita-pendii-naturali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico** e al **geologo** per l'**inquadramento dello studio e della
verifica di stabilita' dei pendii naturali** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.3**:
prescrizioni e indagini, modellazione geologica e geotecnica, verifica di sicurezza, interventi di
stabilizzazione e monitoraggio. Target: ingegneri geotecnici e geologi.

**E' una skill documentale per il tecnico**: fornisce i criteri e la definizione della verifica (coefficiente
di sicurezza F = tau_f/tau su valori caratteristici), i criteri di scelta delle superfici (accertate per i
pendii in frana, ricerca della superficie critica negli altri casi) e le regole di monitoraggio (soglie di
attenzione/allarme); **non calcola** il coefficiente di sicurezza, **non definisce** il modello
geologico/geotecnico e **non progetta** gli interventi.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `opere-sostegno-ntc` (§6.5), `tiranti-ancoraggio-ntc` (§6.6) e
`relazione-geologica-geotecnica-ntc` (che esplicitamente esclude i §6.3-6.12). La distinzione ancorata al testo
e' che, a differenza di muri, fondazioni e tiranti (che usano i coefficienti parziali A1/A2, M ed R), la
verifica di stabilita' dei pendii naturali usa il **coefficiente di sicurezza globale F = tau_f/tau** con
parametri e azioni al **valore caratteristico**. Condivide con le altre skill NTC la stessa fonte (PDF GU del
S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope la stabilita' sismica (§7.11.3.5) e le opere in materiali
sciolti / fronti di scavo (§6.8).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-3**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 6.3 estratto con `pdftotext -layout` (pp. GU 187-188) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-3.md`; estratto operativo in
`references/estratti/stabilita-pendii-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (§6.3): pendii naturali, anche in **condizioni sismiche** (rinvio §7.11.3.5); progetto/esecuzione/
  controllo degli interventi di stabilizzazione.
- **Prescrizioni e indagini** (§6.3.1): osservazioni e rilievi di superficie, notizie storiche, movimenti in
  atto, dati idrogeologici/pluviometrici; verifiche basate su **specifiche indagini geotecniche**.
- **Modellazione** (§6.3.2-6.3.3): modello **geologico** e **geotecnico** (rilievo plano-altimetrico esteso a
  monte e valle, successione stratigrafica, pressioni interstiziali, superficie/i di scorrimento, numero minimo
  di verticali, modello geotecnico di sottosuolo §6.2.2).
- **Verifica** (§6.3.4): coefficiente di sicurezza **F = tau_f/tau** (resistenza al taglio disponibile /
  tensione di taglio agente) lungo la superficie di scorrimento, con parametri e azioni al **valore
  caratteristico** (NON i coefficienti parziali A1/A2, M, R). Pendii **in frana** → superfici accertate;
  **altri casi** → ricerca della **superficie critica** (grado di sicurezza piu' basso); pressioni interstiziali
  nelle **condizioni piu' sfavorevoli**; margine **giustificato dal progettista**.
- **Interventi/monitoraggio** (§6.3.5-6.3.6): entita' del miglioramento e altri meccanismi di collasso;
  monitoraggio di spostamenti e pressioni interstiziali, **soglie di attenzione e di allarme**.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** il coefficiente di sicurezza né **eseguire** le verifiche (equilibrio limite/metodi
  numerici); non **definire** il modello geologico/geotecnico né **progettare** gli interventi di
  stabilizzazione.
- Non **trattare** la stabilita' dei pendii in **condizioni sismiche** (§7.11.3.5) né le **opere in materiali
  sciolti / fronti di scavo** (§6.8); non **riprodurre** la Circolare 21/1/2019 n. 7.

### Cosa fare
- Fornire i criteri, la definizione della verifica (F = tau_f/tau su valori caratteristici), i criteri di scelta
  delle superfici e le regole di monitoraggio, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.3. Verificare la definizione F = tau_f/tau, i criteri delle superfici
(accertate/critica) e il rinvio alla stabilita' sismica (§7.11.3.5).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico/geologo).

## Stato attuale

- Versione: 0.1.0-alpha (closes #409)
- Task files: 2 (`inquadra-verifica-stabilita-pendio.md`, `inquadra-indagini-interventi-monitoraggio.md`)
- Esempi: 2 (coefficiente di sicurezza F = tau_f/tau su valori caratteristici; scelta delle superfici di
  scorrimento per pendio in frana e pendio non in frana)
