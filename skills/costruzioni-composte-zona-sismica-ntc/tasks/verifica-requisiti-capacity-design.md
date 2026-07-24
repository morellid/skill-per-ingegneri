# Task — Verifica i requisiti del capacity design per le strutture dissipative (NTC 2018 §7.6.4)

Supporto documentale per inquadrare i **capisaldi del capacity design** di una struttura composta acciaio-
calcestruzzo dissipativa in zona sismica secondo il par. 7.6.4 delle NTC 2018 (DM 17/1/2018): limite superiore
EU,Rd, capacità dei collegamenti, limite sullo sforzo normale delle colonne e classe delle sezioni. **Non**
sostituisce le verifiche di resistenza/duttilità.

Fonte: `../references/fonti/ntc2018-par-7-6.md`; checklist: `../references/estratti/composte-sismica-checklist.md`.

## Input tipico

- Comportamento **dissipativo** (tipo b) o c)); tipologia strutturale e localizzazione delle zone dissipative.
- Per le zone dissipative: **limite inferiore Epl,Rd** della capacità; per i collegamenti adiacenti la capacità
  del collegamento **Rj,d**; acciaio strutturale (per γov, §7.5.1).
- Per le **colonne primarie** dei telai con zone dissipative: **NEd** e **Npl,Rd**.
- Per i nodi trave-colonna con colonne rivestite in cls: altezze relative di trave e pilastro.

## Passi

1. **Limite superiore della capacità e collegamenti (§7.6.4.2)**
   - La progettazione è basata sul **limite inferiore Epl,Rd** (ESd < Epl,Rd) e sul **limite superiore
     EU,Rd = 1,1·γov·Epl,Rd** (γov definito al §7.5.1), da usare per la capacità delle altre componenti.
   - Per i collegamenti adiacenti alle zone dissipative: **Rj,d ≥ RU,Rd** [7.6.1].
   - Nodi trave-colonna con colonne rivestite di cls, se l'altezza della trave differisce dalla colonna **≤ 40%**:
     capacità a taglio del pannello d'anima **Vwp,Rd = 0,8·(Vwp,s,Rd + Vwp,c,Rd)** [7.6.2].
   - Nel **tipo b)** la capacità degli elementi in acciaio è valutata secondo il **§7.5**.

2. **Duttilità e limite sullo sforzo normale (§7.6.4.3)**
   - Duttilità locale **μ = θu/θy**; capacità al collasso θu alla **riduzione del 15%** della resistenza massima.
   - Per le sezioni delle **colonne primarie** dei telai con zone dissipative: **NEd/Npl,Rd ≤ 0,3** [7.6.3].
   - Rapporti larghezza/spessore di anime e ali: zone in **solo acciaio** → §7.5.6; zone **rivestite in cls** →
     **Tab. 7.6.I**.

3. **Output**: scheda con EU,Rd (in funzione di Epl,Rd e γov), esito Rj,d ≥ RU,Rd (se disponibile), esito del
   limite NEd/Npl,Rd ≤ 0,3 per le colonne dei telai e rinvio alla riga pertinente (§7.5.6 o Tab. 7.6.I) per i
   rapporti larghezza/spessore. Segnala che è un inquadramento, non una verifica di resistenza.

## Cosa NON fare

- Non confondere i **capisaldi** del capacity design con le **verifiche** di dettaglio RES/DUT di membrature e
  collegamenti e con le regole per tipologia (§§ 7.6.4-7.6.8, Tab. 7.6.I-IV): restano fuori scope.
- Non applicare la formula [7.6.2] se l'altezza della trave differisce dalla colonna di oltre il 40%.
- Non inventare valori: ogni limite deve essere rintracciabile in `../references/fonti/ntc2018-par-7-6.md`.
