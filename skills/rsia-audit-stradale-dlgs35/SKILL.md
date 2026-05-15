---
name: rsia-audit-stradale-dlgs35
description: Supporta il professionista nelle quattro procedure di gestione della sicurezza delle infrastrutture stradali previste dal D.Lgs 35/2011 (come modificato dal D.Lgs 213/2021 di recepimento della Direttiva UE 2019/1936) - Valutazione di Impatto sulla Sicurezza Stradale (VISS), Controlli di Sicurezza Stradale (RSA), Valutazione di Sicurezza a Livello di Rete (NSA), e ispezioni periodiche/mirate. Use when user asks to draft, audit, or validate any of these procedures on Italian motorways, primary roads, or other roads in the scope of the decree.
license: MIT
---

# Audit RSIA / RSA sicurezza stradale (D.Lgs 35/2011 modificato D.Lgs 213/2021)

## Quando usare questa skill

Questa skill e' appropriata quando l'utente (auditor, ingegnere stradale, controllore della sicurezza stradale ai sensi dell'art. 4, comma 7 del D.Lgs 35/2011, oppure tecnico dell'organo competente o del concessionario autostradale) deve impostare, redigere o validare uno dei quattro processi di gestione della sicurezza stradale del decreto: **Valutazione di Impatto sulla Sicurezza Stradale (VISS)** per progetti di infrastruttura, **Controlli di Sicurezza Stradale (RSA)** sulle fasi progettuali, **Valutazione di Sicurezza a Livello di Rete (NSA)** sulla rete in esercizio, **ispezioni di sicurezza stradale periodiche o mirate** sulle strade aperte al traffico. La skill non e' appropriata per: gallerie stradali (escluse dal decreto e disciplinate dal D.Lgs 264/2006), strade urbane non rientranti nella rete di interesse nazionale, piste ciclabili e strade di accesso a siti industriali/agricoli/forestali esplicitamente escluse dal nuovo art. 1, comma 3 del D.Lgs 35/2011.

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione e verifica degli atti previsti dal D.Lgs 35/2011 (controlli, valutazioni, ispezioni, relazioni). **Non sostituisce il giudizio del professionista firmatario.** Le procedure regolate dal decreto richiedono sempre la firma di soggetti qualificati ai sensi dell'art. 4, comma 7 e dell'art. 9 (titolari di certificato di idoneita' professionale, iscritti nell'elenco nazionale dei controllori della sicurezza stradale, in possesso dei requisiti di indipendenza dell'art. 9, par. 4 lettera c della direttiva 2008/96/CE: il controllore non puo' partecipare ne' alla progettazione ne' al funzionamento del progetto di infrastruttura interessato). L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito, alla firma o alla trasmissione all'ANSFISA o all'organo competente.

## Sotto-attivita' disponibili

Questa skill supporta cinque sotto-attivita'. In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Verifica ambito di applicazione**: quando l'utente chiede se una determinata strada o progetto rientra nel campo di applicazione del decreto, leggere `tasks/check-ambito-applicazione.md`.
- **Redazione VISS (Valutazione Impatto Sicurezza Stradale)**: quando l'utente deve preparare la VISS per un nuovo progetto di infrastruttura o per una modifica sostanziale della rete, leggere `tasks/draft-viss.md`.
- **Redazione RSA (Controllo Sicurezza Stradale) per fase progettuale**: quando l'utente deve preparare o validare un RSA in una delle quattro fasi (PFTE, progettazione esecutiva, ultimazione, prima fase di funzionamento), leggere `tasks/draft-rsa.md`.
- **Redazione NSA (Valutazione Sicurezza a Livello di Rete)**: quando l'utente deve impostare la valutazione quinquennale della rete in esercizio ai sensi del nuovo art. 5 D.Lgs 35/2011 (testo introdotto dal D.Lgs 213/2021), leggere `tasks/draft-nsa.md`.
- **Verifica requisiti del controllore della sicurezza stradale**: quando l'utente deve verificare l'idoneita' di un controllore o di una squadra di controllo (qualifiche, incompatibilita', formazione), leggere `tasks/verifica-requisiti-controllore.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita' desiderata dall'utente.
2. Verifica preliminarmente l'ambito di applicazione (la strada o il progetto e' soggetto al decreto?).
3. Carica il file `tasks/<task-scelto>.md`.
4. Richiedi input necessari come specificato nel task.
5. Applica la procedura descritta, ricavando le componenti e i criteri dagli allegati specifici (Allegato I per VISS, Allegato II per RSA, Allegato II-bis per ispezioni mirate, Allegato III per NSA, Allegato IV per relazioni di incidente).
6. Produci l'output nel formato atteso.
7. Includi sempre nel report finale un rinvio alla verifica del professionista firmatario e, dove richiesto dal decreto, alla trasmissione all'organo competente o all'ANSFISA.

## Fonti normative

- D.Lgs 15 marzo 2011, n. 35 - testo originale di recepimento della Direttiva 2008/96/CE.
- D.Lgs 15 novembre 2021, n. 213 - recepimento della Direttiva (UE) 2019/1936 che modifica il D.Lgs 35/2011 (estensione del campo di applicazione, introduzione della valutazione di sicurezza a livello di rete, ispezioni mirate, protezione degli utenti vulnerabili).
- Direttiva 2008/96/CE - atto-quadro UE su cui si fondano le quattro procedure.

Riferimenti completi in `references/sources.yaml`. Estratti testuali per articolo, comma e allegato in `references/estratti/`.

## Limiti

Cosa questa skill NON fa:

- Non produce documenti auto-firmati. Ogni output e' una bozza tecnica che richiede revisione e firma di un controllore qualificato.
- Non sostituisce verifiche di campo (sopralluoghi, ispezioni visive, misure di velocita' di esercizio).
- Non determina automaticamente la qualifica di un soggetto come controllore della sicurezza stradale: la verifica formale dei requisiti dell'art. 9 D.Lgs 35/2011 e dell'elenco nazionale tenuto dall'art. 4, comma 7 e' del MIMS / ANSFISA.
- Non si applica alle gallerie stradali (D.Lgs 264/2006), alle piste ciclabili, alle strade non aperte al traffico generale.
- Non calcola il costo sociale degli incidenti (art. 7, comma 2 della direttiva): il riferimento e' ai dati ufficiali nazionali aggiornati almeno ogni cinque anni.
- Non fornisce un parere legale sulle responsabilita' civili o penali derivanti dall'omissione delle procedure.
