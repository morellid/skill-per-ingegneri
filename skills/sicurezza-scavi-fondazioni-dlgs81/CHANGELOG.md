# CHANGELOG - sicurezza-scavi-fondazioni-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #356)
- Prima versione della skill di supporto al **coordinatore per la sicurezza**, al **direttore dei
  lavori** e all'**impresa** per la **sicurezza degli scavi e delle fondazioni** in cantiere, ai sensi
  del **D.Lgs. 9 aprile 2008, n. 81, Titolo IV, Capo II, Sezione III, artt. 118-121**, nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e (codice 008G0104, idGruppo 21).
    Artt. 118-121 via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-118-121.md` (artt. 118-121 per intero).
- Estratto operativo `references/estratti/sicurezza-scavi-checklist.md` con tabella delle soglie
  numeriche.
- Due task: `inquadra-presidi-scavo.md` e `inquadra-gas-negli-scavi.md`.
- Due esempi: trincea 2,20 m (armature, tavole sporgenti, deposito sul ciglio); pozzo di fondazione 4 m
  (impalcato oltre 3 m, assistenza esterna, rischio gas).

### Contenuto ancorato al testo
- Splateamento e sbancamento: inclinazione/tracciato anti-franamento, divieto di scalzamento alla base
  oltre m 1,50, armatura/consolidamento, divieti su escavatore/ciglio, delimitazione (118); pozzi, scavi
  e cunicoli: armature oltre m 1,50, tavole sporgenti almeno 30 cm, armature di cunicoli e
  sottomurazioni, impalcato nei pozzi oltre 3 m, assistenza esterna e recupero infortunato, Allegato
  XVIII punto 3.4 (119); divieto di deposito sul ciglio salvo puntellature (120); presenza di gas -
  DPI, sistema di salvataggio con sorveglianza esterna, bonifica/ventilazione, divieto fiamme, lavoro in
  coppia (121).

### Scope e limiti
- Non redige il POS/PSC ne' la relazione geotecnica, non dimensiona armature/sbadacchiature, non calcola
  la stabilita' delle pareti, non riproduce l'Allegato XVIII. Non sostituisce il coordinatore, il
  direttore dei lavori, il progettista ne' il preposto.

### Note di sviluppo
- Distinta da `terre-rocce-scavo-dpr120` (gestione terre) e `capacita-portante-fondazione-ntc`
  (geotecnica). Rinvio al DPR 177/2011 per gli ambienti confinati (art. 121).
- Artt. 118-119 modificati dal D.Lgs. 106/2009. Validazione Livello 2 con coordinatore/geotecnico.
