# Task: classifica-intervento-sismico

Classifica un intervento come **"rilevante"**, **"di minore rilevanza"** o **"privo di
rilevanza"** per la pubblica incolumita' ai sensi dell'**art. 94-bis del DPR 380/2001** e ne
deduce il **regime** (autorizzazione preventiva vs deposito/denuncia). Non esegue calcoli ne'
sostituisce le linee guida/regioni.

## Input

- Tipo di intervento: adeguamento/miglioramento sismico, riparazione/intervento locale, nuova
  costruzione (ordinaria o atipica/complessa), edificio strategico/opera infrastrutturale.
- **Zona sismica** (1/2/3/4) e, per la zona 2, il valore di **ag** (0,15-0,20 g oppure
  0,20-0,25 g).
- Destinazione d'uso e presenza di persone.

## Procedura

1. **Interventi "rilevanti" (art. 94-bis c. 1 lett. a)**
   - Adeguamento/miglioramento sismico su esistente in **zona 1** o **zona 2** (ag
     **0,20-0,25 g**) (a.1);
   - **nuove costruzioni** atipiche o di **particolare complessita' strutturale** (escluse
     zone 3-4) (a.2);
   - **edifici strategici**/opere infrastrutturali rilevanti per protezione civile o con
     conseguenze gravi in caso di collasso (escluse zone 3-4) (a.3).

2. **Interventi "di minore rilevanza" (art. 94-bis c. 1 lett. b)**
   - Adeguamento/miglioramento su esistente in **zona 2** (ag **0,15-0,20 g**) e **zona 3**
     (b.1);
   - **riparazioni e interventi locali** (anche su edifici/opere di cui alla lett. a.3) (b.2);
   - **nuove costruzioni** non atipiche (non rientranti in a.2) (b.3);
   - nuove costruzioni a **presenza occasionale** di persone e **edifici agricoli** (punto
     2.4.2 NTC 2018) (b.3-bis).

3. **Interventi "privi di rilevanza" (art. 94-bis c. 1 lett. c)**
   - Interventi che, per caratteristiche intrinseche e destinazione d'uso, **non costituiscono
     pericolo** per la pubblica incolumita'.

4. **Regime conseguente (art. 94-bis cc. 3-6)**
   - **Rilevanti** → **autorizzazione preventiva** dell'ufficio tecnico regionale (c. 3, ex
     art. 94), ferma la denuncia/deposito (art. 93).
   - **Minore rilevanza / privi di rilevanza** → **niente autorizzazione preventiva** (deroga,
     c. 4), salvo **controlli a campione** regionali (c. 5); resta il deposito ex art. 93 (ove
     dovuto) e restano ferme le procedure degli **artt. 65 e 67 c. 1** (c. 6).
   - Rinvia alle **linee guida MIT** (DM 30/4/2018) e alle **elencazioni regionali** per il
     dettaglio (c. 2).

## Output

Classificazione dell'intervento (rilevante / minore / privo di rilevanza) motivata per zona
sismica e tipologia, con il **regime** conseguente (autorizzazione vs deposito) e i rinvii a
linee guida/regioni. Rinvia la classificazione puntuale e i calcoli al progettista e
all'ufficio regionale.

## Riferimenti

- `../references/fonti/dpr-380-2001-93-94-94bis.md` (art. 94-bis)
- `../references/estratti/sismica-checklist.md` (sez. 3)
