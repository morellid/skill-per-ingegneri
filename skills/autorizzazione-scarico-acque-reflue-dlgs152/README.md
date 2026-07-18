# autorizzazione-scarico-acque-reflue-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ambientale / idraulico da completare)

Skill di **supporto documentale** al **tecnico ambientale/degli impianti** e al **titolare dello
scarico** per l'**autorizzazione allo scarico di acque reflue** e per la **domanda** di autorizzazione
degli **scarichi industriali**, ai sensi del **D.Lgs. 3 aprile 2006, n. 152 (Codice dell'ambiente),
Parte III, artt. 124 e 125**.

**Non redige** la domanda né **progetta** l'impianto di depurazione, **non applica** i valori limite di
emissione e **non sostituisce** il tecnico, il gestore del servizio idrico integrato o l'autorità
competente: inquadra obblighi, competenze, termini e contenuti.

## Target

Tecnici ambientali, progettisti di impianti di depurazione e titolari di scarichi che devono inquadrare
l'autorizzazione allo scarico e la domanda per gli scarichi industriali.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-autorizzazione-scarico` | Obbligo, titolare, regimi, competenza, termini, validità/rinnovo, prescrizioni e spese (art. 124) |
| `inquadra-domanda-scarico-industriale` | Contenuto della domanda per gli scarichi industriali e indicazioni per la Tabella 3/A (art. 125) |

Nucleo: **obbligo di autorizzazione preventiva** e titolare (art. 124 cc. 1-2), **competenza** e **90
giorni** (c. 7), **validità 4 anni** e **rinnovo** (c. 8), **prescrizioni/spese/modifiche** (cc. 9-12),
**contenuto della domanda** per gli scarichi industriali (art. 125).

## Fonti consultate

- **D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente) - Parte III, artt. 124-125 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 006G0171, idGruppo 25).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la domanda né **progetta** l'impianto di depurazione o lo scarico.
- **Non applica** i valori limite di emissione dell'Allegato 5 alla Parte III (Tab. 1/2/3/3-A/4).
- **Non tratta** l'AUA (DPR 59/2013) né l'AIA (skill `autorizzazione-integrata-ambientale-dlgs152`) come
  procedure, né le definizioni di scarico dell'art. 74, se non nei richiami.

**La skill è un supporto documentale: non sostituisce il tecnico, il gestore del servizio idrico
integrato o l'autorità competente, né la lettura degli artt. 124-125 del D.Lgs. 152/2006 e dell'Allegato
5.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
