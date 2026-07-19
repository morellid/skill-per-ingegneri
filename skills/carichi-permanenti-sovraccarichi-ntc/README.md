# carichi-permanenti-sovraccarichi-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**analisi dei carichi** - **carichi
permanenti** (pesi propri strutturali e non strutturali) e **sovraccarichi variabili** (carichi imposti)
per **categoria d'uso** delle costruzioni civili e industriali - secondo le **NTC 2018** (D.M. 17 gennaio
2018), **paragrafo 3.1**.

**Non calcola** i carichi di progetto né **combina** le azioni, **non dimensiona** gli elementi e **non
sostituisce** il progettista: fornisce i valori tabellari (Tab. 3.1.I e 3.1.II), il carico equivalente dei
divisori e i coefficienti di riduzione.

## Target

Ingegneri strutturisti e progettisti che devono impostare l'analisi dei carichi permanenti e dei
sovraccarichi variabili secondo le NTC 2018 par. 3.1.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-sovraccarichi-categoria` | Sovraccarichi qk/Qk/Hk per categoria d'uso (Tab. 3.1.II) e verifiche locali (§3.1.4) |
| `inquadra-permanenti-riduzioni` | Pesi propri (Tab. 3.1.I), carico equivalente g2 dei divisori e riduzioni α_A/α_n (§3.1.2, 3.1.3, 3.1.4.1) |

Nucleo: **pesi propri** (Tab. 3.1.I), **carico equivalente g2** dei divisori, **sovraccarichi** qk/Qk/Hk
per categoria d'uso (Tab. 3.1.II), **riduzioni** per area di influenza e numero di piani, **carichi
concentrati e orizzontali** nelle verifiche locali (§3.1).

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** i carichi di progetto né **combina** le azioni (skill `combinazioni-carico-ntc`);
  **non dimensiona** gli elementi.
- **Non tratta** i **carichi da ponte** (cap. 5), l'**azione sismica** (§3.2) né il **vento/neve**
  (§3.3/3.4, skill `carichi-atmosferici-ntc`).
- **Non riproduce** la **Tab. 2.5.I** (coefficienti ψ) né la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
3.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
