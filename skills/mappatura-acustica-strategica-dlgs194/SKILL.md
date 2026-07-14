---
name: mappatura-acustica-strategica-dlgs194
description: "Supporto documentale agli obblighi di mappatura acustica strategica e piani d'azione contro il rumore ambientale ai sensi del D.Lgs. 194/2005 (attuazione della direttiva 2002/49/CE). Aiuta a determinare l'applicabilita' in base alle soglie (agglomerati oltre 100.000 abitanti, aeroporti oltre 50.000 movimenti/anno, assi ferroviari oltre 30.000 treni/anno, assi stradali oltre 3.000.000 di veicoli/anno), a individuare il soggetto obbligato (autorita' regionale per gli agglomerati, gestori per le infrastrutture), i due deliverable (mappe acustiche strategiche art. 3 e piani d'azione art. 4), le scadenze quinquennali, i descrittori Lden/Lnight, l'informazione del pubblico (osservazioni entro 45 giorni) e le sanzioni. Use when an Italian public authority, infrastructure operator or environmental engineer needs the D.Lgs. 194/2005 strategic noise mapping and action plan obligations, thresholds and deadlines; it is a documentary aid and does not produce the maps or plans nor run the acoustic modelling."
license: MIT
area: ambiente-territorio-mobilita
title: "Mappatura acustica strategica e piani d'azione - D.Lgs. 194/2005"
summary: "Obblighi di mappatura acustica strategica e piani d'azione contro il rumore ambientale (D.Lgs. 194/2005, dir. 2002/49/CE): soglie (agglomerati >100k, assi/aeroporti principali), soggetti obbligati, deliverable art. 3/4, scadenze quinquennali, sanzioni; supporto documentale"
normative_refs:
  - "D.Lgs. 19/8/2005 n. 194 (testo vigente) - artt. 1-11 (attuazione dir. 2002/49/CE)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-194-2005
  - rumore-ambientale
  - mappatura-acustica-strategica
  - piani-azione
  - direttiva-2002-49-ce
---

# Mappatura acustica strategica e piani d'azione - D.Lgs. 194/2005

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi del **D.Lgs. 194/2005** (rumore
ambientale, recepimento della direttiva 2002/49/CE):

- determinare l'**applicabilita'** in base alle soglie (agglomerati, aeroporti,
  assi stradali/ferroviari principali);
- individuare il **soggetto obbligato** (autorita' regionale per gli agglomerati;
  societa'/enti gestori per le infrastrutture);
- distinguere i due deliverable: **mappe acustiche strategiche** (art. 3) e
  **piani d'azione** (art. 4);
- ricostruire le **scadenze quinquennali** e gli obblighi di **informazione del
  pubblico** e le **sanzioni**.

Target: enti locali e regioni, gestori di infrastrutture di trasporto, ingegneri
e consulenti acustici/ambientali.

## Avvertenza

Questa skill e' un **supporto documentale** basato sul testo vigente del D.Lgs.
194/2005. **Non produce** le mappe acustiche strategiche ne' i piani d'azione,
**non esegue** la modellazione acustica (Lden/Lnight, CNOSSOS-EU), **non
riproduce** gli allegati tecnici (1-6) e **non sostituisce** l'autorita'
competente, il gestore o il tecnico acustico.

## Sotto-attivita' disponibili

- **Diagnosi di applicabilita' e obblighi**: dato l'elemento (agglomerato/asse/
  aeroporto), determina soglie, soggetto obbligato, deliverable e scadenze ->
  `tasks/diagnosi-applicabilita.md`
- **Checklist mappe/piani e informazione del pubblico**: verifica gli adempimenti
  (contenuti minimi, scadenze, consultazione) -> `tasks/checklist-adempimenti.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input (tipo di elemento, dati di traffico/popolazione, ruolo).
4. Applica le soglie/scadenze **citando l'articolo preciso** (artt. 1-11).
5. Chiudi con il rinvio all'autorita' competente e al tecnico acustico.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dlgs-194-2005.md` (testo vigente da Normattiva, pagina indice
pinnata `!vig=2026-07-14`), estratto operativo in
`references/estratti/mappatura-acustica-checklist.md`.

## Limiti

Cosa questa skill NON fa:
- non produce le mappe acustiche strategiche ne' i piani d'azione;
- non esegue la modellazione acustica ne' il calcolo di Lden/Lnight (CNOSSOS-EU,
  dir. (UE) 2015/996);
- non riproduce gli allegati tecnici 1-6 (descrittori, metodi, requisiti minimi,
  dati);
- non copre l'inquinamento acustico "ordinario" della L. 447/1995 (classificazione
  acustica, impatto/clima acustico) oltre ai richiami: per quello vedi la skill
  `valutazione-impatto-clima-acustico-l-447`.
