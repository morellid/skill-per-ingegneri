# AGENTS.md - pfte-allegato-i7-checker

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **verifica di completezza documentale** dei due livelli di progettazione delle opere pubbliche italiane previsti dal D.Lgs. 31 marzo 2023 n. 36 (Codice dei contratti pubblici): **PFTE** (Progetto di Fattibilita' Tecnico-Economica) e **progetto esecutivo**. Riferimento principale: **art. 41 + Allegato I.7** del Codice, integrato dal correttivo **D.Lgs. 209/2024**. Target utente: **ingegneri civili**, **RUP**, **stazioni appaltanti**, **studi professionali** che lavorano su appalti pubblici di lavori, servizi e forniture.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **D.Lgs. 36/2023** (id `dlgs-36-2023-originale-gu-2023`) - GU n. 87 del 13/04/2023 SO n. 14
- **D.Lgs. 209/2024** correttivo (id `dlgs-209-2024-correttivo-gu-2025`) - GU n. 17 del 22/01/2025 SO
- **Portale Normattiva** (id `normattiva-portale-dlgs-36`) - per cross-check vigenza articoli

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dlgs-36-art-41.md` - testo strutturato art. 41 (commi 1-15-quater)
- `allegato-i7-pfte.md` - struttura Allegato I.7 + elenco elaborati PFTE (art. 6 co. 7)
- `allegato-i7-esecutivo.md` - elaborati progetto esecutivo (art. 22 co. 4)
- `dlgs-209-2024-modifiche.md` - modifiche del correttivo

## Articoli e punti chiave

Quando l'agent produce output, **cita sempre l'articolo preciso**, non il decreto in generale. Riferimenti piu' frequenti:

- **Art. 41 co. 1** D.Lgs. 36/2023: due livelli di progettazione (PFTE + esecutivo)
- **Art. 41 co. 5 / 5-bis**: regimi alternativi per manutenzioni
- **Art. 41 co. 7**: PFTE sostituisce preliminare + definitivo per varianti urbanistiche
- **Art. 41 co. 8**: coerenza esecutivo / PFTE
- **Art. 41 co. 14**: scorporo costo manodopera
- **Allegato I.7 art. 1**: quadro esigenziale
- **Allegato I.7 art. 2 co. 5-6**: DOCFAP (obbligatorio sopra soglia europea art. 14; facoltativo per importi 150.001 EUR - soglia europea)
- **Allegato I.7 art. 3**: documento di indirizzo alla progettazione (DIP)
- **Allegato I.7 art. 6 co. 7**: elenco elaborati PFTE (lett. a-t)
- **Allegato I.7 art. 7-20**: contenuto dei singoli elaborati PFTE
- **Allegato I.7 art. 21**: appalto su PFTE (appalto integrato) - elaborati aggiuntivi
- **Allegato I.7 art. 22 co. 4**: elenco elaborati progetto esecutivo (lett. a-p)
- **D.Lgs. 81/2008 Allegato XVI**: fascicolo dell'opera (richiamato da art. 22 lett. p)

## Convenzioni specifiche

### Cosa NON fare
- **Non confondere il PFTE con il vecchio progetto definitivo** del D.Lgs. 50/2016: il D.Lgs. 36/2023 ha eliminato il livello "definitivo".
- **Non applicare l'Allegato I.7 a contratti pre-1 luglio 2023**: per quelle procedure vale il D.Lgs. 50/2016 + DPR 207/2010 (regime transitorio - rinvio al RUP).
- **Non valutare l'adeguatezza tecnica** dei contenuti dei singoli elaborati: questa e' competenza del progettista firmatario e, dove ricorra, del verificatore ex art. 42.
- **Non emettere giudizi di "conformita'"**: emettere un esito strutturato (completo / incompleto / dubbio per ciascun elaborato) e rinviare alla verifica professionale.
- **Non confondere "verifica di completezza" (skill)** con **"verifica della progettazione" ex art. 42** (verificatore qualificato): sono due adempimenti distinti.
- **Non includere elaborati non previsti** dall'Allegato I.7 senza inquadramento normativo (es. relazione paesaggistica DPR 31/2017 puo' essere richiesta ma e' al di fuori del Codice contratti).

### Cosa fare
- **Cita sempre articolo + comma + lettera** dell'Allegato I.7 (es. "art. 6 co. 7 lett. h"), non il numero d'ordine generico nell'elenco.
- **Distingui sempre obbligatorieta' assoluta vs condizionale** (es. piano espropri solo se necessarie procedure espropriative).
- **Inquadra l'intervento prima di rispondere**: tipologia, importo, espropri, VIA, BIM, modalita' di affidamento, regime manutenzione. Senza questi dati la checklist non puo' essere accurata.
- **Per il PFTE post-correttivo (2025+)**, applica le modifiche del D.Lgs. 209/2024 (vedi estratto).
- **Per ogni elaborato segnalato come mancante**, indica l'articolo dell'Allegato I.7 che lo richiede e l'eventuale eccezione applicabile.
- Concludi sempre l'output con: (a) elementi non automaticamente verificabili dalla skill, (b) rinvio al progettista firmatario e al verificatore ex art. 42 dove ricorra.

## Validatori

- Da identificare per Livello 2 validation. Profilo richiesto: ingegnere civile / RUP con esperienza diretta su procedure di affidamento post D.Lgs. 36/2023.

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1 (autore-driven, fonti pubbliche)
- Task files:
  - `genera-checklist-pfte.md`
  - `verifica-completezza-pfte.md`
  - `verifica-coerenza-esecutivo.md`
- Esempi: 1 conforme + 1 incompleto (PFTE), oltre eventuali manutenzioni e appalto integrato
