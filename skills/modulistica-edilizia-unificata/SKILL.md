---
name: modulistica-edilizia-unificata
description: Indica il modulo edilizio unificato corretto (Edilizia libera, CILA, SCIA, SCIA alternativa al PdC, Permesso di Costruire) per un intervento, restituisce l'elenco strutturato degli allegati richiesti e applica le modifiche introdotte dal "Salva Casa" (DL 69/2024 conv. L. 105/2024), dal "Piano Casa" (DL 66/2026, in vigore 8/05/2026) e dal DPR 73/2026 (modifiche DPR 31/2017, in vigore 27/05/2026). Use when an architect, engineer, geometra, or operatore SUE/SUAP needs to determine the correct procedural regime under DPR 380/2001 and D.Lgs. 222/2016 Tabella A for a specific Italian building intervention, identify the attachments required for the unified national module (versione 27/3/2025 Conferenza Unificata), or check whether the Salva Casa or Piano Casa changes apply. Target users are ingegneri edili, architetti, geometri italiani, e tecnici degli sportelli SUE/SUAP.
license: MIT
---

# Modulistica edilizia unificata + Salva Casa

## Quando usare questa skill

Usare quando un ingegnere edile, architetto, geometra o operatore SUE/SUAP chiede di:

- Sapere **quale modulo edilizio** unificato presentare per un determinato intervento (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / Permesso di Costruire) ai sensi del DPR 380/2001 e della Tabella A del D.Lgs. 222/2016
- Conoscere l'**elenco degli allegati** da accompagnare al modulo (relazioni, asseverazioni, autorizzazioni paesaggistiche/MiC, sicurezza cantiere, antincendio, etc.) come da modulistica nazionale unificata aggiornata al **27/3/2025** (Conferenza Unificata - Salva Casa)
- Verificare se al caso si applichino le **modifiche del Salva Casa** (DL 69/2024 conv. L. 105/2024): nuove tolleranze costruttive (art. 34-bis), sanatoria semplificata art. 36-bis, cambio destinazione d'uso art. 23-ter, stato legittimo art. 9-bis, edilizia libera ampliata
- Distinguere fra **sanatoria art. 36** (doppia conformita' piena) e **sanatoria art. 36-bis** (doppia conformita' alleggerita)
- Inquadrare un intervento al limite tra due regimi (CILA vs SCIA, SCIA vs PdC, SCIA alternativa vs PdC)

**Non usare** se l'utente chiede:
- Redazione del **contenuto tecnico** di un singolo elaborato (relazione paesaggistica, relazione strutturale, computo metrico): la skill liste gli allegati richiesti, non li redige
- Verifica di **conformita' urbanistica al PRG/PUC comunale**: la skill rinvia al regolamento locale ma non lo legge
- Calcolo del **contributo di costruzione** o degli **oneri di urbanizzazione**: la skill segnala l'allegato ma non calcola l'importo
- Pareri di **legittimita'** di un intervento gia' eseguito senza titolo: la skill propone il regime di sanatoria applicabile (art. 36 vs 36-bis), ma non sostituisce l'istruttoria del Comune
- Compilazione campo per campo del modulo: la skill fornisce la **mappa** dei quadri e degli allegati, non riempie il PDF
- Verifica di **vincoli paesaggistici / culturali / idrogeologici / sismici** specifici: la skill segnala l'eventuale obbligo di pre-autorizzazione ma non sostituisce l'istruttoria di Soprintendenza, ASL, ufficio sismica

## Avvertenza

Questa skill e' uno strumento di **supporto alla scelta del modulo edilizio** e all'identificazione degli allegati richiesti. **Non sostituisce il giudizio del tecnico abilitato firmatario, ne' del responsabile del procedimento dello sportello SUE/SUAP.** L'utilizzo improprio degli output e' responsabilita' esclusiva dell'utente. La skill non produce moduli pronti al deposito o alla firma, ne' sostituisce il regolamento edilizio comunale, gli strumenti urbanistici locali, o eventuali pareri di Conferenza dei Servizi. Per casi al limite, **interpellare sempre lo sportello SUE comunale** prima del deposito.

## Sotto-attivita' disponibili

Questa skill supporta tre sotto-attivita'. In base alla richiesta dell'utente, carica il task file appropriato:

- **Determina regime edilizio e modulo**: l'utente chiede "che modulo devo presentare?", "quale procedura?", "CILA o SCIA?", "serve PdC?" -> leggi [`tasks/determina-regime-edilizio.md`](tasks/determina-regime-edilizio.md)
- **Genera elenco allegati per modulo**: l'utente conosce gia' il modulo (CILA/SCIA/PdC/SCIA alternativa/sanatoria) e chiede "quali allegati?", "cosa devo allegare?", "checklist documenti" -> leggi [`tasks/genera-elenco-allegati.md`](tasks/genera-elenco-allegati.md)
- **Verifica applicabilita' Salva Casa**: l'utente chiede "il Salva Casa si applica?", "rientra in sanatoria semplificata?", "sono in tolleranza art. 34-bis?", "cambio uso post Salva Casa?" -> leggi [`tasks/verifica-salva-casa.md`](tasks/verifica-salva-casa.md)

