# Output atteso - Palificata di pali trivellati sotto un plinto

## Impostazione (§6.4.3)

Poiché si verifica con riferimento ai **soli pali** (interazione con la struttura di collegamento non
considerata), valgono i §§6.4.3.1 (SLU) e 6.4.3.2 (SLE). Tra le **azioni permanenti** vanno inclusi il
**peso proprio del palo** e l'eventuale **attrito negativo** (coefficienti γM del caso **M1**, Tab.
6.2.II). Il caso **sismico** (§7.11.5.3.2) non è trattato da questa skill.

## Quali stati limite (§6.4.3.1)

Accertare [6.2.1] (**E_d ≤ R_d**) per:
- **SLU GEO**: carico limite della palificata per **carichi assiali**; per **carichi trasversali**;
  **sfilamento** (carichi assiali di trazione); **stabilità globale**;
- **SLU STR**: resistenza dei **pali** e della **struttura di collegamento** (plinto).

## Con quale approccio e quali coefficienti

- **Stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (coefficienti dalle Tab. 6.2.I/6.2.II
  e Tab. 6.8.I - non riprodotte qui).
- **Rimanenti verifiche** → **Approccio 2 (A1+M1+R3)**, con i coefficienti delle **Tab. 6.4.II** (carichi
  assiali) e **6.4.VI** (trasversali). Nelle verifiche **STR** il coefficiente γR **non** si porta in
  conto.

**Tab. 6.4.II (γR, R3) - pali trivellati** (la colonna pertinente):

| Resistenza | γR (trivellati) |
|---|---|
| Base | 1,35 |
| Laterale in compressione | 1,15 |
| Totale | 1,30 |
| Laterale in trazione | 1,25 |

Il valore di progetto è **R_d = R_k / γR**, dove **R_k** si determina con i **fattori di correlazione ξ**
(Tab. 6.4.III se da prove di carico statico, 6.4.IV se da metodi analitici/prove in sito, 6.4.V se da
prove dinamiche) - vedi l'altro esempio.

## Effetto di gruppo (§6.4.3.1.1.1)

Per la **palificata** la resistenza caratteristica è la **somma** delle R_k dei singoli pali, ma va
valutata una possibile **riduzione per effetto di gruppo**, in funzione della **tipologia** dei pali
(trivellati), della **natura dei terreni** e della **configurazione geometrica** (interasse) della
palificata.

## Carichi orizzontali in testa (§6.4.3.1.2)

Per i **carichi trasversali** valgono le stesse regole dei carichi assiali, ma con il coefficiente
parziale **γT = 1,3** (**Tab. 6.4.VI**). Va considerato il **vincolo alla testa** dei pali offerto dal
plinto e una possibile **riduzione per effetto di gruppo**.

## SLE (§6.4.3.2)

Verificare **cedimenti/sollevamenti** e **spostamenti trasversali** nelle **combinazioni caratteristiche**
(§2.5.3), compatibili con i requisiti prestazionali della struttura in elevazione [6.2.7].

## Nota

La skill **inquadra** stati limite, approcci e coefficienti: **non calcola** R_k/R_d, non valuta l'effetto
di gruppo, non dimensiona i pali e **non riproduce** le Tab. 6.2.I/6.2.II/6.8.I né la Circolare 7/2019,
che restano compito del progettista con la relazione geotecnica.
