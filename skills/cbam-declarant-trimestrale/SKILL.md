---
name: cbam-declarant-trimestrale
description: Supporta il dichiarante CBAM autorizzato negli adempimenti della fase definitiva (Reg. UE 2023/956 dal 1/1/2026, modificato dal Reg. UE 2025/2083) - verifica della qualifica e applicabilita' delle deroghe, pianificazione dell'obbligo trimestrale 50 % sui certificati CBAM (Art. 22 §2 dal 2027), redazione della dichiarazione CBAM annuale (Art. 6, entro 30/9 - prima volta 2027 per anno 2026), valutazione dell'esposizione sanzionatoria (Art. 26). Use when user asks about CBAM authorized declarant obligations, quarterly 50% balance, annual CBAM declaration, soglia 50 t, deroga 31/3/2026, Y128/Y134-Y238 TARIC codes, or CBAM sanctions.
license: MIT
---

# CBAM Declarant Trimestrale - Reg. (UE) 2023/956 fase definitiva

## Quando usare questa skill

Usare questa skill quando un soggetto - importatore stabilito UE o
rappresentante doganale indiretto - deve adempiere agli obblighi del CBAM
nella fase definitiva (dal **1° gennaio 2026**), con particolare attenzione a:

- verifica della necessita' della qualifica di dichiarante CBAM autorizzato
  rispetto all'**esenzione de minimis** (Art. 2bis, **soglia 50 t/anno civile**
  cumulativi su ferro/acciaio, alluminio, fertilizzanti, cemento);
- gestione della **deroga transitoria Art. 17 §7bis** per chi ha presentato
  domanda entro il 31 marzo 2026 (codice TARIC **Y238**, utilizzabile fino al
  27 settembre 2026);
- pianificazione dell'**obbligo trimestrale del 50 %** di certificati CBAM sul
  conto del dichiarante (Art. 22 §2, applicabile **dal 1° gennaio 2027**);
- supporto alla redazione della **dichiarazione CBAM annuale** (Art. 6,
  presentazione entro il 30 settembre, prima volta nel 2027 per l'anno 2026);
- valutazione dell'**esposizione sanzionatoria** (Art. 26 §§1, 1bis, 2, 2bis,
  4bis) per mancata restituzione, restituzione incompleta o importazione non
  autorizzata.

**Target utente**: importatore di merci CBAM stabilito UE, rappresentante
doganale indiretto, responsabile dogane/compliance, consulente fiscale o legale
che li supporta. Non destinata a operatori extra-UE, gestori di impianti paesi
terzi (lato Art. 10), verificatori accreditati o autorita' competenti.

NON usare la skill per:

- predisporre la **domanda di autorizzazione** nel registro CBAM (Art. 5
  §§5-7): la skill ha contesto normativo ma il flusso procedurale e' definito
  dal MASE e dal Reg. di esecuzione (UE) 3210/2024, fuori scope di livello 1;
- calcolare le **emissioni incorporate effettive** per la metodologia di
  Allegato IV punti 2-3 (richiede dati impianto del gestore paese terzo,
  verifica Art. 8): la skill puo' usare valori predefiniti ma non calcola
  emissioni effettive;
- adempimenti **non-CBAM** correlati (Reg. 2023/957 EU ETS settori marittimo,
  dazi anti-dumping, Reg. UE 1186/2009 franchigie, ecc.);
- attivita' di **verificatore accreditato** (Art. 18, Reg. esec. UE
  2018/2067): fuori scope.

## Avvertenza

Questa skill e' uno strumento di **supporto** agli adempimenti CBAM. **Non
sostituisce il giudizio del professionista responsabile** (responsabile
compliance, consulente doganale/fiscale, rappresentante legale del dichiarante
CBAM autorizzato). Le interpretazioni su:

- qualificazione di "importatore" ai fini CBAM (Art. 3 punto 15) per
  procedure semplificate;
