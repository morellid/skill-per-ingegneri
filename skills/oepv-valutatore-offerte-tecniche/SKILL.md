---
name: oepv-valutatore-offerte-tecniche
description: Supporto alla commissione di gara e al RUP per la costruzione della matrice criteri/sottocriteri OEPV, la valutazione delle offerte tecniche con il metodo aggregativo-compensatore, e la verifica di conformita' della matrice al art. 108 D.Lgs. 36/2023. Use when an Italian RUP, stazione appaltante, or commissione di gara needs to build or verify an OEPV evaluation matrix for a public tender, evaluate technical offers against an existing matrix, or check a criteria matrix for compliance and TAR-appeal risk.
license: MIT
area: appalti-opere-pubbliche
title: "OEPV - Valutatore offerte tecniche"
summary: "Costruzione della matrice criteri/sottocriteri OEPV, valutazione delle offerte tecniche con metodo aggregativo-compensatore, verifica di conformita' all'art. 108 di una matrice gia' redatta"
normative_refs:
  - "D.Lgs. 36/2023 art. 108"
version: 0.2.0
status: alpha
tags:
  - oepv
  - dlgs-36-2023
  - offerte
---

# OEPV - Valutatore offerte tecniche

## Quando usare questa skill

Usare quando un RUP, una commissione di gara o una stazione appaltante chiede di:
- **Costruire la matrice criteri/sottocriteri**: impostare criteri, sottocriteri, pesi e metodi di valutazione per un appalto OEPV, con controllo dei limiti dell'art. 108 D.Lgs. 36/2023
- **Valutare le offerte tecniche**: applicare il metodo aggregativo-compensatore alle offerte dei concorrenti e produrre il prospetto punteggi con classifica
- **Verificare una matrice esistente**: controllare che la matrice nel disciplinare di gara rispetti l'art. 108 e individuare criticita' esposte a ricorso TAR/CdS

**Non usare** se l'utente chiede:
- Redazione dei documenti di gara completi (bando, disciplinare, capitolato): usa skill [`bandi-tipo-anac-checker`](../bandi-tipo-anac-checker/SKILL.md) per la verifica di conformita' del disciplinare al Bando tipo n. 2/2026 SIA o n. 1/2023
- Verifica di un PFTE o degli elaborati progettuali di base: usa skill [`pfte-allegato-i7-checker`](../pfte-allegato-i7-checker/SKILL.md)
- Calcolo della soglia di anomalia: quella e' disciplinata dall'Allegato II.2 D.Lgs. 36/2023 e non e' oggetto di questa skill
- Giudizio sulla legittimita' di un provvedimento di aggiudicazione gia' emesso: richiede parere legale
- Valutazione dell'anomalia dell'offerta economica (sub-procedimento soccorso istruttorio e contraddittorio): fuori scope

## Avvertenza

Questa skill e' uno strumento di supporto alla **preparazione e verifica della documentazione di gara OEPV**. **Non sostituisce il giudizio del RUP, del responsabile dei procedimenti e della commissione giudicatrice.** L'output della skill non e' un atto amministrativo, non ha valenza legale e non puo' essere allegato direttamente agli atti di gara come documento ufficiale. Ogni matrice, punteggio o verifica prodotti dalla skill richiedono revisione, approvazione e firma del responsabile competente. La skill non garantisce la legittimita' della procedura ne' esclude il rischio di impugnativa.

## Sotto-attivita' disponibili

Questa skill supporta tre sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Costruzione matrice criteri**: l'utente chiede "come imposto i criteri OEPV?", "quali criteri metto nel disciplinare?", "aiutami a costruire la griglia di valutazione" -> leggi [`tasks/costruisci-matrice-criteri.md`](tasks/costruisci-matrice-criteri.md)
- **Valutazione offerte tecniche**: l'utente chiede "valuta queste offerte", "calcola i punteggi", "chi vince tecnicamente?", "applica il metodo aggregativo-compensatore" -> leggi [`tasks/valuta-offerta-tecnica.md`](tasks/valuta-offerta-tecnica.md)
- **Verifica matrice esistente**: l'utente chiede "controlla questa matrice", "e' corretta la griglia del disciplinare?", "ci sono problemi TAR?", "verifica la conformita' all'art. 108" -> leggi [`tasks/check-matrice-criteri.md`](tasks/check-matrice-criteri.md)

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' vuole eseguire e raccogli le **variabili di inquadramento** prima di procedere.

## Processo generale

