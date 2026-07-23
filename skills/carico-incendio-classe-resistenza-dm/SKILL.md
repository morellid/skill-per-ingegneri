---
name: carico-incendio-classe-resistenza-dm
description: "Supporto documentale al progettista antincendio/strutturale per determinare il carico d'incendio specifico di progetto e la classe di resistenza al fuoco richiesta agli elementi costruttivi secondo il DM 9 marzo 2007 (Prestazioni di resistenza al fuoco delle costruzioni nelle attivita' soggette al controllo del CNVVF). Aiuta a inquadrare: il carico d'incendio specifico qf uguale a q diviso A, con q uguale alla somma di gi per Hi per mi per psi-i, dove Hi e' il potere calorifico inferiore secondo UNI EN ISO 1716, mi vale 0,80 per legno e materiali cellulosici e 1,00 per gli altri, e psi-i vale 0 per contenitori progettati per resistere al fuoco, 0,85 per contenitori non combustibili non progettati e 1 negli altri casi; il carico d'incendio specifico di progetto qf,d uguale a delta-q1 per delta-q2 per delta-n per qf, con delta-q1 in funzione della superficie del compartimento (Tabella 1, da 1,00 a 2,00), delta-q2 in funzione della classe di rischio dell'attivita' (Tabella 2, 0,80/1,00/1,20 per rischio basso/moderato/alto) e delta-n prodotto dei fattori delle misure di protezione presenti (Tabella 3); i livelli di prestazione da I a V; le classi di resistenza al fuoco 15, 20, 30, 45, 60, 90, 120, 180, 240 e 360 minuti; la classe richiesta per il livello II (30 o 60) e per il livello III in funzione di qf,d (Tabella 4); le curve nominali di incendio (standard theta-g uguale a 20 piu' 345 log10 di 8t piu' 1, idrocarburi ed esterna) e la Tabella 5 per l'approccio con curve naturali. Use when a fire-safety or structural designer must compute the design specific fire load and the required fire resistance class under the Italian DM 9 March 2007; it is a documentary aid, does NOT run the performance-based design with natural fire curves nor the thermal/mechanical analyses, does NOT reproduce the vertical fire-brigade technical rules nor the Eurocodes part 1-2 material properties, and does NOT replace the fire-safety professional. It complements the NTC 2018 par. 3.6.1 skill, which frames the fire resistance of structures but defers the fire-load calculation to this DM."
license: MIT
area: strutture-geotecnica
title: "Carico d'incendio e classe di resistenza al fuoco (DM 9 marzo 2007)"
summary: "Determina il carico d'incendio specifico di progetto qf,d=dq1*dq2*dn*qf (Tab.1/2/3) e la classe di resistenza al fuoco richiesta secondo il DM 9 marzo 2007: livelli di prestazione I-V, classe 30/60 (liv. II), Tab. 4 (liv. III) e Tab. 5 (curve naturali), classi 15-360 min."
normative_refs:
  - "DM 9 marzo 2007 (Prestazioni di resistenza al fuoco, CNVVF) - qf=somma(gi*Hi*mi*psi)/A; qf,d=dq1*dq2*dn*qf (Tab.1/2/3); livelli I-V; Tab.4 (liv.III) e Tab.5 (curve naturali); classi 15-360 min"
  - "Rinvio (fuori scope): NTC 2018 par. 3.6.1 (skill resistenza-fuoco-strutture-ntc), DM 14/9/2005 (livelli IV-V), regole tecniche verticali VVF, Eurocodici parte 1-2, UNI EN ISO 1716"
version: 0.1.0-alpha
status: alpha
tags:
  - carico-incendio
  - resistenza-al-fuoco
  - dm-9-marzo-2007
  - classi-rei
  - prevenzione-incendi
---

# Carico d'incendio e classe di resistenza al fuoco (DM 9 marzo 2007)

## Quando usare questa skill

