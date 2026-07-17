# attrezzature-pressione-esercizio-dm329

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico della sicurezza / verificatore INAIL-ASL da completare)

Skill di **supporto documentale** alla **messa in servizio** e alle **verifiche** delle
**attrezzature e insiemi a pressione in esercizio** (fase post-marcatura CE): campo di applicazione,
verifica di primo impianto, esclusioni, dichiarazione di messa in servizio, riqualificazione
periodica, esenzioni e verifica di funzionamento, secondo il **D.M. 1 dicembre 2004, n. 329** (artt.
1, 4, 5, 6, 10, 11, 13).

**Non esegue** le verifiche, **non redige** la dichiarazione di messa in servizio e **non
sostituisce** l'utilizzatore/datore di lavoro, il soggetto verificatore (INAIL/ASL/soggetti
abilitati) né il fabbricante: inquadra il metodo documentale.

## Target

Ingegneri, datori di lavoro/utilizzatori e tecnici della sicurezza che devono impostare la messa in
servizio o la riqualificazione periodica di attrezzature a pressione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `imposta-messa-in-servizio` | Verifica se è dovuta la verifica di messa in servizio (art. 4/5) e compone i contenuti della dichiarazione di messa in servizio (art. 6) |
| `imposta-riqualificazione-periodica` | Inquadra la riqualificazione periodica (integrità + funzionamento), la periodicità (allegati A/B) e le esenzioni (art. 11) |

Nucleo: **ambito e verifiche** (art. 1); **verifica di primo impianto/messa in servizio** (art. 4)
ed **esclusioni** (art. 5); **dichiarazione di messa in servizio** a INAIL/ASL (art. 6);
**riqualificazione periodica** (art. 10) ed **esenzioni** (art. 11); **verifica di funzionamento**
(art. 13).

## Fonti consultate

- **D.M. 1 dicembre 2004, n. 329** - artt. 1, 4, 5, 6, 10, 11, 13 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-16`, codice 005G0017)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** le verifiche (primo impianto, riqualificazione, funzionamento) né rilascia
  attestazioni/verbali: le eseguono **INAIL/ASL** o i **soggetti abilitati**.
- **Non redige** la dichiarazione di messa in servizio né la relazione tecnica di impianto.
- **Non riproduce** le tabelle di periodicità (**allegati A e B**) né gli articoli non trascritti
  (artt. 2, 3, 12): rinvio all'atto e al manuale d'uso del fabbricante.
- **Distinta** dalla marcatura CE (D.Lgs. 93/2000 → `ped-classificazione-conformita`) e dalle
  verifiche periodiche ex art. 71 D.Lgs. 81/2008 (→ `verifiche-periodiche-attrezzature-dlgs81`).

**La skill è un supporto documentale: non sostituisce l'utilizzatore/datore di lavoro, il soggetto
verificatore né il fabbricante, né la lettura del D.M. 329/2004 e dei suoi allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
