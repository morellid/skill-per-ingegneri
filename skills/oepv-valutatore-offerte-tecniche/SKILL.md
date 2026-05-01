---
name: oepv-valutatore-offerte-tecniche
description: Supporto alla commissione di gara e al RUP per la costruzione della matrice criteri/sottocriteri OEPV, la valutazione delle offerte tecniche con il metodo aggregativo-compensatore, e la verifica di conformita' della matrice al art. 108 D.Lgs. 36/2023. Use when an Italian RUP, stazione appaltante, or commissione di gara needs to build or verify an OEPV evaluation matrix for a public tender, evaluate technical offers against an existing matrix, or check a criteria matrix for compliance and TAR-appeal risk.
license: MIT
---

# OEPV - Valutatore offerte tecniche

## Quando usare questa skill

Usare quando un RUP, una commissione di gara o una stazione appaltante chiede di:
- **Costruire la matrice criteri/sottocriteri**: impostare criteri, sottocriteri, pesi e metodi di valutazione per un appalto OEPV, con controllo dei limiti dell'art. 108 D.Lgs. 36/2023
- **Valutare le offerte tecniche**: applicare il metodo aggregativo-compensatore alle offerte dei concorrenti e produrre il prospetto punteggi con classifica
- **Verificare una matrice esistente**: controllare che la matrice nel disciplinare di gara rispetti l'art. 108 e individuare criticita' esposte a ricorso TAR/CdS

**Non usare** se l'utente chiede:
- Redazione dei documenti di gara completi (bando, disciplinare, capitolato): usa skill PR.2 dedicata - bandi-tipo ANAC (non ancora rilasciata)
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

## Quando l'OEPV e' obbligatorio

Ai sensi dell'art. 108 co. 2 D.Lgs. 36/2023, l'aggiudicazione con criterio qualita'/prezzo e' **obbligatoria** per:
- Servizi sociali e di ristorazione ospedaliera, assistenziale e scolastica
- Servizi di architettura, ingegneria e altri servizi tecnici di importo >= 140.000 EUR
- Servizi ad alto contenuto tecnologico o con carattere innovativo di importo >= 140.000 EUR
- Forniture ad alto contenuto tecnologico di importo >= 140.000 EUR
- Dialogo competitivo e partenariato per l'innovazione
- Contratti con componente progettuale (appalti integrati)
- Servizi di trasporto scolastico

Per tutti gli altri contratti, il criterio del prezzo piu' basso e' ammesso se l'oggetto e' standardizzato, tranne per i servizi ad alta intensita' di manodopera (art. 108 co. 3).

## Criteri premianti obbligatori (art. 108 co. 7)

In ogni gara OEPV, il testo dell'art. 108 co. 7 stabilisce che "e' **sempre previsto** il maggiore punteggio possibile" per **tutte e tre** le seguenti categorie:
1. **Produttori di beni a basse emissioni di CO2** - principalmente per forniture e lavori con componente materiali significativa
2. **Imprese con misure di welfare aziendale** - applicabile a qualsiasi contratto
3. **Imprese con certificazione parita' di genere** (UNI/PdR 125:2022 o equivalente, D.Lgs. 198/2006 art. 46-bis) - applicabile a qualsiasi contratto

Omettere anche una sola delle tre categorie rende la matrice contestabile. Se una categoria non e' pertinente all'oggetto specifico del contratto (art. 108 co. 6), documentare la ragione nel disciplinare.

## Limiti sul punteggio economico (art. 108 co. 4)

- **Appalti IT in contesti di interesse strategico nazionale**: punteggio economico max **10%** del totale
- **Contratti ad alta intensita' di manodopera**: punteggio economico max **30%** del totale
- Per tutti gli altri contratti OEPV: nessun limite percentuale esplicito nell'art. 108, ma il bilanciamento tecnico/economico deve essere proporzionato e motivato

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 31 marzo 2023 n. 36, artt. 93, 107, 108 - Criteri di aggiudicazione e commissione giudicatrice
- ANAC Linea Guida n. 2, Delibera n. 424 del 2 maggio 2018 - Metodologia valutazione OEPV (non vincolante sotto D.Lgs. 36/2023 ma ancora di riferimento operativo)

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dlgs-36-art93.md`](references/estratti/dlgs-36-art93.md) - commissione giudicatrice
- [`dlgs-36-art107-108.md`](references/estratti/dlgs-36-art107-108.md) - criteri di aggiudicazione, OEPV obbligatorio, limiti punteggio economico
- [`anac-lg-n2-metodologia-oepv.md`](references/estratti/anac-lg-n2-metodologia-oepv.md) - metodo aggregativo-compensatore, formule, metodi di attribuzione punteggio

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
