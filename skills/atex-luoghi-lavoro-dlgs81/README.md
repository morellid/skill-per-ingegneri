# atex-luoghi-lavoro-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RSPP/esperto sicurezza di processo da completare)

Skill di **supporto documentale alla protezione dei lavoratori dai rischi da
atmosfere esplosive** (ATEX luoghi di lavoro) ai sensi del **Titolo XI del D.Lgs.
81/2008** (recepimento della dir. 1999/92/CE).

**Non e' una skill di calcolo**: mappa ambito, obblighi, zone, DPCE, verifiche e
sanzioni; non classifica le zone, non redige la valutazione ne' il DPCE. Non
tratta la **marcatura ATEX degli apparecchi** (dir. 2014/34/UE).

## Target

Datori di lavoro, RSPP, tecnici della sicurezza e consulenti.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `applicabilita-e-obblighi` | Dato il luogo di lavoro (sostanze infiammabili, processi, esclusioni), determina se si applica il Titolo XI e la sequenza degli obblighi (prevenzione, valutazione, zone, DPCE, verifiche) |
| `checklist-dpce` | Verifica i contenuti minimi del documento sulla protezione contro le esplosioni (art. 294) e le sanzioni (art. 297) |

Nucleo: **ambito** ed esclusioni (art. 287), **obblighi** del datore di lavoro
(art. 289), **valutazione** del rischio (art. 290), **zone** (art. 293, allegato
XLIX), **DPCE** (art. 294), **verifiche** (art. 296, DPR 462/2001), **sanzioni**
(art. 297).

## Fonti consultate

- **D.Lgs. 9/4/2008 n. 81** (TU sicurezza), Titolo XI, testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`) - artt. 287-290, 293, 294,
  296, 297 (recepimento dir. 1999/92/CE)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non classifica le **zone** (allegato XLIX) ne' riproduce prescrizioni minime
  (allegato L) e segnaletica (allegato LI): rinvia agli allegati e alle norme
  tecniche (CEI EN 60079)
- Non redige la valutazione del rischio di esplosione ne' il **DPCE**
- Non copre la **marcatura ATEX degli apparecchi** (dir. 2014/34/UE)

**La skill e' un supporto documentale: non sostituisce il datore di lavoro,
l'RSPP ne' il tecnico qualificato.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
