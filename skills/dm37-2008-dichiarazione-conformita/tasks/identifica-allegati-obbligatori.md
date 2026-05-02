# Task: Identifica allegati obbligatori per categoria di impianto

Determina quali documenti devono essere allegati alla DdC in base alla categoria di impianto (a-g), alle caratteristiche dimensionali/di potenza e alle soglie dell'Art. 6 DM 37/2008.

## Obiettivo

Produrre un elenco preciso degli allegati obbligatori, distinto tra sempre-obbligatori e condizionali (dipendono da soglie), con citazione normativa per ognuno.

## Input richiesti

Raccogliere dall'utente prima di procedere:

1. **Categoria di impianto** (a-g ai sensi Art. 1 DM 37/2008):
   - a) Impianto elettrico (energia, protezione scariche, automazione accessi)
   - b) Impianto radiotelevisivo / antenne / elettronico
   - c) Riscaldamento, climatizzazione, condizionamento, refrigerazione, ventilazione
   - d) Impianto idrico-sanitario
   - e) Impianto gas (distribuzione e utilizzo)
   - f) Impianto di sollevamento (ascensori, montacarichi, scale mobili)
   - g) Impianto protezione antincendio

2. **Caratteristiche dell'impianto** (solo quelle rilevanti per la categoria dichiarata):
   - Per cat. a): superficie dell'unita' immobiliare (mq) + potenza impegnata (kW) + tipo edificio (residenziale/commerciale/industriale) + presenza di classificazione ATEX + altezza in gronda (m)
   - Per cat. c) ed e): potenza termica nominale (kW)
   - Per cat. d): numero di unita' abitative dell'edificio + superficie utile (se non residenziale)
   - Per cat. g): sempre richiede progetto (vedi sotto)

3. **Tipo di intervento**: nuova installazione / trasformazione / ampliamento

Se i dati non sono disponibili, procedere per il caso piu' cautelativo (richiedere progetto e schema se c'e' incertezza) e indicare esplicitamente l'assunzione.

## Fonti normative

Prima di procedere, leggere:
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md` - Art. 6 (soglie obbligo progetto) e Art. 7 co. 2 (allegati DdC)

## Procedura

### Passo 1 - Allegato sempre obbligatorio

**Relazione con tipologia dei materiali utilizzati** (Art. 7 co. 2 DM 37/2008):
- Obbligatoria in **TUTTI** i casi, per tutte le categorie, sempre
- Non e' opzionale: la legge dice "fanno parte integrante" della DdC
- Contenuto minimo: elenco dei principali materiali e componenti installati (es. marca/modello del quadro elettrico, tipo cavi, marca caldaia, ecc.)

### Passo 2 - Obbligo di progetto e schema impianto per categoria a) (elettrico)

Il progetto e' obbligatorio (Art. 6 co. 1) per impianti cat. a) se almeno una delle seguenti condizioni e' soddisfatta:

| Condizione | Soglia | Riferimento |
|-----------|--------|-------------|
| Utenze in media tensione | qualsiasi | Art. 6 co. 1 lett. a) |
| Potenza impegnata | > 6 kW | Art. 6 co. 1 lett. a) |
| Luoghi con pericolo di esplosione (ATEX) | qualsiasi | Art. 6 co. 1 lett. a) |
| Altezza in gronda edificio civile | > 12 m | Art. 6 co. 1 lett. a) |
| Unita' abitativa residenziale (superficie) | > 400 mq | Art. 6 co. 1 lett. b) |

**NOTA IMPORTANTE**: Le soglie di Art. 6 DM 37/2008 sono state oggetto di diverse interpretazioni e modifiche nel tempo. La soglia di 200 mq era presente in versioni precedenti; il testo vigente su Normattiva riporta 400 mq per le unita' abitative. **Verificare sempre il testo aggiornato su Normattiva prima di determinare l'obbligo.** In caso di dubbio, consigliare la redazione del progetto come misura cautelativa.

Se il progetto era obbligatorio:
- [ ] **Progetto di impianto** (Art. 6 co. 2): redatto da tecnico abilitato iscritto all'albo
- [ ] **Schema dell'impianto realizzato** (as-built): allegato obbligatorio insieme al progetto

Se il progetto NON era obbligatorio:
- Lo schema impianto non e' obbligatorio per legge, ma e' fortemente raccomandato per manutenzione futura
- Il committente puo' sempre richiederlo e l'installatore puo' includerlo volontariamente

### Passo 3 - Obbligo di progetto per categoria c) (riscaldamento, climatizzazione)

| Condizione | Soglia | Riferimento |
|-----------|--------|-------------|
| Potenza termica nominale (impianto riscaldamento) | > 35 kW | Art. 6 co. 1 lett. d) |
| Impianto di climatizzazione/condizionamento | > 35 kW | Art. 6 co. 1 lett. d) |

Se il progetto era obbligatorio: allegare progetto + schema impianto (come per cat. a).

Per impianti termici civili: se la potenza e' <= 35 kW, il progetto non e' obbligatorio ex DM 37/2008 (ma verificare se altri regolamenti - es. regolamento edilizio comunale, DGUE regionale - richiedono documentazione aggiuntiva).

### Passo 4 - Obbligo di progetto per categoria e) (gas)

| Condizione | Soglia | Riferimento |
|-----------|--------|-------------|
| Portata termica dell'impianto gas | > 35 kW | Art. 6 co. 1 lett. c) |

Nota: la UNI 7129 (impianti gas per uso domestico) definisce soglie e requisiti tecnici aggiuntivi che l'installatore deve dichiarare nella DdC come norma applicata. Per impianti sopra soglia, la UNI 11528 (impianti a gas di portata maggiore) e' la norma tecnica di riferimento.

### Passo 5 - Obbligo di progetto per categoria d) (idrico-sanitario)

| Condizione | Soglia | Riferimento |
|-----------|--------|-------------|
| Edificio di civile abitazione | > 16 unita' abitative | Art. 6 co. 1 lett. e) |
| Edificio commerciale/terziario/produttivo | superficie > 1000 mq | Art. 6 co. 1 lett. e) |

### Passo 6 - Categorie con obbligo di progetto incondizionato

**Categoria g) (protezione antincendio)**: il progetto e' sempre obbligatorio ai sensi dell'Art. 6 co. 1 lett. f). Non esistono soglie: qualsiasi impianto di protezione antincendio richiede progetto.

**Categoria f) (sollevamento - ascensori, montacarichi)**: gli ascensori sono soggetti a disciplina speciale (DPR 162/1999 e DM 587/1987) che prevede propri obblighi progettuali e di collaudo. Il DM 37/2008 si applica ma e' integrato dalla normativa specifica di settore.

### Passo 7 - Riepilogo e output

Produrre il seguente report:

```markdown
# Allegati obbligatori DdC - DM 37/2008

