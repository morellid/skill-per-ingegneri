# AGENTS.md - opere-materiali-sciolti-scavi-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico** per l'**inquadramento della progettazione e della verifica
delle opere di materiali sciolti** (rilevati, argini di difesa, rinfianchi, rinterri, terrapieni, colmate) e dei
**fronti di scavo** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.8**: criteri generali, verifiche
SLU/SLE, aspetti costruttivi, controlli e monitoraggio, e disciplina dei fronti di scavo. Target: ingegneri
geotecnici.

**E' una skill documentale per il tecnico**: fornisce i criteri, la procedura di verifica (Combinazione 2
A2+M2+R2, Tab. 6.8.I con gamma_R = 1,1, stabilita' globale nelle diverse fasi) e la regola della struttura di
sostegno dei fronti di scavo; **non calcola** le verifiche, **non dimensiona** il manufatto/fronte e **non
definisce** il modello geotecnico.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `opere-sostegno-ntc` (§6.5, muri e paratie),
`stabilita-pendii-naturali-ntc` (§6.3) e `relazione-geologica-geotecnica-ntc` (che esclude i §6.3-6.12). E'
**distinta** da `sicurezza-scavi-fondazioni-dlgs81` (sicurezza dei lavoratori negli scavi, D.Lgs 81/2008 Titolo
IV: armature/sbadacchiature a protezione degli addetti) e da `terre-rocce-scavo-dpr120` (terre e rocce da scavo
come sottoprodotti, DPR 120/2017): il §6.8 e' la **verifica geotecnica** del manufatto/fronte come opera.
Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope
gli sbarramenti di ritenuta idraulica (dighe in terra: normativa specifica) e la progettazione sismica (Cap. 7).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-8**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 6.8 estratto con `pdftotext -layout` (pp. GU 201-202) e trascritto verbatim; Tab. 6.8.I e la soglia dei
  2 m verificate anche sull'immagine renderizzata della pagina (pdftoppm).

Trascrizione in `references/fonti/ntc2018-par-6-8.md`; estratto operativo in
`references/estratti/materiali-sciolti-scavi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (§6.8): manufatti di materiali sciolti (rilevati, argini, rinfianchi, rinterri, terrapieni,
  colmate) e opere con funzioni di drenaggio/filtro/transizione/fondazione/tenuta/protezione. **Esclusi** gli
  sbarramenti di ritenuta idraulica.
- **Criteri generali** (§6.8.1): requisiti prestazionali, terreni di fondazione, scelta e qualificazione dei
  materiali, posa in opera (spessore max strati, compattazione, deformabilita').
- **Verifiche SLU** (§6.8.2): condizione [6.2.1]; **Combinazione 2 (A2+M2+R2)** dell'Approccio 1; Tab. 6.2.I,
  6.2.II e **6.8.I (gamma_R = 1,1, R2)**; stabilita' globale manufatto-terreno nelle diverse fasi/fine
  costruzione/esercizio; verifiche locali sugli elementi di rinforzo; ritenuta idraulica -> sifonamento/erosione.
- **SLE** (§6.8.3): spostamenti manufatto/terreno, compatibili con funzionalita' e manufatti adiacenti.
- **Costruttivi/monitoraggio** (§6.8.4-6.8.5): posa in strati; geosintetici certificati; monitoraggio di
  spostamenti e pressioni interstiziali.
- **Fronti di scavo** (§6.8.6): indagini (profondita', ampiezza, destinazione, permanente/provvisorio); verifica
  analoga ai materiali sciolti; **struttura di sostegno** per scavi in trincea a **fronte verticale > 2 m con
  permanenza di personale** o **in prossimita' di manufatti** (verifiche SLU e SLE); azioni nelle condizioni piu'
  sfavorevoli.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le verifiche né **dimensionare** il manufatto, il fronte di scavo o la struttura di sostegno;
  non **definire** il modello geotecnico.
- Non **confondere** la struttura di sostegno delle pareti di scavo (verifica geotecnica NTC §6.8.6) con le
  armature/sbadacchiature per la **sicurezza dei lavoratori** (D.Lgs 81/2008 Titolo IV).
- Non **trattare** gli sbarramenti di ritenuta idraulica (dighe in terra), le terre e rocce da scavo come
  sottoprodotti (DPR 120/2017) né la progettazione sismica (Cap. 7).

### Cosa fare
- Fornire criteri, procedura di verifica (A2+M2+R2, Tab. 6.8.I gamma_R = 1,1, stabilita' globale nelle varie
  fasi) e la regola dei fronti di scavo, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.8. Verificare la Combinazione 2 (A2+M2+R2), il valore della Tab. 6.8.I
(gamma_R = 1,1) e la soglia dei 2 m dei fronti di scavo verticali.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #411)
- Task files: 2 (`inquadra-verifica-materiali-sciolti.md`, `inquadra-fronti-scavo.md`)
- Esempi: 2 (verifica di un rilevato stradale con Combinazione 2 e Tab. 6.8.I; fronte di scavo in trincea e
  soglia dei 2 m per la struttura di sostegno)
