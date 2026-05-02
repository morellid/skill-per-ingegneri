# Task: Verifica completezza Dichiarazione di Conformita'

Verifica che la DdC fornita dall'utente contenga tutti gli elementi obbligatori del modello Allegato I ai sensi dell'Art. 7 DM 37/2008.

## Obiettivo

Produrre un report strutturato che per ogni sezione del modello Allegato I indica se il campo e' presente, assente o inadeguato, con citazione normativa per ogni carenza.

## Input richiesti

- Testo o trascrizione della DdC (o descrizione dei campi compilati)
- Opzionali (migliorano la qualita' dell'analisi):
  - Categoria di impianto (lettera a-g)
  - Superfice/potenza dell'impianto (per verificare obbligo progetto)
  - Documentazione allegata disponibile

Se l'input e' solo parziale, segnalarlo nel report e limitare la verifica a quanto fornito.

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

**Casistica**: Se la DdC riporta solo il nome del singolo artigiano senza iscrizione CCIAA, classificare CCIAA come `assente` e segnalare che Art. 5 DM 37/2008 richiede l'iscrizione all'albo o registro come pre-requisito di abilitazione.

### Passo 3 - Verifica Sezione 2: Responsabile tecnico

Campi obbligatori:
- [ ] Nome e cognome del responsabile tecnico
- [ ] Qualifica (titolo di studio o esperienza ai sensi Art. 5)
- [ ] Abilitazione specifica per la categoria di impianto dichiarata

**Verifica coerenza**: Se la categoria dichiarata e' "c) riscaldamento" ma il responsabile tecnico dichiara abilitazione solo per "a) elettrico", segnalare come `potenziale incongruenza` - richiedere chiarimento.

### Passo 4 - Verifica Sezione 3: Dati impianto

Campi obbligatori:
- [ ] Tipologia impianto (lettera categoria a-g indicata esplicitamente)
- [ ] Destinazione d'uso dell'edificio
- [ ] Indirizzo completo dell'impianto (via, numero civico, comune, provincia)
- [ ] Committente (nome/ragione sociale)

**Nota**: L'indirizzo dell'impianto puo' coincidere con l'indirizzo del committente (es. proprietario che installa nel proprio appartamento) ma entrambi devono essere presenti.

### Passo 5 - Verifica Sezione 4: Testo della dichiarazione e norme

- [ ] Formula dichiarativa presente ("dichiara sotto la propria responsabilita' che l'impianto e' stato realizzato in conformita' alla regola dell'arte")
- [ ] Almeno una norma tecnica applicata indicata (es. CEI 64-8 per cat. a), UNI 7129 per cat. e gas)
- [ ] Data della dichiarazione presente
- [ ] Firma del responsabile tecnico presente

**Verifica adeguatezza norma citata**: Se la DdC per un impianto elettrico (cat. a) cita solo "DM 37/2008" senza la norma tecnica di settore, classificare come `inadeguato`: il DM 37/2008 e' la norma procedurale, non tecnica; la regola dell'arte per gli impianti elettrici e' la CEI 64-8.

### Passo 6 - Verifica Sezione 5: Allegati

Verificare la coerenza tra:
1. Le caselle barrate nella sezione allegati
2. Gli allegati effettivamente presenti o dichiarati dall'utente

Casella obbligatoria:
- [ ] Relazione con tipologia dei materiali utilizzati: **sempre obbligatoria** (Art. 7 co. 2 DM 37/2008)

Casella condizionale (dipende da soglie Art. 6):
- [ ] Schema dell'impianto realizzato: obbligatorio quando il progetto era richiesto da Art. 6; fortemente raccomandato anche quando non obbligatorio
- [ ] Progetto: obbligatorio nei casi Art. 6 (vedi task `identifica-allegati-obbligatori.md` per le soglie esatte)

Se l'utente non ha eseguito il task di identificazione allegati, suggerire di eseguire prima `identifica-allegati-obbligatori.md`.