1. **Inquadra la gara**: tipo di contratto (lavori / servizi / forniture), oggetto, importo a base d'asta, criterio di aggiudicazione gia' scelto o da scegliere
2. **Verifica applicabilita' OEPV**: controlla se l'OEPV e' obbligatorio (art. 108 co. 2) o solo facoltativo per quella tipologia
3. **Identifica la sotto-attivita'**: usa il routing della sezione "Sotto-attivita' disponibili"
4. **Carica il task file** corrispondente e applica la procedura
5. **Produci l'output** strutturato con citazione precisa degli articoli e commi per ogni regola applicata
6. **Concludi** sempre con:
   - elenco delle **scelte discrezionali non automaticamente verificabili** (adeguatezza dei pesi scelti, pertinenza dei criteri rispetto all'oggetto)
   - rinvio alla **revisione del RUP e della commissione** prima di pubblicare o formalizzare

## Bando Tipo n. 2/2026 per SIA sopra soglia (dal 30 maggio 2026)

Con Delibera ANAC n. 153 del 15 aprile 2026 (GU n. 111 del 15/05/2026, efficace dal 30/05/2026),
ANAC ha approvato il **Bando tipo n. 2/2026** come schema per procedure di SIA sopra soglia europea.

**Impatto su questa skill per gare SIA sopra soglia:**

### Schema OEPV codificato per SIA (Paragrafo 18)

Articolazione criteri offerta tecnica standard:
- **A. Professionalita' ed adeguatezza dell'offerta**: max 3 servizi affini (senza limite decennale)
- **B. Caratteristiche metodologiche dell'offerta**: relazione tecnico-organizzativa
- (eventuale) **Criteri premianti CAM**
- (se previsto BIM) **Adozione metodologia BIM** come criterio premiale; certificazione UNI 11337-7 valorizzabile
- **Parita' di genere** (art. 46-bis D.Lgs. 198/2006): obbligatorio art. 108 co. 7

**Tetto 30% punteggio economico**: imposto dall'art. 41 c. 15-bis lett. b Codice per TUTTI i SIA
(non solo alta intensita' manodopera).

**Formula punteggio economico non lineare** (Paragrafo 18.3):
- Se Ri < Rmed: PEi = (Ri/Rmed)^alpha; Se Ri >= Rmed: PEi = 1
- dove Ri = ribasso, Rmed = media ribassi, alpha = [0,1 - 0,3]
- Il ribasso si applica al solo **35% soggetto a ribasso** (65% e' prezzo fisso ex art. 41 c. 15-bis)

### BIM come elemento obbligatorio

Quando la progettazione riguarda lavori con costo presunto **> 2.000.000 euro** (o beni culturali sopra soglia art. 14 c. 1 lett. a), il Bando tipo n. 2/2026 codifica:
- Requisiti speciali obbligatori: BIM Manager, BIM Coordinator, BIM Specialist, CDE Manager (UNI 11337-7) - para. 6.1 lett. h-k
- La certificazione UNI 11337-7:2018 delle figure BIM e' valorizzabile come criterio premiale OEPV
- Compenso maggiorato del **10%** (Allegato I.13 art. 2 c. 5)

Per verifica matrice OEPV in gara SIA con BIM obbligatorio: la matrice tecnica deve includere sottocriterio BIM e l'offerta tecnica deve includere l'offerta di gestione informativa digitale.

### Dichiarazione AI nell'offerta tecnica (art. 13 L. 132/2025)

Per SIA sopra soglia (Paragrafi 15.1 e 16 Bando tipo n. 2/2026):
- In **domanda di partecipazione**: dichiarazione obbligatoria sull'uso AI nell'elaborazione dell'offerta tecnica e sull'uso AI in esecuzione (art. 13 L. 132/2025, versione "servizi intellettuali")
- In **offerta tecnica**: indicazione delle attivita' strumentali per cui si e' usata AI
- La commissione verifica la coerenza tra dichiarazione in domanda e indicazioni in offerta

Per il disciplinare nel suo complesso, usare anche: [`bandi-tipo-anac-checker`](../bandi-tipo-anac-checker/SKILL.md).

Estratto normativo: [`references/estratti/anac-bando-tipo-n2-2026-sia-oepv-bim.md`](references/estratti/anac-bando-tipo-n2-2026-sia-oepv-bim.md).

---

## Quando l'OEPV e' obbligatorio

Ai sensi dell'art. 108 co. 2 D.Lgs. 36/2023 (GU 2023), l'aggiudicazione con criterio qualita'/prezzo e' **obbligatoria** per (le sei fattispecie del co. 2):
- a) Servizi sociali e di ristorazione ospedaliera, assistenziale e scolastica; servizi ad alta intensita' di manodopera
- b) Servizi di ingegneria e architettura e altri servizi tecnici di importo >= 140.000 EUR
- c) Servizi e forniture di importo >= 140.000 EUR con notevole contenuto tecnologico o carattere innovativo
- d) Dialogo competitivo e partenariato per l'innovazione
- e) Appalti integrati (progettazione + esecuzione)
- f) Lavori con notevole contenuto tecnologico o carattere innovativo

Per tutti gli altri contratti, il criterio del prezzo piu' basso e' ammesso se l'oggetto e' standardizzato, tranne per i servizi ad alta intensita' di manodopera (art. 108 co. 3).

**Nota**: il co. 2 nella GU 2023 originale ha 6 lettere (a-f). Versioni precedenti di questa skill citavano anche il trasporto scolastico e i servizi con requisiti DPR 328 come categorie obbligatorie distinte, ma queste fattispecie non compaiono nel co. 2 del testo originale GU 2023. Verificare sul testo consolidato Normattiva se il D.Lgs. 209/2024 correttivo abbia aggiunto ulteriori fattispecie.

