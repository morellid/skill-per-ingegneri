---
name: cra-segnalazione-art14
description: Guida il fabbricante di un prodotto con elementi digitali (PDE) negli obblighi di segnalazione dell'art. 14 del Regolamento (UE) 2024/2847 (Cyber Resilience Act), applicabili dall'11 settembre 2026. Use when an engineer, product security engineer or compliance manager must decide whether a discovered vulnerability qualifies as "actively exploited" or an event as a "severe incident", which deadlines apply (24h early warning, 72h notification, 14-day final report for vulnerabilities, one-month final report for incidents), what minimum content each submission must carry, which coordinator CSIRT is territorially competent, and which internal artefacts (CVD policy, SBOM, single point of contact, incident log) must be in place beforehand.
license: MIT
area: software-dati-cybersecurity
title: "CRA - Segnalazione di vulnerabilita' e incidenti (art. 14)"
summary: "Qualificazione di vulnerabilita' attivamente sfruttate e incidenti gravi ex art. 14 Reg. UE 2024/2847 (CRA), scadenze 24h/72h/14gg/un mese, contenuto minimo delle notifiche, CSIRT coordinatore competente e prerequisiti interni. Obbligo applicabile dall'11 settembre 2026."
normative_refs:
  - "Reg. UE 2024/2847 (Cyber Resilience Act) artt. 3, 13, 14, 15, 16, 17, 64, 71, allegato I parte II"
  - "Dir. UE 2022/2555 (NIS2) art. 6 punti 5-6, art. 12 par. 1"
  - "D.Lgs. 138/2024 artt. 2, 15, 16 (CSIRT Italia coordinatore CVD)"
version: 0.1.0-alpha
status: alpha
tags:
  - cra
  - reg-ue-2024-2847
  - cyber
  - nis2
  - vulnerability-disclosure
  - incident-reporting
---

# CRA - Segnalazione di vulnerabilita' e incidenti (art. 14)

## Quando usare questa skill

Quando un **fabbricante di un prodotto con elementi digitali (PDE)** - in pratica il
security engineer, il PSIRT, l'ingegnere di prodotto o firmware, il compliance manager -
deve gestire un evento di sicurezza sotto l'**art. 14 del Regolamento (UE) 2024/2847
(Cyber Resilience Act)**, i cui obblighi di segnalazione si applicano **dall'11 settembre
2026** (art. 71, par. 2).

Casi tipici:

- e' arrivata una segnalazione (ricercatore esterno, threat intel, log di campo) e serve
  decidere **se scatta l'obbligo** e da quando decorrono le 24 ore;
- l'obbligo e' scattato e serve costruire la **sequenza degli adempimenti** e il
  **contenuto minimo** di ciascuno;
- serve capire **a quale CSIRT** notificare, dato lo stabilimento del fabbricante;
- si sta preparando l'azienda in vista dell'11 settembre 2026 e serve un **check dei
  prerequisiti interni** (policy CVD, punto di contatto unico, SBOM, registro).

Quando **non** usarla:

- Classificazione del PDE (default / importante Classe I-II / critico), scelta del modulo
  di valutazione della conformita', documentazione tecnica dell'allegato VII: usa
  `cra-classificazione-pde`.
- Notifiche di incidente dovute ai sensi del **D.Lgs. 138/2024** (recepimento NIS2). Sono
  un regime distinto, con presupposti, termini e destinatari propri. Questa skill non li
  copre, non ha letto le disposizioni che ne definiscono l'ambito soggettivo, e non
  stabilisce equivalenze fra i due regimi.
- Progettazione tecnica dei controlli di sicurezza dell'allegato I, parte I (hardening,
  crittografia, gestione degli accessi).
- Analisi tecnica della vulnerabilita' in se' (triage CVSS, reverse engineering,
  sviluppo della patch). La skill inquadra l'adempimento, non sostituisce il lavoro di
  security engineering.
- Redazione della segnalazione in un formato imposto da un atto di esecuzione della
  Commissione: l'art. 14, par. 10, lo prevede come facolta' della Commissione, ma questa
  skill non ha verificato ne' letto eventuali atti adottati in base a quel paragrafo.
  Verificarne l'esistenza prima di fissare un formato.

## Avvertenza

Questa skill e' uno strumento di supporto alla qualificazione e alla tracciatura di un
adempimento normativo. **Non sostituisce il giudizio del responsabile della conformita'
del fabbricante ne' la consulenza legale.** Non trasmette alcuna notifica, non accede
alla piattaforma unica di segnalazione, non produce documenti pronti all'invio. La
decisione se un evento sia una vulnerabilita' attivamente sfruttata o un incidente grave,
e la responsabilita' della notifica, restano interamente del fabbricante.

Due limiti di contesto vanno tenuti presenti a ogni uso:

