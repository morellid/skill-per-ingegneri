# Output atteso - Paratia con un ordine di tiranti

## Tipologia, criteri, modello (§6.5, §6.5.1, §6.5.2)

È una **paratia**: la funzione di sostegno è assicurata **principalmente dalla resistenza del volume di
terreno a valle** e dagli **ancoraggi/puntoni** (qui i **tiranti**) (§6.5). Poiché il sostegno è affidato
al terreno a valle, nel **modello geometrico** (§6.5.2.2) la **quota di valle** va ridotta del **minore**
tra: 10% dell'altezza da sostenere (opere a sbalzo), **10% della differenza di quota tra il livello
inferiore di vincolo e il fondo scavo** (opere vincolate, come qui per la presenza del tirante) e
**0,5 m**. Negli SLU, in assenza di drenaggi, ipotizzare la **falda** non inferiore al livello dei
terreni a bassa permeabilità (**k < 10⁻⁶ m/s**). Con l'edificio adiacente, valutare gli spostamenti a
tergo e la compatibilità, con piano di monitoraggio (§6.5.1).

## Quali stati limite (paratie, §6.5.3.1.2)

Accertare [6.2.1] (**E_d ≤ R_d**) per:

- **SLU geotecnici (GEO) e idraulici (UPL, HYD)**: collasso per **rotazione rigida** intorno a un punto,
  **carico limite verticale**, **sfilamento** di uno o più ancoraggi, **instabilità del fondo scavo** in
  terreni a grana fine non drenati, **instabilità per sollevamento**, **sifonamento** del fondo scavo,
  **instabilità globale** del complesso opera-terreno;
- **SLU strutturali (STR)**: resistenza di **ancoraggi**, **puntoni/sistemi di contrasto** e della
  **paratia**.

## Con quale approccio e quali combinazioni

- **Stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (coefficienti dalle Tab.
  6.2.I/6.2.II e Tab. 6.8.I - non riprodotte qui).
- **Stati limite idraulici (UPL e HYD)** → verifiche come al **§6.2.4.2** (non riprodotto qui): rilevanti
  qui per la **falda** e il **fondo scavo**.
- **Rimanenti verifiche** → **Approccio 1** con **entrambe** le combinazioni:
  - **Combinazione 1: (A1+M1+R1)**
  - **Combinazione 2: (A2+M2+R1)**

  con i coefficienti γR del **gruppo R1 pari all'unità** (Tab. 6.2.I/6.2.II).

Vanno inoltre **verificati gli ancoraggi (tiranti), i puntoni e le strutture di controventamento**.

## Resistenza passiva con attrito elevato (δ > φ'/2)

Per **δ > φ'/2** (angolo d'attrito terreno-parete elevato), nella valutazione della **resistenza
passiva** è necessario **tener conto della non planarità delle superfici di scorrimento** (§6.5.3.1.2):
l'ipotesi di superfici piane sovrastima la resistenza passiva.

## SLE ed edificio adiacente (§6.5.3.2)

Valutare gli **spostamenti** dell'opera e del terreno per la compatibilità con la funzionalità e con la
sicurezza dei manufatti adiacenti. Per l'**edificio sensibile** va sviluppata una **specifica analisi
dell'interazione** opera-terreno tenendo conto della **sequenza delle fasi costruttive**.

## Nota

La skill **inquadra** stati limite, approcci e combinazioni: **non** calcola le spinte, non esegue le
verifiche, non dimensiona la paratia o i tiranti e **non** riproduce le Tab. 6.2.I/6.2.II/6.8.I, il
§6.2.4.2 né la Circolare 7/2019, che restano compito del progettista con la relazione geotecnica. Il
caso **sismico** (§7.11.6) non è trattato.
