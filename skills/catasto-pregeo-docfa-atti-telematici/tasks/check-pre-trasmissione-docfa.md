# Task - Check pre-trasmissione Docfa: Quadro D, EP, ES, ET, planimetrie

## Obiettivo

Eseguire la **checklist di completezza e conformita'** dell'atto Docfa prima della trasmissione telematica via Sister, con focus su:

- **Quadro D - Note relative al documento e relazione tecnica**: dichiarazioni obbligatorie e formule standardizzate (Vademecum Docfa cap. 2.4.2);
- **Elaborato Planimetrico (EP)**: casi di obbligatorieta' e contenuto (cap. 3.1.1);
- **Elenco Subalterni (ES)**: descrizione dei subalterni, BCC/BCNC, graffati, corti esclusive (cap. 3.1.2);
- **Entita' Tipologiche (ET)**: codifica CF/AL/AC/CI/CS per le sole dichiarazioni di accatastamento (cap. 3.1.3);
- **Planimetrie delle UIU**: scala, quotature, esposizione, denominazione locali (cap. 3.2);
- **Coerenza fra Quadro A/B, Quadro U (UIU), Quadro Dati Dichiarante** e modelli 1N (Gruppi A, B, C) o 2N (Gruppi D, E).

L'output e' una **checklist conforme/non conforme** + bozza testuale delle dichiarazioni del Quadro D mancanti, con rinvio al Vademecum.

## Input richiesti

Chiedi all'utente:

1. **Causale di presentazione** (gia' identificata nel task `scelta-causale-categoria-docfa.md`).
2. **Categoria catastale proposta** per ogni UIU (Gruppo F? quale F/x?).
3. **Numero di UIU** dichiarate (1, 2, ..., n) e di BCC/BCNC.
4. **Documenti gia' predisposti**: EP, ES, planimetrie di ciascuna UIU, modelli 1N o 2N, Quadro D, autocertificazioni (es. DSAN ex art. 47 DPR 445/2000 per F/2 sull'assenza di allacci a reti pubbliche), eventuali allegati (foto per F/2, relazione stato lavori per F/3, attestazione AdE per causale "presentazione planimetria mancante").
5. **Riferimenti catastali**: foglio, particella, sezione (per Comuni con sezioni), eventuali subalterni esistenti.
6. **Contesto del fabbricato**: e' un fabbricato singolo o promiscuo (con UIU di CF + particelle di CT)? Esistono BCC o BCNC gia' censiti agli atti?

## Fonti

- `references/estratti/dm-28-1998-uiu.md` - condizioni applicabilita' Gruppo F (vincoli cap. 1.2.4 Vademecum)
- `references/estratti/vademecum-docfa-elaborato-planimetrico.md` - EP, ES, ET, Quadro D
- `references/estratti/vademecum-docfa-categorie-causali.md` - causali, categorie, modelli 1N/2N
- `references/sources.yaml`: `ade-vademecum-docfa-v1`, `dm-138-1998-superficie-catastale`

## Procedura

### 1. Quadro D - dichiarazioni obbligatorie

Verifica la presenza nel Quadro D delle dichiarazioni obbligatorie in base alla causale e alla categoria, secondo l'elenco indicativo del Vademecum cap. 2.4.2:

