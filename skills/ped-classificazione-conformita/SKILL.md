---
name: ped-classificazione-conformita
description: Guida la classificazione di un'attrezzatura a pressione secondo il D.Lgs 26/2016 (Direttiva PED 2014/68/UE) e la selezione del modulo di valutazione della conformita'. Use when an Italian mechanical engineer needs to determine PED category, applicable conformity assessment module, and required marking/declaration for pressure equipment.
license: MIT
---

# PED - Classificazione e valutazione della conformita'

## Quando usare questa skill

Quando un ingegnere meccanico o un tecnico della sicurezza deve impostare la classificazione PED di un'attrezzatura a pressione (recipiente, tubazione, accessorio di sicurezza o a pressione, insieme) e la procedura di valutazione della conformita' applicabile, ai sensi del **D.Lgs 26/2016** (recepimento della Direttiva 2014/68/UE). La skill copre attrezzature con PS > 0,5 bar rientranti nell'ambito dell'art. 1 del D.Lgs 93/2000 cosi' come modificato dal D.Lgs 26/2016.

Quando NON usarla: attrezzature escluse dall'ambito (es. apparecchi a pressione semplici - direttiva 2014/29/UE, attrezzature militari, recipienti per il trasporto - ADR/RID, ecc.), attrezzature gia' immesse sul mercato prima del 19 luglio 2016, fase di esercizio/messa in servizio post-marcatura (regolamentata da D.Lgs 81/2008 + DM 329/2004, fuori dallo scopo PED).

## Avvertenza

Questa skill e' uno strumento di supporto alla redazione/verifica di documenti tecnici. **Non sostituisce il giudizio del professionista firmatario.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce documenti pronti al deposito o alla firma, ne' dichiarazioni di conformita' UE valide; il fabbricante (o il suo rappresentante autorizzato) resta unico responsabile della corretta classificazione e della scelta della procedura di valutazione.

La classificazione finale di un'attrezzatura nelle categorie I/II/III/IV dipende da diagrammi grafici PS/V o PS/DN (tabelle 1-9 dell'Allegato II del decreto) che nella Gazzetta Ufficiale sono pubblicati come immagini. La skill guida l'utente al riconoscimento della tabella applicabile e delle eccezioni testuali, ma rinvia la lettura puntuale delle linee di demarcazione al PDF della GU n.53 del 04/03/2016 (`not_in_repo/dlgs-26-2016-gu53.pdf`).

## Sotto-attivita' disponibili

Questa skill supporta cinque sotto-attivita'. In base alla richiesta dell'utente, carica il file appropriato da `tasks/`:

- **Verifica ambito di applicabilita'**: quando l'utente chiede "questa attrezzatura ricade nella PED?", leggere `tasks/check-ambito-applicabilita.md`.
- **Classificazione del fluido (gruppo 1 vs 2)**: quando l'utente chiede di assegnare un fluido al gruppo 1 o 2 ai sensi dell'art. 9 c. 1, leggere `tasks/classifica-fluido.md`.
- **Determinazione della categoria (I, II, III, IV)**: quando l'utente conosce PS, V o DN, tipo di attrezzatura e gruppo del fluido e chiede la categoria, leggere `tasks/determina-categoria.md`.
- **Scelta della procedura di valutazione della conformita'**: quando l'utente, nota la categoria, chiede quale modulo (A, A2, B+D, ecc.) sia ammissibile e con quale ruolo dell'organismo notificato, leggere `tasks/scegli-procedura-conformita.md`.
- **Checklist marcatura CE e dichiarazione UE di conformita'**: quando l'utente vuole verificare apposizione marcatura CE, contenuto della dichiarazione UE, obblighi di conservazione, leggere `tasks/check-marcatura-ce-dichiarazione.md`.

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera e quali input ha gia' a disposizione (PS, V/DN, fluido, stato fisico, condizioni di esercizio).

## Processo generale

1. Identifica la sotto-attivita' richiesta dall'utente.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input minimi specificati nel task.
4. Applica la procedura citando articoli/allegati del D.Lgs 26/2016 (estratti in `references/estratti/dlgs-26-2016-classificazione-moduli.md`).
5. Quando la lettura delle tabelle 1-9 dell'Allegato II e' necessaria, rinvia esplicitamente al PDF della GU (immagini), non inventare valori soglia.
6. Produci l'output nel formato atteso dal task.
7. Concludi sempre con un rinvio al fabbricante o al professionista firmatario per la verifica finale e per la responsabilita' sulla dichiarazione UE.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Fonte unica autoritativa: **D.Lgs 15 febbraio 2016, n. 26** (GU Serie Generale n.53 del 04/03/2016), recepimento della Direttiva 2014/68/UE. Trascrizione fedele dei paragrafi rilevanti in `references/fonti/dlgs-26-2016.md`. Estratto curato di classificazione e moduli in `references/estratti/dlgs-26-2016-classificazione-moduli.md`.

## Limiti

Cosa questa skill NON fa:
- Non produce dichiarazioni UE di conformita' firmate ne' fascicoli tecnici pronti all'apposizione della marcatura CE.
- Non calcola sollecitazioni, spessori, prove idrostatiche o altri elementi della progettazione: si occupa solo della classificazione e dell'inquadramento procedurale.
- Non legge i valori soglia delle tabelle 1-9 dell'Allegato II (diagrammi grafici nel PDF): rinvia al PDF della GU n.53/2016.
- Non valuta la conformita' alle norme armonizzate (presunzione di conformita' ex art. 5 c. 1): segnala l'eventuale impiego di norme armonizzate ma non ne verifica l'applicabilita' al progetto concreto.
- Non si occupa degli obblighi post-marcatura (messa in servizio, verifiche periodiche INAIL, manutenzione): tali aspetti ricadono sotto D.Lgs 81/2008 e DM 329/2004 e sono fuori scope.
- Non valida la designazione dell'organismo notificato: il fabbricante deve scegliere un organismo regolarmente notificato (banca dati NANDO della Commissione europea).
- Non sostituisce il giudizio del fabbricante o del professionista firmatario su classificazione, modulo, e contenuto della dichiarazione UE.
