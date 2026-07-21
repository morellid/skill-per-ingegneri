# AGENTS.md - costruzioni-muratura-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione delle
costruzioni in muratura** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 4.5**: materiali e categorie degli elementi, organizzazione strutturale, resistenze di
progetto e coefficienti parziali, verifiche agli stati limite e verifiche semplificate, muratura armata.
Target: ingegneri strutturisti e progettisti.

**E' una skill documentale per il tecnico**: fornisce la classificazione degli elementi (Tab. 4.5.I), il
coefficiente γM (Tab. 4.5.II), il coefficiente Φ (Tab. 4.5.III), il fattore di vincolo ρ (Tab. 4.5.IV) e
i criteri di verifica; **non calcola** le resistenze, **non esegue** le verifiche e **non dimensiona** la
muratura.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Complementare, non sovrapposta, alle altre skill NTC del repo (`carichi-…`,
`combinazioni-carico-ntc`, `fondazioni-pali-ntc`, `opere-sostegno-ntc`): questa copre il **materiale
muratura** e le sue verifiche **non sismiche** (§4.5). La progettazione **sismica** della muratura (§7.8)
e la **resistenza al fuoco** (§4.5.11) restano fuori scope. Condivide con le altre skill NTC la stessa
fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-4-5**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 4.5 estratto con `pdftotext -layout` (pp. 141-146) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-4-5.md`; estratto operativo in
`references/estratti/costruzioni-muratura-checklist.md`.

## Punti chiave (verificati sul testo)

- **Elementi** (§4.5.2): classificati per **foratura Π** (Tab. 4.5.Ia laterizio / 4.5.Ib calcestruzzo):
  **pieni** (≤15%), **semipieni** (15-45%), **forati** (45-55%); **categoria I o II** (§11.10.1).
- **Meccanica** (§4.5.3): **fk**, **fvk0**, **E**, **G**; controllo sperimentale se **fk ≥ 8 MPa**.
- **Organizzazione** (§4.5.4): comportamento **scatolare**, cordoli e incatenamenti; **spessori minimi**
  150/200/240 (artificiali pieni/semipieni/forati) e 240/400/500 (pietra squadrata/listata/non squadrata)
  mm; **snellezza λ = h0/t ≤ 20**.
- **Resistenze di progetto** (§4.5.6.1): **fd = fk/γM**, **fvd = fvk/γM**; **Tab. 4.5.II** γM da **2,0** a
  **3,0** secondo categoria, malta e classe di esecuzione (1/2).
- **SLU** (§4.5.6.2): pressoflessione fuori/nel piano, taglio, carichi concentrati; metodo semplificato
  **fd,rid = Φ·fd** (Tab. 4.5.III), **h0 = ρ·h** (Tab. 4.5.IV), eccentricità **e1, e2 ≤ 0,33 t**.
- **Verifiche semplificate** (§4.5.6.4): **γM = 4,2**; ≤ 3 piani (ordinaria)/4 (armata); interpiano ≤ 3,5
  m; snellezza ≤ 12; carico variabile ≤ 3,00 kN/m²; rapporto lati ≥ 1/3; **σ = N/(0,65 A) ≤ fk/γM**.
- **Muratura armata** (§4.5.7): barre ≥ 5 mm; percentuali di armatura; malta ≥ 10 MPa, cls ≥ C12/15;
  **γs = 1,15**.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le resistenze (fd, fvd) né **eseguire** le verifiche (pressoflessione, taglio, tensione
  media); non **dimensionare** la muratura né le armature.
- Non **trattare** la **progettazione sismica** della muratura (§7.8) né la **Tab. 7.8.II** (percentuali di
  parete), la **resistenza al fuoco** (§4.5.11), il **cap. 11.10** (materiali) né gli **Eurocodici** (§4.6).
- Non **riprodurre** la **Circolare 21/1/2019 n. 7**.

### Cosa fare
- Fornire la classificazione degli elementi (Tab. 4.5.I), i coefficienti γM (Tab. 4.5.II), Φ (Tab. 4.5.III)
  e ρ (Tab. 4.5.IV), gli spessori minimi e la snellezza, i criteri delle verifiche SLU e semplificate, i
  requisiti della muratura armata, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 4.5. Verificare che le Tab. 4.5.I/II/III/IV e i coefficienti (γM, γs,
snellezze, spessori) non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #380)
- Task files: 2 (`inquadra-materiali-resistenze-muratura.md`,
  `inquadra-organizzazione-verifiche-muratura.md`)
- Esempi: 2 (categoria elemento e coefficiente γM per un muro portante; applicabilità delle verifiche
  semplificate a un edificio in muratura ordinaria)
