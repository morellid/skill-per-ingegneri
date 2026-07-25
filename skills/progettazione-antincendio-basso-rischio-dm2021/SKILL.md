---
name: progettazione-antincendio-basso-rischio-dm2021
description: "Supporto documentale per la progettazione, realizzazione ed esercizio della sicurezza antincendio nei luoghi di lavoro secondo il D.M. 3 settembre 2021 (attuativo dell'art. 46 c.3 lett. a punti 1 e 2 del D.Lgs 81/2008, in vigore dal 29 ottobre 2022, sostituisce il D.M. 10/3/1998). Aiuta RSPP, progettista antincendio e datore di lavoro a: inquadrare la valutazione del rischio di incendio come parte specifica del DVR (art. 2); stabilire quale corpo di regole si applica (art. 3: regola tecnica verticale se applicabile; luoghi a basso rischio secondo l'Allegato I - il minicodice; altrimenti il Codice di prevenzione incendi D.M. 3/8/2015); verificare i requisiti di basso rischio (attivita' non soggetta e senza RTV con affollamento minore o uguale a 100 occupanti, superficie minore o uguale a 1000 mq, piani tra -5 e 24 m, assenza di materiali combustibili, sostanze pericolose e lavorazioni pericolose significative); e applicare la strategia antincendio dell'Allegato I (compartimentazione; esodo con almeno due vie indipendenti, lunghezze e larghezze minime, densita' 0,7 persone/mq; gestione della sicurezza antincendio GSA; controllo dell'incendio con estintori e reti idranti; rivelazione e allarme IRAI; controllo di fumi e calore; operativita' antincendio; sicurezza degli impianti tecnologici). Use when an RSPP/fire-safety designer must frame the fire-risk assessment in the DVR, decide whether the low-risk minicode or the fire-prevention Code applies, or apply the minimum fire-safety strategy for a low-risk workplace; it is a documentary aid, does NOT design the measures in place of the technician, does NOT reproduce the Fire Prevention Code (D.M. 3/8/2015) nor the cited UNI standards and does NOT replace the fire-safety professional."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Progettazione antincendio luoghi di lavoro a basso rischio (D.M. 3/9/2021)"
summary: "Progettazione sicurezza antincendio nei luoghi di lavoro (D.M. 3/9/2021, art. 46 D.Lgs 81/2008): rischio incendio nel DVR, quale regola si applica (RTV / minicodice / Codice PI), requisiti di basso rischio e strategia antincendio (esodo, estintori, GSA). Non progetta le misure."
normative_refs:
  - "D.M. 3 settembre 2021 (progettazione sicurezza antincendio luoghi di lavoro) - artt. 1-5 e Allegato I"
  - "D.Lgs. 81/2008 art. 46 c.3 lett. a) punti 1-2 e art. 17 c.1 lett. a) (DVR)"
version: 0.1.0-alpha
status: alpha
tags:
  - antincendio
  - progettazione
  - basso-rischio
  - minicodice
  - dm-3-9-2021
  - sicurezza-lavoro
---

# Progettazione antincendio luoghi di lavoro a basso rischio (D.M. 3 settembre 2021)

Supporto documentale per impostare/verificare la **progettazione, realizzazione ed esercizio della sicurezza
antincendio nei luoghi di lavoro** secondo il **D.M. 3 settembre 2021** (attuativo dell'**art. 46 c. 3 lett. a) punti 1
e 2 del D.Lgs 81/2008**), in vigore dal **29 ottobre 2022**.

**La skill è un supporto documentale: non progetta le misure al posto del tecnico, non riproduce il Codice di prevenzione incendi (D.M. 3/8/2015) né le norme UNI citate e non sostituisce il professionista antincendio.**

## A chi serve

RSPP, progettista antincendio, datore di lavoro: chiunque debba inquadrare la valutazione del rischio di incendio nel
DVR e la strategia antincendio di un luogo di lavoro, in particolare a basso rischio.

## Cosa fa

1. **Inquadra la valutazione del rischio di incendio** come parte specifica del DVR (art. 2).
2. **Stabilisce quale corpo di regole si applica** (art. 3): RTV se applicabile; **basso rischio → Allegato I
   (minicodice)**; altrimenti **Codice PI (D.M. 3/8/2015)**.
3. **Verifica i requisiti di basso rischio** (affollamento ≤ 100, superficie ≤ 1000 m², quota -5/+24 m, no
   combustibili/sostanze/lavorazioni pericolose significative).
4. **Applica la strategia antincendio** dell'Allegato I (compartimentazione, esodo, GSA, controllo dell'incendio,
   rivelazione e allarme, controllo fumi e calore, operatività, impianti tecnologici).

## Sotto-attività

- [`inquadra-applicabilita-e-rischio`](tasks/inquadra-applicabilita-e-rischio.md) — decide quale corpo di regole si
  applica (RTV / minicodice / Codice PI) verificando i requisiti di basso rischio, e inquadra la valutazione del
  rischio di incendio nel DVR.
- [`imposta-strategia-antincendio`](tasks/imposta-strategia-antincendio.md) — imposta le misure minime dell'Allegato I
  (esodo, compartimentazione, controllo dell'incendio, GSA e le altre) con i parametri numerici verificati.

## Fonte (Regola zero)

D.M. 3 settembre 2021, pubblicato in **GU Serie Generale n. 259 del 29/10/2021**; testo trascritto in
[`references/fonti/dm-3-9-2021-progettazione-antincendio.md`](references/fonti/dm-3-9-2021-progettazione-antincendio.md),
hash SHA256 in [`references/sources.yaml`](references/sources.yaml). Costanti numeriche verificate a immagine. Checklist
in [`references/estratti/progettazione-antincendio-checklist.md`](references/estratti/progettazione-antincendio-checklist.md).

## Limiti

- Non **progetta** le misure al posto del tecnico né firma elaborati.
- Non riproduce il **Codice di prevenzione incendi (D.M. 3/8/2015)**, richiamato per i luoghi non a basso rischio, né le
  **norme UNI** citate (diritto d'autore): ne inquadra il rinvio.
- Non è la **gestione dell'emergenza** (D.M. 2/9/2021) né il **controllo/manutenzione** dei sistemi (D.M. 1/9/2021):
  temi con skill dedicate.
