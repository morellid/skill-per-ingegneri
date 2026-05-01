# Task - Workflow misto Pregeo -> Docfa (Tipo Mappale + accatastamento)

## Obiettivo

Guidare il professionista nella **sequenza corretta** di un workflow tipico in cui un nuovo fabbricato (o un ampliamento sostanziale) richiede prima un atto Pregeo (Tipo Mappale o Atto Misto FM) per aggiornare la mappa catastale del Catasto Terreni e poi un atto Docfa per accatastare le UIU al Catasto Fabbricati.

L'output e' una **scheda di workflow** con i passi sequenziali, le precondizioni di ciascun passo, gli adempimenti collaterali (atto notarile, voltura) e i punti di controllo per evitare salti di sequenza.

## Input richiesti

Chiedi all'utente:

1. **Tipo di intervento**: nuova costruzione su area libera; ampliamento di fabbricato esistente; ricostruzione post-demolizione; passaggio dalla qualita' "Ente Urbano" senza fabbricato a fabbricato accatastato.
2. **Stato del Catasto Terreni**: la particella e' gia' di qualita' Ente Urbano? Esiste una particella autonoma per il fabbricato? Esistono particelle limitrofe da accorpare/scorporare?
3. **Stato del Catasto Fabbricati**: il fabbricato e' gia' censito (es. F/6 da precedente Tipo Mappale)? esistono UIU di fatto non dichiarate?
4. **Sequenza prevista**: e' previsto un atto notarile di trasferimento (es. compravendita di parte del lotto)? Quando? Prima o dopo l'accatastamento delle UIU?

## Fonti

- `references/estratti/dpr-380-2001-art-30.md` - regime deposito Tipi di Frazionamento
- `references/estratti/circolare-3-2009-pregeo10.md` - Tipo Mappale e iscrizione automatica F/6
- `references/estratti/dm-28-1998-uiu.md` - condizione di unita' immobiliare
- `references/estratti/vademecum-docfa-categorie-causali.md` - causale "Nuova Costruzione" e "Unita' afferenti"
- `references/sources.yaml`: `ade-circolare-1t-2009-F6` (categoria F/6), `ade-circolare-11-2023-frazionamento-enti-urbani` (frazionamento Enti Urbani)

## Procedura

### 1. Sequenza standard "nuova costruzione"

```
[1] Approvazione del titolo edilizio (PdC, SCIA, CILA, ecc.)
       (rinvio: skill `modulistica-edilizia-unificata`)
       v
[2] Esecuzione dei lavori e ultimazione (anche parziale, per F/3)
       v
[3] Predisposizione del Tipo Mappale Pregeo
       - tipologia: TM, eventualmente con stralcio di corte (SC) o
         in forma mista FM (TM + TF) se l'intervento richiede anche
         frazionamento di particella
       - regime deposito comunale: TM ordinario -> art. 30 co. 5 (deposito
         a cura del professionista); FM/SC dal 1/7/2025 -> art. 30 co. 5-bis
         (deposito a cura AdE - Risoluzione 40/E 2025)
       - software: Pregeo 10.6.5 - APAG 2.15 (obbligatoria dal 1/7/2025)
       v
[4] Trasmissione telematica Pregeo via Sister
       v
[5] Approvazione Pregeo da parte dell'Ufficio
       - per FR/FM/SC dal 1/7/2025: deposito sul Portale dei Comuni a
         cura AdE + comunicazione al Comune via PEC unica
         depositofrazionamenticatastali@pec.agenziaentrate.it
       - per altre tipologie: previo deposito comunale gia' fatto
       v
[6] Iscrizione automatica della particella urbana al CF in categoria F/6
       (Vademecum cap. 1.2.4 - "Fabbricato in attesa di dichiarazione";
       Circ. AdE Territorio 1/T del 8/5/2009)
       v
[7] Predisposizione del Docfa di accatastamento
       - causale: "Nuova Costruzione" se l'intero fabbricato e' nuovo;
         "Unita' afferenti - in sopraelevazione" / "su area di corte" /
         "su area urbana F/1" / "su lastrico solare F/5" se le UIU si
         aggiungono a fabbricato gia' censito
       - per ogni UIU: categoria proposta (Vademecum cap. 1.2);
         eventuali F/3 se non ultimate (con relazione stato lavori in
         Quadro D); eventuali F/4 se in corso di definizione
         (solo per fabbricato con piu' UIU)
       - EP obbligatorio se piu' UIU o presenza Gruppo F (Vademecum cap. 3.1.1)
       - ES obbligatorio (Vademecum cap. 3.1.2)
       - ET (CF, AL, AC, CI, CS) per accatastamento (cap. 3.1.3)
       - planimetrie per ogni UIU (cap. 3.2)
       - software: Docfa 4.00.5 (vigente al last_verified)
       v
[8] Trasmissione telematica Docfa via Sister
       v
[9] Approvazione Docfa - sostituzione automatica della F/6 con le nuove UIU
       (Vademecum cap. 1.2.4 - F/6 nota 39)
       v
[10] Eventuale atto notarile di trasferimento (compravendita, donazione,
       successione)
       v
[11] Voltura catastale post-rogito (a cura del notaio o del professionista
       a seconda del caso) per aggiornare la ditta intestataria
```

