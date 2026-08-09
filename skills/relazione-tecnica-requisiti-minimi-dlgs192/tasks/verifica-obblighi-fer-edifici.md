# Task: verifica-obblighi-fer-edifici

Stabilisce **se** e **in che misura** scattano gli **obblighi di integrazione delle fonti
rinnovabili negli edifici** dell'**Allegato III del D.Lgs. 199/2021**, come **modificato dall'art. 29
del D.Lgs. 9 gennaio 2026, n. 5** (RED III), e cosa deve contenere di
conseguenza la **relazione tecnica ex art. 8, c. 1, del D.Lgs. 192/2005**.

Fonti: `references/estratti/obblighi-fer-allegato-iii.md`,
`references/fonti/dlgs-5-2026-allegato-iii.md`.

## Input richiesti

- **Categoria di intervento** qualificata secondo il **DM 26/6/2015** come modificato dal **DM MASE
  28/10/2025**: nuova costruzione, ristrutturazione importante di **primo** livello,
  ristrutturazione importante di **secondo** livello, ristrutturazione dell'**impianto termico**, o
  nessuna di queste.
- **Data di presentazione della richiesta del titolo edilizio** (o data prevista).
- Natura dell'edificio: **pubblico** o privato; classificazione energetica delle unita' immobiliari
  se si intende ricorrere a generazione elettrica con effetto Joule.
- **Fabbisogni/consumi previsti** per ACS, climatizzazione invernale, climatizzazione estiva.
- **Superficie in pianta** dell'edificio al livello del terreno (proiezione al suolo della sagoma),
  al netto delle pertinenze.
- Eventuale **allaccio a rete di teleriscaldamento/teleraffrescamento efficiente** e relativa
  copertura del fabbisogno.
- Disponibilita' di superfici su edificio e pertinenze (con geometria delle falde o del tetto piano).

## Procedura

1. **Ambito** (Sezione A punto 1): verificare che l'intervento rientri in una delle quattro
   categorie e che la **richiesta del titolo edilizio** cada **decorsi 180 giorni dall'entrata in
   vigore** del decreto. Il D.Lgs. 5/2026 non ha un articolo di entrata in vigore; la scheda
   Normattiva dell'atto attesta l'**entrata in vigore al 4 febbraio 2026**, quindi
   **180 giorni dopo = 3 agosto 2026**. Se la data e' prossima a quella soglia, **segnalare
   esplicitamente l'ambiguita' testuale** del rinvio a "presente decreto" (vedi estratto, sezione 1)
   e verificare testo vigente ed eventuali chiarimenti MASE: non dare per acquisito il regime.
2. **Quote** (Sezione B punto 1): applicare la riga corrispondente alla categoria.
   - Nuova costruzione: **60%** dei consumi ACS **e** **60%** della somma ACS + clim. invernale +
     clim. estiva (obblighi **contemporanei**).
   - Ristrutturazione importante di **primo** livello: **40%** e **40%** sulle stesse basi.
   - Ristrutturazione importante di **secondo** livello: **15%** della somma clim. invernale +
     clim. estiva.
   - Ristrutturazione dell'**impianto termico**: **15%** della somma clim. invernale + clim. estiva.
3. **Edifici pubblici** (Sezione B punto 5): maggiorare le percentuali del punto 2 di **ulteriori
   cinque punti percentuali** e incrementare del **10%** l'obbligo di potenza elettrica del punto 3.
4. **Effetto Joule** (Sezione B punto 2): escludere l'assolvimento tramite impianti FER che
   producono **solo** energia elettrica destinata a dispositivi di produzione di calore per effetto
   Joule, **salvo** unita' immobiliari in **classe energetica B o superiore**.