1. **La disponibilita' operativa della piattaforma unica di segnalazione (art. 16) non e'
   accertata da questa skill.** L'art. 71, par. 2, anticipa all'11 settembre 2026 il solo
   art. 14 e il capo IV; l'art. 16 ricade nella data generale dell'11 dicembre 2027. Il
   Regolamento non disciplina il periodo intermedio. Prima di costruire una procedura
   aziendale sul canale di invio, **verifica lo stato della piattaforma e del terminale
   nazionale sui canali ufficiali ENISA e ACN/CSIRT Italia**.
2. **Le fonti lette non descrivono la procedura di registrazione o di accesso alla
   piattaforma.** Chi cerca istruzioni di onboarding non le trovera' qui, perche' non
   sono nel testo del Regolamento.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Qualificare l'evento e capire se scatta l'obbligo**: quando l'utente descrive una
  vulnerabilita' o un evento e chiede "devo segnalare?", leggere
  `tasks/qualifica-evento-segnalabile.md`.
- **Costruire la sequenza degli adempimenti e il contenuto delle notifiche**: quando
  l'obbligo e' gia' accertato e serve la timeline con i contenuti minimi, leggere
  `tasks/costruisci-sequenza-notifiche.md`.
- **Individuare il CSIRT coordinatore competente**: quando serve stabilire a quale
  terminale nazionale indirizzare la notifica, leggere
  `tasks/individua-csirt-coordinatore.md`.
- **Verificare i prerequisiti interni**: quando l'utente si sta preparando alla scadenza
  e chiede cosa deve avere pronto, leggere `tasks/check-prerequisiti-interni.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita' e carica il file `tasks/` corrispondente.
2. Raccogli gli input richiesti dal task. Se un input decisivo manca (in particolare il
   **momento in cui il fabbricante e' venuto a conoscenza** dell'evento), chiedilo: non
   assumerlo.
3. Applica la procedura del task citando l'articolo e il paragrafo su cui si fonda ogni
   conclusione.
4. Distingui sempre, nell'output, cio' che il testo **impone** da cio' che e'
   **condizionato** ("se del caso", "se disponibili") e da cio' su cui il testo **tace**.
5. Chiudi con il rinvio al responsabile della conformita' e, per i punti di
   coordinamento aperti (vedi `references/estratti/cra-art14-obblighi-e-termini.md`,
   sezioni H e I), al consulente legale.

## Regola di prudenza sui termini

Le 24 ore dell'art. 14, par. 2, lett. a), e par. 4, lett. a), decorrono da un fatto -
"il momento in cui il fabbricante ne e' venuto a conoscenza" - che **il Regolamento non
definisce**. Non esiste nel testo alcuna soglia di gravita', numero di utenti o punteggio
CVSS che escluda l'obbligo.

Ne segue la regola operativa di questa skill: **in caso di dubbio sulla qualificazione,
la skill non conclude che l'obbligo non sussiste.** Espone gli elementi a favore e
contro, indica quali prove mancano, e rimette la decisione al fabbricante ricordando che
l'art. 15 consente comunque la segnalazione volontaria e che l'art. 17, par. 4, esclude
che la sola notifica comporti maggiore responsabilita'.

## Fonti normative

- **Reg. (UE) 2024/2847 (CRA)**: art. 3 (definizioni, punti 1, 13, 19, 21, 22, 40, 42,
  43, 45), art. 13 (par. 6, 7, 8, 17), **art. 14** (integrale), art. 15, art. 16,
  art. 17, art. 64, art. 71, allegato I parte II.
- **Dir. (UE) 2022/2555 (NIS2)**: art. 6 punti 5 e 6 (definizioni di quasi incidente e
  incidente, richiamate dall'art. 3 CRA), art. 12 par. 1 (CSIRT coordinatore).
- **D.Lgs. 4 settembre 2024, n. 138**: art. 2 c. 1 lett. i), art. 15, art. 16 (CSIRT
  Italia designato coordinatore, operante presso ACN).

Trascrizioni verbatim in `references/fonti/`, estratti operativi in
`references/estratti/`, riferimenti completi con SHA256 in `references/sources.yaml`.

## Limiti

Cosa questa skill NON fa:

- Non trasmette notifiche e non interagisce con la piattaforma unica di segnalazione o
  con i terminali nazionali.
- Non descrive la registrazione, l'accreditamento o l'accesso alla piattaforma: le fonti
  lette non lo disciplinano.
- Non classifica il PDE ne' valuta la conformita' (usa `cra-classificazione-pde`).
- Non esegue il triage tecnico della vulnerabilita' ne' scrive la patch.
- Non copre gli obblighi di notifica del D.Lgs. 138/2024 (NIS2) e non afferma che un
  adempimento NIS2 assorba quello dell'art. 14, o viceversa.
- Non quantifica il rischio sanzionatorio: l'art. 64 fissa massimali e rimette agli
  Stati membri le norme sanzionatorie, e la sua data di applicazione presenta il
  problema di coordinamento descritto nell'estratto.
- Non cita atti delegati o di esecuzione della Commissione ex art. 14, par. 9 e 10, ne'
  la politica nazionale CVD ex art. 16, c. 4, D.Lgs. 138/2024: nessuno di questi atti e'
  stato letto. Quando saranno disponibili, gli output vanno riletti alla loro luce.
