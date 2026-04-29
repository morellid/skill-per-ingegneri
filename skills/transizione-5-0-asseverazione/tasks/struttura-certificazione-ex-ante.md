# Task: Struttura della Certificazione Ex Ante (Allegato VIII + IX)

Produce la **bozza testuale** della Certificazione Ex Ante (Allegato VIII della circolare MIMIT 25877/2024) e della relativa **Relazione Tecnica** (Allegato IX), conforme al modello vincolante per la comunicazione preventiva sul portale TR5 GSE.

## Obiettivo

Restituire all'utente:

- La **bozza della Certificazione Ex Ante** (Allegato VIII), con tutti i campi obbligatori compilati sulla base degli input forniti, in forma di testo strutturato pronto a essere riveduto e firmato digitalmente dal certificatore.
- La **bozza della Relazione Tecnica Ex Ante** (Allegato IX), con il dettaglio metodologico del calcolo, da conservare in azienda.
- L'elenco dei **documenti probatori** che la Relazione richiama (foglio di calcolo, schede tecniche, schemi d'impianto, fonti BREF/BAT).
- La **dichiarazione di terzieta'** del valutatore (Allegato III) come bozza separata.
- Una **checklist finale** dei controlli da fare prima della firma digitale.

## Prerequisiti

Prima di eseguire questo task, l'utente deve aver completato:

- **`verifica-ammissibilita.md`**: progetto ammissibile, certificatore qualificato e terzo, DNSH compatibile;
- **`calcola-riduzione-consumi.md`**: calcolo del risparmio in tep, riduzione percentuale, fascia di credito d'imposta.

Se uno di questi e' mancante, **rinvia esplicitamente** al task corrispondente prima di procedere.

## Input richiesti

Riepilogare con l'utente i dati gia' raccolti in `verifica-ammissibilita.md` e `calcola-riduzione-consumi.md`. In particolare:

1. **Dati identificativi del certificatore**:
   - tipo (EGE / ESCo / ingegnere sez. A o B / perito industriale "meccanica ed efficienza energetica" o "impiantistica elettrica ed automazione");
   - nome, cognome, CF (oppure ragione sociale, sede legale, P.IVA, legale rappresentante per ESCo);
   - n. certificazione UNI CEI 11339 (EGE) / 11352 (ESCo) o n. iscrizione albo professionale + provincia + data iscrizione;
   - organismo di certificazione e data di rilascio/validita' (per EGE/ESCo);
   - PEC, recapito, polizza assicurativa professionale (riferimento e massimale - art. 15 co. 8 DM).