5. **Potenza elettrica FER** (Sezione B punto 3): determinarla con la formula dell'Allegato III,
   con **k = 0,025** per edifici esistenti e **k = 0,05** per edifici di nuova costruzione, e **S**
   pari alla superficie in pianta al netto delle pertinenze. La formula e' pubblicata come
   **immagine** nella Gazzetta: **leggerla sulla fonte originale**, non ricostruirla a memoria.
6. **Esonero** (Sezione B punto 4): se l'edificio e' allacciato a **teleriscaldamento e/o
   teleraffrescamento efficiente** ex art. 2 c. 2 lett. tt) del D.Lgs. 102/2014 **con copertura
   integrale** del rispettivo fabbisogno, l'obbligo del punto 1 **non si applica**.
7. **Collocazione** (Sezione C): verificare che gli impianti siano su/dentro l'edificio o nelle
   **pertinenze** (impronta a terra + area confinante non oltre il **triplo** dell'impronta), che il
   **fotovoltaico a terra non concorra**, e che valgano i vincoli geometrici: aderenza/integrazione
   e stesso orientamento e inclinazione su **falda**; su **tetto piano** asse mediano non oltre
   l'altezza minima della balaustra, o **30 cm** in assenza di balaustra.
8. **Deroga** (Sezione D): se l'obbligo non e' assolvibile, **motivare in relazione**
   l'impossibilita' tecnica o la non convenienza economica **esaminando la non fattibilita' di tutte
   le diverse opzioni tecnologiche disponibili**. Se la relazione tecnica **non e' dovuta**, il
   progettista **comunica le stesse informazioni al Comune**. Verificare che l'obbligo compensativo
   su **EP H,C,W,nren < EP H,C,W,nren,limite** sia imposto **solo** a edifici nuovi e a
   ristrutturazioni importanti di **primo** livello; il limite si calcola sull'edificio di
   riferimento (Allegato 1, Cap. 3 del DM 26/6/2015 e s.m.i.) con le efficienze della **Tabella 1**
   dell'Allegato III: **1,54** clim. invernale, **1,28** clim. estiva, **1,28** ACS, gia'
   comprensive del fattore di conversione in energia primaria non rinnovabile.
9. **Verifica e trasmissione** (Sezione E): inserire **calcoli e verifiche nella relazione ex art. 8
   c. 1**, prevedere la **trasmissione di copia al GSE** e ricordare che la verifica e' effettuata
   **dai Comuni su quella relazione**, con possibili ulteriori controlli regionali ex art. 26 c. 7
   del D.Lgs. 199/2021.

## Output atteso

- Determinazione se l'Allegato III **si applica** all'intervento, con categoria e data del titolo
  edilizio citate, e con l'eventuale riserva sulla decorrenza esplicitata.
- **Quote FER** applicabili (una o due, con le rispettive basi di calcolo), maggiorazione per
  edificio pubblico se pertinente, e **potenza elettrica FER** minima richiesta.
- Elenco dei **contenuti da inserire nella relazione tecnica**: calcoli di copertura, verifica della
  potenza elettrica, vincoli di collocazione, eventuale esonero da teleriscaldamento, eventuale
  motivazione di deroga con la verifica compensativa su EP H,C,W,nren dove dovuta.

## Limiti

- La **qualificazione dell'intervento** (primo o secondo livello, ristrutturazione dell'impianto
  termico) dipende dal **DM 26/6/2015 come modificato dal DM MASE 28/10/2025**, non riprodotto:
  e' un **input** del task, non un suo output.
- Il task **non esegue** i calcoli energetici: individua obblighi, basi di calcolo e contenuti da
  documentare.
- I **requisiti e le specifiche tecniche degli impianti** (Allegato II del D.Lgs. 199/2021) e le
  **linee guida CTI** previste dalla Sezione C punto 4 non sono riprodotti: vanno verificati a
  parte.
- La Sezione B punto 6 prevede la **rideterminazione almeno quinquennale** degli obblighi a
  decorrere dal 1° gennaio 2026: verificare sempre il testo vigente prima del deposito.
