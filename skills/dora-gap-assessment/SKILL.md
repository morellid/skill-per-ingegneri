---
name: dora-gap-assessment
description: Esegue un gap assessment di un'entita' finanziaria rispetto ai 5 pillar del Regolamento (UE) 2022/2554 (DORA). Use when user asks to verify DORA compliance for a bank, payment institution, electronic money institution, investment firm, insurance undertaking or other financial entity covered by Reg. (UE) 2022/2554, or to map current ICT risk-management practices against artt. 5-30 and art. 45 of DORA.
license: MIT
---

# DORA Gap Assessment - Reg. (UE) 2022/2554

## Quando usare questa skill

Usare questa skill quando un'entita' finanziaria (banca, istituto di pagamento, istituto di moneta elettronica, impresa di investimento, impresa di assicurazione/riassicurazione, gestore di FIA, depositario centrale di titoli, controparte centrale, prestatore di servizi crittoasset MiCA, ecc.) deve mappare le proprie pratiche di gestione del rischio TIC rispetto agli obblighi del Regolamento (UE) 2022/2554 (DORA), direttamente applicabile in Italia dal 17/01/2025 (DORA art. 64 par. 2).

Target utente: **CISO, ICT risk manager, compliance officer, internal auditor di un'entita' finanziaria** o consulente che li supporta nella preparazione/aggiornamento del proprio quadro DORA. Non usare la skill come strumento di certificazione: produce una mappatura strutturata utile come base per il lavoro del professionista, non un parere di conformita' formale.

NON usare la skill per:
- Valutare fornitori terzi critici di servizi TIC dal lato dell'autorita' di sorveglianza (Capo V Sez. II, artt. 31-44, fuori scope di questa skill).
- Adempimenti relativi all'attuazione delle norme tecniche di regolamentazione (RTS) di secondo livello, che variano nel tempo: la skill mappa rispetto al testo del Regolamento "livello 1", non agli RTS.
- Analisi di conformita' a regolamenti settoriali NON-DORA (es. NIS2, GDPR, EBA Guidelines on ICT Risk).

## Avvertenza

Questa skill e' uno strumento di **supporto** al lavoro di gap assessment DORA. **Non sostituisce il giudizio del professionista responsabile** (CISO, compliance officer, auditor, consulente esterno). Le interpretazioni di articoli e considerando del Regolamento, in particolare per i confini di applicazione (art. 2), il principio di proporzionalita' (art. 4), la qualificazione di "funzione essenziale o importante" (art. 3 n. 22), la qualificazione di "grave incidente TIC" (art. 3 n. 10) e di "minaccia significativa" (art. 3 n. 13), sono di esclusiva responsabilita' del professionista. La skill non produce documenti pronti al deposito presso le autorita' competenti ne' attestazioni di conformita'.

## Sotto-attivita' disponibili

Questa skill supporta cinque sotto-attivita' di gap assessment, una per ciascun Pillar DORA. In base alla richiesta dell'utente, caricare il file appropriato da `tasks/`:

- **Pillar 1 - Gestione del rischio TIC** (artt. 5-16): governance, quadro per la gestione del rischio TIC, identificazione, protezione, individuazione, risposta/ripristino, backup, formazione, comunicazione. Quando l'utente chiede gap assessment su governance ICT/quadro di gestione del rischio: leggere `tasks/check-pillar-1-ict-risk-mgmt.md`.
- **Pillar 2 - Gestione, classificazione e segnalazione incidenti** (artt. 17-23): processo di gestione degli incidenti, classificazione, segnalazione (notifica iniziale, intermedia, finale), comunicazione ai clienti. Quando l'utente chiede gap assessment su incident management/reporting: leggere `tasks/check-pillar-2-incidents.md`.
- **Pillar 3 - Test di resilienza operativa digitale** (artt. 24-27): programma di test, test di sistemi/strumenti, TLPT (Threat-Led Penetration Testing). Quando l'utente chiede gap assessment su DORA testing/TLPT: leggere `tasks/check-pillar-3-testing.md`.
- **Pillar 4 - Rischio fornitori terzi TIC** (artt. 28-30): strategia per i rischi da terzi, registro delle informazioni, valutazione preliminare, clausole contrattuali minime, strategie di uscita. Quando l'utente chiede gap assessment su third-party risk management/contratti TIC: leggere `tasks/check-pillar-4-third-party.md`.
- **Pillar 5 - Condivisione informazioni** (art. 45): meccanismi di condivisione informazioni e analisi delle minacce, notifica alle autorita'. Quando l'utente chiede gap assessment su information sharing: leggere `tasks/check-pillar-5-info-sharing.md`.

