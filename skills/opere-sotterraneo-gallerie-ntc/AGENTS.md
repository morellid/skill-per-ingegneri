# AGENTS.md - opere-sotterraneo-gallerie-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico e strutturale** per l'**inquadramento della progettazione e
della verifica delle opere in sotterraneo** (gallerie, caverne, pozzi) secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 6.7**: prescrizioni generali, caratterizzazione geologica e geotecnica, criteri di progetto,
analisi e verifiche di sicurezza, controllo e monitoraggio. Target: ingegneri geotecnici e strutturisti.

**E' una skill documentale per il tecnico**: fornisce gli elementi da giustificare, gli stati limite (GEO, STR,
UPL, HYD) e la procedura di verifica (Approccio 1 con Comb. 1 A1+M1+R1 e Comb. 2 A2+M2+R2, gamma_R dei gruppi R1
e R2 pari all'unita'); **non calcola** le verifiche, **non dimensiona** l'opera o i rivestimenti e **non
definisce** il modello geologico/geotecnico.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `stabilita-pendii-naturali-ntc` (§6.3, richiamato al §6.7.5 per la
stabilita' dei versanti), `opere-materiali-sciolti-scavi-ntc` (§6.8, richiamato per i fronti agli imbocchi) e
`relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12). Condivide con le altre skill NTC la stessa fonte
(PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope la sicurezza dei lavoratori in sotterraneo, le
macchine di scavo (TBM) come prodotti e la progettazione sismica (Cap. 7).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-7**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 6.7 estratto con `pdftotext -layout` (pp. GU 200-201) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-7.md`; estratto operativo in
`references/estratti/opere-sotterraneo-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (§6.7): gallerie, caverne, pozzi costruiti nel sottosuolo (scavo, stabilizzazione, rivestimento).
- **Prescrizioni generali** (§6.7.1): modello geologico/geotecnico; elementi da specificare/giustificare
  (tracciato, metodi di scavo tradizionale o meccanizzato, interventi di stabilizzazione e rivestimenti,
  imbocchi, acque, antifrana, sicurezza gas/cavita'/venute d'acqua, materiali di risulta).
- **Caratterizzazione** (§6.7.2-6.7.3): geologica (litotipi, faglie, sismotettonica, franosita', carsismo,
  idrogeologia) e geotecnica (potenzialita' spingenti/rigonfianti, pressioni interstiziali, metodo
  osservazionale).
- **Criteri di progetto** (§6.7.4): previsione quantitativa degli effetti indotti al contorno e in superficie
  (gallerie poco profonde in ambienti urbanizzati); rivestimenti; imbocchi; stabilita' dei pendii in versante.
- **Verifiche** (§6.7.5): SLU **GEO** e **STR**, effetti sui manufatti esistenti, SLU idraulici **UPL** e
  **HYD**; stabilita' di versanti e fronti agli imbocchi con §6.3 e §6.8; **Approccio 1** con **Comb. 1
  (A1+M1+R1)** e **Comb. 2 (A2+M2+R2)**, **gamma_R dei gruppi R1 e R2 pari all'unita' (1,0)**; verifiche
  strutturali con valori caratteristici (§6.2.4.1.3) e idrauliche (§6.2.4.2); metodo osservazionale (convergenza
  radiale, deformazione longitudinale del fronte, spostamenti di superficie).
- **Monitoraggio** (§6.7.6): validita' delle previsioni; comportamento di terreno/ammasso, rivestimenti e
  manufatti esistenti; fenomeni franosi (tensioni, spostamenti, pressioni interstiziali).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le verifiche né **dimensionare** l'opera, i rivestimenti o gli interventi di
  stabilizzazione; non **definire** il modello geologico/geotecnico.
- Non **trattare** la sicurezza dei lavoratori in sotterraneo, le macchine di scavo (TBM) come prodotti né la
  progettazione sismica (Cap. 7).

### Cosa fare
- Fornire gli elementi da giustificare, gli stati limite (GEO/STR/UPL/HYD) e la procedura di verifica (Approccio
  1, Comb. 1 e 2, gamma_R = 1,0 per R1/R2), sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.7. Verificare gli stati limite (GEO/STR/UPL/HYD), l'Approccio 1 con entrambe
le combinazioni e il gamma_R dei gruppi R1 e R2 pari all'unita'.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico/strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #414)
- Task files: 2 (`inquadra-verifiche-opere-sotterraneo.md`, `inquadra-caratterizzazione-progetto-monitoraggio.md`)
- Esempi: 2 (stati limite e combinazioni SLU di una galleria; elementi da giustificare nel progetto e grandezze
  del metodo osservazionale)
