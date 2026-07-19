# Output atteso - Solaio di un edificio con uso misto residenziale/uffici/negozio

## Categorie d'uso e sovraccarichi (Tab. 3.1.II)

Assegnando a ogni ambiente la **categoria d'uso** della Tab. 3.1.II (qk [kN/m²], Qk [kN], Hk [kN/m]):

| Ambiente | Categoria | qk | Qk | Hk |
|---|---|---|---|---|
| Negozio (piano terra) | **D1** | 4,00 | 4,00 | 2,00 |
| Uffici aperti al pubblico | **B2** | 3,00 | 2,00 | 1,00 |
| Appartamenti | **A** | 2,00 | 2,00 | 1,00 |
| Scale comuni e balconi (in edificio A/B) | A/B | 4,00 | 4,00 | 2,00 |
| Copertura solo manutenzione | **H** | 0,50 | 1,20 | 1,00 |

> Nota: se il negozio facesse parte di un **centro commerciale/grande magazzino** sarebbe **D2** (qk 5,00).
> Le **scale/balconi** al servizio degli ambienti C o D assumono valori **≥ 4,00** secondo la categoria
> servita.

## Verifiche d'insieme vs verifiche locali

- I **qk** (uniformi) si usano per le **verifiche d'insieme** dell'orizzontamento; in presenza di
  ripartizione trasversale sono assumibili uniformemente ripartiti (§3.1.4.1), con eventuali **riduzioni**
  per area di influenza/numero di piani (vedi l'altro esempio).
- I **Qk** (concentrati) sono per **verifiche locali distinte** e **non** si applicano contemporaneamente
  ai qk d'insieme; impronta 50×50 mm salvo rimesse/parcheggi (§3.1.4.2).

## Parapetti dei balconi (Hk, §3.1.4.3)

I **sovraccarichi orizzontali lineari Hk** si usano per **verifiche locali** e **non** si combinano con le
verifiche d'insieme. Per i **balconi** (in edificio residenziale/uffici) **Hk = 2,00 kN/m**, applicato al
**parapetto/mancorrente** alla quota del **bordo superiore** (per le pareti, invece, a 1,20 m dal
calpestio).

## Nota

La skill fornisce i **valori tabellari** della Tab. 3.1.II e le regole di applicazione: **non calcola i
carichi di progetto, non combina le azioni e non dimensiona** i solai, che restano compito del progettista
con la Circolare 7/2019.
