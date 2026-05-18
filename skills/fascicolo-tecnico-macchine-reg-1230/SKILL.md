---
name: fascicolo-tecnico-macchine-reg-1230
description: Supporta la redazione e la verifica del fascicolo tecnico di una macchina, di un prodotto correlato o di una quasi-macchina ai sensi del Regolamento (UE) 2023/1230, inclusa la qualificazione del prodotto, la scelta della procedura di valutazione della conformita' (art. 25, Allegato I, moduli A/B/C/G/H), la checklist dei contenuti dell'Allegato IV parti A e B, e la struttura delle dichiarazioni UE (Allegato V parti A e B). Use when the user asks to draft, audit or check the technical file (fascicolo tecnico) of a machine, partly completed machinery (quasi-macchina) or related product under the new EU Machinery Regulation 2023/1230 (replacing Directive 2006/42/EC from 14 January 2027).
license: MIT
---

# Fascicolo tecnico macchine - Reg. UE 2023/1230

## Quando usare questa skill

Usala quando devi redigere o controllare il **fascicolo tecnico** (documentazione tecnica) di una macchina, di un prodotto correlato o di una quasi-macchina ai sensi del Regolamento (UE) 2023/1230 del 14 giugno 2023, in vista dell'immissione sul mercato o della messa in servizio a partire dal 14 gennaio 2027 (data di applicazione del regolamento e di abrogazione della direttiva 2006/42/CE).

Target utente: fabbricante (ufficio tecnico, responsabile prodotto), professionista incaricato (ingegnere meccanico, elettrico, dell'automazione, della sicurezza), consulente CE.

**Non** usarla per: prodotti immessi sul mercato prima del 14/01/2027 sotto la direttiva 2006/42/CE (regime transitorio dell'art. 52); macchine escluse dall'ambito dall'art. 2 par. 2 (es. armi, mezzi di trasporto, prodotti gia' coperti dalla 2014/35/UE o 2014/53/UE in modo esclusivo); valutazioni di sicurezza di dettaglio (categoria del sistema di comando, PL/SIL, scelta dei ripari) che richiedono norme armonizzate proprietary-paid e non sono nel perimetro di questa skill.

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica del fascicolo tecnico ai sensi del Reg. (UE) 2023/1230. **Non sostituisce il giudizio del professionista firmatario** ne' la responsabilita' del fabbricante per la conformita' del prodotto. La skill non produce documenti pronti al deposito o alla firma, non valuta l'applicabilita' di norme armonizzate specifiche al progetto, non legge il testo dell'Allegato III (RES) ne' delle norme armonizzate UNI/CEN richiamate dal regolamento (norme tecniche a pagamento non trascritte). La marcatura CE, la firma della dichiarazione UE di conformita' o di incorporazione e la conservazione decennale del fascicolo restano obbligo esclusivo del fabbricante (o del mandatario nei limiti del mandato).

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Qualificare il prodotto** (macchina, prodotto correlato, quasi-macchina, esclusione, modifica sostanziale): `tasks/qualifica-prodotto.md`.
- **Scegliere la procedura di valutazione della conformita'** (Modulo A, B+C, G, H; con o senza organismo notificato): `tasks/identifica-procedura-conformita.md`.
- **Strutturare il fascicolo tecnico** (indice dei contenuti All. IV parte A per macchine/prodotti correlati, All. IV parte B per quasi-macchine): `tasks/struttura-fascicolo-tecnico.md`.
- **Verificare la completezza del fascicolo** (audit puntuale lettera per lettera): `tasks/check-completezza-fascicolo.md`.
- **Strutturare la dichiarazione UE di conformita' o di incorporazione** (All. V parte A o B): `tasks/struttura-dichiarazione-ue.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera e di quale tipo di prodotto si tratta (macchina vs quasi-macchina).

## Processo generale

1. Identifica la sotto-attivita' desiderata e il tipo di prodotto (macchina/prodotto correlato/quasi-macchina).
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input elencati nel task.
4. Applica la procedura del task, citando sempre il riferimento normativo (articolo del Reg. 2023/1230 o lettera dell'Allegato IV/V).
5. Produci l'output nel formato atteso, in italiano.
6. Includi sempre il rinvio alla verifica e firma del professionista/fabbricante.

## Fonti normative

Riferimento unico: Regolamento (UE) 2023/1230 del Parlamento europeo e del Consiglio del 14 giugno 2023 - vedi `references/sources.yaml`. Il testo italiano integrale rilevante per la skill e' trascritto in `references/fonti/reg-ue-2023-1230-macchine.md`. La sintesi operativa (con citazione di articolo/allegato di provenienza) e' in `references/estratti/reg-ue-2023-1230-fascicolo-tecnico.md`.

## Limiti

Cosa questa skill NON fa:

- Non produce documenti auto-firmati ne' pronti al deposito.
- Non sostituisce verifiche di campo, prove, calcoli di progettazione, ne' la valutazione del rischio sostanziale (che resta del progettista).
- Non riproduce ne' interpreta il testo integrale dell'Allegato III (RES): la matrice dei RES applicabili e' a cura del progettista, leggendo direttamente l'Allegato III.
- Non valida se una specifica **norma armonizzata** UNI/CEN/CEI sia applicabile o copra tutti i RES pertinenti per il caso concreto. Le norme armonizzate sono proprietary-paid e fuori dal perimetro source-grounding del repo.
- Non determina **categoria di rischio elettrico, PL, SIL, categoria di sistema di comando di sicurezza**: rinvia alle norme armonizzate pertinenti (es. EN ISO 13849-1, EN 62061, EN 60204-1).
- Non si occupa del regime transitorio della direttiva 2006/42/CE (art. 52 del Reg. 2023/1230): per prodotti immessi sul mercato prima del 14 gennaio 2027 si applica la disciplina previgente.
- Non gestisce la procedura di **notifica dell'organismo notificato** (art. 26-42 del regolamento) ne' la scelta dell'ON: e' responsabilita' del fabbricante.
- Non sostituisce la consultazione di un consulente legale per gli aspetti contrattuali (mandato di rappresentanza ex art. 3 punto 19, contratti di subfornitura, responsabilita' verso terzi).
