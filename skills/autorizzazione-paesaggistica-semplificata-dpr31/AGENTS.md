# AGENTS.md - autorizzazione-paesaggistica-semplificata-dpr31

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **qualificazione di un intervento in area a vincolo paesaggistico**
rispetto all'**autorizzazione paesaggistica**: **escluso** (Allegato A), **semplificato**
(interventi di lieve entita', Allegato B) o **ordinario** (art. 146 del Codice), secondo il
**D.P.R. 13 febbraio 2017, n. 31**. Target: ingegneri, architetti, geometri, operatori SUE/SUAP.

**E' una skill documentale**: inquadra i tre regimi, le condizioni/limiti delle voci e il
procedimento semplificato; **non riproduce la classificazione puntuale** di ogni intervento,
non rilascia l'autorizzazione ne' redige la relazione paesaggistica.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Complementare a `modulistica-edilizia-unificata` e
`regimi-suap-attivita-produttive-dlgs222` (titolo edilizio / regimi SUAP): questa copre il
profilo **paesaggistico** (autorizzazione ex Codice dei beni culturali).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-31-2017**: D.P.R. 13 febbraio 2017, n. 31, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `e71de17b...`; codice 17G00042). Articoli e Allegati caricati via
  `caricaArticolo` e trascritti verbatim: art. 2 (Allegato A), art. 3 (Allegato B), art. 4
  (esonero), art. 7 (rinnovo), art. 9 (presentazione istanza), art. 11 (semplificazioni);
  Allegato A (A.1-A.31) e Allegato B (B.1-B.42) per intero.

Trascrizione in `references/fonti/dpr-31-2017.md`; estratto operativo in
`references/estratti/autorizzazione-paesaggistica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 2 -> Allegato A** (A.1-A.31): interventi **esclusi** (condizionati al rispetto delle
  caratteristiche esistenti e ai limiti dell'art. 136 c. 1 lett. a/b/c del Codice).
- **Art. 3 -> Allegato B** (B.1-B.42): interventi di **lieve entita'** -> **semplificato** (Capo II).
- **Art. 146 del Codice**: procedimento **ordinario** (residuale).
- **Art. 4**: **esonero** dove il vincolo/piano ha prescrizioni d'uso (voci A.2 ultimo periodo,
  A.5, A.7, A.13, A.14 e B.6, B.13, B.26, B.36).
- **Art. 9**: istanza a **SUE** (edilizia) / **SUAP** (DPR 160/2010) / amministrazione procedente.
- **Art. 11**: verifica preliminare (escluso/ordinario/semplificato) + **conferenza di servizi**
  con **termini dimezzati**.
- **Art. 7**: **rinnovo** semplificato (autorizzazione scaduta <= 1 anno, interventi non eseguiti).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre la classificazione puntuale** di ogni intervento: rinviare alle voci degli
  Allegati A e B e ai richiami all'art. 136 del Codice.
- Non **rilasciare l'autorizzazione** ne' redigere la relazione paesaggistica.
- Non trattare il **titolo edilizio** (DPR 380/2001 / D.Lgs. 222/2016) ne' l'accertamento di
  compatibilita' ex art. 167 del Codice.

### Cosa fare
- Qualificare l'intervento (escluso/semplificato/ordinario) con condizioni/limiti ed esonero;
  impostare il procedimento semplificato (istanza, relazione, verifica preliminare, conferenza).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 31/2017 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere artt. 2/3/4/7/9/11 e gli Allegati A e B, verificando eventuali modifiche (es. DPR
73/2026 che ha modificato il DPR 31/2017).

## Validatori

- Non ancora assegnato (Livello 2 con esperto di tutela paesaggistica / funzionario soprintendenza).

## Stato attuale

- Versione: 0.1.0-alpha (closes #249)
- Task files: 2 (`qualifica-intervento-paesaggistico.md`, `imposta-procedimento-semplificato.md`)
- Esempi: 2 (pannelli fotovoltaici esclusi A.6; ampliamento di lieve entita' B.1)
