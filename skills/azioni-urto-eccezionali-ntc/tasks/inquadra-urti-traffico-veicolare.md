# Task - Inquadra le azioni da urto di traffico veicolare (§3.6.3.2, 3.6.3.3)

## Obiettivo

Inquadrare le **azioni eccezionali da urto di traffico veicolare** su strutture esposte (sotto e sopra i
ponti, membrature in autorimesse), con la **classificazione**, le **forze statiche equivalenti** e i **punti
di applicazione**, secondo le NTC 2018 §3.6.3.

## Input richiesti

- posizione dell'elemento esposto (sotto ponte/struttura, sopra ponte, autorimessa) e tipo di strada;
- tipo di membratura (verticale/orizzontale) e, per elementi orizzontali, altezza del sottovia;
- per i carrelli elevatori: peso complessivo W (carrello + massimo carico).

## Procedura (ancorata al testo)

1. **Classificazione** (§3.6.3.2, Tab. 3.6.II). Verificare che le conseguenze dell'urto sull'elemento siano di
   **categoria 2 (localizzati)** o **3 (generalizzati)**: solo in tal caso le azioni da urto vanno applicate.

2. **Sotto ponti/strutture - forze equivalenti** (§3.6.3.3.1, Tab. 3.6.III). Assumere **Fd,x**: **1000 kN**
   (autostrade/extraurbane), **750 kN** (strade locali), **500 kN** (strade urbane), **50 kN** (automobili in
   parcheggi/autorimesse), **150 kN** (veicoli merci > 3,5 t). Considerare **non simultaneamente** Fd,x e
   **Fd,y = 0,50·Fd,x** [3.6.7].

3. **Punti di applicazione** (membrature verticali). Automobili → **0,5 m** sopra la superficie di marcia (area
   0,25 m × min(1,50 m; larghezza)); in generale → **1,25 m** (area 0,5 m × min(1,50 m; larghezza)).

4. **Elementi orizzontali sopra la strada** (§3.6.3.3.1, [3.6.8]). **F = r·Fd,x** con **r = 1,0** fino a 5 m di
   altezza del sottovia, **decrescente da 1,0 a 0** tra 5 e 6 m, **0** oltre 6 m; intradosso a **10° verso
   l'alto**, area **0,25 × 0,25 m**.

5. **Carrelli elevatori** (§3.6.3.3.1, [3.6.9]). Azione orizzontale **F = 5·W** a **0,75 m** dal piano di
   calpestio.

6. **Sopra i ponti** (§3.6.3.3.2). Sugli **elementi di sicurezza** forza orizzontale equivalente **100 kN**
   (100 mm sotto la sommità o 1,0 m sopra il piano di marcia, il minore); verifiche locali dell'impalcato →
   §5.1.3.10.

## Output

Una nota che indichi: la **categoria** di azione, il **valore di Fd,x** (Tab. 3.6.III), **Fd,y = 0,50·Fd,x**,
i **punti/aree di applicazione** e, per gli elementi orizzontali, **F = r·Fd,x**. **La skill inquadra le
azioni; non calcola le sollecitazioni né verifica gli elementi.**
