---
name: verifica-accessibilita-dichiarazione-agid
description: "Supporto documentale al metodo di verifica dell'accessibilita' degli strumenti informatici (siti web, applicazioni mobili, software, documenti) e alla dichiarazione di accessibilita', secondo le Linee guida AgID sull'accessibilita' degli strumenti informatici (adottate ex art. 11 L. 4/2004, versione 21/12/2022). Aiuta a impostare la verifica tecnica (conformita' ai punti 9-11 e ai Prospetti/Appendici della norma UNI CEI EN 301549, con requisito minimo WCAG 2.1 livello AA per il web), la verifica soggettiva a quattro fasi (analisi di uno o piu' esperti di fattori umani con giudizio su scala 1-5, costituzione di un gruppo di valutazione con persone rappresentative dei diversi tipi di disabilita', esecuzione dei task e rapporto conclusivo sul livello di qualita'), obbligatoria per le forniture sopra soglia comunitaria (art. 35 D.Lgs 50/2016) e con metodologia semplificata sotto soglia, applicando i dodici criteri essenziali; a predisporre la dichiarazione di accessibilita' compilando il modello sulla piattaforma AgID, pubblicando il link nel footer, ricavando le informazioni da autovalutazione, valutazione di terzi o dal Modello di autovalutazione, rispettando il riesame annuale entro il 23 settembre e, per le PA, la pubblicazione degli obiettivi annuali entro il 31 marzo; a valutare i casi di deroga per onere sproporzionato (art. 3-ter L. 4/2004) e a predisporre il meccanismo di feedback e il ricorso al Difensore civico digitale. Use when a public administration, a supplier, or a large private operator must verify the accessibility of a website, mobile app, software or document and prepare/renew the accessibility declaration per the Italian AgID guidelines; it is a documentary aid and does NOT perform the technical WCAG/EN 301549 audit for you, does NOT reproduce the paid UNI CEI EN 301549 standard or the WCAG success criteria, does not compile the declaration on the AgID platform in your place, and does not cover the legal obligations/sanctions of the Stanca Act (handled by the accessibilita-siti-app-l4-2004 skill)."
license: MIT
area: software-dati-cybersecurity
title: "Verifica di accessibilita' e dichiarazione (Linee guida AgID)"
summary: "Metodo di verifica dell'accessibilita' (verifica tecnica su EN 301549/WCAG 2.1 AA + verifica soggettiva a 4 fasi) e dichiarazione di accessibilita' sulla piattaforma AgID, con obiettivi annuali, deroghe e feedback. Non esegue l'audit ne' compila la dichiarazione."
normative_refs:
  - "AgID - Linee guida sull'accessibilita' degli strumenti informatici (21/12/2022, ex art. 11 L. 4/2004)"
  - "L. 4/2004 (Legge Stanca) artt. 3-bis, 3-ter, 3-quater, 3-quinquies, 9, 11 + UNI CEI EN 301549 / WCAG 2.1 (richiamate)"
version: 0.1.0-alpha
status: alpha
tags:
  - accessibilita
  - linee-guida-agid
  - dichiarazione-accessibilita
  - en-301549
  - wcag
---

# Verifica di accessibilita' e dichiarazione (Linee guida AgID)

## Quando usare questa skill

Usala quando una **pubblica amministrazione**, un suo **fornitore** o un **grande operatore
privato** deve **verificare l'accessibilita'** di un sito web, un'applicazione mobile, un
software o un documento e **predisporre o rinnovare la dichiarazione di accessibilita'**,
secondo le **Linee guida AgID sull'accessibilita' degli strumenti informatici** (adottate
ex **art. 11 L. 4/2004**, versione 21/12/2022):

- impostare la **verifica tecnica** e la **verifica soggettiva**;
- predisporre la **dichiarazione di accessibilita'** e gli **obiettivi annuali**;
- valutare le **deroghe** per onere sproporzionato;
- attivare il **meccanismo di feedback** e il **Difensore civico digitale**.

Per gli **obblighi giuridici** (chi e' obbligato, esclusioni, appalti, vigilanza, sanzioni)
della Legge Stanca usa la skill `accessibilita-siti-app-l4-2004`: questa copre il **metodo
di verifica** e la **dichiarazione**.

## Requisiti tecnici (cap. 2)

Il riferimento tecnico e' la norma **UNI CEI EN 301549** (richiamata, **non riprodotta** -
e' a pagamento):

- **Web**: requisiti del **punto 9** (Prospetto A.1, Appendice A). Requisito minimo **WCAG
  2.1 livello AA** (equivalente ai punti 9.1-9.4 e 9.6 della EN 301549) per i siti avviati
  dopo l'entrata in vigore delle Linee guida; **WCAG 2.0 AA** per quelli avviati prima del
  23/9/2020.
- **Documenti non web** e **software**: requisiti ai punti **10** e **11** della EN 301549.

## Verifica dell'accessibilita' (cap. 3)

- **Verifica tecnica**: conformita' secondo i Prospetti/Appendici della EN 301549 (Web:
  Prospetto A.1; documenti non web: C.10; software: C.11 + C.5/C.6/C.7/C.13 ove inerenti).
- **Verifica soggettiva** (Web/app/software sviluppato per il soggetto erogatore):
  **obbligatoria** per le forniture **sopra soglia comunitaria** (**art. 35 D.Lgs
  50/2016**); **sotto soglia**, almeno una **metodologia semplificata** (es. Protocollo
  eGLU) con il coinvolgimento di **persone con disabilita'**. Si articola in **4 fasi**:
  1. analisi di uno o piu' **esperti di fattori umani** (giudizio su **scala 1-5**);
  2. costituzione del **gruppo di valutazione** (utenti rappresentativi dei diversi tipi di
     disabilita': sordita', ipovisione, daltonismo, cecita', disabilita' motoria/spastica/
     cognitiva), che usano le proprie tecnologie assistive;
  3. **esecuzione dei task** in contesti usuali e di laboratorio, guidata dall'esperto;
  4. **rapporto conclusivo** con il livello di qualita' (< 2 = assenza; >= 2 e < 3 = primo
     livello; >= 3 e < 4 = secondo; >= 4 = terzo livello).
