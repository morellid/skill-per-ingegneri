# Task: Elencazione e categorizzazione delle attivita' e dei servizi (art. 30 D.Lgs. 138/2024 + Det. ACN 155238/2026)

Prepara l'elenco categorizzato delle attivita' e dei servizi del soggetto NIS da comunicare all'ACN tramite il "Servizio NIS/Categorizzazione" entro la finestra annuale **1 maggio - 30 giugno**.

## Pre-requisito

Il soggetto deve essere in ambito NIS (esito "essenziale" o "importante" del task `valuta-perimetro`), essere iscritto sulla piattaforma ACN ai sensi dell'art. 7 D.Lgs. 138/2024 e aver ricevuto la prima comunicazione di inserimento nell'elenco ex art. 7 co. 3 lett. a).

L'obbligo si applica a **tutti i soggetti NIS** (essenziali e importanti) a partire dall'anno solare **2026** (art. 42 co. 2 D.Lgs. 138/2024). **Esenzione DORA**: le entita' finanziarie ex Reg. (UE) 2022/2554 in ambito NIS sono esentate dal processo di categorizzazione (art. 20 co. 6 Det. 127437/2026), salva adesione volontaria. Attenzione: e' l'opposto dell'elenco fornitori rilevanti, dove l'esenzione DORA non opera (task `elenco-fornitori-rilevanti`).

Questo adempimento e' **distinto** dall'elenco dei fornitori rilevanti NIS (finestra 15 aprile - 31 maggio, "Servizio NIS/Aggiornamento annuale informazioni"): oggetto, finestra e servizio di piattaforma sono diversi.

## Obiettivo

Produrre l'elenco categorizzato delle attivita' e dei servizi pronto per il caricamento sulla piattaforma ACN: per ogni attivita'/servizio la macro-area, la denominazione (descrizione opzionale) e la categoria di rilevanza, con la documentazione delle eventuali deroghe alle categorie pre-assegnate.

## Fonti

Leggere prima:
- `references/estratti/acn-det-155238-2026-categorizzazione.md` - Det. 155238/2026 (artt. 1-5, allegati 1-2), Guida alla lettura ACN, Det. 127437/2026 Capo V (artt. 20-21)
- `references/estratti/dlgs-138-2024-allegati-i-iv.md` - tipologie di soggetto degli allegati I, II e IV (per scegliere tra allegato 1 e allegato 2 del modello)

## Input richiesti

