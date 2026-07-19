---
name: costruzioni-legno-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione delle costruzioni di legno (caso non sismico) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 4.4. Aiuta a inquadrare l'assegnazione delle classi di durata del carico (Tab. 4.4.I: permanente, lunga, media, breve, istantaneo) e delle classi di servizio (Tab. 4.4.II, in funzione di temperatura e umidita' relativa); il calcolo delle resistenze di progetto con la relazione Xd uguale a kmod per Xk diviso il coefficiente parziale gamma_M, dove kmod (Tab. 4.4.IV) dipende dal materiale, dalla classe di servizio e dalla classe di durata (e nelle combinazioni si assume il valore dell'azione di minor durata) e gamma_M (Tab. 4.4.III) vale ad esempio 1,50 per il legno massiccio, 1,45 per il lamellare incollato, 1,40 per LVL e OSB, 1,50 per le unioni, con la colonna B ridotta per le produzioni continuative controllate e 1,00 per le combinazioni eccezionali; le verifiche agli stati limite di esercizio con la deformabilita' a lungo termine tramite il fattore uno su uno piu' kdef (Tab. 4.4.V) e le frecce limite (istantanea inferiore a L su 300, finale inferiore a L su 200); le verifiche agli stati limite ultimi di resistenza (trazione e compressione parallela e perpendicolare alla fibratura, flessione con km uguale a 0,7 per le sezioni rettangolari e 1,0 per le altre, tenso e pressoflessione, taglio, torsione con ksh) e di stabilita' (kcrit per lo svergolamento delle travi inflesse e per l'instabilita' delle colonne compresse, con il coefficiente di imperfezione beta_c uguale a 0,2 per il legno massiccio e 0,1 per il lamellare); i collegamenti, la robustezza, la resistenza al fuoco e le regole per l'esecuzione. Use when a structural designer must frame the design of timber structures (non-seismic) under the Italian NTC 2018 par. 4.4; it is a documentary aid and does NOT compute the strengths or the verifications, does NOT size the members or the connections, does NOT reproduce the material properties fk and elastic moduli of par. 11.7 nor the Eurocodes (EN 1995), does NOT cover the seismic design (par. 7.7), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni di legno: classi, resistenze e verifiche (NTC 2018 par. 4.4)"
summary: "Inquadra la progettazione delle costruzioni di legno (NTC 2018 par. 4.4): classi di durata (Tab. 4.4.I) e di servizio (Tab. 4.4.II), resistenze di progetto Xd=kmod*Xk/gamma_M (Tab. 4.4.III/IV), SLE con kdef e frecce (L/300, L/200), verifiche SLU di resistenza e stabilita'."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 4.4 Costruzioni di legno: classi di durata (Tab. 4.4.I) e di servizio (Tab. 4.4.II), Xd=kmod*Xk/gamma_M (Tab. 4.4.III/IV), kdef, verifiche SLU/SLE e stabilita'"
  - "Rinvio (non riprodotti): par. 11.7 (materiali, fk, moduli, kh), par. 7.7 (sismica), UNI EN 1995 (Eurocodice 5) e UNI EN di prodotto; Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - costruzioni-di-legno
  - legno-strutturale
  - ntc-2018
  - kmod-kdef
  - coefficienti-parziali
---

# Costruzioni di legno: classi, resistenze di progetto e verifiche (NTC 2018 par. 4.4)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la **progettazione delle costruzioni di
legno** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.4**:

- **classi di durata del carico** (Tab. 4.4.I) e **classi di servizio** (Tab. 4.4.II) (§4.4.4-4.4.5);
- **resistenze di progetto** `Xd = kmod·Xk/γM` con **kmod** (Tab. 4.4.IV) e **γM** (Tab. 4.4.III) (§4.4.6);
- **verifiche SLE** con **kdef** (Tab. 4.4.V) e le **frecce** limite (§4.4.7);
- **verifiche SLU** di **resistenza** (km) e di **stabilità** (kcrit, βc) (§4.4.8).

**Non è** uno strumento che calcola resistenze o esegue verifiche, né dimensiona elementi e collegamenti: è
un **supporto documentale** che inquadra classi, coefficienti, resistenze di progetto e criteri di verifica.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-resistenze-progetto-legno` | Classi di durata (Tab. 4.4.I) e di servizio (Tab. 4.4.II), kmod (Tab. 4.4.IV) e γM (Tab. 4.4.III), resistenze di progetto Xd=kmod·Xk/γM (§4.4.4-4.4.6) |
| `inquadra-verifiche-slu-sle-legno` | Verifiche SLU di resistenza (km) e stabilità (kcrit, βc) e verifiche SLE (kdef, frecce L/300 e L/200) (§4.4.7, 4.4.8) |

## Punti chiave (verificati sul testo)

- **Classi di durata** (§4.4.4, Tab. 4.4.I): permanente (>10 anni), lunga (6 mesi-10 anni), media (1
  settimana-6 mesi), breve (<1 settimana), istantaneo.
- **Classi di servizio** (§4.4.5, Tab. 4.4.II): **1** (UR ≤ 65%), **2** (UR > 85% poche settimane/anno),
  **3** (umidità superiore).
- **Resistenza di progetto** (§4.4.6): **Xd = kmod·Xk/γM** [4.4.1]; **kmod** di combinazione = azione di
  **minor durata**; **γM** colonna A (massiccio 1,50, lamellare 1,45, LVL/OSB 1,40, unioni 1,50) o colonna
  B ridotta; **eccezionali γM = 1,00**.
- **SLE** (§4.4.7): deformazione a lungo termine con fattore **1/(1+kdef)** (Tab. 4.4.V); frecce
  **istantanea < L/300**, **finale < L/200**.
- **SLU resistenza** (§4.4.8.1): flessione con **km = 0,7** (rettangolari) / **1,0** (altre); trazione,
  compressione, taglio, torsione (ksh).
- **SLU stabilità** (§4.4.8.2): **kcrit,m = 1 se λrel,m ≤ 0,75**; **kcrit,c = 1 se λrel,c ≤ 0,3**;
  imperfezione **βc = 0,2** (massiccio) / **0,1** (lamellare); moduli al frattile 5%.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.4** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** elementi e collegamenti.
- **Non riproduce** le proprietà dei materiali (fk, moduli elastici, kh) del **§11.7** né gli **Eurocodici**
  (UNI EN 1995).
- **Non tratta** la **progettazione sismica** (§7.7); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.4 delle NTC 2018 e della Circolare applicativa.**
