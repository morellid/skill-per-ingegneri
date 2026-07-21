---
name: valutazione-rischio-biologico-dlgs81
description: "Supporto documentale al RSPP/ASPP, al datore di lavoro e al tecnico della sicurezza per l'inquadramento della valutazione e gestione del rischio da esposizione ad agenti biologici secondo il D.Lgs. 81/2008, Titolo X (artt. 266-280). Aiuta a inquadrare il campo di applicazione e le definizioni di agente biologico, microrganismo e coltura cellulare; la classificazione degli agenti biologici nei quattro gruppi a seconda del rischio di infezione (gruppo 1 poche probabilita', gruppo 2 malattie possibili con propagazione poco probabile e misure disponibili, gruppo 3 malattie gravi con propagazione possibile e misure disponibili, gruppo 4 malattie gravi con elevata propagazione e senza misure), con l'allegato XLVI e la regola del gruppo piu' elevato in caso di dubbio; la valutazione del rischio integrata nel DVR con la buona prassi microbiologica, la rivalutazione almeno triennale, le attivita' dell'allegato XLIV e il programma di emergenza per i gruppi 3 e 4; le misure tecniche, organizzative e procedurali (limitazione degli esposti, segnale di rischio biologico dell'allegato XLV, procedure di emergenza, smaltimento dei rifiuti) e le misure igieniche (servizi con docce, indumenti separati, DPI disinfettati, divieti nelle aree a rischio); la sorveglianza sanitaria con vaccini e allontanamento; e il registro degli esposti dei gruppi 3 e 4 e degli eventi accidentali, con la tenuta tramite l'RSPP, le comunicazioni all'organo di vigilanza e la conservazione fino a dieci o quaranta anni. Use when a safety engineer, RSPP/ASPP or employer must frame the assessment and management of exposure to biological agents at work under the Italian D.Lgs. 81/2008 Title X; it is a documentary aid and does NOT draft the risk assessment document (DVR), does NOT classify the individual agents, does NOT reproduce Annexes XLIV/XLV/XLVI or define containment levels, and does NOT replace the employer, the RSPP or the occupational physician."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Rischio da agenti biologici sul lavoro (D.Lgs 81/2008 Titolo X)"
summary: "Inquadra il rischio da agenti biologici (D.Lgs 81/2008 Titolo X, artt. 266-280): definizioni e classificazione nei 4 gruppi, valutazione del rischio e integrazione del DVR, misure tecniche e igieniche, sorveglianza sanitaria e registro degli esposti dei gruppi 3 e 4."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 - Titolo X, artt. 266-280 (esposizione ad agenti biologici: definizioni, classificazione in 4 gruppi, valutazione, misure, sorveglianza, registro esposti)"
  - "Richiamati (non riprodotti): Allegati XLIV/XLV/XLVI D.Lgs 81/2008; artt. 17, 41, 42; D.Lgs. 106/2009; ISPESL ora INAIL (L. 122/2010)"
version: 0.1.0-alpha
status: alpha
tags:
  - agenti-biologici
  - rischio-biologico
  - dlgs-81-2008
  - valutazione-rischio
  - sorveglianza-sanitaria
---

# Rischio da agenti biologici sul lavoro (D.Lgs 81/2008 Titolo X)

## Quando usare questa skill

Usala quando un **RSPP/ASPP**, un **datore di lavoro** o un **tecnico della sicurezza** deve
**inquadrare** la **valutazione e gestione del rischio** da **esposizione ad agenti biologici** secondo il
**D.Lgs. 81/2008, Titolo X (artt. 266-280)**:

- **definizioni** e **classificazione** degli agenti biologici in 4 gruppi (§267, §268);
- **valutazione del rischio** con integrazione del DVR (§271);
- **misure** tecniche/organizzative/procedurali e igieniche (§272, §273);
- **sorveglianza sanitaria** e **registro degli esposti** (§279, §280).

**Non è** uno strumento che redige il DVR o classifica i singoli agenti: è un **supporto documentale** che
inquadra classificazione, obblighi e adempimenti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classificazione-valutazione-biologico` | Campo, definizioni, classificazione in 4 gruppi, valutazione del rischio e misure tecniche/igieniche (artt. 266-273) |
| `inquadra-sorveglianza-registro-biologico` | Sorveglianza sanitaria (vaccini, allontanamento) e registro degli esposti e degli eventi accidentali (artt. 279-280) |

## Punti chiave (verificati sul testo)

- **Definizioni** (§267): agente biologico (microrganismo anche OGM, coltura cellulare, endoparassita
  umano) che può provocare **infezioni, allergie o intossicazioni**.
- **Classificazione** (§268): **4 gruppi** per rischio di infezione (1 poche probabilità; 2 malattie
  possibili, propagazione poco probabile, misure disponibili; 3 malattie gravi, propagazione possibile,
  misure disponibili; 4 malattie gravi, elevata propagazione, **niente** misure); in dubbio → **gruppo più
  elevato**; **allegato XLVI** per i gruppi 2/3/4.
- **Valutazione** (§271): integrata nel **DVR (art. 17)**; **buona prassi microbiologica**; **rivalutazione
  ogni 3 anni**; **allegato XLIV** (rischio potenziale); **programma di emergenza** per i gruppi **3/4**;
  **RLS consultato**.
- **Misure** (§272-273): limitare gli esposti, **segnale di rischio biologico** (allegato XLV), procedure
  di emergenza, smaltimento rifiuti; **docce**, indumenti separati, **DPI** disinfettati, divieti nelle
  aree a rischio.
- **Sorveglianza** (§279): **art. 41** se necessaria; **vaccini** per i non immuni; **allontanamento** (art.
  42).
- **Registro esposti** (§280): solo **gruppi 3/4**; tenuto **tramite l'RSPP**, accesso MC e RLS;
  conservazione **10 anni** (**40 anni** per agenti con infezioni latenti/gravi sequele).

## Fonti

- **D.Lgs. 9 aprile 2008, n. 81** - **Titolo X, artt. 266-280** - testo vigente su Normattiva (indice
  pinnato a `!vig=2026-07-17`, SHA256 `18fbc542...`, codice 008G0104), articoli letti via `caricaArticolo`
  (formato AKN) e trascritti verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il DVR né la valutazione del rischio; **non classifica** i singoli agenti biologici.
- **Non riproduce** gli **Allegati XLIV/XLV/XLVI** né definisce i **livelli di contenimento** (artt.
  274-275).
- **Non tratta** gli **agenti chimici** (Titolo IX Capo I, skill `valutazione-rischio-chimico-dlgs81`) né i
  **cancerogeni/mutageni** (Titolo IX Capo II, skill `valutazione-rischio-cancerogeni-mutageni-dlgs81`).

**La skill è un supporto documentale: non sostituisce il datore di lavoro, l'RSPP o il medico competente,
né la lettura degli artt. 266-280 del D.Lgs. 81/2008 e dei relativi allegati.**
