# Task - Scelta tipologia atto Pregeo e check pre-trasmissione Catasto Terreni

## Obiettivo

Aiutare il professionista a:

1. classificare correttamente l'atto di aggiornamento del Catasto Terreni nella tipologia codificata da inserire in **riga 9** del libretto delle misure (menu a tendina "elenco atto aggiornamento" della procedura Pregeo 10);
2. verificare se l'atto rientra nel nuovo regime di **deposito telematico** ex art. 30 co. 5-bis DPR 380/2001 (Risoluzione AdE 40/E del 9/6/2025);
3. eseguire un **check pre-trasmissione** delle componenti che, se non conformi, causano sospensione o rigetto dell'atto in fase di approvazione automatica (cfr. Circolare AdE Territorio 3 del 16/10/2009, par. 6).

L'output e' una **scheda di tipizzazione + checklist conforme/non conforme** + bozza testuale della dichiarazione sostitutiva da inserire (riga 9 nella nuova versione 10.6.5 - APAG 2.15).

## Input richiesti

Chiedi all'utente, prima di iniziare la procedura:

1. **Versione di Pregeo in uso** (es. "10.6.5 - APAG 2.15"). Se l'utente non sa, rinvia alla scheda AdE "Software Pregeo" (cfr. `references/sources.yaml: ade-istruzioni-pregeo-software`). **Dal 1/7/2025 e' obbligatoria la 10.6.5 - APAG 2.15** (Risoluzione AdE 40/E 2025 nota 5: gli atti predisposti con versione precedente, presentati telematicamente dal 1/7/2025, sono respinti dal sistema).
2. **Descrizione sintetica dell'intervento** sul Catasto Terreni: e' una nuova costruzione / ampliamento / demolizione di fabbricato? una suddivisione di particella? una variazione di coltura/qualita'? un atto su area demaniale, acque, strade?
3. **Riferimenti catastali di partenza**: foglio, particella, qualita' (Ente Urbano, seminativo, vigneto, ecc.), eventuale presenza di subalterni gia' censiti.
4. **Estratto di mappa**: e' stato richiesto e rilasciato dall'Ufficio via Sister? Oppure si intende usare un estratto autoallestito (caso ammesso solo per TM con conferma posizione fabbricato in esenzione tributi - Circ. 3/2009 par. 5)?
5. **Punti Fiduciali**: archivio mutue distanze scaricato e aggiornato? Misure topografiche nei limiti di tolleranza ex Decreto direttoriale 4A/322 del 19/1/1988?
6. **Per gli atti di frazionamento**: l'atto e' presentato telematicamente (regime ordinario per professionisti, Provv. AdE 11/3/2015) oppure su supporto informatico presso l'Ufficio (caso residuale per irregolare funzionamento Sister)?

## Fonti

- `references/estratti/dpr-380-2001-art-30.md` - regime deposito ante/post 1/7/2025
- `references/estratti/circolare-3-2009-pregeo10.md` - tipologie atti, controlli automatici, cause di rifiuto
- `references/estratti/risoluzione-40-2025-deposito-telematico.md` - ambito FR/FM/SC, dichiarazioni riga 9
- `references/sources.yaml`: `ade-circolare-44-2016-pregeo`, `ade-circolare-11-2023-frazionamento-enti-urbani`, `ade-istruzioni-pregeo-software`

## Procedura

### 1. Tipizzazione dell'atto Pregeo

Confronta la descrizione dell'intervento con la tassonomia ufficiale. Mappa l'atto in una delle famiglie:

| Famiglia | Codici tipici | Descrizione |
|---|---|---|
| **Tipo Mappale (TM)** | varie tipologie codificate nell'Allegato 2 della Circ. 3/2009 | inserimento o modifica di fabbricato su particella del CT (nuova costruzione, ampliamento, demolizione totale/parziale, modesta entita' < 20 mq, conferma di mappa) |
| **Tipo Frazionamento (FR)** | tipologie codificate per FR | suddivisione di una particella in due o piu' nuove particelle |
| **Atto Misto (FM)** | codici FM | combinazione TF + TM in un unico atto |
| **Tipo Mappale con Stralcio di Corte (SC)** | codici SC | TM con contestuale stralcio dell'area di corte da una particella urbana |
| **Tipo Particellare (TP)** | codici TP | modifica qualita'/classe/consistenza di particelle CT senza modifica geometrica - **escluso dall'approvazione automatica** (Circ. 3/2009 par. 5) |
| **Atti per acque, strade, demaniali, esenzione tributi** | codici dedicati | iter speciale, **esclusi dall'approvazione automatica** |
| **Frazionamento Enti Urbani** | codici 282, 278 | disciplina specifica - Circ. 11/E 2023; eccezione tavolare per Libro Fondiario (Risoluzione 40/E 2025 nota 5) |

