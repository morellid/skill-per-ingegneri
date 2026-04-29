# AGENTS.md - modulistica-edilizia-unificata

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

La skill copre la **scelta del modulo edilizio nazionale unificato** (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / Permesso di Costruire / Sanatoria art. 36 / Sanatoria semplificata art. 36-bis) per un intervento edilizio in Italia, e la **mappa degli allegati** richiesti dal modulo. Riferimento principale: **DPR 380/2001** + **D.Lgs. 222/2016 Tabella A sezione II Edilizia**, integrato dalle modifiche del **Salva Casa** (DL 69/2024 conv. L. 105/2024) e dalla modulistica nazionale unificata aggiornata in Conferenza Unificata il **27/3/2025**.

Target utente: **ingegneri edili**, **architetti**, **geometri**, **tecnici dello sportello SUE/SUAP**, **professionisti** che assistono privati/imprese nella presentazione di pratiche edilizie.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **DPR 380/2001** (id `dpr-380-2001-testo-unico-edilizia`) - versione multivigente Normattiva (incorpora Salva Casa)
- **D.Lgs. 222/2016** (id `dlgs-222-2016-scia-2-tabella-a`) - SCIA 2, Tabella A sezione II Edilizia
- **DL 69/2024 conv. L. 105/2024** (id `dl-69-2024-salva-casa`) - Salva Casa
- **Modulistica unificata Salva Casa 27/3/2025** (id `modulistica-unificata-salva-casa-2025`) - Funzione Pubblica
- **Portale Normattiva DPR 380** (id `normattiva-portale-dpr-380`) - per cross-check vigenza articoli

Estratti pertinenti gia' preparati in `references/estratti/`:
- `dpr-380-2001-regimi-edilizi.md` - artt. 3, 6, 6-bis, 9-bis, 10, 22, 23, 23-ter, 34-bis, 36, 36-bis
- `dlgs-222-2016-tabella-a.md` - struttura Tabella A sezione II Edilizia
- `dl-69-2024-salva-casa.md` - sintesi delle modifiche Salva Casa
- `modulistica-unificata-2025.md` - struttura dei moduli unificati e allegati ricorrenti

## Articoli e punti chiave

Quando l'agent produce output, **cita sempre l'articolo preciso** (DPR 380 e/o voce Tabella A D.Lgs. 222/2016), non il decreto in generale. Riferimenti piu' frequenti:

- **DPR 380 art. 3 co. 1**: definizioni delle 6 tipologie di intervento (lett. a-f)
- **DPR 380 art. 6**: edilizia libera (post Salva Casa: VEPA, tende, pergolati, cappotto)
- **DPR 380 art. 6-bis**: CILA (regime residuale)
- **DPR 380 art. 9-bis co. 1-bis e 1-ter**: stato legittimo (pre-requisito di tutti i moduli)
- **DPR 380 art. 10 co. 1 lett. a/b/c**: PdC (nuova costruzione, ristrutturazione urbanistica, ristrutturazione edilizia "pesante")
- **DPR 380 art. 22**: SCIA
- **DPR 380 art. 23 co. 01**: SCIA alternativa al PdC
- **DPR 380 art. 23-ter**: cambio destinazione d'uso (5 categorie funzionali, post Salva Casa ampliato)
- **DPR 380 art. 34-bis**: tolleranze costruttive (post Salva Casa: % variabile per SU + tolleranze esecutive)
- **DPR 380 art. 36**: sanatoria con doppia conformita' piena
- **DPR 380 art. 36-bis**: sanatoria semplificata con doppia conformita' alleggerita (Salva Casa)
- **D.Lgs. 222/2016 Tabella A sez. II**: mapping intervento -> regime
- **D.Lgs. 81/2008 art. 99 + Allegato XV**: notifica preliminare cantiere e PSC (allegati ricorrenti dei moduli)
- **D.Lgs. 42/2004 art. 21 + 146**: autorizzazione MiC (beni culturali) e paesaggistica
- **DPR 31/2017 All. A/B**: interventi liberalizzati o semplificati ai fini paesaggistici

