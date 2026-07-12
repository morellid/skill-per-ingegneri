---
name: cedimenti-edometrici-ntc
description: Calcolo code-driven del cedimento di consolidazione primaria (compressione monodimensionale) e verifica documentale delle verifiche SLE sui cedimenti in ambito NTC 2018. Il quadro delle verifiche viene da NTC 2018 par. 6.2.4.3 (Ed <= Cd) e Circolare 7/2019; la formulazione di calcolo viene dal manuale FHWA NHI-06-088 par. 7.5.2 (eq. 7-2 NC, 7-4 OC con pf > pc, 7-6 sottoconsolidato), fonte in pubblico dominio usata come altro codice internazionale ai sensi del cap. 12 NTC 2018. Dato per ogni strato h0, e0, Cc, Cr, sigma_0', sigma_p', delta_sigma' restituisce OCR, caso (NC/OC/UC), equazione applicata e S in m e mm, con rifiuto esplicito dei casi non coperti (OC con sigma_f <= sigma_p; OCR < 1 non dichiarato sottoconsolidato). Use when an Italian geotechnical or structural engineer needs a preliminary primary consolidation settlement estimate or a completeness check of an SLE settlement verification; the skill does not replace geotechnical modelling.
license: MIT
area: strutture-geotecnica
title: "Cedimenti edometrici - SLE NTC 2018 par. 6.2.4"
summary: "Calcolo code-driven del cedimento di consolidazione primaria (FHWA NHI-06-088 par. 7.5.2, eq. 7-2/7-4/7-6, codice internazionale ex cap. 12 NTC 2018) + verifica documentale della verifica SLE cedimenti (NTC 6.2.4.3): OCR, caso NC/OC/UC, S in mm, casi non coperti rifiutati"
normative_refs:
  - "NTC 2018 par. 6.2.4.3 + cap. 12"
  - "Circolare 7/2019"
  - "FHWA NHI-06-088 (2006) par. 7.5.2"
version: 0.2.0
status: alpha
tags:
  - ntc-2018
  - geotecnica
  - cedimenti
  - code-driven
---

# Cedimenti edometrici - calcolo e verifica documentale (NTC 2018 + FHWA NHI-06-088)

## Quando usare questa skill

Usare quando un ingegnere geotecnico o strutturista italiano deve:

- **Calcolare in via preliminare il cedimento di consolidazione primaria** di uno o piu' strati/sublayer, con le equazioni del FHWA NHI-06-088 par. 7.5.2 ([7-2] normalconsolidato, [7-4] sovraconsolidato con sigma_f > sigma_p, [7-6] sottoconsolidato dichiarato), usate come "altro codice internazionale" ai sensi del **cap. 12 NTC 2018**.
- **Verificare una relazione o nota di calcolo** rispetto al quadro SLE delle NTC (prestazioni attese, spostamenti compatibili, metodo di interazione terreno-struttura, confronto Ed <= Cd - § 6.2.4.3).
- **Verificare valori** prodotti da fogli di calcolo o software geotecnici.

**Non usare** quando l'utente chiede:

- Il calcolo della **diffusione delle tensioni** (delta_sigma' e' un input), la determinazione di **sigma_p'** dalla curva edometrica, i **tempi di consolidazione** (FHWA 7.5.3), la **compressione secondaria** (FHWA 7.5.4) o il cedimento immediato: fuori ambito.
- Il caso **OC con sigma_f <= sigma_p**: le equazioni trascritte dalla fonte valgono per pf > pc; la skill rifiuta il caso invece di inventare la formula.
- La **modellazione geotecnica** completa o la scelta del metodo al posto del progettista.

## Avvertenza

Questa skill e' uno strumento di supporto e **non sostituisce il giudizio del professionista firmatario** ne' il calcolo geotecnico di progetto. La formulazione di calcolo proviene da un codice internazionale (FHWA NHI-06-088) utilizzato ai sensi del cap. 12 NTC 2018, che pone in capo al progettista la responsabilita' di "garantire espressamente livelli di sicurezza coerenti" con le NTC. Il risultato va sempre confrontato con il limite Cd dichiarato dal progetto (NTC § 6.2.4.3, Ed <= Cd [6.2.7]).

