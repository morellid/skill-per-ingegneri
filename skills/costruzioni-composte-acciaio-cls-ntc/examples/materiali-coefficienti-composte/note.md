# Nota

Esempio ancorato al **§4.3.3** (resistenze di progetto e coefficienti, [4.3.6]) e al **§4.3.4.2** (resistenza
a flessione e taglio) delle NTC 2018, trascritti in `references/fonti/ntc2018-par-4-3.md`.

Punti verificati sul testo:

- **fd = fk/γM** [4.3.6]; allo SLU **γC = 1,5**, **γA = 1,05**, **γS = 1,15**, **γV = 1,25**; allo SLE e
  nelle situazioni eccezionali γM = 1.
- Classe del calcestruzzo ammessa **C20/25 - C60/75** (§4.3.3.1.2).
- **Metodo plastico** ammesso per le classi **1 e 2**, con compressione del calcestruzzo pari a **0,85·fcd**
  (§4.3.4.2.1.2). Armatura As in classe 1-2 in B450C, condizione [4.3.1].
- **Taglio verticale** affidato interamente alla trave metallica (§4.3.4.2.2, formule §4.2.4.1.2).

La skill **non** calcola il momento resistente né dimensiona la sezione: fornisce coefficienti e criteri. I
valori caratteristici (fyk, fck, fsk) provengono dai §11.2/11.3 (non trattati).