> **Importante**: la skill non puo' inventare il codice numerico esatto della tipologia in riga 9. Il codice si seleziona dal menu a tendina "elenco atto aggiornamento" della procedura Pregeo 10 (sezione 2.3 Circ. 3/2009). Se non e' chiaro quale scheda dell'Allegato 2 calzi, rinvia al PDF originale (`not_in_repo/circolare-3-2009-pregeo10.pdf`) o al manuale operativo del software per la versione in uso.

Per ciascuna tipologia, verifica i requisiti specifici dalla scheda esemplificativa dell'Allegato 2:
- riga 0 (Standard o Modesta Entita');
- libretto delle misure obbligatorio o facoltativo;
- estratto di mappa rilasciato dall'Ufficio o autoallestito;
- proposta di aggiornamento richiesta o no;
- dichiarazione di conformita' nella relazione tecnica strutturata;
- schema censuario (originali, soppresse, costituite, variate).

### 2. Disciplina del deposito comunale

Applica il decision tree:

```
L'atto e' FR, FM oppure SC?
|-- SI:
|   E' presentato telematicamente?
|   |-- SI: regime art. 30 co. 5-bis DPR 380/2001 (Risoluzione 40/E 2025).
|   |   - il professionista NON deposita presso il Comune;
|   |   - in riga 9 del libretto delle misure dichiara, ex artt. 38 e 47 DPR
|   |     445/2000, che l'atto e' oggetto di deposito presso il Comune
|   |     competente ai sensi dell'art. 30 co. 5-bis DPR 380/2001 OVVERO che
|   |     ricorrono le condizioni di esonero dall'obbligo di deposito;
|   |   - l'AdE deposita sul Portale dei Comuni e comunica via PEC unica
|   |     depositofrazionamenticatastali@pec.agenziaentrate.it.
|   |-- NO (presentazione su supporto informatico presso l'Ufficio per
|       irregolare funzionamento Sister): regime previgente art. 30 co. 5
|       (deposito comunale a cura del professionista PRIMA dell'invio).
|-- NO (TM ordinario, TP, atti speciali): regime previgente art. 30 co. 5
    se l'atto rientra nell'obbligo di deposito comunale (lo verifica il
    professionista in base al titolo edilizio sottostante e al CDU).
```

> **Errore bloccante**: per atti FR/FM/SC trasmessi telematicamente dopo il 1/7/2025, il deposito comunale a cura del professionista rende l'atto privo di effetti (Risoluzione 40/E 2025 nota 4). Segnala questo come blocker.

### 3. Versione del software

Verifica la versione di Pregeo dichiarata dall'utente:

| Versione | Stato | Conseguenza |
|---|---|---|
| 10.6.5 - APAG 2.15 | obbligatoria dal 1/7/2025 | OK per tutti gli atti, compresi FR/FM/SC con dichiarazione 5-bis |
| 10.6.4 - APAG 2.15 o precedenti | non ammessa dal 1/7/2025 | **respinta dal sistema telematico** (Risoluzione 40/E 2025 nota 5). Aggiornare prima di trasmettere. |
| versioni < 10.6.0 | non aggiornate dal 2016 | non utilizzabili per nuove approvazioni automatiche |
| 10.6.5 con patch tavolare | ammessa per frazionamento Enti Urbani in zone Libro Fondiario (codici 282, 278) | giustificazione obbligatoria nella **Relazione Tecnica Libera** (Risoluzione 40/E 2025 nota 5) |

### 4. Check pre-trasmissione (controlli automatici Pregeo 10)

Esegui la checklist sui controlli che il software eseguira' (Circ. 3/2009 par. 2.7-2.9 e Allegato 5):

- [ ] **Estratto di mappa rilasciato dall'Ufficio** via Sister (vincolante salvo eccezione TM con conferma posizione fabbricato in esenzione tributi);
- [ ] **Riga 9 del libretto delle misure** compilata con la tipologia esatta selezionata dal menu;
- [ ] **Riga 0**: modalita' Standard, oppure Modesta Entita' solo se la scheda della tipologia lo prevede (es. TM per fabbricati < 20 mq);
- [ ] **Distanze fra coppie di Punti Fiduciali** entro la tolleranza ex Decreto direttoriale 4A/322 del 19/1/1988; in caso negativo, dichiarazione esplicita nella relazione tecnica strutturata che le proprie misure sono corrette;
- [ ] **Semiasse maggiore dell'ellisse di errore** <= 10 cm; se superato, dichiarazione codificata nella relazione strutturata che illustra l'impossibilita' di realizzare schemi di rilievo ottimizzati (cfr. testo predefinito Allegato 4 Circ. 3/2009);
- [ ] **Deformazione massima delle entita' cartografiche** entro l'indice di affidabilita' della mappa per l'area; se superata, dichiarazione codificata nella relazione strutturata;
- [ ] **Modello censuario** coerente: somma delle particelle "costituite" = particelle "originali" - particelle "soppresse" + variate; per ciascuna nuova particella, qualita', classe, superficie compatibili con la scheda della tipologia;
- [ ] **Proposta di aggiornamento** generata dal software (file grafico) presente, salvo le tipologie per cui la scheda dell'Allegato 2 la esonera (es. Tipologia 1 - TM con conformita' di mappa);
- [ ] **Dichiarazione tecnica della tipologia** inserita nella relazione strutturata (formula predefinita selezionata dall'elenco - es. "La/e particella/e ... corrisponde/ono a quanto rappresentato sulla mappa del Catasto Terreni e che il fabbricato e' correttamente inserito nella cartografia" per la Tipologia 1);
- [ ] **Per FR/FM/SC dal 1/7/2025**: dichiarazione sostitutiva ex artt. 38 e 47 DPR 445/2000 in riga 9 sulla soggezione al deposito ex art. 30 co. 5-bis DPR 380/2001 o sulle condizioni di esonero;
- [ ] **Per atti diversi da FR/FM/SC**: attestazione di avvenuto deposito presso il Comune (regime previgente art. 30 co. 5), se applicabile;
- [ ] **Tributi e bolli**: presenza nella ricevuta Sister (escluse le esenzioni di cui all'allegato 2 della Circ. 3/2009);
- [ ] **Punti Fiduciali**: archivio mutue distanze aggiornato (pubblicato mensilmente dall'AdE).

### 5. Output

Produci una scheda strutturata con:

1. **Tipologia identificata** (es. "Tipo Frazionamento - FR - codice indicativo da menu Pregeo 10.6.5"). Se la skill non riesce a determinare la tipologia esatta, segnala l'incertezza e proponi 2-3 opzioni con il rinvio alla scheda Allegato 2 della Circ. 3/2009.
2. **Regime di deposito comunale**: art. 30 co. 5-bis (deposito a cura AdE) oppure art. 30 co. 5 (deposito a cura professionista).
3. **Versione Pregeo richiesta**.
4. **Bozza testuale della dichiarazione in riga 9** (per FR/FM/SC dal 1/7/2025) - una variante "deposito" e una variante "esonero", da scegliere a cura del professionista in base alla situazione concreta.
5. **Checklist** dei controlli pre-trasmissione (conforme / non conforme / da verificare a cura del professionista) con riferimento alla fonte (Circ. 3/2009 par. ...).
6. **Limiti**: elementi che la skill non puo' verificare (correttezza topografica delle misure, accuratezza dell'inquadramento, qualita' del rilievo GNSS, individuazione corretta dei PF in campo).
7. **Rinvio**: al manuale operativo Pregeo 10.6.5 - APAG 2.15 sulla scheda AdE per la procedura di compilazione campo-per-campo, e al firmatario per la responsabilita' professionale (artt. 359, 481 c.p. + art. 76 DPR 445/2000).

## Limiti

Il task NON:

- riproduce il manuale operativo Pregeo (link in `sources.yaml: ade-istruzioni-pregeo-software`);
- inventa il codice numerico esatto della tipologia in riga 9 (selezionabile dal menu del software);
- esegue calcoli topografici (compensazione, riduzione GNSS, calcolo coordinate PF);
- valuta la qualita' del rilievo in campo (taratura strumenti, accessibilita' PF);
- sostituisce il sopralluogo;
- gestisce gli adempimenti civilistici e fiscali collaterali (atto traslativo, dichiarazione di successione, voltura).

Il **firmatario dell'atto** resta responsabile penalmente, civilmente e disciplinarmente per la veridicita' delle dichiarazioni rese ai sensi degli artt. 38 e 47 DPR 445/2000 (sanzioni ex art. 76 DPR 445/2000 + artt. 359 e 481 c.p.).
