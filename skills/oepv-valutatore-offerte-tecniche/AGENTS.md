# AGENTS.md - oepv-valutatore-offerte-tecniche

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto alla valutazione OEPV (Offerta Economicamente Piu' Vantaggiosa) nelle procedure di appalto pubblico italiano ai sensi del D.Lgs. 31 marzo 2023 n. 36 (Codice dei contratti pubblici). Target: RUP, commissioni giudicatrici, stazioni appaltanti. Il rischio principale e' produrre matrici criteri non conformi all'art. 108 che espongano la gara a ricorso TAR con annullamento dell'aggiudicazione.

## Fonti autoritative

Fonti catalogate in `references/sources.yaml`:

- **D.Lgs. 36/2023** - id `dlgs-36-2023-originale-gu-2023` - fonte primaria vincolante
- **D.Lgs. 209/2024 (correttivo)** - id `dlgs-209-2024-correttivo` - modifiche al codice
- **ANAC Linea Guida n. 2 (Delibera 424/2018)** - id `anac-linea-guida-n2-delibera-424-2018` - metodologia aggregativo-compensatore; NON vincolante sotto D.Lgs. 36/2023 ma ancora standard operativo
- **D.Lgs. 198/2006 art. 46-bis** - id `dlgs-198-2006-art46bis` - certificazione parita' di genere

Estratti in `references/estratti/`:
- `dlgs-36-art93.md` - commissione giudicatrice (composizione, incompatibilita', procedura)
- `dlgs-36-art107-108.md` - criteri di aggiudicazione, OEPV obbligatorio, limiti punteggio economico, tre categorie art. 108 co. 7
- `anac-lg-n2-metodologia-oepv.md` - aggregativo-compensatore, metodi tabellare/discrezionale/formula, riproporzionamento, esempio numerico

## Articoli e punti chiave

- **Art. 108 co. 2**: elenco casi dove OEPV e' OBBLIGATORIO (servizi tecnici >= 140k EUR, IT >= 140k EUR, appalti integrati, servizi sociali, trasporto scolastico)
- **Art. 108 co. 3**: prezzo piu' basso ammesso solo per forniture/servizi standardizzati; VIETATO per alta intensita' manodopera
- **Art. 108 co. 4**: limiti punteggio economico - IT strategico max 10%; alta intensita' manodopera max 30%
- **Art. 108 co. 6**: criteri devono essere COLLEGATI ALL'OGGETTO del contratto - criteri soggettivi sull'impresa (solidita' economica, referenze generiche) sono ILLEGITTIMI come criteri OEPV
- **Art. 108 co. 7**: TRE categorie per cui il punteggio massimo disponibile e' SEMPRE obbligatorio: (1) basse emissioni CO2, (2) welfare aziendale, (3) certificazione parita' di genere (D.Lgs. 198/2006 art. 46-bis)
- **Art. 108 co. 11**: per lavori, VIETATO assegnare punti per varianti o opere non previste nel progetto a base di gara
- **Art. 93 co. 9**: commissione nominata DOPO scadenza offerte (mai prima)
- **Art. 93 co. 4**: cause di incompatibilita' commissari (progettista del progetto a base di gara, chi ha partecipato a consulenze, chi ha rapporti con operatori partecipanti)

## Convenzioni specifiche

### Cosa NON fare

- Non produrre matrici che includono criteri soggettivi sull'impresa (solidita' patrimoniale, referenze generiche, fatturato): quelli sono requisiti di partecipazione, non criteri OEPV. Cita sempre art. 108 co. 6.
- Non omettere nessuna delle tre categorie obbligatorie dell'art. 108 co. 7. Se una categoria sembra non pertinente all'oggetto specifico, documentare la ragione con riferimento all'art. 108 co. 6, non ignorarla silenziosamente.
- Non usare la formula ribasso nella forma `Vmax x (Ribasso_max / Ribasso_i)`: quella formula e' matematicamente sbagliata (supera Vmax). La formula corretta e' `Vmax x (Ribasso_i / Ribasso_max)` (crescente) oppure usare il prezzo `Vmax x (Prezzo_min / Prezzo_i)`.
- Non citare "Allegato II.4 D.Lgs. 36/2023" come fonte per OEPV: quell'allegato riguarda la qualificazione delle stazioni appaltanti, non la valutazione delle offerte. La fonte corretta e' l'art. 108.
- Non definire criteri discrezionali senza descrittori: una matrice con un solo criterio "qualita' tecnica" senza sub-elementi e' illegittima per giurisprudenza costante.
- Non dichiarare mai che una matrice e' "legalmente valida" o "sicura da ricorsi TAR": la skill produce support all'analisi, non certifica la legittimita'.

### Cosa fare

- Citare sempre l'articolo e il comma preciso per ogni regola applicata (es. "art. 108 co. 7 D.Lgs. 36/2023" non "il Codice dei contratti").
- Quando costruisci una matrice, verificare SEMPRE tutti e tre i requisiti di Passo 1: (a) OEPV obbligatorio?, (b) limite punteggio economico?, (c) tutte e tre le categorie art. 108 co. 7?
- Per criteri discrezionali, includere sempre i descrittori per livello (0-0.25 / 0.25-0.50 / 0.50-0.75 / 0.75-1.00) con testo che descrive cosa corrispondono.
- Per il riproporzionamento: dichiararlo esplicitamente nella matrice (non e' implicito). La commissione non puo' applicarlo senza averlo dichiarato nel disciplinare.
- Concludere ogni output di check con le avvertenze sulle revisione legale per gare rilevanti.
- La formula economica corretta per prezzo: `Pe_i = Vmax x (Prezzo_min / Prezzo_i)`. Per ribasso: `Pe_i = Vmax x (Ribasso_i / Ribasso_max)`.

## Validatori

- Nessun validatore Livello 2 identificato al momento del rilascio. La skill richiede validazione da RUP esperto o consulente legale specializzato in appalti pubblici prima di passare a Livello 2.

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 (revisione interna, nessun esperto di dominio esterno)
- Task files: 3 (costruisci-matrice-criteri, valuta-offerta-tecnica, check-matrice-criteri)
- Esempi: 1 conforme (servizi architettura/ingegneria) + 1 non conforme (lavori con matrice problematica)
- Known issues: nessun esempio con calcolo completo per valuta-offerta-tecnica; lifecycle costing (art. 110) non coperto
