# Task: valuta-esclusione-verifica-liquefazione

Inquadra la **definizione** di liquefazione e verifica se ricorre almeno una delle **condizioni di
esclusione** della verifica a liquefazione secondo le **NTC 2018 par. 7.11.3.4.1-7.11.3.4.2**. Supporto
documentale: **non** calcola il coefficiente di sicurezza.

## Quando usarla

Il tecnico, nella relazione geotecnica per un sito sismico, deve stabilire se la verifica a liquefazione è
**necessaria** oppure può essere **omessa**. Se nessuna condizione di esclusione ricorre, usa
`inquadra-metodo-coefficiente-sicurezza`.

## Passi

1. **Definizione e obiettivo** (§7.11.3.4.1): il sito deve essere **stabile nei confronti della liquefazione**
   (perdita di resistenza al taglio / accumulo di deformazioni plastiche in **terreni saturi prevalentemente
   sabbiosi**, sotto **azioni cicliche/dinamiche** in **condizioni non drenate**). Se suscettibile e con
   effetti rilevanti → **interventi di consolidamento** e/o **trasferimento del carico** a strati non
   suscettibili; con **fondazioni profonde** → valutare **riduzione della capacità portante** e **incrementi
   nei pali**.

2. **Condizioni di esclusione** (§7.11.3.4.2): la verifica **può essere omessa** quando si manifesta **almeno
   una** delle seguenti circostanze:
   - **(1)** accelerazione massima attesa al piano campagna in **campo libero** (assenza di manufatti)
     **< 0,1 g**;
   - **(2)** **profondità media stagionale della falda > 15 m** dal piano campagna (piano campagna
     sub-orizzontale, **fondazioni superficiali**);
   - **(3)** **sabbie pulite** con **(N₁)₆₀ > 30** oppure **q_c1N > 180** (resistenze penetrometriche
     normalizzate a una **tensione efficace verticale di 100 kPa**: (N₁)₆₀ da **SPT**, q_c1N da **CPT**);
   - **(4)** **distribuzione granulometrica esterna** ai fusi della **Fig. 7.11.1(a)** per terreni con
     **U_c < 3,5** e **Fig. 7.11.1(b)** per **U_c > 3,5**.

3. **Indagini** (§7.11.3.4.2): se la **condizione 1 non è soddisfatta**, le indagini geotecniche devono essere
   finalizzate almeno alla determinazione dei parametri necessari per le **condizioni 2, 3 e 4**.

4. **Esito**: se ricorre **almeno una** condizione → la verifica **può essere omessa**; se **nessuna** ricorre
   (con strati/lenti di sabbie sciolte sotto falda) → procedere con l'analisi (altro task).

Usa la checklist in `../references/estratti/verifica-liquefazione-checklist.md` (sezioni 1 e 2).

## Output atteso

L'indicazione se la verifica a liquefazione **può essere omessa** (con la/e condizione/i di esclusione
soddisfatta/e) oppure è **necessaria**, con **rinvio ai paragrafi/figura** NTC. Nessun calcolo del
coefficiente di sicurezza.

## Cosa NON fare

- Non **calcolare** il coefficiente di sicurezza (usa l'altro task) né derivare CRR/CSR.
- Non **progettare** gli interventi di consolidamento né le fondazioni profonde.
