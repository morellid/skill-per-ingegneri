# CHANGELOG - documento-informatico-firme-cad

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #270)
- Prima versione della skill di supporto al **valore giuridico del documento informatico** e
  delle **firme elettroniche**, ai sensi degli **artt. 20, 21 e 24 del D.Lgs. 82/2005 (CAD)**,
  nell'area `software-dati-cybersecurity`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 7 marzo 2005, n. 82 (CAD)** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 5e75c6b9215888cba2dd5d118c6aa3baf6b3d26eee09d54af7c2f84e20f28222
    (codice 005G0104). Artt. 20, 21, 24 via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/cad-artt-20-21-24.md`: artt. 20, 21 e 24 per
    intero (testo vigente, con i commi abrogati e i blocchi (( )) come da Normattiva).
- Estratto operativo `references/estratti/documento-informatico-checklist.md`.
- Due task: `valuta-valore-documento.md` e `inquadra-firma-atto.md`.
- Due esempi: relazione tecnica firmata digitalmente (art. 2702 c.c.); e-mail semplice
  (documento informatico liberamente valutabile).

### Contenuto ancorato al testo
- Art. 20: forma scritta ed efficacia art. 2702 c.c. con firma digitale/qualificata/avanzata o
  processo con requisiti AgID; libera valutazione negli altri casi; presunzione di
  riconducibilita' al titolare (c. 1-ter).
- Art. 21: scritture private art. 1350 nn. 1-12 c.c. a pena di nullita' con firma qualificata/
  digitale; atto pubblico informatico (c. 2-bis/2-ter).
- Art. 24: firma digitale univoca; sostituzione di sigilli/timbri; certificato qualificato non
  scaduto/revocato/sospeso; firma su certificato revocato = mancata sottoscrizione (c. 4-bis).

### Scope e limiti
- Non riproduce le Linee guida AgID (art. 71) ne' l'eIDAS (Reg. UE 910/2014): rinvio. Non appone
  ne' verifica firme, non valuta la validita' del singolo atto, non sostituisce professionista,
  notaio ne' giudice. Non tratta conservazione (artt. 43-44) e copie/duplicati (artt. 22-23-bis).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del CAD pinnato (nuovo hash) e
  verificare le modifiche (il CAD e' molto modificato; commi abrogati, blocchi (( ))).
- Validazione Livello 2 con esperto di diritto dell'informatica / notaio.
