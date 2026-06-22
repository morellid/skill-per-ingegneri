---
name: denuncia-opere-strutturali-l1086
description: Guida la decisione su quale adempimento strutturale e sismico applicare a un intervento edilizio in Italia secondo il DPR 380/2001 (denuncia opere c.a./c.a.p./metalliche art. 65, collaudo statico art. 67, preavviso in zona sismica art. 93, autorizzazione preventiva art. 94, classificazione rilevante/minore rilevanza/priva di rilevanza art. 94-bis). Use when the user has an Italian construction or structural intervention and needs to figure out which structural/sismic filing applies, what to attach, and to whom.
license: MIT
area: edilizia-urbanistica-catasto
title: "Denuncia opere strutturali e autorizzazione sismica - DPR 380/2001"
summary: "Decision tree statale per stabilire quali adempimenti DPR 380/2001 si applicano a un intervento: art. 65 c.a./c.a.p./metalliche, art. 67 collaudo, artt. 93-94-94bis zona sismica. Per ingegneri, direttori dei lavori, costruttori."
normative_refs:
  - "DPR 6 giugno 2001 n. 380 - art. 65 (denuncia opere c.a./c.a.p./metalliche)"
  - "DPR 6 giugno 2001 n. 380 - art. 67 (collaudo statico)"
  - "DPR 6 giugno 2001 n. 380 - artt. 83, 93, 94, 94-bis (zona sismica)"
  - "DL 18 aprile 2019 n. 32 conv. L. 14 giugno 2019 n. 55 (introduzione art. 94-bis)"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-380
  - denuncia-strutture
  - zona-sismica
  - collaudo-statico
  - sportello-unico-edilizia
---

# Denuncia opere strutturali e autorizzazione sismica - DPR 380/2001

## Quando usare questa skill

Quando l'utente sta progettando o accompagnando un intervento edilizio o strutturale
in Italia e deve stabilire **quali pratiche strutturali e sismiche** servono prima
dell'avvio dei lavori (denuncia ex art. 65, preavviso ex art. 93, eventuale
autorizzazione preventiva ex art. 94, classificazione ex art. 94-bis) e quali
adempimenti seguono in fase di esecuzione e fine lavori (collaudo statico ex art. 67,
relazione a struttura ultimata ex art. 65 commi 6-8).

Target: ingegnere strutturista / direttore dei lavori / costruttore / responsabile
ufficio tecnico di un'impresa di costruzioni. **Non e' una skill di calcolo
strutturale**: assume che la progettazione tecnica sia gia' fatta o in corso e
risponde solo alla domanda procedurale "che cosa devo depositare, dove, quando,
firmato da chi".

Non e' adatta a:
- determinare il regime edilizio (PdC, SCIA, CILA, ...) - per quello vedi la skill
  `modulistica-edilizia-unificata`;
- classificare interventi al livello regionale toscano - per quello vedi
  `pratiche-edilizie-lr65-2014-toscana`;
- decidere se applicare adeguamento, miglioramento o intervento locale ai sensi NTC
  capitolo 8 - questa e' valutazione tecnica strutturale che resta in capo al
  progettista.

## Avvertenza

Questa skill e' uno strumento di supporto alla decisione procedurale. **Non
sostituisce il giudizio del progettista strutturale firmatario, del direttore dei
lavori e del collaudatore.** La classificazione di "intervento rilevante / minore
rilevanza / privo di rilevanza" ex art. 94-bis e' definita al livello regionale
nelle elencazioni adottate da ciascuna regione: la skill copre il quadro statale
del DPR 380; la classificazione puntuale richiede comunque la verifica della
disciplina regionale vigente nel comune di intervento. L'utilizzo improprio degli
output e' responsabilita' esclusiva dell'utente. La skill non produce documenti
pronti al deposito o alla firma.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Diagnosi adempimenti** (l'utente descrive un intervento e chiede "che pratiche
  devo fare?"): leggere `tasks/diagnosi-adempimenti-struttura.md`.
- **Checklist denuncia ex art. 65** (l'utente ha gia' deciso che deve fare la
  denuncia c.a./c.a.p./metalliche e chiede cosa allegare): leggere
  `tasks/checklist-denuncia-art-65.md`.
- **Checklist preavviso / autorizzazione zona sismica** (l'utente ha gia' deciso
  che il lavoro e' in zona sismica e chiede l'iter art. 93 / 94 / 94-bis):
  leggere `tasks/checklist-zona-sismica-art-93-94.md`.
- **Checklist collaudo statico ex art. 67**: leggere `tasks/checklist-collaudo-art-67.md`.

Se la richiesta dell'utente e' generica ("aiutami con la pratica del genio civile"
oppure "che devo fare per la denuncia"), parti dalla diagnosi.

## Processo generale

1. Identifica la sotto-attivita' (vedi sopra).
2. Carica il task file scelto.
3. Raccogli gli input descritti nel task (tipologia intervento, materiali, ubicazione,
   eventuale zona sismica, stato dell'edificio).
4. Applica la decision tree o la checklist del task, citando ad ogni passo l'articolo
   del DPR 380 da cui deriva il vincolo.
5. Produci l'output nel formato atteso dal task (riepilogo procedurale, tabella
   allegati, schema firme).
6. Concludi sempre con un rinvio alla verifica del professionista firmatario e alla
   disciplina regionale per la classificazione puntuale ex art. 94-bis.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Il testo verbatim degli articoli
DPR 380 rilevanti e' trascritto in `references/fonti/dpr-380-2001-testo-unico-edilizia.md`.
Sintesi operative in `references/estratti/`:

- `references/estratti/dpr-380-art-65-denuncia-ca.md` - denuncia opere
  c.a./c.a.p./metalliche;
- `references/estratti/dpr-380-art-67-collaudo.md` - collaudo statico;
- `references/estratti/dpr-380-artt-93-94-94bis-zone-sismiche.md` - preavviso,
  autorizzazione preventiva e classificazione interventi in zona sismica.

## Limiti

Cosa questa skill NON fa:

- Non produce documenti firmati pronti al deposito.
- Non valuta la complessita' strutturale: la classificazione di un intervento come
  "nuova costruzione che si discosta dalle usuali tipologie o per particolare
  complessita' strutturale" (art. 94-bis comma 1 lett. a n. 2) resta valutazione
  del progettista.
- Non sostituisce l'elencazione regionale ex art. 94-bis comma 2 che operativizza
  rilevante / minore rilevanza / priva di rilevanza in ciascuna regione.
- Non determina la zona sismica del comune (questo dato e' input dell'utente,
  reperibile dalla classificazione regionale o dai siti di Protezione Civile).
- Non sostituisce il direttore dei lavori, il collaudatore o il progettista
  strutturale firmatario.
- Non interpreta la disciplina di sanatoria per interventi gia' realizzati senza
  denuncia o senza autorizzazione (e' tema di disciplina sanzionatoria art. 95 e
  ss. DPR 380, non coperto in v0.1).
