# CHANGELOG - carico-incendio-classe-resistenza-dm

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #443)
- Prima versione della skill di supporto al **progettista antincendio / strutturale** per la
  **determinazione del carico d'incendio specifico di progetto q_f,d** e della conseguente **classe di
  resistenza al fuoco** secondo il **DM 9 marzo 2007** (Prestazioni di resistenza al fuoco delle costruzioni
  nelle attività soggette al controllo del CNVVF), nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **DM 9 marzo 2007** - PDF della G.U. Serie Generale n. 74 del 29 marzo 2007 - Suppl. Ord. n. 87 - SHA256:
    c7003438fcf4142cd87534a4588ba3c66adee81ec9fb06f328c8a7310ab4b0bc (doppio download riproducibile dallo
    stesso URL eli della Gazzetta Ufficiale).
  - Il PDF è una scansione GURITEL (immagine): formula, tabelle e curve sono state lette renderizzando le
    pagine in immagine (`pdftoppm -r 135/150 -png`) e trascritte verbatim in
    `references/fonti/dm-9-3-2007.md` (Tabelle 1-5, formule del carico d'incendio e delle curve nominali).
- Estratto operativo `references/estratti/carico-incendio-checklist.md`.
- Due task: `calcola-carico-incendio-specifico-progetto.md` e `determina-livello-classe-resistenza.md`.
- Due esempi: calcolo di q_f,d per un compartimento con misure di protezione (δ_q1, δ_q2, δ_n);
  determinazione della classe per il livello III via Tabella 4.

### Contenuto ancorato al testo
- Carico d'incendio specifico (punto 1): q = Σ g_i·H_i·m_i·ψ_i [MJ]; q_f = q/A [MJ/m²]; H_i potere calorifico
  inferiore (UNI EN ISO 1716:2002); m_i = 0,80 (legno/cellulosici) / 1,00 (altri); ψ_i = 0 / 0,85 / 1.
  Carico d'incendio di progetto (punto 2): q_f,d = δ_q1·δ_q2·δ_n·q_f; Tabella 1 (δ_q1 per superficie:
  1,00…2,00); Tabella 2 (δ_q2 per classe di rischio I/II/III: 0,80/1,00/1,20); Tabella 3 (δ_n = prodotto dei
  δ_ni delle misure di protezione). Livelli di prestazione I-V (punto 3): livello I non ammesso; livello II
  classe 30/60 alle condizioni previste; livello III classi in Tabella 4 (per q_f,d); livelli IV-V su
  richiesta (DM 14/9/2005). Classi: 15, 20, 30, 45, 60, 90, 120, 180, 240, 360 minuti. Curve nominali
  (punto 4): standard θ_g = 20 + 345·log10(8t+1), idrocarburi, esterna; Tabella 5 (approccio con curve
  naturali).

### Scope e limiti
- Non esegue il progetto prestazionale con curve naturali/modelli d'incendio né le analisi termiche/meccaniche,
  non fornisce le proprietà dei materiali ad alta temperatura (Eurocodici parte 1-2) né i valori di H_i (UNI
  EN ISO 1716), non riproduce le regole tecniche verticali VVF né il DM 14/9/2005 (livelli IV-V), non tratta i
  procedimenti antincendio (DPR 151/2011). Non sostituisce il professionista antincendio né il progettista
  strutturale.

### Note di sviluppo
- Complementare a `resistenza-fuoco-strutture-ntc` (NTC 2018 §3.6.1), che rinvia esplicitamente a questo DM il
  calcolo del carico d'incendio; distinta da `prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti
  VVF). Fonte GURITEL letta via immagine. Validazione Livello 2 con professionista antincendio/ingegnere
  strutturista.
