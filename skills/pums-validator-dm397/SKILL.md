---
name: pums-validator-dm397
description: Verifica la conformita' di un Piano Urbano di Mobilita' Sostenibile (PUMS) al DM 4 agosto 2017 n. 397 come modificato dai DM 28 agosto 2019 n. 396, DM 26 gennaio 2021 n. 29 e DM 12 novembre 2021 n. 444, e al Vademecum MIMS 2022. Use when the user asks to validate a PUMS document for an Italian municipality, citta' metropolitana, or association of comuni with more than 100.000 inhabitants.
license: MIT
area: ambiente-territorio-mobilita
title: "Validatore PUMS - DM 397/2017"
summary: "Verifica della conformita' formale e di completezza di un Piano Urbano di Mobilita' Sostenibile (PUMS) per comuni > 100.000 ab., citta' metropolitane o associazioni di comuni che superano la soglia"
normative_refs:
  - "DM 397/2017"
  - "DM 396/2019"
  - "DM 29/2021"
  - "DM 444/2021"
  - "Vademecum MIMS 2022"
version: 0.1.0-alpha
status: alpha
tags:
  - pums
  - dm-397-2017
  - mobilita
---

# Validatore PUMS (DM 397/2017 e s.m.i.)

## Quando usare questa skill

Questa skill supporta il **controllo di conformita' formale e di completezza** di un Piano Urbano di Mobilita' Sostenibile (PUMS) redatto da una citta' metropolitana, da un comune con popolazione superiore a 100.000 abitanti o da un'associazione di comuni che supera tale soglia, rispetto al quadro normativo italiano vigente (DM 397/2017 + DM 396/2019 + DM 29/2021 + DM 444/2021 + Vademecum MIMS 2022).

Destinatari tipici: tecnico comunale, mobility manager d'area, consulente di un'amministrazione che sta redigendo o aggiornando un PUMS, o un revisore che deve istruire una pratica di accesso a finanziamenti statali per il trasporto rapido di massa (TRM).

**Quando NON usarla**: pianificazione regionale, piani settoriali (PUT, Biciplan, PRG-TPL) che non rientrano nel perimetro del PUMS, o documenti redatti per realta' inferiori a 100.000 abitanti non aderenti volontariamente alle Linee guida italiane.

## Avvertenza

Questa skill e' uno strumento di supporto al controllo di conformita' del PUMS. **Non sostituisce il giudizio del professionista firmatario, del Tavolo Tecnico PUMS, ne' delle competenti amministrazioni che valutano l'accesso ai finanziamenti.** L'output e' una check-list ragionata: e' responsabilita' dell'utente verificare in via diretta la corrispondenza con le fonti normative ufficiali e con eventuali Linee guida regionali integrative. La skill non produce documenti pronti al deposito o alla firma, ne' giudizi vincolanti sulla idoneita' ai finanziamenti.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Verifica obbligo e ambito di applicazione**: quando l'utente vuole capire se il proprio ente e' tenuto al PUMS, leggere `tasks/check-ambito-obbligo.md`.
- **Verifica procedura di redazione**: quando l'utente vuole controllare che il PUMS segua gli 8 passi dell'Allegato 1, leggere `tasks/check-procedura-redazione-pums.md`.
- **Verifica obiettivi**: quando l'utente vuole controllare che i 17 macro-obiettivi minimi obbligatori e gli obiettivi specifici siano presenti, leggere `tasks/check-obiettivi-pums.md`.
- **Verifica indicatori (Tabella 1 DM 396/2019)**: quando l'utente vuole controllare gli indicatori di risultato obbligatori e i target, leggere `tasks/check-indicatori-tabella1.md`.
- **Verifica piano di monitoraggio e aggiornamento**: quando l'utente vuole controllare la presenza del rapporto biennale e dell'aggiornamento quinquennale, leggere `tasks/check-monitoraggio-aggiornamento.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera o se vuole una valutazione completa (in tal caso esegui le 5 sotto-attivita' in sequenza).

## Processo generale

1. Identifica la sotto-attivita' desiderata dall'utente (puo' essere singola o "valutazione completa").
2. Carica il file `tasks/<task-scelto>.md` ed eventualmente l'estratto fonti pertinente da `references/estratti/`.
3. Richiedi i materiali del PUMS (documento principale, allegati, atto di adozione) o, se non disponibili, chiedi all'utente di descrivere lo stato di redazione/adozione.
4. Applica le check di conformita' del task, segnando ESITO per ciascuna voce: CONFORME / NON CONFORME / NON DETERMINABILE.
5. Produci un report strutturato (vedi sezione "Output" del task) che chiude sempre con: (a) elenco esiti, (b) elenco rilievi bloccanti, (c) elenco rilievi non bloccanti / suggerimenti migliorativi, (d) rinvio esplicito a verifica del professionista firmatario.

## Fonti normative

Riferimenti completi e hash SHA256 in `references/sources.yaml`. Trascrizioni fedeli in `references/fonti/`. Estratti curati per la validazione in `references/estratti/`.

Fonti coperte:
- DM 4 agosto 2017 n. 397 (Linee guida PUMS - testo originario, GU n.233 del 05/10/2017).
- DM 28 agosto 2019 n. 396 (modifica DM 397/2017: estensione obbligo TRM ai comuni superiori a 100.000 ab. non in citta' metropolitane, proroga 12 mesi, sostituzione Tabella 1 Macrobiettivi).
- DM 26 gennaio 2021 n. 29 (sostituisce l'art. 3 c.1 DM 397/2017 fissando i termini al 4 aprile / 4 agosto 2021; modifica il regime transitorio dell'art. 7 c.1 DM 396/2019).
- DM 12 novembre 2021 n. 444 (termine unitario di adozione al 1 gennaio 2023; sostituisce l'art. 1 c.2 DM 397/2017 estendendolo alla mobilita' ciclistica; abroga l'art. 7 c.3 DM 396/2019; affida le verifiche alla piattaforma dell'Osservatorio nazionale TPL).
- Vademecum PUMS MIMS-Politecnico di Milano del 27/09/2022 (interpretazione operativa, metodologia indicatori, fonti dati).

Nel testo della skill, il termine **"Linee guida italiane"** indica il DM 397/2017 come modificato dal DM 396/2019 (terminologia adottata dal Vademecum, nota 1 p.4). Le modifiche posteriori (DM 29/2021 e DM 444/2021) sono trattate come parte della catena vigente.

## Limiti

Cosa questa skill NON fa:
- Non produce documenti auto-firmati o atti di adozione.
- Non interpreta normativa regionale specifica (es. Linee guida regionali integrative).
- Non simula scenari ne' calcola valori di indicatori partendo da dati grezzi (richiede che il PUMS sia gia' redatto).
- Non sostituisce la Valutazione Ambientale Strategica (VAS).
- Non valuta l'ammissibilita' a finanziamenti specifici (es. avvisi TRM o mobilita' ciclistica): rinvia alle procedure specifiche dell'avviso e ai controlli della piattaforma dell'Osservatorio nazionale TPL (art. 3 DM 444/2021).
- Non valuta gli effetti di leggi regionali, piani regionali o linee guida regionali integrative.

Questa skill e' in versione 0.1.0-alpha: la validazione di Livello 2 (revisione da parte di un secondo ingegnere di dominio) non e' ancora stata effettuata.
