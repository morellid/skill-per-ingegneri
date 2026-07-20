# CHANGELOG - controlli-accettazione-cls-acciaio-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #396)
- Prima versione della skill di supporto al **Direttore dei Lavori** e al **collaudatore** per
  l'**inquadramento dei controlli di accettazione in cantiere** del **calcestruzzo** (§11.2.4-11.2.5) e
  dell'**acciaio da cemento armato** (§11.3.2.12) secondo le **NTC 2018** (DM 17 gennaio 2018), **Capitolo
  11**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 11.2 e 11.3 estratti con `pdftotext -layout` (pp. 307-309 e 326-327) e trascritti verbatim in
    `references/fonti/ntc2018-cap-11-controlli.md` (Tab. 11.2.I, Tab. 11.3.VII a/b).
- Estratto operativo `references/estratti/controlli-accettazione-checklist.md`.
- Due task: `inquadra-controllo-accettazione-calcestruzzo.md` e `inquadra-accettazione-acciaio-ca.md`.
- Due esempi: controllo di accettazione tipo A per un getto di 250 m³ di C25/30 (Rck 30); accettazione in
  cantiere di 80 t di barre B450C.

### Contenuto ancorato al testo
- **Calcestruzzo**: prelievo di 2 provini, resistenza di prelievo = media, scarto tra i due > 20% del minore →
  non accettato (§11.2.4). Controllo di accettazione tipo A (≤ 300 m³, 3 prelievi ≤ 100 m³, ≥ 1/giorno) e tipo
  B statistico (> 1500 m³, ≥ 1 controllo/1500 m³, ≥ 15 prelievi, coeff. variazione ≤ 0,3) (§11.2.5.1-2).
  Criteri Tab. 11.2.I: tipo A Rcm28 ≥ Rck + 3,5 e Rc,min ≥ Rck − 3,5; tipo B Rcm28 ≥ Rck + 1,48·s e Rc,min ≥
  Rck − 3,5. Prescrizioni comuni: verbale, laboratorio art. 59 DPR 380/2001, prove tra 28° e 30° giorno (entro
  45 gg), non conformità, obbligo del collaudatore (§11.2.5.3).
- **Acciaio da c.a.**: controlli obbligatori entro 30 gg dalla consegna, laboratorio art. 59 DPR 380; 3
  campioni ogni 30 t della stessa classe/stabilimento; valori di accettazione Tab. 11.3.VII a) barre e b)
  reti/tralicci (fy 425-572 N/mm²; Agt ≥ 6,0% B450C / ≥ 2,0% B450A; ft/fy 1,13-1,37 B450C / ≥ 1,03 B450A;
  piegamento senza cricche; distacco nodo per reti); non conformità: 6 campioni → 25 campioni → inidoneità
  della partita (§11.3.2.12).

### Scope e limiti
- Non esegue le prove né valuta la resistenza (compito del laboratorio ex art. 59 DPR 380/2001), non sostituisce
  il Direttore dei Lavori né il collaudatore, non copre i controlli in stabilimento/qualificazione
  (§11.3.2.10-11), i carotaggi/resistenza in opera (§11.2.6-11.2.7), gli aggregati, l'acciaio da carpenteria
  (§11.3.4), il legno (§11.7) né la muratura (§11.10).

### Note di sviluppo
- Copre il compito di cantiere/collaudo rinviato al §11 dalle skill "costruzioni di X" (§4.1/4.2), condividendo
  la stessa fonte GU. Validazione Livello 2 con Direttore dei Lavori/collaudatore.