Se la richiesta e' generica ("fammi un gap assessment DORA"), proporre l'utente di selezionare un pillar alla volta o di eseguirli tutti in sequenza. Avvertire che ciascun pillar genera un report distinto.

## Processo generale

1. Identifica con l'utente quale entita' finanziaria si sta valutando, la sua categoria (art. 2 par. 1 lettere a-u), e l'eventuale qualifica di microimpresa/quadro semplificato (art. 16 par. 1).
2. Identifica il pillar (o i pillar) oggetto del gap assessment.
3. Carica il file `tasks/check-pillar-N-*.md` corrispondente.
4. Richiedi all'utente input documentale e descrittivo come specificato nel task.
5. Per ciascun obbligo DORA elencato nel task, classifica lo stato come: **CONFORME** (evidenza presente e adeguata) / **PARZIALE** (presente ma con lacune o mancanza di evidenze documentate) / **NON CONFORME** (assente) / **NON APPLICABILE** (con motivazione esplicita basata su art. 16, art. 4 par. 2, art. 2 par. 3).
6. Produci il report nel formato indicato dal task.
7. Includi sempre nel report finale: (a) avvertenza che il giudizio finale spetta al professionista responsabile; (b) elenco esplicito delle valutazioni "PARZIALE" e "NON APPLICABILE" che richiedono verifica/decisione del professionista; (c) rinvio al testo committato in `references/fonti/reg-ue-2022-2554-dora.md` per il riscontro testuale di ogni articolo citato.

## Fonti normative

- Regolamento (UE) 2022/2554 (DORA), versione PE-CONS 41/22 - testo trilogue-finale identico in contenuto a quello pubblicato in GU UE L 333 del 27/12/2022. Fonte registrata in `references/sources.yaml` con SHA256 del binario PDF originale. Trascrizione fedele degli artt. 1-30, 45 e 64 in `references/fonti/reg-ue-2022-2554-dora.md`. Estratti curati per pillar in `references/estratti/reg-ue-2022-2554-dora.md`.

Per l'applicazione completa, l'entita' finanziaria deve consultare anche le RTS/ITS adottate dalla Commissione su delega delle AEV (vedi rinvii negli artt. 15, 16, 18, 20, 26, 28, 30 di DORA). Questa skill **non** copre il livello RTS/ITS.

## Limiti

Cosa questa skill NON fa:
- Non produce documenti di policy interna pronti per la firma del CISO o dell'organo di gestione.
- Non sostituisce il giudizio del professionista responsabile sui confini interpretativi dell'applicabilita' (art. 4 proporzionalita', art. 16 quadro semplificato, qualificazione di "funzione essenziale o importante", soglie di "incidente grave").
- Non copre il Capo V Sez. II (artt. 31-44, sorveglianza dei fornitori critici lato autorita') ne' il Capo VII (autorita' competenti, artt. 46-56) ne' le disposizioni sanzionatorie/finali (Capo VIII salvo art. 64).
- Non produce mappature verso framework esterni (NIS2, ISO/IEC 27001, NIST CSF, EBA ICT Guidelines): quelle richiedono lavoro manuale di crosswalk, fuori scope.
- Non valuta gli RTS/ITS DORA di secondo livello (le RTS/ITS sono in costante evoluzione e devono essere consultate separatamente).
- Non genera attestazioni di conformita' verso autorita' competenti.