**Categoria impianto**: [a-g]
**Tipo intervento**: [nuova installazione / trasformazione / ampliamento]
**Caratteristiche dichiarate**: [elenco dati rilevanti forniti]

## Obbligo di progetto

[SI / NO / DA VERIFICARE]

Motivazione: [es. "Potenza dichiarata 8 kW > soglia 6 kW Art. 6 co. 1 lett. a) DM 37/2008"]

## Allegati obbligatori per la DdC

### Sempre obbligatori (Art. 7 co. 2 DM 37/2008)
- [X] Relazione con tipologia dei materiali utilizzati

### Obbligatori condizionali
- [X / ] Schema dell'impianto realizzato - [obbligatorio: si/no - motivo]
- [X / ] Progetto di impianto redatto da tecnico abilitato - [obbligatorio: si/no - motivo]
- [ ] Libretto di impianto (per impianti termici - obbligatorio per impianti cat. c) secondo DPR 74/2013)

## Raccomandazioni anche se non obbligatori per legge

- Schema dell'impianto: [raccomandato per facilita' di manutenzione futura, anche quando non obbligatorio]
- ...

## Avvertenze

[Eventuali incertezze sulle soglie, variazioni regionali, normativa speciale di settore]

## Rinvio al responsabile tecnico

La responsabilita' di determinare correttamente gli obblighi documentali e di redigere la DdC con i corretti allegati resta in capo al responsabile tecnico firmatario. In caso di dubbio sulle soglie o sull'applicabilita' delle norme di settore, consultare un tecnico abilitato o la CCIAA competente.
```

## Note su normativa collegata

### Impianti termici - Libretto impianto
Per gli impianti di riscaldamento (cat. c), il DPR 16 aprile 2013 n. 74 (recepimento Direttiva 2010/31/UE sull'efficienza energetica degli edifici) richiede il **libretto di impianto** o **libretto di centrale** come documento separato dalla DdC. L'installatore deve compilarlo e consegnarlo al responsabile dell'impianto.

### Impianti gas - Verifiche aggiuntive
Per gli impianti gas (cat. e), dopo il rilascio della DdC, e' necessaria la **verifica di tenuta** dell'impianto prima della messa in servizio. La DdC attesta la conformita' ma non sostituisce la verifica di tenuta obbligatoria.

### Impianti elettrici - Denunce ASL/INAIL
Per gli impianti di messa a terra e protezione scariche atmosferiche (rientranti in cat. a), la **denuncia/dichiarazione di conformita' agli impianti di terra** va presentata all'ente competente (ex ISPESL, ora INAIL o ASL secondo regioni) ai sensi del DPR 462/2001. Questa e' un adempimento **separato** dalla DdC DM 37/2008 e non sostituisce ne' e' sostituita da essa.