- **Tipologia di soggetto NIS** (numero e allegato del D.Lgs. 138/2024 in cui ricade, dall'esito di `valuta-perimetro`): determina quale allegato del modello si applica.
- **Mappa organizzativa**: organigramma, elenco delle funzioni e dei processi di business (per l'approccio top-down).
- **Inventario dei sistemi informativi e di rete**: apparati, applicazioni, servizi informatici in uso (per l'approccio bottom-up).
- **Analisi preesistenti riusabili** (se disponibili): analisi dei processi, catalogo dei servizi, valutazione del rischio, business impact analysis.
- **Perimetro PSNC**: eventuali attivita'/servizi soggetti agli obblighi del DL 105/2019 (perimetro di sicurezza nazionale cibernetica).
- **Per le PA**: eventuale classificazione dei dati e dei servizi gia' svolta ai sensi dell'art. 3 del DD ACN 21007/24 (Regolamento Cloud).

## Procedura

### Passo 0 - Verifica dei casi speciali che cambiano il modello

| Caso | Riferimento | Conseguenza |
|------|-------------|-------------|
| Il soggetto ha svolto la classificazione dati/servizi ex art. 3 DD ACN 21007/24 (Regolamento Cloud PA) | art. 4 Det. 155238/2026 | Si applica **quel** modello in luogo del modello di categorizzazione: l'elenco coincide con i dati/servizi digitali classificati e le categorie di rilevanza coincidono con le classi del Regolamento Cloud (ordinari, critici, strategici). Le modifiche devono restare coerenti con quella classificazione. Il resto di questo task non si applica |
| Attivita'/servizi con obblighi PSNC (DL 105/2019 conv. L. 133/2019) | art. 5 Det. 155238/2026 | Categoria **"impatto alto"** attribuita d'ufficio; tali attivita'/servizi **non sono oggetto dell'art. 3** (non si categorizzano con il modello). Escluderli dai passi successivi e riportarli direttamente nell'output |
| Entita' finanziaria DORA | art. 20 co. 6 Det. 127437/2026 | Esente dal processo, salva adesione volontaria. Se non aderisce, il task termina qui |

### Passo 1 - Verifica finestra temporale

La finestra annuale e' **1 maggio - 30 giugno** (art. 30 co. 1 D.Lgs. 138/2024; art. 20 co. 1 Det. 127437/2026). Prima applicazione: **2026** (art. 42 co. 2 D.Lgs. 138/2024; la Det. 155238/2026 e il Capo V della Det. 127437/2026 si applicano dal 1 maggio 2026).

**Nota operativa** (art. 20 co. 4-5 Det. 127437/2026): decorso il 30 giugno l'elenco si intende **definitivamente acquisito e non ulteriormente modificabile**; le sottomissioni tardive sono precluse, salvo documentate criticita' tecnico-operative non imputabili al soggetto. Pianificare la raccolta dati con anticipo rispetto alla chiusura della finestra.

### Passo 2 - Selezione dell'allegato del modello (art. 2 Det. 155238/2026)

| Tipologia di soggetto | Allegato del modello |
|----------------------|----------------------|
| Numeri 1, 2, 5, 6, 7 e 10 dell'allegato I; numeri 1, 2, 3, 4 e 5 dell'allegato II; numero 1 dell'allegato IV del D.Lgs. 138/2024 | **Allegato 1** (Logistica = impatto basso) |
| Tutte le altre tipologie | **Allegato 2** (Logistica = impatto minimo) |

I due allegati differiscono **solo** per la categoria pre-assegnata alla macro-area Logistica. Le 10 macro-aree e le altre pre-assegnazioni sono identiche:

| Macro-area | Categoria pre-assegnata |
|------------|--------------------------|
| Monitoraggio e controllo | Impatto alto |
| Produzione di beni e servizi | Impatto medio |
| Ricerca, sviluppo e progettazione | Impatto medio |
| Gestione finanziaria | Impatto basso |
| Gestione dei clienti | Impatto basso |
| Gestione delle risorse umane | Impatto basso |
| Logistica | Impatto basso (all. 1) / Impatto minimo (all. 2) |
| Comunicazione e marketing | Impatto minimo |
| Gestione amministrativa | Impatto minimo |
| Altri servizi e attivita' (residuale) | Impatto minimo |

Le descrizioni complete delle macro-aree sono in `references/fonti/acn-det-155238-2026-allegato-1.md` e `references/fonti/acn-det-155238-2026-allegato-2.md`.

### Passo 3 - Identificazione delle attivita' e dei servizi (Guida, cap. 2.2.1)

Individuare **tutte le attivita' svolte e i servizi erogati, internamente ed esternamente** (art. 3 co. 1 Det. 155238/2026), che risultano supportati, svolti o erogati da sistemi informativi e di rete.

Approcci suggeriti dalla Guida (nessuna metodologia e' obbligatoria):

| Approccio | Punto di partenza | Come |
|-----------|-------------------|------|
| Top-down | Funzioni e processi dell'organizzazione | Esaminare struttura organizzativa (organigramma) e processi di business per identificare attivita' svolte e servizi erogati |
| Bottom-up | Inventario dei sistemi informativi e di rete | Ricognizione di apparati fisici, applicazioni e servizi informatici; identificare le funzionalita' supportate e quindi le attivita'/servizi abilitati |
| Combinato | Entrambi | Le attivita' da analisi funzioni/processi sono verificate e integrate con quelle emerse dall'esame dei sistemi, per evidenziare incongruenze e omissioni |

**Granularita'** (Guida, cap. 2.2.1): individuare attivita'/servizi sufficientemente unitari ai fini dell'attribuzione della categoria; scomporre progressivamente fino a elementi con categoria di rilevanza omogenea, evitando l'eccessiva frammentazione. Per ogni macro-area e' sufficiente, **al piu', un numero di attivita'/servizi pari al numero di categorie di rilevanza** (4). Ulteriori livelli di dettaglio possono restare interni senza essere comunicati.

**Nota operativa**: nell'area privata della piattaforma ACN e' disponibile un documento di **esempi** di attivita'/servizi per ogni macro-area (comuni a tutte le tipologie di soggetto, tranne "Produzione di beni e servizi" e "Monitoraggio e controllo", declinati per tipologia). Consultarlo prima di compilare.

### Passo 4 - Mappatura in macro-aree (Guida, cap. 2.2.2)

Associare ogni attivita'/servizio alla **sola** macro-area che meglio ne rappresenta finalita' e caratteristiche, considerando natura dell'attivita', funzioni organizzative coinvolte e processi di business supportati.

- Se un'attivita' e' riconducibile a piu' macro-aree: **scomporla ulteriormente** fino ad avere elementi 1:1 con le macro-aree.
- Se non rientra in nessuna macro-area: usare la residuale **"Altri servizi e attivita'"**.
- Macro-aree senza attivita'/servizi del soggetto: **non vanno compilate** (art. 3 co. 4 Det. 155238/2026).

### Passo 5 - Attribuzione della categoria di rilevanza (art. 3 co. 3 + Guida, cap. 2.2.3)

Per default ogni attivita'/servizio acquisisce la **categoria pre-assegnata** della macro-area.

**Deroga**: si puo' attribuire una categoria diversa sulla base di una valutazione dell'impatto di una possibile compromissione dell'attivita'/servizio sulla capacita' del soggetto di svolgere le attivita' e i servizi NIS. In tal caso il soggetto **conserva la documentazione della valutazione** (art. 3 co. 3). Una stessa macro-area puo' contenere attivita' con categorie diverse.

L'attribuzione e' in sostanza una **Business Impact Analysis (BIA) semplificata** che considera le tre dimensioni della sicurezza informatica: **riservatezza, integrita', disponibilita'** (Guida, cap. 2.2.3 e Appendice B). Nessuna metodologia specifica e' richiesta. Criteri di valutazione desunti dall'Appendice B della Guida:

| Criterio | Cosa valuta |
|----------|-------------|
| Coordinamento delle attivita' e dei servizi NIS | Grado con cui l'attivita'/servizio contribuisce al coordinamento, gestione o supervisione delle attivita' e servizi NIS |
| Incidenza sulle funzioni di sicurezza | Grado con cui ha effetto sulle funzioni riguardanti la sicurezza |
| Interdipendenza con le attivita' e i servizi NIS | Dipendenza reciproca ed effetti a catena derivanti da una compromissione |
| Natura e/o volume dei dati trattati | Tipologia (es. presenza di dati personali) e volume dei dati |
| Continuita' operativa delle attivita' e dei servizi NIS | Grado con cui influenza la continuita' di svolgimento/erogazione |

**Perche' conta**: le categorie di rilevanza guideranno le future **misure di sicurezza a lungo termine** differenziate per categoria (art. 31 co. 2 lett. a D.Lgs. 138/2024; Guida, box cap. 2.1). Sottostimare una categoria espone a non conformita' future; sovrastimarla estende senza necessita' il perimetro delle misure piu' onerose.

### Passo 6 - Compilazione dell'output e trasmissione

```markdown
# Elenco categorizzato delle attivita' e dei servizi - [nome organizzazione]

**Data**: [YYYY-MM-DD]
**Finestra ACN**: 1 maggio - 30 giugno [YYYY]
**Allegato del modello applicato**: [1 / 2] (tipologia di soggetto: [n. X allegato Y D.Lgs. 138/2024])
**Compilato da**: [nome / ruolo]

## Elenco categorizzato

| # | Macro-area | Denominazione attivita'/servizio | Descrizione (opzionale) | Categoria di rilevanza | Pre-assegnata? | Rif. valutazione (se deroga) |
|---|------------|-----------------------------------|--------------------------|------------------------|----------------|-------------------------------|
| 1 | [...] | [...] | [...] | [alto/medio/basso/minimo] | SI/NO | [doc. interno] |
| ... | | | | | | |

## Attivita'/servizi PSNC (art. 5 Det. 155238/2026)

| # | Attivita'/servizio | Categoria |
|---|--------------------|-----------|
| ... | [...] | Impatto alto (d'ufficio, fuori dal modello) |

## Macro-aree non compilate (art. 3 co. 4)

[Elenco delle macro-aree per cui il soggetto non svolge attivita' ne' eroga servizi]

## Deroghe alle categorie pre-assegnate

| # | Attivita'/servizio | Pre-assegnata | Attribuita | Sintesi valutazione BIA (R/I/D) | Documento conservato |
|---|--------------------|----------------|-------------|----------------------------------|----------------------|
| ... | [...] | [...] | [...] | [...] | [path/protocollo] |

## Trasmissione

- [ ] Elenco caricato nel "Servizio NIS/Categorizzazione" entro il 30 giugno [YYYY] (art. 20 co. 1 Det. 127437/2026).
- [ ] Il punto di contatto ha confermato le informazioni ai sensi del DPR 445/2000 e le ha trasmesse (art. 20 co. 3).
- [ ] Copia ricevuta al domicilio digitale del soggetto (art. 20 co. 3).
- [ ] Documentazione delle valutazioni di deroga archiviata (art. 3 co. 3 Det. 155238/2026).
```

### Passo 7 - Dopo la trasmissione: verifiche di conformita' (art. 21 Det. 127437/2026)

- ACN analizza **a campione** gli elenchi (ex art. 30 co. 3 D.Lgs. 138/2024), anche in relazione a soggetti NIS comparabili.
- Riscontro entro **90 giorni** dalla trasmissione, prorogabile una sola volta fino a **+60 giorni**.
- Eventuali richieste di integrazioni **sospendono** i termini: rispondere entro **30 giorni**, pena possibile rigetto dell'elenco.
- In assenza di comunicazione nei termini, l'elenco **si intende convalidato** (art. 21 co. 5).
- Un esito negativo **non solleva** dall'obbligo di elencazione e categorizzazione ex art. 30 co. 1 (art. 21 co. 6): occorre ripresentare un elenco corretto.

## Casi tipici

| Caso | Trattamento | Riferimento |
|------|-------------|-------------|
| SOC interno, funzione compliance, supporto al CdA | Macro-area "Monitoraggio e controllo", impatto alto | Allegati 1-2 |
| Erogazione del servizio core (es. produzione energia, trasporto, servizio digitale) | "Produzione di beni e servizi", impatto medio (valutare deroga verso l'alto se la BIA lo giustifica) | Allegati 1-2 + art. 3 co. 3 |
| Laboratorio R&D con proprieta' intellettuale critica | "Ricerca, sviluppo e progettazione", impatto medio | Allegati 1-2 |
| ERP contabilita'/fatturazione | "Gestione finanziaria", impatto basso | Allegati 1-2 |
| Magazzino e spedizioni di un operatore trasporti (tipologia allegato I n. 2) | "Logistica", impatto basso (allegato 1) | art. 2 co. 2 |
| Magazzino di un soggetto non ricompreso nelle tipologie dell'allegato 1 | "Logistica", impatto minimo (allegato 2) | art. 2 co. 3 |
| Sito web vetrina e canali social | "Comunicazione e marketing", impatto minimo | Allegati 1-2 |
| Attivita' non riconducibile ad alcuna macro-area | "Altri servizi e attivita'", impatto minimo | Guida cap. 2.2.2 |
| Sistema incluso nel perimetro PSNC | Impatto alto d'ufficio, fuori dal modello | art. 5 Det. 155238/2026 |
| PA che ha classificato dati/servizi ex Regolamento Cloud | Usa il modello del Regolamento Cloud (ordinari/critici/strategici) | art. 4 Det. 155238/2026 |

## Limiti di questo task

- L'elenco e' una **dichiarazione di parte** confermata dal punto di contatto ai sensi del DPR 445/2000 (art. 20 co. 3 Det. 127437/2026); ACN puo' verificarla a campione (art. 21).
- La BIA semplificata non ha soglie quantitative fissate dalle fonti: la valutazione di deroga e' qualitativa e va documentata internamente (art. 3 co. 3 Det. 155238/2026). Questo task non sostituisce una BIA completa di continuita' operativa.
- Il documento di **esempi per macro-area** e' disponibile solo nell'area privata della piattaforma ACN e non e' catalogato tra le fonti di questa skill: consultarlo direttamente in piattaforma.
- Le **misure di sicurezza a lungo termine** differenziate per categoria di rilevanza non sono ancora state adottate (la Guida le annuncia come oggetto di successive determinazioni ACN): questo task copre solo l'adempimento di elencazione e categorizzazione.
- Il rinvio interno dell'art. 20 co. 2 Det. 127437/2026 cita "articolo 5, comma 5, lettera i)" del decreto NIS; il riferimento sostanziale, coerente con le premesse della Det. 155238/2026, e' l'art. 40 co. 5 lett. i).
