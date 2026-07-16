# CHANGELOG - gap-analysis-misure-minime-ict-agid

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #53)
- Prima versione della skill di supporto alla **gap analysis delle Misure Minime di
  Sicurezza ICT per le PA** (ABSC, Circolare AgID 2/2017), nell'area
  `software-dati-cybersecurity`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Circolare AgID 18/4/2017 n. 2/2017** - **PDF ufficiale della G.U. n. 103/2017**
    (codice 17A03060). SHA256: 24e4956ef483426bb9ebbdc425d941c150830436bdc4ba7fa71e558dc7986725
    (riproducibile, doppio download; host gazzettaufficiale.it in allowlist). Articoli
    letti anche via caricaArticolo; trascritti verbatim in
    `references/fonti/circolare-agid-2-2017.md` gli artt. (Premessa/Scopo, 2-5), la
    struttura degli ABSC, i tre livelli e i titoli+descrizioni delle 8 famiglie ABSC.
- Estratto operativo `references/estratti/absc-gap-analysis-checklist.md`.
- Due task: `imposta-gap-analysis.md` e `compila-modulo-implementazione.md`.
- Due esempi: piccolo Comune (livello minimo, da dove partire); gruppo ABSC 5 (privilegi
  di amministratore, come determinare l'obbligatorieta').

### Contenuto ancorato al testo
- **8 gruppi ABSC**: 1 inventario dispositivi, 2 inventario software, 3 configurazioni, 4
  vulnerabilita', 5 privilegi admin, 8 malware, 10 backup, 13 protezione dati.
- **3 livelli**: Minimo (soglia obbligatoria), Standard (base), Alto (obiettivo).
- **Framework**: destinatari (art. 2), responsabile (art. 3), modulo di implementazione
  con firma digitale + marcatura temporale e CERT-PA (art. 4), tempi (art. 5).

### Limite di resa e scope
- La **matrice completa** dei singoli controlli (`ABSC_ID x.y.z` con i flag
  Minimo/Standard/Alto) e' una **tabella in formato grafico** nel PDF: la resa testuale
  non conserva l'allineamento delle colonne X, quindi il **livello esatto** va letto sul
  PDF. La skill copre ambito, struttura, livelli e metodo, non la matrice puntuale.
- Non esegue l'assessment tecnico. Per alcuni soggetti si aggiunge **NIS2** (D.Lgs
  138/2024): vedi `nis2-self-assessment`.

### Note di sviluppo
- Fonte GU: il PDF della G.U. n. 103/2017 e' stabile (hash 24e4956e...). Verificare
  l'evoluzione del quadro (NIS2/misure ACN) prima di modifiche sostanziali.
- Validazione Livello 2 con esperto sicurezza ICT PA.
