---
name: dnsh-pnrr-checker
description: Verifica e struttura la documentazione DNSH (Do No Significant Harm) per interventi PNRR/PNC, con mappatura della misura, scelta delle schede tecniche RGS, checklist ex ante/ex post, piano evidenze e report di conformita'. Use when a RUP, progettista, direttore lavori, supporto al RUP, soggetto attuatore o consulente deve impostare o controllare il rispetto del principio DNSH secondo Reg. UE 2020/852, Reg. UE 2021/241 e Guida operativa RGS aggiornata con circolare n. 22/2024.
license: MIT
---

# DNSH PNRR - verifica schede e checklist

## Quando usare questa skill

Usare quando l'utente deve impostare, verificare o integrare la documentazione DNSH di un intervento finanziato dal PNRR o dal Piano Nazionale Complementare: relazione DNSH, checklist ex ante/ex post, capitolato con vincoli ambientali, evidenze da caricare su ReGiS, fascicolo documentale per SAL/rendicontazione.

La skill e' pensata per RUP, tecnici di supporto al RUP, progettisti, direttori lavori, collaudatori, responsabili di misura, consulenti ambientali e stazioni appaltanti. E' particolarmente utile per lavori pubblici, forniture ICT, impianti, edifici, mobilita', rifiuti, acque, energia e acquisti collegati a misure PNRR.

Non usare questa skill per certificare automaticamente il rispetto DNSH, per sostituire verifiche progettuali specialistiche, per calcolare LCA/EPD/diagnosi energetiche non fornite dall'utente, o per derogare a prescrizioni specifiche della misura PNRR, del bando, del decreto di finanziamento o del sistema ReGiS.

## Avvertenza

Questa skill e' uno strumento di supporto alla **redazione e verifica documentale** DNSH. **Non sostituisce il giudizio del professionista firmatario, del RUP, del soggetto attuatore o dell'amministrazione titolare della misura.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito, alla firma digitale o al caricamento su ReGiS senza revisione professionale.

> **ATTENZIONE - vigenza documentale**: la versione 0.1.0-alpha usa come riferimento operativo la Guida RGS allegata alla circolare n. 22 del 14 maggio 2024, che aggiorna le precedenti circolari RGS n. 32/2021 e n. 33/2022. Prima di applicare la skill su casi reali verificare la pagina ufficiale Italia Domani / RGS, eventuali FAQ, istruzioni di misura, decreti di finanziamento e template ReGiS vigenti alla data di rendicontazione.

## Sotto-attivita' disponibili

Questa skill supporta tre sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Inquadramento misura e schede DNSH**: se l'utente chiede "quali schede DNSH si applicano?", "quale regime DNSH?", "come mappo un intervento PNRR?" -> leggi [`tasks/inquadra-misura-schede.md`](tasks/inquadra-misura-schede.md)
- **Checklist ex ante / ex post**: se l'utente chiede "compila/verifica checklist DNSH", "cosa devo controllare in progettazione o rendicontazione?", "quali risposte SI/NO/NA sono coerenti?" -> leggi [`tasks/verifica-checklist.md`](tasks/verifica-checklist.md)
- **Piano evidenze e report DNSH**: se l'utente chiede "quali documenti devo allegare?", "scrivi una relazione DNSH", "prepara il fascicolo DNSH per gara/SAL/collaudo/ReGiS" -> leggi [`tasks/piano-evidenze-report.md`](tasks/piano-evidenze-report.md)

Se la richiesta non e' chiara, chiedi almeno: misura PNRR/PNC, CUP/intervento, tipologia di opera/fornitura/servizio, fase (progettazione, affidamento, esecuzione, SAL, collaudo, rendicontazione), documenti gia' disponibili.

## Processo generale

1. **Inquadra il progetto**: misura, missione/componente/investimento, soggetto attuatore, CUP, oggetto, importo, localizzazione, fase procedurale, fonte di finanziamento.
2. **Verifica la fonte specifica di misura**: bando/decreto/convenzione/atto d'obbligo, eventuale scheda DNSH gia' assegnata dall'amministrazione titolare, template ReGiS e linee guida settoriali.
3. **Carica il task** pertinente dalla sezione "Sotto-attivita' disponibili".
4. **Applica la mappatura DNSH**: individua schede tecniche, regime 1 o regime 2 dove previsto, vincoli ex ante/ex post e riferimenti a CAM o normativa ambientale richiamata.
5. **Produci un output tracciabile**: ogni requisito deve avere riferimento fonte, esito (`Conforme`, `Non conforme`, `Non applicabile motivato`, `Da integrare`), evidenza richiesta e responsabile della verifica.
6. **Evidenzia le lacune**: dati non forniti, documenti mancanti, verifiche non desumibili automaticamente, prescrizioni di misura non disponibili.
7. **Concludi sempre** con rinvio alla revisione del professionista/RUP/soggetto attuatore e con avvertenza che il caricamento su ReGiS deve seguire il template vigente.

## Fonti normative e operative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Estratti sintetici in [`references/estratti/`](references/estratti/).

Fonti primarie:

- Regolamento (UE) 2020/852, art. 17 - definizione del danno significativo ai sei obiettivi ambientali.
- Regolamento (UE) 2021/241, art. 5 e art. 18 - principio DNSH nel Dispositivo per la ripresa e resilienza.
- Circolare RGS n. 22 del 14 maggio 2024 - aggiornamento della Guida operativa DNSH.
- Guida operativa RGS DNSH, terza edizione 2024 - schede tecniche, checklist, mappature, evidenze e CAM.

Fonti storiche di rinvio:

- Circolare RGS n. 32 del 30 dicembre 2021 - prima Guida operativa DNSH.
- Circolare RGS n. 33 del 13 ottobre 2022 - aggiornamento 2022 della Guida operativa.

## Limiti

Cosa questa skill NON fa:

- Non sostituisce la verifica della **scheda specifica di misura** o delle istruzioni dell'amministrazione titolare.
- Non certifica automaticamente la conformita' DNSH e non firma relazioni, checklist o asseverazioni.
- Non esegue calcoli specialistici non forniti dall'utente: LCA, CAM dettagliati, diagnosi energetiche, analisi rischio climatico, modellazioni acustiche/idrauliche/emissive, verifiche geologiche o strutturali.
- Non verifica direttamente caricamenti o stati ReGiS.
- Non valuta profili fiscali, contabili, di ammissibilita' della spesa o di appalto diversi dal perimetro DNSH.
- Non riproduce integralmente schede/checklist ufficiali se coperte da allegati dinamici: ne usa la struttura operativa e rinvia alla fonte ufficiale vigente.

**Ogni output e' supporto istruttorio e documentale: resta necessaria la revisione del tecnico competente, del RUP e del soggetto attuatore.**
