---
name: valutazione-cem-srb-art-87-cce
description: Supporto al professionista per la pratica di autorizzazione SRB (stazioni radio base, ripetitori, ponti radio) ex art. 87 D.Lgs. 259/2003 - check completezza istanza/SCIA, mapping iter (Ente locale + parere ARPA art. 14 L. 36/2001), verifica strutturale dei limiti CEM del DPCM 8/7/2003, redazione checklist per la relazione predittiva CEM (modelli CEI 211-7). Use when user is preparing or reviewing an art. 87 CCE application for a radioelectric installation in Italy.
license: MIT
---

# Valutazione CEM SRB - art. 87 CCE

## Quando usare questa skill

Questa skill aiuta l'ingegnere/tecnico abilitato che predispone o revisiona la pratica autorizzativa di una **infrastruttura per impianto radioelettrico** (stazione radio base GSM/UMTS/LTE/5G, ripetitore, ponte radio, rete a radiofrequenza in banda 100 kHz - 300 GHz) ai sensi dell'**art. 87 D.Lgs. 1 agosto 2003 n. 259** (Codice delle comunicazioni elettroniche - CCE), e che deve allegare la **valutazione predittiva CEM** secondo i limiti del **DPCM 8 luglio 2003**.

Target: ingegnere delle telecomunicazioni / tecnico operatore mobile / consulente CEM ARPA-side, che redige istanza Modello A allegato 13 oppure SCIA Modello B allegato 13 (impianti <= 20 W per singola antenna), o che valida una pratica gia' redatta prima del deposito.

NON usare questa skill per:
- Calcolo numerico predittivo CEM (la skill non sostituisce un software conforme CEI 211-7).
- Adempimenti relativi a esposizioni professionali dei lavoratori (D.Lgs. 81/2008 Titolo VIII Capo IV - fuori scope).
- Impianti radar o esposizioni pulsate (DPCM dedicato, non DPCM 8/7/2003 - vedi art. 1 c. 3 DPCM).
- Reti GSM-R ferroviarie (regime speciale art. 87 c. 3-bis CCE: l'installazione sul sedime ferroviario o in area immediatamente limitrofa procede con le modalita' degli impianti di sicurezza e segnalamento ferroviario - fuori scope di questa skill).

## Avvertenza

Questa skill e' uno strumento di **supporto** alla redazione/verifica della pratica art. 87 CCE. **Non sostituisce il giudizio del professionista firmatario** (ingegnere abilitato/tecnico competente CEM, e ARPA per il parere vincolante). L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill **non produce documenti pronti al deposito o alla firma**, **non calcola valori numerici di campo elettrico/magnetico/densita' di potenza**, e **non sostituisce la verifica del testo vigente** dell'art. 87 CCE su Normattiva (la fonte MIMIT catalogata in `references/sources.yaml` riflette il testo aggiornato fino al 2013-2014; modifiche successive - D.L. 76/2020 conv. L. 120/2020, D.Lgs. 8 novembre 2021 n. 207 - DEVONO essere verificate dall'utente per qualunque pratica da depositare).

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Check completezza istanza/SCIA art. 87**: quando l'utente chiede di verificare se una pratica art. 87 CCE e' completa (allegati, modello A o B, relazione CEM, parere ARPA, ecc.) -> leggere `tasks/check-completezza-istanza.md`.
- **Mapping iter procedurale art. 87**: quando l'utente chiede tempistiche, attori, soglie, procedure (Ente locale, ARPA, conferenza di servizi, silenzio-assenso, decadenza) -> leggere `tasks/mappa-iter-procedurale.md`.
- **Checklist relazione predittiva CEM**: quando l'utente chiede cosa deve contenere la relazione di valutazione predittiva CEM allegata alla pratica (rispetto al DPCM 8/7/2003 e alla CEI 211-7) -> leggere `tasks/checklist-relazione-cem.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input necessari (tipo impianto, potenza singola antenna, comune, banda, ecc.).
4. Applica la procedura del task, citando articoli/commi puntuali (mai "la legge dice in generale").
5. Produci output strutturato: lista di item con "OK / mancante / da verificare", riferimenti normativi, azioni del professionista.
6. Includi sempre nel report finale il rinvio alla **verifica del professionista firmatario** e alla **versione consolidata** dell'art. 87 su Normattiva.

## Fonti normative

Catalogate in `references/sources.yaml`. Estratti testuali in `references/estratti/`:
- `dlgs-259-2003-art-87.md` - art. 87 CCE (procedimento autorizzativo SRB), commi 1-10 + 3-bis.
- `dpcm-8-7-2003-limiti-cem.md` - DPCM 8/7/2003 (limiti, valori di attenzione, obiettivi di qualita' CEM 100 kHz - 300 GHz), articoli 1-7. Le Tabelle 1-3 dell'Allegato B (valori numerici) sono pubblicate come immagini in GU e NON sono riprodotte: la skill rinvia strutturalmente alle Tabelle e demanda al firmatario la verifica puntuale.

## Limiti

Cosa questa skill NON fa:
- Non produce documenti auto-firmati ne' relazioni CEM pronte al deposito.
- Non calcola valori numerici di E (V/m), H (A/m), S (W/m^2): demanda al software CEI 211-7 dell'utente.
- Non riproduce le Tabelle 1, 2, 3 dell'Allegato B DPCM 8/7/2003 (vincolo della fonte: pubblicate come immagine in GU).
- Non interpreta dissensi qualificati (art. 87 c. 8 CCE) ne' modifiche post-2014 dell'art. 87: rinvia alla verifica del testo consolidato su Normattiva.
- Non valida il regime speciale GSM-R ferroviario (art. 87 c. 3-bis CCE): fuori scope.
- Non gestisce le esposizioni pulsate / impianti radar (DPCM dedicato, non DPCM 8/7/2003).
- Non gestisce gli adempimenti di tutela del lavoratore (D.Lgs. 81/2008 Titolo VIII).
