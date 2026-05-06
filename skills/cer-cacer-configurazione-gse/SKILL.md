---
name: cer-cacer-configurazione-gse
description: Supporta la configurazione di una Comunita' di Energia Rinnovabile (CER), di un Gruppo di Autoconsumatori (GAC) o di un Autoconsumatore Individuale a Distanza (AID) ai sensi del DM MASE 7 dicembre 2023 n. 414 e del D.Lgs. 199/2021 art. 30-32, con verifica del perimetro cabina primaria, redazione guidata dello statuto, simulazione semplificata dell'autoconsumo condiviso e dei flussi economici (TIP, TR, contributo PNRR per Comuni < 5000 abitanti) secondo il TIAD ARERA 727/2022/R/eel, e checklist documentale per la qualifica al portale GSE in conformita' alle Regole Operative CACER. Use when an Italian engineer, energy manager, EGE/ESCo, GSE consultant, ente locale, or amministratore di condominio needs to assess CER/GAC/AID feasibility, prepare the statute of a renewable energy community, simulate shared self-consumption and incentive cash flows, or build the GSE qualification dossier for the CACER service.
license: MIT
---

# Configurazione CER/CACER e Qualifica GSE (DM 7/12/2023 + Regole Operative GSE + TIAD)

## Quando usare questa skill

Usare questa skill quando un **ingegnere**, **energy manager**, **EGE/ESCo**, **consulente GSE**, **ente locale** o **amministratore di condominio** deve:
- decidere se un'iniziativa di autoconsumo da fonti rinnovabili puo' configurarsi come **AID**, **GAC** o **CER** ai sensi del **D.Lgs. 199/2021 art. 30-32**;
- verificare il **perimetro di cabina primaria** richiesto dal DM 7/12/2023 per accedere alla tariffa incentivante (TIP);
- redigere una **bozza di statuto / atto costitutivo** di una CER coerente con il DM 7/12/2023 e con le Regole Operative CACER del GSE;
- effettuare una **simulazione semplificata** dell'energia condivisa, della TIP, della tariffa di restituzione (TR) e del **contributo PNRR a fondo perduto** per Comuni con popolazione inferiore a 5.000 abitanti;
- predisporre la **checklist documentale** per la richiesta di qualifica al GSE (servizio CACER, accesso TIP, accesso eventuale al contributo PNRR).

**Non usare** questa skill come unico strumento quando l'utente chiede:
- progettazione esecutiva, dimensionamento elettrico/strutturale o calcoli di rete dell'impianto FER;
- dichiarazione fiscale o trattamento tributario di benefici economici (rinvio a commercialista / consulente fiscale);
- pareri legali su forma societaria, antitrust, concorrenza o aiuti di Stato;
- gestione del processo autorizzativo dell'impianto (PAS, AU, comunicazione/Modello Unico): la skill verifica solo che il titolo sia coerente con la richiesta GSE, non lo redige;
- attivita' di trading energetico o stipula contratti PPA che esulino dal modello CACER;
- iniziative di autoconsumo non FER o impianti di potenza superiore alla soglia di legge ammessa al servizio CACER.

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario**, del notaio per gli atti costitutivi, del commercialista per gli aspetti fiscali, ne' del soggetto referente nei rapporti con il GSE. L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito, alla firma o al caricamento sul portale GSE.

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
   - **D.Lgs. 199/2021 art. 30, 31, 32** (definizioni AID, GAC, CER);
   - **DM MASE 7 dicembre 2023 n. 414** (regolamentazione CACER, TIP, contributo PNRR);
   - **Regole Operative CACER del GSE** (Allegato 1 - procedure di qualifica e gestione);
   - **TIAD - Delibera ARERA 727/2022/R/eel** (regolazione dei flussi fisici/economici di autoconsumo diffuso).
5. Produci output strutturato che distingua nettamente:
   - dati certi (forniti dall'utente o da fonte ufficiale);
   - stime parametriche (con assunzioni esplicite);
   - voci `DA VERIFICARE CON GSE / NOTAIO / COMMERCIALISTA`.
6. Chiudi sempre ricordando che la qualifica formale e' rilasciata dal GSE secondo le proprie Regole Operative e che lo statuto deve essere finalizzato in atto pubblico.

## Fonti normative

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie usate dalla skill:

- **D.Lgs. 8 novembre 2021 n. 199** - art. 30 (Autoconsumo individuale a distanza), art. 31 (Comunita' di energia rinnovabile), art. 32 (Autoconsumatori che agiscono collettivamente).
- **DM MASE 7 dicembre 2023 n. 414** - Regolamentazione delle CACER e contributo PNRR.
- **Delibera ARERA 727/2022/R/eel - TIAD** - Testo Integrato Autoconsumo Diffuso e successivi aggiornamenti applicabili alle CACER.
- **Regole Operative CACER del GSE** (Allegato 1) - procedure di qualifica, gestione, calcolo energia condivisa.

Estratti operativi in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Non produce statuti pronti per atto pubblico: l'atto costitutivo richiede notaio o intermediario abilitato.
- Non simula in modo certificato l'energia condivisa: il calcolo orario ufficiale e' eseguito dal GSE su dati di misura (Allegato A TIAD).
- Non sostituisce la mappa cabine primarie del GSE: la verifica del perimetro va fatta sul portale GSE prima di costituire la CACER.
- Non determina importi puntuali della TIP: la TIP e' una sommatoria di una parte fissa e di un correttivo legato al prezzo zonale, e va sempre validata sulla pubblicazione GSE/MASE vigente.
- Non gestisce gli aspetti fiscali (IVA, Ires, irap, agevolazioni terzo settore) ne' il regime degli aiuti di Stato.
- Non interpreta il contratto di partecipazione condominiale ne' il regolamento di condominio: rinvio all'amministratore.
- Non rilascia dichiarazioni o asseverazioni: queste restano a cura del professionista firmatario.
