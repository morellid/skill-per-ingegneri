---
name: transizione-5-0-asseverazione
description: Supporta la redazione e la verifica delle certificazioni tecniche (ex ante ed ex post) richieste dal Piano Transizione 5.0 ai sensi dell'art. 38 DL 19/2024 (convertito da L. 56/2024) e del DM MIMIT-MEF 24 luglio 2024. Fornisce inquadramento dell'ammissibilita' del progetto, calcolo strutturato della riduzione dei consumi energetici (soglie >=3% struttura produttiva o >=5% processo interessato) con conversione in tep, generazione delle bozze testuali della Certificazione Ex Ante (Allegato VIII) e Certificazione Ex Post (Allegato X) e delle relative Relazioni Tecniche (Allegati IX e XI), verifica della coerenza ex ante / ex post per i controlli GSE. Use when an EGE (UNI CEI 11339), an ESCo (UNI CEI 11352), an ingegnere iscritto all'albo (sez. A o B) o un perito industriale qualificato deve predisporre o verificare l'asseverazione tecnica per il credito d'imposta Transizione 5.0, sia in fase di prenotazione (comunicazione preventiva) sia in fase di completamento (entro 28 febbraio 2026).
license: MIT
area: energia-incentivi
title: "Transizione 5.0 - Asseverazione tecnica"
summary: "Asseverazione tecnica ex ante / ex post per il credito d'imposta Piano Transizione 5.0 (calcolo riduzione consumi >=3% struttura o >=5% processo, conversione tep, modelli MIMIT)"
normative_refs:
  - "DL 19/2024 art. 38"
  - "DM MIMIT-MEF 24/7/2024"
  - "Circolare MIMIT 25877/2024"
version: 0.2.0
status: stable
tags:
  - transizione-5-0
  - credito-imposta
  - mimit
---

# Transizione 5.0 - Asseverazione tecnica EGE/ESCO/ingegnere/perito

## Quando usare questa skill

Usare quando un soggetto qualificato per il rilascio della certificazione tecnica del Piano Transizione 5.0 (EGE certificato UNI CEI 11339, ESCo certificata UNI CEI 11352, ingegnere sez. A/B, perito industriale "meccanica ed efficienza energetica" o "impiantistica elettrica ed automazione") chiede di:

- **Verificare l'ammissibilita'** di un progetto di innovazione al credito d'imposta Transizione 5.0 (ambito soggettivo, oggettivo, DNSH, attivita' escluse, scadenze).
- **Strutturare il calcolo della riduzione dei consumi energetici** della struttura produttiva (soglia minima 3%) o del processo interessato (soglia minima 5%), con baseline ex ante, normalizzazione, scenario controfattuale dove richiesto, conversione in tep secondo la circolare MISE 18/12/2014.
- **Predisporre la bozza della Certificazione Ex Ante** (Allegato VIII della circolare MIMIT 25877/2024) per la comunicazione preventiva al GSE.
- **Predisporre la bozza della Certificazione Ex Post** (Allegato X della circolare MIMIT 25877/2024) per la comunicazione di completamento al GSE entro il 28 febbraio 2026.
- **Strutturare la Relazione Tecnica** (Allegati IX ed XI) con dati registrati, variabili operative, indicatori di prestazione, algoritmo di calcolo dei risparmi, scenario controfattuale, DNSH.
- **Verificare la coerenza fra ex ante e ex post** in vista dei controlli GSE (art. 20 co. 2 lett. b DM 24/7/2024).

**Non usare** se l'utente chiede:

- Redazione della **perizia tecnica asseverata caratteristiche e interconnessione beni 4.0** (art. 16 DM 24/7/2024 + art. 1 co. 11 L. 232/2016): documento distinto, riservato a ingegnere o perito industriale (FAQ MIMIT 2.4), rilasciabile anche tramite **attestato di conformita'** da ente accreditato. Non e' la certificazione tecnica del risparmio energetico oggetto di questa skill.
- **Certificazione contabile** (art. 17 DM 24/7/2024): rilasciata da revisore legale dei conti.
- **Compilazione operativa del portale TR5 GSE**: la skill non sostituisce il "Manuale Utente Portale Transizione 5.0" del GSE.
- **Verifica preliminare 4.0 dei beni** (caratteristiche tecniche e interconnessione ai sensi degli allegati A/B L. 232/2016): rinvio a perizia di cui sopra.
- **Calcolo del credito d'imposta come adempimento fiscale**: la skill mostra le aliquote dell'art. 10 DM e fornisce un esempio di calcolo, ma il computo finale ai fini della compensazione F24 e' adempimento del consulente fiscale dell'impresa.
- **Pareri in materia di accreditamento EGE/ESCO**: la skill assume che il certificatore sia gia' qualificato.
- **Modifiche sostanziali al progetto** in corso d'opera: in tal caso (FAQ MIMIT 2.10) l'impresa deve rinunciare alla domanda e presentarne una nuova.

## Avvertenza

Questa skill e' uno strumento di supporto alla **redazione e verifica della certificazione tecnica** ex ante/ex post del Piano Transizione 5.0. **Non sostituisce il giudizio professionale del valutatore indipendente firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente.

