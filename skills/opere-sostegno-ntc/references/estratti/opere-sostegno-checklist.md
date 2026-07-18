# Estratto operativo - Opere di sostegno: muri e paratie (NTC 2018 §6.5)

> Parafrasi ancorata a `references/fonti/ntc2018-par-6-5.md`. Ogni voce cita il paragrafo NTC.
> La skill inquadra tipologie, azioni, stati limite, approcci e coefficienti; **non** esegue calcoli né
> dimensiona l'opera.

## 1. Tipologie (§6.5)

- **Muri**: sostegno affidato al **peso proprio** del muro e del terreno su di esso (muri a gravità, a
  mensola, a contrafforti);
- **Paratie**: sostegno dato dalla **resistenza del terreno a valle** e da eventuali **ancoraggi/puntoni**;
- **Strutture miste**: sostegno per trattamenti di miglioramento ed elementi di rinforzo/collegamento.

In presenza di **azioni sismiche** si applica anche il **§7.11.6** (non trattato qui).

## 2. Criteri di progetto (§6.5.1)

- Scelta del tipo in base a dimensioni, terreni, pressioni interstiziali, interazione con manufatti,
  stabilità del sito, dispositivi complementari e fasi costruttive.
- **Muri**: riempimento a tergo **costipato** e con granulometria drenante; **drenaggio** efficace nel
  tempo (eventuali geotessili); valutare la **perdita di efficacia** di drenaggi/tiranti/ancoraggi con
  **piano di monitoraggio**.
- **Costruzioni preesistenti**: valutare gli **spostamenti** del terreno a tergo e la compatibilità; se
  variano le **pressioni interstiziali** valutarne gli effetti.
- **Indagini geotecniche** estese alla **stabilità locale e globale** del complesso opera-terreno.

## 3. Azioni e modello geometrico (§6.5.2)

- **Azioni**: peso terreno/riempimento, **sovraccarichi**, acqua, ancoraggi presollecitati, moto ondoso,
  urti, temperatura, ghiaccio (§6.5.2). Sovraccarichi a tergo: costruzioni, depositi, veicoli, apparecchi
  di sollevamento (§6.5.2.1).
- **Modello geometrico** (§6.5.2.2): considerare le variazioni del profilo. Se il sostegno è affidato al
  terreno a valle, **ridurre la quota di valle** del **minore** tra:
  - **10%** dell'altezza di terreno da sostenere (opere a sbalzo);
  - **10%** della differenza di quota tra vincolo inferiore e fondo scavo (opere vincolate);
  - **0,5 m**.
- **Falda**: negli SLU, in assenza di drenaggi, ipotizzare la superficie libera **non inferiore** al
  livello di sommità dei terreni a bassa permeabilità (**k < 10⁻⁶ m/s**).

## 4. Verifiche SLU dei MURI (§6.5.3.1.1)

Verificare [6.2.1] (E_d ≤ R_d) per gli stati limite:
- **GEO**: **scorrimento** sul piano di posa, **carico limite** fondazione-terreno, **ribaltamento**,
  **stabilità globale**;
- **STR**: resistenza degli elementi strutturali.

**Approcci e combinazioni**:
- **stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (come §6.8; Tab. 6.2.I/6.2.II/6.8.I);
- **rimanenti verifiche** → **Approccio 2 (A1+M1+R3)** con **Tab. 6.5.I**; nel **ribaltamento** i R3
  agiscono sugli effetti delle azioni **stabilizzanti**.

**Tab. 6.5.I - coefficienti parziali γR (gruppo R3)**

| Verifica | γR |
|---|---|
| Capacità portante della fondazione | 1,4 |
| Scorrimento | 1,1 |
| Ribaltamento | 1,15 |
| Resistenza del terreno a valle | 1,4 |

- **Spinte**: giustificate su spostamenti relativi o da interazione terreno-struttura; tener conto di
  sovraccarico, inclinazione del piano campagna e del paramento, pressioni interstiziali, filtrazione,
  **attrito parete-terreno** (giustificato).
- **Traslazione (scorrimento)**: in generale **non** considerare la **resistenza passiva** a valle; se
  giustificata, al più il **50%** e con verifica di compatibilità degli spostamenti.

## 5. Verifiche SLU delle PARATIE (§6.5.3.1.2)

- Stati limite **GEO/UPL/HYD** (rotazione rigida, carico limite verticale, sfilamento ancoraggi,
  instabilità/sollevamento/sifonamento del fondo scavo, stabilità globale) e **STR** (ancoraggi, puntoni,
  resistenza della paratia).
- **Stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (Tab. 6.2.I/6.2.II/6.8.I); **UPL/HYD**
  come §6.2.4.2.
- **Rimanenti verifiche** → **Approccio 1**, **Comb. 1 (A1+M1+R1)** e **Comb. 2 (A2+M2+R1)**, con **γR del
  gruppo R1 = 1** (unità). Verificare **ancoraggi/puntoni/controventi**. Per **δ > φ'/2** considerare la
  **non planarità** delle superfici di scorrimento nella resistenza passiva.

## 6. Verifiche di esercizio (SLE) (§6.5.3.2)

Valutare gli **spostamenti** dell'opera e del terreno, compatibili con la funzionalità dell'opera e la
sicurezza dei manufatti adiacenti; per manufatti sensibili, **analisi di interazione** con le fasi
costruttive.

## Cosa la skill NON fa

- **Non calcola** spinte, verifiche o coefficienti; **non dimensiona** muro o paratia.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 7/2019**.
- **Non tratta** il **sismico** (§7.11.6) se non nel richiamo.
- **Non sostituisce** il progettista strutturale/geotecnico né la relazione geotecnica.
