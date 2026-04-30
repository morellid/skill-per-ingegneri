# Task: Calcolo della riduzione dei consumi energetici

Imposta in modo metodologicamente corretto il calcolo della riduzione dei consumi energetici (>=3% struttura produttiva o >=5% processo interessato) secondo l'art. 9 del DM 24/7/2024 e il cap. 2 della circolare MIMIT 25877/2024. Restituisce un foglio di calcolo strutturato con baseline ex ante, indicatori di prestazione, normalizzazione, scenario controfattuale (dove applicabile) e conversione in tep.

## Obiettivo

Restituire all'utente:

- La **definizione del perimetro** del programma di misura: struttura produttiva o processo interessato (con motivazione conforme agli esempi 1-4 della circolare MIMIT cap. 2.1).
- La **baseline energetica ex ante** in tep, suddivisa per vettore energetico, con dichiarazione del metodo di determinazione (dati misurati / stima da carichi tracciabili / dati riproporzionati / scenario controfattuale).
- Gli **indicatori di prestazione energetica** caratteristici del settore/processo (selezionati dalla tabella della circolare o equivalenti documentati).
- Le **variabili operative di normalizzazione** ex ante e ex post, con rationale.
- L'**algoritmo di calcolo** dei risparmi, esplicito e applicato.
- Il **risparmio annuo in tep e in percentuale**, con verifica del rispetto della soglia minima.
- La **descrizione dello scenario controfattuale** con almeno 3 alternative di mercato (UE/SEE, ultimi 5 anni), dove applicabile.
- Una **lista di documenti probatori** da conservare (foglio di calcolo, schede tecniche, schemi d'impianto, documentazione misurazioni, fonti BREF/BAT/letteratura).

## Input richiesti

Variabili minime da raccogliere (chiedere se non fornite):

1. **Tipologia di impresa**:
   - attiva da piu' di 12 mesi con dati misurati: si'/no;
   - attiva da 6-12 mesi con dati misurati: si'/no;
   - di nuova costituzione (<6 mesi o variazione sostanziale prodotti/servizi <6 mesi): si'/no.

2. **Perimetro selezionato**:
   - struttura produttiva (sito su particelle catastali contigue, autonomia tecnico-funzionale-organizzativa);
   - processo interessato (linea/processo che garantisce in autonomia la trasformazione input/output).

3. **Beni oggetto di investimento**:
   - elenco beni materiali Allegato A L. 232/2016 (descrizione, voce di allegato, costo);
   - elenco beni immateriali Allegato B L. 232/2016 (descrizione, voce, costo);
   - beni autoproduzione FER (tipologia, potenza in kW elettrico/termico, dati catastali, POD, CENSIMP);
   - costo totale beni 4.0, costo totale FER, costo formazione.

4. **Dati di consumo ex ante** (per ciascun vettore energetico, sui 12 mesi precedenti l'avvio del progetto):
   - energia elettrica prelevata da rete [kWh] e/o autoprodotta [kWh];
   - gas naturale [Sm3] o [kWh termici];
   - gasolio [t] / [l];
   - GPL [t] / [l];
   - olio combustibile [t];
   - calore acquistato [MWh termici];
   - vapore di processo [t] o [MWh termici];
   - altri vettori (specificare).

5. **Variabili operative ex ante** sulla stessa finestra temporale:
   - volume produttivo [unita' adeguata: t, kg, m3, l, kWh, n. pratiche, etc.];
   - condizioni esterne rilevanti (gradi-giorno, temperature, fattore di carico, stagionalita').

6. **Stima dei consumi ex post** (situazione conseguibile per il tramite degli investimenti):
   - per ciascun vettore energetico, valore atteso post intervento;
   - metodologia di stima: dati misurati post (se intervento gia' completato), schede tecniche fornitore, modellizzazione, prove in situ, BREF/BAT, dati di letteratura.

7. **Indicatori di prestazione energetica** scelti:
   - es. tep/t prodotto, tep/m3 acqua trattata, tep/n. pezzi, tep*GG/m2;
   - fonte normativa o di settore di riferimento (BREF, BAT, studi MISE/ENEA, offerte mercato).

8. **Scenario controfattuale** (se l'impresa e' di nuova costituzione o l'intervento comporta sostanziale modifica del servizio reso):
   - per ciascun bene agevolato, almeno 3 alternative disponibili sul mercato UE/SEE negli ultimi 5 anni;
   - per ciascuna alternativa: marca, modello, prestazione, prezzo, fonte dati.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-24-07-2024-articoli-chiave.md` - art. 9 (criteri determinazione risparmi)
- `references/estratti/circolare-mimit-criteri-risparmio.md` - cap. 2 (definizioni operative, indicatori, scenario controfattuale)
- `references/estratti/circolare-mise-2014-tep.md` - coefficienti di conversione in tep

## Procedura

### Passo 1 - Definizione del perimetro (cap. 2.1 circolare MIMIT)

Distinguere fra **struttura produttiva** e **processo interessato**:

- **Struttura produttiva**: sito (una o piu' unita' locali su particelle catastali contigue) con autonomia tecnica, funzionale, organizzativa, costituente centro autonomo di imputazione di costi. I consumi sono la **somma** dei consumi dei processi produttivi e dei servizi generali. Soglia minima: **3%**.
- **Processo interessato**: il processo produttivo interessato dalla riduzione, che includa **tutti i beni materiali e immateriali oggetto di investimento** e che garantisca **in autonomia la trasformazione dell'input nell'output del processo**. Soglia minima: **5%**.

**Regole operative** (cap. 2.1, esempi 1-4):

- Se l'investimento riguarda **un solo bene materiale facente parte di un processo produttivo**: il processo interessato include i componenti complementari necessari alla trasformazione (es. componenti 1c+2c+3c, dove 2c e' l'investimento). Non e' ammissibile escludere componenti necessari (esempio 1, fig. 3).
- Se l'investimento riguarda **due o piu' beni materiali dello stesso processo**: il processo interessato deve includere tutti i beni oggetto di investimento, non separatamente. Vedi esempi 2, fig. 5-8.
- Se l'investimento riguarda un **bene immateriale a servizio di un processo**: il processo interessato comprende i beni materiali su cui il software/sistema agisce, salvo che questi garantiscano in autonomia la trasformazione (esempi 3, fig. 9-11).
- Se l'investimento riguarda **beni a servizio di piu' processi produttivi**: il calcolo va fatto **sull'intera struttura produttiva** (esempi 4, fig. 12-16).

> Eccezione: bene immateriale che riduce consumi su un solo processo e si interfaccia (senza ridurre consumi) con beni di altri processi: e' possibile riferirsi sia al processo sia alla struttura (cap. 2.1 fig. 17).

**Output del passo 1**: dichiarazione motivata della scelta del perimetro, con citazione dell'esempio applicabile della circolare MIMIT.

### Passo 2 - Baseline ex ante (art. 9 co. 2 DM)

Determinare la **situazione ex ante** secondo la tipologia dell'impresa:

| Tipologia | Modalita' |
|---|---|
| Impresa attiva >12 mesi con dati misurati | Direttamente sui dati disponibili (es. fatture energia, contatori dedicati, MID-conformi) |
| Impresa attiva >12 mesi senza dati misurati | Stima tramite analisi dei carichi energetici basata su **dati tracciabili**: schede tecniche, modellizzazione (anche con software), prove in situ, BREF, BAT, analisi di mercato, analisi dei volumi produttivi |
| Impresa attiva 6-12 mesi con dati misurati | Dati misurati **riproporzionati** sull'intera annualita' |
| Impresa di nuova costituzione (<6 mesi) | **Scenario controfattuale** (vedi Passo 5) |

**Tabella baseline ex ante** da compilare:

| Vettore energetico | Consumo ex ante (unita' naturale) | Fattore tep (rinvio circ. MISE 2014) | Consumo ex ante in tep |
|---|---|---|---|
| Energia elettrica prelevata da rete | [kWh] | 0,000187 tep/kWh | [...] |
| Energia elettrica autoprodotta da FER | [kWh] | 0,000187 tep/kWh | [...] |
| Gas naturale | [Sm3] | [vedi circ.] | [...] |
| Gasolio | [t] | [vedi circ.] | [...] |
| GPL | [t] | [vedi circ.] | [...] |
| Calore acquistato | [MWh termici] | [vedi circ.] | [...] |
| Altri vettori | [...] | [...] | [...] |
| **Totale baseline ex ante (tep/anno)** | | | **[somma]** |

> **Importante**: includere anche l'energia autoprodotta in sito da fonti rinnovabili (cap. 2 circolare MIMIT, in fine).

> **Strumenti di misura**: devono essere conformi alla **direttiva MID 2014/32/UE** e alla normativa tecnica di settore (art. 9 co. 4 DM). Tarature in corso di validita'.

### Passo 3 - Variabili operative e indicatori di prestazione (art. 9 co. 3 DM, cap. 2 circolare)

Selezionare:

a. **Variabili operative** sulle quali normalizzare i consumi:
   - volume/quantita' produttiva (es. tonnellate prodotte, kg di filato, m3 di acqua);
   - servizio reso (es. n. pratiche gestite, fatturato, n. dipendenti);
   - condizioni esterne (gradi-giorno, temperature medie, fattore di carico).

b. **Indicatore di prestazione energetica** caratteristico del settore (cap. 2, tab. 2 circolare):
   - es. settore ceramico: tep/t prodotto ceramico lavorato;
   - es. settore servizi: tep/n. pratiche gestite o tep/EUR fatturato;
   - es. BMS regolazione termica: (tep*GG)/m2 o (tep*GG)/n. occupanti.

> Per ogni indicatore selezionato, dichiarare la **fonte** (BREF, BAT, letteratura tecnica, offerte di mercato, studi di settore, documentazione MISE/ENEA).

**Tabella indicatori ex ante**:

| Indicatore | Unita' di misura | Valore ex ante | Fonte / motivazione |
|---|---|---|---|
| [es. Cons. specifico processo X] | tep/t | [...] | [es. media 12 mesi precedenti, fatture + produzione MES] |

### Passo 4 - Stima ex post (art. 9 co. 3 DM)

Determinare i **consumi conseguibili per il tramite degli investimenti complessivi** (situazione ex post):

- Compilare la stessa tabella baseline (vettori energetici -> tep) con i valori attesi post intervento.
- Documentare la **metodologia di stima**: schede tecniche fornitore, modellizzazione, prove in situ, BREF, BAT, dati di letteratura, calcoli analitici.

**Tabella consumi ex post (stima)**:

| Vettore energetico | Consumo ex post (unita' naturale) | Fattore tep | Consumo ex post in tep | Metodo di stima |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [scheda tecnica fornitore X] |
| **Totale ex post (tep/anno)** | | | **[somma]** | |

**Tabella indicatori ex post**:

| Indicatore | Unita' di misura | Valore ex post |
|---|---|---|
| [es. Cons. specifico processo X] | tep/t | [...] |

### Passo 5 - Scenario controfattuale (art. 9 co. 5 DM, cap. 2.2 circolare)

Applicabile a:

a. **imprese di nuova costituzione** (<6 mesi o variazione sostanziale prodotti/servizi <6 mesi);
b. **interventi che comportano una sostanziale modifica del servizio reso** tale da non consentire la corretta normalizzazione delle prestazioni energetiche dalla situazione ex ante alle condizioni ex post.

**Procedura**:

1. Per ciascun bene agevolato, individuare **almeno 3 alternative di beni analoghi** disponibili sul mercato UE/SEE negli ultimi **5 anni**.
2. Per ciascuna alternativa, determinare il **consumo energetico medio annuo** (da scheda tecnica, banca dati, studio di settore).
3. Calcolare la **media** dei consumi delle 3 alternative -> ottieni il consumo del componente nello scenario controfattuale.
4. Sommare i consumi dei componenti dello scenario controfattuale -> ottieni il consumo della struttura produttiva o del processo interessato nello scenario controfattuale.

**Tabella scenario controfattuale** (per ogni bene agevolato):

| Bene agevolato | Alternativa 1 | Alternativa 2 | Alternativa 3 | Consumo medio (tep/anno) |
|---|---|---|---|---|
| Bene 1 [marca/modello investito] | [marca/modello/prezzo/cons.] | [...] | [...] | [media] |
| Bene 2 [...] | [...] | [...] | [...] | [media] |

**Consumo controfattuale totale (tep/anno)**: [somma].

> **Confronto**: nei casi in cui si applica lo scenario controfattuale, il risparmio si calcola come `Risparmio = Consumo_controfattuale - Consumo_ex_post`.

### Passo 6 - Algoritmo di calcolo dei risparmi (art. 9 co. 1 e 3 DM)

Forma generale (modello Allegato VIII/X della circolare):

```
Risp_tep = (Indicatore_ex_ante - Indicatore_ex_post) * Variabile_operativa_post
```

Oppure, se si lavora direttamente sui consumi assoluti:

```
Risp_tep = Consumo_tep_ex_ante - Consumo_tep_ex_post
```

Oppure, in scenario controfattuale:

```
Risp_tep = Consumo_tep_controfattuale - Consumo_tep_ex_post
```

**Riduzione percentuale**:

```
Riduzione_% = Risp_tep / Consumo_tep_ex_ante * 100
```

(o, in scenario controfattuale, `Risp_tep / Consumo_tep_controfattuale * 100`).

**Verifica delle soglie**:

| Perimetro | Soglia minima | Riduzione calcolata | Esito |
|---|---|---|---|
| Struttura produttiva | >=3% | [X%] | [Conforme / Non conforme] |
| Processo interessato | >=5% | [X%] | [Conforme / Non conforme] |

> Una sola delle due soglie deve essere soddisfatta (a seconda del perimetro selezionato al Passo 1).

### Passo 7 - Fascia di risparmio per il credito d'imposta

Identificare la **fascia di riduzione conseguita** ai fini del calcolo del credito d'imposta (art. 10 DM, tab. 1 circolare):

| Riduzione struttura produttiva | Riduzione processo interessato | Fascia |
|---|---|---|
| 3% - 6% | 5% - 10% | **Fascia 1** (aliquote 35/15/5%) |
| 6% - 10% | 10% - 15% | **Fascia 2** (aliquote 40/20/10%) |
| > 10% | > 15% | **Fascia 3** (aliquote 45/25/15%) |

(Le aliquote si applicano per scaglioni di investimento: fino a 2,5 mln EUR / da 2,5 a 10 mln EUR / da 10 a 50 mln EUR.)

> La skill **non calcola** il credito d'imposta finale ai fini della compensazione: il computo e' adempimento del consulente fiscale dell'impresa, sulla base della classificazione delle voci di costo e dell'eventuale ripartizione fra annualita'.

### Passo 8 - Output

Produrre il report nel formato:

```markdown
# Calcolo riduzione consumi energetici - Piano Transizione 5.0

**Data**: [oggi]
**Soggetto beneficiario**: [...]
**Struttura produttiva (dati catastali)**: [...]
**Perimetro del programma di misura**: [struttura produttiva | processo interessato]
**Motivazione della scelta del perimetro**: [...]
**Tipologia di impresa per baseline**: [>12 mesi misurata | >12 mesi stimata | 6-12 mesi | nuova costituzione]
**Riferimenti normativi**: art. 9 DM 24/7/2024, cap. 2 circolare MIMIT 25877/2024.

## 1. Baseline ex ante
[Tabella per vettore energetico -> tep]
**Totale baseline ex ante**: [X tep/anno]

## 2. Variabili operative e indicatori di prestazione
[Tabella]

## 3. Stima ex post
[Tabella per vettore energetico -> tep, con metodo di stima]
**Totale ex post**: [Y tep/anno]

## 4. Scenario controfattuale (se applicabile)
[Tabella alternative, se applicabile]
**Consumo controfattuale**: [Z tep/anno]

## 5. Algoritmo di calcolo
[Formula esplicitata]
- Risparmio annuo: [Risp tep/anno]
- Riduzione percentuale: [%]

## 6. Verifica soglia
| Perimetro | Soglia | Riduzione | Esito |
| ... | ... | ... | ... |

## 7. Fascia di risparmio per credito d'imposta
[Fascia 1 / 2 / 3]

## 8. Documentazione probatoria da conservare (5 anni - art. 19 DM)
- Foglio di calcolo dell'algoritmo dei risparmi (con tutti i dati: consumi, variabili operative, indicatori, fattori tep)
- Schede tecniche dei componenti ante e post intervento
- Schemi d'impianto con posizionamento misuratori
- Specifiche tecniche degli strumenti di misura (conformita' MID 2014/32/UE, tarature)
- Documentazione utilizzata per la stima ex ante (es. fatture, contatori, BREF, BAT, letteratura)
- Documentazione utilizzata per la stima ex post (schede fornitore, modellizzazione, prove in situ)
- Per scenario controfattuale: documentazione delle 3 alternative per ciascun bene (offerte di mercato, schede tecniche, banche dati)

## 9. Elementi non automaticamente verificabili dalla skill
- Conformita' degli strumenti di misura alla direttiva MID 2014/32/UE (verifica tarature)
- Adeguatezza degli indicatori di prestazione al settore specifico (giudizio del certificatore)
- Veridicita' delle stime di consumo ex post (giudizio del certificatore con sopralluogo)
- Rappresentativita' della baseline 12 mesi (eventuali eventi eccezionali, fermi macchina, stagionalita' atipica)
- Conformita' tecnica dei beni agli allegati A/B L. 232/2016 (oggetto della perizia art. 16 DM)
- DNSH e attivita' escluse (oggetto del task `verifica-ammissibilita.md`)

## 10. Avvertenze e rinvio professionale
- Il presente calcolo e' **strumentale alla redazione della certificazione ex ante / ex post** ma deve essere **rivisto e validato dal valutatore indipendente** ai sensi dell'art. 15 DM 24/7/2024.
- I coefficienti di conversione in tep applicati sono quelli della circolare MISE 18/12/2014: verificare aggiornamenti vigenti alla data di asseverazione.
- La normalizzazione tramite indicatori di prestazione e' lo strumento per garantire il calcolo a parita' di servizio reso. La scelta degli indicatori e delle variabili operative e' di responsabilita' del certificatore, che deve documentarne le fonti.
- Il foglio di calcolo dell'algoritmo deve essere conservato in azienda per 5 anni (art. 19 DM) e reso disponibile in caso di vigilanza/controllo GSE.

**Il presente calcolo e' uno strumento di supporto e non sostituisce il giudizio professionale.**
```

## Casi limite da gestire

### Indicatore di prestazione non disponibile per il settore
Se il settore non e' fra quelli esemplificati nella tab. 2 della circolare MIMIT, il certificatore deve:
1. Costruire l'indicatore tramite **analogia** con settori simili o con dati di letteratura specifica;
2. Documentare la **fonte** dell'analogia;
3. Validare la **rappresentativita'** dell'indicatore tramite analisi sensitivita' (rapporti tra i consumi e variabili operative su piu' periodi).

Segnalare il caso come **da approfondire** nella relazione tecnica.

### Stagionalita' o eventi eccezionali nei 12 mesi di baseline
Se nei 12 mesi di baseline si sono verificati eventi che rendono i dati non rappresentativi (es. fermi prolungati, inattivita' COVID, picchi anomali di produzione), il certificatore deve:
1. **Normalizzare** i dati alle condizioni standard;
2. Documentare l'evento eccezionale e la metodologia di normalizzazione;
3. Valutare se utilizzare un periodo piu' lungo (es. media triennale) come riferimento, motivandolo.

Segnalare il caso esplicitamente nella relazione tecnica.

### Investimenti che alterano profondamente il servizio reso
Se l'intervento modifica sostanzialmente il prodotto/servizio (cambio di SKU, aggiunta di lavorazioni, dismissione di linee), la **normalizzazione dei consumi ex ante** ai sensi dell'art. 9 co. 3 puo' non essere applicabile. In tal caso applicare lo **scenario controfattuale** anche per imprese non di nuova costituzione (cap. 2.2 circolare MIMIT).

### Impianti FER per autoconsumo
L'energia elettrica prodotta dall'impianto FER (art. 7 DM) e autoconsumata dalla struttura **rientra nel computo dei consumi della struttura produttiva** (cap. 2 circolare). La riduzione dei consumi imputabile alla FER e' rilevante ai fini del **credito d'imposta** ma **non concorre alla soglia minima 3%/5%** (che si calcola **esclusivamente sui beni 4.0** allegati A/B L. 232/2016, cfr. art. 38 co. 4 DL 19/2024).

### Mix di processi - calcolo per struttura produttiva
Se gli investimenti riguardano piu' processi produttivi nella stessa struttura, **non e' ammesso** calcolare la riduzione separatamente per ogni processo: il calcolo va fatto sulla struttura produttiva (cap. 2.1 esempio 4 circolare). Soglia: 3%.

### Discrepanze fra dati misurati e schede tecniche
Se i dati misurati ex ante divergono significativamente dalle schede tecniche dei componenti, il certificatore deve **prevalentemente fidarsi dei dati misurati** (sono autoritativi per definizione di "dati tracciabili" art. 9 co. 2 DM), salvo dimostrare errori di misura. Documentare la discrepanza.

## Limiti di questo task

- Genera la **struttura del calcolo**, non sostituisce le **misurazioni in campo** ne' il **giudizio del certificatore** sulla rappresentativita' dei dati.
- I **coefficienti di conversione tep** indicati sono indicativi (rinvio circ. MISE 2014): verificare i valori vigenti alla data del calcolo.
- Non sostituisce la **direttiva MID 2014/32/UE** per la verifica della conformita' degli strumenti di misura.
- Non valuta la **plausibilita'** dei valori dichiarati (giudizio del certificatore con sopralluogo).
- Non valuta la **conformita' delle schede tecniche fornitore** ai requisiti dell'allegato A/B L. 232/2016 (rinvio perizia art. 16 DM).

## Esempi

Vedi `examples/`:
- `conforme-investimento-3-2-mln/` - calcolo riduzione 10,10% sul processo interessato (linea utensili + software MES) -> Fascia 2
- `non-conforme-cogenerazione-fossili/` - cogenerazione gas naturale: riduzione consumi reale 8,9% ma esclusa per DNSH (art. 5 co. 1 lett. a DM)
