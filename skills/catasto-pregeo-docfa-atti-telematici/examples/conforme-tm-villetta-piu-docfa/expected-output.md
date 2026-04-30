# Output atteso - Workflow conforme: villetta unifamiliare + autorimessa

## 1. Inquadramento del workflow

Si tratta di un workflow **misto Pregeo -> Docfa** in due passi sequenziali:

1. **Pregeo - Tipo Mappale (TM)** per inserire il nuovo fabbricato sulla particella 345 e modificarne la qualita' da seminativo a Ente Urbano. Iscrizione automatica della particella urbana al Catasto Fabbricati in categoria F/6 (Vademecum cap. 1.2.4 - F/6).
2. **Docfa - Accatastamento** delle due UIU (abitazione + autorimessa) con causale "Nuova Costruzione" e sostituzione automatica della F/6 (Vademecum cap. 1.2.4 - F/6 nota 39).

Sequenza obbligata: il Docfa puo' essere trasmesso solo dopo l'approvazione del TM. Cfr. task `workflow-pregeo-docfa.md` paragrafo "Sequenza standard nuova costruzione".

## 2. Risposte puntuali

### 2.1 Che tipo di atto Pregeo e che codice in riga 9?

L'atto Pregeo da redigere e' un **Tipo Mappale (TM)** per nuova costruzione. Trattandosi di particella intera che cambia qualita' (passaggio all'Urbano), e poiche' il rilievo include misure topografiche complete con PF, la tipologia codificata in **riga 9** del libretto delle misure va selezionata dal menu "elenco atto aggiornamento" della procedura Pregeo 10.6.5 - APAG 2.15 nel gruppo dei Tipi Mappali per nuova costruzione su particella intera (cfr. schede Allegato 2 Circ. AdE Territorio 3/2009 e successive integrazioni Circ. 44/E 2016).

