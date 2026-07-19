# Task - Inquadra i sovraccarichi variabili per categoria d'uso (§3.1.4, Tab. 3.1.II)

## Obiettivo

Individuare i **sovraccarichi variabili** (carichi imposti) - **qk** distribuiti, **Qk** concentrati,
**Hk** orizzontali - per la **categoria d'uso** dell'ambiente, secondo la **Tab. 3.1.II** delle NTC 2018,
e le regole di applicazione delle verifiche locali.

## Input richiesti

- **destinazione d'uso** dei diversi ambienti (residenziale, uffici, affollamento, commerciale,
  magazzino, rimessa, copertura, scale/balconi);
- presenza di **carichi atipici** (macchinari, serbatoi, depositi, impianti);
- elementi da verificare (orizzontamento d'insieme, verifiche locali, parapetti/pareti).

## Procedura (ancorata al testo)

1. **Categoria d'uso** (Tab. 3.1.II). Assegnare a ogni ambiente la categoria e leggere qk/Qk/Hk:
   - **A** residenziale 2,00/2,00/1,00; **scale/balconi** 4,00/4,00/2,00;
   - **B1** uffici non aperti 2,00; **B2** aperti al pubblico 3,00 (Qk 2,00, Hk 1,00);
   - **C1** 3,00; **C2** 4,00; **C3/C4/C5** 5,00 (affollamento); scale/balconi ≥4,00 secondo categoria;
   - **D1** negozi 4,00; **D2** centri commerciali 5,00;
   - **E1** magazzini ≥6,00 (Qk 7,00); **E2** industriale **caso per caso**;
   - **F** rimesse veicoli leggeri 2,50 (Qk 2×10,00); **G** veicoli medi ≥5,00 (Qk 2×50,00);
   - **H** coperture di sola manutenzione 0,50 (Qk 1,20); **I** praticabili → categoria servita; **K** usi
     speciali **caso per caso**.

2. **Carichi atipici** (§3.1.4). Macchinari, serbatoi, depositi, ecc. → intensità **valutate caso per
   caso** sui massimi prevedibili e **indicate in progetto** e nel collaudo statico.

3. **qk uniformi** (§3.1.4.1). Per le verifiche d'insieme, in presenza di ripartizione trasversale,
   assumibili uniformemente ripartiti; verificare le riduzioni per **area di influenza** e **numero di
   piani** (task dedicato).

4. **Qk concentrati** (§3.1.4.2). **Verifiche locali distinte**, **non** contemporanee ai qk d'insieme;
   impronta **50×50 mm** (F: 100×100 mm a 1,80 m; G: 200×200 mm a 1,80 m).

5. **Hk orizzontali** (§3.1.4.3). **Verifiche locali**, **non** combinate con le verifiche d'insieme;
   applicati a **1,20 m** dal calpestio e ai **parapetti** al bordo superiore.

## Output

Una nota che assegni a ogni ambiente la **categoria d'uso** e i valori **qk/Qk/Hk** della Tab. 3.1.II,
distinguendo le **verifiche d'insieme** (qk) dalle **verifiche locali** (Qk, Hk) e segnalando i **carichi
atipici** da valutare caso per caso. **La skill fornisce i valori tabellari; non calcola i carichi di
progetto né dimensiona.**
