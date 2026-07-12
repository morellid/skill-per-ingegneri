# AGENTS.md - relazione-cam-dm-24-11-2025

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Redazione e verifica della **Relazione CAM di progetto** (criterio 2.1.1 dell'Allegato 1 al **DM MASE 24 novembre 2025**, CAM edilizia in vigore dal 2/2/2026, che abroga il DM 256/2022 e il correttivo DM 5/8/2024). Il target utente e' il progettista (architetto/ingegnere) incaricato di una commessa pubblica soggetta all'obbligo CAM (art. 57 co. 2 D.Lgs. 36/2023).

## Fonti autoritative

Fonti catalogate in `references/sources.yaml`:

- **dm-cam-24-11-2025**: articolato del DM (GU n. 281 del 3/12/2025) - hash + trascrizione in `references/fonti/dm-cam-24-11-2025-articolato.md`
- **dm-cam-24-11-2025-allegato-1**: Allegato 1 (criteri, PDF MASE) - hash + trascrizione dei paragrafi citati in `references/fonti/dm-cam-24-11-2025-allegato-1.md`
- **circolare-mase-10-04-2026**: chiarimenti ambito/transitorio - `references/fonti/circolare-mase-10-04-2026.md`
- **modello-relazione-cam-2026**: modello MASE vers. 02/02/2026 - `references/fonti/modello-relazione-cam-2026.md`
- **dlgs-36-2023-art57**: obbligo CAM - estratto `references/estratti/dlgs-36-2023-art57.md`
- **dm-256-2022 / dm-256-2022-allegato**: [ABROGATI, regime transitorio] estratti [STORICO]

## Punti chiave

- **Art. 1 co. 2 DM**: regime temporale (lett. a progettazione/DL; lett. b lavori e congiunti con "progetto validato in vigenza"; lett. c progettazione interna non validata)
- **Art. 2 DM + circolare par. C**: transitorio DM 256/2022 con doppia condizione (validazione conforme al vecchio DM + bando entro tre mesi dalla validazione)
- **Art. 3 DM**: definizioni ex art. 3 DPR 380/2001 e Reg. UE 2024/3110; niente piu' NC/R1/R2/MS
- **Criterio 2.1.1**: Relazione CAM per ogni livello di progettazione, evidenza per ogni criterio, esclusioni motivate tecnicamente
- **Par. 1.3.5**: mezzi di prova; divieto di "certificazioni CAM" di prodotto; verifiche in tre fasi (premianti, verifica progetto ex art. 42/allegato I.7, DL in esecuzione con penali ex art. 122)
- **Criterio 3.1.1**: Relazione CAM dell'impresa appaltatrice (documento distinto, non generato dalla skill)
- **Modello MASE**: sezioni normativa/progetto/allegati, Tabella 1 di applicabilita', Scheda Tipo per criterio

## Convenzioni specifiche

### Cosa NON fare
- Non applicare i criteri del DM 256/2022 fuori dal regime transitorio (e viceversa): verificare SEMPRE il regime prima di tutto
- Non usare la numerazione del vecchio DM (es. la Relazione CAM era il criterio 2.2.1, ora e' il 2.1.1; i prodotti erano il cap. 2.5, ora sono il 2.4)
- Non inventare soglie o requisiti prestazionali dei singoli criteri: la skill trascrive solo i paragrafi strutturali; per il merito rinviare al testo integrale del criterio nel PDF ufficiale con segnaposto "[VERIFICARE]"
- Non accettare "certificati CAM" / "attestati di conformita' ai CAM" come mezzi di prova (par. 1.3.5)
- Non dichiarare criteri "non applicabili" senza motivazione tecnica (criterio 2.1.1)
- Non confondere la Relazione CAM di progetto (2.1.1) con la Relazione CAM dell'impresa (3.1.1) ne' con l'APE o la relazione di sostenibilita' ex art. 11 allegato I.7

### Cosa fare
- Determinare il regime (nuovo DM vs transitorio) con dati di procedura: data bando/inviti, regime e data di validazione del progetto a base di gara
- Identificare la tipologia di intervento con le definizioni dell'art. 3 DPR 380/2001
- Usare la struttura del modello MASE (Tabella 1 + Schede Tipo) per ogni output
- Citare numero criterio e fonte per ogni affermazione (es. "criterio 2.5.2", "par. 1.3.5", "circolare MASE 10/4/2026 par. C")
- Concludere sempre con il rinvio al progettista firmatario

## Validatori

- Non ancora assegnato (validazione Livello 2 da effettuare con professionista esperto di gare PA sui nuovi CAM)

## Stato attuale

- Versione: 1.0.0-alpha (major update normativo: DM 24/11/2025 sostituisce il DM 256/2022; rinominata da `relazione-cam-dm256-2022`)
- Validazione: Livello 1 (fonti scaricate, hashate, trascritte; contenuto riscritto sui testi letti)
- Task files: 3 (identifica-criteri-applicabili, draft-relazione-cam, check-relazione-cam)
- Esempi: 1 conforme (nuova costruzione uffici, appalto integrato) + 1 non conforme (ristrutturazione ERP, relazione lacunosa)
