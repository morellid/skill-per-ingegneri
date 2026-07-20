# azioni-traffico-ponti-stradali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista/progettista di ponti da completare)

Skill di **supporto documentale** al **progettista strutturale di ponti** per l'**inquadramento della
definizione delle azioni da traffico** (e delle altre azioni) sui **ponti stradali** secondo le **NTC 2018**
(D.M. 17 gennaio 2018), **paragrafo 5.1.3**: corsie convenzionali, Schemi di Carico, intensità dei carichi,
categorie stradali, frenamento e forza centrifuga, altre azioni e combinazioni.

**Non calcola** le sollecitazioni né **esegue** le verifiche, **non individua** la disposizione più gravosa
dei carichi mobili, **non dimensiona** l'impalcato e **non sostituisce** il progettista: fornisce la
suddivisione in corsie (Tab. 5.1.I), gli Schemi di Carico 1-5, le intensità Qik/qik (Tab. 5.1.II), le formule
di frenamento q3 [5.1.4] e centrifuga q4 (Tab. 5.1.III) e i coefficienti delle combinazioni.

## Target

Ingegneri strutturisti e progettisti di ponti che devono inquadrare le azioni da traffico per il progetto di
un ponte stradale secondo le NTC 2018 par. 5.1.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-corsie-schemi-carico` | Corsie convenzionali (Tab. 5.1.I), Schemi di Carico 1-5, categorie stradali e intensità Qik/qik (Tab. 5.1.II) (§5.1.3.3) |
| `inquadra-azioni-derivate-combinazioni` | Frenamento q3 [5.1.4], centrifuga q4 (Tab. 5.1.III), altre azioni e coefficienti delle combinazioni (Tab. 5.1.IV/V/VI) (§5.1.3.4-5.1.3.14) |

Nucleo: **corsie convenzionali** (nl = 1/2/Int(w/3)), **Schemi di Carico** (1-5, folla 5,0/2,5 kN/m²),
**intensità Qik/qik** (corsia 1: 300 kN/9,00 kN/m²), **frenamento** (180-900 kN) e **centrifuga**, con i
**gruppi di azioni** e i **coefficienti** per le combinazioni (§5.1.3).

## Relazione con altre skill

- **Apre** il **Capitolo 5 (ponti)** delle skill NTC; si affianca alle skill sulle azioni
  (`carichi-permanenti-sovraccarichi-ntc` §3.1, `carichi-atmosferici-ntc` §3.3-3.4, `combinazioni-carico-ntc`
  §2.5.3) e alle "costruzioni di X" (§4.1-4.5). Il §5.1.3 rinvia al Cap. 3 per neve/vento/temperatura e al
  Cap. 2 per le combinazioni.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 5.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** le sollecitazioni né **esegue** le verifiche; **non individua** la disposizione più gravosa
  dei carichi mobili; **non dimensiona** l'impalcato, le pile o gli appoggi.
- **Non riproduce** le **Fig. 5.1.1/5.1.2/5.1.3** (numerazione corsie, geometrie degli Schemi e delle
  impronte, diffusione dei carichi → norma/EC1) né la geometria di dettaglio dei carichi.
- **Non tratta** i **ponti ferroviari** (§5.2), la **fatica** (§5.1.4) né la **progettazione sismica dei
  ponti** (§7.9); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 5.1 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
