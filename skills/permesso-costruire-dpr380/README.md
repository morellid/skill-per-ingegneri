# permesso-costruire-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico SUE / esperto di diritto urbanistico da completare)

Skill di **supporto documentale** al regime del **permesso di costruire**:
caratteristiche del titolo, presupposti per il rilascio, efficacia temporale e
decadenza, procedimento e termini, secondo il **D.P.R. 380/2001 (Testo unico
edilizia), artt. 11, 12, 15, 20**.

**Non redige** la domanda né l'asseverazione, **non decide** se un intervento
richieda il PdC anziché SCIA/CILA (rinvio a `modulistica-edilizia-unificata`), **non
calcola** il contributo di costruzione e **non sostituisce** il SUE, il progettista o
il Comune: inquadra presupposti, procedimento ed efficacia.

## Target

Ingegneri e architetti (progettisti, tecnici comunali/SUE) e richiedenti del titolo.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-presupposti-caratteristiche` | Verifica i presupposti per il rilascio (conformità urbanistica, urbanizzazioni, salvaguardia; art. 12) e le caratteristiche del titolo (art. 11) |
| `verifica-procedimento-termini-decadenza` | Ricostruisce il procedimento e i termini (art. 20: 60/30 giorni, silenzio-assenso) e l'efficacia temporale/decadenza (art. 15) |

Nucleo: **caratteristiche** del titolo (art. 11); **presupposti** (art. 12);
**efficacia e decadenza** - inizio 1 anno / fine 3 anni (art. 15); **procedimento**,
termini e **silenzio-assenso** (art. 20).

## Fonti consultate

- **D.P.R. 6/6/2001 n. 380** (Testo unico edilizia) - artt. 11, 12, 15, 20 - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non decide** il **titolo** edilizio (PdC vs SCIA/CILA/edilizia libera - art. 10):
  rinvio a `modulistica-edilizia-unificata`.
- **Non redige** la domanda, gli elaborati o l'**asseverazione** del progettista.
- **Non calcola** il **contributo di costruzione** (art. 16); non tratta agibilità
  (art. 24) né vigilanza/sanzioni (artt. 27 ss.).
- **Non sostituisce** il progettista, il SUE o il Comune, né le leggi regionali di
  semplificazione.

**La skill è un supporto documentale: non sostituisce il progettista, lo sportello
unico per l'edilizia (SUE) né il Comune, né la lettura degli artt. 11/12/15/20 del
D.P.R. 380/2001.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
