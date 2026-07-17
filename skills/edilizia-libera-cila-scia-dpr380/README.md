# edilizia-libera-cila-scia-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico abilitato/esperto edilizia da completare)

Skill di **supporto documentale** ai **regimi del titolo edilizio** diversi dal permesso
di costruire: **attività edilizia libera** (art. 6), **CILA** (art. 6-bis), **SCIA** (art.
22) e **SCIA in alternativa al permesso di costruire** (art. 23), secondo il **DPR
380/2001** (Testo unico edilizia), Titolo II.

**Non qualifica** in concreto l'intervento (art. 3), **non redige** la CILA/SCIA, **non
tratta** il permesso di costruire e **non sostituisce** il tecnico abilitato o il
SUE/Comune: inquadra il regime applicabile e gli adempimenti.

## Target

Tecnici, progettisti, cittadini, uffici SUE.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `scegli-titolo-edilizio` | Inquadra il regime applicabile (edilizia libera art. 6, CILA art. 6-bis, SCIA art. 22, SCIA alternativa art. 23) a partire dalla categoria dell'intervento (art. 3) |
| `imposta-scia-alternativa` | Imposta gli adempimenti della SCIA (art. 22) e della SCIA in alternativa al PdC (art. 23): relazione, termini, contributo, efficacia, collaudo |

Nucleo: **edilizia libera** senza titolo (art. 6); **CILA** comunicazione asseverata
residuale (art. 6-bis); **SCIA** ex art. 19 L. 241/1990 (art. 22); **SCIA alternativa al
PdC** con preavviso di 30 giorni e contributo di costruzione (art. 23).

## Fonti consultate

- **D.P.R. 6/6/2001 n. 380** (Testo unico edilizia) - Titolo II - artt. 6, 6-bis, 22, 23 -
  testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non qualifica** in concreto l'intervento (categoria ex art. 3): rinvio a
  `definizioni-interventi-edilizi-dpr380`.
- **Non tratta** il permesso di costruire (skill `permesso-costruire-dpr380`).
- **Non riproduce** il glossario dell'edilizia libera (DM 2/3/2018) né la modulistica
  unificata (skill `modulistica-edilizia-unificata`).
- **Non redige** CILA/SCIA/asseverazioni.
- **Non tratta** le discipline regionali (che possono ampliare/ridurre gli ambiti) né i
  vincoli (paesaggio, sismica).
- **Non sostituisce** il tecnico abilitato né il SUE/Comune.

**La skill è un supporto documentale: non sostituisce il tecnico abilitato, il SUE/Comune,
né la lettura degli artt. 6, 6-bis, 22, 23 del DPR 380/2001 e delle discipline regionali.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
