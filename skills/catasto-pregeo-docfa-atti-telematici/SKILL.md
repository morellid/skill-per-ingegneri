---
name: catasto-pregeo-docfa-atti-telematici
description: Assiste geometri, ingegneri, architetti, dottori agronomi e periti edili nella redazione e nella verifica pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni (procedura Pregeo 10) e del Catasto Fabbricati (procedura Docfa 4). Guida la scelta della tipologia di atto in riga 9 del libretto Pregeo (Tipo Mappale, Tipo Frazionamento, Atto Misto FM, Tipo Mappale con Stralcio di Corte SC, Tipo Particellare), la coerenza del modello censuario, la nuova disciplina del deposito telematico dei frazionamenti dal 1/7/2025 (art. 30 co. 5-bis DPR 380/2001 - Risoluzione AdE 40/E del 9/6/2025), la corretta scelta della causale Docfa (Quadro A o B), della categoria catastale (Gruppi A, B, C, D, E, F) e delle relative dichiarazioni nel Quadro D, la completezza di Elaborato Planimetrico, Elenco Subalterni, Entita' Tipologiche e planimetrie, fino al check pre-invio Sister per ridurre i rifiuti telematici. Use when an Italian land surveyor, civil engineer or architect must prepare or review a Pregeo or Docfa filing before sending it to Agenzia delle Entrate via Sister.
license: MIT
area: edilizia-urbanistica-catasto
title: "Catasto - Atti telematici Pregeo 10 + Docfa 4"
summary: "Assistente alla redazione e check pre-trasmissione degli atti telematici Catasto Terreni (Pregeo 10) e Fabbricati (Docfa 4): scelta tipologia atto, causale, categoria, quadri EP/ES/ET/D, deposito telematico frazionamenti, diagnosi rifiuti via Sister."
normative_refs:
  - "DPR 380/2001 art. 30"
  - "DM 28/1998"
  - "Circ. AdE 3/2009"
  - "Vademecum Docfa v1.0 (7/2022)"
  - "Risoluzione AdE 40/E del 9/6/2025"
version: 0.1.1-alpha
status: alpha
tags:
  - catasto
  - pregeo
  - docfa
---

# Catasto - Atti telematici Pregeo 10 + Docfa 4

## Quando usare questa skill

Usare quando un soggetto abilitato alla redazione di atti di aggiornamento catastale (geometra, ingegnere, architetto, dottore agronomo, perito agrario, perito edile, dipendente di Pubblica Amministrazione titolare ex Provv. AdE 28/1/2021) chiede di:

