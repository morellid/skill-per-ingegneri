# Task - Inquadra le azioni termiche sugli edifici e gli effetti (§3.5.5, 3.5.7)

## Obiettivo

Inquadrare la **componente uniforme ΔTu** per gli edifici e i **coefficienti di dilatazione termica** per la
valutazione degli effetti, secondo le NTC 2018 §3.5.5 e §3.5.7.

## Input richiesti

- tipo di struttura (c.a./c.a.p. o acciaio) e condizione (esposta/protetta);
- se la temperatura costituisce o meno **azione fondamentale** per sicurezza/efficienza funzionale;
- materiale e geometria (per gli effetti di dilatazione).

## Procedura (ancorata al testo)

1. **Azioni termiche sugli edifici** (§3.5.5). Se la temperatura **non** è azione fondamentale, per gli edifici
   si può considerare la **sola componente uniforme ΔTu** dalla **Tab. 3.5.II**:
   - c.a. e c.a.p. **esposte**: **± 15 °C**; **protette**: **± 10 °C**;
   - acciaio **esposte**: **± 25 °C**; **protette**: **± 15 °C**.
   Se la temperatura **è** azione fondamentale, l'andamento di T nelle sezioni va valutato studiando la
   trasmissione del calore.

2. **Strutture con azioni termiche speciali** (§3.5.6). Ciminiere, tubazioni, sili, serbatoi, torri di
   raffreddamento, ecc. vanno progettati per le distribuzioni di temperatura delle specifiche condizioni di
   servizio (fuori scope della skill).

3. **Effetti delle azioni termiche** (§3.5.7). Per valutare gli effetti (dilatazioni, sollecitazioni indotte da
   deformazioni contrastate) usare i **coefficienti di dilatazione termica αT** della **Tab. 3.5.III** (×10⁻⁶/°C):
   alluminio 24, acciaio da carpenteria 12, calcestruzzo strutturale 10, strutture miste 12, calcestruzzo
   alleggerito 7, muratura 6÷10, legno ∥ fibre 5, legno ⊥ fibre 30÷70.

## Output

Una nota che indichi: la **ΔTu** applicabile (Tab. 3.5.II) per il tipo/condizione della struttura, il criterio
"azione fondamentale o meno", e il **coefficiente di dilatazione αT** (Tab. 3.5.III) per il materiale. **La
skill fornisce i valori di riferimento; non calcola le dilatazioni/sollecitazioni né esegue le verifiche.**
