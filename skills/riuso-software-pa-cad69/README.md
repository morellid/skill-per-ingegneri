# riuso-software-pa-cad69

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RTD/esperto open source PA da completare)

Skill di **supporto documentale** agli obblighi di **acquisizione, riuso e rilascio in
open source** del software delle pubbliche amministrazioni (**C.A.D. artt. 68-69**), con
la **documentazione a corredo** richiesta dalle **Linee guida AgID** (README,
documentazione tecnica, `publiccode.yml`, tempi, registrazione su Developers Italia).

**Non sceglie la licenza**, **non compila campo-per-campo il publiccode.yml** e **non
esegue la valutazione comparativa tecnica**: inquadra obblighi e contenuti.

## Target

PA e loro fornitori (RTD, uffici IT) che devono adempiere agli obblighi di riuso/rilascio
open source del software.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `imposta-analisi-comparativa` | Imposta la valutazione comparativa tecnico-economica tra le soluzioni dell'art. 68 (sviluppo ad hoc, riuso, open source, cloud, proprietario) |
| `prepara-rilascio-open-source` | Struttura il rilascio ex art. 69: licenza aperta, README, documentazione (formati ammessi), tempi (15 gg), registrazione su Developers Italia via publiccode.yml |

Nucleo: **analisi comparativa** (art. 68), **obbligo di rilascio** del codice sorgente
sotto licenza aperta (art. 69), **README** (A.7), **documentazione** in formato
versionabile (A.8), **tempi** 15 gg (A.9), **`publiccode.yml`** e registrazione su
Developers Italia (A.11).

## Fonti consultate

- **D.Lgs. 82/2005 (C.A.D.)** artt. 68-69 - testo vigente su Normattiva (indice pinnato a
  `!vig=`)
- **AgID - Linee guida su acquisizione e riuso di software per le PA** - PDF ufficiale su
  agid.gov.it (Allegato A)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non sceglie la licenza** aperta né la valida legalmente.
- **Non riproduce il formato campo-per-campo del `publiccode.yml`** (standard Developers
  Italia): rinvia alla documentazione ufficiale del formato.
- **Non esegue la valutazione comparativa tecnica** né redige codice/documentazione.
- È complementare a `specifiche-tecniche-ict-appalti-dlgs36` (lato gara/acquisizione,
  art. 79 D.Lgs 36/2023 + CAD art. 68): questa copre il lato riuso/rilascio (art. 69).

**La skill e' un supporto documentale: non sostituisce il RTD, il consulente legale ne'
la lettura delle Linee guida AgID e della documentazione del formato publiccode.yml.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