> **Nota della skill**: il codice numerico esatto della tipologia va scelto dal menu della procedura Pregeo in funzione della scheda esemplificativa applicabile (l'allegato 2 contiene oltre 40 tipologie codificate). La skill non puo' suggerire un codice numerico vincolante senza accesso all'estratto di mappa rilasciato dall'Ufficio. Verificare la scheda corretta dell'Allegato 2 della Circ. 3/2009 e dei successivi rilasci documentali del software (rinvio: `references/sources.yaml: ade-istruzioni-pregeo-software`).

### 2.2 Si applica il deposito comunale ex art. 30 co. 5-bis?

**No**, non si applica.

L'art. 30 co. 5-bis DPR 380/2001 (introdotto da art. 25 D.Lgs. 1/2024 e operativo dal 1/7/2025 con Provv. AdE 30/12/2024 e Risoluzione AdE 40/E del 9/6/2025) riguarda esclusivamente:

- **Tipi di Frazionamento (FR)**;
- **Atti Misti (FM = TF + TM)**;
- **Tipi Mappali con Stralcio di Corte (SC)**.

Un Tipo Mappale **ordinario** per nuova costruzione su particella intera (senza frazionamento ne' stralcio di corte) NON rientra nell'ambito della Risoluzione 40/E 2025. Per questo TM **permane il regime previgente dell'art. 30 co. 5 DPR 380/2001**: il deposito presso il Comune (se richiesto in base al titolo edilizio sottostante e al CDU) e' a cura del professionista, prima della trasmissione telematica.

> Nel caso in oggetto, trattandosi di TM puro su particella intera con cambio di qualita' a Ente Urbano, valutare se il Comune richiede comunque il deposito (la prassi locale puo' variare). Se il Comune non lo richiede, l'atto si trasmette direttamente via Sister.

### 2.3 Categorie e causale Docfa

**Causale di presentazione (Quadro A)**: **Nuova Costruzione** (Vademecum cap. 2.2.1.4) - fabbricato mai dichiarato al CF.

**Tipologia di documento**: **Dichiarazione ordinaria** (Vademecum cap. 2.2.1.5).

**Categorie proposte**:

| UIU | Descrizione | Categoria proposta | Motivazione |
|---|---|---|---|
| UIU 1 (sub futuro) | villetta unifamiliare ~145 mq, due piani, ingresso, soggiorno, cucina, bagno, 3 camere, doppi servizi | **A/7** (abitazione in villini) | Vademecum cap. 1.2.2 + Prospetto 1.1: villini = abitazioni isolate o a schiera con caratteristiche di pregio costruttivo medio-alto, presenza di area pertinenziale; consistenza in vani utili (Vademecum cap. 1.3.2 Gruppo A) |
| UIU 2 (sub futuro) | autorimessa autonoma ~22 mq, esterna al corpo principale | **C/6** (stalle, scuderie, rimesse, autorimesse) | Vademecum cap. 1.2.2 + Prospetto 1.3 |

> **Nota classamento**: la classe (e quindi la rendita) dipende dalla zona censuaria e dalle caratteristiche intrinseche/estrinseche della UIU (ubicazione, salubrita', servizi pubblici, esposizione, finiture - Vademecum cap. 1.3.1). La determinazione della classe e della rendita resta a cura del professionista, sulla base del Prospetto delle Tariffe d'Estimo vigente per il Comune di Crespina-Lorenzana e per la zona censuaria di ubicazione.

> **Nota corte esclusiva**: l'area scoperta pertinenziale della villetta puo' essere dichiarata come **corte esclusiva** della UIU 1 (stesso subalterno). Va specificato nell'Elenco Subalterni la presenza della corte esclusiva (es. "abitazione con corte esclusiva") - Vademecum cap. 3.1.2.

> **Alternative considerate**:
> - A/2 (abitazione di tipo civile) sarebbe applicabile se la villetta non avesse caratteristiche tipologiche di villino isolato; valutare in base alla prassi locale dell'Ufficio Provinciale Territorio di Pisa e alla comparazione con UIU di riferimento (art. 11 co. 1 DL 70/1988).
> - C/2 (magazzini e locali di deposito) NON e' appropriata per autorimessa funzionale (la categoria C/6 prevale).

### 2.4 Elaborato Planimetrico obbligatorio?

**Si'**, l'EP e' obbligatorio (Vademecum cap. 3.1.1):

- ricorre il caso "costituzione di due o piu' unita' immobiliari" (UIU 1 abitazione + UIU 2 autorimessa);
- ricorre presumibilmente il caso "costituzione di BCNC" se le aree di pertinenza scoperte non sono interamente assegnate come corte esclusiva (es. piccola area di accesso comune, recinzione perimetrale).

L'EP deve contenere (cfr. checklist task `check-pre-trasmissione-docfa.md` - sezione 2):

- simbolo orientamento in basso a destra;
- perimetro del lotto urbano + due particelle/strade/acque a confine (es. particelle 344 e 346 + strada vicinale);
- per ogni piano: perimetro parti edificate, coperte, scoperte;
- perimetro singole UIU + accessi (segmento ortogonale al perimetro);
- subalterni indicati per ogni porzione, copertura completa di tutta la superficie di piano;
- riferimenti di piano (terra, primo);
- scala 1:200 o 1:500;
- **NON inserire**: spessore dei muri, altezze dei locali, protocollo del TM nel cartiglio.

L'**Elenco Subalterni** (ES) accompagna l'EP. Esempio di descrizioni:

- sub 1: "abitazione con corte esclusiva" (UIU 1)
- sub 2: "autorimessa" (UIU 2)
- (eventuale) sub 3: "bene non censibile comune ai sub 1 e 2: area di accesso e recinzione perimetrale" (BCNC)

Per accatastamento serve anche la rappresentazione delle **Entita' Tipologiche** (Vademecum cap. 3.1.3): es. CF1 (corpo villetta), CF2 (corpo autorimessa), AL1 (corte esclusiva e BCNC).

## 3. Checklist pre-trasmissione

### Pregeo (Tipo Mappale)

- [x] Versione Pregeo 10.6.5 - APAG 2.15 (obbligatoria dal 1/7/2025, ok)
- [x] Estratto di mappa rilasciato dall'Ufficio (richiesto via Sister il 23/2/2026)
- [x] Riga 9: tipologia da menu "elenco atto aggiornamento" (TM nuova costruzione)
- [x] Riga 0: Standard
- [x] Distanze fra PF entro tolleranza (4A/322/1988)
- [x] Semiasse maggiore ellisse = 7,2 cm < 10 cm
- [x] Deformazione = 0,18 m < indice affidabilita' 0,42 m
- [x] Modello censuario: particella 345 (originaria, qualita' seminativo) -> particella 345 (variata, qualita' Ente Urbano). Verifica somma superfici.
- [x] Proposta di aggiornamento generata
- [x] Relazione tecnica strutturata con dichiarazioni codificate (nessuna deroga necessaria, valori entro tolleranza)
- [ ] **Da verificare a cura del professionista**: il Comune di Crespina-Lorenzana richiede deposito comunale dell'attestazione ex art. 30 co. 5 per il TM ordinario? Verificare con UTC.

### Docfa (Accatastamento)

- [x] Versione Docfa 4.00.5 (vigente, ok)
- [x] Causale Quadro A: Nuova Costruzione
- [x] Tipologia documento: Dichiarazione ordinaria
- [x] 2 UIU (A/7 + C/6) + eventuale BCNC
- [x] EP obbligatorio (almeno 2 UIU)
- [x] ES con descrizioni complete (corte esclusiva indicata)
- [x] ET CF1, CF2, AL1 (per accatastamento)
- [x] 2 planimetrie (una per UIU)
- [x] Quadro D: nessuna dichiarazione speciale richiesta in questo caso (no F/x, no porzioni, no graffati)
- [x] Quadro Dati Dichiarante completo
- [x] Modelli 1N (parte I e II) per A/7 e per C/6 (categorie ordinarie)
- [ ] **Da verificare a cura del professionista**: classe e consistenza esatta (vani per A/7, mq per C/6) sulla base del Prospetto Tariffe d'Estimo e della prassi locale UPT Pisa
- [ ] **Da verificare a cura del professionista**: coerenza dell'indirizzo proposto con lo stradario certificato (Vademecum cap. 2.4.1.5)

## 4. Limiti di verifica della skill

La skill non ha verificato:

- **correttezza topografica del rilievo** (compete al professionista che ha eseguito le misure);
- **legittimita' urbanistica** del Permesso di Costruire (rinvio alla skill `modulistica-edilizia-unificata`);
- **classe catastale e rendita** (richiede consultazione del Prospetto Tariffe e comparazione con UIU di riferimento - art. 11 co. 1 DL 70/1988);
- **superficie catastale numerica** ex Allegato C DPR 138/1998;
- **deposito comunale** del TM ordinario presso UTC Crespina-Lorenzana (prassi locale).

## 5. Rinvio al professionista

Il geometra firmatario resta responsabile per:

- la veridicita' delle dichiarazioni rese ai sensi degli artt. 38 e 47 DPR 445/2000 (sanzioni ex art. 76 DPR 445/2000 + artt. 359 e 481 c.p. in quanto persona esercente servizio di pubblica necessita');
- la correttezza topografica del rilievo;
- la scelta finale della categoria, classe, consistenza e rendita catastale;
- il classamento e la coerenza con UIU di riferimento;
- l'osservanza della prassi locale dell'Ufficio Provinciale Territorio di Pisa.

Si consiglia di consultare il **Quaderno Docfa** della Direzione Provinciale di Pisa (se pubblicato) per eventuali prassi locali su classamento di villini in zona collinare e tipologia delle pertinenze (link in `references/sources.yaml: ade-quaderno-docfa`).
