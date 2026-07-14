---
name: consulente-adr-dlgs40
description: "Supporto documentale agli obblighi relativi al consulente per la sicurezza dei trasporti di merci pericolose (DGSA) ai sensi del D.Lgs. 40/2000: aiuta a determinare se un'impresa e' tenuta a nominare il consulente (ambito - trasporto o carico/scarico di merci pericolose su strada, ferrovia o via navigabile interna, art. 2; esenzioni per quantitativi limitati o trasporti occasionali, art. 3 c. 6), gli obblighi del capo dell'impresa (nomina, comunicazione alla motorizzazione civile, conservazione della relazione per cinque anni, art. 3), gli obblighi del consulente (relazione annuale e a ogni evento modificativo, relazione d'incidente al Ministero dei trasporti, art. 4), la qualificazione con certificato di formazione professionale (art. 5) e le sanzioni e la vigilanza (art. 6). Use when an Italian company transporting or loading dangerous goods must map the dangerous-goods safety adviser duties, the annual report and penalties; it is a documentary aid and does not draft the annual report nor cover the ADR technical rules."
license: MIT
area: ambiente-territorio-mobilita
title: "Consulente sicurezza trasporti merci pericolose (DGSA) - D.Lgs. 40/2000"
summary: "Obblighi del consulente sicurezza trasporti merci pericolose - DGSA (D.Lgs. 40/2000): chi deve nominarlo ed esenzioni (artt. 2, 3), obblighi del capo dell'impresa (art. 3) e del consulente (relazione annuale e d'incidente, art. 4), qualificazione (art. 5), sanzioni (art. 6)"
normative_refs:
  - "D.Lgs. 4/2/2000 n. 40 (testo vigente) - artt. 2, 3, 4, 5, 6 (attuazione dir. 96/35/CE; quadro ADR 1.8.3)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-40-2000
  - merci-pericolose
  - consulente-adr
  - dgsa
  - trasporti
---

# Consulente sicurezza trasporti merci pericolose (DGSA) - D.Lgs. 40/2000

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi relativi al **consulente per la
sicurezza dei trasporti di merci pericolose** (DGSA) ai sensi del **D.Lgs.
40/2000**:

- capire se un'impresa e' **tenuta a nominare** il consulente (ambito dell'art.
  2; **esenzioni** dell'art. 3 c. 6);
- gli **obblighi del capo dell'impresa** (nomina, comunicazione alla
  motorizzazione civile, conservazione della relazione per 5 anni - art. 3);
- gli **obblighi del consulente** (relazione **annuale** e a ogni evento
  modificativo; **relazione d'incidente** - art. 4);
- la **qualificazione** (certificato di formazione professionale - art. 5) e le
  **sanzioni** (art. 6).

**Non e' una skill di calcolo**: non redige la relazione annuale ne' la relazione
d'incidente, non riproduce gli allegati e non tratta il merito tecnico dell'ADR.

## Cosa NON fa (limiti)

- Non riproduce gli **allegati I e II** (compiti e materie d'esame) ne' il
  **formato della relazione annuale** (ADR 1.8.3, UNECE): li cita.
- Non redige la relazione annuale ne' la relazione d'incidente.
- Non tratta le **regole tecniche ADR** (classificazione, imballaggi,
  etichettatura) ne' il D.Lgs. 35/2010 (dir. 2008/68/CE) oltre ai richiami.
- Non sostituisce il consulente qualificato ne' la motorizzazione civile.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-obbligo-nomina`](tasks/verifica-obbligo-nomina.md) | Dato il profilo dell'impresa (attivita', quantitativi, occasionalita'), determina se deve nominare il consulente o se e' esente (artt. 2, 3 c. 6) |
| [`checklist-adempimenti`](tasks/checklist-adempimenti.md) | Verifica gli adempimenti del capo dell'impresa e del consulente (nomina, comunicazione, relazione annuale, relazione d'incidente) e le sanzioni (art. 6) |

## Riferimenti normativi

- **D.Lgs. 4/2/2000 n. 40** (consulente merci pericolose), testo vigente su
  Normattiva (pagina indice pinnata `!vig=2026-07-14`) - artt. 2, 3, 4, 5, 6.
- Quadro internazionale: **ADR 1.8.3** (UNECE), richiamato dal **D.Lgs. 35/2010**
  (dir. 2008/68/CE) - citati, non riprodotti.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-40-2000.md`,
`references/estratti/consulente-adr-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la nomina, la relazione annuale e la
qualificazione del consulente richiedono un professionista certificato; il formato
della relazione segue l'ADR 1.8.3. La responsabilita' resta del capo dell'impresa.
