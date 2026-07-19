---
name: dop-marcatura-ce-prodotti-cpr
description: "Supporto documentale al fabbricante, all'ufficio tecnico-qualita' e al tecnico per l'inquadramento della redazione della Dichiarazione di Prestazione (DoP) e dell'apposizione della marcatura CE dei prodotti da costruzione secondo il Regolamento (UE) n. 305/2011 (CPR). Aiuta a inquadrare quando la DoP e' obbligatoria (prodotto che rientra in una norma armonizzata o con una valutazione tecnica europea) e le deroghe dell'articolo 5 (esemplare unico o su ordinazione non in serie, fabbricazione in cantiere, metodi tradizionali o di conservazione del patrimonio); il contenuto della DoP secondo l'articolo 6 e il modello dell'Allegato III (riferimento del prodotto-tipo, sistema o sistemi di valutazione e verifica della costanza della prestazione dell'Allegato V, norma armonizzata o valutazione tecnica europea, uso previsto, elenco delle caratteristiche essenziali, prestazione espressa in livelli, classi o descrizione, e la sigla NPD, nessuna prestazione determinata, per le caratteristiche non dichiarate), con le informazioni REACH da fornire assieme, e la fornitura della DoP in forma cartacea, elettronica o su sito web; le regole di apposizione della marcatura CE degli articoli 8 e 9 (marcatura apposta solo se e' stata redatta la DoP, marcatura unica di conformita', e gli elementi che seguono la marcatura: anno, nome e indirizzo del fabbricante, codice del prodotto-tipo, numero della DoP, livello o classe della prestazione, riferimento alla specifica tecnica armonizzata, numero dell'organismo notificato e uso previsto); i sistemi di valutazione e verifica della costanza della prestazione dell'Allegato V (sistemi 1+, 1, 2+, 3 e 4, con i compiti del fabbricante, del controllo della produzione in fabbrica e dell'organismo notificato di certificazione del prodotto, di certificazione del controllo della produzione o del laboratorio di prova); e gli obblighi degli operatori economici degli articoli 11-16 (fabbricante con la documentazione tecnica conservata per dieci anni, mandatario che non redige la documentazione tecnica, importatore, distributore, e la regola per cui chi immette col proprio nome o marchio o modifica il prodotto assume gli obblighi del fabbricante). Use when a manufacturer or a technician must frame the drafting of the Declaration of Performance (DoP) and the CE marking of construction products under the EU Regulation 305/2011 (CPR); it is a documentary aid and does NOT draft the DoP, does NOT identify the applicable harmonised standard or the product's assessment and verification system, does NOT run tests or assessments, does NOT cover in detail the European Technical Assessment (art. 19-27) nor the notified bodies (art. 39-56), and does NOT replace the product harmonised standard or the manufacturer."
license: MIT
area: impianti-macchine-prodotti
title: "DoP e marcatura CE dei prodotti da costruzione (Reg. UE 305/2011)"
summary: "Inquadra la redazione della Dichiarazione di Prestazione (DoP) e la marcatura CE dei prodotti da costruzione (Reg. UE 305/2011): obbligo e deroghe (artt. 4-5), contenuto DoP (art. 6, NPD), marcatura CE (artt. 8-9), sistemi VVCP (All. V) e obblighi degli operatori (artt. 11-16)."
normative_refs:
  - "Reg. (UE) n. 305/2011 (CPR) - artt. 4-9 (DoP e marcatura CE), artt. 11-16 (obblighi operatori economici), Allegato III (modello DoP), Allegato V (sistemi VVCP 1+/1/2+/3/4)"
  - "Rinvio (non riprodotti): Reg. delegato (UE) 574/2014 (modello DoP aggiornato); artt. 19-27 (ETA/EAD) e 39-56 (organismi notificati) CPR; norme armonizzate hEN; Reg. 765/2008 e 1907/2006 (REACH)"
