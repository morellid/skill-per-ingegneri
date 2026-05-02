# Task: Verifica completezza Dichiarazione di Conformita'

Verifica che la DdC fornita dall'utente contenga tutti gli elementi obbligatori del modello Allegato I ai sensi dell'Art. 7 DM 37/2008.

## Obiettivo

Produrre un report strutturato che per ogni sezione del modello Allegato I indica se il campo e' presente, assente o inadeguato, con citazione normativa per ogni carenza.

## Input richiesti

- Testo o trascrizione della DdC (o descrizione dei campi compilati)
- Opzionali (migliorano la qualita' dell'analisi):
  - Categoria di impianto (lettera a-g)
  - Superficie/potenza dell'impianto (per verificare la coerenza con l'obbligo di progetto Art. 5)
  - Documentazione allegata disponibile

Se l'input e' solo parziale, segnalarlo nel report e limitare la verifica a quanto fornito.

**Nota**: Per determinare la coerenza degli allegati con le soglie Art. 5, eseguire anche il task
`identifica-allegati-obbligatori.md` prima o in parallelo.

## Fonti normative

Prima di procedere, leggere:
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md` - Art. 7 (obblighi DdC) e struttura Allegato I

## Procedura

### Passo 1 - Identifica la categoria

Dalla DdC o dall'utente, determina quale/i categoria/e di impianto sono dichiarate (a-g, Art. 1 DM 37/2008). Se la categoria non e' indicata nella DdC, classificarla come **assente - non conforme** (e' un campo obbligatorio del modello Allegato I).

### Passo 2 - Verifica Sezione 1: Dati impresa installatrice

Campi obbligatori:
- [ ] Ragione sociale / denominazione impresa
- [ ] Sede legale (indirizzo completo: via, comune, provincia, CAP)
- [ ] Numero di iscrizione al Registro delle Imprese o all'Albo Imprese Artigiane
- [ ] Camera di Commercio di riferimento
- [ ] Codice fiscale / P.IVA

Classificare ogni campo: `presente`, `assente`, `incompleto`.

**Casistica**: Se la DdC riporta solo il nome del singolo artigiano senza iscrizione CCIAA/Albo,
classificare iscrizione come `assente` e segnalare che Art. 3 DM 37/2008 richiede l'iscrizione
come pre-requisito di abilitazione.

### Passo 3 - Verifica Sezione 2: Responsabile tecnico

Campi obbligatori:
- [ ] Nome e cognome del responsabile tecnico
- [ ] Qualifica ai sensi Art. 4 DM 37/2008 (titolo di studio o esperienza specifica)
- [ ] Abilitazione specifica per la categoria di impianto dichiarata

**Verifica coerenza**: Se la categoria dichiarata e' "c) riscaldamento" ma il responsabile tecnico
dichiara abilitazione solo per "a) elettrico", segnalare come `potenziale incongruenza`.

**Qualifica generica**: Se la DdC riporta solo "tecnico abilitato" senza specificare il titolo di
studio o il percorso di abilitazione (Art. 4 co. 1), classificare come `incompleto`.

### Passo 4 - Verifica Sezione 3: Dati impianto

Campi obbligatori:
- [ ] Tipologia impianto (lettera categoria a-g indicata esplicitamente)
- [ ] Destinazione d'uso dell'edificio
- [ ] Indirizzo completo dell'impianto (via, numero civico, comune, provincia)
- [ ] Committente (nome/ragione sociale)

### Passo 5 - Verifica Sezione 4: Testo della dichiarazione e norme

- [ ] Formula dichiarativa presente e conforme al modello Allegato I ("dichiara sotto la propria responsabilita' che l'impianto e' stato realizzato in conformita' alla regola dell'arte")
- [ ] Almeno una norma tecnica specifica indicata (es. CEI 64-8 per cat. a), UNI 7129 per cat. e))
- [ ] Data della dichiarazione presente
- [ ] Firma del responsabile tecnico presente

**Verifica formula generica**: "L'impianto e' stato realizzato secondo le norme vigenti" senza
citazione specifica e' `inadeguato` - il modello Allegato I richiede la formula specifica e l'elenco
delle norme applicate.

**Verifica adeguatezza norma citata**: Se la DdC per un impianto elettrico (cat. a) cita solo
"DM 37/2008" senza la norma tecnica di settore, classificare come `inadeguato`. Il DM 37/2008 e'
la norma procedurale, non tecnica; la regola dell'arte per impianti elettrici e' la CEI 64-8.
Tuttavia, la citazione delle norme e' responsabilita' tecnica del responsabile tecnico firmatario:
segnalare il problema senza sostituirsi alla sua valutazione tecnica.

### Passo 6 - Verifica Sezione 5: Allegati

Verificare la coerenza tra le caselle barrate nella sezione allegati e gli allegati dichiarati
dall'utente.

**Allegato sempre obbligatorio (Art. 7 co. 1 DM 37/2008)**:
- [ ] Relazione con tipologia dei materiali utilizzati: deve essere presente in tutti i casi.
  Una relazione generica ("materiali conformi alle norme") senza specificare tipologia/marca/modello
  e' `inadeguata`.

**Elaborato tecnico (sempre necessario - Art. 7 co. 1-2 DM 37/2008)**:
- [ ] Schema dell'impianto o progetto: deve essere sempre presente. La distinzione e' nel livello:
  - Sotto soglie Art. 5: schema dell'impianto realizzato redatto dal responsabile tecnico (minimo - Art. 7 co. 2)
  - Sopra soglie Art. 5: progetto da professionista + schema as-built (Art. 7 co. 1)
  - Se **nessun elaborato tecnico** e' allegato, classificare come `assente - non conforme`
    indipendentemente dalle dimensioni dell'impianto

Se l'utente non ha eseguito il task allegati, suggerire di eseguire `identifica-allegati-obbligatori.md`
per determinare se era necessario il progetto professionale.

### Passo 7 - Generazione output

```markdown
# Verifica completezza DdC - DM 37/2008 Allegato I

