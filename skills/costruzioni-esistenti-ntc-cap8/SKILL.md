---
name: costruzioni-esistenti-ntc-cap8
description: "Consultazione del capitolo 8 delle NTC 2018 (costruzioni esistenti) e della Circolare 7/2019 cap. C8. Aiuta a classificare un intervento nelle tre categorie del par. 8.4 (riparazione/intervento locale, miglioramento, adeguamento), a stabilire se l'adeguamento e' obbligatorio (casi a-e del par. 8.4.3) e la relativa soglia del rapporto zeta_E (a,b,d -> 1,0; c,e -> 0,80), a individuare la soglia di zeta_E per il miglioramento in funzione della classe d'uso (classe III scolastica e IV -> 0,6; restanti III e II -> +0,1) e a determinare il livello di conoscenza LC1/LC2/LC3 e il fattore di confidenza FC (1,35/1,2/1,0 da Circolare C8.5.4 e Tab. C8.5.IV). Chiarisce quando sono obbligatorie la valutazione della sicurezza e la verifica del sistema di fondazione (par. 8.3). Use when an Italian structural engineer needs to classify an intervention on an existing building, find the applicable zeta_E threshold, or determine the knowledge level and confidence factor per NTC 2018 chapter 8; it is a normative-consultation aid and does not replace the designer's safety assessment."
license: MIT
area: strutture-geotecnica
title: "Costruzioni esistenti - NTC 2018 cap. 8 (interventi, LC/FC, zeta_E)"
summary: "Consultazione NTC 2018 cap. 8 + Circolare C8: classificazione interventi (locale/miglioramento/adeguamento, par. 8.4), soglie zeta_E, livelli di conoscenza LC1/LC2/LC3 e fattori di confidenza FC 1,35/1,2/1,0 (Tab. C8.5.IV) - non calcola, non sostituisce il progettista"
normative_refs:
  - "NTC 2018 (DM 17/01/2018) cap. 8 (parr. 8.3, 8.4, 8.5.4)"
  - "Circolare C.S.LL.PP. 21/01/2019 n. 7 cap. C8 (parr. C8.3, C8.4, C8.5.4, Tab. C8.5.IV)"
version: 0.1.0-alpha
status: alpha
tags:
  - ntc-2018
  - strutture
  - costruzioni-esistenti
  - vulnerabilita-sismica
  - consultazione-norma
---

# Costruzioni esistenti - NTC 2018 cap. 8 (interventi, LC/FC, zeta_E)

## Quando usare questa skill

Usala quando un progettista deve, per una costruzione esistente:

- **classificare un intervento** nelle tre categorie del par. 8.4
  (riparazione/intervento locale, miglioramento, adeguamento);
- capire **se l'adeguamento e' obbligatorio** (casi a-e del par. 8.4.3) e quale
  **soglia di zeta_E** si applica;
- individuare la **soglia di zeta_E per il miglioramento** in base alla classe
  d'uso;
- determinare il **livello di conoscenza (LC1/LC2/LC3)** raggiungibile con le
  indagini disponibili e il **fattore di confidenza (FC)** corrispondente;
- sapere **quando sono obbligatorie** la valutazione della sicurezza e la
  verifica del sistema di fondazione (par. 8.3).

Target: ingegneri strutturisti, progettisti di interventi su edifici esistenti,
collaudatori statici.

## Avvertenza

Questa skill e' uno strumento di **consultazione della norma**. **Non sostituisce
la valutazione della sicurezza ne' il giudizio del progettista firmatario.**
Non esegue verifiche strutturali, non calcola zeta_E ne' le capacita' degli
elementi, non sceglie ne' dimensiona gli interventi. La valutazione della
sicurezza e la relativa relazione (par. 8.3) sono responsabilita' del
progettista. L'uso improprio degli output e' responsabilita' dell'utente.

## Sotto-attivita' disponibili

In base alla richiesta, carica il file appropriato da `tasks/`:

- **Classifica intervento e trova la soglia zeta_E**: l'utente descrive un
  intervento e vuole sapere in quale categoria ricade e quale soglia di zeta_E
  si applica -> `tasks/classifica-intervento.md`
- **Determina livello di conoscenza e fattore di confidenza**: l'utente descrive
  le indagini svolte/previste e vuole il LC e l'FC -> `tasks/determina-lc-fc.md`
- **Q&A su valutazione della sicurezza e obblighi**: domande su quando e'
  obbligatoria la valutazione della sicurezza, la verifica delle fondazioni, gli
  stati limite, gli elaborati minimi -> `tasks/qa-cap8.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input necessari (tipo di intervento, classe d'uso, indagini,
   materiale strutturale, ecc.).
4. Rispondi **citando sempre il paragrafo preciso** (NTC par. 8.x / Circolare
   C8.x / Tab. C8.5.IV) da cui deriva ogni soglia o definizione.
5. Distingui esplicitamente cio' che e' **cogente nelle NTC** da cio' che e'
   **chiarimento/valore numerico della Circolare**.
6. Chiudi ogni risposta con il rinvio alla valutazione della sicurezza e al
   progettista firmatario.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizioni verificate delle
fonti lette in `references/fonti/`, estratto operativo in `references/estratti/`:

- `fonti/ntc2018-dm-17-01-2018.md` - NTC 2018 cap. 8 integrale (8.1-8.7.5)
- `fonti/circ-7-2019-mit.md` - Circolare 7/2019 C8.3, C8.4.x, C8.5.4.x + Tab. C8.5.IV
- `estratti/ntc2018-cap8-costruzioni-esistenti.md` - estratto operativo con tabelle

## Limiti

Cosa questa skill NON fa:
- non esegue verifiche strutturali ne' calcola zeta_E, le capacita' degli
  elementi o le analisi (lineari/non lineari, statiche/dinamiche);
- non sceglie ne' dimensiona le tecniche di intervento (par. 8.7);
- non fornisce i valori di tabella dei parametri meccanici della muratura
  (Tabelle C8.5.I/II/III) ne' le correlazioni;
- non copre i meccanismi locali/globali della muratura e degli aggregati
  (par. 8.7.1) oltre ai richiami di definizione;
- non produce documenti auto-firmati ne' la valutazione della sicurezza ex
  par. 8.3.