Se la richiesta non e' chiara, chiedi all'utente quale delle tre sotto-attivita' vuole eseguire e raccogli le **variabili di inquadramento** (tipologia intervento, immobile esistente o nuovo, vincoli, zona urbanistica) prima di procedere.

## Processo generale

1. **Inquadra l'intervento**: chiedi all'utente le variabili minime - tipologia opera, immobile esistente/nuovo, parti strutturali coinvolte, cambio destinazione d'uso, vincoli sovraordinati (paesaggio, beni culturali, idrogeologico, sismico), zona urbanistica.
2. **Identifica la sotto-attivita'**: usa il routing della sezione "Sotto-attivita' disponibili".
3. **Carica il task file** corrispondente.
4. **Applica la procedura** descritta nel task.
5. **Produci l'output** strutturato con citazione precisa di articolo del DPR 380/2001 e voce della Tabella A D.Lgs. 222/2016 per ogni decisione.
6. **Concludi** sempre con:
   - elenco di **elementi non automaticamente verificabili** dalla skill (regolamento edilizio comunale, strumenti urbanistici locali, varianti regionali del Salva Casa)
   - rinvio allo **sportello SUE/SUAP** del Comune competente per i casi borderline
   - rinvio al **tecnico abilitato firmatario** per l'asseverazione

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DPR 6 giugno 2001 n. 380 - Testo Unico Edilizia (versione consolidata vigente)
- D.Lgs. 25 novembre 2016 n. 222 - SCIA 2 - Allegato Tabella A sezione II Edilizia
- DL 29 maggio 2024 n. 69 conv. L. 24 luglio 2024 n. 105 - Salva Casa
- Conferenza Unificata - Modulistica edilizia unificata, aggiornamento Salva Casa **27/3/2025** (Funzione Pubblica)
- **DL 7 maggio 2026 n. 66 - Piano Casa** (GU n. 104 del 07/05/2026, in vigore 08/05/2026) - SCIA per demolizione/ricostruzione ERP
- **DPR 20 febbraio 2026 n. 73** (GU n. 108 del 12/05/2026, in vigore 27/05/2026) - modifica All. A e B del DPR 31/2017

Estratti testuali in [`references/estratti/`](references/estratti/):
- [`dpr-380-2001-regimi-edilizi.md`](references/estratti/dpr-380-2001-regimi-edilizi.md) - artt. 3, 6, 6-bis, 9-bis, 10, 22, 23, 23-ter, 34-bis, 36, 36-bis
- [`dlgs-222-2016-tabella-a.md`](references/estratti/dlgs-222-2016-tabella-a.md) - struttura Tabella A sezione II Edilizia
- [`dl-69-2024-salva-casa.md`](references/estratti/dl-69-2024-salva-casa.md) - sintesi delle modifiche Salva Casa
- [`modulistica-unificata-2025.md`](references/estratti/modulistica-unificata-2025.md) - struttura dei moduli unificati e allegati ricorrenti
- [`dl-66-2026-piano-casa.md`](references/estratti/dl-66-2026-piano-casa.md) - SCIA per demolizione/ricostruzione ERP (art. 8 co. 1 DL 66/2026)
- [`dpr-73-2026-paesaggio.md`](references/estratti/dpr-73-2026-paesaggio.md) - modifiche All. A voce A.27 e All. B voce B.26 del DPR 31/2017

## Limiti

Questa skill NON fa:
- Non legge il **regolamento edilizio comunale**, gli strumenti urbanistici (PRG/PUC), il piano attuativo: i dettagli locali possono integrare/ridurre il regime nazionale (es. soglia pertinenze, definizione di sagoma, oneri di urbanizzazione locali)
- Non integra automaticamente le **leggi regionali** (es. recupero sottotetti, distanze, vincoli idraulici, paesaggio): la skill cita il regime nazionale e segnala il rinvio alla LR
- Non valuta **l'adeguatezza tecnica** del progetto (idoneita' delle scelte progettuali, accuratezza dei calcoli, conformita' a NTC 2018, antincendio, accessibilita', acustica)
- Non sostituisce la **istruttoria del SUE/SUAP** ne' la valutazione di **Conferenza dei Servizi**
- Non emette **pareri preventivi** della Soprintendenza, ASL, VVF, Ufficio Sismica
- Non calcola il **contributo di costruzione**, gli **oneri di urbanizzazione**, le **sanzioni pecuniarie** di sanatoria
- Non gestisce le **specificita' di varianti in corso d'opera** complesse (es. variante essenziale che reinquadra l'intervento in regime diverso): segnala il principio ma rinvia al SUE
- Non sostituisce la **firma del tecnico abilitato** sulla relazione di asseverazione

**Ogni indicazione prodotta dalla skill e' supporto al tecnico abilitato e all'utente, non sostituzione.**