## Criterio premiante obbligatorio: parita' di genere (art. 108 co. 7)

Il testo dell'art. 108 co. 7 D.Lgs. 36/2023 (GU 2023) stabilisce un obbligo esplicito: "Al fine di promuovere la parita' di genere, le stazioni appaltanti **prevedono** nei bandi di gara, negli avvisi e negli inviti, il maggior punteggio da attribuire alle imprese che attestano, anche a mezzo di autocertificazione, il possesso dei requisiti di cui all'articolo 46-bis del codice delle pari opportunita' tra uomo e donna, di cui al decreto legislativo 11 aprile 2006, n. 198."

Questo e' l'**unico criterio premiante esplicitamente obbligatorio** nell'art. 108 co. 7 del testo originale GU 2023. L'autocertificazione e' ammessa ma la SA verifica l'attendibilita' sull'aggiudicataria.

Il co. 7 consente altresi' alla SA di inserire **criteri premiali facoltativi** per PMI, operatori locali (principio di prossimita'), start-up innovative, ecc.

**Nota**: Versioni precedenti di questa skill riportavano erroneamente che anche basse emissioni CO2 e welfare aziendale erano obbligatori ai sensi del co. 7. Questa affermazione non e' rintracciabile nel testo GU 2023 dell'art. 108. CO2 e welfare possono essere inclusi come criteri premianti facoltativi, purche' connessi all'oggetto (art. 108 co. 6).

**Nota sul D.Lgs. 209/2024**: il testo del co. 7 potrebbe essere stato modificato dal correttivo. Verificare sul testo consolidato Normattiva prima della pubblicazione di gare successive al 31/12/2024.

## Limiti sul punteggio economico

- **SIA sopra soglia europea (Bando tipo n. 2/2026)**: punteggio economico max **30%** del totale (art. 41 c. 15-bis lett. b Codice) - vincolo specifico per SIA, non dipende dall'art. 108 co. 4
- **Appalti IT in contesti di interesse strategico nazionale**: punteggio economico max **10%** del totale (art. 108 co. 4)
- **Contratti ad alta intensita' di manodopera (non SIA)**: punteggio economico max **30%** del totale (art. 108 co. 4)
- Per tutti gli altri contratti OEPV: nessun limite percentuale esplicito nell'art. 108, ma il bilanciamento tecnico/economico deve essere proporzionato e motivato

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 31 marzo 2023 n. 36, artt. 93, 107, 108 - Criteri di aggiudicazione e commissione giudicatrice
- ANAC Linea Guida n. 2, Delibera n. 424 del 2 maggio 2018 - Metodologia valutazione OEPV (non vincolante sotto D.Lgs. 36/2023 ma ancora di riferimento operativo)
- ANAC Bando tipo n. 2/2026 (Delibera n. 153 del 15 aprile 2026) - Schema OEPV per SIA sopra soglia

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dlgs-36-art93.md`](references/estratti/dlgs-36-art93.md) - commissione giudicatrice
- [`dlgs-36-art107-108.md`](references/estratti/dlgs-36-art107-108.md) - criteri di aggiudicazione, OEPV obbligatorio, limiti punteggio economico
- [`anac-lg-n2-metodologia-oepv.md`](references/estratti/anac-lg-n2-metodologia-oepv.md) - metodo aggregativo-compensatore, formule, metodi di attribuzione punteggio
- [`anac-bando-tipo-n2-2026-sia-oepv-bim.md`](references/estratti/anac-bando-tipo-n2-2026-sia-oepv-bim.md) - schema OEPV SIA, BIM obbligatorio, formula economica non lineare, clausole AI

## Limiti

Questa skill NON fa:
- Non redige i documenti di gara ufficiali (bando, disciplinare, capitolato speciale) - quelli richiedono la skill PR.2 bandi-tipo ANAC
- Non valuta la **legittimita' della procedura di gara** nel suo complesso (scelta della procedura, soglie, requisiti partecipazione)
- Non calcola la **soglia di anomalia** (Allegato II.2 D.Lgs. 36/2023)
- Non gestisce il **sub-procedimento di anomalia** (contraddittorio, giustificazioni)
- Non valuta la **conformita' delle offerte tecniche** rispetto ai requisiti tecnici del capitolato: valuta solo l'attribuzione dei punteggi OEPV sulla base dei criteri definiti
- Non sostituisce il **giudizio discrezionale della commissione** sui criteri qualitativi non automaticamente quantificabili
- Non copre l'**anomalia dell'offerta economica** ne' le verifiche di congruita'
- Non gestisce **fattispecie speciali** (contratti esclusi, difesa e sicurezza, settori speciali) senza rinvio al consulente legale
- Non interpreta il **merito delle offerte tecniche**: l'output e' un framework di calcolo, non una valutazione sostanziale
