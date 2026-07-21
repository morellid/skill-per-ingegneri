---
name: valutazione-rischio-cancerogeni-mutageni-dlgs81
description: "Supporto documentale al RSPP/ASPP, al datore di lavoro e al tecnico della sicurezza per l'inquadramento della valutazione e gestione del rischio da agenti cancerogeni, mutageni e da sostanze tossiche per la riproduzione secondo il D.Lgs. 81/2008, Titolo IX, Capo II (artt. 233-243), nel testo vigente aggiornato dal D.Lgs. 135/2024. Aiuta a inquadrare il campo di applicazione (con l'esclusione dell'amianto del Capo III); le definizioni di agente cancerogeno e mutageno (categorie 1A/1B del regolamento CLP 1272/2008 e allegato XLII) e di sostanza tossica per la riproduzione (priva di soglia o con valore soglia, allegato XLIII), con il valore limite, il valore limite biologico e la sorveglianza sanitaria; la gerarchia di sostituzione e riduzione (sostituzione, sistema chiuso, riduzione al piu' basso valore tecnicamente possibile, rispetto del valore limite); la valutazione del rischio riportata e integrata nel DVR; le misure tecniche, organizzative, procedurali e igieniche (quantitativi minimi, limitazione degli esposti e aree con divieto di fumo, aspirazione localizzata, misurazione, smaltimento, servizi igienici, indumenti e DPI); l'informazione e la formazione con etichettatura CLP; la sorveglianza sanitaria e il registro di esposizione con le cartelle sanitarie e di rischio, l'invio all'INAIL e la conservazione. Use when a safety engineer, RSPP/ASPP or employer must frame the assessment and management of exposure to carcinogens, mutagens and reprotoxic substances at work under the Italian D.Lgs. 81/2008 Title IX Chapter II; it is a documentary aid and does NOT draft the risk assessment document (DVR), does NOT perform measurements or sampling, does NOT apply the exposure limit values, does NOT reproduce Annexes XLI/XLII/XLIII/XLIII-bis or the CLP/REACH regulations, does NOT cover asbestos (Chapter III) or chemical agents (Chapter I), and does NOT replace the employer, the RSPP or the occupational physician."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Rischio cancerogeni e mutageni sul lavoro (D.Lgs 81/2008 Titolo IX Capo II)"
summary: "Inquadra il rischio da agenti cancerogeni, mutageni e sostanze tossiche per la riproduzione (D.Lgs 81/2008 Titolo IX Capo II, artt. 233-243, agg. D.Lgs 135/2024): definizioni, sostituzione/riduzione, integrazione del DVR, misure, sorveglianza sanitaria e registro esposti."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 - Titolo IX, Capo II, artt. 233-243 (agenti cancerogeni, mutageni e sostanze tossiche per la riproduzione), testo vigente aggiornato dal D.Lgs. 4 settembre 2024, n. 135"
  - "Richiamati (non riprodotti): Allegati XLI/XLII/XLIII/XLIII-bis D.Lgs 81/2008; artt. 17, 18, 25, 28, 29, 42; Reg. CE 1272/2008 (CLP); D.M. 12/7/2007 n. 155"
version: 0.1.0-alpha
status: alpha
tags:
  - cancerogeni-mutageni
  - sostanze-tossiche-riproduzione
  - dlgs-81-2008
  - valutazione-rischio
  - sorveglianza-sanitaria
---

# Rischio cancerogeni, mutageni e tossici per la riproduzione (D.Lgs 81/2008 Titolo IX Capo II)

## Quando usare questa skill

Usala quando un **RSPP/ASPP**, un **datore di lavoro** o un **tecnico della sicurezza** deve
**inquadrare** la **valutazione e gestione del rischio** da **agenti cancerogeni, mutageni o sostanze
tossiche per la riproduzione** secondo il **D.Lgs. 81/2008, Titolo IX, Capo II (artt. 233-243)**, nel
testo vigente aggiornato dal **D.Lgs. 135/2024**:

