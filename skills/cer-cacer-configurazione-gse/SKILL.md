---
name: cer-cacer-configurazione-gse
description: Supporta la configurazione di una Comunita' di Energia Rinnovabile (CER, art. 31 D.Lgs. 199/2021), di un Gruppo di Autoconsumatori (GAC, art. 30 c. 2) o di un Autoconsumatore Individuale a Distanza (AID, art. 30 c. 1 lett. a) n. 2) ai sensi del DM MASE 7 dicembre 2023 n. 414 come modificato dal DM MASE 16 maggio 2025 n. 127, con verifica del perimetro cabina primaria, redazione guidata dello statuto, simulazione semplificata dell'autoconsumo condiviso e dei flussi economici (TIP, TR, contributo PNRR per Comuni con popolazione < 50.000 abitanti) secondo il TIAD ARERA 727/2022/R/eel, e checklist documentale per la qualifica al portale GSE in conformita' alle Regole Operative CACER. Use when an Italian engineer, energy manager, EGE/ESCo, GSE consultant, ente locale, or amministratore di condominio needs to assess CER/GAC/AID feasibility, prepare the statute of a renewable energy community, simulate shared self-consumption and incentive cash flows, or build the GSE qualification dossier for the CACER service.
license: MIT
---

# Configurazione CER/CACER e Qualifica GSE (DM 7/12/2023 e DM 127/2025 + Regole Operative GSE + TIAD)

## Quando usare questa skill

Usare questa skill quando un **ingegnere**, **energy manager**, **EGE/ESCo**, **consulente GSE**, **ente locale** o **amministratore di condominio** deve:
- decidere se un'iniziativa di autoconsumo da fonti rinnovabili puo' configurarsi come **AID** (art. 30 c. 1 lett. a) n. 2), **GAC** (art. 30 c. 2) o **CER** (art. 31) del **D.Lgs. 199/2021**;
- verificare il **perimetro di cabina primaria** richiesto dal DM 7/12/2023 per accedere alla tariffa incentivante (TIP) sulla sotto-configurazione incentivata, distinguendolo dal perimetro **soggettivo/giuridico** della CER (che puo' coprire piu' cabine primarie con piu' richieste GSE);
- redigere una **bozza di statuto / atto costitutivo** di una CER coerente con il DM 7/12/2023 e con le Regole Operative CACER del GSE;
- effettuare una **simulazione semplificata** dell'energia condivisa, della TIP, della tariffa di restituzione (TR) e del **contributo PNRR a fondo perduto** per Comuni con popolazione inferiore a **50.000 abitanti** (soglia introdotta dal DM MASE 127/2025, in luogo dei < 5.000 abitanti del testo originario);
- predisporre la **checklist documentale** per la richiesta di qualifica al GSE (servizio CACER, accesso TIP, accesso eventuale al contributo PNRR).

**Non usare** questa skill come unico strumento quando l'utente chiede:
- progettazione esecutiva, dimensionamento elettrico/strutturale o calcoli di rete dell'impianto FER;
- dichiarazione fiscale o trattamento tributario di benefici economici (rinvio a commercialista / consulente fiscale);
- pareri legali su forma societaria, antitrust, concorrenza o aiuti di Stato;
- gestione del processo autorizzativo dell'impianto (PAS, AU, comunicazione/Modello Unico): la skill verifica solo che il titolo sia coerente con la richiesta GSE, non lo redige;
- attivita' di trading energetico o stipula contratti PPA che esulino dal modello CACER;
- iniziative di autoconsumo non FER o impianti di potenza superiore alla soglia di legge ammessa al servizio CACER.

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario**, del soggetto chiamato a formalizzare l'atto costitutivo (notaio o intermediario abilitato secondo la forma giuridica scelta), del commercialista per gli aspetti fiscali, ne' del soggetto referente nei rapporti con il GSE. L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito, alla firma o al caricamento sul portale GSE.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Verifica perimetro e scelta della configurazione**: quando l'utente chiede se POD e impianto stanno nella stessa cabina primaria, o se conviene configurarsi come AID, GAC o CER -> leggi [`tasks/valuta-perimetro-configurazione.md`](tasks/valuta-perimetro-configurazione.md)
- **Redazione guidata dello statuto CER**: quando l'utente chiede di impostare statuto / atto costitutivo della CER -> leggi [`tasks/redigi-statuto-cer.md`](tasks/redigi-statuto-cer.md)
- **Simulazione autoconsumo condiviso e flussi economici**: quando l'utente chiede di stimare energia condivisa, TIP, TR e contributo PNRR -> leggi [`tasks/simula-autoconsumo-condiviso.md`](tasks/simula-autoconsumo-condiviso.md)
- **Checklist qualifica GSE (CACER + TIP + PNRR)**: quando l'utente chiede quali documenti servono per la richiesta sul portale GSE -> leggi [`tasks/predisponi-qualifica-gse.md`](tasks/predisponi-qualifica-gse.md)

Se la richiesta e' generica ("aiutami a fare una CER"), parti da `valuta-perimetro-configurazione.md`, poi proponi gli altri task.

## Processo generale

1. Identifica la sotto-attivita' richiesta e la **configurazione di riferimento** (AID/GAC/CER).
2. Carica il task file specifico.
3. Richiedi solo i dati necessari per quel task:
   - localizzazione POD impianti e POD utenze (Comune, indirizzo, codice POD se disponibile);
   - cabina primaria (da mappa GSE) e zona di mercato;
   - potenza installata o prevista degli impianti FER e data di entrata in esercizio;
   - soggetti partecipanti (persone fisiche, PMI, enti locali, terzo settore) e ruolo (produttore, consumatore, prosumer, referente);
   - profili di consumo medi orari/annui se disponibili (altrimenti procedi con stime parametriche dichiarate).
4. Applica la procedura del task con riferimenti puntuali a:
   - **D.Lgs. 199/2021**: art. 30 c. 1 lett. a) n. 2 (AID), art. 30 c. 2 (GAC, con il vincolo "stesso edificio o condominio" alla lett. a)), art. 31 (CER), art. 32 (ARERA, contratti, ruolo del referente);
   - **DM MASE 7 dicembre 2023 n. 414** come modificato dal **DM MASE 16 maggio 2025 n. 127** (regolamentazione CACER, TIP, contributo PNRR per Comuni < 50.000 ab., completamento lavori entro 30/6/2026, esercizio entro 24 mesi dal completamento e comunque non oltre 31/12/2027, erogazione in tre fasi: anticipazione 30% + quota intermedia 40% + saldo);
   - **Regole Operative CACER del GSE** (Allegato 1 - procedure di qualifica e gestione, da consultare nella versione vigente);
   - **TIAD - Delibera ARERA 727/2022/R/eel** (regolazione dei flussi fisici/economici di autoconsumo diffuso).
