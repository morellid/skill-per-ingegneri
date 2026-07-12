# Cedimenti edometrici - SLE NTC 2018 par. 6.2.4

> Versione: 0.2.0 | Stato: in sviluppo (validazione Livello 1; Livello 2 vs casi pubblicati/software geotecnico da completare)

Skill per il **calcolo del cedimento di consolidazione primaria** (compressione monodimensionale, per strati/sublayer) e per la **verifica documentale** delle verifiche SLE sui cedimenti.

- Il **quadro delle verifiche** viene da NTC 2018 § 6.2.4.3 (Ed <= Cd [6.2.7]) e Circ. 7/2019 C6.2.
- La **formulazione di calcolo** viene dal manuale **FHWA NHI-06-088 "Soils and Foundations - Reference Manual Volume I"** (U.S. DOT, 2006, pubblico dominio), par. 7.5.2: eq. [7-2] (normalconsolidato), [7-4] (sovraconsolidato con sigma_f > sigma_p), [7-6] (sottoconsolidato dichiarato). E' usata come "**altro codice internazionale**" ai sensi del **cap. 12 NTC 2018**, che pone in capo al progettista la responsabilita' sui livelli di sicurezza.

## Target

Ingegneri geotecnici e strutturisti italiani in fase preliminare (fondazioni superficiali su terreni coesivi). La skill calcola il cedimento primario per strati; per modellazioni complete servono software geotecnici dedicati.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `calcola-cedimento-edometrico` | Dato per strato h0, e0, Cc, Cr, sigma_0', sigma_p', delta_sigma' (al centro dello strato): OCR, caso NC/OC/UC, equazione FHWA applicata, contributi dei termini, S in m e mm, epsilon media; multistrato con somma dei contributi. Casi non coperti **rifiutati** (OC con sigma_f <= sigma_p; OCR < 1 senza dichiarazione di sottoconsolidazione) |
| `check-verifica-cedimenti` | Verifica documentale della relazione/nota di calcolo rispetto al quadro SLE NTC (prestazioni attese, limiti dichiarati, interazione terreno-struttura, confronto Ed <= Cd) |

Calcolo deterministico con `tasks/lib/cedimento_edometrico.py` (15 test in `tasks/lib/test_cedimento_edometrico.py`):

```bash
python3 tasks/lib/cedimento_edometrico.py --h0 2 --e0 0.8 --cc 0.30 --cr 0.05 \
  --sigma0 100 --sigmap 150 --dsigma 200
# -> S = 110,1 mm, eq. [7-4], OCR = 1,5
```

## Fonti consultate

- **DM 17/01/2018 (NTC 2018)**, GU n. 42 del 20/02/2018 - § 6.2.4.3 + cap. 12
- **Circolare MIT n. 7 del 21/01/2019**, GU n. 35 dell'11/02/2019 - C6.2
- **FHWA NHI-06-088** (U.S. DOT, dicembre 2006) - par. 7.5.2 e 5.4.6.1 - pubblico dominio, "No restrictions"

Dettaglio (URL, SHA256, trascrizioni) in [`references/sources.yaml`](references/sources.yaml), `references/fonti/`, `references/estratti/`.

## Limiti noti

- Solo cedimento **primario** di consolidazione (no immediato, no secondario/creep, no tempi di consolidazione)
- Solo compressione monodimensionale; delta_sigma' e sigma_p' sono input del progettista
- Caso OC con sigma_f <= sigma_p **non coperto** (le eq. FHWA trascritte valgono per pf > pc): rifiutato
- OCR < 1 accettato solo con dichiarazione esplicita di sottoconsolidazione reale (eq. [7-6])
- Correlazioni per Cc citate solo come sanity check ("should not be used for final design", FHWA 5.4.6.1)
- Non valuta cedimenti differenziali, distorsioni, tilt; non verifica Ed <= Cd (il limite Cd e' del progetto)

**La skill non sostituisce la relazione geotecnica firmata dal progettista.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