2. **Dati identificativi dell'impresa beneficiaria**:
   - ragione sociale, P.IVA, CF;
   - flag "impresa di nuova costituzione" (si'/no).

3. **Localizzazione della struttura produttiva**:
   - regione, provincia, comune, via;
   - dati catastali: codice catastale comune, sezione, foglio, particella, sub;
   - codice ATECO.

4. **Investimenti (con classificazione allegati A/B L. 232/2016)**:
   - elenco voci dell'Allegato A (gruppi 1.1-1.13, 2.1-2.9, 3.1-3.4) e Allegato B (1-23) coinvolte;
   - descrizione discorsiva dei beni materiali e immateriali con riconducibilita' alle voci dell'allegato (es. "macchine per il confezionamento e l'imballaggio");
   - eventuali investimenti FER per autoconsumo (Allegato A.7 DM);
   - eventuali attivita' di formazione (art. 8 DM).

5. **Risparmio dichiarato**:
   - risparmio in tep/anno;
   - riduzione percentuale (sulla struttura produttiva o sul processo interessato);
   - perimetro selezionato (struttura / processo);
   - fascia di credito (3-6%/5-10%, 6-10%/10-15%, >10%/>15%).

6. **Algoritmo di calcolo**:
   - formula esplicita;
   - variabili operative ex post 1, ex post 2, ...;
   - fonte degli indicatori di prestazione (BREF, BAT, letteratura, offerte mercato).

7. **Scenario controfattuale** (se applicabile - nuova costituzione o sostanziale modifica del servizio):
   - per ogni bene agevolato: 3 alternative di mercato (marca, modello, prestazione, prezzo, fonte).

8. **Impianti FER per autoconsumo** (se applicabile):
   - consumo annuo energia elettrica prelevata da rete [kWh];
   - fabbisogno di energia elettrica equivalente ai consumi annui di energia termica [kWh];
   - combustibili utilizzati per energia termica (dal set di voci ammesse nel modello);
   - producibilita' attesa <= 105% * (Energia elettrica prelevata + min(Energia elettrica prelevata; Energia elettrica equivalente)) [kWh];
   - per ogni impianto: tipologia FER, categoria intervento, potenza [kW] (elettrico/termico).

## Fonti normative

Leggere prima di procedere:

- `references/estratti/circolare-mimit-modelli-certificazioni.md` - Allegati VIII (Certificazione Ex Ante) e IX (Relazione Tecnica)
- `references/estratti/dm-24-07-2024-articoli-chiave.md` - art. 15 (certificazioni)
- `references/estratti/faq-mimit-soggetti-certificatori.md` - FAQ 2.6 (documentazione comunicazione preventiva)

## Procedura

### Passo 1 - Conferma del prerequisito

Verifica con l'utente:

> "Confermi di aver completato i task `verifica-ammissibilita.md` (progetto ammissibile) e `calcola-riduzione-consumi.md` (riduzione = X%, perimetro = ..., fascia = ...)? Procedo con la bozza dell'Allegato VIII?"

Se manca uno dei due, rinvia.

### Passo 2 - Bozza Certificazione Ex Ante (Allegato VIII)

Compila il modello vincolante della circolare MIMIT 25877/2024 - Allegato VIII. Schema:

```markdown
# CERTIFICAZIONE EX ANTE
## Resa ai sensi del DPR 445/2000 artt. 46 e seguenti e degli artt. 359 e 481 del codice penale

---

[Una sola fra le tre intestazioni, in funzione del tipo di certificatore]

## [SE ESCo]
**[Ragione sociale ESCo]**, con sede legale in [...], nel Comune di [...], CF [...] e P.IVA [...], rappresentata da [legale rappresentante], nato a [...] il [...], in qualita' di legale rappresentante, n. [...], CAP [...], tel. [...], PEC [...].
In possesso della certificazione n. [...] rilasciata secondo la norma **UNI CEI 11352** dall'Organismo di Certificazione [...] il [...] e valida fino al [...] e recepita dalla banca dati Accredia, per incarico ricevuto da [ragione sociale completa dell'impresa beneficiaria] [...].
Consapevole delle responsabilita' e delle pene stabilite dalla legge per false attestazioni e mendaci dichiarazioni (art. 76 DPR 445/2000), sotto la sua personale responsabilita'.

## [SE EGE]
Il/la sottoscritto/a [nome cognome], nato/a a [...] il [...], CF/P.IVA [...], residente / con studio / domiciliato in [...] via [...], n. [...], CAP [...], tel. [...], PEC [...].
In possesso della certificazione n. [...] rilasciata secondo la norma **UNI CEI 11339** dall'Organismo di Certificazione [...] il [...] e valida fino al [...] e recepita dalla banca dati Accredia, per incarico ricevuto da [ragione sociale completa dell'impresa beneficiaria] [...].
Consapevole delle responsabilita' e delle pene stabilite dalla legge per false attestazioni e mendaci dichiarazioni (art. 76 DPR 445/2000), sotto la sua personale responsabilita'.

## [SE INGEGNERE / PERITO]
Il/la sottoscritto/a [nome cognome], nato/a a [...] il [...], CF/P.IVA [...], residente / con studio / domiciliato in [...] via [...], n. [...], CAP [...], tel. [...], PEC [...].
Iscritto presso l'Ordine professionale dei [Ingegneri / Periti Industriali] (matricola [...]):
- [ ] ingegnere iscritto nella sezione A dell'albo professionale
- [ ] ingegnere iscritto nella sezione B dell'albo professionale
- [ ] perito industriale o perito industriale laureato iscritto all'albo nella sezione "meccanica ed efficienza energetica"
- [ ] perito industriale o perito industriale laureato iscritto all'albo nella sezione "impiantistica elettrica ed automazione"

della provincia di [...] in data [...] e tuttora in corso di validita'.

Consapevole delle responsabilita' e delle pene stabilite dalla legge per false attestazioni e mendaci dichiarazioni (art. 76 DPR 445/2000), sotto la sua personale responsabilita'.

---

## PREMESSO

- che l'impresa **[ragione sociale]** dichiara:
  - di aver effettuato o aver previsto di effettuare investimenti agevolabili ai sensi dell'art. 38 co. 2 del DL 2 marzo 2024 n. 19 e del DM Transizione 5.0 24 luglio 2024, cosi' come indicato nella documentazione e nei contratti di acquisto di cui ho preso visione;
  - che i costi di tali investimenti sono imputabili ai sensi dell'art. 109 commi 1 e 2 del TUIR al periodo d'imposta agevolabile, saranno determinati secondo corretti criteri fiscali e contabili e saranno correttamente iscritti in bilancio e nel libro cespiti.

## VISTI

- l'art. 38 del DL 2 marzo 2024 n. 19, che istituisce il Piano Transizione 5.0 a sostegno del processo di transizione digitale ed energetica delle imprese, in attuazione di quanto previsto dalla decisione del Consiglio ECOFIN dell'8 dicembre 2023 e, in particolare, di quanto disposto in relazione all'Investimento 15 - Transizione 5.0, della Missione 7 - REPowerEU;
- le disposizioni di cui al DM Transizione 5.0 del 24 luglio 2024.

## ATTESTA

- che quanto dichiarato nella presente certificazione si basa su elementi, dati e informazioni **personalmente acquisiti e verificati** con diligenza tecnico-specialistica, anche mediante l'effettuazione di **sopralluoghi** presso la struttura produttiva;
- che il progetto di innovazione proposto si caratterizza per l'acquisizione di tecnologie ai sensi dell'art. 38 del DL 19/2024 e del DM Transizione 5.0;
- che a seguito della realizzazione del progetto di innovazione, all'interno della struttura produttiva ovvero del processo interessato oggetto del progetto, e' ottenuto un livello di **risparmio energetico pari a [X tep/anno, equivalente al Y%]**;
- di **essersi dotato di idonea copertura assicurativa**, cosi' come previsto dall'art. 15 co. 8 del DM Transizione 5.0.

## ASSEVERA I CONTENUTI DI SEGUITO RIPORTATI

### Informazioni principali sul progetto di innovazione

**Soggetto che effettua l'investimento**
- Ragione sociale: [...]
- P.IVA: [...]
- CF: [...]
- [ ] Spuntare se trattasi di impresa di nuova costituzione

**Indirizzo della struttura produttiva oggetto di intervento**
- Regione: [...]
- Provincia: [...]
- Comune: [...]
- Via: [...]

**Riferimenti catastali prevalenti della struttura produttiva**
- Codice catastale del comune: [...]
- Sezione: [...]
- Foglio: [...]
- Particella: [...]
- Sub: [...]

**Codice ATECO** delle attivita' nella struttura produttiva: [...]

### Indicazione del progetto di innovazione (selezionare la tipologia di investimento)

- [ ] **Investimenti in beni materiali e immateriali nuovi** (Allegati A/B L. 232/2016) con riduzione dei consumi energetici della **struttura produttiva** localizzata in Italia:
  - [ ] non inferiore al 3%
  - [ ] superiore al 6%
  - [ ] superiore al 10%

- [ ] **Investimenti in beni materiali e immateriali nuovi** (Allegati A/B L. 232/2016) con riduzione dei consumi energetici dei **processi interessati** dall'investimento:
  - [ ] non inferiore al 5%
  - [ ] superiore al 10%
  - [ ] superiore al 15%

**Processo/i produttivo/i** all'interno del quale e' stato individuato il processo interessato: [...] (con richiamo a quelli individuati nella relazione tecnica di certificazione).

- [ ] Investimenti in beni materiali nuovi finalizzati all'**autoproduzione di energia da fonti rinnovabili** destinata all'autoconsumo (escluse biomasse), compresi gli impianti per lo stoccaggio dell'energia prodotta.

- [ ] **Formazione del personale** prevista dall'art. 31 par. 3 del Reg. UE 651/2014, finalizzata all'acquisizione/consolidamento delle competenze nelle tecnologie rilevanti per la transizione digitale ed energetica dei processi produttivi.

### Beni impiegati

**Allegato A L. 232/2016 - Primo gruppo** (selezionare le voci pertinenti):
- [ ] 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13

**Allegato A - Secondo gruppo**:
- [ ] 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9

**Allegato A - Terzo gruppo**:
- [ ] 3.1, 3.2, 3.3, 3.4

**Allegato B L. 232/2016**:
- [ ] 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23

**Descrizione**:
- [es. macchina utensile X riconducibile alle "macchine utensili per la deformazione plastica dei metalli e altri materiali" di cui all'Allegato A]
- [es. software MES Y riconducibile ai "software, sistemi, piattaforme e applicazioni per il monitoraggio e controllo delle condizioni di lavoro delle macchine e dei sistemi di produzione interfacciati con i sistemi informativi di fabbrica e/o con soluzioni cloud" di cui all'Allegato B]

### Risparmio conseguibile dal progetto di innovazione

- **Risparmio in tep [tep/anno]**: [X]
- **Risparmio annuo percentuale [%]**: [Y]

### Algoritmo di calcolo dei risparmi

`Risp = (Indicatore di prestazione_ex ante - Indicatore di prestazione_ex post) * Variabile operativa_post`

Dove:
- Variabile operativa_post 1: [...]
- Variabile operativa_post 2: [...]
- ...

(Per il dettaglio, vedi Relazione Tecnica - Allegato IX)

### Configurazione di riferimento utilizzata per il calcolo del risparmio energetico

[Specificare se: ex ante misurato, ex ante stimato, scenario controfattuale]

### Descrizione dello scenario controfattuale [se applicabile]

- **Bene 1**: [marca/modello investito]
  - alternativa 1: [marca, modello, prestazione, prezzo, fonte]
  - alternativa 2: [...]
  - alternativa 3: [...]
- **Bene 2**: [...]
- ...

### Impianto/i di autoproduzione previsto/i per l'autoconsumo [se applicabile]

- Consumo annuo di energia elettrica della struttura produttiva prelevata dalla rete [kWh]: [...]
- Fabbisogno di energia elettrica equivalente ai consumi annui di energia termica [kWh]: [...]
- Combustibili utilizzati per la produzione di energia termica: [Gasolio | Olio combustibile | GPL liquido | GPL gassoso | Oli vegetali | Pellet | Cippato | Gas naturale | GNL | Biogas | Calore da fluido termovettore]
- Producibilita' attesa <= 105% * [Energia elettrica prelevata + min(Energia elettrica prelevata; Energia elettrica equivalente)] [kWh]: [...]

**Energia elettrica** (ripetere per ogni impianto):
- Tipologia FER: [solare FV | eolico | idroelettrico | ...]
- Categoria intervento: [...]
- Potenza [kW]: [...]

**Energia termica** (ripetere per ogni impianto):
- Tipologia FER: [geotermico | pompe di calore | ...]
- Categoria intervento: [...]
- Potenza [kW]: [...]

### Documentazione conservata presso l'impresa beneficiaria

A titolo esemplificativo non esaustivo:
1. Relazione tecnica di certificazione ex ante (Allegato IX);
2. Documentazione attestante le specifiche tecniche dei componenti ante e post intervento (schede tecniche);
3. Schemi d'impianto rappresentativi dell'interconnessione tra struttura produttiva / processo interessato e sistemi di produzione/prelievo dei vettori energetici, con evidenza del posizionamento dei misuratori;
4. Documentazione attestante le specifiche tecniche della strumentazione di misura;
5. Foglio di calcolo contenente l'algoritmo per la determinazione dei risparmi e il dettaglio di tutti i dati utilizzati;
6. Documentazione utilizzata per la stima delle prestazioni energetiche ante e post intervento (BREF, BAT, letteratura, offerte mercato).

---

Luogo e data: [...]

Il Certificatore (timbro e firma digitale): [...]
```

### Passo 3 - Bozza Relazione Tecnica Ex Ante (Allegato IX)

Documento esteso da conservare in azienda. Sezioni:

```markdown
# RELAZIONE TECNICA DI CERTIFICAZIONE EX ANTE
## Beni funzionali alla trasformazione tecnologica e digitale delle imprese secondo il modello "Transizione 5.0"

---

## 1. Dati identificativi dell'impresa
- Denominazione: [...]
- CF: [...]
- P.IVA: [...]

## 2. Dati certificatore
[stesse sezioni dell'Allegato VIII - intestazione]

## 3. Descrizione del progetto di innovazione
- Inquadramento dell'attivita' produttiva: [...]
- Descrizione dei processi produttivi della struttura: [...]
- Tecnologie acquisite e finalita' tecnico-energetica: [...]
- Perimetro del programma di misura: [struttura produttiva / processo interessato]
- Motivazione della scelta del perimetro (con riferimento agli esempi 1-4 cap. 2.1 circolare MIMIT 25877/2024): [...]
- Schemi di processo/impianto allegati: [richiami a fig./elaborati]

## 4. Dati registrati ex ante (per vettore energetico)

| Vettore energetico | Periodo di riferimento (12 mesi) | Consumo (unita' naturale) | Fonte dato | Strumento di misura (conformita' MID) |
|---|---|---|---|---|
| [es. Energia elettrica] | [GG/MM/AAAA - GG/MM/AAAA] | [kWh] | [es. fatture energia + contatore dedicato] | [tarato il GG/MM/AAAA] |
| [...] | [...] | [...] | [...] | [...] |

## 5. Variabili operative ex ante

| Variabile operativa | Unita' di misura | Valore ex ante | Periodo | Fonte |
|---|---|---|---|---|
| [es. Tonnellate prodotte] | t | [...] | [...] | [es. MES + DDT] |

## 6. Indicatori di prestazione ex ante

| Indicatore | Unita' di misura | Valore ex ante | Fonte (BREF, BAT, letteratura, offerte mercato) |
|---|---|---|---|
| [es. tep/t prodotto] | tep/t | [...] | [...] |

## 7. Stima ex post

Metodologia di stima utilizzata: [analisi carichi tracciabili / schede tecniche fornitore / modellizzazione / prove in situ / BREF / BAT].

| Vettore energetico | Consumo ex post (stima, unita' naturale) | Metodo | Fonte |
|---|---|---|---|
| [...] | [...] | [...] | [...] |

| Indicatore | Valore ex post |
|---|---|
| [...] | [...] |

## 8. Algoritmo di calcolo dei risparmi

`Risp_tep = (Indicatore_ex_ante - Indicatore_ex_post) * Variabile_operativa_post`

[Dimostrazione passo passo dell'applicazione dell'algoritmo ai dati delle sezioni 4-7]

- Risparmio in tep/anno: [X]
- Riduzione percentuale: [Y%]

## 9. Conversione in tep

Riferimento: circolare MISE 18/12/2014 (rinvio art. 9 co. 6 DM Transizione 5.0).

| Vettore | Fattore tep applicato | Riferimento |
|---|---|---|
| [...] | [...] | [punto X circ. MISE 2014] |

## 10. Scenario controfattuale (se applicabile)

[Solo se impresa di nuova costituzione (<6 mesi) o intervento con sostanziale modifica del servizio reso che impedisce la normalizzazione - cap. 2.2 circolare MIMIT.]

| Bene agevolato | Alt. 1 (marca/modello/prezzo/fonte) | Alt. 2 | Alt. 3 | Consumo medio (tep/anno) |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] |

Consumo controfattuale totale: [Z tep/anno].

## 11. Verifica delle soglie minime

| Perimetro | Soglia minima (DL 19/2024 art. 38 co. 4) | Riduzione calcolata | Esito |
|---|---|---|---|
| Struttura produttiva | >=3% | [...%] | [Conforme / Non conforme] |
| Processo interessato | >=5% | [...%] | [Conforme / Non conforme] |

## 12. DNSH

Schede DNSH applicabili (Allegato VII circolare MIMIT 25877/2024) compilate o da compilare:
- [ ] Scheda A - Apparecchiature elettriche/elettroniche
- [ ] Scheda B - Servizi informatici hosting/cloud
- [ ] Scheda C - Pannelli solari
- [ ] Scheda D - Eolico
- [ ] Scheda E - Idroelettrico
- [ ] Scheda F1 - Geotermico
- [ ] Scheda F2 - Pompe di calore

Dichiarazione di compatibilita' con i criteri DNSH (richiamo alla DSAN sottoscritta dal beneficiario, art. 18 DM).

## 13. Strumenti di misura e conformita' MID

Conformita' alla **direttiva 2014/32/UE** (MID) degli strumenti utilizzati per la misurazione dei consumi (art. 9 co. 4 DM):
- [...]

## 14. Riferimenti normativi

- DL 2 marzo 2024 n. 19, art. 38, conv. con mod. dalla L. 56/2024
- DM MIMIT-MEF 24 luglio 2024 (Transizione 5.0)
- Circolare operativa MIMIT 16 agosto 2024 prot. 25877
- Circolare MISE 18 dicembre 2014 (coefficienti tep)
- Reg. UE 2020/852 art. 17 (DNSH)
- Direttiva 2014/32/UE (MID)
- DPR 445/2000 artt. 46-76 (DSAN, sanzioni)
- Codice penale artt. 359, 481

## 15. Documentazione probatoria archiviata

[Stesso elenco della sezione "Documentazione conservata" dell'Allegato VIII, integrato con eventuali ulteriori documenti specifici al caso]

---

Luogo e data: [...]

Il Certificatore (timbro e firma): [...]
```

### Passo 4 - Bozza Allegato III (Dichiarazione di terzieta' del valutatore)

Documento obbligatorio da allegare alla comunicazione preventiva (FAQ MIMIT 2.6).

```markdown
# DICHIARAZIONE DI TERZIETA' DEL VALUTATORE INDIPENDENTE
## Resa ai sensi degli artt. 46 e seguenti del DPR 445/2000

Il/la sottoscritto/a [...] (dati anagrafici e identificativi del certificatore come da Allegato VIII), in qualita' di [EGE / ESCo / ingegnere / perito]:

## DICHIARA

- di **non aver fornito consulenza** o intrattenuto rapporti professionali con l'impresa beneficiaria nei **3 anni** precedenti l'incarico, in materie collegate al progetto agevolato;
- di **non avere alcun interesse economico, finanziario o personale** che possa influenzare l'imparzialita' del giudizio (assenza di partecipazioni nel beneficiario, assenza di rapporti di lavoro subordinato in essere, assenza di altri legami di natura commerciale);
- di **non avere rapporti di parentela o affinita'** entro il quarto grado con il legale rappresentante, con i soci o con gli amministratori dell'impresa beneficiaria;
- di essere **consapevole delle responsabilita' civili e penali** derivanti dal rilascio di dichiarazioni non veritiere ai sensi dell'art. 76 del DPR 445/2000.

Luogo e data: [...]

Firma digitale: [...]
```

### Passo 5 - Output

Restituire all'utente il pacchetto:

1. Bozza Certificazione Ex Ante (Allegato VIII)
2. Bozza Relazione Tecnica Ex Ante (Allegato IX) - estesa, da conservare
3. Bozza Dichiarazione di Terzieta' (Allegato III)
4. Checklist finale dei controlli pre-firma:

```markdown
## Checklist pre-firma digitale Certificazione Ex Ante

- [ ] Sopralluogo presso la struttura produttiva effettuato e documentato (foto, verbale, data)
- [ ] Strumenti di misura conformi MID (tarature in corso di validita')
- [ ] Dati misurati ex ante coerenti con fatture/contatori (verifica incrociata)
- [ ] Stima ex post documentata con fonte verificabile (scheda tecnica fornitore, modellizzazione, prove in situ)
- [ ] Indicatori di prestazione documentati con fonte (BREF, BAT, letteratura, offerte mercato)
- [ ] Variabili operative coerenti con i dati produttivi (MES, ERP, DDT)
- [ ] Coefficienti tep applicati = circolare MISE 18/12/2014 vigente
- [ ] Scenario controfattuale documentato con 3 alternative reali (se applicabile)
- [ ] DSAN DNSH del beneficiario compilata e schede VII selezionate
- [ ] Polizza assicurativa professionale in corso di validita' (massimale adeguato)
- [ ] Dichiarazione di terzieta' (Allegato III) firmata
- [ ] Coerenza fra Allegato VIII (sintetico, da caricare) e Allegato IX (esteso, da archiviare): risparmi, perimetro, beni elencati, scenario, FER
- [ ] Foglio di calcolo dell'algoritmo allegato alla Relazione Tecnica (Excel/CSV)
- [ ] Schemi d'impianto e schede tecniche allegate alla Relazione Tecnica
- [ ] Verifica della rispondenza ai modelli MIMIT 25877/2024 (Allegati VIII, IX, III) - tutti i campi obbligatori compilati
- [ ] Conoscenza degli artt. 359, 481 c.p. e art. 76 DPR 445/2000 (responsabilita' penale aggravata)
- [ ] Versioni vigenti delle FAQ MIMIT consultate (non utilizzare FAQ obsolete)

## Avvertenza
**La presente bozza e' uno strumento di supporto. Il certificatore deve riveder ogni voce, integrare i dati mancanti, allegare la documentazione probatoria e firmare digitalmente sotto la propria personale responsabilita'.**
```

## Casi limite da gestire

### Soggetto certificatore = ingegnere senza certificazione EGE/ESCo
La sezione di intestazione non richiede certificazioni UNI: e' sufficiente l'iscrizione all'albo (sezione A o B) con dichiarazione di "competenze e comprovata esperienza nell'ambito dell'efficienza energetica dei processi produttivi" (art. 15 co. 6 lett. c DM). La skill rinvia il giudizio sull'adeguatezza dell'esperienza al certificatore stesso e al MIMIT in sede di vigilanza.

### Investimenti gia' completati al momento dell'ex ante (FAQ MIMIT 2.13)
Anche se l'intervento e' completato, la certificazione ex ante e' obbligatoria. La skill segnala il caso e adatta il testo dell'Allegato VIII (es. nella sezione "Indicazione del progetto di innovazione" si dichiara il completamento; nel passaggio successivo si potra' caricare direttamente la ex post).

### Risparmio dichiarato sopra il 10% sulla struttura (o 15% sul processo)
Selezionare la fascia "superiore al 10%" (struttura) o "superiore al 15%" (processo) nell'Allegato VIII. La fascia accede alle aliquote massime (45/25/15%). Verificare con cura la robustezza della stima ex post: a fascia piu' alta corrisponde rischio di scostamento ex post piu' elevato.

### Investimenti misti (beni 4.0 + FER + formazione)
Compilare tutte le tre tipologie nella sezione "Indicazione del progetto di innovazione" dell'Allegato VIII. Ricordare che la **soglia 3%/5% si calcola SOLO sui beni 4.0** (Allegati A/B), non sul totale del progetto (art. 38 co. 4 DL 19/2024).

### Perimetro ibrido struttura/processo
Non e' ammesso. Il certificatore deve scegliere uno dei due perimetri (cap. 2.1 circolare MIMIT). Se l'investimento e' a servizio di piu' processi, vincolato a struttura produttiva (3%).

### Fascia di credito e fattura mista
Le aliquote per scaglione di investimento si applicano a tutto il progetto, non al singolo bene. Non e' ammesso "ottimizzare" la fascia spezzando il progetto.

## Limiti di questo task

- Genera la **bozza testuale** dei documenti, non sostituisce la **firma digitale** ne' la **revisione professionale** del certificatore.
- Non valida la **completezza dei dati** forniti dall'utente (giudizio del certificatore).
- Non genera la **DSAN del beneficiario** ne' la **dichiarazione antiriciclaggio** (Allegato II): documenti del beneficiario, non del certificatore.
- Non sostituisce la **perizia tecnica caratteristiche e interconnessione** (art. 16 DM) ne' la **certificazione contabile** (art. 17 DM).
- Non interagisce con il **portale TR5 GSE**: il caricamento e' adempimento separato.

## Esempi

Vedi `examples/`:
- `conforme-investimento-3-2-mln/expected-output.md` - bozza Allegato VIII per impresa manifatturiera con processo interessato 7,5%