- **12 criteri essenziali**: percezione, comprensibilita', operabilita', coerenza,
  salvaguardia della salute, sicurezza, trasparenza, apprendibilita', aiuto e
  documentazione, tolleranza agli errori, gradevolezza, flessibilita'.

## Dichiarazione di accessibilita' (cap. 4)

- Il **soggetto erogatore** rilascia una dichiarazione per **ogni sito web e app** di cui e'
  titolare, compilando **esclusivamente sulla piattaforma AgID** il form coerente con il
  **modello (Allegato 1)**; **qualsiasi altro modello non e' conforme** (Decisione UE
  2018/1523; art. 3-quater L. 4/2004).
- Informazioni ricavate da: **autovalutazione**, **valutazione di terzi**, o il **"Modello
  di autovalutazione" (Allegato 2)** AgID; se una verifica completa e' impossibile o molto
  onerosa, e' ammessa una **verifica a campione** con relazione di valutazione.
- Pubblicare il **link** AgID con la dicitura **"Dichiarazione di accessibilita'"** (nel
  **footer** dei siti; per le app, nel sito dell'ente o al download).
- **Riesame annuale** entro il **23 settembre** (validita' 24 settembre - 23 settembre); la
  **mancata pubblicazione** comporta la **responsabilita' ex art. 9 L. 4/2004**.
- **PA**: pubblicare gli **obiettivi annuali di accessibilita'** entro il **31 marzo**.

## Onere sproporzionato - deroghe (cap. 6)

Deroga (art. 3-ter, c. 2, L. 4/2004) invocabile solo su **motivazioni legittime e
giustificate**, per quattro misure (onere organizzativo eccessivo; onere finanziario
eccessivo; rischio di pregiudicare lo scopo prefissato; rischio di pregiudicare la
pubblicazione di informazioni necessarie), **non oltre lo stretto necessario**. Ulteriori
casi di deroga (lett. a-h): file per ufficio pre-23/9/2018; media preregistrati
pre-23/9/2019; dirette; cartografia; contenuti di terzi; patrimonio storico-culturale;
extranet/intranet pre-23/9/2019; contenuti-archivio.

## Feedback e Difensore civico digitale (cap. 7)

Predisporre il **meccanismo di feedback** (art. 3-bis L. 4/2004): chiunque puo' notificare
difetti e chiedere che le informazioni siano rese accessibili. In assenza o inadeguatezza di
risposta **entro 30 giorni**, l'utente puo' ricorrere al **Difensore civico per il digitale**
(art. 3-quinquies L. 4/2004), che puo' disporre misure correttive informando AgID.

## Cosa NON fa (limiti)

- **Non esegue l'audit tecnico** WCAG/EN 301549 ne' la verifica soggettiva al posto del
  professionista/soggetto erogatore.
- **Non riproduce** la norma **UNI CEI EN 301549** (a pagamento) ne' le **WCAG**: rinvia ai
  punti/Prospetti/Appendici e ai criteri di successo.
- **Non compila** la dichiarazione al posto del soggetto (il form e' sulla **piattaforma AgID**).
- **Non copre gli obblighi/sanzioni** della L. 4/2004 (skill `accessibilita-siti-app-l4-2004`).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`imposta-verifica-accessibilita`](tasks/imposta-verifica-accessibilita.md) | Imposta la verifica tecnica (EN 301549/WCAG 2.1 AA) e la verifica soggettiva a 4 fasi, con la soglia dell'art. 35 D.Lgs 50/2016 |
| [`predisponi-dichiarazione-accessibilita`](tasks/predisponi-dichiarazione-accessibilita.md) | Struttura la dichiarazione di accessibilita' (modello AgID, fonti di analisi, link, riesame 23 settembre) e gli obiettivi annuali |

## Riferimenti normativi

- **AgID - Linee guida sull'accessibilita' degli strumenti informatici** (versione
  21/12/2022), adottate ex **art. 11 L. 4/2004**: requisiti tecnici (cap. 2), verifica
  (cap. 3), dichiarazione e obiettivi annuali (cap. 4), monitoraggio (cap. 5), onere
  sproporzionato (cap. 6), procedura di attuazione/feedback/Difensore civico (cap. 7).
- **L. 9 gennaio 2004, n. 4** (Legge Stanca) - artt. **3-bis** (principi generali), **3-ter**
  (onere sproporzionato), **3-quater** (dichiarazione), **3-quinquies** (Difensore civico
  digitale), **9** (responsabilita'), **11** (linee guida).
- **UNI CEI EN 301549** e **WCAG 2.1** (richiamate, non riprodotte); Direttiva UE 2016/2102;
  Decisione di esecuzione UE 2018/1523.

Dettaglio in `references/sources.yaml`, `references/fonti/linee-guida-accessibilita-agid.md`,
`references/estratti/accessibilita-verifica-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la verifica tecnica e soggettiva, la scelta del campione
e la compilazione della dichiarazione sulla piattaforma AgID restano responsabilita' del
soggetto erogatore e del suo fornitore. La skill **non sostituisce** l'audit tecnico di accessibilita', il RTD ne' la lettura delle Linee guida AgID e della norma UNI CEI EN 301549.