- applicabilita' dell'esenzione de minimis (Art. 2bis) in caso di importazioni
  miste, perfezionamenti attivi/passivi, reintroduzioni;
- pratiche di **elusione** (Art. 27 §2 lettera b, accordi non genuini di
  frazionamento);
- riconducibilita' a "merci destinate ad attivita' militari" (Art. 2 §3);
- determinazione del **prezzo del carbonio pagato in paese terzo** (Art. 9)
  per detrazione certificati;

sono **di esclusiva responsabilita' del professionista**. La skill non produce
documenti pronti al deposito presso il registro CBAM ne' ai fini doganali in
ADM, ne' attestazioni di conformita'.

## Sotto-attivita' disponibili

Questa skill supporta quattro sotto-attivita'. In base alla richiesta
dell'utente, caricare il file appropriato da `tasks/`:

- **Verifica della qualifica e applicabilita' delle deroghe** - quando
  l'utente chiede di valutare se serve la qualifica di dichiarante CBAM
  autorizzato, se si applica l'esenzione de minimis (Art. 2bis), o quale
  codice TARIC dichiarativo utilizzare (Y128 vs Y134-Y137-Y237-Y238): leggere
  `tasks/check-qualifica-e-deroghe.md`.
- **Pianificazione equilibrio trimestrale 50 %** - quando l'utente chiede di
  stimare l'obbligo trimestrale Art. 22 §2 (dal 2027), il numero di certificati
  CBAM da detenere a fine trimestre o le tempistiche di acquisto su piattaforma
  centrale: leggere `tasks/plan-equilibrio-trimestrale.md`.
- **Redazione dichiarazione CBAM annuale** - quando l'utente chiede supporto
  per strutturare la dichiarazione annuale Art. 6 (per la prima volta entro
  30/9/2027 per le importazioni 2026), inclusi contenuti obbligatori e
  coerenza con dichiarazione doganale: leggere `tasks/draft-dichiarazione-cbam-annuale.md`.
- **Valutazione esposizione sanzionatoria** - quando l'utente chiede una
  mappa delle sanzioni Art. 26 applicabili a un caso specifico (mancata
  restituzione, importazione non autorizzata sopra soglia, deroga Art. 17 §7bis
  respinta): leggere `tasks/assess-rischio-sanzionatorio.md`.

Se la richiesta non e' chiara, chiedere all'utente quale sotto-attivita'
desidera. Per casi complessi, suggerire la sequenza: qualifica/deroghe ->
trimestrale -> dichiarazione annuale -> sanzioni (cross-cutting).

## Processo generale

1. Identifica con l'utente il **soggetto** (importatore stabilito UE, rdi,
   ente UE non stabilito) e l'**ambito merceologico** (settori CBAM coinvolti:
   ferro/acciaio, alluminio, fertilizzanti, cemento, elettricita', idrogeno).
2. Identifica la sotto-attivita' richiesta e carica
   `tasks/<task-scelto>.md`.
3. Richiedi gli input documentali/operativi come specificato nel task
   (volumi di importazione, codici NC, paesi di origine, numero di conto CBAM
   o numero di domanda, dati su prezzo carbonio paese terzo se rilevante).
4. Applica la procedura descritta nel task, citando sempre **articolo e
   paragrafo** del Reg. (UE) 2023/956 consolidato (`▼M1` indica modifiche del
   Reg. UE 2025/2083) e, dove pertinente, della Circolare ADM 36/2025.
5. Produci l'output nel formato indicato dal task.
6. Includi sempre nel report finale: (a) avvertenza standard che il giudizio
   finale spetta al professionista responsabile; (b) elenco esplicito dei
   punti che richiedono verifica/decisione del professionista; (c) rinvio al
   testo committato in `references/fonti/` per il riscontro testuale di ogni
   articolo citato.

## Fonti normative

