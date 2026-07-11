---
name: nis2-self-assessment
description: Supporta la self-assessment NIS2 per soggetti italiani ai sensi del D.Lgs. 138/2024. Aiuta a determinare se l'organizzazione rientra nel perimetro come "soggetto essenziale" o "soggetto importante", a impostare la gap analysis rispetto alle misure di base ACN (Determinazione 379907/2025, vigente dal 15/01/2026), a preparare l'elenco dei fornitori rilevanti NIS richiesto dall'art. 18 Det. ACN 127437/2026 (finestra annuale 15 aprile - 31 maggio), a verificare gli obblighi di notifica di incidenti significativi al CSIRT Italia e gli obblighi di governance dell'organo di amministrazione. Per i soggetti inseriti nell'elenco per la prima volta nel 2026 si applicano i termini speciali della Det. ACN 127434/2026 (misure entro 31/07/2027; notifica incidenti dal 01/01/2027). Use when an Italian organization (private or public) asks whether and how NIS2 applies to it, needs a structured self-assessment of perimeter and minimum measures, must prepare the annual list of "fornitori rilevanti NIS" for the ACN platform, or wants to plan the path to compliance. Target users are CISO, IT manager, DPO, ingegneri dell'informazione e consulenti cybersecurity di organizzazioni italiane potenzialmente in ambito NIS.
license: MIT
area: software-dati-cybersecurity
title: "NIS2 self-assessment (D.Lgs. 138/2024)"
summary: "Self-assessment NIS2 (perimetro, gap analysis misure ACN, elenco fornitori rilevanti, notifica incidenti, governance)"
normative_refs:
  - "D.Lgs. 138/2024"
  - "Det. ACN 379907/2025"
  - "Det. ACN 127437/2026"
  - "Det. ACN 127434/2026"
version: 0.2.1-alpha
status: alpha
tags:
  - nis2
  - dlgs-138-2024
  - acn
---

# NIS2 self-assessment (D.Lgs. 138/2024)

## Quando usare questa skill

Usare quando un'organizzazione italiana (privata o pubblica), o un consulente cybersecurity / ingegnere dell'informazione che la supporta, deve:
- Determinare se rientra nel perimetro NIS2 come **soggetto essenziale**, **soggetto importante** o se e' **fuori ambito** (art. 3 e 6, Allegati I-IV del D.Lgs. 138/2024)
- Impostare una **gap analysis** delle misure di sicurezza esistenti rispetto alle misure di base previste dalla Determinazione ACN 379907/2025 (vigente dal 15/01/2026, sostitutiva della 164179/2025): Allegato 1 per soggetti importanti, Allegato 2 per soggetti essenziali
- Preparare l'**elenco dei fornitori rilevanti NIS** richiesto dall'art. 18 della Determinazione ACN 127437/2026, da comunicare tramite il "Servizio NIS/Aggiornamento annuale informazioni" sulla piattaforma ACN nella finestra annuale **15 aprile - 31 maggio** (prima applicazione: 2026)
- Verificare se un evento subito **e' un incidente significativo** ai sensi dell'art. 25 D.Lgs. 138/2024 e quali tempistiche di notifica al CSIRT Italia si applicano
- Verificare gli **obblighi sull'organo di amministrazione** (art. 23): approvazione delle modalita' di implementazione, formazione, responsabilita' personale per le violazioni