version: 0.1.0-alpha
status: alpha
tags:
  - marcatura-ce
  - dichiarazione-di-prestazione
  - prodotti-da-costruzione
  - cpr-305-2011
  - vvcp
---

# Dichiarazione di Prestazione (DoP) e marcatura CE prodotti da costruzione (Reg. UE 305/2011)

## Quando usare questa skill

Usala quando un **fabbricante**, un **ufficio tecnico-qualità** o un **tecnico** deve **inquadrare** la
**redazione della Dichiarazione di Prestazione (DoP)** e l'**apposizione della marcatura CE** di un
**prodotto da costruzione** secondo il **Regolamento (UE) n. 305/2011 (CPR)**:

- **obbligo** e **deroghe** alla DoP (artt. 4-5);
- **contenuto** della DoP e **modello** (art. 6, Allegato III) e **fornitura** (art. 7);
- **marcatura CE**: principi e apposizione (artt. 8-9);
- **sistemi VVCP** (Allegato V) e **obblighi** degli operatori economici (artt. 11-16).

**Non è** uno strumento che redige la DoP, individua la norma armonizzata o il sistema VVCP del prodotto, né
esegue prove: è un **supporto documentale** che inquadra requisiti, contenuti e procedura.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-contenuto-dop` | Obbligo e deroghe della DoP, contenuto (art. 6), modello Allegato III (NPD) e fornitura (artt. 4-7) |
| `inquadra-marcatura-ce-vvcp` | Marcatura CE (artt. 8-9), sistemi VVCP (All. V) e obblighi degli operatori economici (artt. 11-16) |

## Punti chiave (verificati sul testo)

- **Obbligo DoP** (art. 4): quando il prodotto rientra in una **norma armonizzata (hEN)** o ha una
  **valutazione tecnica europea (ETA)**. **Deroghe** (art. 5): esemplare unico/non in serie, cantiere,
  metodi tradizionali/patrimonio.
- **Contenuto DoP** (art. 6): prodotto-tipo, sistema/i **VVCP** (All. V), hEN/ETA, uso previsto,
  caratteristiche essenziali, prestazione in livelli/classi/descrizione, **«NPD»** per le non dichiarate;
  modello **Allegato III**; info **REACH**.
- **Marcatura CE** (artt. 8-9): apposta **solo se redatta la DoP**; **unica** marcatura di conformità;
  seguita da anno, fabbricante, codice prodotto-tipo, n. DoP, livello/classe, specifica tecnica armonizzata,
  n. organismo notificato, uso previsto.
- **Sistemi VVCP** (All. V): **1+** e **1** (certificazione del prodotto → certificato di costanza della
  prestazione; nel 1+ anche prove audit su campioni), **2+** (certificazione del FPC), **3** (laboratorio di
  prova), **4** (solo fabbricante).
- **Operatori** (artt. 11-16): fabbricante (DoP + documentazione tecnica, **10 anni**); mandatario (no
  documentazione tecnica); importatore; distributore; **art. 15** (nome/marchio proprio o modifica →
  obblighi del fabbricante).

## Fonti

- **Regolamento (UE) n. 305/2011 (CPR)** - GU UE L 88 del 4.4.2011 - testo EUR-Lex (CELEX 32011R0305, SHA256
  `2e98d2f0...`), estratto con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** la DoP; **non individua** la norma armonizzata applicabile né il **sistema VVCP** del
  prodotto (dipendono dalla hEN/decisione della Commissione); **non esegue** prove né valutazioni.
- **Non tratta** in dettaglio la **ETA** (artt. 19-27) né gli **organismi notificati** (artt. 39-56); **non
  riproduce** il modello di DoP aggiornato dal **Reg. delegato (UE) 574/2014**.

**La skill è un supporto documentale: non sostituisce la norma armonizzata di prodotto, il fabbricante, né la lettura del Reg. UE 305/2011 e dei suoi allegati.**
