---
name: via-screening-sia-dlgs152
description: "Supporto documentale alla Valutazione di Impatto Ambientale (VIA) ai sensi della Parte Seconda del D.Lgs. 152/2006 (testo vigente) e del DM 30/03/2015. Copre due fasi: (1) la verifica di assoggettabilita' a VIA (screening, art. 19) con la procedura e i termini perentori, la checklist dei contenuti dello Studio Preliminare Ambientale (Allegato IV-bis) e i criteri di decisione (Allegato V), incluse le linee guida per lo screening di competenza regionale (DM 30/03/2015, meccanismi di adeguamento delle soglie); (2) la struttura e la checklist di completezza dei contenuti dello Studio di Impatto Ambientale - SIA (Allegato VII, art. 22). Use when an Italian engineer or environmental consultant needs to plan the VIA screening procedure, check a Studio Preliminare Ambientale or a SIA for completeness against the current D.Lgs. 152/2006 requirements; it is a documentary aid and does not decide assoggettabilita' nor replace the authority or the signing professional."
license: MIT
area: ambiente-territorio-mobilita
title: "VIA - screening (art. 19) e SIA (Allegato VII) D.Lgs. 152/2006"
summary: "Supporto documentale VIA (D.Lgs. 152/2006 + DM 30/03/2015): procedura e termini della verifica di assoggettabilita' (art. 19), checklist dello Studio Preliminare Ambientale (All. IV-bis) e dei criteri (All. V), struttura/checklist del SIA (All. VII); non decide l'esito"
normative_refs:
  - "D.Lgs. 3/4/2006 n. 152 Parte Seconda - artt. 19, 22 + Allegati IV-bis, V, VII (testo vigente)"
  - "DM 30/03/2015 (linee guida verifica assoggettabilita' competenza regionale)"
version: 0.1.0-alpha
status: alpha
tags:
  - via
  - dlgs-152-2006
  - valutazione-impatto-ambientale
  - screening-assoggettabilita
  - studio-impatto-ambientale
---

# VIA - screening (art. 19) e SIA (Allegato VII) D.Lgs. 152/2006

## Quando usare questa skill

Usala quando devi, nell'ambito della Valutazione di Impatto Ambientale (VIA):

- pianificare la **verifica di assoggettabilita' a VIA** (screening) di un
  progetto: procedura, termini perentori, documenti (art. 19);
- verificare la **completezza dello Studio Preliminare Ambientale** rispetto
  all'Allegato IV-bis e ai criteri dell'Allegato V;
- impostare o verificare la **struttura dello Studio di Impatto Ambientale
  (SIA)** rispetto all'Allegato VII (i 12 punti dell'art. 22);
- orientarti sui **criteri e soglie per lo screening di competenza regionale**
  (DM 30/03/2015) e i meccanismi di adeguamento regionale.

Target: ingegneri ambientali, consulenti ambientali, proponenti e tecnici che
predispongono la documentazione VIA.

## Avvertenza

Questa skill e' un **supporto documentale**. **Non decide l'assoggettabilita' a
VIA** (competenza dell'autorita' competente), **non stabilisce se un progetto
specifico rientri negli allegati II-bis/IV** (per questo servono gli elenchi con
le soglie e le norme regionali) e **non sostituisce** i tecnici che redigono e
firmano lo Studio Preliminare Ambientale o il SIA. Fornisce procedura, termini e
checklist di completezza tratti dal testo vigente delle norme.

## Sotto-attivita' disponibili

- **Screening / verifica di assoggettabilita'**: pianificare il procedimento
  (art. 19) e verificare lo Studio Preliminare Ambientale (All. IV-bis + criteri
  All. V) -> `tasks/screening-verifica-assoggettabilita.md`
- **Checklist SIA**: verificare la struttura/completezza di uno Studio di Impatto
  Ambientale rispetto ai 12 punti dell'Allegato VII ->
  `tasks/checklist-sia.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input necessari (tipo di progetto, competenza statale/regionale,
   documento da verificare, ecc.).
4. Applica la procedura/checklist **citando l'articolo o l'allegato preciso**
   (art. 19, All. IV-bis, All. V, All. VII, DM 30/03/2015).
5. Distingui cio' che e' **cogente** (D.Lgs. 152/2006, DM) da cio' che dipende
   dalle **norme regionali** di adeguamento.
6. Chiudi con il rinvio all'autorita' competente e ai tecnici firmatari.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizioni verificate in
`references/fonti/`, estratto operativo in `references/estratti/`:

- `fonti/dlgs-152-2006-via.md` - D.Lgs. 152/2006 art. 19, All. IV-bis, V, VII
  (testo vigente da Normattiva, pagina indice pinnata `!vig=2026-07-14`)
- `fonti/dm-30-03-2015-via.md` - DM 30/03/2015 (linee guida screening regionale)
- `estratti/via-screening-sia-checklist.md` - checklist operative

## Limiti

Cosa questa skill NON fa:
- non contiene gli elenchi integrali dei progetti (allegati II-bis e IV) con le
  soglie dimensionali: per stabilire se un progetto rientri nello screening,
  consultare gli allegati alla Parte Seconda e il DM 30/03/2015 + norme regionali;
- non copre la procedura di VIA vera e propria (artt. 23-27), il PAUR (art.
  27-bis), la VAS (artt. 11-18) ne' la VIA statale (Commissione art. 8);
- non decide l'assoggettabilita' ne' redige gli studi: fornisce procedura e
  checklist di completezza.
