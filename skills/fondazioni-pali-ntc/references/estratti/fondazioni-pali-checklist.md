# Estratto operativo - Fondazioni su pali (NTC 2018 §6.4.3)

> Parafrasi ancorata a `references/fonti/ntc2018-par-6-4-3.md`. Ogni voce cita il paragrafo NTC.
> La skill inquadra stati limite, approcci, coefficienti e fattori di correlazione; **non** esegue calcoli
> né dimensiona i pali.

## 1. Impostazione del progetto (§6.4.3)

- Scelta del tipo di palo, tecnologie e modalità di esecuzione, dimensionamento dei pali e delle strutture
  di collegamento, con **effetti di gruppo** in SLU e SLE.
- Indagini geotecniche (§6.2.2) estese all'idoneità del tipo di palo. Verifiche preferibilmente da
  **analisi di interazione** terreno-fondazione (fondazione mista a platea su pali).
- Se l'interazione è **non significativa/omessa** → verifiche sui **soli pali** (§6.4.3.1, §6.4.3.2); se
  **significativa** → verifiche sulla **fondazione mista** (§6.4.3.3, §6.4.3.4).
- Tra le **azioni permanenti**: peso proprio del palo e **attrito negativo** (coefficienti γM del caso
  **M1**, Tab. 6.2.II). Sisma: §7.11.5.3.2 (non trattato qui).

## 2. Verifiche SLU (§6.4.3.1)

Accertare [6.2.1] (**E_d ≤ R_d**) per:
- **GEO**: carico limite della palificata per **carichi assiali**; per **carichi trasversali**; carico
  limite di **sfilamento** (trazione); **stabilità globale**;
- **STR**: resistenza dei **pali** e della **struttura di collegamento**.

**Approcci e combinazioni**:
- **stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (Tab. 6.2.I/6.2.II/6.8.I);
- **rimanenti verifiche** → **Approccio 2 (A1+M1+R3)** con Tab. 6.2.I/6.2.II/**6.4.II**/**6.4.VI**. Nelle
  verifiche **STR** il coefficiente γR **non** si porta in conto.

## 3. Resistenze a carico assiale e coefficienti (§6.4.3.1.1)

**R_d = R_k / γR** con γR della **Tab. 6.4.II (gruppo R3)**:

| Resistenza | Simbolo | Infissi | Trivellati | Elica continua |
|---|---|---|---|---|
| Base | γb | 1,15 | 1,35 | 1,3 |
| Laterale in compressione | γs | 1,15 | 1,15 | 1,15 |
| Totale | γt | 1,15 | 1,30 | 1,25 |
| Laterale in trazione | γst | 1,25 | 1,25 | 1,25 |

**R_k** dal minore tra media e minimo delle resistenze, tramite i **fattori di correlazione ξ**:
- **prove di carico statico** su pali pilota → **Tab. 6.4.III** (ξ1/ξ2, per numero di prove: 1,40→1,0);
- **metodi analitici / prove in sito** → **Tab. 6.4.IV** (ξ3/ξ4, per numero di **verticali indagate**:
  1,70→1,40/1,21);
- **prove dinamiche** su pali pilota → **Tab. 6.4.V** (ξ5/ξ6).

**Palificata** (§6.4.3.1.1.1): R_k = somma delle R_k dei pali, con possibili **riduzioni per effetto di
gruppo** (tipologia, terreni, geometria).

## 4. Carichi trasversali (§6.4.3.1.2)

Come §6.4.3.1.1 ma con il coefficiente **γT = 1,3** (**Tab. 6.4.VI**, R3). Considerare i vincoli alla
testa dei pali (struttura di collegamento) e l'effetto di gruppo.

## 5. Verifiche SLE (§6.4.3.2)

Stati limite (quando pertinenti): eccessivi **cedimenti/sollevamenti** ed **eccessivi spostamenti
trasversali**. Spostamenti e distorsioni nelle **combinazioni caratteristiche** (§2.5.3), compatibili con
i requisiti prestazionali della struttura in elevazione [6.2.7].

## 6. Fondazioni miste a platea su pali (§6.4.3.3-6.4.3.4)

- **SLU**: GEO (carico limite assiale/trasversale, stabilità globale) e STR; stabilità globale in
  **Approccio 1 Comb. 2 (A2+M2+R2)**.
- Se la [6.2.1] è garantita dalla **sola platea** (§6.4.2.1) → ai pali la sola funzione di **riduzione
  degli spostamenti** (con verifiche SLU STR e SLE).
- Contributo dei pali alle azioni verticali: R_d = somma R_k pali (§6.4.3.1) + platea, diviso il γR (R3)
  di capacità portante della **Tab. 6.4.I** (§6.4.2.1).
- **SLE**: interazione terreno-fondazione compatibile con i requisiti prestazionali [6.2.7].

## 7. Aspetti costruttivi, integrità, prove di carico (§6.4.3.5-6.4.3.7)

- **Aspetti costruttivi** (§6.4.3.5): distanza, sequenza, refluimento/sifonamento (trivellati),
  addensamento (infissi), falda e aggressione chimica, durabilità.
- **Controlli d'integrità** (§6.4.3.6): almeno il **5% dei pali**, **minimo 2**; per gruppi di **grande
  diametro (d ≥ 80 cm)** con **≤ 4 pali**, **tutti** i pali del gruppo.
- **Prove di carico** (§6.4.3.7): **di progetto** su **pali pilota**, carico **≥ 2,5× l'azione SLE**,
  resistenza al cedimento del **10% del diametro** (d < 80 cm) o **≥ 5%** (d ≥ 80 cm); **in corso d'opera**
  a **1,5×** (o **1,2×** se strumentati) l'azione SLE, con numero minimo di prove per numero di pali (1 se
  ≤20; 2 se 21-50; 3 se 51-100; 4 se 101-200; 5 se 201-500; ~5+n/500 se n>500) e **almeno una prova
  statica**.

## Cosa la skill NON fa

- **Non calcola** resistenze, verifiche o coefficienti; **non dimensiona** pali o palificata.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 7/2019**.
- **Non tratta** il **sismico** (§7.11.5.3.2) se non nel richiamo.
- **Non sostituisce** il progettista strutturale/geotecnico né la relazione geotecnica.