Usala quando un **progettista antincendio o strutturale** deve **determinare il carico d'incendio
specifico di progetto q_f,d** di un compartimento e la conseguente **classe di resistenza al fuoco**
richiesta agli elementi costruttivi, secondo il **DM 9 marzo 2007** ("Prestazioni di resistenza al fuoco
delle costruzioni nelle attività soggette al controllo del CNVVF"):

- **carico d'incendio specifico** q_f (punto 1);
- **carico d'incendio specifico di progetto** q_f,d = δ_q1·δ_q2·δ_n·q_f (punto 2, Tabelle 1-3);
- **livelli di prestazione** I-V e **classi** richieste (punto 3, Tabella 4);
- **curve nominali** e **Tabella 5** (approccio con curve naturali) (punto 4).

È il **calcolo di dettaglio** che le NTC 2018 §3.6.1 richiamano ma **rinviano** a questo DM. È un
**supporto documentale**: inquadra formula, coefficienti tabellari e classi; **non** esegue il progetto
prestazionale con curve naturali né le analisi termiche/meccaniche. È **complementare** alla skill
`resistenza-fuoco-strutture-ntc` (framework NTC) e **distinta** dalle skill di procedimento amministrativo
antincendio (`prevenzione-incendi-attivita-procedimenti-dpr151`).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `calcola-carico-incendio-specifico-progetto` | Carico d'incendio specifico q_f (m_i, ψ_i) e di progetto q_f,d = δ_q1·δ_q2·δ_n·q_f con le Tabelle 1, 2 e 3 (punti 1-2) |
| `determina-livello-classe-resistenza` | Livelli di prestazione I-V, classe per il livello II (30/60) e per il livello III (Tabella 4), curve nominali e Tabella 5 (punti 3-4) |

## Punti chiave (verificati sul testo/immagine)

- **Carico d'incendio specifico** (punto 1): **q = Σ g_i·H_i·m_i·ψ_i** [MJ]; **q_f = q/A** [MJ/m²]; H_i
  potere calorifico inferiore (**UNI EN ISO 1716:2002**); **m_i = 0,80** legno/cellulosici, **1,00** altri;
  **ψ_i = 0 / 0,85 / 1** (contenitori progettati / non combustibili non progettati / altri casi).
- **Carico d'incendio di progetto** (punto 2): **q_f,d = δ_q1·δ_q2·δ_n·q_f**; **δ_q1** per superficie
  (Tab. 1: 1,00→2,00); **δ_q2** per classe di rischio (Tab. 2: **0,80/1,00/1,20**); **δ_n = Π δ_ni**
  (Tab. 3: es. estinzione ad acqua 0,60, rivelazione 0,85, accessibilità VVF 0,90).
- **Livelli di prestazione** (punto 3): I (non ammesso), II evacuazione, III gestione emergenza, IV
  limitato danneggiamento, V totale funzionalità. **Classi**: 15, 20, 30, 45, 60, 90, 120, 180, 240, 360.
- **Livello II**: **classe 30** (1 piano f.t. senza interrati) / **classe 60** (≤2 piani f.t. + 1 interrato),
  alle condizioni previste (esodo, no danni ad altre costruzioni, affollamento ≤100 e densità ≤0,2 pers/m²…).
- **Livello III — Tabella 4** (q_f,d → classe): ≤100→0, ≤200→15, ≤300→20, ≤450→30, ≤600→45, ≤900→60,
  ≤1200→90, ≤1800→120, ≤2400→180, >2400→240.
- **Curve nominali** (punto 4): **standard θ_g = 20 + 345·log10(8t+1)**; idrocarburi; esterna. **Tabella 5**
  (curve naturali, q_f,d → classe): ≤300→0, ≤450→15, ≤600→20, ≤900→30, ≤1200→45, ≤1800→60, ≤2400→90, >2400→120.

## Fonti

- **DM 9 marzo 2007** — **G.U. Serie Generale n. 74 del 29/3/2007 — Suppl. Ord. n. 87** (PDF Gazzetta
  Ufficiale, SHA256 `c7003438...`). Scansione **GURITEL**: contenuto letto renderizzando le pagine in
  immagine (`pdftoppm`) e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** il progetto prestazionale con **curve naturali/modelli d'incendio** né le **analisi
  termiche/meccaniche** degli elementi (verifica R in combinazione eccezionale).
- **Non fornisce** le proprietà dei materiali ad alta temperatura (**Eurocodici parte 1-2**) né i valori
  di H_i (**UNI EN ISO 1716**); **non** riproduce le **regole tecniche verticali** VVF né il DM 14/9/2005
  (livelli IV-V).
- **Non tratta** i procedimenti amministrativi di prevenzione incendi (→ skill
  `prevenzione-incendi-attivita-procedimenti-dpr151`) né il framework NTC (→ skill
  `resistenza-fuoco-strutture-ntc`).

**La skill è un supporto documentale: non sostituisce il professionista antincendio né il progettista strutturale, né la lettura del DM 9 marzo 2007 e delle regole tecniche di prevenzione incendi applicabili.**
