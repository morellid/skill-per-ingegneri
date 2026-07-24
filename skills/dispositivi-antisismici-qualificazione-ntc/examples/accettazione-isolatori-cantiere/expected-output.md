# Output atteso — Accettazione in cantiere di isolatori elastomerici (NTC 2018 §11.9.3, §11.9.7)

> Supporto documentale: inquadra la procedura di accettazione e i limiti per gli isolatori elastomerici. **Non**
> esegue il progetto dell'isolamento (§7.10).

## 1. Chi accetta e come si campiona (§11.9.3)

- I controlli di accettazione sono **obbligatori** e **demandati al Direttore dei Lavori**, che prima della messa in
  opera accerta la **documentazione di qualificazione** (UNI EN 15129 + Marcatura CE), effettua la **verifica
  geometrica e delle tolleranze** e **rifiuta le forniture non conformi**.
- Le prove di Controllo di Produzione in Fabbrica possono essere impiegate ai fini dell'accettazione **solo se**: il
  **campionamento** è stato effettuato **sui lotti destinati a questo cantiere, dal Direttore dei Lavori**; le prove
  sono **eseguite e certificate da un laboratorio ex art. 59 DPR 380/2001**; i certificati riportano esplicitamente
  il cantiere. → La proposta del fabbricante di far valere prove FPC su **un lotto generico non campionato dal DL**
  **non è accettabile**: il campionamento deve avvenire sui lotti del cantiere a cura del Direttore dei Lavori.

## 2. Numerosità delle prove (§11.9.7.1)

- **Almeno il 20% dei dispositivi, comunque non meno di 4** e non più del numero da mettere in opera.
- Su **28 isolatori**: 20% = 5,6 → **almeno 6 dispositivi** (≥ 20% e ≥ 4).

## 3. Limiti prestazionali per gli isolatori elastomerici (§11.9.7)

- Le **piastre di acciaio**: **allungamento minimo a rottura 18%**, spessore minimo **2 mm** (interne) e **20 mm**
  (esterne).
- Parametri sintetici: **Ke = F/d** (= Gdin·A/te), **ξe = Ed/(2π·F·d)**, rigidezza verticale **Kv = Fv/dv**; fattori
  di forma **S1 = A'/L**, **S2 = D/te**.
- Massime differenze in **Tab. 11.9.IV** (variazioni al 3° ciclo; frequenze di prova **0,1 Hz e 0,5 Hz**):

| | Fornitura | Invecchiamento | Temperatura | Frequenza di prova |
|---|---|---|---|---|
| Ke | ±20% | ±20% | ±20% | ±20% |
| Kv | −30% | - | - | - |
| ξe | ±20% | ±20% | ±20% | ±20% |

- Le variazioni dovute al **carico verticale** (differenza tra carico verticale massimo e minimo) non devono superare
  il **15%** del valore di progetto.

## 4. Esito

| Aspetto | Esito |
|---|---|
| Documentazione (§11.9.2/11.9.3) | UNI EN 15129 + CE presenti → verificare |
| Campionamento (§11.9.3) | Deve essere fatto dal **DL sui lotti del cantiere** → proposta FPC su lotto generico **non accettabile** |
| Numerosità prove (§11.9.7.1) | **≥ 6 dispositivi** (20% di 28, comunque ≥ 4) |
| Laboratorio | **Art. 59 DPR 380/2001**, certificati con indicazione del cantiere |
| Limiti (§11.9.7) | Piastre 18% e 2/20 mm; Tab. 11.9.IV; carico verticale ≤ 15% |

**Fuori scope**: progetto e dimensionamento dell'isolamento (§7.10, → skill `isolamento-sismico-ntc`); accettazione
generale di cls/acciaio (§§11.2/11.3).

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.9 delle NTC 2018, della UNI EN 15129 e della relativa Circolare applicativa.**