> **ATTENZIONE - vigenza normativa**: la versione 0.1.0-alpha della skill e' costruita sul testo del DL 19/2024 + DM 24/7/2024 + circolare MIMIT 25877/2024 + FAQ MIMIT 10/4/2025. La **L. 207/2024 (Bilancio 2025) art. 1 co. 427-429** ha modificato il Piano Transizione 5.0 (semplificazioni procedurali, perimetro temporale, **possibili modifiche ad aliquote e fasce**). Eventuali DM correttivi successivi e FAQ MIMIT post 10/4/2025 possono ulteriormente modificare aliquote, soglie, perimetro. **Prima di applicare la skill su un caso reale verificare la vigenza** del set normativo consultato (`last_verified` di `references/sources.yaml`). In caso di disallineamento, **prevale il testo vigente** alla data dell'asseverazione.

La certificazione tecnica del Piano Transizione 5.0 e' resa ai sensi degli **artt. 46 e segg. del DPR 445/2000** e degli **artt. 359 e 481 del codice penale**. Il certificatore agisce in qualita' di **persona esercente un servizio di pubblica necessita'**: false attestazioni o mendaci dichiarazioni espongono a **responsabilita' penale aggravata** (art. 76 DPR 445/2000) oltre che a responsabilita' civile verso lo Stato e l'impresa beneficiaria, perdita dell'abilitazione al rilascio (art. 19 DM 24/7/2024) e revoca del beneficio.

La skill non produce documenti pronti al deposito, alla firma digitale o al caricamento sul portale TR5 GSE: ogni output **deve essere riveduto, integrato e firmato dal valutatore indipendente** dotato di idonea copertura assicurativa (art. 15 co. 8 DM 24/7/2024).

## Sotto-attivita' disponibili

Questa skill supporta quattro sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Verifica ammissibilita' del progetto**: l'utente chiede "il mio progetto e' ammissibile a Transizione 5.0?", "che requisiti soggettivi e oggettivi devo verificare?", "il mio investimento rispetta il DNSH?" -> leggi [`tasks/verifica-ammissibilita.md`](tasks/verifica-ammissibilita.md)
- **Calcolo riduzione consumi energetici**: l'utente chiede "come calcolo la riduzione dei consumi del 3% o 5%?", "come imposto la baseline ex ante?", "come converto in tep?", "come applico la normalizzazione?", "come imposto lo scenario controfattuale?" -> leggi [`tasks/calcola-riduzione-consumi.md`](tasks/calcola-riduzione-consumi.md)
- **Struttura Certificazione Ex Ante**: l'utente chiede "scrivi la bozza di certificazione ex ante", "cosa devo asseverare nella ex ante?", "quali contenuti minimi prevede l'Allegato VIII?", "come strutturo la relazione tecnica ex ante (Allegato IX)?" -> leggi [`tasks/struttura-certificazione-ex-ante.md`](tasks/struttura-certificazione-ex-ante.md)
- **Struttura Certificazione Ex Post**: l'utente chiede "scrivi la bozza di certificazione ex post", "come dimostro l'effettiva riduzione dei consumi?", "come confronto i dati ex post con quelli asseverati ex ante?", "come gestisco eventuali scostamenti o modifiche al progetto?" -> leggi [`tasks/struttura-certificazione-ex-post.md`](tasks/struttura-certificazione-ex-post.md)

Se la richiesta non e' chiara, chiedi all'utente in quale **fase** del Piano si trova (prenotazione del credito / comunicazione di completamento) e quali **dati di inquadramento** del progetto sono gia' disponibili (tipologia investimento, perimetro su struttura produttiva o processo, soggetto certificatore qualificato).

## Processo generale

