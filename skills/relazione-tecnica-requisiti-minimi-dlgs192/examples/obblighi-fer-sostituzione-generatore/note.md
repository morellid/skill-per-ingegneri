# Note - sostituzione del generatore e obbligo FER

Caso **problematico**: l'errore da intercettare è l'equivalenza "relazione tecnica esclusa" =
"nessun adempimento energetico". Il D.Lgs. 5/2026 la rompe su due fronti (ambito dell'Allegato III
esteso alla ristrutturazione dell'impianto termico; comunicazione al Comune quando la relazione non è
dovuta).

- Fonti: `references/fonti/dlgs-5-2026-allegato-iii.md` (art. 29; Allegato III Sezioni A, B, C, D) e
  `references/fonti/dlgs-192-2005-art8-15.md` (art. 8 c. 1, esclusioni).
- Punti chiave verificati sul testo:
  - **Sezione A punto 1**: campo di applicazione esteso agli "edifici esistenti oggetto di interventi
    di ristrutturazione dell'impianto termico"; criterio temporale sulla richiesta del titolo
    edilizio, "decorsi centottanta giorni dall'entrata in vigore del presente decreto".
  - **Sezione B punto 1 lett. d)**: **15%** della somma dei consumi per climatizzazione invernale ed
    estiva. Una sola quota, senza obbligo autonomo su ACS.
  - **Sezione B punto 2**: divieto di effetto Joule, con l'unica eccezione delle unità immobiliari in
    **classe B o superiore** introdotta dal D.Lgs. 5/2026.
  - **Sezione B punto 3**: k = **0,025** per gli edifici esistenti; **Sezione B punto 5**: +5 punti
    solo per edifici pubblici.
  - **Sezione D punto 1**: motivazione nella relazione ex art. 8 c. 1, esaminando tutte le opzioni
    tecnologiche; **se la relazione non è dovuta, comunicazione al Comune** secondo le modalità da
    esso individuate.
  - **Sezione D punto 2**: obbligo compensativo su EP H,C,W,nren limitato a edifici nuovi e
    ristrutturazioni importanti di **primo** livello.
- Cose deliberatamente **non** decise nell'output atteso:
  - Se la sostituzione della caldaia integri o no una "ristrutturazione dell'impianto termico": la
    definizione è nel DM 26/6/2015 come modificato dal DM MASE 28/10/2025, che non è fonte di questa
    skill. L'output impone la verifica invece di sostituirsi ad essa.
  - La decorrenza del 3 agosto 2026: ancorata alla data di entrata in vigore attestata da Normattiva
    (4/2/2026) più 180 giorni di calendario, e accompagnata dalla riserva sull'ambiguità della
    formula "presente decreto" e sul caso in cui non sia richiesto alcun titolo edilizio.
  - La **formula** della potenza elettrica FER: pubblicata come immagine in Gazzetta, non
    trascrivibile. L'output cita i soli parametri descritti a parole e rinvia all'originale.
- Cross-reference: per l'esercizio e il controllo dell'impianto termico dopo la sostituzione vedi la
  skill `esercizio-controllo-impianti-termici-dpr74`.
