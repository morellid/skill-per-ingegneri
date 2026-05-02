---
name: relazione-cam-dm256-2022
description: Supporta la redazione e la verifica della Relazione Tecnica dei Requisiti Ambientali CAM ai sensi del DM 23/06/2022 n. 256 (Criteri Ambientali Minimi per l'affidamento di servizi di progettazione di interventi edilizi e per lavori di nuova costruzione, ristrutturazione e manutenzione di edifici pubblici). Identifica i criteri CAM applicabili alla tipologia di intervento (NC/R1/R2/MS), genera la struttura della relazione capitolo per capitolo e guida il progettista a fornire i dati tecnici per ciascun criterio, oppure verifica una relazione esistente. Use when an architect, civil engineer or technical consultant must draft or review the CAM environmental requirements report for a public works tender under Italian DM 256/2022.
license: MIT
---

# Relazione CAM DM 256/2022 - redazione e verifica

## Quando usare questa skill

Usare quando un **progettista (architetto, ingegnere civile, consulente tecnico)** incaricato di una commessa pubblica deve:

- **Identificare i criteri CAM applicabili** alla propria tipologia di intervento (nuova costruzione, ristrutturazione I/II livello, manutenzione straordinaria) ai sensi del DM 23/06/2022 n. 256.
- **Redigere la bozza della Relazione Tecnica dei Requisiti Ambientali**: struttura capitolare, per ciascun criterio, e dialogo guidato per raccogliere i dati tecnici necessari alla dimostrazione della conformita'.
- **Verificare una Relazione CAM esistente** per completezza e conformita' al DM 256/2022: segnala criteri mancanti, documentazione insufficiente, affermazioni vaghe non supportate da dati.

**Quando NON usare questa skill:**

- Progettazione per soggetti privati senza obbligo CAM (il DM 256/2022 riguarda appalti pubblici ex D.Lgs. 36/2023 art. 57).
- Verifiche ambientali diverse dai CAM edilizia (es. CAM arredi, CAM illuminazione pubblica, CAM pulizie): ogni categoria merceologica ha un proprio DM.
- Calcolo energetico ai sensi del D.Lgs. 192/2005 o APE (il criterio 2.5 rinvia ai requisiti energetici vigenti, ma la relazione APE/EPG e' un documento separato).
- Verifica conformita' urbanistica o edilizia (permessi, conformita' al PRG/PUC): adempimento distinto.
- Valutazione OEPV (calcolo punteggi offerta tecnica): la skill identifica i criteri premianti applicabili, ma la griglia di valutazione e' competenza della commissione di gara.

## Avvertenza

Questa skill e' uno strumento di supporto alla **redazione e verifica della Relazione Tecnica dei Requisiti Ambientali CAM**. **Non sostituisce il giudizio del progettista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti alla firma o al deposito nella piattaforma di gara.

> **ATTENZIONE - vigenza normativa**: la skill e' costruita sul DM 23/06/2022 n. 256 (GU n. 183 del 06/08/2022), in vigore dall'08/10/2022. Il DM puo' essere oggetto di aggiornamenti ministeriali. Verificare `last_verified` in `references/sources.yaml` prima di applicare la skill su un caso reale. In caso di disallineamento con il DM vigente al momento dell'offerta, **prevale il testo del DM vigente** alla data di pubblicazione del bando.

I CAM edilizia sono **obbligatori** per tutte le stazioni appaltanti per gli affidamenti di cui all'art. 57 co. 2 D.Lgs. 36/2023. La mancata applicazione integra un vizio del bando, ma la verifica dell'obbligo da parte della stazione appaltante e' adempimento distinto da questa skill.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Identificazione criteri applicabili**: l'utente chiede "quali CAM si applicano al mio progetto?", "che criteri devo dimostrare per una ristrutturazione R1?", "ho un intervento di MS, quali criteri CAM devo rispettare?" -> leggi [`tasks/identifica-criteri-applicabili.md`](tasks/identifica-criteri-applicabili.md)

- **Redazione guidata bozza Relazione CAM**: l'utente chiede "aiutami a scrivere la relazione CAM", "genera la struttura della relazione", "devo compilare la relazione tecnica dei requisiti ambientali per la gara, da dove inizio?", "guidami criterio per criterio" -> leggi [`tasks/draft-relazione-cam.md`](tasks/draft-relazione-cam.md)

- **Verifica relazione CAM esistente**: l'utente allega o incolla una relazione CAM gia' redatta e chiede "e' completa?", "ho rispettato tutti i criteri?", "cosa manca?", "e' conforme al DM 256/2022?" -> leggi [`tasks/check-relazione-cam.md`](tasks/check-relazione-cam.md)

Se la richiesta non e' chiara, chiedi all'utente:
1. Tipologia di intervento (NC / R1 / R2 / MS)?
2. Sta scrivendo la relazione da zero oppure vuole verificarne una esistente?

## Processo generale

1. **Inquadra il progetto**: tipologia di intervento (NC/R1/R2/MS), destinazione d'uso, localizzazione, importo lavori, tipologia stazione appaltante.
2. **Identifica la sotto-attivita'**: usa il routing sopra.
3. **Carica il task file** corrispondente e seguine la procedura.
4. **Cita sempre** il numero del criterio del DM 256/2022 (es. "Criterio 2.3.1", "Criterio 2.8") e la fonte dell'estratto (`references/estratti/`) per ogni affermazione tecnica.
5. **Produci l'output** nel formato indicato dal task.
6. **Concludi** con:
   - elenco degli **elementi non automaticamente verificabili** dalla skill (sopralluogo, DCF dei materiali, certificazioni di prodotto);
   - rinvio alla **revisione e firma del progettista**;
   - segnalazione che la relazione deve essere allegata agli atti di gara ex art. 57 D.Lgs. 36/2023.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Estratti in [`references/estratti/`](references/estratti/).

- **DM 23/06/2022 n. 256** - Criteri Ambientali Minimi per affidamento servizi di progettazione e lavori di edilizia pubblica (GU n. 183 del 06/08/2022)
- **Allegato DM 256/2022** - testo integrale dei criteri CAM (base + premianti)
- **D.Lgs. 31/03/2023 n. 36 art. 57** - obbligo di applicazione dei CAM negli appalti pubblici (Codice dei Contratti Pubblici 2023)

## Limiti

Cosa questa skill NON fa:

- Non elabora i **calcoli energetici** ai sensi del D.Lgs. 192/2005 o del DM 26/06/2015 (requisiti minimi): rinvia alle metodologie standard per l'APE/EPG, che sono documenti separati dalla Relazione CAM.
- Non verifica la **conformita' dei prodotti** ai requisiti tecnici specifici (es. contenuto di riciclato, marchi di ecolabel): la verifica delle dichiarazioni di prodotto (EPD, DAP) e' responsabilita' del progettista tramite richiesta ai fornitori.
- Non produce **specifiche tecniche di progetto** o **capitolati**: la relazione CAM dimostra conformita', ma le specifiche tecniche di progetto (es. classe di calcestruzzo, U-value degli infissi) sono elaborate nel progetto strutturale/architettonico.
- Non gestisce la **procedura di gara** (bando, disciplinare, piattaforma telematica): adempimento della stazione appaltante.
- Non valuta il punteggio OEPV complessivo: identifica i criteri premianti ma non costruisce la griglia di valutazione.
- Non aggiorna automaticamente i requisiti tecnici CAM a fronte di modifiche ministeriali successive: verificare `last_verified`.
- Non copre i **CAM per altre categorie merceologiche** (arredi, illuminazione, pulizie, ristorazione, etc.): ogni categoria ha il proprio DM.
