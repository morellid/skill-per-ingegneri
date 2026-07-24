# AGENTS.md - componenti-prefabbricati-ca-cap-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale**, al **Direttore dei Lavori** e ai **produttori** per la
**qualificazione**, il **controllo di produzione** e l'**accettazione** dei componenti prefabbricati in c.a. e
c.a.p. secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.8** (Cap. 11 «Materiali e prodotti per uso
strutturale»): generalità e metodi di dichiarazione (§11.8.1), requisiti degli stabilimenti (§11.8.2), controllo
di produzione e sui materiali di serie e marchiatura (§11.8.3), procedure di qualificazione serie dichiarata/
controllata (§11.8.4), documenti di accompagnamento e accettazione (§11.8.5), dispositivi di collegamento (§11.8.6).

**È una skill documentale per il tecnico**: inquadra qualificazione, controllo e accettazione; **non** esegue il
progetto degli elementi prefabbricati né le verifiche (§4.1.10).

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre la **qualificazione/controllo di produzione/accettazione dei componenti
prefabbricati** (§11.8, Cap. 11). È **distinta** da `costruzioni-calcestruzzo-ntc` (§4.1, **progetto/verifiche**),
da `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3, accettazione **generale** di cls/acciaio in cantiere) e
da `denuncia-collaudo-statico-ca-dpr380` (DPR 380, denuncia/collaudo): il §11.8 è il paragrafo specifico per i
prefabbricati (produzione in stabilimento, serie dichiarata/controllata, marchiatura, certificato d'origine).
Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope
il progetto (§4.1.10) e i controlli di accettazione generali di cls/acciaio (§§11.2/11.3).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-11-8**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 11.8 (pagine GU 351-353 = pagine PDF 355-357) estratto con `pdftotext -layout` e verificato sull'immagine
  (`pdftoppm -r 150 -png`) delle pagine PDF 356/357 per le frequenze delle prove, i registri, la marchiatura e le
  validità quinquennali.

Trascrizione in `references/fonti/ntc2018-par-11-8.md`; estratto operativo in
`references/estratti/prefabbricati-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§11.8.1**: processo industrializzato + sistema permanente di controllo della produzione in stabilimento; per
  elementi qualificati ai **punti A/C del §11.1** i requisiti procedurali del **deposito art. 58 DPR 380/2001** si
  considerano assolti; **Metodi 1/2/3** di dichiarazione delle prestazioni; materiali base qualificati (§11.1).
- **§11.8.3**: sistema qualità **UNI EN ISO 9001**. **Cls**: controllo continuo (§11.2), apparecchiature **tarate
  annualmente**, registri **10 anni**, prove a **28 giorni**, resistenza caratteristica **controllo tipo B**
  (§11.2.5), controlli esterni **≥ 1 prelievo/5 giorni** con **controllo tipo A** su **3 prelievi**. **Acciaio**:
  **piegatura 3 campioni/90 t** (min mensile, UNI EN ISO 15630-1), **trazione 3 campioni/10 rotoli**; solo per
  prodotti **privi di marcatura CE**.
- **§11.8.3.4**: **marchiatura fissa/indelebile** per la rintracciabilità; per manufatti **> 8 kN** indicare anche
  il **peso**.
- **§11.8.4**: **STC** (art. 58 DPR 380); **serie dichiarata** (§4.1.10.2.1) → **attestato quinquennale**; **serie
  controllata** (§4.1.10.2.2) → **Certificato di Valutazione Tecnica quinquennale** + prove a rottura su prototipo.
- **§11.8.5**: il **Direttore dei Lavori** rifiuta le forniture non conformi; istruzioni trasporto/montaggio,
  disegni d'assieme, **certificato d'origine**, prove a compressione, verifica della marchiatura (art. 65 DPR 380).

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** il **progetto** degli elementi prefabbricati né le **verifiche** (§4.1.10).
- Non trattare i **controlli di accettazione generali** di cls/acciaio (§§11.2/11.3) né la **denuncia/collaudo
  statico** (DPR 380): rinvia alle skill dedicate.
- Non inventare valori: ogni frequenza/soglia deve essere rintracciabile in `references/fonti/ntc2018-par-11-8.md`.

### Cosa fare
- Fornire i metodi di dichiarazione, i requisiti di stabilimento e controllo di produzione (cls/acciaio), le regole
  di marchiatura, le procedure di qualificazione (serie dichiarata/controllata) e i documenti di accompagnamento/
  accettazione, sempre con rinvio al sotto-paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e riestrarre
il par. 11.8. Verificare sull'immagine i valori (28 giorni; tarature annuali; registri 10 anni; 1 prelievo/5
giorni; piegatura 3/90 t e min mensile; trazione 3/10 rotoli; marchiatura > 8 kN; validità quinquennali).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista / Direttore tecnico di stabilimento di prefabbricati).

## Stato attuale

- Versione: 0.1.0-alpha (closes #468)
- Task files: 2 (`inquadra-qualificazione-e-controllo-produzione.md`, `verifica-marchiatura-e-documenti-accettazione.md`)
- Esempi: 2 (qualificazione di una serie in stabilimento; accettazione in cantiere di una fornitura di elementi
  prefabbricati con verifica marchiatura e certificato d'origine)