- **Scegliere la tipologia corretta dell'atto Pregeo** (Tipo Mappale, Tipo Frazionamento, Atto Misto Tipo Frazionamento+Tipo Mappale "FM", Tipo Mappale con Stralcio di Corte "SC", Tipo Particellare, atti speciali su acque/strade/demaniali) e codificarla in riga 9 del libretto delle misure, in coerenza con la scheda esemplificativa della Circolare AdE 3/2009 e successive integrazioni (Circolare 44/E 2016).
- **Verificare la disciplina del deposito comunale** ai sensi dell'art. 30 co. 5 e 5-bis DPR 380/2001: dal 1/7/2025 i Tipi di Frazionamento (FR), gli Atti Misti (FM) e i Tipi Mappali con Stralcio di Corte (SC) presentati telematicamente sono depositati dall'Agenzia delle Entrate sul Portale dei Comuni; per le altre tipologie permane il deposito a cura del professionista (Risoluzione AdE 40/E del 9/6/2025).
- **Strutturare la dichiarazione sostitutiva di atto di notorieta'** ex artt. 38 e 47 DPR 445/2000 nella riga 9 del libretto Pregeo (per FR/FM/SC dal 1/7/2025) o nella sezione corrispondente per le altre tipologie.
- **Eseguire il check pre-trasmissione Pregeo**: versione obbligatoria del software (10.6.5 - APAG 2.15 dal 1/7/2025), estratto di mappa rilasciato dall'Ufficio (vincolante salvo casi di estratto autoallestito), valori di tolleranza (semiasse maggiore ellisse di errore < 10 cm, distanze fra Punti Fiduciali entro tolleranza ex Decreto direttoriale 4A/322 del 19/1/1988, deformazione massima entro l'indice di affidabilita' della mappa), coerenza del modello censuario (originali, soppresse, costituite, variate).
- **Scegliere la causale Docfa corretta**: per accatastamento (Quadro A: Nuova Costruzione, Unita' afferenti in sopraelevazione / area di corte / altro), per variazione (Quadro B: Variazione planimetrica - divisione, frazionamento per trasferimento di diritti, fusione, ampliamento, demolizione totale/parziale, diversa distribuzione spazi interni, ristrutturazione, frazionamento+fusione; Variazione toponomastica; Ultimazione fabbricato urbano; Variazione di destinazione; Modifica identificativo; Presentazione planimetria mancante; Richiesta ruralita'; Unita' afferenti).
- **Scegliere la categoria catastale corretta**: ordinaria (Gruppi A, B, C - tariffa d'estimo x consistenza), speciale e particolare (Gruppi D, E - stima diretta con destinazione d'uso codificata ai sensi del Vademecum Docfa cap. 1.2.3 e Circ. AdE 2/E 1/2/2016, esclusione "imbullonati" L. 208/2015 art. 1 co. 21), fittizia (Gruppo F - art. 3 DM 28/1998).
- **Strutturare il Quadro D Docfa** (Note relative al documento e relazione tecnica) con le dichiarazioni obbligatorie del Vademecum cap. 2.4.2 in funzione della causale e della categoria F/x.
- **Verificare la completezza dell'Elaborato Planimetrico** (EP), dell'**Elenco Subalterni** (ES) e delle **Entita' Tipologiche** (CF, AL, AC, CI, CS) e delle **planimetrie** delle singole UIU prima della trasmissione Docfa.
- **Diagnosticare un rifiuto telematico** Pregeo o Docfa, mappando il messaggio dell'Ufficio Provinciale Territorio sulle cause ricorrenti (cfr. Allegato 5 Circ. 3/2009 e cap. 2.4.2 / 3.1 Vademecum Docfa) e proponendo la correzione.

**Non usare** se l'utente chiede:

- **Calcoli topografici** di rilievo (compensazione poligonali, calcolo coordinate Punti Fiduciali, riduzione misure GNSS): la skill rinvia alle "Istruzioni per il rilievo catastale di aggiornamento" - decreto direttoriale 4A/322 del 19/1/1988 e al manuale operativo Pregeo. Le formule e i coefficienti vanno applicati dal software certificato AdE.
- **Calcolo della rendita catastale**: la skill ricorda che la rendita ordinaria si determina come tariffa d'estimo x consistenza (vani per A, mc per B, mq per C) e per le UIU di Gruppo D/E in stima diretta secondo Circ. AdE 6/T 2012; il calcolo numerico finale e la tariffa applicabile sono adempimento del professionista (la tariffa varia per zona censuaria).
- **Determinazione della superficie catastale**: la skill rinvia all'Allegato C del DPR 138/1998 e ricorda che il valore entra nel Quadro U Docfa, ma il calcolo va eseguito dal professionista (la skill non riproduce i coefficienti per il ragguaglio delle accessorie/scoperte).
- **Operazioni sul portale Sister** (login, gestione dei lotti, upload del file Pregeo/Docfa, riscossione tributi/bollo): la skill non sostituisce il manuale operativo Sister.
- **Adempimenti civilistici e fiscali collaterali** (atto notarile di trasferimento, dichiarazione di successione, voltura catastale, Imposta di Registro/IVA, IMU/TARI conseguenti alla variazione): la skill cita il vincolo (es. il Tipo di Frazionamento deve precedere l'atto di trasferimento ai sensi dell'art. 30 co. 2 DPR 380/2001) ma non esegue i calcoli fiscali.
- **Pareri sulla legittimita' urbanistica** (titolo edilizio, conformita' al PUC/PRG): la skill assume che l'intervento sia stato gia' ricondotto al titolo edilizio corretto (per quel filone, vedi la skill `modulistica-edilizia-unificata`).
- **Verifiche su acque, strade, particelle demaniali**: queste tipologie sono escluse dalla trattazione automatica Pregeo (Circ. 3/2009 par. 5) e seguono iter dedicati a cura dell'Ufficio.
- **Frazionamento di Enti Urbani in zone tavolari** (territori del Libro Fondiario - RD 499/1929): la skill ricorda l'eccezione tavolare della Risoluzione AdE 40/E 2025 (utilizzo di patch specifica con giustificazione in Relazione Tecnica Libera) ma non riproduce la disciplina tavolare di dettaglio.

