---
name: ponti-zona-sismica-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le regole generali dei ponti in zona sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.9. Aiuta a inquadrare: il campo di applicazione del par. 7.9.1 (ponti a pile e travate, continue o semplicemente appoggiate, con pile a fusto unico); i criteri generali di progettazione del par. 7.9.2 (comportamento non dissipativo secondo il Capitolo 4, oppure dissipativo con meccanismo dissipativo stabile e dissipazione limitata alle pile, comportamento inelastico flessionale ed esclusione della rottura per taglio; pali di fondazione con sollecitazioni sismiche divise per 1,5 e dettagli CD\"B\" per dieci diametri; perdita dei copriferri allo 0,35 per cento; impalcato, apparecchi di appoggio, fondazioni e spalle mantenuti elastici); i valori del fattore di comportamento del par. 7.9.2.1 (q0 pari a 1,0 nel caso non dissipativo; nel caso dissipativo q0 dalla Tab. 7.3.II con lambda(alfa)=1 se alfa>=3 e (alfa/3)^0,5 se 3>alfa>=1, alfa=L/H; per gli elementi duttili di calcestruzzo armato q0 valido solo se la compressione normalizzata nu_k=NEd/(Ac fck) non supera 0,3 e comunque nu_k<=0,6, con q0 ridotto per valori intermedi; regolarita' con KR=1 se il rapporto rmax/rmin e' minore di 2 e KR=2/r altrimenti; ponti a geometria irregolare con q=1,5, fino a 3,5 solo con analisi non lineare); e il modello e i requisiti dell'analisi statica lineare dei par. 7.9.3-7.9.4.1 (eccentricita' accidentale 0,03 volte la dimensione dell'impalcato; attenzione ai moti rigidi per obliquita' oltre 20 gradi o B/L oltre 2,0; massa efficace delle pile non oltre un quinto della massa dell'impalcato). Use when a structural engineer must frame the general rules for bridges in seismic zones under the Italian NTC 2018 par. 7.9; it is a documentary aid, does NOT run the ductility/resistance verifications, does NOT design the details, and does NOT replace the designer. It is distinct from the traffic-load bridge skills (par. 5.1.3 and 5.2.2) and the behaviour-factor q skill for buildings (par. 7.3.1)."
license: MIT
area: strutture-geotecnica
title: "Ponti in zona sismica: regole generali (NTC 2018 par. 7.9)"
summary: "Inquadra le regole generali dei ponti in zona sismica (NTC 2018 par. 7.9): campo di applicazione (7.9.1), criteri dissipativo/non dissipativo (7.9.2), fattore q0/nu_k/lambda(alfa) e regolarita' KR (7.9.2.1), modello e analisi statica lineare (7.9.3-7.9.4.1)."
normative_refs:
  - "NTC 2018 - par. 7.9: pile/travate (7.9.1); dissip. pile, pali /1,5, copriferri 0,35% (7.9.2); q0=1 non diss., nu_k<=0,3/0,6, [7.9.1], KR=2/r (7.9.2.1); analisi statica lineare (7.9.3-7.9.4.1)"
  - "Rinvio (fuori scope): verifiche duttilita'/resistenza e dettagli (7.9.4-7.9.6); carichi traffico par. 5.1.3/5.2.2 e fattore q par. 7.3.1 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - ponti
  - zona-sismica
  - ntc-2018
  - fattore-comportamento
  - pile
---

# Ponti in zona sismica: regole generali (NTC 2018 par. 7.9)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le regole generali** dei **ponti in zona sismica**
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.9**:

- **campo di applicazione** (§7.9.1);
- **criteri generali** di progettazione, comportamento dissipativo/non dissipativo (§7.9.2);
- **valori del fattore di comportamento** q0, νk, λ(α) e regolarità KR (§7.9.2.1);
- **modello** e **analisi statica lineare** (§7.9.3-7.9.4.1).

È un **supporto documentale**: inquadra criteri, fattore di comportamento e requisiti dell'analisi; **non** esegue
le verifiche (duttilità/resistenza delle pile) né progetta i dettagli. È **distinta** dalle skill sui **carichi da
traffico** dei ponti (`azioni-traffico-ponti-stradali-ntc` §5.1.3, `azioni-traffico-ponti-ferroviari-ntc` §5.2.2)
e da `fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q per gli edifici).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-fattore-comportamento` | Campo di applicazione (§7.9.1), criteri dissipativo/non dissipativo (§7.9.2) e valori del fattore di comportamento q0/νk/λ(α) (§7.9.2.1) |
| `verifica-regolarita-requisiti-analisi` | Regolarità KR (§7.9.2.1), modello strutturale e requisiti dell'analisi statica lineare (§7.9.3-7.9.4.1) |

## Punti chiave (verificati sul testo/immagine)

- **Campo** (§7.9.1): ponti a **pile e travate** (continue o appoggiate); pile a **fusto unico**; q0 da Tab. 7.3.II.
- **Criteri** (§7.9.2): **non dissipativo** (Cap. 4; no curvatura di prima plasticizzazione / snervamento) o
  **dissipativo** (meccanismo stabile, **dissipazione limitata alle pile**, inelastico **flessionale**, no rottura
  per taglio). Pali: sollecitazioni **/1,5**, dettagli CD "B" per **10 diametri**. Perdita copriferri a **0,35%**.
  **Impalcato, appoggi, fondazioni, spalle** sempre elastici (progettazione in capacità).
- **Fattore di comportamento** (§7.9.2.1): non dissipativo **q0 = 1,0**; dissipativo q0 (Tab. 7.3.II) con
  **λ(α)=1 se α≥3**, **(α/3)^0,5 se 3>α≥1** (α=L/H); c.a. duttili solo se **νk = NEd/(Ac·fck) ≤ 0,3**, comunque
  **νk ≤ 0,6**, e per 0,3<νk<0,6 **q0(νk)=q0−[(νk/0,3)−1]·(q0−1)** [7.9.1]. **Regolarità**: **r̃<2 → KR=1**;
  **r̃≥2 → KR=2/r̃** [7.9.2]. Ponti irregolari: **q=1,5** (fino a **3,5** con analisi non lineare).
- **Modello/analisi** (§7.9.3-7.9.4.1): **eccentricità accidentale 0,03·dimensione impalcato**; attenzione ai
  moti rigidi per **obliquità φ>20°** o **B/L>2,0**; analisi statica lineare se massa efficace pila **≤ 1/5** massa
  impalcato ed eccentricità **≤ 5%**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.9** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 269-271 (q0, νk, λ(α), formula [7.9.1], KR/[7.9.2]).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche** di duttilità e di resistenza delle pile e dei dispositivi né i **metodi di
  analisi non lineare** (§§ 7.9.4-7.9.6).
- **Non progetta** i **dettagli costruttivi** (§7.9.6) né calcola il valore numerico di **q0** (Tab. 7.3.II).
- **Non tratta** i **carichi da traffico** (§§ 5.1.3/5.2.2, → skill dedicate) né il framework del **fattore q**
  per gli edifici (§7.3.1, → skill `fattore-comportamento-q-sismica-ntc`); **non** sostituisce il progettista.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.9 delle NTC 2018 e della relativa Circolare applicativa.**
