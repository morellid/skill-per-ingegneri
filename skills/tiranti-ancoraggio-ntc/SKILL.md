---
name: tiranti-ancoraggio-ntc
description: "Supporto documentale al progettista geotecnico e strutturale per l'inquadramento del progetto e della verifica dei tiranti di ancoraggio secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.6. Aiuta a inquadrare i criteri di progetto (ancoraggi provvisori o permanenti, attivi o presollecitati e passivi; nel progetto vanno indicati orientazione, lunghezza, numero, resistenza di progetto Rad e programma di tesatura; la conferma sperimentale con prove di trazione in sito e' sempre necessaria); la verifica di sicurezza allo stato limite ultimo di sfilamento della fondazione dell'ancoraggio con la condizione Ed minore o uguale a Rad e la combinazione A1+M1+R3, con la resistenza di progetto Rad uguale alla resistenza caratteristica Rak divisa per il coefficiente parziale gamma_R della Tab. 6.6.I (gamma_R uguale a 1,1 per gli ancoraggi temporanei e 1,2 per quelli permanenti); la determinazione della resistenza caratteristica Rak dalle prove di progetto (Rak uguale al minore fra il valor medio diviso xi_a1 e il valor minimo diviso xi_a2, con xi dalla Tab. 6.6.II in funzione del numero di ancoraggi di prova) oppure dal calcolo analitico (Rak uguale al minore fra il valor medio diviso xi_a3 e il valor minimo diviso xi_a4, con xi dalla Tab. 6.6.III in funzione del numero di profili di indagine, riferendosi ai coefficienti parziali M1 senza applicare gamma ai parametri del terreno); gli aspetti costruttivi (sistemi qualificati par. 11.5.2, diametro dei fori non inferiore al nominale, tesatura dopo l'esaurimento della presa e dell'indurimento); e le prove di carico, sia le prove di progetto su ancoraggi preliminari (numero minimo pari a 1 se gli ancoraggi sono meno di 30, 2 tra 31 e 50, 3 tra 51 e 100, 7 tra 101 e 200, 8 tra 201 e 500, 10 oltre 500) sia le prove in corso d'opera su tutti gli ancoraggi con un ciclo di carico e scarico pari a 1,2 volte l'azione di progetto Pd delle verifiche di esercizio. Use when a geotechnical or structural designer must frame the design and verification of ground anchors under the Italian NTC 2018 par. 6.6; it is a documentary aid and does NOT compute the pull-out resistance nor size the anchor or its tendon, does NOT run or interpret the load tests, does NOT cover the anchorage systems as products (par. 11.5.2), the retaining works (par. 6.5) nor the seismic design, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Tiranti di ancoraggio: progetto e verifica (NTC 2018 par. 6.6)"
summary: "Inquadra progetto e verifica dei tiranti di ancoraggio (NTC 2018 par. 6.6): verifica SLU a sfilamento Ed<=Rad con Rad=Rak/gamma_R (Tab. 6.6.I: 1,1 temporanei / 1,2 permanenti), Rak da prove (Tab. 6.6.II) o calcolo (Tab. 6.6.III), combinazione A1+M1+R3, e prove di carico."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.6: verifica SLU a sfilamento Ed<=Rad, Rad=Rak/gamma_R (Tab. 6.6.I: 1,1/1,2), Rak da prove o calcolo [6.6.1-2] con xi (Tab. 6.6.II/III), comb. A1+M1+R3"
  - "NTC 2018 - par. 6.6.4 prove di carico: prove di progetto (numero minimo per numero di ancoraggi) e prove in corso d'opera su tutti a 1,2 Pd; rinvio par. 6.5, 11.5.2 e Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - tiranti-di-ancoraggio
  - geotecnica
  - ntc-2018
  - verifica-slu
  - prove-di-carico
---

# Tiranti di ancoraggio: progetto e verifica (NTC 2018 par. 6.6)

## Quando usare questa skill

Usala quando un **progettista geotecnico o strutturale** deve **inquadrare il progetto e la verifica dei
tiranti di ancoraggio** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.6**:

- **criteri di progetto** (§6.6.1): provvisori/permanenti, attivi/passivi;
- **verifica SLU a sfilamento** (§6.6.2): Ed ≤ Rad, Rad = Rak/γR, fattori di correlazione;
- **aspetti costruttivi** (§6.6.3);
- **prove di carico** (§6.6.4): di progetto e in corso d'opera.

**Non è** uno strumento che calcola la resistenza allo sfilamento o dimensiona il tirante, né esegue le prove:
è un **supporto documentale** che inquadra criteri, coefficienti, formule e prove. Complementa
`opere-sostegno-ntc` (§6.5), poiché paratie e muri tirantati impiegano i tiranti del §6.6.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-sfilamento-tiranti` | Verifica SLU a sfilamento: Ed ≤ Rad, Rad = Rak/γR (Tab. 6.6.I), Rak da prove/calcolo (Tab. 6.6.II/III), combinazione A1+M1+R3 (§6.6.2) |
| `inquadra-criteri-prove-tiranti` | Criteri di progetto (§6.6.1), aspetti costruttivi (§6.6.3) e prove di carico di progetto e in corso d'opera (§6.6.4) |

## Punti chiave (verificati sul testo)

- **Definizione** (§6.6): tiranti = elementi strutturali collegati al terreno che sostengono trazione.
- **Criteri** (§6.6.1): provvisori/permanenti, attivi (presollecitati)/passivi; indicare orientazione,
  lunghezza, numero, Rad, tesatura; **conferma sperimentale con prove sempre necessaria**.
- **Verifica SLU** (§6.6.2): **Ed ≤ Rad**, combinazione **A1+M1+R3**; **Rad = Rak/γR** con **Tab. 6.6.I**
  (**γR = 1,1** temporanei, **1,2** permanenti).
- **Rak**: (a) da prove **Rak = Min{Ra,m,medio/ξa1; Ra,m,min/ξa2}** [6.6.1] (Tab. 6.6.II: ξa1 1,5/1,4/1,3, ξa2
  1,5/1,3/1,2 per n=1/2/>2); (b) da calcolo **Rak = Min{Ra,c,medio/ξa3; Ra,c,min/ξa4}** [6.6.2] (Tab. 6.6.III,
  n=1..≥5); nel calcolo analitico non si applicano γ ai parametri (M1).
- **Aspetti costruttivi** (§6.6.3): sistemi qualificati (§11.5.2), fori ≥ nominale, tesatura dopo presa.
- **Prove** (§6.6.4): di progetto su ancoraggi preliminari (**1/2/3/7/8/10** per <30/31-50/51-100/101-200/
  201-500/>500 ancoraggi); in corso d'opera su **tutti** a **1,2·Pd** (SLE).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.6** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** la resistenza allo sfilamento né **dimensiona** il tirante o la sua armatura; **non** valuta
  Ra,m/Ra,c al posto del progettista.
- **Non esegue** né **interpreta** le prove di carico; **non riproduce** i **sistemi di ancoraggio come
  prodotti** (§11.5.2) né la progettazione strutturale dell'armatura.
- **Non tratta** le **paratie/muri** (§6.5, skill `opere-sostegno-ntc`) né la **progettazione sismica** (Cap.
  7); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.6 delle NTC 2018 e della Circolare applicativa.**
