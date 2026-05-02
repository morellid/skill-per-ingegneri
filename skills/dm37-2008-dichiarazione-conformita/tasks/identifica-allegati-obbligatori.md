# Task: Identifica allegati obbligatori per categoria di impianto

Determina quali documenti devono essere allegati alla DdC in base alla categoria di impianto (a-g), alle caratteristiche dimensionali/di potenza e alle soglie dell'Art. 5 DM 37/2008.

## Obiettivo

Produrre un elenco preciso degli allegati obbligatori, distinguendo tra:
1. Sempre obbligatori (per tutte le categorie, sempre)
2. Elaborato tecnico minimo (schema o progetto - sempre necessario, varia il livello e l'autore)
3. Progetto da professionista (obbligatorio sopra le soglie Art. 5)

Con citazione normativa per ognuno.

## Input richiesti

Raccogliere dall'utente:

1. **Categoria di impianto** (a-g, Art. 1 DM 37/2008):
   - a) Elettrico (produzione, distribuzione, utilizzo energia elettrica; protezione scariche atmosferiche; automazione porte/cancelli)
   - b) Radiotelevisivo, antenne, elettronico
   - c) Riscaldamento, climatizzazione, condizionamento, refrigerazione, ventilazione
   - d) Idrico-sanitario
   - e) Gas (distribuzione e utilizzo)
   - f) Sollevamento (ascensori, montacarichi, scale mobili)
   - g) Protezione antincendio

2. **Caratteristiche dimensionali/di potenza** (rilevanti per la categoria):
   - Cat. a): potenza impegnata (kW) + superficie unita' immobiliare (mq) + altezza in gronda edificio (m) + numero unita' immobiliari edificio + presenza classificazione ATEX + alimentazione media tensione (si/no)
   - Cat. b): potenza nominale complessiva (VA)
   - Cat. c): portata termica nominale (kW) + potenza frigorifera (frigorie/h) se pertinente
   - Cat. d): numero unita' abitative edificio + superficie utile (se non residenziale)
   - Cat. e): portata termica totale (kW)
   - Cat. f): tipo impianto (ascensore, montacarichi, scala mobile)
   - Cat. g): sempre progetto professionale - non servono dati dimensionali per questa determinazione

3. **Tipo di intervento**: nuova installazione / trasformazione / ampliamento

Se i dati non sono disponibili, procedere con il caso piu' cautelativo e indicare l'assunzione esplicitamente.

## Fonti normative

Prima di procedere, leggere:
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md` - Art. 5 (soglie progetto professionale), Art. 7 co. 1 (allegati DdC) e Art. 7 co. 2 (schema del RT come elaborato minimo)

**ATTENZIONE**: le soglie nell'estratto sono parafrasate e potrebbero differire dal testo vigente su Normattiva. In caso di dubbio o uso operativo, verificare il testo aggiornato.

## Procedura

### Passo 1 - Allegato sempre obbligatorio per tutte le categorie

**Relazione con tipologia dei materiali utilizzati** (Art. 7 co. 1 DM 37/2008):
- Obbligatoria in **TUTTI** i casi, per tutte le categorie a-g, sempre
- Contenuto minimo: tipologia, marca/modello dei principali componenti installati

### Passo 2 - Elaborato tecnico: schema o progetto

**Per tutte le categorie e tutti gli interventi** (nuova installazione, trasformazione, ampliamento),
deve essere predisposto un elaborato tecnico che viene allegato alla DdC (Art. 7 co. 1-2 DM 37/2008):

- **Elaborato minimo (sotto-soglia Art. 5)**: schema dell'impianto realizzato, redatto dal responsabile tecnico dell'impresa installatrice
- **Progetto completo (sopra-soglia Art. 5)**: progetto redatto da professionista iscritto all'albo, allegato insieme allo schema as-built

In entrambi i casi un elaborato tecnico deve essere allegato. La differenza e' il livello di dettaglio e l'autore, non la presenza/assenza.

### Passo 3 - Soglie per obbligo di progetto da professionista (Art. 5)

Determina se le caratteristiche dell'impianto superano le soglie che richiedono un professionista:

#### Categoria a) - Elettrico

| Condizione | Soglia | Obbligo |
|-----------|--------|---------|
| Alimentazione in media tensione | qualsiasi | Progetto professionista |
| Potenza impegnata | > 6 kW | Progetto professionista |
| Luoghi ATEX | qualsiasi | Progetto professionista |
| Altezza in gronda (edifici civili) | > 12 m | Progetto professionista |
| Superficie unita' abitativa | > 200 mq (*) | Progetto professionista |
| Edificio condominiale (impianti comuni) | > 16 unita' immob. | Progetto professionista |

(*) La soglia per unita' abitative residenziali - verificare testo vigente su Normattiva prima
dell'uso operativo: alcune versioni indicano 400 mq. In caso di incertezza, usare la soglia
piu' bassa (200 mq) come misura cautelativa.

#### Categoria b) - Radiotelevisivo/elettronico

- Potenza nominale complessiva > 1200 VA: **verificare testo vigente** - la soglia esatta
  richiede consultazione diretta di Art. 5 DM 37/2008 su Normattiva.

#### Categoria c) - Riscaldamento/climatizzazione

| Condizione | Soglia | Obbligo |
|-----------|--------|---------|
| Portata termica nominale | > 35 kW | Progetto professionista |
| Potenza frigorifera (climatizzazione) | > 40.000 frigorie/h (*) | Progetto professionista |

(*) Verificare testo vigente su Normattiva per la soglia esatta.

#### Categoria d) - Idrico-sanitario

| Condizione | Soglia | Obbligo |
|-----------|--------|---------|
| Edificio di civile abitazione | > 16 unita' abitative | Progetto professionista |
| Edificio commerciale/terziario/produttivo | superficie > 1000 mq | Progetto professionista |

#### Categoria e) - Gas

- Portata termica totale > 50 kW: **verificare testo vigente** - alcune fonti indicano 35 kW.
  Usare la soglia piu' bassa come misura cautelativa.

#### Categoria f) - Sollevamento (ascensori, montacarichi)

Soggetta a disciplina speciale (DPR 162/1999 e DM 587/1987) che prevede obblighi progettuali
e di collaudo specifici. Il DM 37/2008 si applica ma e' integrato dalla normativa di settore.
Indicare all'utente la necessita' di verificare anche la normativa specifica per ascensori.

#### Categoria g) - Antincendio

**Progetto da professionista sempre obbligatorio**, indipendentemente dalle dimensioni.
Non applicare soglie dimensionali: qualsiasi impianto cat. g) richiede progetto professionale.

### Passo 4 - Documenti aggiuntivi per categorie specifiche

**Cat. c) impianti termici**: il DPR 16/04/2013 n. 74 (efficienza energetica) richiede il
**libretto di impianto** (o libretto di centrale per impianti > 35 kW), separato dalla DdC.
L'installatore deve compilarlo e consegnarlo al responsabile dell'impianto.

**Cat. a) messa a terra e protezione scariche atmosferiche**: la DdC DM 37/2008 e' separata
dalla **denuncia/dichiarazione impianti di terra** da presentare a INAIL o ASL ai sensi del
DPR 462/2001. Sono due adempimenti distinti con iter separati.

**Cat. e) gas**: dopo la DdC, la **verifica di tenuta** dell'impianto e' obbligatoria prima
della messa in servizio. Non e' un allegato della DdC ma un atto separato.

### Passo 5 - Riepilogo e output

```markdown
# Allegati obbligatori DdC - DM 37/2008

