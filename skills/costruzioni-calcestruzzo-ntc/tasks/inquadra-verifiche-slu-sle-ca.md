# Task - Inquadra le verifiche SLU e SLE del c.a. (§4.1.2.2, 4.1.2.3)

## Obiettivo

Inquadrare le **verifiche agli stati limite ultimi** (pressoflessione, taglio, torsione, punzonamento) e
agli **stati limite di esercizio** (fessurazione, limitazione delle tensioni, deformazione) delle strutture
in calcestruzzo, secondo le NTC 2018 §4.1.

## Input richiesti

- tipo di sollecitazione (flessione, pressoflessione, taglio, torsione, carichi concentrati);
- classe di resistenza e tipo di armatura;
- condizioni ambientali (per la fessurazione) e combinazioni di azioni (SLE).

## Procedura (ancorata al testo)

1. **Verifiche SLU** (§4.1.2.3). Individuare le verifiche pertinenti: **pressoflessione** (conservazione
   delle sezioni piane, calcestruzzo non reagente a trazione, diagrammi di calcolo dei materiali); **taglio**
   con il modello a **traliccio** e inclinazione dei puntoni **1 ≤ ctgθ ≤ 2,5** [4.1.25] (resistenza con e
   senza armature trasversali); **torsione** (traliccio periferico, **1 ≤ ctgθ ≤ 2,5** [4.1.38]);
   **punzonamento** e carichi concentrati. Le resistenze di progetto sono fcd, fctd, fyd (§4.1.2.1.1).

2. **SLE - limitazione delle tensioni** (§4.1.2.2.5). Verificare: **σc ≤ 0,60·fck** in **combinazione
   caratteristica (rara)** [4.1.15] e **σc ≤ 0,45·fck** in **combinazione quasi permanente** [4.1.16] per il
   calcestruzzo; **σs ≤ 0,8·fyk** [4.1.17] per l'acciaio.

3. **SLE - fessurazione** (§4.1.2.2.4). Scegliere lo stato limite (**decompressione**, **formazione delle
   fessure**, **apertura delle fessure**) e il valore limite di apertura **w1 = 0,2 mm**, **w2 = 0,3 mm**,
   **w3 = 0,4 mm**, in funzione delle **condizioni ambientali** (ordinarie/aggressive/molto aggressive),
   della **sensibilità delle armature** (poco/molto sensibili) e della **combinazione** (frequente, quasi
   permanente). Verificare che il valore caratteristico wk non superi il limite pertinente.

4. **SLE - deformazione e vibrazioni** (§4.1.2.2.2-3). Contenere gli spostamenti (frecce) entro limiti
   compatibili con l'uso, l'aspetto e gli elementi non strutturali.

## Output

Una nota che elenchi: le **verifiche SLU** pertinenti (pressoflessione, taglio con ctgθ, torsione,
punzonamento); le **verifiche SLE** di limitazione delle tensioni (0,60·fck, 0,45·fck, 0,8·fyk) e di
fessurazione (stato limite e apertura w1/w2/w3 secondo ambiente e sensibilità). **La skill inquadra criteri
e limiti; non esegue le verifiche, non calcola le tensioni né le aperture di fessura e non arma la sezione.**
