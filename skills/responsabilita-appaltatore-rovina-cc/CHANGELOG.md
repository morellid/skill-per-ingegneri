# CHANGELOG - responsabilita-appaltatore-rovina-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #290)
- Prima versione della skill di supporto alla **responsabilità dell'appaltatore** per difformità/vizi
  dell'opera e per la **rovina e i gravi difetti** degli edifici, ai sensi del **Codice civile, artt.
  1667, 1668, 1669**, nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice civile (R.D. 262/1942)** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (codice 042U0262). Artt. 1667, 1668, 1669 (idGruppo 208, flagTipoArticolo 2) via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/cc-artt-1667-1668-1669.md`.
- Estratto operativo `references/estratti/responsabilita-appaltatore-checklist.md`.
- Due task: `inquadra-garanzia-vizi.md` e `inquadra-rovina-1669.md`.
- Due esempi: vizi scoperti dopo la consegna (artt. 1667-1668); gravi difetti dell'edificio verso
  l'acquirente/avente causa (art. 1669).

### Contenuto ancorato al testo
- Art. 1667 garanzia per difformità/vizi (esclusione per vizi noti/riconoscibili salvo mala fede;
  denuncia 60 gg a pena di decadenza; prescrizione 2 anni dalla consegna; eccezione del committente
  convenuto); art. 1668 rimedi (eliminazione/riduzione/risarcimento/risoluzione); art. 1669 rovina e
  gravi difetti di immobili a lunga durata, responsabilità decennale verso committente e aventi causa,
  denuncia entro 1 anno dalla scoperta, prescrizione 1 anno dalla denuncia.

### Scope e limiti
- Non accerta i vizi/la rovina, il nesso causale o il quantum, non fornisce l'interpretazione
  giurisprudenziale dell'art. 1669 né la strategia processuale, non sostituisce il legale, il CTU o il
  giudice. Altri articoli del Capo VII (1655, 1660-1666, 1670-1676) citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del Codice civile pinnato (nuovo hash) e
  rileggere gli artt. 1667-1669.
- Validazione Livello 2 con avvocato civilista o CTU esperto in edilizia.
