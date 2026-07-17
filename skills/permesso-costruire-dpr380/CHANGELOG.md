# CHANGELOG - permesso-costruire-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #303)
- Prima versione della skill di supporto al regime del **permesso di costruire**
  (caratteristiche, presupposti, procedimento, efficacia e decadenza), ai sensi del
  **D.P.R. 380/2001, artt. 11, 12, 15, 20**, nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 6/6/2001 n. 380** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: bac3f7b170cfd122936873c835b3f728e7880d058bd98ad45f55b94ba89a632f
    (codice 001G0429). Artt. 11, 12, 15 (idGruppo 3), 20 (idGruppo 5),
    flagTipoArticolo 0, via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-380-2001-permesso.md`.
- Estratto operativo `references/estratti/permesso-costruire-checklist.md`.
- Due task: `inquadra-presupposti-caratteristiche.md` e
  `verifica-procedimento-termini-decadenza.md`.
- Due esempi: presupposti e caratteristiche del titolo (artt. 11-12); termini,
  silenzio-assenso e decadenza (artt. 20, 15).

### Contenuto ancorato al testo
- Art. 11 caratteristiche (legittimazione, trasferibilita', irrevocabilita',
  onerosita' art. 16, diritti dei terzi); art. 12 presupposti (conformita'
  urbanistica, urbanizzazione primaria esistente/prevista/impegno, misure di
  salvaguardia); art. 15 efficacia temporale (inizio 1 anno, ultimazione 3 anni),
  decadenza, proroga, nuovo permesso per la parte non ultimata, decadenza per
  contrastanti previsioni; art. 20 procedimento (SUE, asseverazione, responsabile,
  termini 60/30 gg, interruzione/sospensione, conferenza di servizi, silenzio-assenso
  e vincoli, sanzioni per false attestazioni).

### Scope e limiti
- Non decide il titolo (PdC vs SCIA/CILA - art. 10), non redige domanda/asseverazione,
  non calcola il contributo (art. 16), non tratta agibilita' (art. 24) ne'
  vigilanza/sanzioni (artt. 27 ss.), non sostituisce il progettista, il SUE o il
  Comune. Artt. 10, 13, 16, 22, 24 e la L. 241/1990 citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del DPR 380/2001 pinnato
  (nuovo hash) e rileggere gli artt. 11, 12, 15, 20 (testo tra `(( ))`, es. Salva Casa
  DL 69/2024 conv. L. 105/2024).
- Validazione Livello 2 con tecnico SUE / esperto di diritto urbanistico.
