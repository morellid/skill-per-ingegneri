# Output atteso: plinto 2x3, drenata, falda a -1,5 m, Ed = 900 kN

## Comando eseguito

```bash
python3 tasks/lib/capacita_portante.py --b 2 --l 3 --df 1 --gamma 18 \
  --condizione drenata --phi 30 --c 5 --dw 1.5 --ed 900
```

## Risultato (JSON del modulo, campi principali)

```json
{
  "qult_kPa": 843.24,
  "q_Rd_kPa": 366.63,
  "R_d_kN": 2199.76,
  "dettaglio": {
    "fattori_N": {"Nc": 30.14, "Nq": 18.401, "Ngamma": 22.402},
    "fattori_forma": {"sc": 1.407, "sq": 1.3849, "sgamma": 0.7333},
    "fattori_falda": {"Cwq": 1.0, "Cwgamma": 0.5833},
    "termini_kpa": {"coesione": 212.04, "sovraccarico": 458.71, "peso": 172.5},
    "gamma_R": 2.3,
    "Ed_kn": 900.0
  },
  "Ed_minore_uguale_Rd": true
}
```

(Avvertenze del modulo omesse per brevita': riportarle sempre integralmente nella risposta.)

## Sintesi testuale attesa

- **qult = 843,2 kPa** con la formulazione FHWA NHI-06-089 par. 8.4 (eq. [8-6] con base e piano campagna orizzontali): fattori Nc = 30,14 / Nq = 18,40 / Ngamma = 22,40 (eq. [8-2][8-3][8-5], phi' = 30); fattori di forma per L/B = 1,5 (Table 8-4); falda a DW = 1,5 m fra Df = 1,0 m e la soglia 1,5B+Df = 4,0 m -> Cwgamma = 0,583 per interpolazione (Table 8-5), Cwq = 1,0.
- **Catena NTC (par. 6.4.2.1, Approccio 2 A1+M1+R3)**: q_Rd = 843,2/2,3 = **366,6 kPa** (gamma_R = 2,3, Tab. 6.4.I); R_d = q_Rd x A' = 366,6 x 6,0 = **2.199,8 kN** (forza normale al piano di posa, C6.4.2.1).
- **Verifica [6.2.1]: Ed = 900 kN <= Rd = 2.199,8 kN -> soddisfatta** (Ed calcolato dall'utente con i coefficienti A1, Tab. 6.2.I; parametri caratteristici = di progetto con M1 = 1,0, Tab. 6.2.II).
- **Verifiche non coperte da richiamare**: scorrimento (gamma_R = 1,1), stabilita' globale, STR, SLE/cedimenti (skill `cedimenti-edometrici-ntc`), azioni sismiche (NTC 7.11.5.3.1).
- Formulazione usata come codice internazionale ex **cap. 12 NTC**: responsabilita' del progettista sui livelli di sicurezza; rinvio alla revisione e firma del progettista.
