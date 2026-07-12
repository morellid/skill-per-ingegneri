---
name: relazione-cam-dm-24-11-2025
description: Supporta la redazione e la verifica della Relazione CAM di progetto (criterio 2.1.1 dell'Allegato 1 al DM MASE 24/11/2025, in vigore dal 2/2/2026, che abroga e sostituisce il DM 256/2022) secondo il modello ufficiale MASE del 2/2/2026. Determina il regime applicabile (nuovo DM vs regime transitorio DM 256/2022 ex art. 2 e circolare MASE 10/4/2026), identifica i criteri applicabili all'intervento (clausole contrattuali 2.1, specifiche 2.2-2.5, premianti 2.6/3.2/4.3) con la tabella di applicabilita' e le Schede Tipo del modello MASE, genera la struttura della relazione per ogni livello di progettazione (dal PFTE), oppure verifica una relazione esistente. Use when an architect, civil engineer or technical consultant must draft or review the CAM report for public works tenders under the Italian DM 24 novembre 2025 (CAM edilizia).
license: MIT
area: appalti-opere-pubbliche
title: "Relazione CAM di progetto (DM 24.11.2025)"
summary: "Redazione e verifica della Relazione CAM di progetto ex criterio 2.1.1 DM MASE 24/11/2025 (CAM edilizia in vigore dal 2/2/2026): regime applicabile (nuovo DM vs transitorio), tabella di applicabilita' e Schede Tipo del modello MASE, check di relazioni esistenti"
normative_refs:
  - "DM MASE 24/11/2025 (CAM edilizia, GU n. 281/2025)"
  - "Circolare MASE 10/4/2026"
  - "Modello MASE Relazione CAM 2/2/2026"
  - "D.Lgs. 36/2023 art. 57"
version: 1.0.0-alpha
status: alpha
tags:
  - cam
  - dm-24-11-2025
  - appalti-verdi
  - gpp
---

# Relazione CAM di progetto (DM 24.11.2025) - redazione e verifica

## Quando usare questa skill

Usare quando un **progettista (architetto, ingegnere civile, consulente tecnico)** incaricato di una commessa pubblica deve:

- **Stabilire il regime CAM applicabile** alla propria procedura: DM 24/11/2025 (bandi/inviti dal 2/2/2026) oppure regime transitorio DM 256/2022 (art. 2 DM 24/11/2025 + circolare MASE 10/4/2026).
- **Identificare i criteri CAM applicabili** all'intervento (costruzione, ristrutturazione, manutenzione, adeguamento, opere di ingegneria civile) secondo le regole di capitolo e le "Indicazioni al progettista" dei singoli criteri dell'Allegato 1.
- **Redigere la bozza della Relazione CAM di progetto** (criterio 2.1.1) secondo il modello ufficiale MASE (versione 2/2/2026): sezioni normativa / progetto / allegati, tabella di applicabilita' dei criteri (Tabella 1), Scheda Tipo per ogni criterio applicato.
- **Verificare una Relazione CAM esistente** per completezza e conformita' al DM 24/11/2025: criteri mancanti, esclusioni non motivate tecnicamente, mezzi di prova assenti o inammissibili (es. "certificazioni CAM" di prodotto, vietate dal par. 1.3.5).

**Quando NON usare questa skill:**

- Progettazione per soggetti fuori dal perimetro dei soggetti obbligati (Allegato 1, premessa: stazioni appaltanti, enti concedenti, concessionari e privati che eseguono opere di urbanizzazione a scomputo).
- **Infrastrutture stradali**: si applicano i CAM strade (DM 5/8/2024 CAM infrastrutture stradali, richiamato dal par. 1.1 dell'Allegato 1), non questa skill.
- Altre categorie merceologiche CAM (verde pubblico, arredo urbano, illuminazione pubblica, ecc.): ogni categoria ha il proprio DM; il modello MASE chiede solo di citarli nella sezione normativa della relazione.
- **Relazione CAM dell'impresa appaltatrice** (criterio 3.1.1): documento distinto, redatto dall'impresa in corso d'opera; la skill lo segnala ma non lo genera.
- Calcoli energetici (APE, D.Lgs. 192/2005), studi LCA veri e propri, verifica urbanistico-edilizia, procedura di gara e punteggi OEPV: adempimenti distinti (la skill identifica i criteri premianti ma non costruisce la griglia di valutazione).

## Avvertenza

Questa skill e' uno strumento di supporto alla **redazione e verifica della Relazione CAM di progetto**. **Non sostituisce il giudizio del progettista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti alla firma o al deposito nella piattaforma di gara.

> **ATTENZIONE - vigenza normativa**: la skill e' costruita sul **DM MASE 24/11/2025** (GU n. 281 del 3/12/2025), **in vigore dal 2/2/2026**, che **abroga il DM 256/2022 e il correttivo DM 5/8/2024** (art. 4). Il regime transitorio (art. 2 + circolare MASE 10/4/2026) mantiene il DM 256/2022 solo per procedure con PFTE/progetto esecutivo validato in conformita' al vecchio DM e bando/avviso entro tre mesi dalla validazione. Il MASE puo' aggiornare modulistica e chiarimenti: verificare `last_verified` in `references/sources.yaml` e la pagina MASE "CAM vigenti" prima di applicare la skill a una gara reale. In caso di disallineamento **prevale il testo vigente** alla data di pubblicazione del bando.

I CAM edilizia (specifiche tecniche e clausole contrattuali) sono **obbligatori** ai sensi dell'art. 57 co. 2 D.Lgs. 36/2023. La mancata applicazione integra un vizio della documentazione di gara; la verifica dell'obbligo da parte della stazione appaltante e' adempimento distinto da questa skill.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Identificazione del regime e dei criteri applicabili**: l'utente chiede "quali CAM si applicano al mio progetto?", "vale ancora il DM 256/2022 per la mia gara?", "che criteri devo dimostrare per una manutenzione straordinaria?" -> leggi [`tasks/identifica-criteri-applicabili.md`](tasks/identifica-criteri-applicabili.md)

- **Redazione guidata bozza Relazione CAM**: l'utente chiede "aiutami a scrivere la relazione CAM", "genera la struttura della relazione secondo il modello MASE", "compila la scheda del criterio 2.3.16", "da dove inizio?" -> leggi [`tasks/draft-relazione-cam.md`](tasks/draft-relazione-cam.md)

- **Verifica relazione CAM esistente**: l'utente allega o incolla una relazione CAM gia' redatta e chiede "e' completa?", "e' conforme al DM 24/11/2025?", "cosa manca?" -> leggi [`tasks/check-relazione-cam.md`](tasks/check-relazione-cam.md)

Se la richiesta non e' chiara, chiedi all'utente:
1. Data (prevista) di pubblicazione del bando o di invio degli inviti e - per lavori e affidamenti congiunti - in vigenza di quale DM e' stato validato il progetto a base di gara, con la data di validazione (per stabilire il regime).
2. Tipologia di intervento (costruzione / ristrutturazione / manutenzione ordinaria o straordinaria / adeguamento / opera di ingegneria civile) e livello di progettazione (PFTE / esecutivo).
3. Sta scrivendo la relazione da zero oppure vuole verificarne una esistente?

## Processo generale

1. **Stabilisci il regime** (DM 24/11/2025 vs transitorio DM 256/2022) con l'estratto [`dm-cam-2025-ambito-transitorio.md`](references/estratti/dm-cam-2025-ambito-transitorio.md). Se la procedura ricade nel transitorio, avverti che questa skill copre il DM 24/11/2025 e che i criteri del vecchio DM restano disponibili negli estratti marcati [STORICO].
2. **Inquadra il progetto**: tipologia di intervento (definizioni ex art. 3 DPR 380/2001, richiamate dall'art. 3 DM 24/11/2025), livello di progettazione, tipo di affidamento (progettazione / lavori / congiunto), criterio di aggiudicazione (i premianti rilevano solo col miglior rapporto qualita'/prezzo).
3. **Identifica la sotto-attivita'** con il routing sopra e carica il task file.
4. **Cita sempre** il numero del criterio del DM 24/11/2025 (es. "criterio 2.3.16", "par. 1.3.5") e la fonte (`references/fonti/` o `references/estratti/`) per ogni affermazione tecnica. Per i requisiti puntuali dei singoli criteri rinvia al testo integrale dell'Allegato 1 (PDF ufficiale MASE): la skill non li riproduce.
5. **Produci l'output** nel formato del modello MASE (sezioni normativa/progetto/allegati, Tabella 1 di applicabilita', Schede Tipo).
6. **Concludi** con:
   - elenco degli **elementi non automaticamente verificabili** dalla skill (sopralluogo, indagini, rapporti di prova, EPD e certificazioni di prodotto, studio LCA);
   - rinvio alla **revisione e firma del progettista**;
   - segnalazione che la Relazione va prodotta **per ogni livello di progettazione** e allegata alla documentazione soggetta a verifica ex art. 42 e allegato I.7 D.Lgs. 36/2023, e che gli inadempimenti in esecuzione sono sanzionabili con penali o risoluzione ex art. 122 del Codice (par. 1.3.5).

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie (scaricate, hashate e trascritte in [`references/fonti/`](references/fonti/)):

- **DM MASE 24 novembre 2025** - articolato (GU n. 281 del 3/12/2025) - [`dm-cam-24-11-2025-articolato.md`](references/fonti/dm-cam-24-11-2025-articolato.md)
- **Allegato 1 al DM 24/11/2025** - testo dei criteri (PDF ufficiale MASE) - [`dm-cam-24-11-2025-allegato-1.md`](references/fonti/dm-cam-24-11-2025-allegato-1.md)
- **Circolare MASE 10 aprile 2026** - chiarimenti su ambito e transitorio - [`circolare-mase-10-04-2026.md`](references/fonti/circolare-mase-10-04-2026.md)
- **Modello MASE di Relazione CAM di progetto** (versione 2/2/2026) - [`modello-relazione-cam-2026.md`](references/fonti/modello-relazione-cam-2026.md)
- **D.Lgs. 36/2023 art. 57** - obbligo CAM (estratto [`dlgs-36-2023-art57.md`](references/estratti/dlgs-36-2023-art57.md))

Estratti curati in [`references/estratti/`](references/estratti/):
- [`dm-cam-2025-ambito-transitorio.md`](references/estratti/dm-cam-2025-ambito-transitorio.md) - entrata in vigore, ambito, regime transitorio
- [`dm-cam-2025-relazione-cam-struttura.md`](references/estratti/dm-cam-2025-relazione-cam-struttura.md) - criterio 2.1.1, modello MASE, struttura e applicabilita' dei criteri
- `dm-256-2022-*.md` - [STORICO] criteri del DM 256/2022, solo per il regime transitorio

## Limiti

Cosa questa skill NON fa:

- Non riproduce il **testo integrale dei singoli criteri** (requisiti prestazionali, tabelle, soglie numeriche): trascrive i paragrafi strutturali e rinvia al PDF ufficiale dell'Allegato 1. Per ogni criterio applicato al caso concreto **il progettista deve leggere il testo integrale del criterio** ("Indicazioni", "Criterio", "Verifica").
- Non redige lo **studio LCA/LCC** (par. 1.3.2) ne' calcola il GWPtotal: indica solo dove inserirli nella relazione.
- Non verifica la **conformita' dei prodotti** (EPD, etichette ambientali, rapporti di prova): la verifica dei mezzi di prova e' del progettista/DL; ricorda il divieto di usare "certificazioni CAM" di prodotto come mezzo di prova (par. 1.3.5).
- Non produce il **capitolato speciale d'appalto** (criterio 2.1.2): segnala solo i contenuti che il capitolato deve riportare.
- Non genera la **Relazione CAM dell'impresa appaltatrice** (criterio 3.1.1) ne' i piani operativi di cantiere dell'impresa.
- Non gestisce la **procedura di gara** ne' calcola punteggi OEPV.
- Non copre i **CAM di altre categorie** (strade DM 5/8/2024, verde pubblico, arredo urbano, ecc.).
- Non aggiorna automaticamente criteri e modulistica a fronte di aggiornamenti MASE successivi: verificare `last_verified`.
