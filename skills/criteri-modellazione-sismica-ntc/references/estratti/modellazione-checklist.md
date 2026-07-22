# Estratto operativo - Criteri di modellazione (NTC 2018 par. 7.2.6)

Checklist di inquadramento per il progettista strutturale. Ogni punto e' ancorato al testo trascritto in
`../fonti/ntc2018-par-7-2-6.md`. La skill **inquadra**, non costruisce il modello ne' esegue l'analisi.

## 1. Modellazione della struttura (par. 7.2.6)

- [ ] Il modello e' **tridimensionale** e rappresenta le distribuzioni spaziali di massa, rigidezza e resistenza,
      con attenzione alle **forze d'inerzia verticali** indotte (travi di grande luce, sbalzi significativi)?
- [ ] Per comportamento **non dissipativo** o dissipativo con **q**, si usano **leggi costitutive elastiche**?
      (per comportamento dissipativo con capacita' dissipativa esplicita, il legame costitutivo va giustificato)
- [ ] Delle **non linearita' geometriche**, se significative, si tiene conto in entrambi i comportamenti?
- [ ] **Rigidezza fessurata**: in assenza di analisi specifiche, la rigidezza flessionale e a taglio di elementi
      in muratura, c.a. e acciaio-cls e' ridotta **sino al 50%** di quella dei corrispondenti elementi **non
      fessurati** (tenendo conto dello stato limite e della sollecitazione assiale permanente)?
- [ ] **Orizzontamenti infinitamente rigidi** nel piano (se le aperture non ne riducono la rigidezza) assunti
      solo se: **c.a.**; oppure **latero-cemento con soletta c.a. >= 40 mm**; oppure **struttura mista con soletta
      c.a. >= 50 mm** collegata da connettori a taglio?
- [ ] **Elementi non strutturali non collaboranti** (tamponature, tramezzi) rappresentati **solo in termini di
      massa**? (il contributo di rigidezza/resistenza si considera **solo** se ha **effetti negativi** sulla
      sicurezza)

## 2. Modellazione dell'azione sismica (par. 7.2.6)

- [ ] L'azione e' modellata con **forze statiche equivalenti**, **spettri di risposta** o **storie temporali**
      opportunamente selezionate?
- [ ] In presenza di **risposta sismica locale (RSL)** o **interazione terreno-struttura (ITS)**:
      - lo spettro (con **5% di smorzamento**) e' **>= 70%** di quello per **sottosuolo A** (§3.2.3.2)?
      - la risultante di **taglio + sforzo normale** alla fondazione e' **>= 70%** di quella a **base fissa**
        (sottosuolo A)?
      - si evita l'uso di **storie temporali artificiali** per RSL e ITS con legami isteretici (§3.2.3.6)?
- [ ] **Eccentricità accidentale** del centro di massa attribuita in ogni direzione (variabilita' spaziale del
      moto e incertezze)? Per i **soli edifici** e in assenza di determinazioni piu' accurate:
      - **e_a >= 0,05 x** dimensione media dell'edificio **perpendicolare** alla direzione dell'azione sismica;
      - assunta **costante** (entita' e direzione) su **tutti gli orizzontamenti**.

## Fuori scope (rinvii)

- **Non** costruisce il modello ne' esegue l'analisi (metodi al par. 7.3); **non** determina **q**.
- **Risposta sismica locale** e storie temporali: par. 3.2.3.6; **fondazioni miste**: par. 6.4.3.
- **Regolarita' strutturale** (par. 7.2.1) e **spostamenti di interpiano allo SLD** (par. 7.3.6.1): skill
  `regolarita-strutturale-sismica-ntc` e `spostamenti-interpiano-sld-ntc`.
