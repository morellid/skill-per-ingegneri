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

Le soglie nell'estratto sono tratte dal PDF MIMIT (testo originale 2008, SHA256 verificato).
Per uso operativo, confrontare con il testo consolidato su Normattiva per eventuali modifiche
successive. In caso di dubbio, la scelta cautelativa e' sempre redigere il progetto da professionista.

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

Il DM 37/2008 Art. 5 co. 2 distingue tre sottocasi per cat. a):

**Utenze residenziali (Art. 5 co. 2 lett. a):**

| Condizione | Soglia | Obbligo |
|-----------|--------|---------|
| Utenze condominiali | qualsiasi | Progetto professionista |
| Potenza impegnata (unita' abitativa) | > 6 kW | Progetto professionista |
| Superficie (unita' abitativa) | > 400 mq | Progetto professionista |

**Utenze non residenziali - attivita' produttive/commerciali/terziarie (Art. 5 co. 2 lett. c):**

| Condizione | Soglia | Obbligo |
|-----------|--------|---------|
| Tensione di alimentazione | > 1000 V | Progetto professionista |
| Potenza impegnata | > 6 kW | Progetto professionista |
| Superficie | > 200 mq | Progetto professionista |

**Ambienti particolari (Art. 5 co. 2 lett. d):**

| Condizione | Obbligo |
|-----------|---------|
| Locali adibiti ad uso medico | Progetto professionista |
| Locali con pericolo di esplosione (ATEX) | Progetto professionista |
| Locali a maggior rischio di incendio | Progetto professionista |
| Protezione scariche atmosferiche (edifici volume > 200 mc) | Progetto professionista |

#### Categoria b) - Radiotelevisivo/elettronico

- **Impianti elettronici che coesistono con impianti elettrici con obbligo di progettazione**
  (Art. 5 co. 2 lett. e): segue l'obbligo dell'impianto elettrico associato.
- **Lampade fluorescenti a catodo freddo** (Art. 5 co. 2 lett. b): progetto professionista se
  gia' obbligatorio per l'impianto elettrico, e in ogni caso se potenza complessiva > **1200 VA**
  resa dagli alimentatori.

#### Categoria c) - Riscaldamento/climatizzazione

| Condizione | Obbligo |
|-----------|---------|
| Impianti dotati di canne fumarie collettive ramificate | Progetto professionista |
| Potenzialita' frigorifera >= 40.000 frigorie/ora | Progetto professionista |

_(Art. 5 co. 2 lett. f - letto da PDF MIMIT, SHA256 verificato)_

**Nota**: Il testo originale del 2008 non prevede una soglia di portata termica (es. 35 kW) per
cat. c) in generale. Il criterio e' la presenza di canne fumarie collettive ramificate oppure la
potenzialita' frigorifera >= 40.000 frigorie/ora. Per verificare eventuali modifiche nel testo
consolidato vigente, consultare Normattiva.

#### Categoria d) - Idrico-sanitario

Il testo originale del DM 37/2008 (Art. 5 co. 2) NON include casi specifici per cat. d) che
richiedano un professionista. La progettazione e' sempre richiesta (Art. 5 co. 1 include d)),
ma e' redatta dal responsabile tecnico dell'impresa installatrice (Art. 7 co. 2), non da un
professionista esterno, salvo normative piu' rigorose applicabili al caso specifico.

Per verificare se il testo consolidato vigente (Normattiva) ha introdotto soglie specifiche per
cat. d), consultare Normattiva prima dell'uso operativo.

#### Categoria e) - Gas

- **Portata termica > 50 kW**: Progetto professionista (Art. 5 co. 2 lett. g)
- **Canne fumarie collettive ramificate**: Progetto professionista (Art. 5 co. 2 lett. g)
- **Gas medicali per uso ospedaliero e simili** (compreso stoccaggio): Progetto professionista
  (Art. 5 co. 2 lett. g)

_(letto da PDF MIMIT, SHA256 verificato - la soglia e' 50 kW, non 35 kW)_

#### Categoria f) - Sollevamento (ascensori, montacarichi)

La categoria f) NON e' inclusa nell'Art. 5 co. 1 del DM 37/2008: e' soggetta a disciplina
specifica (DPR 30 aprile 1999, n. 162 per ascensori; DM 587/1987 per montacarichi).
Il DM 37/2008 si applica per gli aspetti non disciplinati dalla normativa specifica.
Indicare all'utente la necessita' di verificare la normativa specifica di settore.

#### Categoria g) - Antincendio

Progetto da professionista obbligatorio nei seguenti casi (Art. 5 co. 2 lett. h):
- Attivita' soggetta al rilascio del **certificato prevenzione incendi (CPI)**
- In ogni caso: numero di idranti >= **4**
- In ogni caso: numero di apparecchi di rilevamento >= **10**

_(letto da PDF MIMIT, SHA256 verificato)_

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

Le soglie Art. 5 indicate sono tratte dal testo originale del DM 37/2008 (PDF MIMIT, SHA256
verificato, letto in data 2026-05-10). Per uso operativo, verificare il testo consolidato vigente
su Normattiva per eventuali modifiche successive. In caso di dubbio, la scelta cautelativa e'
sempre redigere il progetto da professionista.

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