- [ ] Se il **dichiarante non e' tra gli intestatari catastali**: specificata la qualifica con cui sottoscrive (es. delegato, erede, amministratore di condominio, curatore fallimentare).
- [ ] Per UIU in **F/1** ottenute da frazionamento al CF di unita' gia' censite (senza preventivo frazionamento dell'ente urbano al CT): indicato lo scopo della presentazione del documento di aggiornamento tecnico, sulla base di eventuale dichiarazione del titolare di diritti. **L'assenza di questo elemento rende l'atto inidoneo alla registrazione** (Vademecum cap. 1.2.4 nota 30).
- [ ] Per UIU in **F/3**: descritto lo stato dei lavori al momento della dichiarazione (Vademecum cap. 1.2.4 + cap. 2.4.2). Allegata relazione tecnica supplementare se necessaria.
- [ ] Per UIU in **F/4**: dichiarato che "trattasi di intervento di ristrutturazione edilizia ai sensi del D.P.R. 380/01, articolo 3 comma 1 lettera d" (Vademecum cap. 2.4.2). Verificare anche che il fabbricato sia composto da PIU' UIU (Vademecum cap. 1.2.4): se l'UIU e' unica, F/4 NON e' ammessa.
- [ ] Per UIU in **F/2**: presenza della DSAN dell'intestatario ex artt. 47 e 76 DPR 445/2000 sull'assenza di allacciamento alle reti dei servizi pubblici di energia elettrica, acqua e gas; documentazione fotografica e relazione che attestino lo stato di degrado (Vademecum cap. 1.2.4); copia documento di identita' del sottoscrittore.
- [ ] Per causale **Unita' afferenti - Altro: RECUPERO PER ERRATA SOPPRESSIONE**: motivata l'utilizzo del tipo di operazione "R - Recuperata".
- [ ] Per dichiarazioni di **porzioni di UIU**: riportata l'affermazione "Porzione di UIU unita di fatto con quella di foglio xxx part. yyy sub zzz. Rendita attribuita alla porzione di UIU ai fini fiscali".
- [ ] Per causale **Demolizione totale** SENZA costituzione di area urbana F/1: dichiarato che "A seguito di demolizione totale, l'area di risulta non viene costituita come area urbana ma acquisisce le caratteristiche di area destinata alla produzione agricola".
- [ ] Per causale **Presentazione planimetria mancante**: indicati i riferimenti dell'attestazione rilasciata dall'Ufficio (rasterizzazione vs accertamento d'Ufficio).
- [ ] Se sono usate **causali multiple non tutte indicabili nella Sezione Causale**: specificate le causali aggiuntive nel Quadro D.
- [ ] In presenza di **Docfa concatenati**: indicato "Docfa N di M".
- [ ] Per ciascun **allegato**: elencato (es. "Allegata DSAN ex art. 47 DPR 445/2000 sull'assenza di allacci ai servizi pubblici, copia C.I., relazione descrittiva, n. 6 foto").
- [ ] In presenza di **difficolta' oggettive di misurazione** dello spessore dei muri: esplicitata.

### 2. Elaborato Planimetrico (EP)

Verifica obbligatorieta' e contenuto (Vademecum cap. 3.1.1):

- [ ] **EP obbligatorio se** ricorre uno dei casi:
  - costituzione di due o piu' UIU (di fatto sempre obbligatorio quando ci sono almeno 2 UIU);
  - costituzione/variazione di unita' in categorie del Gruppo F;
  - costituzione/variazione di BCNC;
  - variazione che genera/cancella/modifica geometrie su EP gia' agli atti;
  - dichiarazione su fabbricati promiscui.
- [ ] **Scala**: 1:500 o 1:200, in funzione delle dimensioni.
- [ ] **Simbolo orientamento** in basso a destra.
- [ ] **Perimetro del lotto urbano** con almeno due particelle/strade/acque a confine.
- [ ] Per ogni piano: **perimetro parti edificate, coperte e scoperte**.
- [ ] Per ogni piano: **parti comuni** (cortili, ingressi, vani scale, centrale termica, ascensore) - linea di confine continua e completa.
- [ ] Per ogni piano: **perimetro singole UIU + accessi** (segmento ortogonale al perimetro in corrispondenza dell'apertura).
- [ ] **Subalterno o numero di mappa** indicato per ogni porzione, copre l'intera superficie di piano.
- [ ] Linea **tratto-punto** per confini fra particelle adiacenti (se rappresentate piu' particelle urbane).
- [ ] **Riferimenti di piano** (terra, primo, ecc.).
- [ ] Quotatura solo nella scheda del piano terra (facoltativa) - se gia' presente in EP storico va mantenuta e aggiornata limitatamente alle porzioni interessate.
- [ ] **NON inserire**: spessore dei muri, altezze dei locali, protocollo del TM, elementi del rilievo topografico, commenti non pertinenti.

### 3. Elenco Subalterni (ES)

Verifica (Vademecum cap. 3.1.2):

- [ ] ES presente e collegato all'EP (sono parte integrante).
- [ ] Per ogni subalterno: **descrizione** chiara della destinazione (abitazione, autorimessa, negozio, ecc.).
- [ ] Per **subalterni graffati**: indicazione "graffato col sub. x" oppure "graffato col mapp. y sub. x".
- [ ] Per **corti esclusive con stesso sub** della UIU: descrizione "abitazione con corte esclusiva", "autorimessa con corte esclusiva", ecc.
- [ ] Per **BCC e BCNC**: indicate le UIU servite (es. "sub xx bene non censibile comune a tutti i subb.: scale, ascensore, centrale termica, area scoperta", "sub yy bene comune censibile ai sub 5 e 6: cantina").
- [ ] Per **subalterni non trattati nella dichiarazione**: descrizione gia' agli atti riportata in modo coerente.

### 4. Entita' Tipologiche (ET)

Verifica per le sole dichiarazioni di **accatastamento** (Vademecum cap. 3.1.3):

- [ ] ET individuate e rappresentate graficamente con codice alfanumerico:
  - **CF** = Costruzione di fabbricato (qualsiasi costruzione fuori terra);
  - **AL** = Area libera (es. posti auto, F/1, BCC condominiali);
  - **AC** = Area coperta (tettoie, tensostrutture - escludono balconi/aggetti);
  - **CI** = Costruzione interrata (volume entro terra calpestabile - le porzioni interne al perimetro CF non hanno valenza autonoma);
  - **CS** = Costruzione sovrastante (sopra superficie con destinazione particolare, es. acque/strade).
- [ ] Codice progressivo per ciascuna ET (es. CF1, CF2, AL1, AC1, CI1).
- [ ] Associazione fra ET e singoli cespiti coerente con EP.

### 5. Planimetrie delle UIU

Verifica (Vademecum cap. 3.2):

- [ ] Una **planimetria per ogni UIU** dichiarata.
- [ ] **Scala 1:200** (o 1:100 per UIU di piccola dimensione).
- [ ] **Quotature** dei muri (interne) corrette e leggibili.
- [ ] **Denominazione dei locali** (cucina, soggiorno, camera, bagno, ripostiglio, balcone, ecc.).
- [ ] **Esposizione prevalente** indicata.
- [ ] **Indicazione dei lati esterni** e degli ingressi.
- [ ] **Indicazione del piano** (terra, primo, secondo, sottotetto, ecc.).
- [ ] Coerenza con il **Quadro U** (consistenza, classamento, ubicazione).

### 6. Quadro U - Dati UIU

Verifica (Vademecum cap. 2.4.1):

- [ ] **Tipo Operazione** corretto (C - Costituita, S - Soppressa, V - Variata, R - Recuperata, ecc.).
- [ ] **Identificativi catastali** completi (sezione, foglio, particella, sub).
- [ ] **Sezione Ubicazione**: indirizzo da stradario certificato; in mancanza, indirizzo per esteso + nota nel Quadro D che lo stradario certificato non lo prevede; per assenza di numero civico: SNC + nota nel Quadro D.
- [ ] **Sezione Dati di Classamento Proposti**:
  - per UIU di Gruppi A/B/C: zona censuaria, categoria, classe, consistenza (vani per A, m3 per B, m2 per C);
  - per UIU di Gruppi D/E: categoria, destinazione d'uso codificata (Vademecum Prospetti 1.6 - 1.24), n° Modelli 2N (= numero di corpi di fabbrica);
  - per UIU di F/1 e F/5: categoria + superficie;
  - per altre UIU di Gruppo F: solo categoria.
- [ ] **Superficie catastale** calcolata secondo Allegato C DPR 138/1998 (per UIU ordinarie) e riportata nel Quadro U.
- [ ] Eventuale annotazione nel Riquadro F del Modello 1N parte II - "Destinazione d'uso e Osservazioni" se il classamento proposto si discosta da quello automatico della procedura o da quello in atti.

### 7. Quadro Dati del Dichiarante

Verifica (Vademecum cap. 2.4.3):

- [ ] Anagrafica del dichiarante completa.
- [ ] Qualifica corretta (intestatario, delegato, erede, amministratore, ecc.).
- [ ] Riferimenti del **titolo giustificativo** dell'intestazione in catasto (data, numero atto, notaio, ecc.).

### 8. Output

Produci una **checklist conforme/non conforme/da verificare** (con riferimenti puntuali al Vademecum) e:

- bozza testuale delle **dichiarazioni mancanti nel Quadro D** in formula standardizzata (es. testo per F/3, F/4, demolizione totale senza area urbana, planimetria mancante);
- elenco di **allegati richiesti ma non ancora prodotti** (DSAN per F/2, relazione stato lavori per F/3, attestazione AdE per planimetria mancante, foto, ecc.);
- elenco di **elementi di EP/ES/ET/planimetrie da correggere o integrare**;
- **rinvio al Vademecum** per la formula esatta del testo da inserire nel Quadro D quando la skill propone una bozza ("controllare il testo sul Vademecum cap. 2.4.2" + paragrafo specifico);
- **rinvio al firmatario** per il giudizio finale di completezza e per la responsabilita' penale (artt. 359, 481 c.p. + art. 76 DPR 445/2000).

## Limiti

Il task NON:

- valuta la **correttezza tecnica della planimetria** (qualita' del disegno, accuratezza delle quotature);
- determina la **superficie catastale numerica** (richiede applicazione coefficienti DPR 138/1998 All. C);
- determina **classe e rendita catastale**;
- interpreta atti notarili o titoli edilizi sottostanti;
- esegue il sopralluogo per perimetrazione UIU e individuazione BCC/BCNC;
- verifica la **legittimita' urbanistica** dell'intervento (titolo edilizio - rinvio alla skill `modulistica-edilizia-unificata`);
- gestisce l'**upload Sister** (cambia con i rilasci - rinvio al manuale Sister).

Il **firmatario del Docfa** resta responsabile per ogni dichiarazione resa.
