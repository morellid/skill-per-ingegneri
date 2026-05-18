---
name: pratiche-edilizie-lr65-2014-toscana
description: Supporta l'inquadramento preliminare del titolo edilizio in Toscana coordinando LR 65/2014, DPR 380/2001 e quadro sismico regionale. Aiuta a distinguere edilizia libera, CILA, SCIA e permesso di costruire e a costruire una checklist documentale prudente, senza sostituire la verifica sul testo vigente, sul regolamento regionale e sulle prescrizioni del Comune.
license: MIT
---

# Pratiche edilizie Toscana - inquadramento preliminare

## Quando usare questa skill

Usala quando serve un aiuto preliminare per:
- distinguere tra edilizia libera, CILA, SCIA e permesso di costruire per un intervento in Toscana;
- capire se la presenza di opere strutturali esclude la CILA;
- ricordare gli adempimenti sismici da verificare sul portale regionale;
- preparare una checklist documentale di base da completare con Comune e tecnico firmatario.

## Avvertenza

Questa skill e' uno strumento di supporto e **non sostituisce** il giudizio del professionista firmatario, del SUE/SUAP o del Genio Civile competente. I titoli edilizi dipendono anche dal testo vigente, dal regolamento comunale, dagli strumenti urbanistici e dagli atti di assenso esterni.

## Sotto-attivita'

- se l'utente chiede quale pratica serve -> `tasks/determina-tipo-pratica.md`
- se l'utente chiede quali allegati preparare -> `tasks/checklist-documenti.md`

## Quadro minimo verificato nelle fonti

- LR 65/2014: art. 134 (permesso di costruire), art. 135 (SCIA), art. 136 (attivita' edilizia libera), art. 137 (opere prive di rilevanza edilizia), art. 141 (rinvio al regolamento per la documentazione)
- DPR 380/2001: artt. 3, 6, 6-bis, 10, 22, 23, 23-ter, 93, 94
- Toscana: regolamento 1/R/2022 per la procedura sismica e pagina istituzionale regionale per la classificazione sismica dei comuni
- DL 66/2026 (Piano Casa, in vigore dall'8/05/2026): art. 8 co. 1 (SCIA per demolizione/ricostruzione ERP - Capo II), art. 8 co. 2 (conferenza servizi semplificata), art. 9 (edilizia integrata - Capo III, non modifica DPR 380/2001 artt. 10/22)

## Norma sopravvenuta: DL 66/2026 Piano Casa

Il DL 7 maggio 2026 n. 66 (GU n. 104, in vigore dall'8/05/2026) introduce misure rilevanti per specifiche categorie di intervento:

- **Demolizione e ricostruzione ERP (Capo II, art. 8 co. 1)**: per interventi di ristrutturazione urbanistica, edilizia o di demolizione/ricostruzione rientranti nel Capo II del DL 66/2026 (edilizia residenziale pubblica e sociale), si applica per rinvio la SCIA in luogo del PdC. La deroga non modifica il DPR 380/2001 art. 10 in via generale: opera solo per gli interventi del programma Piano Casa ERP.
- **Conferenza di servizi semplificata (art. 8 co. 2)**: gli interventi del comma 1 sono soggetti a conferenza di servizi semplificata ex L. 241/1990 art. 14-bis, con termine di 30 giorni (40 se presenti tutele art. 14-quinquies).
- **Edilizia integrata (Capo III, art. 9)**: il DL 66/2026 art. 9 introduce programmi infrastrutturali di edilizia integrata senza modificare i regimi edilizi ordinari (DPR 380/2001 artt. 10/22 restano invariati per l'edilizia privata ordinaria).
- **Direttive regionali**: la Regione Toscana potrebbe emanare direttive applicative; monitorare il portale regionale.

## Regole operative essenziali

- se l'intervento riguarda solo manutenzione ordinaria o opere minori tipizzate, verifica se puo' rientrare in edilizia libera;
- se l'intervento non tocca parti strutturali, verifica l'ipotesi CILA;
- se l'intervento interessa parti strutturali e non ricade nel permesso di costruire, orienta verso SCIA;
- se l'intervento e' nuova costruzione o ristrutturazione piu' incisiva, orienta verso permesso di costruire o SCIA alternativa nei casi tassativi;
- per ogni intervento strutturale ricorda sempre gli adempimenti sismici ex DPR 380/2001 e il rinvio al quadro regionale toscano.

## Limiti

La skill non:
- determina automaticamente la zona sismica del comune;
- sostituisce la lettura del Piano Operativo o del regolamento edilizio comunale;
- istruisce pratiche paesaggistiche, beni culturali o altre autorizzazioni specialistiche;
- redige asseverazioni o relazioni tecniche firmabili.