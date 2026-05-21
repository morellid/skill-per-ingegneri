---
name: cer-cacer-configurazione-gse
description: Supporta un pre-check operativo per configurazioni CACER usando esclusivamente contenuti verificati sulle Regole Operative GSE e sui portali istituzionali GSE. Aiuta a verificare cabina primaria, soglia 1 MW, ruolo del referente, checklist di qualifica e stime parametriche prudenti dei flussi, senza sostituire il calcolo ufficiale o la domanda al GSE.
license: MIT
area: energia-incentivi
title: "Configurazione CER/CACER e Qualifica GSE"
summary: "Configurazione di CER (art. 31), GAC (art. 30 c. 2) o AID (art. 30 c. 1 lett. a n. 2): perimetro cabina primaria, statuto, simulazione energia condivisa/TIP/tariffa, contributo PNRR per Comuni <50k ab., checklist qualifica portale GSE."
normative_refs:
  - "D.Lgs. 199/2021 artt. 30-31-32"
  - "DM MASE 7/12/2023 n. 414"
  - "DM MASE 16/5/2025 n. 127"
  - "DL 19/2/2026 n. 19 art. 27"
  - "Delibera ARERA 727/2022/R/eel (TIAD)"
  - "Regole Operative CACER del GSE"
version: 0.2.0
status: alpha
tags:
  - cer
  - gse
  - dlgs-199-2021
---

# Configurazione CACER - pre-check operativo GSE

## Quando usare questa skill

Usala quando serve un supporto preliminare per:
- verificare se POD e impianti stanno nella stessa cabina primaria ai fini della configurazione incentivata;
- controllare i requisiti operativi minimi GSE (referente, soglia 1 MW, canale di domanda);
- costruire una checklist documentale per l'accesso al servizio;
- impostare una stima parametrica prudente dei flussi economici, chiarendo che il conteggio ufficiale e' del GSE.

## Avvertenza

Questa skill e' uno strumento di supporto e **non sostituisce** il giudizio del professionista firmatario, del referente o delle verifiche del GSE. Non produce domande pronte all'invio, non attribuisce in automatico la cabina primaria e non promette importi incentivanti.

## Sotto-attivita'

- verifica perimetro e prerequisiti GSE -> `tasks/valuta-perimetro-configurazione.md`
- impostazione di una stima parametrica -> `tasks/simula-autoconsumo-condiviso.md`
- checklist qualifica GSE -> `tasks/predisponi-qualifica-gse.md`
- promemoria per atto interno/referente -> `tasks/redigi-statuto-cer.md`

## Quadro verificato nelle fonti

La skill usa solo contenuti trascritti da:
- Regole Operative GSE CACER;
- Portale GSE Autoconsumo;
- pagina GSE sulle misure PNRR;
- notizie GSE del 12 maggio 2026 sui primi atti di concessione PNRR Facilities CACER;
- pagina GSE PNRR CER comuni <5000 ab. (bando e atti di concessione), letta il 18 maggio 2026.

## Regole operative minime che la skill puo' usare

- i punti della configurazione incentivata devono stare nella stessa cabina primaria;
- il codice della cabina primaria va verificato e dichiarato tramite il portale GSE;
- per gli incentivi CACER l'impianto deve rispettare la soglia di 1 MW;
- i corrispettivi del servizio hanno durata ventennale secondo le Regole lette;
- il contributo PNRR, nel perimetro GSE letto, riguarda impianti in comuni con popolazione inferiore a 50.000 abitanti e segue un cronoprogramma e una rendicontazione specifici.

## Stato aggiornato PNRR Facilities CACER (maggio 2026)

### Primi atti di concessione emessi (12 maggio 2026)

Il 12 maggio 2026 il GSE ha pubblicato i primi atti di concessione per la misura PNRR CACER (M2C2 Investimento 1.2 "Promozione rinnovabili per le comunita' energetiche e l'autoconsumo"), ai sensi dell'art. 27 del DL 19 febbraio 2026, n. 19 (DL PNRR). Fonte: notizia GSE del 12/05/2026.

Implicazioni operative per le configurazioni CACER in qualifica:
- Il GSE ha completato le verifiche previste (divieto doppio finanziamento, assenza conflitti di interesse, verifiche antimafia) per i primi beneficiari e ha avviato la fase contrattuale.
- I beneficiari ammessi devono prendere visione del proprio atto di concessione nella sezione CACER del sito GSE.
- Il GSE invia notifica via e-mail ai contatti registrati in fase di procedura.
- Gli atti dei successivi beneficiari saranno pubblicati nelle medesime sezioni.

### Scadenza stipula accordi di concessione: 30 giugno 2026

Dalla pagina GSE PNRR CER comuni <5000 ab. letta il 18 maggio 2026:

> "Entro il 30 giugno 2026, il GSE stipulera' accordi di concessione con i soggetti beneficiari fino a concorrenza della dotazione finanziaria."

Questa scadenza riguarda il completamento della fase contrattuale da parte del GSE, non la realizzazione dell'impianto. La scadenza per l'entrata in esercizio degli impianti e' il 31 dicembre 2027 (o entro 24 mesi dalla notifica dell'accordo di concessione, se precedente).

### Risorse richieste al 30 novembre 2025

Dalla stessa pagina GSE:

> "Le risorse richieste al 30 novembre 2025 ammontano a 1.456 Mln euro per una potenza degli impianti oggetto degli interventi per i quali e' stato richiesto il contributo di 3.343,8 MW."

### Nota sul contatore risorse PNRR M.7 I.17

Nella settimana 8-9 maggio 2026 il GSE ha comunicato prima la riattivazione (8 maggio) e poi l'esaurimento (9 maggio) del contatore delle risorse per la misura M.7 I.17 (efficientamento energetico edilizia residenziale pubblica). Tale misura e' distinta dalla misura PNRR CACER (M2C2 I.1.2): non influisce direttamente sulle configurazioni CER/CACER e sui relativi contributi in conto capitale.

## Limiti

La skill non:
- sostituisce la mappa cabine del GSE;
- sostituisce il calcolo ufficiale dell'energia condivisa;
- fa consulenza legale su forma societaria o statuto;
- verifica cumulabilita' fiscali o altri incentivi fuori dalle Regole GSE lette.