5. Produci output strutturato che distingua nettamente:
   - dati certi (forniti dall'utente o da fonte ufficiale);
   - stime parametriche (con assunzioni esplicite);
   - voci `DA VERIFICARE CON GSE / NOTAIO / COMMERCIALISTA`.
6. Chiudi sempre ricordando che la qualifica formale e' rilasciata dal GSE secondo le proprie Regole Operative e che lo statuto va formalizzato secondo la forma giuridica scelta (atto pubblico presso notaio per le forme che lo richiedono, scrittura privata autenticata o procedure RUNTS per gli enti del terzo settore, ecc.).

## Fonti normative

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie usate dalla skill:

- **D.Lgs. 8 novembre 2021 n. 199** - art. 30 c. 1 lett. a) n. 2 (AID), art. 30 c. 2 (GAC, con stesso edificio/condominio alla lett. a)), art. 31 (CER), art. 32 (ARERA + contratti).
- **DM MASE 7 dicembre 2023 n. 414** - Regolamentazione delle CACER, TIP, contributo PNRR.
- **DM MASE 16 maggio 2025 n. 127** - Modifiche al DM 414/2023: estensione perimetro PNRR ai Comuni < 50.000 ab.; completamento dei lavori entro 30/6/2026; esercizio entro 24 mesi dal completamento dei lavori e comunque non oltre 31/12/2027; erogazione in tre fasi (anticipazione fino al 30% del contributo, quota intermedia del 40% al 40% delle spese ammissibili sostenute, saldo); applicazione alle persone fisiche dell'esclusione del fattore di riduzione F.
- **Delibera ARERA 727/2022/R/eel - TIAD** - Testo Integrato Autoconsumo Diffuso e successivi aggiornamenti applicabili alle CACER.
- **Regole Operative CACER del GSE** (Allegato 1) - procedure di qualifica, gestione, calcolo energia condivisa.

Estratti operativi in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non produce statuti pronti per la formalizzazione: a seconda della forma giuridica scelta, l'atto costitutivo va perfezionato con atto pubblico presso notaio, scrittura privata autenticata, procedure RUNTS per gli enti del terzo settore, ecc.
- Non simula in modo certificato l'energia condivisa: il calcolo orario ufficiale e' eseguito dal GSE su dati di misura (Allegato A TIAD).
- Non sostituisce la mappa cabine primarie del GSE: la verifica del perimetro va fatta sul portale GSE prima di costituire la CACER.
- Non determina importi puntuali della TIP: la TIP e' una sommatoria di una parte fissa e di un correttivo legato al prezzo zonale, e va sempre validata sulla pubblicazione GSE/MASE vigente.
- Non gestisce gli aspetti fiscali (IVA, Ires, irap, agevolazioni terzo settore) ne' il regime degli aiuti di Stato.
- Non interpreta il contratto di partecipazione condominiale ne' il regolamento di condominio: rinvio all'amministratore.
- Non rilascia dichiarazioni o asseverazioni: queste restano a cura del professionista firmatario.