## Sotto-attivita' disponibili

- **Calcolo del cedimento di consolidazione primaria**: l'utente chiede "calcolami il cedimento", "che cedimento da' questo strato?", "OCR e ramo di consolidazione", fornisce h0/e0/Cc/Cr/tensioni -> leggi [`tasks/calcola-cedimento-edometrico.md`](tasks/calcola-cedimento-edometrico.md). Usa SEMPRE il modulo [`tasks/lib/cedimento_edometrico.py`](tasks/lib/cedimento_edometrico.py) (test in [`tasks/lib/test_cedimento_edometrico.py`](tasks/lib/test_cedimento_edometrico.py)): mai calcoli a mano.
- **Verifica documentale della verifica SLE cedimenti**: l'utente incolla una relazione/nota di calcolo e chiede "e' completa?", "e' impostata bene rispetto alle NTC?" -> leggi [`tasks/check-verifica-cedimenti.md`](tasks/check-verifica-cedimenti.md).

## Processo generale

1. Identifica la sotto-attivita' (calcolo vs verifica documentale).
2. Per il calcolo: raccogli i dati per strato (valori al centro, sublayer 1,5-3 m - FHWA 7.5.2.2), esegui il modulo, riporta JSON e avvertenze integralmente.
3. **Cita sempre** l'equazione FHWA applicata per strato ([7-2]/[7-4]/[7-6], par. 7.5.2) e l'aggancio normativo (cap. 12 + § 6.2.4.3 NTC).
4. Rifiuta i casi non coperti con il messaggio del modulo, senza aggirarlo.
5. Concludi con i limiti (primaria soltanto; delta_sigma' e sigma_p' input del progettista) e il rinvio al progettista firmatario.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti (scaricate, hashate e trascritte in [`references/fonti/`](references/fonti/)):

- **DM 17 gennaio 2018 (NTC 2018)** - § 6.2.4.3 (verifiche SLE) e cap. 12 (riferimenti tecnici / altri codici internazionali) - [`ntc2018-dm-17-01-2018.md`](references/fonti/ntc2018-dm-17-01-2018.md)
- **Circolare 7/2019 C.S.LL.PP.** - C6.2 - [`circ-7-2019-mit.md`](references/fonti/circ-7-2019-mit.md)
- **FHWA NHI-06-088 "Soils and Foundations - Reference Manual Volume I"** (U.S. DOT, 2006, pubblico dominio, "No restrictions") - par. 7.5.2 (eq. 7-2..7-7) e 5.4.6.1 - [`fhwa-nhi-06-088.md`](references/fonti/fhwa-nhi-06-088.md)

Estratti in [`references/estratti/`](references/estratti/): [`fhwa-consolidazione-primaria.md`](references/estratti/fhwa-consolidazione-primaria.md), [`ntc2018-par-6-2.md`](references/estratti/ntc2018-par-6-2.md), [`circ-7-2019-c-6-2.md`](references/estratti/circ-7-2019-c-6-2.md).

## Limiti

Cosa questa skill NON fa:

- Non calcola **delta_sigma'** (diffusione delle tensioni) ne' determina **sigma_p'** dalla curva edometrica (correzione Table 7-6a FHWA: richiamata, non implementata).
- Non calcola **decorso nel tempo** (FHWA 7.5.3), **compressione secondaria** (FHWA 7.5.4), cedimenti immediati o differenziali.
- Non copre **OC con sigma_f <= sigma_p** (le eq. 7-4/7-5 della fonte valgono per pf > pc): caso rifiutato.
- Non accetta **OCR < 1** senza dichiarazione esplicita di sottoconsolidazione reale (eq. 7-6, da giustificare).
- Non usa le **correlazioni per Cc** (FHWA Table 5-5) nel calcolo: solo sanity check, "should not be used for final design" (par. 5.4.6.1).
- Non verifica **Ed <= Cd**: il limite Cd e' del progetto (§ 6.2.4.3).
- Non sceglie il metodo geotecnico al posto del progettista e non sostituisce prove, modellazione o relazione geologica.

**Ogni output e' supporto al progettista, non sostituzione.**
