---
name: relazione-geologica-geotecnica-ntc
description: Supporta il controllo di completezza della relazione geologica e della relazione geotecnica richieste dalle NTC 2018 (parr. 6.1.2, 6.2.1, 6.2.2) e dalla Circolare 7/2019 (C6.2.1, C6.2.2.5), il controllo di coerenza tra le due relazioni e la stesura della struttura di una relazione geotecnica. Use when the user asks to check, review or draft a relazione geologica or relazione geotecnica per NTC 2018.
license: MIT
area: strutture-geotecnica
title: "Relazione geologica e geotecnica - NTC 2018 cap. 6"
summary: "Checklist di completezza e coerenza per relazione geologica e relazione geotecnica secondo NTC 2018 parr. 6.1.2-6.2.6 e Circolare 7/2019 cap. C6, con bozza di struttura della relazione geotecnica - supporto documentale che non sostituisce il professionista firmatario"
normative_refs:
  - "NTC 2018 (DM 17/01/2018) parr. 6.1-6.2.6"
  - "Circolare C.S.LL.PP. 21/01/2019 n. 7 parr. C6.2, C9.1 lett. g, C10.1"
  - "DPR 380/2001 art. 59 (laboratori prove, per rinvio dalle NTC)"
version: 0.1.0-alpha
status: alpha
tags:
  - ntc-2018
  - geotecnica
  - relazione-geologica
  - relazione-geotecnica
---

# Relazione geologica e geotecnica - NTC 2018 cap. 6

## Quando usare questa skill

Usala quando devi verificare che una relazione geologica o una relazione
geotecnica contenga cio' che NTC 2018 e Circolare 7/2019 richiedono, quando
devi controllare la coerenza tra le due relazioni (e con la relazione di
calcolo), o quando devi impostare l'indice di una relazione geotecnica.
Target: ingegneri civili progettisti, geologi, collaudatori statici.

Non usarla per eseguire le verifiche geotecniche delle singole opere
(fondazioni, opere di sostegno, pendii: NTC parr. 6.3-6.11, fuori scope).

## Avvertenza

Questa skill e' uno strumento di supporto alla verifica e all'impostazione
di documenti tecnici. **Non sostituisce il giudizio del professionista
firmatario.** Non produce documenti pronti al deposito o alla firma; la
relazione geologica e' un elaborato del Geologo e la relazione geotecnica e'
responsabilita' del Progettista (Circolare 7/2019, C9.1 lett. g e C10.1).
L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Check relazione geologica**: l'utente ha una relazione geologica da
  verificare -> `tasks/check-relazione-geologica.md`
- **Check relazione geotecnica**: l'utente ha una relazione geotecnica da
  verificare -> `tasks/check-relazione-geotecnica.md`
- **Check coerenza geologica/geotecnica**: l'utente ha entrambe le relazioni
  (o relazione geotecnica + relazione di calcolo) e vuole verificarne la
  coerenza -> `tasks/check-coerenza-geologica-geotecnica.md`
- **Bozza struttura relazione geotecnica**: l'utente deve impostare una
  relazione geotecnica e vuole un indice commentato ->
  `tasks/draft-struttura-relazione-geotecnica.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita'
desidera.

## Processo generale

1. Identifica la sotto-attivita' desiderata dall'utente
2. Carica il file `tasks/<task-scelto>.md`
3. Richiedi gli input necessari come specificato nel task
4. Applica la procedura descritta, citando i paragrafi normativi precisi
5. Produci l'output nel formato atteso
6. Includi sempre nel report finale il rinvio alla verifica del
   professionista firmatario

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizioni delle fonti
lette in `references/fonti/`, estratti operativi in `references/estratti/`:

- `estratti/ntc2018-cap6-relazioni.md` - NTC 2018 parr. 6.1-6.2.6
- `estratti/circ-7-2019-c6-relazioni.md` - Circolare 7/2019 cap. C6
- `estratti/circ-7-2019-c9-c10-ruoli-elaborati.md` - ruoli, firme, elaborati

## Limiti

Cosa questa skill NON fa:
- non esegue verifiche geotecniche di opere specifiche (NTC parr. 6.3-6.11)
  ne' calcoli (portanza, cedimenti, stabilita')
- non valuta nel merito i contenuti geologici o geotecnici (correttezza del
  modello, adeguatezza dei parametri): controlla presenza, tracciabilita' e
  coerenza documentale
- non copre la progettazione in condizioni sismiche (NTC parr. 3.2, 7.11)
  oltre ai richiami presenti nel cap. 6
- non produce documenti auto-firmati ne' sostituisce indagini in sito o
  prove di laboratorio
