# AGENTS.md - controlli-accettazione-cls-acciaio-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **Direttore dei Lavori** e al **collaudatore** per l'**inquadramento dei controlli di
accettazione in cantiere** del **calcestruzzo** (§11.2.4-11.2.5) e dell'**acciaio da cemento armato**
(§11.3.2.12) secondo le **NTC 2018** (DM 17 gennaio 2018), **Capitolo 11**: prelievo, numero minimo di
prelievi/campioni, criteri di accettazione e non conformità. Target: direttori dei lavori, collaudatori,
tecnici di cantiere.

**E' una skill documentale per il tecnico**: fornisce le modalità di prelievo, i criteri della Tab. 11.2.I
(cls) e della Tab. 11.3.VII (acciaio) e le procedure; **non esegue** le prove e **non valuta** la resistenza
(compito del laboratorio ex art. 59 DPR 380/2001), **non sostituisce** il Direttore dei Lavori.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre il compito di **cantiere/collaudo** che le skill "costruzioni di X"
(`costruzioni-calcestruzzo-ntc` §4.1, `costruzioni-acciaio-ntc` §4.2) rinviano esplicitamente al **§11** come
fuori scope. Si affianca alle altre skill NTC condividendone la fonte (PDF GU del S.O. n. 8 alla G.U. n.
42/2018). Restano fuori scope i controlli in stabilimento/qualificazione (§11.3.2.10-11), i carotaggi e la
resistenza in opera (§11.2.6-11.2.7), gli aggregati, l'acciaio da carpenteria (§11.3.4), il legno (§11.7) e la
muratura (§11.10).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-cap-11-controlli**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill
  NTC). Par. 11.2 e 11.3 estratti con `pdftotext -layout` (pp. 307-309 e 326-327) e trascritti verbatim.

Trascrizione in `references/fonti/ntc2018-cap-11-controlli.md`; estratto operativo in
`references/estratti/controlli-accettazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Prelievo cls** (§11.2.4): 2 provini, resistenza di prelievo = media; scarto tra i due > 20% del minore →
  non accettato.
- **Tipo A** (§11.2.5.1): ≤ 300 m³, 3 prelievi (≤ 100 m³), ≥ 1/giorno. **Tipo B** (§11.2.5.2): > 1500 m³, ≥ 1
  controllo/1500 m³, ≥ 15 prelievi, coeff. variazione ≤ 0,3.
- **Tab. 11.2.I**: A → Rcm28 ≥ Rck + 3,5 e Rc,min ≥ Rck − 3,5; B → Rcm28 ≥ Rck + 1,48·s e Rc,min ≥ Rck − 3,5.
- **Acciaio** (§11.3.2.12): entro 30 gg, laboratorio art. 59 DPR 380; 3 campioni ogni 30 t (stessa
  classe/stabilimento).
- **Tab. 11.3.VII a/b**: fy 425-572 N/mm²; Agt ≥ 6,0% (B450C) / ≥ 2,0% (B450A); ft/fy 1,13-1,37 (B450C) / ≥
  1,03 (B450A); piegamento senza cricche; non conformità 6 → 25 campioni.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le prove né **valutare** la resistenza (spettano al laboratorio ex art. 59 DPR 380/2001);
  non **dichiarare** idoneità/conformità al posto del laboratorio/Direttore dei Lavori.
- Non **coprire** i controlli in stabilimento/qualificazione (§11.3.2.10-11), i carotaggi/resistenza in opera
  (§11.2.6-11.2.7), gli aggregati, l'acciaio da carpenteria (§11.3.4), il legno (§11.7) né la muratura
  (§11.10).

### Cosa fare
- Fornire modalità di prelievo, numero minimo di prelievi/campioni, criteri di accettazione (Tab. 11.2.I /
  11.3.VII) e procedure di non conformità, sempre con rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il Cap. 11. Verificare i criteri (Tab. 11.2.I: +3,5 / +1,48·s / −3,5), i volumi (300
/ 1500 m³) e i valori dell'acciaio (Tab. 11.3.VII: 425/572 N/mm², Agt, ft/fy, 3 campioni/30 t).

## Validatori

- Non ancora assegnato (Livello 2 con Direttore dei Lavori/collaudatore).

## Stato attuale

- Versione: 0.1.0-alpha (closes #396)
- Task files: 2 (`inquadra-controllo-accettazione-calcestruzzo.md`, `inquadra-accettazione-acciaio-ca.md`)
- Esempi: 2 (controllo tipo A per 250 m³ di C25/30; accettazione di 80 t di barre B450C)
