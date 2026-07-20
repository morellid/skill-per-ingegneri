# controlli-accettazione-cls-acciaio-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con Direttore dei Lavori/collaudatore da completare)

Skill di **supporto documentale** al **Direttore dei Lavori** e al **collaudatore** per l'**inquadramento dei
controlli di accettazione in cantiere** del **calcestruzzo** (§11.2.4-11.2.5) e dell'**acciaio da cemento
armato** (§11.3.2.12) secondo le **NTC 2018** (D.M. 17 gennaio 2018), **Capitolo 11**: modalità di prelievo,
numero minimo di prelievi/campioni, criteri di accettazione e gestione delle non conformità.

**Non esegue** le prove né **valuta** la resistenza (compito del **laboratorio ex art. 59 DPR 380/2001**) e
**non sostituisce** il Direttore dei Lavori: fornisce i criteri della Tab. 11.2.I (cls) e della Tab. 11.3.VII
(acciaio) e le relative procedure.

## Target

Direttori dei lavori, collaudatori e tecnici di cantiere che devono impostare o validare i controlli di
accettazione dei materiali strutturali secondo le NTC 2018 Cap. 11.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-controllo-accettazione-calcestruzzo` | Prelievo (§11.2.4), tipo A/B e criteri di accettazione (Tab. 11.2.I) del calcestruzzo (§11.2.5) |
| `inquadra-accettazione-acciaio-ca` | Numerosità (3 campioni/30 t), valori di accettazione (Tab. 11.3.VII a/b) e non conformità dell'acciaio da c.a. (§11.3.2.12) |

Nucleo: **prelievo** (2 provini, scarto ≤ 20%), **tipo A** (≤ 300 m³, 3 prelievi) / **tipo B** (> 1500 m³, ≥
15 prelievi), **criteri Tab. 11.2.I** (Rcm28 ≥ Rck+3,5 / Rck+1,48s; Rc,min ≥ Rck−3,5), **acciaio** (3
campioni/30 t, **Tab. 11.3.VII**: fy 425-572 N/mm², Agt, ft/fy) e **non conformità**.

## Relazione con altre skill

- **Copre** il compito di cantiere/collaudo che `costruzioni-calcestruzzo-ntc` (§4.1) e `costruzioni-acciaio-ntc`
  (§4.2) rinviano esplicitamente al **§11**. Condivide la fonte GU con le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **Cap. 11** (§11.2.4-11.2.5, §11.3.2.12) - testo del Supplemento
  Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto
  con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le prove né **valuta** la resistenza (compito del **laboratorio ex art. 59 DPR 380/2001**);
  **non sostituisce** il Direttore dei Lavori né il collaudatore.
- **Non copre** i controlli in stabilimento/qualificazione (§11.3.2.10-11), il controllo della resistenza in
  opera / carotaggi (§11.2.6-11.2.7), gli aggregati, l'acciaio da carpenteria (§11.3.4), il legno (§11.7) né
  la muratura (§11.10).

**La skill è un supporto documentale: non sostituisce il Direttore dei Lavori, il collaudatore o il laboratorio, né la lettura del Cap. 11 delle NTC 2018.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