## Avvertenza

Questa skill e' uno strumento di supporto alla **redazione e verifica pre-trasmissione** degli atti di aggiornamento catastale Pregeo 10 e Docfa 4. **Non sostituisce il giudizio del professionista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente.

> **ATTENZIONE - vigenza normativa e versione software**: la versione 0.1.0-alpha della skill e' costruita sui testi di:
> - DPR 380/2001 art. 30 (testo coordinato con D.Lgs. 1/2024 art. 25);
> - DM 2/1/1998, n. 28 (definizione UIU);
> - Circolare AdE Territorio 3 del 16/10/2009 (Pregeo 10) + Circ. 44/E 2016 (Pregeo 10.6.0 APAG 2.08) + Circ. 11/E 2023 (frazionamento enti urbani);
> - Risoluzione AdE 40/E del 9/6/2025 (deposito telematico frazionamenti dal 1/7/2025);
> - Vademecum Do.C.Fa. v1.0 - luglio 2022;
> - Istruzioni operative Docfa 4.00.5 (luglio 2019, versione vigente al last_verified).
>
> La materia e' altamente dinamica: AdE pubblica frequentemente nuove versioni di Pregeo (10.6.5 - APAG 2.15 obbligatoria dal 1/7/2025) e Docfa, nuove versioni del Vademecum, FAQ aggiornate. **Prima di applicare la skill su un caso reale verificare la versione del software in uso** sulla scheda AdE "Software Pregeo" e "Istruzioni operative Docfa professionisti" (link in `references/sources.yaml`). In caso di disallineamento prevale il testo vigente alla data della trasmissione.

