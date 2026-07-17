# accessi-passi-carrabili-cds

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di polizia stradale / ente proprietario della strada da completare)

Skill di **supporto documentale** all'inquadramento di **accessi, diramazioni e passi carrabili**
dalla strada ai fondi e fabbricati laterali, secondo l'**art. 22 del Codice della Strada (D.Lgs.
30 aprile 1992, n. 285)**: preventiva autorizzazione dell'ente proprietario, regolarizzazione,
divieti e trasformazioni, opere e parcheggi, condizioni tecniche e sanzioni.

**Non rilascia l'autorizzazione**, **non redige** l'istanza né il progetto dell'accesso e **non
sostituisce** l'ente proprietario/gestore della strada: inquadra il regime autorizzatorio.

## Target

Ingegneri, geometri, proprietari e operatori che devono aprire, trasformare o regolarizzare un
accesso, una diramazione o un passo carrabile su una strada pubblica.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-autorizzazione-accesso` | Stabilisce se serve l'autorizzazione dell'ente proprietario e con quali obblighi (opere, parcheggi, opere particolari) per un nuovo accesso/diramazione o passo carrabile (commi 1-10) |
| `verifica-divieti-sanzioni` | Verifica i divieti (rampe, corsie di accelerazione/decelerazione) e inquadra le sanzioni per accessi non autorizzati o abusivi (commi 4, 10-12) |

Nucleo: **preventiva autorizzazione** dell'ente proprietario (c. 1), **passi carrabili** con segnale
(c. 3), **regolarizzazione** (c. 2), **opere sui fossi** (c. 6), **parcheggi** per insediamenti (c.
8), **opere particolari e consorzi** (c. 9), **divieti** su rampe/corsie e **caratteristiche
tecniche** (c. 10), **sanzioni** (cc. 11-12).

## Fonti consultate

- **D.Lgs. 30 aprile 1992, n. 285** (Codice della Strada) - art. 22 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-17`, codice 092G0306)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non rilascia l'autorizzazione**/concessione né esprime il diniego (competono all'ente
  proprietario/gestore).
- **Non redige** l'istanza, il progetto dell'accesso/passo carrabile né calcola le opere.
- **Non riproduce** il Regolamento di esecuzione (DPR 495/1992, artt. 44-46) né i decreti MIT sulle
  caratteristiche tecniche; non tratta il titolo edilizio/SUE né il canone.

**La skill è un supporto documentale: non sostituisce l'ente proprietario/gestore della strada né la
lettura dell'art. 22 del Codice della Strada e del Regolamento di esecuzione.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
