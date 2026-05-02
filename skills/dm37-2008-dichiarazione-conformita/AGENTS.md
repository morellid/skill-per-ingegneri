# AGENTS.md - dm37-2008-dichiarazione-conformita

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill per la Dichiarazione di Conformita' (DdC) degli impianti tecnologici negli edifici ai sensi del DM 22/01/2008 n. 37. Copre le **7 categorie (a-g)** di impianti (elettrico, radiotelevisivo/elettronico, riscaldamento/climatizzazione, idrico-sanitario, gas, sollevamento, antincendio). L'automazione di porte/cancelli e' inclusa in cat. a), non e' categoria separata. Target: installatori abilitati, responsabili tecnici di impresa installatrice, ingegneri/periti che verificano la documentazione.

## Fonti autoritative

- **DM 37/2008 - Normattiva** (testo consolidato vigente)
  - id `dm37-2008-normattiva` in `references/sources.yaml`
  - URL: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.ministeriale:2008-01-22;37
- **DM 37/2008 - GU originale** - id `dm37-2008-gu-originale` in `references/sources.yaml`
  - GU n. 61 del 12/03/2008 Suppl. Ordinario n. 54

Estratti in `references/estratti/`:
- `dm37-2008-artt-1-7-allegato-i.md` - parafasi operativa di Art. 1, 3, 4, 5, 7 e struttura Allegato I.
  **Contiene soglie che devono essere verificate su Normattiva prima dell'uso operativo.**

## Articoli e punti chiave

- **Art. 1**: Categorie di impianti a-g; automazione cancelli dentro cat. a); esclusioni
- **Art. 3**: Requisiti per l'abilitazione delle imprese installatrici (iscrizione CCIAA/Albo)
- **Art. 4**: Responsabile tecnico - requisiti di qualifica (diploma, formazione, esperienza)
- **Art. 5**: Progettazione degli impianti - soglie per obbligo di progetto da professionista iscritto all'albo; sotto le soglie il responsabile tecnico predispone almeno lo schema impianto
- **Art. 6**: Realizzazione secondo la regola dell'arte; riferimento alle norme UNI, CEI, etc.
- **Art. 7 co. 1**: DdC obbligatoria al termine dei lavori, su modello Allegato I
- **Art. 7 co. 1**: DdC obbligatoria su modello Allegato I; allegati integranti: relazione materiali (sempre) e progetto (quando richiesto da Art. 5)
- **Art. 7 co. 2**: Quando il progetto e' redatto dal responsabile tecnico (sotto soglia Art. 5), l'elaborato tecnico e' almeno lo schema dell'impianto
- **Art. 7 co. 4**: Responsabilita' del soggetto che rilascia la DdC per la veridicita' dei contenuti
- **Art. 8**: Collaudo degli impianti (separato dalla DdC)
- **Art. 15**: Sanzioni per violazioni DM 37/2008

## Convenzioni specifiche

### Cosa NON fare
- Non confondere Art. 3/4 (abilitazione imprese/responsabile tecnico) con Art. 5 (progettazione)
- Non affermare "progetto non necessario" senza specificare che sotto-soglia serve comunque lo schema dell'impianto a cura del responsabile tecnico (Art. 7 co. 2 DM 37/2008)
- Non omettere di citare numero articolo e comma per ogni obbligo citato
- Non applicare soglie categoria a) alle altre categorie: ogni categoria ha soglie proprie nell'Art. 5
- Non citare "Art. 6 obbligo progetto": Art. 6 riguarda la regola dell'arte, non il progetto; usare "Art. 5"
- Non scrivere "categoria h)" o "8 categorie": le categorie sono a-g (7)

### Cosa fare
- Prima di determinare l'obbligo di progetto professionale, verificare la categoria e confrontarla con le soglie specifiche dell'Art. 5
- Distinguere sempre tra "progetto da professionista iscritto all'albo" (sopra soglia Art. 5) e "schema/elaborato tecnico del responsabile tecnico" (sotto soglia, ma sempre necessario)
- Segnalare esplicitamente che le soglie Art. 5 devono essere verificate su Normattiva perche' sono state oggetto di modifiche e interpretazioni
- Citare la norma tecnica specifica nella DdC (es. CEI 64-8 per cat. a), non solo "DM 37/2008")

## Validatori

- Da identificare: ingegnere elettrico o responsabile tecnico di impresa installatrice abilitata ai sensi del DM 37/2008.

## Stato attuale

- Versione: 0.1.0-alpha
- Validazione: Livello 1 (autore) - post revisione adversarial review Codex
- Task files: `verifica-completezza-ddc.md`, `identifica-allegati-obbligatori.md`
- Esempi: 1 conforme + 1 problematico
- Nota: le soglie Art. 5 nell'estratto sono parafrasate; richiedono verifica su Normattiva prima di v1.0