Le dichiarazioni rese dal professionista nella riga 9 del libretto Pregeo e nel Quadro D Docfa sono **dichiarazioni sostitutive di atto di notorieta'** ai sensi degli artt. 38 e 47 DPR 445/2000. Mendacio o false attestazioni sono sanzionati ai sensi dell'art. 76 DPR 445/2000 (artt. 359 e 481 c.p. in quanto persona esercente servizio di pubblica necessita'), oltre a esporre a responsabilita' civile verso il committente e a sanzioni disciplinari da parte dell'Ordine/Collegio. La skill non produce documenti pronti alla firma digitale o all'upload Sister: ogni output deve essere riveduto, integrato e firmato dal professionista incaricato.

## Sotto-attivita' disponibili

Questa skill supporta cinque sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Scelta della tipologia di atto Pregeo e check pre-trasmissione Catasto Terreni**: l'utente chiede "che tipo di atto Pregeo devo redigere?", "qual e' la riga 9 corretta?", "il mio atto e' un FR, FM o SC?", "ho i requisiti per il deposito telematico ex art. 30 co. 5-bis?", "quali tolleranze devo rispettare prima di trasmettere?" -> leggi [`tasks/scelta-tipo-pregeo-e-check.md`](tasks/scelta-tipo-pregeo-e-check.md)
- **Scelta della causale Docfa e categoria catastale**: l'utente chiede "che causale Docfa devo scegliere fra divisione/fusione/ristrutturazione/...?", "in che categoria catastale rientra l'UIU?", "e' un'unita' di Gruppo F? quale F/x?", "devo dichiarare un'unita' afferente in sopraelevazione o su area di corte?" -> leggi [`tasks/scelta-causale-categoria-docfa.md`](tasks/scelta-causale-categoria-docfa.md)
- **Check pre-trasmissione Docfa - Quadro D, EP, ES, planimetrie**: l'utente chiede "il mio Docfa e' completo?", "cosa devo scrivere nel Quadro D?", "l'Elaborato Planimetrico e' obbligatorio nel mio caso?", "le entita' tipologiche sono da rappresentare?" -> leggi [`tasks/check-pre-trasmissione-docfa.md`](tasks/check-pre-trasmissione-docfa.md)
- **Diagnosi di un rifiuto/sospensione telematica Pregeo o Docfa**: l'utente chiede "ho ricevuto un rifiuto dall'Ufficio: cosa controllare?", "il messaggio di sospensione dice X, come correggere?", "l'atto e' inidoneo alla registrazione: che opzioni ho?" -> leggi [`tasks/diagnosi-rifiuti-telematici.md`](tasks/diagnosi-rifiuti-telematici.md)
- **Workflow misto Pregeo -> Docfa (Tipo Mappale + accatastamento Docfa)**: l'utente chiede "ho appena fatto un Tipo Mappale: come passo all'accatastamento Docfa?", "la particella e' in F/6, devo dichiarare le UIU?", "che ordine devo seguire fra Tipo Mappale, Atto Notarile, Docfa, voltura?" -> leggi [`tasks/workflow-pregeo-docfa.md`](tasks/workflow-pregeo-docfa.md)

Se la richiesta non e' chiara, chiedi all'utente: (a) si tratta di Catasto Terreni (Pregeo) o Catasto Fabbricati (Docfa)?; (b) che tipologia di intervento e' (nuova costruzione, ampliamento, frazionamento, demolizione, ristrutturazione, regolarizzazione)?; (c) la trasmissione e' gia' avvenuta (rifiuto da diagnosticare) o e' in fase di redazione (check pre-invio)?

## Processo generale

1. **Inquadra il professionista**: chi e' (geometra, ingegnere, architetto, dottore agronomo, perito agrario, perito edile, dipendente PA)? L'iscrizione all'Ordine/Collegio e l'abilitazione all'invio telematico via Sister sono in corso di validita' (Provv. AdE 11/3/2015)? La trasmissione e' obbligatoria (professionisti ordinistici) o facoltativa (PA su beni propri, Provv. 28/1/2021)?
2. **Inquadra l'atto**: si tratta di Catasto Terreni (Pregeo 10) o Catasto Fabbricati (Docfa 4)? Tipologia (TM, TF/FR, FM, SC, TP per Pregeo; accatastamento o variazione per Docfa)? Si tratta di un atto autonomo o di un workflow misto Pregeo+Docfa?
3. **Verifica la versione software** in uso: Pregeo 10.6.5 - APAG 2.15 obbligatoria dal 1/7/2025 per tutti gli atti (link `sources.yaml: ade-istruzioni-pregeo-software`); Docfa 4.00.5 (versione vigente al last_verified, link `sources.yaml: ade-istruzioni-operative-docfa-2019`). Avvisa l'utente che, in caso di nuove versioni, la skill puo' essere disallineata.
4. **Identifica la sotto-attivita'** richiesta tramite il routing della sezione "Sotto-attivita' disponibili".
5. **Carica il task file** corrispondente.
6. **Applica la procedura** descritta nel task, citando precisamente articolo, comma, paragrafo della fonte normativa per ogni affermazione (es. "Vademecum Docfa cap. 1.2.4 - F/2", "Circ. 3/2009 par. 6 - criteri di approvazione", "Risoluzione AdE 40/E del 9/6/2025 - ambito FR/FM/SC", "art. 30 co. 5-bis DPR 380/2001").
7. **Produci l'output** nel formato indicato dal task (checklist conforme/non conforme, bozza di dichiarazione, mapping rifiuto -> causa -> correzione, ecc.).
8. **Concludi** sempre con:
   - elenco di **elementi non automaticamente verificabili** dalla skill (sopralluogo fisico per perimetrazione UIU, taratura strumentazione topografica, conformita' urbanistica dell'intervento, indipendenza catastale dei BCNC);
   - rinvio alla **revisione del professionista incaricato** ai sensi dell'art. 1 co. 374 L. 311/2004 e Provv. AdE 11/3/2015 (responsabilita' professionale esclusiva del firmatario);
   - segnalazione del **rischio penale** (artt. 359, 481 c.p. + art. 76 DPR 445/2000) per false attestazioni nelle DSAN;
   - rinvio al manuale operativo del software in uso (Pregeo, Docfa) e alla scheda AdE per la versione vigente al momento della trasmissione.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:

