# CHANGELOG - ancoraggi-precompressione-appoggi-qualificazione-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #472)
- Prima versione della skill di supporto al **progettista strutturale** e al **Direttore dei Lavori** per la
  **qualificazione** e i **controlli di accettazione in cantiere** di **ancoranti per uso strutturale**, **giunti di
  dilatazione stradale**, **sistemi di precompressione a cavi post-tesi**, **tiranti di ancoraggio per uso
  geotecnico** e **appoggi strutturali** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 11.4, 11.5 e
  11.6** (Cap. 11), nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.4-11.6 (pagina PDF 348 = GU 344) estratto con `pdftotext -layout`; i riferimenti (categoria C2, Sistema
    VVCP 1, sigle ETAG 001/032/013, serie UNI EN 1337) verificati sull'immagine (`pdftoppm -r 150 -png`) della pagina
    PDF 348 e trascritti verbatim in `references/fonti/ntc2018-par-11-4-11-6.md`.
- Estratto operativo `references/estratti/ancoraggi-appoggi-checklist.md`.
- Due task: `inquadra-ancoranti-e-giunti.md` e `inquadra-precompressione-tiranti-e-appoggi.md`.
- Due esempi: accettazione di ancoranti in zona sismica con categoria C2; accettazione di appoggi strutturali per un
  ponte (UNI EN 1337).

### Contenuto ancorato al testo
- Ancoranti (§11.4.1): qualificazione punto C) del §11.1, base ETAG 001 (anche prove di accettazione); per azioni
  sismiche, per tutte le classi d'uso (punto 2.4.2) categoria di prestazione minima da soddisfare = C2 (Annesso E,
  tab. 1.1, §1.2 ETAG 001). Giunti di dilatazione stradale (§11.4.2): punto C) del §11.1, base ETAG 032.
  Precompressione a cavi post-tesi (§11.5.1): punto C) del §11.1; Certificato di valutazione tecnica (Linea Guida
  CSLP); fornitura con CVT o marcatura CE su ETA + manuale; il Direttore dei Lavori verifica, rifiuta le forniture
  prive di documentazione, verifica la posa e le prove di accettazione (verifica geometrica/tolleranze +
  caratteristiche meccaniche); prove secondo ETAG 013. Tiranti geotecnici (§11.5.2): attivi/passivi punto C) del
  §11.1; per i tipo attivo CVT (Linea Guida CSLP). Appoggi strutturali (§11.6): dispositivi di vincolo per trasmettere
  carichi e vincolare gradi di libertà; punto A del §11.1 → conformi alla serie UNI EN 1337 + Marcatura CE, Sistema
  VVCP 1 per applicazioni critiche; se non ricadenti → caso C) del §11.1.

### Scope e limiti
- Non esegue il progetto né le verifiche dei prodotti (progetto appoggi, verifiche ancoranti, progetto cavi post-tesi,
  verifiche geotecniche dei tiranti al §6.6); non riproduce il dettaglio delle prove delle Linee guida/norme europee
  (ETAG 001/013/032, UNI EN 1337). Non sostituisce il progettista né il Direttore dei Lavori.

### Note di sviluppo
- Distinta da `tiranti-ancoraggio-ntc` (§6.6, progetto/verifiche), `dispositivi-antisismici-qualificazione-ntc`
  (§11.9, UNI EN 15129) e dalle skill materiali del Cap. 11. Condivide la fonte GU con le altre skill NTC. Validazione
  Livello 2 con ingegnere strutturista / Direttore dei Lavori esperto di prodotti da costruzione.
