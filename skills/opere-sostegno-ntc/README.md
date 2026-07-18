# opere-sostegno-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista / geotecnico da completare)

Skill di **supporto documentale** al **progettista strutturale e geotecnico** per l'**inquadramento delle
verifiche delle opere di sostegno** - **muri di sostegno**, **paratie** e **strutture miste** - secondo
le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 6.5**.

**Non calcola** le spinte, le verifiche o i coefficienti, **non dimensiona** il muro o la paratia e **non
sostituisce** il progettista o la relazione geotecnica: inquadra tipologie, criteri, azioni, stati
limite, approcci progettuali e coefficienti parziali.

## Target

Ingegneri strutturisti e geotecnici e progettisti di opere di sostegno e di scavi che devono inquadrare
le verifiche agli stati limite di muri e paratie secondo le NTC 2018 par. 6.5.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-azioni-sostegno` | Tipologie e criteri di progetto (§6.5, 6.5.1), azioni e modello geometrico di riferimento (§6.5.2) |
| `inquadra-verifiche-slu-sostegno` | Verifiche SLU/SLE di muri e paratie, approcci progettuali e coefficienti della Tab. 6.5.I (§6.5.3) |

Nucleo: **tipologie** (muri/paratie/strutture miste, §6.5), **criteri** e **modello geometrico** (§6.5.1,
6.5.2), **verifiche SLU dei muri** con stabilità globale in **Approccio 1 (A2+M2+R2)** e rimanenti in
**Approccio 2 (A1+M1+R3)** e **Tab. 6.5.I**, **verifiche SLU delle paratie** con **Approccio 1**,
**verifiche di esercizio** (§6.5.3).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.5** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** spinte, verifiche o coefficienti; **non dimensiona** il muro o la paratia.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 21/1/2019 n. 7**.
- **Non tratta** il caso **sismico** (§7.11.6) né la stabilità dei pendii (§6.8) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista strutturale/geotecnico o la
relazione geotecnica, né la lettura del par. 6.5 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
