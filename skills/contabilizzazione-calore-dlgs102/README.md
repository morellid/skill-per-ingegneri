# contabilizzazione-calore-dlgs102

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con termotecnico / amministratore di condominio da completare)

Skill di **supporto documentale** all'inquadramento degli obblighi di
**contabilizzazione del calore** e di **ripartizione delle spese** negli edifici e
condomini con **impianto centralizzato** o **teleriscaldamento/teleraffrescamento**,
secondo il **D.Lgs. 102/2014, art. 9, comma 5** (e commi 5-bis/5-ter/5-quater).

**Non calcola** i millesimi termici né le quote (UNI 10200/EN 15459), **non redige** la
relazione tecnica di esenzione né la tabella di ripartizione e **non sostituisce** il
progettista/termotecnico o l'amministratore: inquadra obblighi e criteri.

## Target

Ingegneri/termotecnici (progettisti, direttori dei lavori) e amministratori di
condominio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-obbligo-contabilizzazione` | Individua gli obblighi (contatore di fornitura, sotto-contatori o ripartitori) e i presupposti di esenzione con relazione tecnica (art. 9 c. 5 a-c, 5-bis, 5-ter) |
| `imposta-ripartizione-spese` | Imposta lo schema di ripartizione: quota ≥ 50% ai prelievi volontari e quota residua (millesimi/mq/mc/potenze, UNI 10200), con i casi particolari (art. 9 c. 5 d, 5-quater) |

Nucleo: **contatore di fornitura** (a); **sotto-contatori** UNI EN 15459 (b);
**termoregolazione/contabilizzazione individuale** (c); **ripartizione** con quota ≥
50% ai prelievi volontari e quota residua UNI 10200 (d); **lettura da remoto** (5-bis),
**nuove costruzioni** (5-ter), **guida ENEA** (5-quater).

## Fonti consultate

- **D.Lgs. 4/7/2014 n. 102** (efficienza energetica) - art. 9 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 14G00113)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** i **millesimi termici**, le **quote** né la verifica di **efficienza
  in termini di costi** (UNI 10200, UNI EN 15459 - non riprodotte).
- **Non redige** la **relazione tecnica** di impossibilità/inefficienza né la **tabella
  millesimale** di ripartizione.
- **Non riproduce** i **provvedimenti ARERA** (art. 9 cc. 1-4, sistemi di misurazione
  intelligenti) né le regole di fatturazione di dettaglio.
- **Non tratta** la **diagnosi energetica** (art. 8 — vedi `diagnosi-energetica-dlgs102`)
  né l'esercizio/manutenzione degli impianti termici (DPR 74/2013).
- **Non sostituisce** il progettista/termotecnico né l'amministratore.

**La skill è un supporto documentale: non sostituisce il progettista/termotecnico né
l'amministratore, né la lettura dell'art. 9 del D.Lgs. 102/2014.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
