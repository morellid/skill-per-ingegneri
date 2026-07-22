# Task: inquadra-combinazione-componenti

Inquadra la **combinazione delle tre componenti dell'azione sismica** secondo le **NTC 2018 par. 7.3.5** (analisi
dinamica o statica, lineare o non lineare). Supporto documentale: **non** esegue l'analisi ne' calcola gli
effetti.

## Quando usarla

Il progettista deve combinare gli effetti delle componenti Ex, Ey, Ez dell'azione sismica. Per l'analisi con
integrazione al passo e la variabilità spaziale del moto usa `inquadra-analisi-integrazione-passo-variabilita`.

## Passi

1. **Espressione di combinazione** (§7.3.5): la risposta si calcola **unitariamente** per le tre componenti
   applicando:

       1,00 x Ex + 0,30 x Ey + 0,30 x Ez    [7.3.10]

   dove Ex, Ey, Ez sono gli effetti delle componenti dell'azione sismica nelle tre direzioni; il coefficiente
   **1,00** si applica alla componente dominante e **0,30** alle altre due.
2. **Permutazione circolare** (§7.3.5): gli **effetti più gravosi** si ricavano dal confronto tra le **tre
   combinazioni** ottenute **permutando circolarmente** i coefficienti moltiplicativi, cioe' assegnando a turno
   il coefficiente 1,00 a ciascuna delle tre componenti:
   - Comb. 1: **1,00** x Ex + 0,30 x Ey + 0,30 x Ez;
   - Comb. 2: 0,30 x Ex + **1,00** x Ey + 0,30 x Ez;
   - Comb. 3: 0,30 x Ex + 0,30 x Ey + **1,00** x Ez.
3. **Componente verticale** (§7.3.5): la componente **verticale (Ez)** deve essere tenuta in conto **unicamente
   nei casi previsti al §7.2.2**; negli altri casi la combinazione riguarda le sole due componenti orizzontali
   (con il coefficiente 1,00 assegnato a turno a Ex e Ey e 0,30 all'altra).

Usa la checklist in `../references/estratti/combinazione-componenti-checklist.md` (sezioni 1-2).

## Output atteso

Un inquadramento che riporti l'espressione [7.3.10] (1,00 x Ex + 0,30 x Ey + 0,30 x Ez), le tre combinazioni per
permutazione circolare e la condizione per la componente verticale (§7.2.2), con **rinvio al paragrafo/formula**
NTC. Nessun calcolo degli effetti.

## Cosa NON fare

- Non calcolare gli effetti Ex, Ey, Ez ne' eseguire l'analisi.
- Non trattare i casi che richiedono la **componente verticale** (§7.2.2) ne' la **variabilità spaziale del
  moto** (§3.2.4): rinvio ai paragrafi.
