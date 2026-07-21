# CHANGELOG - valutazione-rischio-cancerogeni-mutageni-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #370)
- Prima versione della skill di supporto al **RSPP/ASPP**, al **datore di lavoro** e al **tecnico della
  sicurezza** per l'inquadramento della **valutazione e gestione del rischio da agenti cancerogeni,
  mutageni e da sostanze tossiche per la riproduzione** ai sensi del **D.Lgs. 81/2008, Titolo IX, Capo II
  (artt. 233-243)**, testo vigente aggiornato dal **D.Lgs. 135/2024**, nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e (codice 008G0104, idGruppo 42/43/44).
    Artt. 233 (v2), 234 (v3), 235 (v3), 236 (v3), 237 (v2), 238 (v1), 239 (v2), 242 (v4), 243 (v3) via
    `caricaArticolo` (header X-Requested-With, formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-233-243.md` (testo in vigore dal 11-10-2024).
- Estratto operativo `references/estratti/rischio-cancerogeni-checklist.md`.
- Due task: `inquadra-valutazione-misure-cancerogeni.md` e `inquadra-sorveglianza-registro-esposti.md`.
- Due esempi: officina galvanica con composti del cromo VI (campo di applicazione, gerarchia sostituzione/
  riduzione, valutazione e integrazione del DVR, misure); esposti a polveri di legno duro (sorveglianza
  sanitaria, registro di esposizione e conservazione).

### Contenuto ancorato al testo
- Campo di applicazione, salvo Capo III amianto e radiazioni Euratom (233). Definizioni: cancerogeno/
  mutageno cat. 1A/1B (Reg. CE 1272/2008 CLP) o allegato XLII, sostanza tossica per la riproduzione priva
  di soglia / con valore soglia (allegato XLIII), valore limite, valore limite biologico, sorveglianza
  sanitaria (234). Sostituzione e riduzione con gerarchia sostituzione / sistema chiuso / riduzione al
  piu' basso valore tecnicamente possibile e rispetto del valore limite dell'allegato XLIII (235).
  Valutazione del rischio nel documento dell'art. 17 e integrazione del DVR (artt. 28 c. 2 / 29 c. 5)
  (236). Misure tecniche, organizzative, procedurali - quantitativi minimi, limitazione degli esposti,
  aree con divieto di fumo, aspirazione localizzata (art. 18 c. 1 lett. q), misurazione (allegato XLI),
  smaltimento (237); misure igieniche - servizi igienici, indumenti separati, DPI, divieti (238);
  informazione e formazione prima dell'adibizione e con ripetizione almeno quinquennale, etichettatura CLP
  (239). Accertamenti sanitari e sorveglianza sanitaria, allontanamento art. 42, ruolo del medico
  competente (242). Registro di esposizione tenuto tramite il medico competente con accesso di RSPP e RLS,
  cartelle sanitarie e di rischio (art. 25), invio all'INAIL e conservazione fino a 40 anni (cancerogeni/
  mutageni) e almeno 5 anni (tossici per la riproduzione), comunicazione all'organo di vigilanza (243).

### Scope e limiti
- Non redige il DVR ne' la valutazione del rischio, non esegue misurazioni ne' campionamenti, non applica
  i valori limite di esposizione, non riproduce gli Allegati XLI/XLII/XLIII/XLIII-bis ne' i regolamenti
  CLP/REACH, non tratta l'amianto (Capo III), gli agenti chimici (Capo I) ne' gli agenti biologici
  (Titolo X). Non sostituisce il datore di lavoro, l'RSPP ne' il medico competente.

### Note di sviluppo
- Complementare a `valutazione-rischio-chimico-dlgs81` (Capo I). Distinta dai rischi fisici e dagli agenti
  biologici. Validazione Livello 2 con RSPP/tecnico della sicurezza o medico competente.