1. **Inquadra il certificatore**: chi e' (EGE, ESCo, ingegnere sez. A/B, perito industriale)? La sua certificazione/iscrizione e' in corso di validita'? Ha dichiarato la terzieta' rispetto all'impresa beneficiaria (Allegato III)?
2. **Inquadra il progetto**: tipologia investimenti (beni 4.0 art. 6, autoproduzione FER art. 7, formazione art. 8), avvio (>=1/1/2024), completamento (<=31/12/2025), tetto 50 mln EUR/anno, perimetro (struttura produttiva o processo interessato).
3. **Identifica la sotto-attivita'**: usa il routing della sezione "Sotto-attivita' disponibili".
4. **Carica il task file** corrispondente.
5. **Applica la procedura** descritta nel task, citando precisamente articolo, comma e fonte normativa per ogni affermazione (es. "art. 9 co. 1 DM 24/7/2024", "circolare MIMIT 25877/2024 cap. 2.1", "FAQ MIMIT 10/4/2025 - 2.10").
6. **Produci l'output** nel formato indicato dal task, con riferimento ai modelli ufficiali Allegati VIII/IX/X/XI.
7. **Concludi** sempre con:
   - elenco di **elementi non automaticamente verificabili** dalla skill (sopralluogo fisico, taratura strumenti di misura, indipendenza del certificatore, idoneita' polizza assicurativa);
   - rinvio alla **revisione e firma del valutatore indipendente** ai sensi dell'art. 15 DM 24/7/2024;
   - segnalazione del **rischio penale** (artt. 359, 481 c.p. + art. 76 DPR 445/2000) e della **conservazione obbligatoria** della documentazione probatoria per 5 anni (art. 19 DM 24/7/2024).

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:

- **DL 2 marzo 2024 n. 19** art. 38 (convertito da L. 56/2024) - istituzione Piano Transizione 5.0
- **DM MIMIT-MEF 24 luglio 2024** - decreto attuativo (GU n. 183 del 06/08/2024, codice 24A04160)
- **Circolare operativa MIMIT 16 agosto 2024 prot. 25877** - chiarimenti tecnici e modelli vincolanti delle certificazioni (Allegati VIII, IX, X, XI)
- **FAQ MIMIT** - aggiornamento 10 aprile 2025 (versione vigente)
- **GSE - Portale Transizione 5.0** - Regole operative + Manuale utente
- **Circolare MISE 18 dicembre 2014** - coefficienti di conversione in tep ex art. 19 L. 10/1991

Fonti di rinvio:
- **UNI CEI 11339:2009** - EGE (norma proprietaria, requisiti del certificatore)
- **UNI CEI 11352:2014** - ESCo (norma proprietaria, requisiti del certificatore)
- **L. 232/2016** allegati A e B - beni 4.0
- **DPR 445/2000** artt. 46-76 - DSAN e sanzioni penali per false dichiarazioni
- **Codice penale** artt. 359, 481 - persona esercente servizio di pubblica necessita' / falsita' ideologica in certificati
- **Regolamento UE 2020/852** art. 17 - principio DNSH

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dl-19-2024-art-38.md`](references/estratti/dl-19-2024-art-38.md) - inquadramento del Piano e soglie minime
- [`dm-24-07-2024-articoli-chiave.md`](references/estratti/dm-24-07-2024-articoli-chiave.md) - articoli chiave del decreto attuativo
- [`circolare-mimit-criteri-risparmio.md`](references/estratti/circolare-mimit-criteri-risparmio.md) - criteri tecnici di calcolo, definizioni di struttura produttiva e processo interessato
- [`circolare-mimit-modelli-certificazioni.md`](references/estratti/circolare-mimit-modelli-certificazioni.md) - modelli Allegati VIII, IX, X, XI
- [`faq-mimit-soggetti-certificatori.md`](references/estratti/faq-mimit-soggetti-certificatori.md) - FAQ MIMIT chiave
- [`circolare-mise-2014-tep.md`](references/estratti/circolare-mise-2014-tep.md) - coefficienti di conversione in tep

## Limiti

Cosa questa skill NON fa:

- Non e' la **perizia tecnica asseverata** caratteristiche e interconnessione beni 4.0 (art. 16 DM, art. 1 co. 11 L. 232/2016): adempimento distinto, riservato a ingegnere/perito o certificato di conformita' di ente accreditato.
- Non e' la **certificazione contabile** (art. 17 DM): adempimento del revisore legale.
- Non valida l'**indipendenza, imparzialita', onorabilita', professionalita'** del certificatore: la skill assume che il certificatore stia rendendo la dichiarazione di terzieta' (Allegato III) in modo veritiero. La verifica e' del MIMIT/GSE in sede di vigilanza.
- Non sostituisce il **sopralluogo fisico** presso la struttura produttiva, espressamente richiesto dai modelli di certificazione (Allegato VIII e X).
- Non valuta l'**adeguatezza tecnica** delle scelte progettuali, dell'idoneita' delle macchine 4.0 alle specifiche dell'allegato A/B L. 232/2016 (requisito di interconnessione, capacita' di scambio dati con ERP, etc.).
- Non riproduce il **testo completo** delle norme UNI CEI 11339 e 11352 (proprietarie a pagamento). Cita solo l'inquadramento normativo che richiede tali certificazioni.
- Non aggiorna automaticamente i **coefficienti di conversione tep**, le aliquote, le soglie a fronte di modifiche normative successive (es. L. 207/2024 Bilancio 2025 ed eventuali DM correttivi). Verificare `last_verified` di `sources.yaml`.
- Non gestisce le **interazioni operative con il portale TR5 GSE** (registrazione, SPID, upload documenti, codice TR5-XXXXX): rinvio al Manuale Utente GSE.
- Non valuta il **cumulo con altre agevolazioni** (es. Industria 4.0, ZES, contributi regionali): adempimento del consulente fiscale.
- Non interpreta le **modifiche sostanziali al progetto** (FAQ MIMIT 2.10): in tal caso l'impresa deve rinunciare e ripresentare. La skill segnala l'incompatibilita' ma non rinegozia il progetto.
- Non sostituisce le **schede DNSH** (Allegato VII della circolare): la skill richiama la loro obbligatorieta' ma il certificatore deve compilarle in autonomia con il beneficiario.

**Ogni output prodotto dalla skill e' supporto al valutatore indipendente, non sostituzione.** Il rischio penale (artt. 359 e 481 c.p. + art. 76 DPR 445/2000) e civile resta in capo al certificatore firmatario.
