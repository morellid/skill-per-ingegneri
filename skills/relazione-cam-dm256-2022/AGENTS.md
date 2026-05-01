# AGENTS.md - relazione-cam-dm256-2022

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Redazione e verifica della Relazione Tecnica dei Requisiti Ambientali CAM per lavori di edilizia pubblica. Il riferimento normativo principale e' il **DM 23 giugno 2022 n. 256** (Allegato: criteri CAM di base e premianti). Il target utente e' il progettista (architetto/ingegnere) incaricato di una commessa pubblica soggetta all'obbligo CAM.

## Fonti autoritative

Fonti catalogate in `references/sources.yaml`:

- **dm-256-2022**: DM 23/06/2022 n. 256 - normattiva.it
- **dm-256-2022-allegato**: Allegato DM 256/2022 (criteri CAM) - sha256 da popolare
- **dlgs-36-2023-art57**: D.Lgs. 36/2023 art. 57 - normattiva.it

Estratti testuali in `references/estratti/`:
- `dm-256-2022-articoli-chiave.md` - artt. 1-4 del decreto (definizioni, obblighi SA)
- `dm-256-2022-allegato-criteri-2x.md` - criteri di base 2.1-2.9 con tabella applicabilita'
- `dm-256-2022-allegato-criteri-premianti.md` - criteri premianti 4.1-4.6
- `dlgs-36-2023-art57.md` - testo art. 57 e note operative

## Articoli e punti chiave

- **DM 256/2022 art. 2**: definizioni NC/R1/R2/MS (fondamentale per classificare l'intervento)
- **DM 256/2022 art. 3**: obblighi SA e ruolo della Relazione Tecnica dei Requisiti Ambientali
- **Allegato DM 256/2022 Criterio 2.1-2.9**: specifiche tecniche di base (obbligatorie)
- **Allegato DM 256/2022 Criterio 4.1-4.6**: specifiche premianti (OEPV)
- **D.Lgs. 36/2023 art. 57 co. 2**: soglie di obbligatorieta' (100% servizi/forniture, 50% lavori)

## Convenzioni specifiche

### Cosa NON fare
- Non produrre relazioni CAM senza citare esplicitamente il DM 23/06/2022 n. 256
- Non dichiarare criteri "non applicabili" senza motivazione
- Non omettere il Criterio 2.7 (rifiuti C&D) per interventi con demolizioni
- Non confondere la Relazione CAM con l'APE (documenti distinti)
- Non applicare il DM 11/01/2017 (superato dall'08/10/2022)

### Cosa fare
- Classificare sempre l'intervento come NC/R1/R2/MS prima di elencare i criteri
- Citare il numero del criterio (es. "Criterio 2.3.2") e il riferimento al DM in ogni sezione
- Indicare per ogni criterio: requisito minimo, scelta adottata, documentazione di verifica
- Usare la terminologia esatta del DM 256/2022 (vedi tabella in AGENTS.md)
- Concludere sempre con il rinvio al progettista firmatario

## Validatori

- Non ancora assegnato (validazione Livello 2 da effettuare con professionista esperto di gare PA)

## Stato attuale

- Versione: 0.1.0-alpha
- Validazione: Livello 1 (struttura e contenuto normativo revisionati internamente)
- Task files: 3 (identifica-criteri-applicabili, draft-relazione-cam, check-relazione-cam)
- Esempi: 1 conforme (NC uffici) + 1 non conforme (R1 lacunosa)