## Convenzioni specifiche

### Cosa NON fare

- **Non confondere SCIA (art. 22) e SCIA alternativa al PdC (art. 23)**: sono regimi distinti, con diversi termini di inizio lavori (immediato vs 30 gg) e diverse sanzioni. La SCIA alternativa si applica SOLO ai casi che richiederebbero PdC (art. 23 co. 01).
- **Non confondere art. 36, art. 36-bis e art. 6-bis co. 5**: art. 36 per assenza/totale difformita' da PdC o SCIA alternativa (doppia conformita' piena); art. 36-bis (post Salva Casa) per parziali difformita' art. 34, variazioni essenziali art. 32 e abusi del regime SCIA art. 22 (regime art. 37, doppia conformita' alleggerita); art. 6-bis co. 5 (sanzione pecuniaria) per CILA omessa.
- **Non emettere giudizi di "conformita' urbanistica"**: la conformita' al PRG/PUC e al regolamento edilizio e' giudizio del tecnico abilitato + verifica del SUE. La skill segnala l'obbligo, non lo verifica.
- **Non assumere che il regolamento edilizio comunale coincida con il nazionale**: i Comuni possono integrare (es. soglia pertinenze ridotta, vincolo coloristico, dotazione standard).
- **Non integrare automaticamente le leggi regionali** (recupero sottotetti, paesaggio, distanze): la skill cita il regime nazionale e rinvia alla LR.
- **Non confondere "stato legittimo" con "regolarita' catastale"**: lo stato legittimo (art. 9-bis) e' urbanistico-edilizio; la regolarita' catastale (Pregeo/Docfa) e' separata.
- **Non applicare il Salva Casa retroattivamente in modo automatico**: il regime transitorio e i contenziosi pendenti vanno valutati caso per caso. La skill cita il principio (la legge si applica dalla sua entrata in vigore) ma segnala il rinvio al SUE per le pratiche pendenti.

### Cosa fare

- **Cita sempre articolo + comma + lettera** del DPR 380 (es. "art. 10 co. 1 lett. c") + voce della Tabella A D.Lgs. 222/2016 quando applicabile.
- **Distingui sempre "obbligatorieta' assoluta" vs "condizionale"** per ogni allegato (es. notifica preliminare obbligatoria solo se cantiere multiimpresa o sopra soglia D.Lgs. 81).
- **Inquadra l'intervento prima di rispondere**: tipologia (art. 3), immobile esistente o nuovo, parti strutturali coinvolte, cambio destinazione, vincoli sovraordinati, zona urbanistica.
- **Per ogni regime proposto**, indica l'**articolo del DPR 380** e la **voce/sezione della Tabella A**, oltre al **modulo unificato corrispondente** della modulistica 2025.
- **Per il Salva Casa**, segnala sempre se la modifica e' rilevante per il caso in esame (es. nuova soglia tolleranza per immobile da 80 mq SU = 5%).
- **Per ogni modulo**, fornisci elenco allegati strutturato in: sempre obbligatori / condizionali (con condizione esplicita) / facoltativi.
- **Concludi sempre l'output** con: (a) elementi non automaticamente verificabili dalla skill, (b) rinvio allo sportello SUE / tecnico abilitato.

## Validatori

- Da identificare per Livello 2 validation. Profilo richiesto: **ingegnere edile / architetto / geometra** con esperienza diretta su pratiche edilizie post Salva Casa, oppure **operatore SUE/SUAP comunale**. Validazione tipica: 10 interventi reali, confronto modulo proposto dalla skill vs scelta corretta dello sportello SUE.

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1 (autore-driven, fonti pubbliche)
- Task files:
  - `determina-regime-edilizio.md`
  - `genera-elenco-allegati.md`
  - `verifica-salva-casa.md`
- Esempi: 1 caso CILA/SCIA borderline + 1 cambio destinazione d'uso post Salva Casa + 1 sanatoria semplificata art. 36-bis
