# Task: Struttura della Certificazione Ex Post (Allegato X + XI)

Produce la **bozza testuale** della Certificazione Ex Post (Allegato X della circolare MIMIT 25877/2024) e della relativa **Relazione Tecnica** (Allegato XI), conforme al modello vincolante per la comunicazione di completamento sul portale TR5 GSE entro il 28 febbraio 2026.

> **Nota vigenza (2026)**: il termine del 28/2/2026 e' decorso. Il task resta rilevante per: (a) i controlli GSE ex art. 20 DM 24/7/2024, che verificano la coerenza fra certificazione ex ante ed ex post; (b) le pratiche "tecnicamente ammissibili" pagate con il credito dell'89,77% ex art. 8 DL 38/2026 (conv. L. 88/2026), per le quali il comma 3 richiama il DM 24/7/2024 "anche ai fini delle attivita' di controllo". Vedi `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md`.

## Obiettivo

Restituire all'utente:

- La **bozza della Certificazione Ex Post** (Allegato X), con dichiarazione esplicita dell'avvenuta realizzazione degli investimenti conformemente alla certificazione ex ante e dell'**effettivo conseguimento** del risparmio energetico asseverato ex ante.
- La **bozza della Relazione Tecnica Ex Post** (Allegato XI), con dati misurati post intervento e confronto con i valori asseverati ex ante.
- L'analisi degli **scostamenti** rispetto all'ex ante, con motivazione (modifiche al progetto, condizioni operative diverse, scostamento di stima).
- La **verifica del rispetto della soglia minima** alla luce dei dati ex post effettivi.
- La **checklist documentale** per il pacchetto da caricare sul portale TR5 entro il 28 febbraio 2026.

## Prerequisiti

Prima di eseguire questo task, l'utente deve avere:

- **Certificazione Ex Ante** gia' rilasciata e prenotazione confermata sul portale TR5 GSE;
- **Investimenti completati** entro il 31 dicembre 2025 (art. 4 DM 24/7/2024);
- **Dati di consumo ex post effettivi** misurati su un periodo rappresentativo dell'esercizio post intervento;
- **Perizia tecnica asseverata** caratteristiche e interconnessione beni 4.0 (art. 16 DM, art. 1 co. 11 L. 232/2016) e/o **attestato di conformita'** dell'ente certificatore;
- **Certificazione contabile** (art. 17 DM) gia' rilasciata o programmata.

Se uno di questi e' mancante, **rinvia esplicitamente** al task corrispondente o al consulente competente.

## Input richiesti

Riepilogare con l'utente i dati gia' raccolti nelle fasi ex ante:

