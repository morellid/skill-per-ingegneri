# CHANGELOG - mog-231-sicurezza-lavoro

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #46, parte speciale salute e sicurezza sul lavoro)
- Prima versione della skill di supporto documentale al **MOG 231 per la salute e
  sicurezza sul lavoro** (art. 25-septies D.Lgs 231/2001 + art. 30 D.Lgs 81/2008),
  nell'area `sicurezza-lavoro-cantieri`.
- Chiude l'issue #46 (MOG 231 - mappatura rischi reato) limitatamente alla **parte
  speciale sicurezza sul lavoro**, la piu' rilevante per l'ingegneria; mirror del pattern
  di `mog-231-reati-ambientali` (#63, reati ambientali).
- Fonti scaricate, hashate e lette (Regola zero):
  - **D.Lgs. 231/2001** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: f6025f504910c6bd3f0e49a5f50e94a93b33e5124e50ea6f5fc9b394d7b66eb6
    (codice 001G0293). Artt. 5, 6, 7 e 25-septies (idSottoArticolo=7) via caricaArticolo.
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831
    (codice 008G0104). Art. 30 via caricaArticolo.
  - Trascritti verbatim in `references/fonti/mog-231-sicurezza-lavoro.md`.
- Estratto operativo `references/estratti/mog-231-sicurezza-checklist.md`.
- Due task: `mappa-rischio-reato.md` e `struttura-mog-art30.md`.
- Due esempi: impresa di costruzioni (perche'/quando risponde l'ente); PMI con ISO 45001
  (presunzione di conformita' "per le parti corrispondenti").

### Contenuto ancorato al testo
- Responsabilita' dell'ente (art. 5), esimente apicali/sottoposti (artt. 6-7), reato
  art. 25-septies (omicidio/lesioni colpose sul lavoro, sanzioni in quote e interdittive).
- Requisiti del MOG art. 30: obblighi a-h, registrazione (c.2), funzioni + sistema
  disciplinare (c.3), controllo/riesame (c.4), presunzione di conformita' UNI-INAIL SGSL /
  UNI EN ISO 45001 (c.5), semplificazioni PMI (c.5-bis, c.5-ter agg. L. 34/2026).

### Scope e limiti
- Non redige il modello ne' i protocolli; non certifica l'idoneita'/efficace attuazione
  (giudizio del giudice). Non copre gli altri reati presupposto 231 (ambientali ->
  `mog-231-reati-ambientali`; o la mappatura generale multi-reato).

### Note di sviluppo
- Normattiva: riscaricare le pagine pinnate (nuovi hash) e rileggere gli articoli ad ogni
  aggiornamento; attenzione all'agg. L. 34/2026 sull'art. 30 c.5-ter.
- Validazione Livello 2 con esperto 231 / legale del lavoro.
