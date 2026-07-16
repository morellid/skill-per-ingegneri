# autorizzazione-paesaggistica-semplificata-dpr31

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di tutela paesaggistica / soprintendenza da completare)

Skill di **supporto documentale** alla **qualificazione di un intervento** su un immobile o
un'area sottoposta a **vincolo paesaggistico** rispetto all'**autorizzazione paesaggistica**:
**escluso** (Allegato A), **semplificato** per interventi di **lieve entità** (Allegato B) o
**ordinario** (art. 146 del Codice), secondo il **D.P.R. 13 febbraio 2017, n. 31**.

**Non riproduce la classificazione puntuale** di ogni intervento, **non rilascia
l'autorizzazione** e **non redige la relazione paesaggistica**: inquadra i tre regimi, le
condizioni/limiti delle voci e il procedimento.

## Target

Ingegneri, architetti, geometri e operatori del **SUE/SUAP** che devono qualificare un
intervento in area vincolata prima della presentazione dell'istanza.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `qualifica-intervento-paesaggistico` | Stabilisce se l'intervento è escluso (Allegato A), semplificato (Allegato B) o ordinario (art. 146 Codice), con condizioni e limiti |
| `imposta-procedimento-semplificato` | Imposta il procedimento semplificato (istanza a SUE/SUAP, relazione semplificata, verifica preliminare, conferenza di servizi) e il rinnovo |

Nucleo: tre regimi (**escluso** art. 2 + Allegato A voci A.1-A.31; **semplificato** art. 3 +
Allegato B voci B.1-B.42; **ordinario** art. 146 Codice), **esonero** (art. 4),
**presentazione** dell'istanza (art. 9 SUE/SUAP), **semplificazioni** procedimentali (art. 11:
verifica preliminare + conferenza di servizi con termini dimezzati), **rinnovo** (art. 7).

## Fonti consultate

- **D.P.R. 13 febbraio 2017, n. 31** - artt. 2, 3, 4, 7, 9, 11 e Allegati A e B - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-16`, codice 17G00042)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce la classificazione puntuale** di ogni intervento: la qualificazione esatta
  va letta sulle voci degli Allegati A e B dell'atto (con i richiami all'art. 136 del Codice).
- **Non rilascia l'autorizzazione** né redige la relazione paesaggistica.
- **Non tratta il titolo edilizio** (DPR 380/2001 / D.Lgs. 222/2016 → `modulistica-edilizia-unificata`,
  `regimi-suap-attivita-produttive-dlgs222`) né l'accertamento di compatibilità ex art. 167 del Codice.

**La skill è un supporto documentale: non sostituisce l'amministrazione procedente, il
soprintendente né la lettura degli Allegati A e B del D.P.R. 31/2017 e del Codice.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
