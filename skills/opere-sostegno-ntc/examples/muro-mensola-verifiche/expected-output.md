# Output atteso - Muro di sostegno a mensola in c.a., altezza 4 m

## Tipologia e criteri (§6.5, §6.5.1)

È un **muro** (funzione di sostegno affidata al **peso proprio** del muro e del terreno su di esso):
tipologia a **mensola** in c.a. (§6.5). Vanno curati il **riempimento a tergo** costipato e a
granulometria drenante e un **drenaggio** efficace nel tempo (§6.5.1). Se ci sono costruzioni
preesistenti, valutare gli spostamenti del terreno a tergo e la compatibilità. Il caso **sismico**
(§7.11.6) **non** è trattato da questa skill: se rilevante, va aggiunto.

## Azioni e modello geometrico (§6.5.2)

Considerare peso del terreno/riempimento, **sovraccarichi** a tergo (qui i **veicoli in transito** del
rilevato stradale, §6.5.2.1), acqua e le altre azioni pertinenti (§6.5.2). Negli SLU, in assenza di
drenaggi, ipotizzare la **falda** non inferiore al livello dei terreni a bassa permeabilità
(**k < 10⁻⁶ m/s**) (§6.5.2.2). La **riduzione della quota di valle** (minore tra 10% dell'altezza, 10%
della differenza di quota e 0,5 m) riguarda le opere che affidano il sostegno alla resistenza a valle:
per un **muro a mensola** il sostegno è affidato al peso proprio, quindi in generale non si conta la
resistenza a valle (vedi scorrimento).

## Quali stati limite (muri, §6.5.3.1.1)

Accertare [6.2.1] (**E_d ≤ R_d**) per:

- **SLU geotecnici (GEO)**: **scorrimento** sul piano di posa, **carico limite** del complesso
  fondazione-terreno, **ribaltamento**, **stabilità globale** del complesso opera-terreno;
- **SLU strutturali (STR)**: resistenza degli elementi strutturali (fusto, mensola di fondazione).

## Con quale approccio e quali coefficienti

- **Stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (come §6.8; coefficienti dalle Tab.
  6.2.I/6.2.II e Tab. 6.8.I - non riprodotte qui).
- **Rimanenti verifiche** (scorrimento, carico limite, ribaltamento, STR) → **Approccio 2 (A1+M1+R3)**,
  con i coefficienti della **Tab. 6.5.I**. Nel **ribaltamento** i coefficienti R3 si applicano agli
  effetti delle azioni **stabilizzanti**.

**Tab. 6.5.I (γR, gruppo R3)**

| Verifica | γR |
|---|---|
| Capacità portante della fondazione | 1,4 |
| Scorrimento | 1,1 |
| Ribaltamento | 1,15 |
| Resistenza del terreno a valle | 1,4 |

## Resistenza passiva davanti al muro nello scorrimento? In generale no

Per la verifica **alla traslazione (scorrimento)** sul piano di posa di muri con fondazioni superficiali,
**non** si deve **in generale** considerare il contributo della **resistenza passiva** del terreno
antistante il muro (§6.5.3.1.1). Solo in **casi particolari**, da giustificare con le caratteristiche
meccaniche dei terreni e le modalità costruttive, se ne può contare **al più il 50%**, a condizione che
il contributo sia effettivamente permanente e che gli spostamenti necessari a mobilitarlo siano
compatibili con le prestazioni attese dell'opera.

## SLE (§6.5.3.2)

Valutare gli **spostamenti** dell'opera e del terreno, compatibili con la funzionalità dell'opera (qui il
rilevato/sede stradale) e con la sicurezza dei manufatti adiacenti.

## Nota

La skill **inquadra** stati limite, approcci e coefficienti (Tab. 6.5.I): **non calcola** le spinte, non
esegue le verifiche E_d ≤ R_d, non dimensiona il muro e **non riproduce** le Tab. 6.2.I/6.2.II/6.8.I né
la Circolare 7/2019, che restano compito del progettista con la relazione geotecnica.
