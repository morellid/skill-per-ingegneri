# CHANGELOG - esercizio-controllo-impianti-termici-dpr74

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #255)
- Prima versione della skill di supporto ai criteri di **esercizio, conduzione, controllo e
  manutenzione** degli **impianti termici** per la climatizzazione, ai sensi del **D.P.R. 16
  aprile 2013, n. 74**, nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 16 aprile 2013, n. 74** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 13aa0ad0fb0edbe235455d2b79f2173ec2dc3dff8c28abc5b606e9d4cb8e32f5 (codice 13G00114).
    Artt. 3, 4, 5, 6, 7, 8 via `caricaArticolo`, trascritti verbatim in
    `references/fonti/dpr-74-2013.md`.
- Estratto operativo `references/estratti/impianti-termici-checklist.md`.
- Due task: `verifica-limiti-esercizio.md` e `imposta-controllo-manutenzione.md`.
- Due esempi: riscaldamento in zona climatica E (temperatura e periodi/orari); terzo
  responsabile in unita' residenziale singola vs condominio.

### Contenuto ancorato al testo
- Temperature massime (art. 3: 18C+2 industriale / 20C+2 altri; estiva >= 26C-2); limiti di
  esercizio per zona climatica A-F (art. 4) e ordinanze del sindaco (art. 5); responsabile e
  terzo responsabile con limiti alla delega (art. 6); controllo e manutenzione da ditte abilitate
  DM 37/2008 (art. 7); controllo di efficienza energetica per impianti > 10/12 kW con RCEE (art. 8).

### Scope e limiti
- Non riproduce i **modelli RCEE** (Allegato A, in formato tabellare) ne' il **libretto di
  impianto** (DM 10/2/2014). Non esegue il controllo/manutenzione ne' redige il RCEE. Non copre
  la disciplina regionale di dettaglio (periodicita', catasto impianti, bollino). Complementare a
  `trasmittanza-termica-opache-dm2015` e `diagnosi-energetica-dlgs102`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 74/2013 pinnato (nuovo hash);
  verificare il DM 10/2/2014 e la disciplina regionale.
- Validazione Livello 2 con termotecnico / manutentore abilitato.
