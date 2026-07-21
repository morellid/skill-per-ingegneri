# CHANGELOG - opere-sotterraneo-gallerie-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #414)
- Prima versione della skill di supporto al **progettista geotecnico e strutturale** per l'**inquadramento della
  progettazione e della verifica delle opere in sotterraneo** (gallerie, caverne, pozzi) secondo le **NTC 2018**
  (DM 17 gennaio 2018), **paragrafo 6.7**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 6.7 estratto con `pdftotext -layout` (pp. GU 200-201) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-7.md`.
- Estratto operativo `references/estratti/opere-sotterraneo-checklist.md`.
- Due task: `inquadra-verifiche-opere-sotterraneo.md` e `inquadra-caratterizzazione-progetto-monitoraggio.md`.
- Due esempi: stati limite e combinazioni SLU di una galleria (GEO/STR/UPL/HYD, Approccio 1 con Comb. 1 e Comb.
  2, gamma_R = 1,0 per R1/R2); elementi da specificare e giustificare nel progetto e grandezze del metodo
  osservazionale.

### Contenuto ancorato al testo
- Ambito (§6.7): gallerie, caverne e pozzi costruiti nel sottosuolo. Prescrizioni generali (§6.7.1): modello
  geologico e geotecnico; elementi da specificare/giustificare (geometria/ubicazione/tracciato; metodi e
  tecniche di scavo tradizionale o meccanizzato; interventi di stabilizzazione e rivestimenti; intercettazione
  acque e pressioni interstiziali; provvedimenti antifrana; sicurezza per gas/cavita'/venute d'acqua; materiali
  di risulta). Caratterizzazione geologica (§6.7.2) e geotecnica (§6.7.3). Criteri di progetto (§6.7.4):
  previsione quantitativa degli effetti indotti, rivestimenti, imbocchi, stabilita' dei pendii in versante.
  Analisi e verifiche (§6.7.5): SLU GEO e STR, effetti sui manufatti esistenti, SLU idraulici UPL e HYD;
  stabilita' di versanti e fronti agli imbocchi con i criteri dei §6.3 e §6.8; Approccio 1 con Combinazione 1
  (A1+M1+R1) e Combinazione 2 (A2+M2+R2), coefficienti Tab. 6.2.I/6.2.II e gamma_R dei gruppi R1 e R2 pari
  all'unita' (1,0); verifiche strutturali con valori caratteristici (§6.2.4.1.3) e idrauliche (§6.2.4.2); metodo
  osservazionale (§6.2.5) con convergenza radiale, deformazione longitudinale del fronte e spostamenti di
  superficie. Controllo e monitoraggio (§6.7.6).

### Scope e limiti
- Non calcola le verifiche né dimensiona l'opera/rivestimenti, non definisce il modello geologico/geotecnico, non
  tratta la sicurezza dei lavoratori in sotterraneo, le macchine di scavo (TBM) come prodotti né la
  progettazione sismica (Cap. 7), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `stabilita-pendii-naturali-ntc` (§6.3), `opere-materiali-sciolti-scavi-ntc` (§6.8) e
  `relazione-geologica-geotecnica-ntc`, condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere
  geotecnico/strutturista.
