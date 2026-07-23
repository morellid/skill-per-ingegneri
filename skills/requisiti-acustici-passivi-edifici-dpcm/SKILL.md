---
name: requisiti-acustici-passivi-edifici-dpcm
description: "Supporto documentale al progettista edile o al tecnico per l'inquadramento dei requisiti acustici passivi degli edifici secondo il DPCM 5 dicembre 1997 (Determinazione dei requisiti acustici passivi degli edifici, in attuazione della legge quadro sull'inquinamento acustico 447/1995). Aiuta a classificare l'ambiente abitativo nelle categorie della Tabella A (A residenza, B uffici, C alberghi e pensioni, D ospedali cliniche e case di cura, E attivita' scolastiche, F attivita' ricreative o di culto, G attivita' commerciali); a individuare le grandezze e gli indici di valutazione (potere fonoisolante apparente di partizioni R'w, isolamento acustico standardizzato di facciata D2m,nT,w con D2m,nT uguale a D2m piu' dieci volte il logaritmo del rapporto tra il tempo di riverberazione e quello di riferimento pari a 0,5 secondi, livello di rumore di calpestio normalizzato L'n,w, livello massimo LASmax e livello continuo equivalente LAeq, calcolati secondo le norme UNI e ISO citate); e ad applicare i valori limite della Tabella B per ciascuna categoria (categoria D con R'w almeno 55, D2m,nT,w almeno 45, L'n,w non oltre 58, LASmax non oltre 35, LAeq non oltre 25; categorie A e C con 50, 40, 63, 35, 35; categoria E con 50, 48, 58, 35, 25; categorie B, F, G con 50, 42, 55, 35, 35), tenendo conto che gli indici di isolamento R'w e D2m,nT,w sono valori minimi mentre i livelli di rumore L'n,w, LASmax e LAeq sono valori massimi, e dei limiti del rumore degli impianti tecnologici (35 dB(A) LASmax per i servizi a funzionamento discontinuo e 25 dB(A) LAeq per quelli a funzionamento continuo). Use when a building designer or technician must classify the dwelling category and apply the passive acoustic requirement limits of the Italian DPCM 5 December 1997; it is a documentary aid and does NOT run acoustic measurements or calculations, does NOT perform the on-site acoustic testing, does NOT reproduce the cited UNI/ISO standards, and does NOT replace the competent acoustics technician (L. 447/1995)."
license: MIT
area: edilizia-urbanistica-catasto
title: "Requisiti acustici passivi degli edifici (DPCM 5 dicembre 1997)"
summary: "Inquadra i requisiti acustici passivi degli edifici (DPCM 5/12/1997): categorie di ambiente (Tab. A, A-G), grandezze e indici (R'w, D2m,nT,w, L'n,w, LASmax, LAeq) e valori limite per categoria (Tab. B), piu' i limiti del rumore degli impianti tecnologici (35 dB(A)/25 dB(A))."
normative_refs:
  - "DPCM 5 dicembre 1997 (G.U. n. 297 del 22/12/1997) - art. 1-2: requisiti acustici passivi degli edifici e componenti in opera; categorie di ambiente Tab. A (A-G); attuazione L. 447/1995"
  - "DPCM 5/12/1997 - Allegato A: grandezze e indici R'w, D2m,nT,w (D2m,nT = D2m + 10 log(T/T0), T0=0,5 s), L'n,w, LASmax, LAeq; impianti 35 dB(A) LASmax (discontinuo) / 25 dB(A) LAeq (continuo)"
  - "DPCM 5/12/1997 - Tab. B valori limite per categoria: D 55/45/58/35/25; A,C 50/40/63/35/35; E 50/48/58/35/25; B,F,G 50/42/55/35/35 (R'w e D2m,nT,w minimi; L'n,w/LASmax/LAeq massimi)"
version: 0.1.0-alpha
status: alpha
tags:
  - acustica-edilizia
  - requisiti-acustici-passivi
  - isolamento-acustico
  - dpcm-5-12-1997
  - collaudo-acustico
---

# Requisiti acustici passivi degli edifici (DPCM 5 dicembre 1997)

## Quando usare questa skill

