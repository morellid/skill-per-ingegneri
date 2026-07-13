# capacita-portante-fondazione-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 vs esempi pubblicati/software geotecnico da completare)

Skill code-driven per il **calcolo della capacita' portante di fondazioni superficiali** e la verifica GEO a carico limite delle **NTC 2018 par. 6.4.2.1** (Approccio 2, A1+M1+R3).

- Il **quadro della verifica** e' delle NTC: Ed <= Rd [6.2.1], gamma_R = 2,3 (Tab. 6.4.I), M1 = 1,0 (Tab. 6.2.II), azione e resistenza come forze normali al piano di posa (Circ. C6.4.2.1).
- La **formulazione del carico limite** viene dal **FHWA NHI-06-089 "Soils and Foundations - Reference Manual Volume II"** (U.S. DOT, 2006, pubblico dominio), par. 8.4: fattori Nc/Nq/Ngamma (espressioni AASHTO), fattori di forma (Table 8-4), falda con interpolazione (Table 8-5), dimensioni efficaci per eccentricita' (eq. 8-7..8-9, limite e < 1/6). E' usata come "**altro codice internazionale**" ai sensi del **cap. 12 NTC 2018**.

## Target

Ingegneri geotecnici e strutturisti italiani in fase preliminare (nastri e plinti su terreno omogeneo). Per modellazioni complete e casi complessi servono software geotecnici dedicati.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `calcola-capacita-portante` | Dato B, L (o nastro), Df, condizione drenata/non drenata, parametri caratteristici, falda, eventuali eccentricita' e sovraccarico: qult con termini e fattori esposti, q_Rd = qult/2,3, R_d = q_Rd*A', confronto Ed <= Rd se Ed fornito. Casi fuori ambito **rifiutati** (carico inclinato, base inclinata, pendio, stratificazione, rottura locale, sisma; eccentricita' >= 1/6) |

Calcolo deterministico con `tasks/lib/capacita_portante.py` (21 test):

```bash
python3 tasks/lib/capacita_portante.py --b 2 --l 3 --df 1 --gamma 18 \
  --condizione drenata --phi 30 --c 5 --dw 1.5 --ed 900
# -> qult = 843,2 kPa; q_Rd = 366,6 kPa; R_d = 2.199,8 kN; Ed <= Rd: si
```

## Fonti consultate

- **DM 17/01/2018 (NTC 2018)**, GU n. 42 del 20/02/2018 - parr. 6.2.4.1.1-6.2.4.1.2, 6.4.2-6.4.2.1, cap. 12
- **Circolare MIT n. 7 del 21/01/2019**, GU n. 35 dell'11/02/2019 - C6.4.2.1
- **FHWA NHI-06-089** (U.S. DOT, dicembre 2006) - par. 8.4 - pubblico dominio

Dettaglio (URL, SHA256, trascrizioni) in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Solo carico verticale (anche eccentrico entro 1/6), base e piano campagna orizzontali, terreno omogeneo, rottura generale
- Non calcola Ed (combinazioni A1), scorrimento, stabilita' globale, STR, SLE (cedimenti: skill `cedimenti-edometrici-ntc`), verifiche sismiche
- Non stima i parametri geotecnici (niente correlazioni SPT ne' capacita' presuntive)
- dq solo come input esplicito (Table 8-6), default conservativo 1,0

**La skill non sostituisce il progetto geotecnico firmato dal progettista.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
