# Estratto operativo - Azioni eccezionali da esplosione (NTC 2018 §3.6.2)

> Parafrasi ancorata a `references/fonti/ntc2018-par-3-6-2.md`. Ogni voce cita il paragrafo/tabella/formula
> NTC. La skill **inquadra** classificazione, modellazione e criteri; **non** calcola le sollecitazioni né
> dimensiona/verifica gli elementi. Gli operatori delle formule sono verificati sull'immagine del PDF.

## 1. Ambito (§3.6.2.1)

- Costruzioni con **miscele esplosive di polveri o gas in aria** o con **materiali esplosivi**.
- **Escluse** le esplosioni che si verificano **all'esterno** della costruzione.

## 2. Classificazione (§3.6.2.2, Tab. 3.6.I)

| Categoria | Effetti |
|---|---|
| **1** | Trascurabili sulle strutture |
| **2** | Localizzati su parte delle strutture |
| **3** | Generalizzati sulle strutture |

## 3. Modellazione (§3.6.2.3)

Le onde di pressione sono ricondotte a **pressioni statiche equivalenti** (se comprovate da modelli teorici
adeguati).

- **Categoria 1**: **nessuna verifica**.
- **Categoria 2** (ambienti con **pannelli di sfogo**): pressione statica equivalente nominale pd [kN/m²] =
  **valore maggiore** fra:

      pd = 3 + pv                          [3.6.5a]
      pd = 3 + pv/2 + 0,04/(Av/V)²         [3.6.5b]

  con **pv** = pressione a cui cedono le aperture di sfogo [kN/m²], **Av** = area aperture [m²], **V** = volume
  ambiente [m³]. Vincolo:

      0,05 m⁻¹ ≤ Av/V ≤ 0,15 m⁻¹           [3.6.6]

  - Espressioni valide per **volume ≤ 1.000 m³**; pressione agente **simultaneamente su tutte le pareti**.
  - **Elementi chiave** e connessioni: **pd = 20 kN/m²** da **ogni direzione** (con la reazione trasmessa dagli
    elementi collegati soggetti alla stessa pressione).
- **Categoria 3**: **studi più approfonditi**.

## 4. Criteri di progettazione (§3.6.2.4)

- Sono **accettabili i danneggiamenti localizzati** (anche gravi), purché non espongano al pericolo l'intera
  struttura o la capacità portante sia mantenuta per il tempo necessario alle misure di emergenza.
- **Misure di protezione**: **superfici collassabili** sotto sovrappressioni prestabilite; **giunti
  strutturali** per separare le porzioni a rischio; **prevenzione di crolli** significativi da cedimenti
  localizzati.

## Cosa la skill NON fa

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non svolge** i **modelli teorici** delle onde di pressione né gli **studi di Categoria 3**; **non** tratta
  le **esplosioni esterne**.
- **Non tratta** l'**incendio** (§3.6.1, skill `resistenza-fuoco-strutture-ntc`) né gli **urti** (§3.6.3, skill
  `azioni-urto-eccezionali-ntc`).
- **Non sostituisce** il progettista strutturale né la lettura del §3.6.2 delle NTC 2018 e della Circolare
  applicativa.
