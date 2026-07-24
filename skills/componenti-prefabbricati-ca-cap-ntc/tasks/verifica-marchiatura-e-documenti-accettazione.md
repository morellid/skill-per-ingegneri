# Task — Verifica la marchiatura e i documenti di accompagnamento in accettazione (NTC 2018 §11.8.3.4, §11.8.5)

Supporto documentale per impostare, dal lato del **Direttore dei Lavori**, la **verifica della marchiatura** degli
elementi prefabbricati e il controllo dei **documenti di accompagnamento** in fase di accettazione in cantiere
secondo le NTC 2018 (DM 17/1/2018), §11.8.3.4 e §11.8.5. **Non** esegue il progetto né le verifiche degli elementi.

Fonte: `../references/fonti/ntc2018-par-11-8.md`; checklist: `../references/estratti/prefabbricati-checklist.md`.

## Input tipico

- Fornitura in cantiere di elementi prefabbricati (di serie qualificata o occasionale).
- Documentazione trasmessa dal fabbricante (certificato d'origine, istruzioni di montaggio, attestato/CVT dello STC).

## Passi

1. **Verifica della marchiatura (§11.8.3.4)**
   - Ogni elemento di serie deve recare **marchiatura fissa, indelebile o non rimovibile** che garantisca la
     **rintracciabilità** del fabbricante/stabilimento e individui la **serie di origine**.
   - Per **manufatti di peso superiore a 8 kN**: deve essere indicato in modo **visibile**, almeno fino
     all'eventuale getto di completamento, anche il **peso** dell'elemento.

2. **Documenti di accompagnamento (§11.8.5)**
   - Verifica che ogni fornitura sia accompagnata dalle istruzioni su **trasporto e montaggio** (art. 58 DPR 380),
     da consegnare al Direttore dei Lavori, comprendenti almeno:
     a) **disegni d'assieme** con posizione/connessioni ed elenco degli elementi con contrassegni;
     b) relazione sui **materiali** per unioni/completamenti;
     c) istruzioni di **montaggio** (movimentazione, posa, regolazione);
     d) elaborati per **impiego e manutenzione** (da consegnare al Committente);
     e) per elementi di serie qualificati, **certificato di origine** firmato dal fabbricante e dal Direttore
        Tecnico (con nominativo del progettista e copia dell'**attestato STC**);
     f) documentazione delle **prove a compressione** in stabilimento e certificati del laboratorio art. 59.
   - Copia del **certificato d'origine** è allegata alla **relazione del Direttore dei Lavori** ex **art. 65 DPR
     380/2001**.

3. **Accettazione o rifiuto**
   - Il **Direttore dei Lavori** è tenuto a **rifiutare** le forniture non conformi. Prima dell'accettazione
     verifica che i manufatti siano **contrassegnati** come da §11.8.3.4.

4. **Output**: checklist di accettazione della fornitura (marchiatura presente e leggibile; peso indicato se
   > 8 kN; certificato d'origine e attestato STC; disegni d'assieme e istruzioni di montaggio; prove a
   compressione) con esito accettazione/rifiuto e note per la relazione ex art. 65.

## Cosa NON fare

- Non eseguire il **progetto/verifiche** degli elementi (§4.1.10, → skill `costruzioni-calcestruzzo-ntc`).
- Non confondere la marchiatura §11.8.3.4 con la **marcatura CE** dei prodotti da costruzione (Reg. UE 305/2011,
  → skill dedicata): sono piani distinti.
- Non trattare i **controlli di accettazione generali** di cls/acciaio (§§11.2/11.3, → skill dedicata) né la
  **denuncia/collaudo statico** (DPR 380, → skill dedicata).
- Non inventare valori/documenti: ogni requisito deve essere rintracciabile in
  `../references/fonti/ntc2018-par-11-8.md`.