### Passo 7 - Generazione output

Produrre un report nel formato seguente:

```markdown
# Verifica completezza DdC - DM 37/2008 Allegato I

**Data verifica**: [data]
**DdC analizzata**: [identificativo se disponibile - es. n. DdC o indirizzo impianto]
**Categoria impianto**: [a-g]

## Esito sintetico

[COMPLETA | INCOMPLETA CON NOTE | INCOMPLETA - NON CONFORME]

Campi presenti: X/Y
Allegati obbligatori presenti: Z/W

## Dettaglio per sezione

### Sezione 1 - Dati impresa
- [ ] Ragione sociale: [presente/assente/incompleto]
- [ ] Sede legale: [presente/assente/incompleto - motivo]
- [ ] Iscrizione CCIAA / Albo: [presente/assente]
- [ ] C.F. / P.IVA: [presente/assente]

### Sezione 2 - Responsabile tecnico
- [ ] Nome e cognome: [presente/assente]
- [ ] Qualifica: [presente/assente/incompleto]
- [ ] Abilitazione categoria specifica: [presente/assente/incongruenza]

### Sezione 3 - Dati impianto
- [ ] Categoria impianto (lettera): [presente/assente]
- [ ] Destinazione d'uso: [presente/assente]
- [ ] Indirizzo impianto: [presente/assente/incompleto]
- [ ] Committente: [presente/assente]

### Sezione 4 - Dichiarazione e norme
- [ ] Formula dichiarativa: [presente/assente]
- [ ] Norma tecnica applicata: [presente/assente/inadeguata - motivo]
- [ ] Data: [presente/assente]
- [ ] Firma: [presente/assente]

### Sezione 5 - Allegati
- [ ] Relazione materiali (OBBLIGATORIA): [presente/assente]
- [ ] Schema impianto: [presente/assente/non-richiesto]
- [ ] Progetto tecnico: [presente/assente/non-richiesto]

## Carenze rilevate

| # | Sezione | Campo | Carenza | Riferimento | Priorita' |
|---|---------|-------|---------|-------------|-----------|
| 1 | 1 | Iscrizione CCIAA | Non indicata | Art. 7 co. 1 + Art. 5 DM 37/2008 | Alta |
| ... |

## Raccomandazioni

- Integrare [campo] con [indicazione su cosa aggiungere]
- ...

## Limiti di questa verifica

- Verifica formale sulla presenza dei campi, non sulla veridicita' delle dichiarazioni
- Non verifica l'effettiva abilitazione dell'installatore (richiede consultazione registro CCIAA)
- Non giudica l'adeguatezza tecnica delle norme citate rispetto all'impianto specifico

## Rinvio al responsabile tecnico firmatario

**La presente verifica non sostituisce la revisione e firma del responsabile tecnico abilitato.** La responsabilita' penale e civile per la DdC resta esclusivamente in capo all'installatore firmatario (Art. 7 co. 4 DM 37/2008).
```

## Casi limite

### DdC su modello regionale
Alcune regioni (es. Lombardia, Toscana) hanno adottato modelli regionali. Se il modello regionale e' conforme all'Allegato I, la verifica resta valida. Se il modello aggiunge sezioni ulteriori (es. dati CURIE o CUP), verificarle separatamente rispetto alle sezioni obbligatorie nazionali.

### DdC per manutenzione straordinaria (non nuova installazione)
Il DM 37/2008 si applica anche a "trasformazione e ampliamento" degli impianti, non solo alle nuove installazioni. Per manutenzione ordinaria la DdC non e' obbligatoria (salvo interventi che modificano sostanzialmente l'impianto). Se la DdC indica "manutenzione" in luogo di "installazione/trasformazione", segnalare questo punto per chiarimento.

### Impianto per piu' categorie
Se la stessa DdC copre piu' categorie (es. impianto elettrico + antenne), verificare che le categorie siano tutte elencate e che il responsabile tecnico abbia abilitazione per ciascuna.
