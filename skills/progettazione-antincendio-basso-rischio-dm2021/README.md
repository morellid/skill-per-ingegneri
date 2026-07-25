# progettazione-antincendio-basso-rischio-dm2021

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con professionista antincendio / RSPP abilitato da completare)

Skill di **supporto documentale** per la **progettazione, realizzazione ed esercizio della sicurezza antincendio nei
luoghi di lavoro** secondo il **D.M. 3 settembre 2021** (attuativo dell'**art. 46 c. 3 lett. a) punti 1 e 2 del D.Lgs
81/2008**), in vigore dal **29 ottobre 2022**: inquadramento della valutazione del rischio nel DVR, scelta del corpo di
regole applicabile (RTV / minicodice / Codice PI), verifica dei requisiti di basso rischio e strategia antincendio
minima.

**Non progetta** le misure al posto del tecnico, **non riproduce** il Codice di prevenzione incendi (D.M. 3/8/2015) né
le norme UNI citate e **non sostituisce** il professionista antincendio. È il **terzo** dei tre decreti antincendio del
settembre 2021, **distinto** da `piano-emergenza-antincendio-dm2021` (D.M. 2/9) e `controllo-manutenzione-antincendio-dm2021`
(D.M. 1/9).

## Target

RSPP, progettisti antincendio e datori di lavoro che devono inquadrare la valutazione del rischio di incendio e la
strategia antincendio di un luogo di lavoro, in particolare a basso rischio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-applicabilita-e-rischio` | Decide quale corpo di regole si applica (RTV / minicodice / Codice PI) verificando i requisiti di basso rischio, e inquadra la valutazione del rischio nel DVR (artt. 1-3) |
| `imposta-strategia-antincendio` | Imposta le misure minime dell'Allegato I (esodo, compartimentazione, controllo dell'incendio, GSA e le altre) con i parametri numerici verificati |

Nucleo: la valutazione del rischio è **parte del DVR** (art. 2); tre casi di applicabilità (art. 3: **RTV** /
**minicodice Allegato I** / **Codice PI D.M. 3/8/2015**); requisiti di **basso rischio** (affollamento ≤ 100, superficie
≤ 1000 m², quota -5/+24 m, no combustibili/sostanze/lavorazioni pericolose significative); **strategia antincendio** in
otto misure (compartimentazione, esodo, GSA, controllo dell'incendio, rivelazione e allarme, controllo fumi e calore,
operatività, impianti tecnologici).

## Relazione con altre skill

- Copre il **D.M. 3/9/2021** (progettazione). **Distinta** da `piano-emergenza-antincendio-dm2021` (D.M. 2/9/2021),
  `controllo-manutenzione-antincendio-dm2021` (D.M. 1/9/2021),
  `prevenzione-incendi-attivita-procedimenti-dpr151` (DPR 151/2011) e `carico-incendio-classe-resistenza-dm` (D.M.
  9/3/2007).

## Fonti consultate

- **D.M. 3 settembre 2021** — GU Serie Generale n. 259 del 29/10/2021, PDF ufficiale Gazzetta Ufficiale, SHA256
  `ed6c9c91...` (doppio download riproducibile), estratto con `pdftotext`; **costanti numeriche verificate a immagine**.
  Testo di legge liberamente riproducibile (art. 5 L. 633/1941).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non **progetta/dimensiona** le misure al posto del tecnico né firma elaborati.
- Non riproduce il **Codice di prevenzione incendi (D.M. 3/8/2015)**, richiamato per i luoghi non a basso rischio, né le
  **norme UNI** citate (UNI EN 1125, 1838, 1869, 10779, 12845, 9795, 11744): ne inquadra il rinvio.
- Non è la **gestione dell'emergenza** (D.M. 2/9/2021, → `piano-emergenza-antincendio-dm2021`) né il
  **controllo/manutenzione** dei sistemi (D.M. 1/9/2021, → `controllo-manutenzione-antincendio-dm2021`).

**La skill è un supporto documentale: non progetta le misure al posto del tecnico, non riproduce il Codice di prevenzione incendi (D.M. 3/8/2015) né le norme UNI citate e non sostituisce il professionista antincendio.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
