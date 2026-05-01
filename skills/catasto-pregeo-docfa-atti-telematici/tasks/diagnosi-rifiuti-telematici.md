# Task - Diagnosi di rifiuti / sospensioni telematiche Pregeo o Docfa

## Obiettivo

Mappare il **messaggio di sospensione, rigetto o non conformita'** ricevuto dall'Ufficio Provinciale Territorio (canale Sister) sulla **causa probabile** e proporre la **correzione** da apportare prima della ri-trasmissione, citando precisamente la fonte normativa.

L'output e' una **scheda di diagnosi** con: classificazione del rifiuto (Pregeo o Docfa, automatico vs tradizionale), cause possibili (probabilita' relativa), interventi correttivi suggeriti, rinvio a task specifici per la ri-redazione.

## Input richiesti

Chiedi all'utente:

1. **Procedura interessata**: Pregeo (Catasto Terreni) o Docfa (Catasto Fabbricati)?
2. **Tipo di esito ricevuto**: rifiuto definitivo (atto inidoneo alla registrazione), sospensione (richiesta integrazione), rinvio al tecnico dell'Ufficio per ulteriori verifiche?
3. **Testo letterale del messaggio** dell'Ufficio (riportato dalla ricevuta Sister o dalla comunicazione PEC).
4. **Tipologia di atto** (per Pregeo: TM, FR, FM, SC, TP, ecc.; per Docfa: causale Quadro A o B + categoria proposta).
5. **Versione del software** in uso al momento della trasmissione.
6. **Riferimenti dell'atto**: protocollo Sister, data trasmissione.

## Fonti

- `references/estratti/circolare-3-2009-pregeo10.md` - cause ricorrenti di rifiuto Pregeo
- `references/estratti/risoluzione-40-2025-deposito-telematico.md` - rifiuti specifici per FR/FM/SC dal 1/7/2025
- `references/estratti/vademecum-docfa-categorie-causali.md` - vincoli su categorie F (cap. 1.2.4)
- `references/estratti/vademecum-docfa-elaborato-planimetrico.md` - obbligatorieta' EP, Quadro D

## Procedura

### 1. Catalogazione del rifiuto

Classifica il rifiuto secondo la combinazione **procedura x esito**:

| Procedura | Esito | Significato |
|---|---|---|
| Pregeo | atto **inidoneo alla registrazione** | uno o piu' controlli automatici hanno fornito esito negativo non giustificato (Circ. 3/2009 par. 6 lett. d) |
| Pregeo | **rinviato al tecnico dell'Ufficio** per ulteriori verifiche | uno dei tre controlli "soglia": distanze fra PF fuori tolleranza misurate dall'Ufficio, semiasse maggiore ellisse > 10 cm, deformazione > indice affidabilita' (Circ. 3/2009 par. 6 lett. c) |
| Pregeo | **non aggiornamento delle basi dati** post-registrazione | controlli di qualita' a valle hanno intercettato fattispecie non gestite dall'automatico (Circ. 3/2009 par. 8) |
| Pregeo telematico FR/FM/SC dal 1/7/2025 | atto **non approvabile** per deposito comunale a cura del professionista | violazione Risoluzione AdE 40/E 2025 nota 4 (deposito comunale duplicato) |
| Pregeo telematico | atto **respinto in fase di trasmissione** | versione software obsoleta (precedente alla 10.6.5 - APAG 2.15 dal 1/7/2025) - Risoluzione 40/E 2025 nota 5 |
| Docfa | richiesta di integrazione su Quadro D, EP, ES, planimetrie | non conformita' a Vademecum cap. 2.4.2 / 3.1 / 3.2 |
| Docfa | rifiuto su categoria proposta | violazione vincoli applicabilita' Gruppo F (Vademecum cap. 1.2.4) o classamento non motivato (cap. 1.3.1) |
| Docfa | richiesta di stradario certificato / chiarimenti su ubicazione | mancato rispetto cap. 2.4.1.5 Vademecum |

### 2. Mapping messaggi -> cause -> correzioni (Pregeo)

Cause ricorrenti dal capitolo "Cause ricorrenti di rifiuto" dell'estratto `circolare-3-2009-pregeo10.md`:

| Messaggio dell'Ufficio (sintetico) | Causa probabile | Correzione |
|---|---|---|
| "Tipologia di atto non coerente con i dati censuari" | riga 9 errata (codice tipologia non corrispondente al caso) | rivedere la scheda dell'Allegato 2 della Circ. 3/2009 e selezionare la tipologia corretta dal menu "elenco atto aggiornamento". Rinvio al task `scelta-tipo-pregeo-e-check.md` |
| "Estratto di mappa non rilasciato dall'Ufficio" / "estratto autoallestito non ammesso" | uso di estratto autoallestito fuori dai casi consentiti (Circ. 3/2009 par. 5) | richiedere via Sister un nuovo estratto di mappa rilasciato dall'Ufficio e ripredisporre l'atto su quello |
| "Distanze fra coppie di Punti Fiduciali fuori tolleranza" | misure topografiche oltre i limiti del Decreto direttoriale 4A/322/1988 | (a) controllare se le proprie misure sono corrette; (b) se si', inserire nella relazione strutturata la dichiarazione predefinita che le proprie misure sono corrette; (c) se le misure sono errate, rifare il rilievo |
| "Semiasse maggiore dell'ellisse di errore > 10 cm" | schemi di rilievo non ottimizzati o complessita' topografica | inserire la dichiarazione codificata che giustifica l'impossibilita' di realizzare schemi ottimizzati (Allegato 4 Circ. 3/2009) |
| "Deformazione massima > indice di affidabilita' della mappa" | mappa con indice basso o errore nel rilievo | inserire la dichiarazione codificata pertinente; in alternativa rivedere il rilievo |
| "Modello censuario incoerente" | somme particelle non quadrano (originali != soppresse + costituite) o qualita'/classe non compatibili con la scheda | ricostruire il modello censuario secondo lo schema della scheda dell'Allegato 2 |
| "Atto privo di attestazione di deposito presso il Comune" | TM ordinario, TP o atti speciali per cui il deposito comunale e' presupposto e manca | depositare presso il Comune e allegare l'attestazione |
| "Atto non approvabile - deposito comunale duplicato" | FR/FM/SC dopo il 1/7/2025 con deposito comunale a cura del professionista | rifare l'atto e dichiarare in riga 9 il regime art. 30 co. 5-bis (Risoluzione AdE 40/E 2025 nota 4) |
| "Atto respinto - versione software non valida" | Pregeo precedente alla 10.6.5 - APAG 2.15 (post 1/7/2025) o 10.6.5 trasmessa prima del 1/7/2025 | aggiornare alla versione vigente o attendere la decorrenza |
| "Punti Fiduciali non aggiornati" | archivio mutue distanze obsoleto | scaricare l'archivio aggiornato dal sito AdE e ripredisporre l'atto |
| "Tipologia esclusa dall'approvazione automatica" | TP, atti su acque/strade, particelle demaniali, atti in esenzione tributi | l'atto deve essere trattato dal tecnico dell'Ufficio in modalita' tradizionale; rinvio al manuale operativo Pregeo per la procedura corretta |

### 3. Mapping messaggi -> cause -> correzioni (Docfa)

| Messaggio dell'Ufficio (sintetico) | Causa probabile | Correzione |
|---|---|---|
| "Causale di presentazione non coerente con la situazione di fatto" | causale Quadro A/B non corretta | rivedere la causale secondo il task `scelta-causale-categoria-docfa.md` (es. "ristrutturazione" invece di "diversa distribuzione spazi interni") |
| "Categoria F/4 non ammessa per UIU unica" | F/4 attribuita a unica UIU oggetto di intervento | F/4 ammessa solo per fabbricati con piu' UIU (Vademecum cap. 1.2.4); per UIU singola la rendita ordinaria gia' tiene conto delle perdite reddituali per manutenzione (cfr. nota 36) |
| "Categoria F/3 non ammessa per UIU gia' censita produttiva di reddito" | F/3 attribuita in dichiarazione di variazione | F/3 ammessa solo per UIU non ultimate al momento dell'accatastamento (Vademecum cap. 1.2.4) |
| "Categoria F/2 non ammessa - immobile iscrivibile in altra categoria o non perimetrabile" | F/2 attribuita impropriamente | F/2 richiede degrado totale + assenza allacci + DSAN + relazione + foto (Vademecum cap. 1.2.4) |
| "Manca dichiarazione su scopo di presentazione - F/1 da frazionamento al CF" | UIU in F/1 da frazionamento al CF di unita' gia' censite, senza scopo nel Quadro D | inserire nel Quadro D lo scopo della presentazione (Vademecum cap. 1.2.4 nota 30 - rende altrimenti l'atto inidoneo) |
| "Manca relazione stato avanzamento lavori per F/3" | UIU in F/3 senza relazione tecnica | allegare relazione che illustri lo stato dei lavori (Vademecum cap. 1.2.4) |
| "Manca DSAN per F/2 sull'assenza di allacciamenti" | UIU in F/2 senza DSAN dell'intestatario ex artt. 47 e 76 DPR 445/2000 | predisporre la DSAN + copia C.I. del sottoscrittore + relazione + documentazione fotografica |
| "Elaborato Planimetrico mancante" | atto con almeno 2 UIU o con UIU di Gruppo F senza EP | predisporre EP secondo Vademecum cap. 3.1.1 |
| "Elenco Subalterni non completo / descrizioni mancanti" | descrizioni di subalterni o BCC/BCNC incomplete | integrare ES con descrizioni di destinazione, indicazione di graffati, corti esclusive, BCC/BCNC e UIU servite (Vademecum cap. 3.1.2) |
| "Entita' Tipologiche non rappresentate" | dichiarazione di accatastamento senza ET | inserire ET (CF, AL, AC, CI, CS) con codice progressivo per ciascuna (Vademecum cap. 3.1.3) |
| "Indirizzo non presente nello stradario certificato" | UIU con indirizzo proposto non trovato in stradario | scrivere indirizzo per esteso e nota nel Quadro D che lo stradario certificato non lo prevede (Vademecum cap. 2.4.1.5) |
| "Manca attestazione AdE per planimetria mancante" | causale "presentazione planimetria mancante" senza riferimento all'attestazione | indicare nel Quadro D i riferimenti dell'attestazione (rasterizzazione vs accertamento d'Ufficio) (Vademecum cap. 2.4.2) |
| "Classamento proposto non coerente con UIU di riferimento" | categoria/classe attribuita non comparabile con UIU di riferimento della zona censuaria | rivedere il classamento secondo Vademecum cap. 1.3.1; per UIU di Gruppo D/E verificare se la stima diretta e' applicata correttamente (Circ. 6/T 2012 + esclusione "imbullonati" L. 208/2015) |

### 4. Indicazioni operative dopo la diagnosi

- Per ogni causa identificata, **identifica il task della skill** che gestisce la correzione (`scelta-tipo-pregeo-e-check.md`, `scelta-causale-categoria-docfa.md`, `check-pre-trasmissione-docfa.md`, `workflow-pregeo-docfa.md`) e rinvia a quello.
- **Documenta la diagnosi**: produci un breve testo che il professionista puo' allegare alla relazione tecnica per giustificare la rielaborazione (es. "in seguito al rifiuto del XX/XX/XXXX prot. NNNNN, l'atto e' stato ridepositato con le seguenti correzioni: ...").
- **Verifica la versione del software**: se il rifiuto deriva da incompatibilita' di versione (Pregeo < 10.6.5 - APAG 2.15 dopo 1/7/2025), aggiornare prima di ri-trasmettere.
- **Verifica le scadenze**: per il deposito comunale ex art. 30 co. 5 (regime previgente) e per la conseguente scadenza dell'attestazione, verificare le tempistiche del Comune di competenza.
- Per rifiuti **non riconducibili alle cause tipizzate** sopra, suggerisci al professionista di:
  - contattare l'**Ufficio Provinciale Territorio** per chiarimenti (numerazione protocollo Sister + descrizione del messaggio);
  - consultare il **Quaderno Docfa** della Direzione Provinciale (link in `sources.yaml: ade-quaderno-docfa`);
  - consultare la **commissione catasto** del proprio Ordine/Collegio.

### 5. Output

Produci una scheda strutturata con:

1. **Procedura e tipo di esito** (es. "Pregeo - rinviato al tecnico dell'Ufficio per ulteriori verifiche").
2. **Causa diagnosticata** (es. "semiasse maggiore ellisse > 10 cm senza dichiarazione codificata") con riferimento a Circ. 3/2009 par. ... o Vademecum cap. ... .
3. **Correzione proposta** (es. "inserire nella relazione tecnica strutturata la dichiarazione predefinita ... selezionata dall'elenco Allegato 4 Circ. 3/2009").
4. Se la causa e' incerta, **lista delle 2-3 cause piu' probabili** con probabilita' relativa indicativa.
5. **Task di rielaborazione** consigliato.
6. **Limiti**: la skill non vede il file Pregeo/Docfa originale ne' il messaggio testuale completo dell'Ufficio; la diagnosi e' di indirizzo, va sempre verificata sul caso specifico.
7. **Rinvio**: al manuale operativo del software, al firmatario per la responsabilita' professionale, eventualmente all'Ufficio Provinciale Territorio per chiarimenti diretti.

## Limiti

Il task NON:

- legge il **file binario Pregeo (.dat / .raw)** o il file Docfa originale;
- accede al **portale Sister** per scaricare la ricevuta o la comunicazione formale del rifiuto;
- valuta la **qualita' tecnica del rilievo topografico** (taratura strumenti, accessibilita' PF);
- sostituisce il **dialogo con l'Ufficio Provinciale Territorio** in casi controversi;
- gestisce le **eventuali sanzioni amministrative** per ritardi nell'aggiornamento catastale.

Il **firmatario** resta responsabile delle correzioni apportate e delle nuove dichiarazioni rese ai sensi degli artt. 38 e 47 DPR 445/2000 (sanzioni ex art. 76 DPR 445/2000 + artt. 359 e 481 c.p.).
