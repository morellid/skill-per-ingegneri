# Valutazione CEM SRB - art. 87 CCE

> Versione: 0.1.0-alpha
> Stato: in sviluppo

Skill di supporto al tecnico/ingegnere che predispone o revisiona la pratica autorizzativa di un impianto radioelettrico (SRB GSM/UMTS/LTE/5G NR FR1, ripetitore, ponte radio) ai sensi dell'**art. 87 D.Lgs. 1 agosto 2003 n. 259** (Codice delle comunicazioni elettroniche), inclusa la valutazione predittiva CEM ai limiti del **DPCM 8 luglio 2003** con modelli predittivi conformi alla **norma CEI 211-7**.

## Target

- Ingegnere TLC che redige istanza Modello A Allegato 13 oppure SCIA Modello B Allegato 13 (impianti <= 20 W per singola antenna).
- Tecnico operatore mobile / consulente CEM che predispone documentazione di pratica.
- Validatore ARPA-side che riceve la pratica e ne verifica la completezza.

## Cosa fa

Tre sotto-attivita' (`tasks/`):

1. **Check completezza istanza/SCIA art. 87** (`check-completezza-istanza.md`): verifica della completezza della pratica art. 87 (modello A o B, documentazione tecnica, relazione predittiva CEM, asseverazione, trasmissione contestuale ARPA).
2. **Mappa iter procedurale** (`mappa-iter-procedurale.md`): timeline degli attori e delle tempistiche (Ente locale, ARPA 30 giorni, integrazioni 15 giorni, conferenza di servizi, silenzio-assenso 90 giorni, decadenza 12 mesi).
3. **Checklist relazione predittiva CEM** (`checklist-relazione-cem.md`): verifica che la relazione predittiva CEM contenga conformita' CEI 211-7, citazione delle Tabelle 1/2/3 Allegato B DPCM 8/7/2003, mediazione 6 minuti / sezione verticale, calcolo cumulativo per esposizioni multiple, asseverazione.

Per il dettaglio tecnico vedi `SKILL.md`.

## Installazione

Vedi `README.md` di repo (root) per le istruzioni di installazione delle skill in Claude Code (`~/.claude/skills/`) e in OpenAI Codex (`~/.agents/skills/`).

## Fonti consultate

- D.Lgs. 1 agosto 2003 n. 259 - Codice delle comunicazioni elettroniche - art. 87 (versione MIMIT consolidata 2013-2014).
- DPCM 8 luglio 2003 - limiti di esposizione, valori di attenzione, obiettivi di qualita' CEM 100 kHz - 300 GHz (GU Serie Generale n. 199 del 28 agosto 2003).
- L. 22 febbraio 2001 n. 36 - legge quadro CEM (riferimento strutturale, non quotata).

Dettaglio completo (URL, hash sha256, licenza, data accesso) in `references/sources.yaml`. Estratti testuali in `references/estratti/`.

## Limiti noti per v0.1.0-alpha

- **Tabelle 1, 2, 3 Allegato B DPCM 8/7/2003 NON riprodotte**: pubblicate come immagine in GU; la skill rinvia strutturalmente alla riga di tabella applicabile e demanda al firmatario la verifica dei valori numerici.
- **Modifiche post-2014 dell'art. 87**: non integrate automaticamente nella fonte MIMIT catalogata. Verificare il testo vigente su Normattiva (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-08-01;259) prima di ogni deposito.
- **Calcolo numerico CEM**: la skill non calcola V/m, A/m, W/m^2; demanda al software predittivo CEI 211-7 dell'utente.
- **Regimi speciali fuori scope**: GSM-R ferroviario (art. 87 c. 3-bis), impianti radar / esposizioni pulsate (DPCM dedicato), esposizioni dei lavoratori (D.Lgs. 81/2008 Titolo VIII Capo IV).
- **Validazione Livello 2** (ingegnere CEM diverso dall'autore) non ancora effettuata.

## Disclaimer

La skill e' uno strumento di supporto. **Non sostituisce il giudizio del professionista firmatario** (ingegnere abilitato, tecnico competente CEM) ne' il parere tecnico di ARPA (art. 14 L. 36/2001 richiamato dall'art. 87 c. 1 D.Lgs. 259/2003). L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
