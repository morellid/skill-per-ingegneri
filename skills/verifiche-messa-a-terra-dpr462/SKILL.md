---
name: verifiche-messa-a-terra-dpr462
description: "Supporto documentale agli adempimenti del DPR 462/2001 per impianti elettrici di messa a terra, dispositivi di protezione contro le scariche atmosferiche e impianti elettrici in luoghi con pericolo di esplosione nei luoghi di lavoro. Determina la periodicita' della verifica periodica (5 anni ordinari; 2 anni per cantieri, locali ad uso medico, ambienti a maggior rischio in caso di incendio e luoghi con pericolo di esplosione), i soggetti abilitati (ASL/ARPA o organismi abilitati MISE), gli adempimenti di messa in esercizio (dichiarazione di conformita' = omologazione, denuncia entro 30 giorni a INAIL e ASL/ARPA), la prima verifica a campione INAIL, la comunicazione del nominativo dell'organismo alla banca dati INAIL (art. 7-bis) e le comunicazioni di variazione. Use when an Italian employer, electrical engineer or safety consultant needs to know the DPR 462/2001 obligations, the verification frequency for a specific installation, or who performs the checks; it is a documentary aid and does not replace the installer, the verifying body or the datore di lavoro."
license: MIT
area: impianti-macchine-prodotti
title: "Verifiche impianti di messa a terra e luoghi pericolosi - DPR 462/2001"
summary: "Adempimenti DPR 462/2001 (messa a terra, scariche atmosferiche, luoghi con pericolo di esplosione nei luoghi di lavoro): periodicita' delle verifiche periodiche (5 anni / 2 anni), soggetti abilitati (ASL/ARPA/organismi), denuncia entro 30 gg, banca dati INAIL; documentale"
normative_refs:
  - "D.P.R. 22/10/2001 n. 462 (testo vigente) - artt. 1-8"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-462-2001
  - messa-a-terra
  - sicurezza-elettrica
  - verifiche-periodiche
  - luoghi-di-lavoro
---

# Verifiche impianti di messa a terra e luoghi pericolosi - DPR 462/2001

## Quando usare questa skill

Usala quando devi orientarti sugli adempimenti del **DPR 462/2001** per un
impianto in un luogo di lavoro:

- determinare la **periodicita' della verifica periodica** (5 anni o 2 anni) in
  base al tipo di impianto e all'ambiente;
- sapere **chi esegue** le verifiche (ASL/ARPA o organismi abilitati);
- ricostruire gli adempimenti di **messa in esercizio** (dichiarazione di
  conformita', omologazione, denuncia entro 30 giorni a INAIL e ASL/ARPA);
- capire la **prima verifica a campione** dell'INAIL e la **comunicazione del
  nominativo dell'organismo** alla banca dati INAIL (art. 7-bis);
- gestire le **comunicazioni di variazione** (cessazione, modifiche,
  trasferimento).

Target: datori di lavoro, ingegneri e periti elettrotecnici, consulenti della
sicurezza, RSPP, installatori.

## Avvertenza

Questa skill e' un **supporto documentale** basato sul testo vigente del DPR
462/2001. **Non definisce le regole tecniche di realizzazione degli impianti**
(norme CEI, non riprodotte), **non calcola** parametri di impianto, **non
fornisce gli importi delle tariffe** e **non sostituisce** l'installatore,
l'organismo verificatore o il datore di lavoro nei rispettivi adempimenti. Le
date concrete delle scadenze vanno calcolate dall'utente sui documenti reali.

## Sotto-attivita' disponibili

- **Diagnosi degli adempimenti per un impianto**: dato il tipo di impianto e
  l'ambiente, determina periodicita', soggetti e adempimenti ->
  `tasks/diagnosi-adempimenti.md`
- **Checklist adempimenti DPR 462/2001**: verifica la completezza degli
  adempimenti (messa in esercizio, denuncia, verifiche, comunicazioni INAIL) ->
  `tasks/checklist-adempimenti.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input (tipo di impianto, ambiente, stato degli adempimenti).
4. Applica la regola/checklist **citando l'articolo preciso** del DPR 462/2001.
5. Ricorda che l'**ISPESL** del testo e' oggi l'**INAIL**.
6. Chiudi con il rinvio agli obblighi del datore di lavoro e ai soggetti
   competenti.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dpr-462-2001.md` (testo vigente da Normattiva, pagina indice
pinnata `!vig=2026-07-14`), estratto operativo in
`references/estratti/verifiche-messa-a-terra-checklist.md`.

## Limiti

Cosa questa skill NON fa:
- non definisce le regole tecniche di realizzazione/verifica degli impianti
  (norme CEI, es. CEI 64-8, CEI EN 62305) ne' esegue calcoli;
- non fornisce gli importi delle tariffe (decreto ISPESL 7/7/2005, non trascritto);
- non gestisce la modulistica INAIL puntuale ne' i portali telematici;
- non copre gli obblighi generali del D.Lgs. 81/2008 oltre al richiamo del datore
  di lavoro;
- non calcola le date concrete delle scadenze: fornisce le periodicita' e gli
  obblighi.