Usala quando un **progettista edile o un tecnico** deve **inquadrare i requisiti acustici passivi** di un edificio
— classificare l'ambiente abitativo e applicare i valori limite di isolamento e di rumore — secondo il **DPCM 5
dicembre 1997** (in attuazione della legge quadro sull'inquinamento acustico, L. 447/1995):

- **classificazione** dell'ambiente in categorie (Tab. A);
- **grandezze e indici** di valutazione (Allegato A);
- **valori limite** per categoria (Tab. B) e **rumore degli impianti**.

**Non è** uno strumento che esegue misure o calcoli acustici né il collaudo in opera: è un **supporto documentale**
che inquadra categorie, indici e limiti. La valutazione e il collaudo competono al **tecnico competente in
acustica** (L. 447/1995). Complementa le skill su rumore ambientale (`valutazione-impatto-clima-acustico-l-447`,
`mappatura-acustica-strategica-dlgs194`) e sul rumore negli ambienti di lavoro (`valutazione-rischio-rumore-dlgs81`),
che trattano ambiti diversi.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-ambiente-e-valori-limite` | Categoria dell'ambiente (Tab. A) e valori limite dei requisiti acustici passivi per quella categoria (Tab. B: R'w, D2m,nT,w, L'n,w, LASmax, LAeq) |
| `inquadra-grandezze-e-rumore-impianti` | Grandezze e indici (R'w, D2m,nT,w, L'n,w, LASmax, LAeq; D2m,nT = D2m + 10 log(T/T0)) e limiti del rumore degli impianti tecnologici (35/25 dB(A)) |

## Punti chiave (verificati sul testo)

- **Categorie di ambiente** (Tab. A): **A** residenza; **B** uffici; **C** alberghi/pensioni; **D**
  ospedali/cliniche/case di cura; **E** scolastiche; **F** ricreative/culto; **G** commerciali.
- **Grandezze/indici** (Allegato A): **R'w** (potere fonoisolante apparente di partizioni), **D2m,nT,w**
  (isolamento di facciata, con **D2m,nT = D2m + 10 log(T/T0)** e **T0 = 0,5 s**), **L'n,w** (calpestio),
  **LASmax** e **LAeq** (rumore impianti); indici calcolati secondo UNI 8270:1987 Parte 7 e le norme EN ISO/ISO
  citate.
- **Valori limite** (Tab. B) — R'w / D2m,nT,w / L'n,w / LASmax / LAeq: **D** 55/45/58/35/25; **A,C** 50/40/63/35/35;
  **E** 50/48/58/35/25; **B,F,G** 50/42/55/35/35. **R'w** e **D2m,nT,w** sono valori **minimi** (in opera ≥
  limite); **L'n,w**, **LASmax**, **LAeq** sono valori **massimi** (in opera ≤ limite). R'w è riferito a elementi
  di separazione tra **due distinte unità immobiliari**.
- **Rumore impianti tecnologici** (Allegato A): **35 dB(A) LASmax** (servizi a funzionamento **discontinuo**);
  **25 dB(A) LAeq** (servizi a funzionamento **continuo**); misure nell'ambiente più rumoroso, diverso da quello
  di origine.

## Fonti

- **DPCM 5 dicembre 1997** - "Determinazione dei requisiti acustici passivi degli edifici" - G.U. Serie Generale
  n. 297 del 22 dicembre 1997 (PDF Gazzetta Ufficiale, SHA256 `5a8ae1f4...`, riproducibile via doppio download). Il
  PDF è una scansione GURITEL (immagine): contenuto letto renderizzando le pagine in immagine (`pdftoppm`) e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** misure, calcoli degli indici o il **collaudo** acustico in opera.
- **Non riproduce** le **norme UNI/ISO** citate (UNI 8270:1987 Parte 7, EN ISO 140-5/-6, ISO 3382).
- **Non tratta** il tempo di riverberazione degli **edifici scolastici** (circolare MLLPP 3150/1967) nel dettaglio,
  né la classificazione acustica delle unità immobiliari (UNI 11367).
- **Non sostituisce** il **tecnico competente in acustica** (L. 447/1995).

**La skill è un supporto documentale: non sostituisce il tecnico competente in acustica né il progettista, né la lettura diretta del DPCM 5 dicembre 1997 e delle norme tecniche applicabili.**
