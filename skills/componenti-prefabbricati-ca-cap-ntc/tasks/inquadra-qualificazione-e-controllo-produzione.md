# Task — Inquadra la qualificazione e il controllo di produzione dei prefabbricati (NTC 2018 §11.8.1-11.8.4)

Supporto documentale per inquadrare la **dichiarazione delle prestazioni**, i **requisiti dello stabilimento**, il
**controllo di produzione** (calcestruzzo e acciaio) e le **procedure di qualificazione** (serie dichiarata/
controllata) dei componenti prefabbricati in c.a. e c.a.p. secondo le NTC 2018 (DM 17/1/2018). **Non** esegue il
progetto né le verifiche degli elementi.

Fonte: `../references/fonti/ntc2018-par-11-8.md`; checklist: `../references/estratti/prefabbricati-checklist.md`.

## Input tipico

- Tipologia di produzione: **serie dichiarata** (§4.1.10.2.1) o **serie controllata** (§4.1.10.2.2), oppure
  produzione occasionale.
- Elementi già qualificati ai **punti A/C del §11.1** (deposito art. 58 assolto) o no.
- Materiali impiegati: calcestruzzo (classi, cicli tecnologici) e acciaio d'armatura (con/senza marcatura CE).

## Passi

1. **Generalità e dichiarazione delle prestazioni (§11.8.1)**
   - Verifica che la produzione avvenga con **processo industrializzato** e **sistema permanente di controllo della
     produzione in stabilimento** (che comprende il cls secondo §11.2).
   - Per elementi qualificati ai **punti A o C del §11.1** i requisiti procedurali del **deposito art. 58 DPR
     380/2001** si considerano assolti (restano gli adempimenti presso l'ufficio territoriale; art. 56 per pannelli
     portanti); tali prodotti rispettano comunque §§11.8.2, 11.8.3.4 e 11.8.5.
   - Individua il **metodo di dichiarazione**: **Metodo 1** (caratteristiche geometriche e proprietà del
     materiale); **Metodo 2** (proprietà di prodotto con Appendici Nazionali agli Eurocodici); **Metodo 3**
     (specifica di progetto con le NTC). Materiali base **qualificati all'origine** (§11.1).

2. **Requisiti degli stabilimenti (§11.8.2)**
   - Sili/contenitori che evitino confusione; **dosaggio a peso** dei componenti solidi (a volume o peso i
     liquidi) con strumenti tarati; sequenza completa di produzione/controllo; sistema di controllo **documentato**.

3. **Controllo di produzione e sui materiali di serie (§11.8.3)**
   - Sistema qualità **UNI EN ISO 9001** certificato da organismo terzo.
   - **Calcestruzzo**: controllo continuo (§11.2); apparecchiature **tarate annualmente**; registri con data certa
     conservati **10 anni**; prove a **28 giorni**; resistenza caratteristica con **controllo di tipo B** (§11.2.5)
     in stabilimento; controlli esterni presso laboratorio art. 59 con **≥ 1 prelievo ogni 5 giorni** di produzione
     effettiva per ogni cls omogeneo, soggetti a **controllo di tipo A** (§11.2.5) su **3 prelievi consecutivi**;
     verifica statistica almeno **annuale**.
   - **Acciaio**: verifica documentazione in ingresso (§11.3.1.5), rifiuto non conformi; **piegatura su 3 campioni
     ogni 90 t** (min **1 volta/mese**, UNI EN ISO 15630-1, senza cricche); **saldature** UNI EN ISO 17635 (al
     rinnovo **biennale** della qualifica dell'operatore, tutte le prove previste); **trazione su 3 campioni ogni
     10 rotoli** (laboratorio art. 59); registro **10 anni**. Questi controlli si applicano solo ai prodotti
     **privi di marcatura CE**.

4. **Procedure di qualificazione (§11.8.4)**
   - **Qualificazione dello stabilimento** presso il **Servizio Tecnico Centrale (STC)** (art. 58 DPR 380), per
     ciascuna unità produttiva.
   - **Serie dichiarata** (§4.1.10.2.1): domanda allo STC → **attestato con validità quinquennale**, rinnovabile.
   - **Serie controllata** (§4.1.10.2.2): oltre alla documentazione della serie dichiarata, **prove a rottura su
     prototipo** e relazione interpretativa → **Certificato di Valutazione Tecnica** (STC, sentito il CSLP), con
     **validità quinquennale** rinnovabile; possibili sospensioni/revoche.

5. **Output**: scheda con metodo di dichiarazione, requisiti di stabilimento, piano di controllo di produzione
   (cls/acciaio con frequenze e conservazione dei registri) e percorso di qualificazione (serie dichiarata vs
   controllata). Segnala che il **progetto/verifiche** (§4.1.10) restano fuori scope.

## Cosa NON fare

- Non calcolare le **verifiche** degli elementi né dimensionarli (§4.1.10, → skill `costruzioni-calcestruzzo-ntc`).
- Non applicare i controlli §11.8.3 ai prodotti **con marcatura CE** (per i quali valgono le regole della CE).
- Non trattare i **controlli di accettazione generali** di cls/acciaio (§§11.2/11.3, → skill dedicata) né la
  **denuncia/collaudo statico** (DPR 380, → skill dedicata).
- Non inventare valori: ogni frequenza/soglia deve essere rintracciabile in
  `../references/fonti/ntc2018-par-11-8.md`.