**Data verifica**: [data]
**DdC analizzata**: [identificativo - es. indirizzo impianto]
**Categoria impianto**: [a-g]

## Esito sintetico

[COMPLETA | INCOMPLETA CON NOTE | INCOMPLETA - NON CONFORME]

Campi presenti: X/Y
Allegati obbligatori: [stato]

## Dettaglio per sezione

### Sezione 1 - Dati impresa
- [ ] Ragione sociale: [presente/assente/incompleto]
- [ ] Sede legale: [presente/assente/incompleto - motivo]
- [ ] Iscrizione CCIAA / Albo (Art. 3 DM 37/2008): [presente/assente]
- [ ] C.F. / P.IVA: [presente/assente]

### Sezione 2 - Responsabile tecnico
- [ ] Nome e cognome: [presente/assente]
- [ ] Qualifica (Art. 4 DM 37/2008): [presente/assente/incompleto]
- [ ] Abilitazione categoria specifica: [presente/assente/incongruenza]

### Sezione 3 - Dati impianto
- [ ] Categoria impianto (lettera a-g): [presente/assente]
- [ ] Destinazione d'uso: [presente/assente]
- [ ] Indirizzo impianto: [presente/assente/incompleto]
- [ ] Committente: [presente/assente]

### Sezione 4 - Dichiarazione e norme
- [ ] Formula dichiarativa conforme Allegato I: [presente/assente/generica]
- [ ] Norma tecnica specifica citata: [presente/assente/inadeguata - motivo]
- [ ] Data: [presente/assente]
- [ ] Firma: [presente/assente]

### Sezione 5 - Allegati
- [ ] Relazione materiali (OBBLIGATORIA - Art. 7 co. 1): [presente/assente/generica]
- [ ] Elaborato tecnico (schema/progetto - sempre necessario): [presente/assente - livello]
- [ ] Progetto da professionista: [presente/assente/non-richiesto sopra-soglia]

## Carenze rilevate

| # | Sezione | Campo | Carenza | Riferimento | Priorita' |
|---|---------|-------|---------|-------------|-----------|
| 1 | 5 | Elaborato tecnico | Schema/progetto assente | Art. 7 co. 1-2 DM 37/2008 | Alta |
| ... |

## Raccomandazioni

- ...

## Limiti di questa verifica

- Verifica formale sulla presenza dei campi, non sulla veridicita' delle dichiarazioni
- Non verifica l'effettiva abilitazione dell'installatore (richiede consultazione registro CCIAA)
- Non giudica l'adeguatezza tecnica delle norme citate rispetto all'impianto specifico
- Le soglie Art. 5 richiedono verifica su Normattiva per uso operativo

## Rinvio al responsabile tecnico firmatario

**La presente verifica non sostituisce la revisione e firma del responsabile tecnico abilitato.**
La responsabilita' penale e civile per la DdC resta in capo all'installatore firmatario (Art. 7 co. 4 DM 37/2008).
```

## Casi limite

### DdC su modello regionale
Alcune regioni hanno adottato modelli regionali. Se conforme all'Allegato I, la verifica e' valida.
Aggiungere un avviso se il modello sembra diverso dallo standard nazionale.

### DdC per manutenzione ordinaria
Per manutenzione ordinaria (senza trasformazione/ampliamento dell'impianto) la DdC non e'
obbligatoria ex DM 37/2008. Se la DdC indica "manutenzione ordinaria", segnalare che la DdC
sarebbe facoltativa e chiedere conferma sulla natura dell'intervento.

### Impianto che copre piu' categorie
Verificare che il responsabile tecnico abbia abilitazione per tutte le categorie dichiarate.

## Esempi

Vedi `examples/` per:
- `conforme-elettrico-residenziale-piccolo/`: DdC con tutti i campi corretti, schema impianto incluso
- `problematico-progetto-mancante/`: DdC con progetto professionale mancante sopra soglia