### 2. Variante "passaggio all'Urbano di fabbricato gia' presente sulla mappa"

Se il fabbricato e' gia' rappresentato sulla mappa del CT con il proprio numero di particella ma non e' di qualita' Ente Urbano, applicare la **Tipologia 1 dell'Allegato 2 alla Circ. 3/2009** (Tipo Mappale con conformita' di mappa - "Passaggio all'Urbano di Fabbricato Rurale"):

- TM senza necessita' di libretto delle misure ne' di estratto di mappa;
- dichiarazione obbligatoria nella relazione tecnica strutturata: "La/e particella/e ... corrisponde/ono a quanto rappresentato sulla mappa del Catasto Terreni e che il fabbricato e' correttamente inserito nella cartografia";
- dopo l'approvazione, iscrizione automatica della F/6 e prosecuzione del workflow al passo [7].

### 3. Variante "frazionamento + accatastamento"

Se l'intervento richiede prima un frazionamento di particella (es. la nuova UIU sorge su una porzione di particella che va separata dal resto del lotto agricolo), valutare:

- **opzione FM (Atto Misto)**: TF + TM nello stesso atto Pregeo - regime deposito 5-bis dal 1/7/2025;
- **opzione TF + TM separati**: due atti Pregeo distinti, prima il TF poi il TM - regimi deposito eventualmente diversi (TF in regime 5-bis, TM ordinario in regime 5).

Per la scelta fra FM e TF+TM consultare la scheda esemplificativa dell'Allegato 2 della Circ. 3/2009 (Tipologie codificate per FM) e il manuale operativo Pregeo per le ricadute sui codici di riga 9.

### 4. Variante "frazionamento di Enti Urbani"

Se l'intervento riguarda un frazionamento di una particella urbana gia' edificata (cd. frazionamento di Ente Urbano - codici 282, 278), applicare la **Circ. AdE 11/E dell'8/5/2023** (Allegato tecnico con casistiche A-G) e considerare l'eventuale necessita' di Docfa contestuale o successivo.

In zone tavolari (Trentino, Alto Adige, Trieste, Gorizia, parte della Venezia Giulia ex RD 499/1929), eccezione: Pregeo 10.6.5 con patch dedicata + giustificazione obbligatoria nella **Relazione Tecnica Libera** (Risoluzione AdE 40/E 2025 nota 5).

### 5. Adempimenti collaterali (cenni)

La skill richiama, ma non gestisce, gli adempimenti civilistici e fiscali correlati:

