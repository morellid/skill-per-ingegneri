# CHANGELOG - barriere-architettoniche-edifici-privati-dm236

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #253)
- Prima versione della skill di supporto al **superamento delle barriere architettoniche** negli
  **edifici privati** e di **edilizia residenziale pubblica** (obbligo, livelli di accessibilita'/
  visitabilita'/adattabilita', criteri di progettazione), ai sensi della **L. 13/1989** e del
  **D.M. 236/1989**, nell'area `edilizia-urbanistica-catasto`.
- Fonti scaricate, hashate e lette (Regola zero):
  - **L. 9 gennaio 1989, n. 13** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: b95aa2b54dbc897c74238ce940d138861bc382a505cc1a6e6ab20bf6e72e4ff6 (codice 089G0031).
    Artt. 1 e 7 via `caricaArticolo`.
  - **D.M. LL.PP. 14 giugno 1989, n. 236** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: f72a56a40612c1da1a6b5d2056e9a4219ce97aa26622b30bb2f63b44e4a9cef8 (codice 089G0298).
    Artt. 2, 3, 4, 8.0 via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/l13-dm236-1989.md`.
- Estratto operativo `references/estratti/barriere-architettoniche-checklist.md`.
- Due task: `individua-livello-accessibilita.md` e `imposta-criteri-progettazione.md`.
- Due esempi: palazzina residenziale di 3 piani (livelli + deroga ascensore); ristorante
  (visitabilita').

### Contenuto ancorato al testo
- Obbligo di progettazione conforme (art. 1 L. 13/1989); definizioni e tre livelli (artt. 2-3 DM
  236/1989) con applicazione per categoria di edificio; deroga ascensore per edifici <= 3 livelli
  fuori terra; criteri di progettazione (art. 4); modalita' di misura (art. 8.0); regime
  abilitativo delle opere di adattamento (art. 7 L. 13/1989).

### Scope e limiti
- Non riproduce i **valori dimensionali** del DM 236/1989 (art. 8, in **formato grafico**:
  pendenza rampe, luce porte, cabina ascensore, spazi di manovra, altezze) - da leggere sull'atto.
  Non redige l'asseverazione di conformita'. Non copre gli edifici/spazi pubblici (DPR 503/1996)
  ne' l'accessibilita' digitale (`accessibilita-siti-app-l4-2004`).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare gli indici di L. 13/1989 e DM 236/1989 pinnati
  (nuovi hash) e verificare il coordinamento con il DPR 380/2001.
- Validazione Livello 2 con esperto di accessibilita' / ufficio tecnico comunale.
