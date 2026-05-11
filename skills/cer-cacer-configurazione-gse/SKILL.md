---
name: cer-cacer-configurazione-gse
description: Supporta un pre-check operativo per configurazioni CACER usando esclusivamente contenuti verificati sulle Regole Operative GSE e sui portali istituzionali GSE. Aiuta a verificare cabina primaria, soglia 1 MW, ruolo del referente, checklist di qualifica e stime parametriche prudenti dei flussi, senza sostituire il calcolo ufficiale o la domanda al GSE.
license: MIT
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
- pagina GSE sulle misure PNRR.

## Regole operative minime che la skill puo' usare

- i punti della configurazione incentivata devono stare nella stessa cabina primaria;
- il codice della cabina primaria va verificato e dichiarato tramite il portale GSE;
- per gli incentivi CACER l'impianto deve rispettare la soglia di 1 MW;
- i corrispettivi del servizio hanno durata ventennale secondo le Regole lette;
- il contributo PNRR, nel perimetro GSE letto, riguarda impianti in comuni con popolazione inferiore a 50.000 abitanti e segue un cronoprogramma e una rendicontazione specifici.

## Limiti

La skill non:
- sostituisce la mappa cabine del GSE;
- sostituisce il calcolo ufficiale dell'energia condivisa;
- fa consulenza legale su forma societaria o statuto;
- verifica cumulabilita' fiscali o altri incentivi fuori dalle Regole GSE lette.