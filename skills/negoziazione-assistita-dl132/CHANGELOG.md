# CHANGELOG - negoziazione-assistita-dl132

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #307)
- Prima versione della skill di supporto al procedimento di **negoziazione assistita
  da avvocati** (convenzione, condizione di procedibilita', invito, esecutivita'
  dell'accordo), ai sensi del **D.L. 132/2014 (conv. L. 162/2014), artt. 2-5**,
  nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.L. 12/9/2014 n. 132** (conv. L. 162/2014) - indice Normattiva pinnato
    `!vig=2026-07-17`
    SHA256: 9642e055b2868ebfa983741ab9857a3fd84bc29cf65c2705d78cd3d369f0452c
    (codice 14G00147). Artt. 2, 3, 4, 5, idGruppo 2, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dl-132-2014-negoziazione.md`.
- Estratto operativo `references/estratti/negoziazione-assistita-checklist.md`.
- Due task: `verifica-condizione-procedibilita.md` e `inquadra-convenzione-accordo.md`.
- Due esempi: condizione di procedibilita' per pagamento <= 50.000 euro (art. 3);
  requisiti della convenzione ed effetti dell'accordo (artt. 2, 5).

### Contenuto ancorato al testo
- Art. 2 convenzione (buona fede; termine 1-3 mesi prorogabile 30 gg; oggetto su diritti
  disponibili; forma scritta a pena di nullita'; almeno un avvocato per parte;
  certificazione firme; modello CNF); art. 3 condizione di procedibilita' (danni da
  circolazione di veicoli/natanti, pagamenti <= 50.000 euro; esclusioni ingiunzione/ATP/
  esecuzione/camera di consiglio/consumatori; rilievo entro la prima udienza; condizione
  avverata; salvezza urgenti/cautelari); art. 4 invito, avvertimento spese (artt. 96/642
  c.p.c.), certificazioni; art. 5 accordo titolo esecutivo e per ipoteca giudiziale,
  valore, conformita' a norme imperative/ordine pubblico, trascrizione nel precetto,
  autentica del pubblico ufficiale, illecito deontologico impugnare l'accordo.

### Scope e limiti
- Non redige convenzione/invito/accordo, non fornisce consulenza legale, non tratta la
  negoziazione in materia di famiglia (art. 6) ne' la mediazione civile (D.Lgs.
  28/2010), non sostituisce l'avvocato o il giudice. Artt. 6, 9-11 e gli artt. 96, 480,
  642, 696-bis c.p.c. citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.L. 132/2014 pinnato
  (nuovo hash) e rileggere gli artt. 2-5 (testo tra `(( ))`, es. riforma Cartabia
  D.Lgs. 149/2022).
- Validazione Livello 2 con avvocato civilista.
