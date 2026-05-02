# AGENTS.md - dm37-2008-dichiarazione-conformita

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill per la Dichiarazione di Conformita' (DdC) degli impianti tecnologici negli edifici ai sensi del DM 22/01/2008 n. 37. Copre le 8 categorie di impianti (elettrico, radiotelevisivo, riscaldamento/climatizzazione, idrico-sanitario, gas, sollevamento, antincendio, automazione accessi). Target: installatori abilitati, responsabili tecnici di impresa installatrice, ingegneri/periti che verificano la documentazione.

## Fonti autoritative

- **DM 37/2008 - Normattiva** - id `dm37-2008-normattiva` in `references/sources.yaml`
  - URL: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.ministeriale:2008-01-22;37
- **DM 37/2008 - GU originale** - id `dm37-2008-gu-originale` in `references/sources.yaml`
  - GU n. 61 del 12/03/2008 Suppl. Ordinario n. 54

Estratti pertinenti in `references/estratti/`:
- `dm37-2008-artt-1-7-allegato-i.md` - Art. 1 (campo applicazione e categorie), Art. 5 (abilitazioni), Art. 6 (obbligo progetto), Art. 7 (contenuto DdC), Allegato I (modello DdC)

## Articoli e punti chiave

- **Art. 1**: Campo di applicazione - definisce le 8 categorie (a-h) di impianti soggetti al DM 37/2008 negli edifici
- **Art. 5**: Imprese abilitate - requisiti (iscrizione CCIAA, responsabile tecnico con abilitazione per categoria)
- **Art. 6 co. 1**: Obbligo di progettazione per categoria a) (elettrico): superficie > 200 mq, potenza > 6 kW, ambienti con pericolo di esplosione, edifici > 16 unita' immobiliari
- **Art. 6 co. 2**: Obbligo di progettazione per categoria c) (riscaldamento/climatizzazione): potenza termica nominale > 35 kW
- **Art. 6 co. 4**: Il progetto deve essere redatto da un tecnico abilitato (ingegnere/perito/geometra secondo competenze di legge)
- **Art. 7 co. 1**: Contenuto obbligatorio DdC (dati impresa, responsabile tecnico, tipo impianto, ubicazione, dichiarazione conformita', norme applicate, data e firma)
- **Art. 7 co. 2**: Allegati obbligatori - relazione tipologia materiali (sempre); schema impianto realizzato (quando progetto obbligatorio o richiesto da committente)
- **Art. 7 co. 3**: La DdC va consegnata al committente entro 30 gg dal termine dei lavori
- **Art. 7 co. 6**: Responsabilita' penale e civile per DdC falsa o incompleta in capo all'installatore firmatario
- **Allegato I**: Modello ufficiale della DdC - 5 sezioni obbligatorie da compilare

## Convenzioni specifiche

### Cosa NON fare
- Non affermare che un impianto e' "conforme alle norme tecniche" senza precisare quali CEI/UNI specifiche sono applicabili: la skill verifica solo la completezza formale della DdC
- Non confondere la DdC DM 37/2008 con il Certificato di Collaudo o con la SCIA edilizia: sono documenti distinti con iter separati
- Non omettere di citare il numero di articolo e comma quando si indica un obbligo (es. "Art. 6 co. 1 lett. a)")
- Non applicare le soglie Art. 6 per la categoria a) anche alle altre categorie: le soglie sono diverse per ogni categoria

### Cosa fare
- Per ogni categoria, indicare esplicitamente se l'impianto ricade o meno nell'obbligo di progetto Art. 6
- Nella verifica completezza DdC, esaminare ogni campo dell'Allegato I separatamente
- Segnalare se il committente e' anche il proprietario o e' un soggetto diverso (rilevante per la consegna DdC)
- Indicare il codice ATECO dell'installatore come elemento di verifica abilitazione (non obbligatorio nel modello ma indicatore di coerenza)

## Validatori

- Da identificare: ingegnere elettrico o responsabile tecnico di impresa installatrice elettrica abilitata ai sensi del DM 37/2008.

## Stato attuale

- Versione: 0.1.0-alpha
- Validazione: Livello 1 (autore)
- Task files: `verifica-completezza-ddc.md`, `identifica-allegati-obbligatori.md`
- Esempi: 1 conforme + 1 problematico