**Non usare** quando l'utente chiede:
- Pareri legali su singole interpretazioni del decreto (richiede legale specializzato in cybersecurity)
- Stesura tecnica di policy specifiche di sicurezza (questa skill produce gap analysis, non i deliverable)
- Risposte a richieste di audit ACN gia' avviato (richiede consulenza specialistica)
- Compliance al Regolamento UE 2024/2690 oltre il riferimento di ambito (la skill gestisce il quadro italiano ACN, non la specifica tecnica europea per cloud/DNS/data center)
- Compliance NIS2 di soggetti non italiani (la skill e' tarata sul recepimento italiano e sulle determinazioni ACN)

## Avvertenza

Questa skill e' uno strumento di supporto alla self-assessment NIS2. **Non sostituisce il giudizio del CISO, del responsabile compliance, del consulente cybersecurity o del legale.** L'esito della self-assessment di perimetro e' una valutazione orientativa: la classificazione ufficiale e' quella che il soggetto registra sulla piattaforma ACN sotto la propria responsabilita' (art. 7 D.Lgs. 138/2024). La gap analysis non sostituisce un audit di conformita'. La verifica di significativita' di un incidente non sostituisce la decisione di notifica, che resta in capo al soggetto e al suo punto di contatto NIS. **Sanzioni amministrative ex art. 38 D.Lgs. 138/2024** si applicano in caso di violazione: la skill non fornisce difesa legale.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Valutazione del perimetro NIS2**: l'utente chiede "siamo soggetti NIS2?", "siamo essenziali o importanti?", "rientriamo nell'ambito?" -> leggi [`tasks/valuta-perimetro.md`](tasks/valuta-perimetro.md)
- **Gap analysis misure di base**: l'utente chiede "siamo conformi alle misure ACN?", "che gap abbiamo rispetto alla Determinazione 379907?" (o, in domande riferite alla precedente Det. 164179/2025 ora superata, "rispetto alla 164179?") -> leggi [`tasks/gap-analysis-misure.md`](tasks/gap-analysis-misure.md)
- **Elenco fornitori rilevanti NIS**: l'utente chiede "quali fornitori dobbiamo comunicare ad ACN?", "come compiliamo l'art. 18 della 127437?", "fornitori rilevanti NIS", "fornitori ICT da comunicare", "scadenza 31 maggio fornitori ACN" -> leggi [`tasks/elenco-fornitori-rilevanti.md`](tasks/elenco-fornitori-rilevanti.md)
- **Verifica incidente significativo**: l'utente chiede "questo incidente va notificato?", "quali tempistiche di notifica si applicano?" -> leggi [`tasks/verifica-incidente-significativo.md`](tasks/verifica-incidente-significativo.md)
- **Obblighi organo di amministrazione**: l'utente chiede "che obblighi ha il CdA?", "che formazione devono fare i dirigenti?" -> leggi [`tasks/check-obblighi-governance.md`](tasks/check-obblighi-governance.md)

Se la richiesta e' generica ("aiutami con NIS2"), chiedi all'utente quale delle cinque azioni vuole svolgere. La sequenza logica naturale e': prima `valuta-perimetro`, poi (se in ambito) `gap-analysis-misure` + `check-obblighi-governance` + `elenco-fornitori-rilevanti` (annuale, nella finestra 15 aprile - 31 maggio), infine `verifica-incidente-significativo` quando occorre.

## Processo generale

1. Identifica la sotto-attivita' richiesta.
2. Carica il task file specifico in `tasks/`.
3. Acquisisci dall'utente i dati necessari (settore, dimensioni, asset critici, stato delle misure, dati incidente, ecc.).
4. Applica la procedura del task, citando sempre l'articolo o l'allegato di riferimento.
5. Produci output strutturato (classificazione, gap analysis, raccomandazione di notifica, checklist governance).
6. Concludi sempre con rinvio al CISO / compliance / legale.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- D.Lgs. 4 settembre 2024, n. 138 (recepimento NIS 2 in Italia) - in particolare art. 2 (definizioni), art. 3 (ambito di applicazione), art. 6 (perimetro essenziali/importanti), art. 7 (registrazione piattaforma ACN), art. 23 (organi di amministrazione), art. 24 (misure di gestione del rischio), art. 25 (notifica incidenti), art. 38 (sanzioni) e Allegati I-IV
- Direttiva (UE) 2022/2555 (NIS 2) - direttiva madre
- Regolamento di esecuzione (UE) 2024/2690 - solo per il sottoinsieme di soggetti coperti direttamente (DNS, cloud, data center, social, ecc.)
- Determinazione ACN n. 379907/2025 del 18/12/2025 (vigente dal 15/01/2026, sostitutiva della Det. 164179/2025) - misure di base e codici di "incidente significativo di base" (IS-1..4)
- Determinazione ACN n. 127437/2026 del 13/04/2026 (vigente dal 15/04/2026, Capo V dal 01/05/2026) - termini, modalita' e procedimenti di utilizzo della piattaforma digitale ACN; art. 18 sull'**elenco dei fornitori rilevanti NIS** (finestra annuale 15 aprile - 31 maggio); definizione di "fornitore rilevante" all'art. 1 lett. ll)
- Determinazione ACN n. 127434/2026 del 13/04/2026 (vigente dal 30/04/2026) - termini speciali per i **soggetti inseriti per la prima volta nel 2026**: misure entro 31/07/2027 (art. 1 co. 1) e notifica incidenti significativi dal 01/01/2027 (art. 1 co. 2)

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non produce documenti pronti per la registrazione sulla piattaforma ACN o per la notifica al CSIRT Italia
- Non sostituisce l'audit di conformita' ne' il parere di un consulente cybersecurity
- Non valuta la conformita' al Regolamento UE 2024/2690 nel dettaglio dei requisiti tecnici per cloud/DNS/data center (rinvio ENISA technical guidance)
- Non gestisce le sovrapposizioni con altre normative settoriali (DORA per il finanziario, codice delle comunicazioni elettroniche per i telco) oltre la segnalazione che esistono
- Non sostituisce la designazione e i compiti del punto di contatto NIS sulla piattaforma ACN
- Non fornisce difesa legale in caso di sanzione

**Ogni output richiede revisione del CISO, del responsabile compliance o del consulente cybersecurity prima di essere usato per decisioni operative o per la registrazione/notifica sulla piattaforma ACN.**
