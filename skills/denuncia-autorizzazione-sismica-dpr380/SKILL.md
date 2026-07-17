---
name: denuncia-autorizzazione-sismica-dpr380
description: "Supporto documentale agli adempimenti per le costruzioni in zone sismiche secondo il DPR 380/2001 (Testo unico edilizia), Parte II, Capo IV. Aiuta a inquadrare la denuncia dei lavori e la presentazione del progetto (art. 93: preavviso scritto allo sportello unico che ne trasmette copia al competente ufficio tecnico della regione, deposito del progetto in doppio esemplare firmato da tecnico abilitato e dal direttore dei lavori, contenuto minimo e dichiarazione del progettista che asseveri il rispetto delle norme tecniche e la coerenza tra progetto strutturale e architettonico, validita' del preavviso anche come denuncia ex art. 65, registro comunale delle denunce), l'autorizzazione per l'inizio dei lavori (art. 94: nelle localita' sismiche, ad eccezione di quelle a bassa sismicita', non si possono iniziare lavori senza preventiva autorizzazione del competente ufficio tecnico della regione, rilascio entro trenta giorni, silenzio assenso, ricorso al presidente della giunta regionale, direzione lavori da tecnico abilitato) e la disciplina degli interventi strutturali (art. 94-bis: classificazione in interventi rilevanti, di minore rilevanza e privi di rilevanza per la pubblica incolumita' in funzione della zona sismica 1/2/3/4, con autorizzazione preventiva per i soli interventi rilevanti e deroga per gli altri, salvo controlli a campione regionali). Use when a technician must frame the seismic works notice, the prior authorization and the classification of structural interventions in seismic zones under the Italian Testo unico edilizia; it is a documentary aid, does not draft the notice or the structural design, does not perform calculations and does not replace the regional technical office or the SUE."
license: MIT
area: strutture-geotecnica
title: "Denuncia lavori e autorizzazione sismica (DPR 380/2001 artt. 93, 94, 94-bis)"
summary: "Inquadra gli adempimenti per le costruzioni in zone sismiche (DPR 380/2001): denuncia lavori e deposito del progetto asseverato (art. 93), autorizzazione preventiva dell'ufficio regionale (art. 94), classificazione degli interventi per rilevanza e zona sismica (art. 94-bis)."
normative_refs:
  - "D.P.R. 6/6/2001 n. 380 - artt. 93 (denuncia lavori e deposito progetto) e 94 (autorizzazione per l'inizio dei lavori)"
  - "D.P.R. 6/6/2001 n. 380 - art. 94-bis (disciplina degli interventi strutturali in zone sismiche)"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-380-2001
  - zone-sismiche
  - denuncia-lavori
  - autorizzazione-sismica
  - interventi-strutturali
  - strutture
---

# Denuncia lavori e autorizzazione sismica (DPR 380/2001 artt. 93, 94, 94-bis)

## Quando usare questa skill

Usala quando devi **inquadrare gli adempimenti** per le **costruzioni in zone sismiche** e
ancorarli al **DPR 380/2001, Parte II, Capo IV**:

- **denuncia dei lavori e deposito del progetto** - **art. 93**: nelle **zone sismiche**
  (art. 83), chi intende procedere a costruzioni/riparazioni/sopraelevazioni da' **preavviso
  scritto** allo **sportello unico**, che ne trasmette copia al **competente ufficio tecnico
  della regione**; **deposito del progetto** (doppio esemplare, firmato da tecnico abilitato
  e dal DL); **contenuto minimo** e **asseverazione** del progettista (rispetto delle NTC,
  coerenza strutture/architettonico, prescrizioni sismiche urbanistiche); il preavviso vale
  anche come **denuncia ex art. 65**; **registro comunale** delle denunce;
- **autorizzazione per l'inizio dei lavori** - **art. 94**: nelle **localita' sismiche**
  (escluse quelle a **bassa sismicita'** indicate nei decreti ex art. 83) non si possono
  **iniziare i lavori senza preventiva autorizzazione** del competente ufficio tecnico
  regionale; **rilascio entro 30 giorni**; **silenzio assenso** (c. 2-bis) con attestazione
  SUE; **ricorso** al presidente della giunta regionale; **direzione lavori** da tecnico
  abilitato;
- **disciplina degli interventi strutturali** - **art. 94-bis**: classifica gli interventi
  in **"rilevanti"** (a), **"di minore rilevanza"** (b) e **"privi di rilevanza"** (c) per la
  pubblica incolumita', in funzione della **zona sismica** (1/2/3/4) e del tipo di
  intervento; per gli interventi **rilevanti** serve l'**autorizzazione** ex art. 94; per gli
  altri **non** si applica l'autorizzazione preventiva (deroga), salvo **controlli a
  campione** regionali; restano ferme le procedure degli **artt. 65 e 67 c. 1**.

**Non e' una skill di calcolo/redazione**: non redige la denuncia/istanza ne' il progetto
strutturale, non esegue calcoli e non sostituisce l'ufficio tecnico regionale/SUE.

## Cosa NON fa (limiti)

- Non **redige** la denuncia/istanza, l'asseverazione ne' il **progetto strutturale**.
- Non **esegue calcoli** strutturali/sismici (NTC, DM 17/1/2018): rinvio alle skill NTC.
- Non riproduce le **linee guida MIT** (DM 30/4/2018) ne' le **elencazioni/procedure
  regionali** di dettaglio: rinvio.
- Non tratta la **denuncia delle opere in c.a./acciaio** (art. 65): skill
  `denuncia-opere-strutturali-l1086`.
- Non individua la **classificazione sismica** del sito (zona 1-4, art. 83): dato di fatto da
  verificare presso la regione/comune.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-denuncia-autorizzazione`](tasks/inquadra-denuncia-autorizzazione.md) | Imposta il preavviso/denuncia e il deposito del progetto (art. 93) e verifica se serve l'autorizzazione preventiva (art. 94) |
| [`classifica-intervento-sismico`](tasks/classifica-intervento-sismico.md) | Classifica l'intervento come rilevante, di minore rilevanza o privo di rilevanza (art. 94-bis) e ne deduce il regime (autorizzazione vs deposito) |

## Riferimenti normativi

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - Parte II, Capo IV - artt. **93**
  (denuncia lavori e deposito progetto), **94** (autorizzazione per l'inizio dei lavori),
  **94-bis** (disciplina degli interventi strutturali); richiamati gli artt. **52**, **65**,
  **67**, **83** (classificazione sismica), il **DM 17/1/2018** (NTC) e le **linee guida MIT
  (DM 30/4/2018)** e le disposizioni regionali (rinvio).

Dettaglio in `references/sources.yaml`,
`references/fonti/dpr-380-2001-93-94-94bis.md`,
`references/estratti/sismica-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione dell'intervento, la redazione della
denuncia/istanza e del progetto strutturale, i calcoli e il rilascio dell'autorizzazione
restano in capo al **progettista/direttore dei lavori**, all'**ufficio tecnico regionale** e
al **SUE**. **Non sostituisce** questi soggetti ne' la lettura degli artt. 93, 94, 94-bis
del DPR 380/2001, delle NTC e delle disposizioni regionali.
