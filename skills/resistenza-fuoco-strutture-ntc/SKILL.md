---
name: resistenza-fuoco-strutture-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della resistenza al fuoco delle strutture secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.6.1 (Incendio). Aiuta a inquadrare le definizioni (capacita' portante R, tenuta E e isolamento I in caso di incendio; resistenza al fuoco; compartimento antincendio; carico d'incendio e carico d'incendio specifico di progetto qf,d uguale a qf per delta_q1 per delta_q2 per delta_n, con delta_q1 maggiore o uguale a 1,00 in funzione della superficie del compartimento, delta_q2 maggiore o uguale a 0,80 in funzione del tipo di attivita' e delta_n maggiore o uguale a 0,20 in funzione delle misure di protezione; il calcolo di dettaglio dei fattori e' nel DM 9 marzo 2007); le richieste di prestazione con i livelli da I a V della Tab. 3.5.IV (nessun requisito, evacuazione, gestione dell'emergenza, limitato danneggiamento, totale funzionalita'); le classi di resistenza al fuoco 15, 20, 30, 45, 60, 90, 120, 180, 240 e 360 minuti riferite alle curve nominali; e la procedura di analisi (individuazione dell'incendio di progetto con curva nominale o naturale, con la curva nominale standard theta_g uguale a 20 piu' 345 log10 di 8t piu' 1 in gradi Celsius, la curva degli idrocarburi e la curva esterna; analisi dell'evoluzione della temperatura; analisi del comportamento meccanico con le azioni della combinazione eccezionale; verifiche di sicurezza sul tempo pari alla classe). Use when a structural designer must frame the fire resistance of structures under the Italian NTC 2018 par. 3.6.1; it is a documentary aid and does NOT compute the fire load (the delta factors are in the DM 9 March 2007) nor run the thermal or mechanical analyses, does NOT provide the high-temperature material properties (Eurocodes part 1-2) nor the specific classes of the fire-brigade technical rules (Legislative Decree 139/2006), and does NOT replace the structural designer or the fire-safety professional. It is distinct from the fire-prevention procedure skill (DPR 151/2011)."
license: MIT
area: strutture-geotecnica
title: "Resistenza al fuoco delle strutture (NTC 2018 par. 3.6.1)"
summary: "Inquadra la resistenza al fuoco delle strutture (NTC 2018 par. 3.6.1): definizioni R/E/I, carico d'incendio qf,d=qf*dq1*dq2*dn, livelli di prestazione I-V (Tab. 3.5.IV), classi 15-360 min, curve nominali e verifiche in combinazione eccezionale."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.6.1: qf,d=qf*dq1*dq2*dn [3.6.1], livelli I-V (Tab. 3.5.IV), classi 15-360 min, curve nominali [3.6.2]-[3.6.4], verifiche in comb. eccezionale"
  - "Rinvio (fuori scope): DM 9 marzo 2007 (calcolo carico d'incendio), D.Lgs 139/2006 e regole tecniche VVF (classi/livelli), Eurocodici parte 1-2 (materiali ad alta temperatura), Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - resistenza-al-fuoco
  - incendio
  - ntc-2018
  - classi-rei
  - combinazione-eccezionale
---

# Resistenza al fuoco delle strutture (NTC 2018 par. 3.6.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare la resistenza al fuoco delle strutture** secondo
le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.1 (Incendio)**:

- **definizioni** (R, E, I; carico d'incendio) (§3.6.1.1);
- **richieste di prestazione** (Livelli I-V, Tab. 3.5.IV) (§3.6.1.2);
- **classi di resistenza al fuoco** (15…360 min) (§3.6.1.3);
- **procedura di analisi** e **verifiche** (curve nominali, combinazione eccezionale) (§3.6.1.5).

**Non è** uno strumento che calcola il carico d'incendio o esegue le analisi termiche/meccaniche: è un
**supporto documentale** che inquadra definizioni, prestazioni, classi, curve e criteri di verifica. È
**distinta** dalla skill `prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti amministrativi VVF).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-prestazioni-classi-fuoco` | Definizioni (R/E/I), carico d'incendio qf,d [3.6.1], livelli di prestazione (Tab. 3.5.IV) e classi 15-360 (§3.6.1.1-3.6.1.3) |
| `inquadra-analisi-verifica-fuoco` | Procedura di analisi: incendio di progetto (curve nominali [3.6.2]-[3.6.4]), evoluzione temperatura, comportamento meccanico e verifiche (§3.6.1.5) |

## Punti chiave (verificati sul testo)

- **Definizioni** (§3.6.1.1): **R** capacità portante, **E** tenuta, **I** isolamento; carico d'incendio
  specifico di progetto **qf,d = qf·δq1·δq2·δn** [3.6.1] (**δq1 ≥ 1,00**, **δq2 ≥ 0,80**, **δn ≥ 0,20**;
  dettaglio dei fattori nel **DM 9/3/2007**).
- **Prestazioni** (§3.6.1.2, Tab. 3.5.IV): **Livelli I-V** (I nessun requisito; II evacuazione; III gestione
  emergenza; IV limitato danneggiamento; V totale funzionalità). Per attività VVF → classi da D.Lgs 139/2006.
- **Classi** (§3.6.1.3): **15, 20, 30, 45, 60, 90, 120, 180, 240, 360** minuti (curve nominali).
- **Curve nominali** (§3.6.1.5.1): **standard θg = 20 + 345·log10(8t+1)** [3.6.2]; **idrocarburi** [3.6.3];
  **esterna** [3.6.4].
- **Analisi meccanica** (§3.6.1.5.3): riduzione della resistenza con la temperatura; azioni in **combinazione
  eccezionale**; no concomitanza con altre eccezionali/sisma.
- **Verifica** (§3.6.1.5.4): resistenza meccanica mantenuta per il **tempo pari alla classe** (curva nominale)
  o per l'intera durata (curva naturale).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** il carico d'incendio (i fattori δni sono nel **DM 9/3/2007**) né esegue le **analisi
  termiche/meccaniche**; **non** fornisce le proprietà dei materiali ad alta temperatura (**Eurocodici parte
  1-2**).
- **Non stabilisce** le **classi/livelli specifici** delle regole tecniche VVF (**D.Lgs 139/2006**, DM 3/8/2015
  RTO); **non** sostituisce il progettista strutturale né il professionista antincendio.
- **Non tratta** la prevenzione incendi come procedimento amministrativo (→ skill
  `prevenzione-incendi-attivita-procedimenti-dpr151`); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale né il professionista antincendio, né la lettura del par. 3.6.1 delle NTC 2018 e delle regole tecniche di prevenzione incendi.**
