# AGENTS.md - azioni-traffico-ponti-stradali-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale di ponti** per l'**inquadramento della definizione delle
azioni da traffico** (e delle altre azioni) sui **ponti stradali** secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 5.1.3**: corsie convenzionali, Schemi di Carico, intensità dei carichi, categorie
stradali, frenamento e forza centrifuga, altre azioni e combinazioni. Target: ingegneri strutturisti e
progettisti di ponti.

**E' una skill documentale per il tecnico**: fornisce la suddivisione in corsie (Tab. 5.1.I), gli Schemi di
Carico 1-5 e le intensità Qik/qik (Tab. 5.1.II), le formule di frenamento q3 [5.1.4] e centrifuga q4 (Tab.
5.1.III) e i coefficienti delle combinazioni (Tab. 5.1.IV/V/VI); **non calcola** le sollecitazioni, **non
individua** la disposizione più gravosa dei carichi e **non dimensiona** l'impalcato.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Apre il Capitolo 5 (ponti)** delle skill NTC, lato azioni da traffico, e si
affianca alle skill sulle azioni (`carichi-permanenti-sovraccarichi-ntc` §3.1, `carichi-atmosferici-ntc`
§3.3-3.4, `combinazioni-carico-ntc` §2.5.3, `spettro-risposta-ntc` §3.2) e alle "costruzioni di X" (§4.1-4.5)
che forniscono le resistenze dei materiali. Il §5.1.3 rinvia al **Cap. 3** per neve/vento/temperatura e al
**Cap. 2** per le combinazioni. Restano fuori scope i **ponti ferroviari** (§5.2), la **fatica** (§5.1.4) e
la **sismica dei ponti** (§7.9). Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla
G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-5-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 5.1 estratto con `pdftotext -layout` (pp. 150-157) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-5-1.md`; estratto operativo in
`references/estratti/azioni-traffico-ponti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Corsie** (Tab. 5.1.I): w < 5,40 → nl = 1 (3,00 m); 5,4 ≤ w < 6,0 → nl = 2 (w/2); 6,0 ≤ w → nl = Int(w/3)
  (3,00 m). Ingombro 3,00 m; min 2 corsie salvo w < 5,40 m.
- **Schemi di Carico** (§5.1.3.3.3): 1 (tandem + distribuito), 2 (asse singolo), 3 (150 kN), 4 (10 kN), 5
  (folla 5,0 kN/m², combinazione 2,5); 6.a/b/c per luce > 300 m.
- **Intensità** (Tab. 5.1.II): corsia 1 300/9,00; corsia 2 200/2,50; corsia 3 100/2,50; altre 0/2,50.
- **Frenamento q3** [5.1.4]: 180 ≤ 0,6·(2·Q1k) + 0,10·q1k·w1·L ≤ 900 kN.
- **Centrifuga q4** (Tab. 5.1.III): R<200 → 0,2·Qv; 200≤R≤1500 → 40·Qv/R; R≥1500 → 0.
- **Parapetti/urto** (§5.1.3.10): h ≥ 1,10 m, 1,5 kN/m; forze da urto ×1,50; γ unitario per l'urto.
- **Combinazioni** (§5.1.3.14): gruppi Tab. 5.1.IV; γ SLU Tab. 5.1.V (traffico 1,35/1,35/1,15); ψ Tab.
  5.1.VI.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le sollecitazioni né **eseguire** le verifiche; non **individuare** la disposizione più
  gravosa dei carichi mobili; non **dimensionare** l'impalcato, le pile o gli appoggi.
- Non **riprodurre** le **Fig. 5.1.1/5.1.2/5.1.3** (numerazione corsie, geometrie/interassi degli Schemi e
  delle impronte, diffusione dei carichi): rinvio al testo NTC e all'**EC1 (UNI EN 1991-2)**.
- Non **trattare** i **ponti ferroviari** (§5.2), la **fatica** (§5.1.4) né la **sismica dei ponti** (§7.9);
  non **riprodurre** la **Circolare 21/1/2019 n. 7**.

### Cosa fare
- Fornire la suddivisione in corsie, gli Schemi di Carico, le intensità, le formule di frenamento/centrifuga
  e i coefficienti delle combinazioni, sempre con rinvio al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 5.1. Verificare le corsie (Tab. 5.1.I), le intensità (Tab. 5.1.II), le
formule di q3 [5.1.4] e q4 (Tab. 5.1.III) e i coefficienti (Tab. 5.1.V/5.1.VI).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista/progettista di ponti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #394)
- Task files: 2 (`inquadra-corsie-schemi-carico.md`, `inquadra-azioni-derivate-combinazioni.md`)
- Esempi: 2 (corsie convenzionali e Schemi di Carico per w = 10,50 m; azione di frenamento q3 sulla corsia 1)
