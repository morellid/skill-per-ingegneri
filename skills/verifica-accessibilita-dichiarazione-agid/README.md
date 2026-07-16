# verifica-accessibilita-dichiarazione-agid

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di accessibilità / RTD da completare)

Skill di **supporto documentale** al **metodo di verifica dell'accessibilità** (verifica
tecnica + verifica soggettiva) e alla **dichiarazione di accessibilità** degli strumenti
informatici (siti web, app mobili, software, documenti), secondo le **Linee guida AgID
sull'accessibilità degli strumenti informatici** (adottate ex art. 11 L. 4/2004, versione
21/12/2022).

**Non esegue l'audit tecnico** WCAG/EN 301549, **non riproduce la norma UNI CEI EN 301549**
(a pagamento) né le **WCAG**, e **non compila** la dichiarazione sulla piattaforma AgID:
inquadra metodo, contenuti e scadenze.

## Target

PA e loro fornitori (RTD, uffici IT) e grandi operatori privati obbligati che devono
verificare l'accessibilità e predisporre/rinnovare la dichiarazione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `imposta-verifica-accessibilita` | Imposta la verifica tecnica (EN 301549 / WCAG 2.1 AA) e la verifica soggettiva a 4 fasi, con la soglia dell'art. 35 D.Lgs 50/2016 |
| `predisponi-dichiarazione-accessibilita` | Struttura la dichiarazione di accessibilità (modello AgID, fonti di analisi, link, riesame 23 settembre) e gli obiettivi annuali |

Nucleo: **requisiti tecnici** (punto 9 EN 301549, WCAG 2.1 AA), **verifica tecnica +
soggettiva** (4 fasi, scala 1-5, 12 criteri; obbligatoria sopra soglia art. 35 D.Lgs
50/2016), **dichiarazione di accessibilità** (piattaforma AgID, footer, riesame 23
settembre), **obiettivi annuali PA** (31 marzo), **deroghe** per onere sproporzionato (art.
3-ter L. 4/2004), **feedback** e **Difensore civico digitale**.

## Fonti consultate

- **AgID - Linee guida sull'accessibilità degli strumenti informatici** (versione
  21/12/2022) - PDF ufficiale su agid.gov.it (capitoli 2, 3, 4, 6, 7)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue l'audit tecnico** WCAG/EN 301549 né la verifica soggettiva.
- **Non riproduce la norma UNI CEI EN 301549** (a pagamento) né le WCAG: rinvia ai
  punti/Prospetti/Appendici e ai criteri di successo.
- **Non compila la dichiarazione** (form sulla piattaforma AgID).
- È complementare a `accessibilita-siti-app-l4-2004` (obblighi/soggetti/sanzioni della Legge
  Stanca): questa copre il metodo di verifica e la dichiarazione.

**La skill è un supporto documentale: non sostituisce l'audit tecnico di accessibilità, il
RTD né la lettura delle Linee guida AgID e della norma UNI CEI EN 301549.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
