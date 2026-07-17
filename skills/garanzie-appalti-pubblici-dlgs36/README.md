# garanzie-appalti-pubblici-dlgs36

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di contratti pubblici / RUP da completare)

Skill di **supporto documentale** all'inquadramento delle **garanzie** negli appalti
pubblici: **garanzia provvisoria** per la partecipazione alla procedura e **garanzia
definitiva** con le relative coperture assicurative, secondo il **D.Lgs. 36/2023
(Codice dei contratti pubblici), artt. 106 e 117**.

**Non calcola** gli importi del caso concreto, **non redige** le fideiussioni/polizze
ne' gli schemi tipo (DM) e **non sostituisce** la stazione appaltante, il RUP, il
garante o l'operatore economico: inquadra tipi, importi, riduzioni, svincoli e
coperture.

## Target

Ingegneri/architetti e tecnici che operano come RUP, progettisti, direttori dei
lavori o come operatori economici in gare e contratti pubblici.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-garanzia-provvisoria` | Importo (2%, modulazione 1%-4%), forma, requisiti, riduzioni cumulabili e svincolo della garanzia provvisoria (art. 106) |
| `inquadra-garanzia-definitiva` | Importo (10%), maggiorazione per ribasso, oggetto/durata, svincolo progressivo (80%), sostituzione e coperture assicurative (art. 117) |

Nucleo: **garanzia provvisoria** (art. 106 - 2%, riduzioni, svincolo automatico);
**garanzia definitiva** (art. 117 - 10%, maggiorazione per ribasso, svincolo
progressivo, polizze CAR/RCT/decennale, schemi tipo).

## Fonti consultate

- **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - artt. 106, 117 -
  testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 23G00044)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** gli importi del caso concreto (valore procedura, importo
  contrattuale, maggiorazione da ribasso, massimali).
- **Non redige** le fideiussioni/cauzioni/polizze ne' gli **schemi tipo** (DM ex
  art. 117 c. 12).
- **Non valuta** escussione/decadenza/contenzioso ne' fornisce consulenza legale o
  assicurativa; non tratta le altre garanzie di sistema salvo i richiami degli artt.
  106 e 117.
- **Non sostituisce** la stazione appaltante, il RUP, il garante o l'operatore
  economico.

**La skill è un supporto documentale: non sostituisce la stazione appaltante, il RUP,
il garante né l'operatore economico, né la lettura degli artt. 106 e 117 del D.Lgs.
36/2023.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
