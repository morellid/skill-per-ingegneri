# vigilanza-sanzioni-abusi-edilizi-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico/ufficio abusi o legale amministrativista da completare)

Skill di **supporto documentale** al **regime repressivo degli abusi edilizi**: vigilanza, sospensione
dei lavori, ordine di demolizione e acquisizione gratuita, ristrutturazione abusiva, parziale
difformità e sanzioni penali, secondo il **D.P.R. 6 giugno 2001, n. 380** (T.U. Edilizia), Titolo IV,
artt. 27, 31, 33, 34, 44.

**Non adotta** i provvedimenti, **non quantifica** le sanzioni, **non tratta** la sanatoria (artt.
36/36-bis) e **non sostituisce** il Comune/SUE, il tecnico o il legale: inquadra il regime e i termini.

## Target

Ingegneri, tecnici e operatori SUE coinvolti in questioni di abusi edilizi.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-abuso-misura` | Classifica l'abuso (assenza/totale difformità - art. 31; ristrutturazione - art. 33; parziale difformità - art. 34) e individua la misura |
| `ricostruisci-vigilanza-termini` | Ricostruisce la sequenza di vigilanza/sospensione (art. 27) e i termini e le sanzioni |

Nucleo: **vigilanza** (art. 27); **assenza/totale difformità** con demolizione e **acquisizione
gratuita** (art. 31); **ristrutturazione abusiva** (art. 33); **parziale difformità** (art. 34);
**sanzioni penali** (art. 44).

## Fonti consultate

- **D.P.R. 6 giugno 2001, n. 380** (Titolo IV) - artt. 27, 31, 33, 34, 44 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-17`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non adotta** i provvedimenti (ordinanze/ingiunzioni) né esegue notifiche/acquisizioni.
- **Non quantifica** le sanzioni (doppio/triplo del valore, importi) né determina il valore venale.
- **Non tratta** la **sanatoria** (artt. 36/36-bis) né le **tolleranze** (art. 34-bis): rinvio a
  `modulistica-edilizia-unificata` (Salva Casa).
- **Non sostituisce** il Comune/SUE, il tecnico o il legale.

**La skill è un supporto documentale: non sostituisce il Comune/SUE, il tecnico né il legale, né la
lettura del Titolo IV del D.P.R. 380/2001 e della disciplina regionale.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
