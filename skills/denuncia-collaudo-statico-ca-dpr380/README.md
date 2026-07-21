# denuncia-collaudo-statico-ca-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con collaudatore statico / strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale**, al **direttore dei lavori** e al
**collaudatore statico** per le **opere in conglomerato cementizio armato** (normale e precompresso)
**e a struttura metallica**, ai sensi del **D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia), Parte
II, Capo I, artt. 64-67**.

**Non redige** il progetto strutturale, la relazione o il certificato di collaudo, **non esegue** il
calcolo né il collaudo e **non sostituisce** il tecnico abilitato, il direttore dei lavori, il
collaudatore o gli uffici competenti: inquadra obblighi, soggetti, documenti e termini.

## Target

Progettisti strutturali, direttori dei lavori, collaudatori statici e uffici tecnici che devono
inquadrare denuncia dei lavori e collaudo statico delle opere in c.a./c.a.p. e acciaio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-denuncia-lavori` | Soggetti e responsabilità (art. 64), denuncia allo sportello unico con allegati e varianti (art. 65 cc. 1-5), documenti in cantiere (art. 66), relazione a struttura ultimata (art. 65 cc. 6-8) |
| `inquadra-collaudo-statico` | Obbligo, requisiti e indipendenza del collaudatore, nomina, termini, certificato e dichiarazione di regolare esecuzione (art. 67) |

Nucleo: **denuncia dei lavori** via PEC (art. 65), **collaudo statico** da ingegnere/architetto iscritto
da 10 anni e indipendente (art. 67), **relazione a struttura ultimata** entro 60 giorni, **documenti in
cantiere** (art. 66), **responsabilità** dei soggetti (art. 64).

## Fonti consultate

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - Parte II, Capo I, artt. 64-67 - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429, idGruppo 12).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il progetto/relazione/certificato di collaudo; **non esegue** il calcolo né il
  collaudo.
- **Non riproduce** le NTC 2018 (D.M. 17/1/2018) né gli artt. 53/59/62/94-bis se non nei richiami.
- **Non tratta** la disciplina sismica (artt. 93-94, skill `denuncia-autorizzazione-sismica-dpr380`) se
  non nei rimandi.

**La skill è un supporto documentale: non sostituisce il tecnico abilitato, il direttore dei lavori, il
collaudatore o gli uffici competenti, né la lettura degli artt. 64-67 del D.P.R. 380/2001 e delle NTC.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
