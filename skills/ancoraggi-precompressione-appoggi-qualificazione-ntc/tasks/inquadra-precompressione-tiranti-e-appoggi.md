# Task — Inquadra precompressione, tiranti geotecnici e appoggi (NTC 2018 §11.5-11.6)

Supporto documentale per individuare la **via di qualificazione** e i **compiti del Direttore dei Lavori** per i
**sistemi di precompressione a cavi post-tesi** e i **tiranti di ancoraggio per uso geotecnico** (§11.5) e per gli
**appoggi strutturali** (§11.6) secondo le NTC 2018 (DM 17/1/2018). **Non** esegue il progetto né le verifiche.

Fonte: `../references/fonti/ntc2018-par-11-4-11-6.md`; checklist: `../references/estratti/ancoraggi-appoggi-checklist.md`.

## Input tipico

- Prodotto/sistema: **sistema di precompressione a cavi post-tesi**, **tirante di ancoraggio geotecnico** (attivo/
  passivo) o **appoggio strutturale** (da ponte o edificio).
- Documentazione del fabbricante (Certificato di valutazione tecnica, ETA/marcatura CE, manuale di posa).

## Passi

1. **Sistemi di precompressione a cavi post-tesi (§11.5.1)**
   - Si applica il **punto C) del §11.1**; qualificazione mediante **Certificato di valutazione tecnica** (Linea
     Guida del Consiglio Superiore dei Lavori Pubblici).
   - Ogni fornitura è accompagnata da **copia del CVT** oppure da **documentazione di marcatura CE su ETA**, più il
     **manuale** di posa in opera e manutenzione.
   - Il **Direttore dei Lavori** verifica la documentazione, **rifiuta le forniture prive** di qualificazione,
     verifica la **conformità della posa** ed effettua **prove di accettazione**: in ogni caso **verifica geometrica
     e delle tolleranze dimensionali** + valutazione delle **principali caratteristiche meccaniche**/prestazioni del
     sistema. Le **modalità di esecuzione** delle prove sono nella **Linea Guida ETAG 013**.

2. **Tiranti di ancoraggio per uso geotecnico (§11.5.2)**
   - Tiranti **attivi e passivi**: si applica il **punto C) del §11.1**.
   - Per i **tipo attivo**: qualificazione mediante **Certificazione di valutazione Tecnica** (Linea Guida CSLP).
   - Fornitura con **CVT** o **CE su ETA** + **manuale**; il DL verifica, rifiuta i non conformi ed effettua le prove
     di accettazione (verifica geometrica/tolleranze + caratteristiche meccaniche).
   - **Nota**: il **progetto/verifiche geotecniche** dei tiranti (aderenza, sfilamento, stati limite) è al **§6.6**
     (skill `tiranti-ancoraggio-ntc`), fuori scope.

3. **Appoggi strutturali (§11.6)**
   - Dispositivi di vincolo per **trasmettere carichi** e **vincolare gradi di libertà** in strutture/ponti/edifici.
   - Si applica il **punto A del §11.1** → **conformi alla serie UNI EN 1337** + **Marcatura CE**, con **Sistema di
     Valutazione e Verifica della Costanza della Prestazione 1 (VVCP 1)** per le applicazioni critiche.
   - Se **non ricadenti (o non completamente)** nella serie UNI EN 1337 → **caso C) del §11.1**.
   - **Nota**: gli **appoggi ordinari** (UNI EN 1337) sono distinti dai **dispositivi antisismici** (UNI EN 15129,
     §11.9, skill dedicata).

4. **Output**: scheda con la via di qualificazione per ciascun prodotto (punto A/C del §11.1, CVT/ETA/UNI EN 1337) e i
   compiti del Direttore dei Lavori (documentazione, rifiuto forniture prive, prove di accettazione).

## Cosa NON fare

- Non **progettare/verificare** i prodotti (progetto dei cavi post-tesi, verifiche geotecniche dei tiranti §6.6,
  progetto degli appoggi).
- Non **riprodurre** le procedure delle Linee guida/norme europee (ETAG 013, UNI EN 1337): sono la fonte per i
  dettagli.
- Non confondere gli **appoggi ordinari** (§11.6, UNI EN 1337) con i **dispositivi antisismici** (§11.9, UNI EN 15129).
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-11-4-11-6.md`.
