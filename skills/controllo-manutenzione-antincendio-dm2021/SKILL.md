---
name: controllo-manutenzione-antincendio-dm2021
description: "Supporto documentale per l'obbligo di controllo e manutenzione degli impianti, attrezzature ed altri sistemi di sicurezza antincendio nei luoghi di lavoro, ai sensi del D.M. 1 settembre 2021 (attuativo dell'art. 46 c.3 lett. a punto 3 del D.Lgs 81/2008, in vigore dal 25 settembre 2022). Aiuta RSPP, datore di lavoro, tecnico antincendio e manutentore a: distinguere i tre livelli di attivita' (sorveglianza, controllo periodico, manutenzione) secondo le definizioni dell'art. 1; impostare e tenere il registro dei controlli antincendio predisposto dal datore di lavoro (Allegato I), con cadenze tratte dalle norme/specifiche tecniche pertinenti e dal manuale d'uso; individuare la norma tecnica di riferimento per tipologia di impianto tramite la Tabella 1 dell'Allegato I (es. UNI 9994-1 estintori, UNI 10779/EN 671-3/EN 12845 idranti e sprinkler, UNI 11224 IRAI); verificare che manutenzione e controllo periodico siano eseguiti da tecnici manutentori qualificati (art. 4 e Allegato II: formazione, valutazione, attestazione dei Vigili del fuoco, regime transitorio per chi ha almeno 3 anni di attivita'). Use when an RSPP/employer/fire-safety technician must set up the fire-safety maintenance register, map equipment to the reference UNI standard, or check the qualification of maintainers under the Italian fire-safety maintenance decree; it is a documentary aid, does NOT set the specific inspection frequencies (which come from the product UNI standards) and does NOT replace the qualified maintainer or the fire-prevention professional."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Controllo e manutenzione antincendio (D.M. 1 settembre 2021)"
summary: "Controllo e manutenzione dei sistemi di sicurezza antincendio nei luoghi di lavoro (D.M. 1/9/2021, art. 46 D.Lgs 81/2008): registro dei controlli, sorveglianza/controllo periodico/manutenzione, norme UNI (Tab. 1), tecnici manutentori qualificati. Non fissa periodicita' puntuali."
normative_refs:
  - "D.M. 1 settembre 2021 (controllo e manutenzione sistemi di sicurezza antincendio) - artt. 1-6 e Allegati I-II"
  - "D.Lgs. 81/2008 art. 46 c.3 lett. a) punto 3 (prevenzione incendi e gestione emergenze)"
version: 0.1.0-alpha
status: alpha
tags:
  - antincendio
  - manutenzione
  - registro-controlli
  - dm-1-9-2021
  - tecnico-manutentore-qualificato
  - sicurezza-lavoro
---

# Controllo e manutenzione antincendio (D.M. 1° settembre 2021)

Supporto documentale per impostare e verificare il **controllo e la manutenzione degli impianti, attrezzature ed altri
sistemi di sicurezza antincendio** nei luoghi di lavoro, secondo il **D.M. 1° settembre 2021** (attuativo dell'**art. 46
c. 3 lett. a) punto 3 del D.Lgs 81/2008**), in vigore dal **25 settembre 2022**.

**La skill è un supporto documentale: non fissa le periodicità puntuali (che discendono dalle norme UNI di prodotto), non certifica il registro e non sostituisce il tecnico manutentore qualificato né il professionista antincendio.**

## A chi serve

RSPP, datore di lavoro, tecnico antincendio, responsabile della manutenzione, manutentore: chiunque debba organizzare
il regime di controllo e manutenzione antincendio di un'attività e tenerne traccia.

## Cosa fa

1. **Distingue i tre livelli di attività** (art. 1): sorveglianza (controlli visivi, anche dei lavoratori istruiti),
   controllo periodico (verifica funzionalità con frequenza non superiore a quella indicata), manutenzione (mantenere
   in efficienza).
2. **Imposta il registro dei controlli** predisposto dal datore di lavoro (Allegato I): cosa annotare, con quali
   cadenze, tenuta aggiornata e disponibile per gli organi di controllo.
3. **Individua la norma tecnica di riferimento** per tipologia di sistema tramite la Tabella 1 dell'Allegato I.
4. **Verifica la qualificazione dei manutentori** (art. 4 + Allegato II): percorso di formazione, valutazione,
   attestazione dei Vigili del fuoco, regime transitorio.

## Sotto-attività

- [`inquadra-registro-e-livelli-controllo`](tasks/inquadra-registro-e-livelli-controllo.md) — imposta il registro dei
  controlli, distingue sorveglianza/controllo periodico/manutenzione e collega ogni sistema alla norma UNI di
  riferimento (Tabella 1).
- [`verifica-qualificazione-manutentori`](tasks/verifica-qualificazione-manutentori.md) — verifica che manutenzione e
  controllo periodico siano eseguiti da tecnici manutentori qualificati (Allegato II) e inquadra il regime transitorio.

## Fonte (Regola zero)

D.M. 1° settembre 2021, pubblicato in **GU Serie Generale n. 230 del 25/09/2021**; testo trascritto in
[`references/fonti/dm-1-9-2021-controllo-manutenzione-antincendio.md`](references/fonti/dm-1-9-2021-controllo-manutenzione-antincendio.md),
hash SHA256 verificato in [`references/sources.yaml`](references/sources.yaml). Checklist operativa in
[`references/estratti/controllo-manutenzione-checklist.md`](references/estratti/controllo-manutenzione-checklist.md).

## Limiti

- Non fissa le **periodicità puntuali** dei controlli: queste discendono dalle **norme UNI di prodotto** (es. UNI
  9994-1 per gli estintori) richiamate nella Tabella 1, soggette a diritto d'autore e non trascritte.
- Non è la **gestione dell'emergenza** (D.M. 2/9/2021), la **progettazione** antincendio (D.M. 3/9/2021), il DPR
  151/2011 né il carico d'incendio (D.M. 9/3/2007): temi con skill dedicate.