- **Atto notarile di trasferimento**: se previsto, deve seguire il Tipo di Frazionamento approvato (art. 30 co. 2 DPR 380/2001 - lottizzazione abusiva). Il notaio richiede l'attestazione di approvazione del Tipo (e per FR/FM/SC dal 1/7/2025 anche la copia della comunicazione PEC al Comune).
- **Voltura catastale**: aggiornamento della ditta intestataria post-rogito. Adempimento del notaio (voltura automatica) o del professionista per casi non automatici (successioni, divisioni).
- **Dichiarazione di successione**: se l'aggiornamento catastale e' funzionale a una successione, coordinare i tempi (Mod. 4 telematico AdE).
- **Dichiarazioni fiscali** (IMU, TARI, Imposta di registro): coordinare con il consulente fiscale/commercialista.

### 6. Punti di controllo (gate)

Prima di passare al passo successivo, verificare:

| Gate | Controllo |
|---|---|
| [3] -> [4] | software Pregeo aggiornato; libretto delle misure completo (riga 9 corretta); estratto di mappa rilasciato dall'Ufficio; relazione strutturata; per FR/FM/SC dal 1/7/2025 dichiarazione 5-bis o esonero in riga 9 |
| [5] -> [6] | esito favorevole dell'Ufficio (attestato di approvazione censuaria + cartografica + per FR/FM/SC: copia PEC al Comune e ricevuta consegna) |
| [6] -> [7] | iscrizione F/6 verificata in visura aggiornata Sister |
| [7] -> [8] | EP, ES, ET, planimetrie completi; Quadro D con tutte le dichiarazioni obbligatorie (rinvio a `check-pre-trasmissione-docfa.md`) |
| [9] -> [10] | UIU correttamente registrate con rendita (per categorie ordinarie) o senza rendita (Gruppo F); F/6 sostituita; eventuali BCC e BCNC dichiarati con identificativi corretti |
| [10] -> [11] | atto notarile registrato e trascritto; estremi dell'atto disponibili per la voltura |

### 7. Output

Produci una scheda strutturata con:

1. **Sequenza** dei passi applicabile al caso (dipende da: nuova costruzione vs ampliamento; frazionamento richiesto o no; passaggio all'Urbano di fabbricato gia' presente sulla mappa).
2. **Atti da redigere**: Pregeo (TM, FM, SC, TF) e Docfa (causale).
3. **Regime di deposito comunale** per ciascun atto Pregeo (5 vs 5-bis).
4. **Versione software** per ciascun atto.
5. **Adempimenti collaterali** (atto notarile, voltura) con tempistica raccomandata.
6. **Gate di controllo** prima di passare a ogni passo successivo.
7. **Limiti**: la skill non gestisce gli adempimenti notarili, fiscali, urbanistici; non fornisce parere sul titolo edilizio (rinvio a `modulistica-edilizia-unificata`).
8. **Rinvio**: ai task specifici della skill per ciascun passo (`scelta-tipo-pregeo-e-check.md` per il Pregeo, `scelta-causale-categoria-docfa.md` + `check-pre-trasmissione-docfa.md` per il Docfa); al manuale operativo del software per la compilazione campo-per-campo; al firmatario per la responsabilita' professionale (artt. 359, 481 c.p. + art. 76 DPR 445/2000).

## Limiti

Il task NON:

- esegue gli **adempimenti notarili** (compravendita, donazione, successione);
- esegue la **voltura catastale** (adempimento del notaio o del professionista in casi specifici);
- valuta la **legittimita' urbanistica** dell'intervento (titolo edilizio - rinvio a `modulistica-edilizia-unificata`);
- gestisce le **dichiarazioni fiscali** (Imposta di registro, IMU, TARI - rinvio al consulente fiscale);
- sostituisce il **dialogo con il notaio** sul coordinamento atto notarile / voltura / Docfa;
- riproduce le **casistiche A-G** dell'Allegato tecnico alla Circ. 11/E 2023 sul frazionamento Enti Urbani (rinvio al PDF e al manuale Pregeo).

Il **firmatario** resta responsabile della correttezza della sequenza adottata e della tempistica fra Pregeo, Docfa e atti collaterali.
