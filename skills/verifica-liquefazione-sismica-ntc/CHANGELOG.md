# CHANGELOG - verifica-liquefazione-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #446)
- Prima versione della skill di supporto al **progettista geotecnico / strutturale** per l'**inquadramento
  della verifica di stabilità del sito nei confronti della liquefazione** in condizioni sismiche secondo le
  **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.11.3.4**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.11.3.4 (pagine PDF 284-285) estratto con `pdftotext -layout` e verificato sull'immagine
    (`pdftoppm -r 150 -png`) per pedici e disuguaglianze; trascritto verbatim in
    `references/fonti/ntc2018-par-7-11-3-4.md`.
- Estratto operativo `references/estratti/verifica-liquefazione-checklist.md`.
- Due task: `valuta-esclusione-verifica-liquefazione.md` e `inquadra-metodo-coefficiente-sicurezza.md`.
- Due esempi: sito escluso dalla verifica per falda profonda / (N₁)₆₀ elevato; inquadramento del coefficiente
  di sicurezza quando nessuna condizione di esclusione è soddisfatta.

### Contenuto ancorato al testo
- Generalità (§7.11.3.4.1): definizione della liquefazione (perdita di resistenza al taglio / accumulo di
  deformazioni plastiche in terreni saturi prevalentemente sabbiosi, azioni cicliche/dinamiche in condizioni
  non drenate); se suscettibile → consolidamento o trasferimento del carico a strati non suscettibili;
  fondazioni profonde → valutare riduzione capacità portante e incrementi nei pali. Esclusione (§7.11.3.4.2,
  basta una circostanza): a_max al piano campagna in campo libero < 0,1 g; falda media stagionale > 15 m
  (piano campagna sub-orizzontale, fondazioni superficiali); sabbie pulite con (N₁)₆₀ > 30 oppure q_c1N > 180
  (SPT/CPT normalizzate a 100 kPa); granulometria esterna ai fusi di Fig. 7.11.1(a) per U_c < 3,5 e (b) per
  U_c > 3,5. Metodi di analisi (§7.11.3.4.3): coefficiente di sicurezza = resistenza disponibile alla
  liquefazione / sollecitazione indotta dal terremoto di progetto; metodi storico-empirici; resistenza da
  prove in sito o cicliche di laboratorio; sollecitazione da a_max alla profondità di interesse; margine
  valutato e motivato dal progettista.

### Scope e limiti
- Non calcola il coefficiente di sicurezza (CRR/CSR, correlazioni con (N₁)₆₀ / q_c1N, magnitudo) con metodi di
  letteratura/prove, non progetta gli interventi di consolidamento, non tratta la stabilità dei pendii sismica
  (§7.11.3.5) o statica (§6.3), né l'azione sismica di dettaglio (§3.2.3). Non sostituisce il progettista
  geotecnico.

### Note di sviluppo
- Distinta da `stabilita-pendii-naturali-ntc` (§6.3) e `verifiche-geotecniche-slu-ntc` (§6.2.4); si appoggia a
  `categorie-sottosuolo-topografiche-ntc` (§3.2.2) e `spettro-risposta-ntc` (§3.2.3). Condivide la fonte GU con
  le altre skill NTC. Validazione Livello 2 con ingegnere geotecnico.
