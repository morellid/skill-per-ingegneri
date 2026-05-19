# Task - Pianificazione rinnovo AUA

## Obiettivo

A partire dalla data di rilascio dell'AUA, identificare la finestra di
sei mesi prima della scadenza entro cui presentare l'istanza di
rinnovo ex art. 5 del D.P.R. 59/2013, costruire la checklist documentale
e gestire la continuita' di esercizio "nelle more".

## Input richiesti dall'utente

Chiedere all'utente:

1. **Data di rilascio dell'AUA in essere** (provvedimento finale, non
   data di domanda).
2. **Identificativo dell'AUA**: numero provvedimento, autorita' che l'ha
   rilasciata, eventuale numero protocollo SUAP.
3. **Elenco titoli incorporati** nell'AUA da rinnovare (vedi mapping
   art. 3 co. 1).
4. **Eventuali modifiche intervenute** dopo il rilascio (anche solo non
   sostanziali ex art. 6): elenco e date.
5. **Variazioni nelle condizioni di esercizio** rispetto a quanto
   autorizzato (cicli produttivi, materie prime, capacita').
6. Presenza di **prescrizioni di adeguamento** non ancora completate
   nel provvedimento in essere.

## Fonti

- `references/estratti/dpr-59-2013-aua-perimetro.md` sezione 4 (Durata
  e rinnovo).
- `references/fonti/dpr-59-2013-articoli-1-12.md` artt. 3 co. 6, 5
  e 4 (richiamato in art. 5 co. 3).

## Procedura

### Step 1 - Calcolo data scadenza AUA e finestra di rinnovo

La durata dell'AUA e' **15 anni** dalla data di rilascio (art. 3 co. 6).
Calcolare:

- **Data scadenza AUA**: [data rilascio] + 15 anni
- **Data limite presentazione istanza di rinnovo**: [data scadenza] - 6
  mesi (art. 5 co. 1)

L'art. 5 co. 1 richiede di presentare l'istanza all'autorita' competente,
tramite SUAP, **almeno sei mesi prima della scadenza**.

### Step 2 - Checklist documentale per il rinnovo

L'art. 5 co. 1 richiede la documentazione di cui all'art. 4 co. 1
(stessa documentazione della domanda di rilascio iniziale). L'art. 5
co. 2 stabilisce che, qualora le condizioni di esercizio siano
**immutate**, e' possibile dichiararlo e rinviare alla documentazione
gia' in possesso dell'autorita' competente.

Costruire la checklist:

| Documento | Stato | Note |
|-----------|-------|------|
| Domanda di rinnovo AUA al SUAP (modello unificato art. 10 co. 3 o moduli regionali) | da preparare | indicare i 9 atti ex art. 3 co. 1 a cui si chiede rinnovo |
| Dichiarazione di invarianza condizioni di esercizio (art. 5 co. 2) | da valutare | se SI, rinvio a documentazione in atti; se NO, allegare aggiornamento |
| Aggiornamento documentale per ogni titolo incorporato (art. 4 co. 1) | per ogni titolo | scarichi: schemi reti, qualita' acque; emissioni: bilancio massico, monitoraggi; rifiuti: registri, formulari; acustica: documentazione previsionale aggiornata; fanghi: piani di utilizzo |
| Eventuali modifiche non sostanziali comunicate art. 6 co. 1 | allegare | con riferimenti agli atti di comunicazione |
| Versamento oneri istruttori (art. 8) | da effettuare | secondo tariffe regionali |
| Procura del professionista firmatario | allegare | quando applicabile |
| Documentazione antimafia / dichiarazioni gestore | secondo modulistica regionale | |

### Step 3 - Esercizio nelle more del rinnovo (art. 5 co. 4)

Se l'istanza viene presentata **entro il termine** (almeno 6 mesi prima
della scadenza), l'attivita' puo' **proseguire** sulla base della
precedente autorizzazione fino all'adozione del provvedimento di
rinnovo (art. 5 co. 4).

Conseguenza operativa: il gestore non interrompe l'esercizio anche se
l'istruttoria di rinnovo supera la data di scadenza dell'AUA in essere,
purche' l'istanza sia stata depositata nei tempi. **Se la finestra dei
6 mesi non viene rispettata**, la continuita' non e' garantita e il
gestore rischia di trovarsi senza titolo abilitativo a scadenza.

### Step 4 - Procedura istruttoria

Il rinnovo segue la **procedura dell'art. 4** (art. 5 co. 3). Quindi:

- 30 giorni per verifica formale (art. 4 co. 3);
- 90 / 120 / 150 giorni per il rilascio (art. 4 co. 4 e 5), con
  conferenza di servizi nei casi previsti (art. 4 co. 5).

Per il dettaglio dei termini, vedi `tasks/pianifica-termini.md`.

### Step 5 - Verifica revisione anticipata d'ufficio (art. 5 co. 5)

Avvisare l'utente che l'autorita' competente puo' imporre il **rinnovo
o la revisione delle prescrizioni** prima della scadenza:

- (lett. a) quando le prescrizioni in essere impediscono il conseguimento
  degli obiettivi di qualita' ambientale;
- (lett. b) quando nuove disposizioni di legge UE, statali o regionali
  rendono necessarie modifiche.

In tal caso non e' il gestore a innescare il procedimento, ma l'autorita'
competente; il gestore riceve l'ordine e dovra' adempiere ai termini
fissati dall'atto.

## Output

Un report sintetico (Markdown):

```
# Pianificazione rinnovo AUA - [nome impianto]

## Dati AUA in essere
- Data rilascio: [data]
- Identificativo: [numero / autorita']
- Titoli incorporati: [elenco]

## Date chiave
- Data scadenza AUA (rilascio + 15 anni, art. 3 co. 6): [data]
- Data limite presentazione istanza rinnovo (scadenza - 6 mesi, art. 5
  co. 1): [data]
- Finestra ottimale di presentazione: [data limite] +/- 1 mese

## Condizioni di esercizio
- Invariate rispetto al rilascio: si / no
  - Se si: utilizzare dichiarazione di invarianza ex art. 5 co. 2
  - Se no: produrre documentazione aggiornata ex art. 4 co. 1 per ogni
    titolo modificato

## Checklist documentale
- [checklist personalizzata, output Step 2]

## Continuita' esercizio
- Istanza presentata nei termini -> continuita' garantita ex art. 5 co. 4
- Istanza in ritardo -> rischio interruzione titolo, ricorrere a SUAP

## Avvertenza
La pianificazione presuppone l'invarianza del quadro normativo. Se prima
della scadenza intervengono modifiche di legge (UE, statale, regionale),
l'autorita' competente puo' attivare la revisione d'ufficio ex art. 5
co. 5. La modulistica e le tariffe sono regionali (art. 8).
```

## Limiti del task

- Non valuta nel merito tecnico la documentazione aggiornata (es. non
  verifica se i nuovi dati di scarico rispettano i limiti, se i bilanci
  emissivi sono coerenti, ecc.).
- Non gestisce il caso di **modifica sostanziale intervenuta** prima
  della scadenza: in tal caso si rinvia a `tasks/triage-modifica-art6.md`
  perche' la modifica sostanziale richiede nuova domanda ex art. 4, non
  rinnovo.
- Non sostituisce la modulistica regionale specifica per il rinnovo (le
  Regioni possono richiedere allegati differenti).
- Non considera il caso di **subingresso** del gestore o di altra
  vicenda soggettiva intercorsa fra rilascio e rinnovo, che si tratta
  con disciplina autonoma e non e' parte di questo task.