- **Regolamento (UE) 2023/956** del Parlamento europeo e del Consiglio del
  10/05/2023 (CBAM), testo consolidato 20/10/2025 che integra il Reg. (UE)
  2025/2083. Trascrizione fedele degli articoli della fase definitiva in
  `references/fonti/reg-ue-2023-956-cbam-consolidato.md`. Estratti curati per
  fase del ciclo del dichiarante CBAM autorizzato in
  `references/estratti/reg-ue-2023-956-articoli-fase-definitiva.md`.
- **Regolamento (UE) 2025/2083** (Omnibus CBAM) dell'8/10/2025. Trascrizione
  in `references/fonti/reg-ue-2025-2083-cbam-omnibus.md`. Estratti dei
  considerando chiave in
  `references/estratti/reg-ue-2025-2083-considerando-chiave.md`.
- **Circolare ADM n. 36/2025** del 24/12/2025 (avvio fase definitiva,
  adempimenti). Trascrizione in `references/fonti/circ-adm-36-2025-cbam.md`.
  Estratti operativi (codici TARIC) in
  `references/estratti/circ-adm-36-2025-codici-taric.md`.
- **Avviso ADM** del 21/10/2025 (conseguenze non conformita'). Trascrizione in
  `references/fonti/avviso-adm-cbam-211025.md`. Estratti in
  `references/estratti/avviso-adm-conseguenze-non-conformita.md`.

Riferimenti completi (SHA256, URL, accessed) in `references/sources.yaml`.

Fuori scope di questa skill ma rilevanti per uso operativo:
- **Reg. di esecuzione (UE) 3210/2024** - registro CBAM: gestione domanda,
  conti, restituzione. Procedura via interfaccia del registro CBAM presso la
  Commissione UE.
- **Direttiva 2003/87/CE** (EU ETS) Art. 16 §§3-4 - **importo base sanzione**
  per quota mancante (€100/quota indicizzato). Rinvio testuale: l'importo di
  sanzione Art. 26 §1 Reg. CBAM coincide con quello ETS.
- **Reg. UE 952/2013 (CDU)** Artt. 18 (rappresentante doganale indiretto), 38
  (AEO), 46 (controlli), e Reg. del. (UE) 2015/2446 Art. 175 §5 (conto di
  appuramento).
- Atti delegati e di esecuzione adottati ai sensi degli artt. 2 §§10-11, 2bis
  §3, 7 §7, 9 §5, 14 §6, 18 §3, 20 §§5bis-6, 21 §3, 27 §6 del Reg. CBAM
  consolidato (in continua evoluzione).

## Limiti

Cosa questa skill NON fa:

- Non produce **documenti pronti al deposito** nel registro CBAM (domanda di
  autorizzazione, dichiarazione CBAM annuale, richiesta riacquisto) ne'
  attestazioni di conformita'.
- Non sostituisce il giudizio del professionista responsabile sui confini
  interpretativi (importatore ai fini CBAM, esenzione de minimis su
  importazioni miste, qualificazione di pratiche di elusione).
- Non determina l'**ambito merceologico** caso per caso (Allegato I): il
  matching codice NC -> CBAM e' attivita' di classificazione doganale che
  spetta al dichiarante.
- Non calcola **emissioni effettive** ex Allegato IV punti 2-3 (richiede dati
  impianto del gestore paese terzo + verifica Art. 8).
- Non calcola l'**adeguamento per assegnazione gratuita** Art. 31: la formula
  e' definita da atti di esecuzione e dipende dal phase-out delle quote ETS
  free, in evoluzione.
- Non gestisce la **detrazione del prezzo del carbonio paese terzo** Art. 9
  oltre l'inquadramento (richiede documentazione specifica e persona
  indipendente che certifica).
- Non sostituisce la consulenza del MASE (autorita' competente nazionale) sul
  procedimento autorizzatorio, ne' la consulenza di ADM su questioni
  prettamente doganali (perfezionamenti attivi/passivi, reintroduzioni,
  origine).
- Non valuta gli **atti delegati/esecutivi** di secondo livello in costante
  aggiornamento (sono rinviati al testo dell'atto pubblicato in GUUE).
