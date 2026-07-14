---
name: bonifica-siti-contaminati-dlgs152
description: "Supporto documentale alla procedura di bonifica dei siti contaminati ai sensi del Titolo V della Parte quarta del D.Lgs. 152/2006: aiuta a orientarsi tra le definizioni chiave (concentrazioni soglia di contaminazione CSC dell'Allegato 5, concentrazioni soglia di rischio CSR determinate con l'analisi di rischio, sito potenzialmente contaminato/contaminato/non contaminato, MISE, MISO, messa in sicurezza permanente, bonifica, ripristino), la procedura operativa a iniziativa del responsabile (art. 242: prevenzione entro 24 ore, autocertificazione entro 48 ore se sotto CSC, piano di caratterizzazione entro 30 giorni, analisi di rischio entro 6 mesi, conferenza di servizi), il procedimento a iniziativa della pubblica amministrazione con ordinanza (art. 244), le aree di ridotte dimensioni (art. 249) e le sanzioni penali (art. 257). Use when an Italian consultant or operator must map the contaminated-site remediation procedure, its deadlines and the actors involved; it is a documentary aid and does not read the CSC tables, does not run the risk analysis nor draft the characterization plan."
license: MIT
area: ambiente-territorio-mobilita
title: "Bonifica siti contaminati - D.Lgs. 152/2006 Titolo V"
summary: "Procedura di bonifica dei siti contaminati (D.Lgs. 152/2006 Titolo V): definizioni CSC/CSR (art. 240), procedura del responsabile (art. 242: 24 ore, 48 ore, caratterizzazione, analisi di rischio), ordinanza della PA (art. 244), aree ridotte (art. 249), sanzioni (art. 257)"
normative_refs:
  - "D.Lgs. 3/4/2006 n. 152 (testo vigente) - Parte quarta Titolo V, artt. 240, 242, 244, 249, 257"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-152-2006
  - bonifica
  - siti-contaminati
  - analisi-di-rischio
  - testo-unico-ambientale
---

# Bonifica siti contaminati - D.Lgs. 152/2006 Titolo V

## Quando usare questa skill

Usala quando devi orientarti sulla **procedura di bonifica dei siti
contaminati** ai sensi del **Titolo V della Parte quarta del D.Lgs. 152/2006**:

- distinguere le **definizioni** (CSC, CSR, sito potenzialmente contaminato /
  contaminato / non contaminato, MISE, MISO, messa in sicurezza permanente,
  bonifica, ripristino) (art. 240);
- seguire la **procedura operativa** a iniziativa del responsabile (art. 242) con
  i suoi termini (24 ore, 48 ore, 30 giorni, 6 mesi, 60 giorni);
- capire il **procedimento a iniziativa della PA** con ordinanza (art. 244);
- conoscere le **aree di ridotte dimensioni** (art. 249) e le **sanzioni** (art.
  257).

**Non e' una skill di calcolo**: non legge i valori CSC (Allegato 5), non esegue
l'analisi di rischio (Allegato 1) ne' redige il piano di caratterizzazione
(Allegato 2).

## Cosa NON fa (limiti)

- Non riproduce i **valori CSC** (Allegato 5) ne' calcola le **CSR**: rinvia agli
  allegati e ai criteri/software di analisi di rischio.
- Non redige il **piano di caratterizzazione**, il progetto di bonifica ne' i
  piani di monitoraggio.
- Non tratta i **SIN** (siti di interesse nazionale, art. 252) ne' oneri reali e
  privilegi (artt. 250, 253) oltre ai richiami.
- Non sostituisce il tecnico competente ne' l'autorita' (regione, provincia,
  comune, ARPA).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`diagnosi-procedura`](tasks/diagnosi-procedura.md) | Dato l'evento (potenziale contaminazione, contaminazione storica, esito indagine preliminare), individua lo step della procedura dell'art. 242, i termini e gli attori, distinguendo sotto/sopra CSC e sopra CSR |
| [`checklist-adempimenti`](tasks/checklist-adempimenti.md) | Verifica la completezza degli adempimenti e dei termini (comunicazioni, autocertificazione, piano di caratterizzazione, analisi di rischio) e le sanzioni (art. 257) |

## Riferimenti normativi

- **D.Lgs. 3/4/2006 n. 152** (TUA), Parte quarta Titolo V, testo vigente su
  Normattiva:
  - **art. 240** (definizioni), **art. 242** (procedure operative), **art. 244**
    (ordinanze PA), **art. 249** (aree ridotte), **art. 257** (sanzioni penali).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-152-2006.md`,
`references/estratti/bonifica-siti-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: i valori CSC, l'analisi di rischio e i
progetti richiedono la lettura degli allegati e l'intervento di tecnici
qualificati; la decisione spetta all'autorita' competente.