**Categoria impianto**: [a-g e descrizione]
**Tipo intervento**: [nuova installazione / trasformazione / ampliamento]
**Caratteristiche dichiarate**: [elenco dati forniti]

## Obbligo di progetto da professionista

[SI / NO / DA VERIFICARE - con motivazione e riferimento Art. 5 DM 37/2008]

In ogni caso, deve essere predisposto un elaborato tecnico:
- [Progetto professionale / Schema del responsabile tecnico]

## Allegati obbligatori per la DdC (Art. 7 co. 1-2 DM 37/2008)

### Sempre obbligatori
- [X] Relazione con tipologia dei materiali utilizzati

### Elaborato tecnico (sempre necessario - livello dipende da soglie Art. 5)
- [X] Schema dell'impianto realizzato (da responsabile tecnico) - minimo obbligatorio in tutti i casi
- [X se sopra soglia] Progetto da professionista iscritto all'albo - [si/no - motivazione]

### Specifici per categoria
- [ ] Libretto di impianto (cat. c - obbligatorio per legge DPR 74/2013, separato dalla DdC)

## Adempimenti separati dalla DdC da non dimenticare

[Eventuale lista: denuncia impianto di terra INAIL, verifica tenuta gas, collaudo ascensore, ecc.]

## Avvertenze sulle soglie

Le soglie Art. 5 indicate sono tratte dall'estratto in references/estratti/ che e' una parafrasi
operativa. Prima di qualsiasi applicazione operativa, verificare il testo vigente su Normattiva.
In caso di dubbio, la scelta cautelativa e' sempre redigere il progetto da professionista.

## Rinvio al responsabile tecnico

La responsabilita' di determinare correttamente gli obblighi documentali e di allegare quanto
richiesto resta in capo al responsabile tecnico firmatario. In caso di dubbio sulle soglie o
sulla normativa specifica di settore, consultare un tecnico abilitato o la CCIAA competente.
```

## Casi limite

### Impianto che tocca piu' categorie
Es. rifacimento elettrico + impianto termico nello stesso intervento: la DdC puo' coprire piu'
categorie, ma le soglie di Art. 5 si applicano separatamente a ciascuna. Se una sola delle
categorie supera le soglie, serve il progetto professionale per quella categoria.

### Ampliamento di impianto esistente
L'obbligo di progetto si valuta sull'intero impianto risultante dopo l'ampliamento, non solo
sulla parte aggiunta. Se l'ampliamento porta il totale sopra soglia, il progetto diventa obbligatorio.

### Impianti eseguiti da professionista direttamente
Se il committente e' anche il progettista (es. ingegnere che fa da se'), il regime DM 37/2008
si applica comunque: la DdC e' emessa dall'impresa installatrice, non dal progettista.