1. **Riferimento alla Certificazione Ex Ante** rilasciata:
   - data della certificazione ex ante;
   - certificatore di origine (se diverso dall'attuale);
   - codice TR5-XXXXX rilasciato dal portale GSE;
   - risparmio asseverato ex ante (tep/anno e %);
   - perimetro selezionato (struttura produttiva o processo interessato);
   - fascia di credito asseverata.

2. **Eventuali modifiche al progetto** rispetto all'ex ante:
   - [ ] **Nessuna modifica**: confermare;
   - [ ] **Modifiche non sostanziali**: descrivere brevemente in relazione a beni e costi (es. sostituzione bene per indisponibilita' fornitore, lieve variazione costo);
   - [ ] **Modifiche sostanziali** (art. 12 DM + FAQ MIMIT 2.10): aggiunta nuove tipologie di beni, modifica perimetro programma di misura, incremento potenza FER, formazione diversa. **In questo caso non si procede con la ex post**: l'impresa deve aver rinunciato alla domanda e ripresentata.

3. **Dati identificativi del certificatore** (analoghi a `struttura-certificazione-ex-ante.md`):
   - tipo, dati anagrafici, certificazione/iscrizione, polizza, terzieta'.
   - Puo' essere lo stesso certificatore della ex ante o diverso. Se diverso, segnalare la discontinuita' e accertarsi che il nuovo certificatore abbia accesso a tutta la documentazione.

4. **Dati di consumo ex post** misurati (fonti tracciabili: fatture, contatori conformi MID, sistemi di monitoraggio):
   - per ciascun vettore energetico, consumo annuale post intervento [unita' naturale];
   - periodo di rilevazione (preferibilmente 12 mesi post completamento);
   - strumenti di misura utilizzati e tarature.

5. **Variabili operative ex post** sulla stessa finestra temporale:
   - volume produttivo, condizioni esterne, analoghe a ex ante.

6. **Documentazione di completamento**:
   - perizia tecnica caratteristiche/interconnessione (art. 16) - **chi l'ha rilasciata, data, riferimenti**;
   - certificazione contabile (art. 17) - **chi l'ha rilasciata, data, riferimenti**;
   - schede DNSH (Allegato VII) compilate ex post;
   - per FV: attestazione produttore moduli (art. 12 co. 1 lett. a/b/c DL 181/2023);
   - documentazione antiriciclaggio (titolare effettivo).

## Fonti normative

Leggere prima di procedere:

- `references/estratti/circolare-mimit-modelli-certificazioni.md` - Allegati X (Certificazione Ex Post) e XI (Relazione Tecnica)
- `references/estratti/dm-24-07-2024-articoli-chiave.md` - art. 12 (procedura di completamento), art. 15 (certificazioni), art. 20 (controlli)
- `references/estratti/faq-mimit-soggetti-certificatori.md` - FAQ 2.7 (documentazione comunicazione completamento), 2.10 (modifiche)
- `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md` - fase post-chiusura: credito 89,77%, contributo comma 3-bis, obblighi documentali

## Procedura

### Passo 1 - Conferma dei prerequisiti

Verifica con l'utente:

> "Confermi che: (1) la certificazione ex ante e' stata rilasciata in data [...] con prenotazione confermata, (2) gli investimenti sono stati completati entro il 31/12/2025, (3) hai 12 mesi (o un periodo rappresentativo) di dati di consumo ex post misurati, (4) l'impresa e' in possesso della perizia tecnica caratteristiche/interconnessione (art. 16 DM) e della certificazione contabile (art. 17 DM)? Procedo con la bozza dell'Allegato X?"

Se manca uno dei prerequisiti, rinvia.

### Passo 2 - Verifica modifiche al progetto (FAQ MIMIT 2.10)

Verifica con l'utente la natura delle eventuali modifiche:

| Modifica | Tipo | Conseguenza |
|---|---|---|
| Sostituzione bene per indisponibilita' fornitore con bene equivalente nelle stesse voci A/B | Non sostanziale | Documentare nell'ex post |
| Lieve variazione di costo entro la stessa fattura | Non sostanziale | Documentare nell'ex post |
| **Aggiunta di nuove tipologie di beni A/B** non previste in ex ante | **Sostanziale** | **Rinuncia + nuova domanda** |
| **Modifica perimetro programma di misura** (es. da processo interessato a struttura produttiva) | **Sostanziale** | **Rinuncia + nuova domanda** |
| **Aggiunta o sostituzione tipologia FER, incremento potenza** | **Sostanziale** | **Rinuncia + nuova domanda** |
| **Modifica attivita' di formazione** (diversa da quella prevista in ex ante) | **Sostanziale** | **Rinuncia + nuova domanda** |

Se sostanziale: **arresta il task** e indica che l'impresa deve aver rinunciato alla domanda e ripresentato (FAQ 2.10).

### Passo 3 - Bozza Certificazione Ex Post (Allegato X)

Compila il modello vincolante della circolare MIMIT 25877/2024 - Allegato X:

```markdown
# CERTIFICAZIONE EX POST
## Resa ai sensi del DPR 445/2000 artt. 46 e seguenti e degli artt. 359 e 481 del codice penale

[Intestazione del certificatore: come Allegato VIII (ESCo / EGE / ingegnere / perito), con la differenza che per Ex Post il modello richiede esplicitamente la qualifica di "tecnico abilitato che assume funzioni di persona esercente un servizio di pubblica necessita' ai sensi degli artt. 359 e 481 del codice penale".]

## PREMESSO

- che l'impresa **[ragione sociale]** dichiara:
  - di aver effettuato gli investimenti agevolabili ai sensi dell'art. 38 co. 4 DL 19/2024 e DM Transizione 5.0 cosi' come indicato nella documentazione e nei contratti di acquisto di cui ho preso visione;
  - che i costi sono imputabili ex art. 109 commi 1 e 2 TUIR al periodo d'imposta agevolabile, sono stati determinati secondo corretti criteri fiscali e contabili e sono stati correttamente iscritti in bilancio e nel libro cespiti.

## VISTI

- art. 38 DL 2 marzo 2024 n. 19;
- DM Transizione 5.0 24 luglio 2024.

## ATTESTA

- che quanto dichiarato si basa su elementi, dati e informazioni **personalmente acquisiti e verificati** con diligenza tecnico-specialistica, anche mediante l'effettuazione di **sopralluoghi** presso la struttura produttiva;
- che e' stata fornita l'attestazione dell'avvenuta redazione della **Perizia Tecnica Giurata ex art. 1 co. 11 L. 232/2016** la quale attesta che:
  - il progetto di innovazione si caratterizza per l'acquisizione di tecnologie ai sensi dell'art. 38 co. 4 DL 19/2024;
  - le tecnologie acquisite sono **interconnesse** al sistema aziendale di gestione della produzione o alla rete di fornitura;
- di aver **ottenuto, all'interno della struttura produttiva ovvero del processo interessato oggetto del progetto di innovazione proposto, i livelli di efficienza energetica asseverati nella certificazione ex ante** aggiornata a seguito della realizzazione del progetto di innovazione;
- di **essersi dotato di idonea copertura assicurativa**, cosi' come previsto dall'art. 15 co. 8 del DM Transizione 5.0.

## ASSEVERA I CONTENUTI DI SEGUITO RIPORTATI

### Informazioni principali sul progetto di innovazione

[Stesse sezioni dell'Allegato VIII: ragione sociale, P.IVA, CF, indirizzo struttura produttiva, dati catastali, codice ATECO]

### Indicazione di eventuali modifiche al progetto di innovazione

- [ ] **Sono state effettuate modifiche** al progetto di innovazione rispetto a quanto previsto nella certificazione ex ante rilasciata in data [...] dal valutatore indipendente [...] (descrizione delle modifiche in relazione ai beni e ai costi):
  > [...descrizione...]

- [ ] **Non sono state effettuate modifiche** al progetto di innovazione rispetto a quanto previsto nella certificazione ex ante rilasciata in data [...] dal valutatore indipendente [...].

> Le modifiche dichiarate **non rientrano fra quelle sostanziali** ai sensi della FAQ MIMIT 2.10 (aggiunta di nuove tipologie di beni, modifica perimetro programma di misura, incremento potenza FER, formazione diversa). [Se questa affermazione non e' veritiera, l'impresa avrebbe dovuto rinunciare e ripresentare.]

### Indicazione del progetto di innovazione (selezionare la tipologia di investimento sostenuto)

[Selezionare le voci come in Allegato VIII, ma riferite ai **valori conseguiti** non solo a quelli previsti.]

### Beni impiegati

[Stesse selezioni Allegato A (gruppi 1-3) e Allegato B (1-23) come in Allegato VIII, riferite ai beni effettivamente acquisiti.]

### Risparmio conseguito dal progetto di innovazione

- **Risparmio in tep [tep/anno]**: [X effettivo]
- **Risparmio annuo percentuale [%]**: [Y effettivo]

[Confronto con quanto asseverato ex ante: vedi Relazione Tecnica Ex Post]

### Algoritmo di calcolo dei risparmi

`Risp = (Indicatore di prestazione_ex ante - Indicatore di prestazione_ex post) * Variabile operativa_post`

Dove le variabili operative_post sono ora **misurate** non stimate. Vedi Allegato XI per il dettaglio.

### Configurazione di riferimento utilizzata per il calcolo

[Specificare se: misurazione diretta ex ante e ex post, scenario controfattuale (se applicabile in continuita' con l'ex ante)]

### Descrizione dello scenario controfattuale [se applicabile]

[Stesso schema dell'Allegato VIII, aggiornato con eventuali variazioni nei dati delle 3 alternative qualora rilevati a sopralluogo.]

### Impianto/i di autoproduzione previsto/i per l'autoconsumo [se applicabile]

- [ ] Autoconsumo fisico
- [ ] Autoconsumo a distanza

**Dati catastali dell'impianto**:
- Codice catastale del comune: [...]
- Sezione: [...]
- Foglio/i: [...]
- Particella/e: [...]
- Sub: [...]

**POD** al quale e' connesso l'impianto: [...]
**CENSIMP**: [...]

[Stessi campi dell'Allegato VIII per consumi, fabbisogno termico equivalente, combustibili, producibilita' attesa, dati per impianto.]

### Documentazione conservata presso l'impresa beneficiaria

A titolo esemplificativo non esaustivo:
1. Relazione tecnica di certificazione ex post (Allegato XI);
2. Documentazione attestante le specifiche tecniche dei componenti ante intervento e post-intervento (schede tecniche);
3. Schemi d'impianto rappresentativi dell'interconnessione, con evidenza del posizionamento dei misuratori;
4. Documentazione attestante le specifiche tecniche della strumentazione di misura;
5. Foglio di calcolo dell'algoritmo per la determinazione dei risparmi e il dettaglio di tutti i dati ex post;
6. Documentazione utilizzata per la stima ex ante e per la **verifica ex post**;
7. Documentazione fotografica e verbali dei sopralluoghi effettuati;
8. Certificazione ex ante (riferimento) e perizia tecnica ex art. 16 DM (riferimento);
9. Certificazione contabile ex art. 17 DM (riferimento);
10. Schede DNSH compilate ex post.

---

Luogo e data: [...]

Il Certificatore (timbro e firma digitale): [...]
```

### Passo 4 - Bozza Relazione Tecnica Ex Post (Allegato XI)

```markdown
# RELAZIONE TECNICA DI CERTIFICAZIONE EX POST
## Beni funzionali alla trasformazione tecnologica e digitale delle imprese secondo il modello "Transizione 5.0"

> Documento da conservare in azienda per i 5 anni successivi all'erogazione dell'ultima agevolazione (art. 19 DM 24/7/2024).

## 1. Dati identificativi dell'impresa
[come Allegato IX]

## 2. Dati certificatore
[come Allegato IX]

## 3. Riferimenti alla Certificazione Ex Ante e prenotazione GSE

- Certificazione ex ante: rilasciata in data [...] dal certificatore [...]
- Codice TR5-XXXXX di prenotazione: [...]
- Data conferma di avvenuta prenotazione GSE: [...]
- Risparmio asseverato ex ante: [X tep/anno, Y%]
- Perimetro: [struttura produttiva / processo interessato]
- Fascia ex ante: [3-6%/5-10% | 6-10%/10-15% | >10%/>15%]

## 4. Cronologia del progetto

- Data avvio: [data primo impegno irreversibile]
- Data effettuazione ordini: [data]
- Data pagamento acconto >=20%: [data]
- Data completamento (ultimo investimento): [data] - **deve essere <= 31/12/2025**
- Data di interconnessione (per beni A/B): [data]
- Periodo di rilevazione consumi ex post: [da GG/MM/AAAA a GG/MM/AAAA]

## 5. Modifiche al progetto rispetto alla Certificazione Ex Ante

- [ ] Nessuna modifica
- [ ] Modifiche non sostanziali (descrizione e impatto su consumi/risparmio): [...]

> Si dichiara che le modifiche dichiarate **non rientrano fra quelle sostanziali** ex FAQ MIMIT 2.10.

## 6. Dati registrati ex post (per vettore energetico)

| Vettore | Periodo (12 mesi) | Consumo ex post (unita' naturale) | Fonte (fatture, contatori, sistemi monitoraggio) | Strumento di misura (conformita' MID, taratura) |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] |

## 7. Variabili operative ex post

| Variabile | Unita' di misura | Valore ex post | Fonte (MES, ERP, DDT) |
|---|---|---|---|

## 8. Indicatori di prestazione ex post

| Indicatore | Unita' di misura | Valore ex post | Confronto con valore ex ante |
|---|---|---|---|

## 9. Algoritmo di calcolo applicato ai dati ex post

`Risp_tep = (Indicatore_ex_ante - Indicatore_ex_post) * Variabile_operativa_post`

[Applicazione passo passo ai dati misurati]

- Risparmio in tep/anno (effettivo): [X]
- Riduzione percentuale (effettiva): [Y%]

## 10. Conversione in tep

[Stesso schema Allegato IX, applicato ai consumi ex post.]

## 11. Confronto ex ante / ex post

| Voce | Valore ex ante (asseverato) | Valore ex post (effettivo) | Scostamento (%) | Motivazione (se rilevante) |
|---|---|---|---|---|
| Risparmio in tep/anno | [...] | [...] | [...] | [...] |
| Riduzione % | [...] | [...] | [...] | [...] |
| Indicatori di prestazione | [...] | [...] | [...] | [...] |

> **Critico**: l'art. 20 co. 2 lett. b DM dispone che i controlli GSE verifichino la **congruenza tra risparmi certificati ex ante e risparmi effettivamente conseguiti ex post**. Scostamenti significativi richiedono motivazione documentata.

## 12. Verifica del rispetto della soglia minima ex post

| Perimetro | Soglia minima | Riduzione effettiva | Esito |
|---|---|---|---|
| Struttura produttiva | >=3% | [...%] | [Conforme / Non conforme] |
| Processo interessato | >=5% | [...%] | [Conforme / Non conforme] |

[Se la riduzione ex post **scende sotto la soglia ex ante asseverata** ma **resta sopra la soglia minima 3%/5%**: il progetto e' ancora ammissibile, **ma il credito d'imposta sara' calcolato sulla fascia inferiore** corrispondente alla riduzione effettivamente conseguita.]

[Se la riduzione ex post **scende sotto la soglia minima 3%/5%**: il progetto **decade dal beneficio** (art. 20 DM, eventuali recuperi).]

## 13. DNSH

- Schede DNSH (Allegato VII circolare) **compilate ex post**: A, B, [C, D, E, F1, F2 se pertinenti].
- Riferimento alla DSAN del beneficiario sottoscritta in fase di completamento.

## 14. Documentazione di completamento allegata

- Perizia tecnica asseverata ex art. 16 DM / attestato di conformita' (riferimenti):
  - rilasciata da [ingegnere/perito/ente accreditato];
  - data: [...];
  - n. iscrizione/accreditamento: [...].
- Certificazione contabile ex art. 17 DM (riferimenti):
  - rilasciata da [revisore legale/societa' di revisione];
  - data: [...];
  - n. iscrizione registro D.Lgs. 39/2010: [...].
- Per impianti FV: attestazione produttore moduli (caratteristiche art. 12 co. 1 lett. a/b/c DL 181/2023).

## 15. Strumenti di misura ex post

[Conformita' MID 2014/32/UE, tarature, posizionamento.]

## 16. Riferimenti normativi
[Lo stesso elenco dell'Allegato IX.]

---

Luogo e data: [...]

Il Certificatore (timbro e firma): [...]
```

### Passo 5 - Pacchetto comunicazione di completamento (FAQ MIMIT 2.7)

Lista documenti da caricare sul portale TR5 GSE entro il **28 febbraio 2026**:

1. **DSAN ex DPR 445/2000** firmata digitalmente dal Rappresentante Legale o Delegato (precompilata dal portale);
2. Documento di identita' del Rappresentante Legale/Delegato;
3. Eventuale delega (Allegato I);
4. **Schede tecniche DNSH** compilate (Allegato VII: A, B, C, D, E, F1, F2 a seconda dell'investimento);
5. **Certificazione ex post** firmata digitalmente dal certificatore (Allegato X);
6. Documento di identita' del certificatore;
7. **Attestazione di possesso della Perizia Tecnica e Certificazione Contabile** (Allegato V);
8. Documentazione attestante l'idoneita' del certificatore: per **EGE/ESCo** la certificazione UNI CEI 11339/11352 in corso di validita' (recepita da banca dati Accredia); per **ingegneri sez. A/B** o **periti industriali** "meccanica ed efficienza energetica" / "impiantistica elettrica ed automazione" il certificato di iscrizione all'albo in corso di validita' + curriculum/dichiarazione di esperienza in efficienza energetica dei processi produttivi (art. 15 co. 6 lett. c DM, FAQ MIMIT 2.3);
9. **Dichiarazione di terzieta'** del certificatore (Allegato III);
10. **Dichiarazione di terzieta' per certificatori contabili** (Allegato IV);
11. Per impianti FV: attestazione produttore moduli (DL 181/2023);
12. Dichiarazione titolare effettivo (Allegato II - antiriciclaggio).

L'impresa beneficiaria conserva inoltre **fatture, DDT e documenti** relativi all'acquisizione dei beni, contenenti il **codice TR5-XXXXX** e il riferimento all'art. 38 DL 19/2024.

### Passo 6 - Output

Restituire all'utente:

1. Bozza Certificazione Ex Post (Allegato X)
2. Bozza Relazione Tecnica Ex Post (Allegato XI) - estesa, da conservare
3. Lista pacchetto comunicazione completamento
4. Checklist finale dei controlli pre-firma:

```markdown
## Checklist pre-firma digitale Certificazione Ex Post

- [ ] Investimenti completati entro il 31/12/2025 (verifica con DDT e fatture)
- [ ] Interconnessione comprovata da perizia tecnica art. 16 DM o attestato di conformita' (per beni A/B)
- [ ] Periodo di rilevazione ex post >= 12 mesi (o periodo rappresentativo motivato)
- [ ] Sopralluogo post intervento effettuato e documentato
- [ ] Strumenti di misura ex post conformi MID, tarature in corso
- [ ] Dati ex post tracciabili (fatture, contatori, sistema monitoraggio)
- [ ] Variabili operative ex post coerenti con MES/ERP/DDT
- [ ] Confronto ex ante / ex post chiaramente esposto, con motivazione di eventuali scostamenti
- [ ] **Modifiche al progetto non sostanziali** (FAQ MIMIT 2.10)
- [ ] DSAN DNSH ex post + schede VII compilate
- [ ] Polizza assicurativa professionale in corso di validita'
- [ ] Dichiarazione di terzieta' (Allegato III) firmata
- [ ] Allegato V (attestazione possesso perizia + cert. contabile) acquisito dal beneficiario
- [ ] Per FV: attestazione produttore moduli acquisita
- [ ] Coerenza fra Allegato X e Allegato XI: risparmi, perimetro, beni
- [ ] Pacchetto completo per upload sul portale TR5 entro 28/2/2026
- [ ] Soglia minima 3%/5% **rispettata** ex post (verifica decadenza)
- [ ] Fascia di credito conseguita coerente con quella asseverata in ex ante (segnalare ricalcolo)

## Avvertenza
**La presente bozza e' uno strumento di supporto. Il certificatore deve:**
- rivedere ogni voce e validare i dati misurati ex post;
- effettuare il sopralluogo post intervento e documentarlo;
- motivare scostamenti rispetto all'ex ante;
- firmare digitalmente sotto la propria personale responsabilita';
- conservare la documentazione probatoria per 5 anni (art. 19 DM).

**Il certificatore agisce in qualita' di persona esercente un servizio di pubblica necessita' (artt. 359 e 481 c.p.). False attestazioni espongono a responsabilita' penale aggravata, oltre a revoca del beneficio per il beneficiario, recupero crediti gia' compensati, perdita dell'abilitazione al rilascio.**
```

## Casi limite da gestire

### Riduzione ex post sotto la soglia ex ante ma sopra il minimo
Se la riduzione ex post conseguita scende dalla fascia asseverata in ex ante (es. da "superiore al 10%" a "non inferiore al 5%" sul processo interessato), il progetto resta ammissibile **ma il credito d'imposta sara' ricalcolato** sulla fascia inferiore. La skill segnala il ricalcolo come informazione al beneficiario; l'aggiornamento ufficiale e' del GSE/Agenzia Entrate.

### Riduzione ex post sotto la soglia minima 3%/5%
**Decadenza dal beneficio** (art. 20 DM). La skill **non puo'** assemblare l'Allegato X attestando un risultato che non rispetta le soglie minime: il certificatore deve riscontrare la non conformita' e l'impresa deve avviare le procedure di rinuncia / ricalcolo / recupero.

### Modifiche sostanziali emergenti in ex post
Vedi tabella Passo 2. Se si rileva una modifica sostanziale (cambio perimetro, aggiunta tipologia bene, incremento potenza FER, formazione diversa), il certificatore **non puo' rilasciare la ex post** sul progetto originario: l'impresa deve aver rinunciato e ripresentato (FAQ MIMIT 2.10).

### Cambio di certificatore fra ex ante e ex post
Ammesso. Il nuovo certificatore deve:
1. acquisire dall'impresa **tutta la documentazione ex ante** (certificazione, relazione tecnica, foglio di calcolo, schede tecniche);
2. fare nuovo **sopralluogo** ex post;
3. eseguire la verifica come se fosse stato lui a rilasciare la ex ante (con possibile esito di disallineamento);
4. firmare la propria dichiarazione di terzieta' (Allegato III) - non puo' essere subentrato a un certificatore con cui ha rapporti professionali nei 3 anni precedenti.

### Investimento gia' completato al momento dell'ex ante (FAQ MIMIT 2.13)
Caso particolare: il progetto era gia' completato al momento della prenotazione. La ex post puo' essere caricata direttamente dopo la "Conferma di prenotazione" senza la fase di "Conferma 20%". I dati ex post sono comunque richiesti su un periodo rappresentativo dell'esercizio post intervento.

### Eventi eccezionali nel periodo di rilevazione ex post
La comunicazione di completamento ha **scadenza fissa al 28/2/2026** (art. 12 DM): il periodo di misurazione ex post deve concludersi entro tale data e quindi raramente potra' arrivare a 12 mesi pieni dal completamento (specie per progetti completati a fine 2025). Se gli eventi eccezionali (fermi prolungati, cause esterne, mercato anomalo) alterano la rappresentativita' del periodo disponibile, il certificatore deve: (1) **utilizzare il periodo rappresentativo disponibile** entro la scadenza, applicando la normalizzazione tramite indicatori e variabili operative per assorbire l'effetto, motivando la scelta nella Relazione Tecnica (Allegato XI); (2) se il periodo disponibile e' insufficiente o non rappresentativo, **segnalare il rischio** o la non procedibilita' al beneficiario, evitando di firmare ex post con dati inattendibili. Non e' ammesso posticipare la comunicazione oltre il 28/2/2026.

### Strumenti di misura non MID-conformi nel periodo ex post
Inammissibile. Il certificatore deve richiedere all'impresa la sostituzione/ricalibrazione e ripetere la misurazione. Se cio' non e' possibile, segnalare la non conformita' e non procedere con la ex post (art. 9 co. 4 DM).

### Pratica "tecnicamente ammissibile" pagata con il credito ex art. 8 DL 38/2026
Se l'impresa ha ricevuto dal GSE la comunicazione di ammissibilita' tecnica con esaurimento delle risorse e la successiva ricevuta di conferma del credito 89,77% (piattaforma Transizione 5.0, dal 29/4/2026 - Avviso MIMIT), la certificazione ex post gia' rilasciata resta pienamente rilevante: l'art. 8 co. 3 richiama l'art. 38 DL 19/2024 e il DM 24/7/2024 "anche ai fini delle attivita' di controllo". Il certificatore deve segnalare al beneficiario gli obblighi dell'Avviso MIMIT 29/4/2026: conservare certificazioni, perizie, fatture e documenti di trasporto; comunicare al GSE variazioni societarie e perdita dei requisiti nel quinquennio, cessioni dei beni, destinazioni estranee, mancato riscatto dei leasing. Le spese di certificazione (contabile, riduzione consumi, DNSH) risultanti dalle comunicazioni sono rimborsabili pro quota tramite il contributo del comma 3-bis (57,7/80/60 mln per il 2026/2027/2028), secondo modalita' rimesse a un decreto MIMIT non ancora pubblicato. Dettagli: `references/estratti/dl-38-2026-credito-pratiche-ammissibili.md`.

## Limiti di questo task

- Genera la **bozza testuale** dei documenti, non sostituisce la **firma digitale**, il **sopralluogo** ne' la **verifica delle misurazioni** del certificatore.
- Non valida la **veridicita' dei dati di consumo ex post** dichiarati dall'impresa (giudizio del certificatore con sopralluogo).
- Non valuta gli **scostamenti tecnico-economici** rispetto all'ex ante (giudizio del certificatore).
- Non sostituisce la **certificazione contabile** ne' la **perizia tecnica ex art. 16**.
- Non interagisce con il **portale TR5 GSE**: il caricamento e' adempimento separato.
- Non gestisce il **calcolo aggiornato del credito d'imposta** in caso di scostamento di fascia.
- Non valuta la **scadenza del 28/2/2026**: la skill segnala il termine ma non emette alert temporali.

## Esempi

Vedi `examples/`:
- `conforme-investimento-3-2-mln/expected-output.md` - sintesi confronto ex ante / ex post con riduzione ex post 10,98% (leggermente superiore all'ex ante 10,10%, Fascia 2 mantenuta)