- **DPR 6/6/2001 n. 380** art. 30 commi 5 e 5-bis (Testo Unico Edilizia)
- **D.Lgs. 8/1/2024 n. 1** art. 25 (introduce art. 30 co. 5-bis DPR 380/2001)
- **DM 2/1/1998 n. 28** art. 2 (definizione UIU) e art. 3 (categorie F)
- **DPR 28/12/2000 n. 445** artt. 38, 47, 76 (DSAN e sanzioni penali)
- **Circolare AdE Territorio n. 3 del 16/10/2009** prot. 54825 - Pregeo 10 (allegato 2 con tipologie codificate, allegato 5 con categorie di controlli automatici)
- **Circolare AdE n. 44/E del 14/12/2016** - Pregeo 10.6.0 APAG 2.08
- **Circolare AdE n. 11/E dell'8/5/2023** - Frazionamento enti urbani
- **Risoluzione AdE n. 40/E del 9/6/2025** - Deposito telematico atti di frazionamento
- **Provvedimento Direttore AdE 30/12/2024** prot. 460141 - Decorrenza 1/7/2025 deposito telematico
- **Provvedimento Direttore AdE 11/3/2015** prot. 35112 - Obbligo trasmissione telematica per professionisti
- **Provvedimento Direttore AdE 28/1/2021** prot. 27427 - Estensione PA
- **Vademecum Do.C.Fa. v1.0 - luglio 2022** - Direzione Centrale Servizi Catastali AdE
- **Istruzioni operative Docfa per professionisti** - versione 4.00.5 (luglio 2019)
- **Circolare AdE n. 2/E del 1/2/2016** - Categorie speciali D ed E (Docfa 4.00.3)
- **Circolare AdE Territorio n. 6/T del 30/11/2012** - Stima diretta UIU D/E (rango normativo per art. 1 co. 244 L. 190/2014)
- **L. 28/12/2015 n. 208** art. 1 commi 21-24 - Esclusione "imbullonati"
- **DPR 23/3/1998 n. 138** Allegato C - Determinazione superficie catastale UIU ordinarie

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dpr-380-2001-art-30.md`](references/estratti/dpr-380-2001-art-30.md) - regime di deposito ante/post 1/7/2025
- [`dm-28-1998-uiu.md`](references/estratti/dm-28-1998-uiu.md) - definizione UIU e categorie F
- [`circolare-3-2009-pregeo10.md`](references/estratti/circolare-3-2009-pregeo10.md) - tipologie atti Pregeo, controlli automatici, cause di rifiuto
- [`risoluzione-40-2025-deposito-telematico.md`](references/estratti/risoluzione-40-2025-deposito-telematico.md) - ambito FR/FM/SC, dichiarazioni riga 9, workflow Portale Comuni
- [`vademecum-docfa-categorie-causali.md`](references/estratti/vademecum-docfa-categorie-causali.md) - categorie A/B/C/D/E/F, causali Quadro A/B
- [`vademecum-docfa-elaborato-planimetrico.md`](references/estratti/vademecum-docfa-elaborato-planimetrico.md) - EP, ES, ET, planimetrie, Quadro D

## Limiti

Cosa questa skill NON fa:

- Non e' un **manuale operativo Pregeo o Docfa**: la skill rinvia ai manuali AdE per le procedure di compilazione campo-per-campo del software (le interfacce cambiano con le release).
- Non riproduce le **schede esemplificative dell'Allegato 2 alla Circ. 3/2009** in versione completa (sono 86 pagine di tipologie codificate). Per la scheda specifica della tipologia in uso, la skill rinvia al PDF originale archiviato in `not_in_repo/`.
- Non riproduce i **prospetti delle tariffe d'estimo** (variano per zona censuaria comunale) ne' i **coefficienti di ragguaglio** dell'Allegato C DPR 138/1998 per il calcolo della superficie catastale.
- Non sostituisce il **rilievo topografico**: la skill assume che il libretto delle misure (file .dat Pregeo) sia gia' redatto in conformita' alle "Istruzioni per il rilievo catastale di aggiornamento" - decreto direttoriale 4A/322 del 19/1/1988.
- Non valida l'**attendibilita' dei Punti Fiduciali**: la skill ricorda che l'archivio mutue distanze va scaricato aggiornato, ma il controllo di tolleranza e' eseguito dal software Pregeo.
- Non esegue il **classamento delle UIU**: l'attribuzione di categoria e classe e' compito del professionista che redige il Docfa, sulla base delle caratteristiche oggettive (Vademecum cap. 1.3.1) e della comparazione con UIU di riferimento (art. 11 co. 1 DL 70/1988 conv. L. 154/1988).
- Non determina la **destinazione d'uso codificata** delle UIU di Gruppo D ed E: la skill cita i Prospetti 1.6 - 1.24 del Vademecum ma il codice numerico della destinazione d'uso va selezionato dal professionista in funzione delle caratteristiche dell'immobile.
- Non sostituisce il **sopralluogo fisico** per la perimetrazione delle UIU, l'individuazione dei BCC/BCNC e l'accertamento dello stato di degrado/incompletezza (F/2, F/3, F/4).
- Non sostituisce il **manuale operativo Sister** ne' la **guida del Portale dei Comuni** per la trasmissione telematica e la verifica del deposito ex art. 30 co. 5-bis.
- Non valuta il **cumulo con adempimenti collaterali** (atto notarile, voltura, dichiarazione di successione, autorizzazione paesaggistica, condono): la skill cita i vincoli di sequenza (es. Tipo di Frazionamento prima dell'atto traslativo, art. 30 co. 2 DPR 380/2001) ma non gestisce gli adempimenti.
- Non interpreta la **disciplina tavolare** (RD 499/1929 - Trentino, Alto Adige, Trieste, Gorizia, parte della Venezia Giulia): la skill ricorda l'eccezione della Risoluzione 40/E 2025 (patch Pregeo 10.6.5) ma non sostituisce le procedure tavolari di Libro Fondiario.
- Non riproduce il contenuto dei **Quaderni Docfa** delle Direzioni Provinciali (raccolta di prassi operativa locale, link in `sources.yaml`).
- Non sostituisce la **polizza professionale** del firmatario ne' il giudizio dell'Ordine/Collegio sulla legittimita' del singolo atto.

**Ogni output prodotto dalla skill e' supporto al professionista, non sostituzione.** La responsabilita' penale (artt. 359 e 481 c.p. + art. 76 DPR 445/2000), civile e disciplinare resta in capo al firmatario dell'atto Pregeo/Docfa.
