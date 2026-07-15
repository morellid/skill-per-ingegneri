---
name: trasporti-eccezionali-cds-art10
description: "Supporto documentale al regime dei veicoli e dei trasporti eccezionali ai sensi dell'art. 10 del Codice della Strada (D.Lgs. 285/1992): aiuta a inquadrare quando un veicolo o un trasporto e' eccezionale (eccedenza dei limiti di sagoma art. 61 o massa art. 62; cose indivisibili; generi tipizzati con massa complessiva fino a 38/48/86/108 t), a stabilire se serve l'autorizzazione alla circolazione e chi la rilascia (ente proprietario o concessionario della strada, regioni), i tipi di autorizzazione (singola volta per volta, multipla per piu' transiti, periodica), le prescrizioni (percorsi, periodi, scorta), i presupposti (compatibilita' con strade, manufatti e sicurezza) e le sanzioni (da 794 a 3.206 euro senza autorizzazione, oltre a sospensione della patente). Use when an Italian haulier or consultant must map whether a transport is abnormal, whether and from whom the road-circulation authorization is needed and the applicable penalties; it is a documentary aid and does not draft the application nor compute size/mass limits."
license: MIT
area: ambiente-territorio-mobilita
title: "Veicoli e trasporti eccezionali - art. 10 Codice della Strada"
summary: "Regime dei veicoli e trasporti eccezionali (art. 10 Codice della Strada, D.Lgs. 285/1992): inquadramento (eccedenza sagoma art. 61 / massa art. 62), obbligo di autorizzazione ed ente competente (c. 6), tipi singola/multipla/periodica (c. 9), prescrizioni, sanzioni (c. 18-25)"
normative_refs:
  - "D.Lgs. 30/4/1992 n. 285 (Codice della Strada, testo vigente) - art. 10"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-285-1992
  - codice-della-strada
  - trasporti-eccezionali
  - autorizzazione-circolazione
  - mobilita
---

# Veicoli e trasporti eccezionali - art. 10 Codice della Strada

## Quando usare questa skill

Usala quando devi orientarti sul regime dei **veicoli e trasporti eccezionali**
ai sensi dell'**art. 10 del Codice della Strada** (D.Lgs. 285/1992):

- inquadrare se un veicolo o un trasporto e' **eccezionale** (eccedenza dei
  limiti di **sagoma** art. 61 o **massa** art. 62; cose indivisibili; generi
  tipizzati con massa complessiva fino a 38/48/86/108 t);
- stabilire se serve l'**autorizzazione alla circolazione** e **chi la rilascia**
  (ente proprietario/concessionario della strada, regioni);
- distinguere i **tipi** di autorizzazione (singola, multipla, periodica), le
  **prescrizioni** (percorsi, periodi, scorta) e i **presupposti**;
- conoscere le **sanzioni** (art. 10 c. 18-25).

**Non e' una skill di calcolo**: non calcola i limiti di sagoma/massa, non
individua l'ente competente nel caso concreto, non redige la domanda ne'
riproduce le Linee guida MIT.

## Cosa NON fa (limiti)

- Non riproduce i **limiti di sagoma (art. 61) e massa (art. 62)** ne' le
  categorie (art. 54): rinvia agli articoli.
- Non redige la domanda ne' individua nel merito l'ente competente/il percorso.
- Non riproduce le **Linee guida MIT** sui trasporti eccezionali (2022) ne' il
  decreto attuativo del comma 10-bis.
- Non sostituisce l'ente proprietario/concessionario ne' il tecnico incaricato.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-eccezionalita`](tasks/inquadra-eccezionalita.md) | Dato il veicolo/trasporto (sagoma, massa, tipo di carico), determina se e' eccezionale, se serve l'autorizzazione e chi la rilascia, e il tipo di autorizzazione |
| [`checklist-autorizzazione`](tasks/checklist-autorizzazione.md) | Verifica presupposti, prescrizioni e adempimenti dell'autorizzazione e le sanzioni (art. 10 c. 18-25) |

## Riferimenti normativi

- **D.Lgs. 30/4/1992 n. 285** (Codice della Strada), **art. 10**, testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`). Articoli richiamati: 61
  (sagoma), 62 (massa), 13 (autorizzazioni), 54 (categorie).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-285-1992.md`,
`references/estratti/trasporti-eccezionali-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: i limiti dimensionali e di massa e
l'individuazione dell'ente competente e del percorso vanno verificati sugli
articoli richiamati e con l'ente proprietario/concessionario; l'autorizzazione e'
rilasciata dall'ente competente.
