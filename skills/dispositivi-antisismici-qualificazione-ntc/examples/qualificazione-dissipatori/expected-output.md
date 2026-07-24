# Output atteso — Qualificazione e requisiti di dissipatori viscosi (NTC 2018 §11.9.2, §11.9.6)

> Supporto documentale: inquadra qualificazione e requisiti dei dispositivi viscosi. **Non** esegue il progetto del
> sistema di dissipazione (§7.10).

## 1. Procedura di qualificazione (§11.9.2)

- I dispositivi antisismici che ricadono nel **punto A del §11.1** devono essere **conformi alla UNI EN 15129** e
  recare la **Marcatura CE**, con sistema di **valutazione e verifica della costanza della prestazione (VVCP) per le
  applicazioni critiche**. → I dissipatori viscosi dichiarati conformi a UNI EN 15129 + CE rientrano in questo
  percorso.
- Se il dispositivo **non ricadesse (o non completamente)** nel campo della UNI EN 15129, si applicherebbe il **caso
  C del §11.1** (Certificazione di valutazione tecnica del Servizio Tecnico Centrale).
- Ogni fornitura deve essere accompagnata dal **manuale** di posa in opera e manutenzione.

## 2. Caratterizzazione e fattore di affidabilità (§11.9.6)

- I viscosi trasmettono in generale solo azioni orizzontali, con forza proporzionale a **v^α**; il comportamento è
  caratterizzato dalla massima forza **Fmax** e dall'energia dissipata **Ed** (costanti **C** e **α**; ciclo ellittico
  per α = 1).
- Stabilità ciclica: **|Ed(i) − Ed(3)| / Ed(3) ≤ 10%** [11.9.7].
- Limiti massimi (Tab. 11.9.III): Fmax ±15%/±5%/±5%/±10%; Ed −15%/−5%/−5%/±10%.
- **Fattore di affidabilità**: per tener conto di velocità superiori a quelle di progetto, la forza massima di
  progetto va amplificata con
  **γv = (1 + td)·(1,5)^α**  [11.9.8]
  dove **td** è la tolleranza sulla forza di progetto fornita dal fabbricante (comprensiva della variabilità per
  temperatura) e **α** è l'esponente della legge costitutiva.

## 3. Requisiti costruttivi (§11.9.6)

- Il dispositivo deve possedere **due cerniere sferiche** alle estremità (per evitare trafilamento/deterioramento
  delle guarnizioni); la **rotazione consentita non deve essere inferiore a 2 gradi sessagesimali**.
- Deve **evitare snervamenti** sotto i carichi di servizio e **rotture** al collasso, sopportare le accelerazioni
  laterali allo SLC e, in assenza di tale valutazione, resistere a una **forza minima trasversale pari ad almeno due
  volte il peso proprio** del dispositivo. Il progetto deve consentire la manutenzione ed evitare instabilità degli
  steli.

## 4. Prove di accettazione (§11.9.6.1)

- Le prove di accettazione devono essere effettuate su **almeno il 20% dei dispositivi, comunque non meno di 4** e non
  più del numero da mettere in opera (a cura del Direttore dei Lavori, laboratorio art. 59 — §11.9.3).

## 5. Sintesi

| Aspetto | Esito |
|---|---|
| Qualificazione (§11.9.2) | UNI EN 15129 + Marcatura CE (VVCP applicazioni critiche); altrimenti caso C |
| Fattore di affidabilità (§11.9.6) | **γv = (1+td)·(1,5)^α** |
| Cerniere / rotazione (§11.9.6) | Due cerniere sferiche; rotazione **≥ 2°** |
| Forza minima trasversale (§11.9.6) | **≥ 2× peso proprio** (in assenza di valutazione allo SLC) |
| Stabilità ciclica (§11.9.6) | |Ed(i)−Ed(3)|/Ed(3) ≤ 10%; Tab. 11.9.III |
| Prove accettazione (§11.9.6.1) | ≥ 20% e ≥ 4 |

**Fuori scope**: progetto del sistema di dissipazione e dimensionamento dei dispositivi (§7.10, → skill
`isolamento-sismico-ntc`).

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.9 delle NTC 2018, della UNI EN 15129 e della relativa Circolare applicativa.**