- **campo di applicazione** e **definizioni** (§233, §234);
- **sostituzione e riduzione** e **valutazione del rischio** con integrazione del DVR (§235, §236);
- **misure** tecniche/organizzative/procedurali e igieniche, **informazione/formazione** (§237-239);
- **sorveglianza sanitaria** e **registro di esposizione** (§242, §243).

**Non è** uno strumento che redige il DVR, esegue misurazioni o applica i valori limite: è un **supporto
documentale** che inquadra obblighi, contenuti, gerarchia delle misure e adempimenti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-valutazione-misure-cancerogeni` | Campo di applicazione, definizioni, sostituzione/riduzione, valutazione del rischio e misure tecniche/organizzative/igieniche e informazione/formazione (artt. 233-239) |
| `inquadra-sorveglianza-registro-esposti` | Sorveglianza sanitaria, registro di esposizione e cartelle sanitarie e di rischio, invio all'INAIL e conservazione (artt. 242-243) |

## Punti chiave (verificati sul testo)

- **Campo** (§233): esposizione a cancerogeni/mutageni/tossici per la riproduzione; **escluso** l'amianto
  (Capo III).
- **Definizioni** (§234): cancerogeno/mutageno **cat. 1A/1B** (CLP Reg. CE 1272/2008) o **allegato XLII**;
  **sostanza tossica per la riproduzione** (priva di soglia / con valore soglia, allegato XLIII); valore
  limite, valore limite biologico, sorveglianza sanitaria.
- **Sostituzione/riduzione** (§235): **sostituzione** se possibile → **sistema chiuso** → riduzione **al
  più basso valore tecnicamente possibile**; esposizione **≤ valore limite** (allegato XLIII).
- **Valutazione** (§236): riportata nel **DVR (art. 17)** e **integrata** (art. 28 c. 2 / art. 29 c. 5)
  con attività, quantitativi, numero e grado di esposizione, misure/DPI, indagini di sostituzione.
- **Misure** (§237-238): quantitativi minimi; **limitazione degli esposti** e **aree con divieto di
  fumo**; **aspirazione localizzata**; **misurazione** (allegato XLI); servizi igienici, indumenti
  separati, DPI.
- **Informazione/formazione** (§239): **prima dell'adibizione** e ripetute **almeno ogni 5 anni**;
  etichettatura **CLP**.
- **Sorveglianza sanitaria** (§242): per i lavoratori con rischio; parere del **medico competente**;
  possibile **allontanamento** (art. 42).
- **Registro esposti** (§243): tenuto **tramite il medico competente**, **accesso RSPP/RLS**; cartella
  sanitaria e di rischio (art. 25); **invio all'INAIL** e conservazione (**40 anni** cancerogeni/mutageni,
  **≥5 anni** tossici per la riproduzione).

## Fonti

- **D.Lgs. 9 aprile 2008, n. 81** - **Titolo IX, Capo II, artt. 233-243** - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-17`, SHA256 `18fbc542...`, codice 008G0104), articoli letti via
  `caricaArticolo` (formato AKN) e trascritti verbatim (agg. D.Lgs. 135/2024).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il DVR né la valutazione del rischio; **non esegue** misurazioni o campionamenti; **non
  applica** i valori limite di esposizione.
- **Non riproduce** gli **Allegati XLI/XLII/XLIII/XLIII-bis** né i regolamenti **CLP/REACH**.
- **Non tratta** l'**amianto** (Capo III), gli **agenti chimici** (Capo I, skill
  `valutazione-rischio-chimico-dlgs81`) né gli **agenti biologici** (Titolo X).

**La skill è un supporto documentale: non sostituisce il datore di lavoro, l'RSPP o il medico competente,
né la lettura degli artt. 233-243 del D.Lgs. 81/2008 e dei relativi allegati.**
