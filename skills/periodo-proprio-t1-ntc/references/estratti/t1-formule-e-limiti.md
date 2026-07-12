# Stima del periodo proprio T1: formule e limiti di applicabilita' (NTC 2018 par. 7.3.3.2 + Circ. 7/2019 par. C7.3.3.2)

> Estratto curato. Fonti (trascritte in `references/fonti/`):
> - `ntc2018-dm-17-01-2018.md` (par. 7.3.3.2, [7.3.6], [7.3.7]; par. 2.5.3, [2.5.7])
> - `circ-7-2019-mit.md` (par. C7.3.3.2, [C7.3.2] e nota 9)
>
> Ogni affermazione seguente e' parafrasi dei passaggi trascritti nei file sopra.

## 1. Le due formule di stima e la loro gerarchia

| Formula | Fonte | Espressione | Input | Status |
|---|---|---|---|---|
| [7.3.6] | NTC 2018 par. 7.3.3.2 | T1 = 2 * sqrt(d) | d = spostamento laterale elastico del punto piu' alto dell'edificio [m], dovuto alla combinazione [2.5.7] applicata in direzione orizzontale | stima di norma, "in assenza di calcoli piu' dettagliati" |
| [C7.3.2] | Circ. 7/2019 par. C7.3.3.2 | T1 = C1 * H^(3/4) | H = altezza della costruzione dal piano di fondazione [m]; C1 da tipologia | "in via di prima approssimazione" |

Gerarchia dichiarata dalla Circolare (C7.3.3.2): la [7.3.6] "porta in conto,
in maniera indiretta, l'effettiva rigidezza laterale della struttura e
risulta, pertanto, piu' affidabile rispetto ad altre formulazioni piu'
semplici, basate unicamente sul numero di piani o sull'altezza complessiva
della costruzione, ma richiede necessariamente un modello di calcolo e
un'analisi statica specifica". La [C7.3.2] e' quindi la stima di primo
livello quando non si dispone ancora di un modello; la [7.3.6] la stima di
norma quando si dispone dello spostamento d.

## 2. Coefficienti C1 della [C7.3.2] (Circ. C7.3.3.2)

| Tipologia strutturale | C1 |
|---|---|
| Telaio di acciaio | 0,085 |
| Telaio di legno | 0,085 |
| Telaio di calcestruzzo armato | 0,075 |
| Muratura o qualsiasi altro tipo di struttura | 0,050 |

H e' misurata "dal piano di fondazione", in metri.

## 3. Limiti di applicabilita' della stima [7.3.6] (NTC 7.3.3.2)

- costruzioni civili o industriali di **altezza non superiore a 40 m**;
- **massa distribuita in modo approssimativamente uniforme** lungo l'altezza;
- d dovuto alla **combinazione [2.5.7]**: G1 + G2 + somma_j(psi_2j * Qkj)
  (le masse gravitazionali associate all'azione sismica, par. 2.5.3),
  applicata come sistema di forze orizzontali.

La Circolare (nota 9) non enuncia limiti dimensionali propri per la
[C7.3.2]; la colloca pero' nello stesso contesto (stima approssimata di T1
per l'analisi lineare statica): l'uso fuori da quel contesto va motivato
dal progettista.

## 4. A cosa serve T1 nell'analisi lineare statica (contesto)

- **Condizioni d'uso dell'analisi lineare statica** (NTC 7.3.3.2): T1 non
  superiore a 2,5*TC o TD, e costruzione regolare in altezza. TC e TD sono i
  periodi dello spettro (par. 3.2.3.2, fuori ambito di questa skill: vedere
  la skill `spettro-risposta-ntc`).
- **Forze statiche equivalenti** [7.3.7]: Fh = Sd(T1)*W*lambda/g,
  distribuite come Fi = Fh*(zi*Wi)/somma_j(zj*Wj), con **lambda = 0,85** se
  T1 < 2*TC e la costruzione ha almeno tre orizzontamenti, **lambda = 1,0**
  in tutti gli altri casi.
- La nota 9 della Circolare descrive l'analisi lineare statica come analisi
  dinamica semplificata a un solo modo (spostamenti linearmente crescenti
  con l'altezza, nessuna combinazione modale).

## 5. Cosa le fonti NON dicono (limiti per la skill)

- Ne' le NTC ne' la Circolare forniscono, in questi paragrafi, formule per
  T1 basate sul **numero di piani**: la Circolare menziona l'esistenza in
  letteratura di formulazioni "basate unicamente sul numero di piani" solo
  per dire che la [7.3.6] e' piu' affidabile. La skill non implementa
  formule da letteratura.
- I paragrafi trascritti non trattano la stima di T1 per **edifici
  esistenti** (cap. 8 NTC) ne' per i **ponti**: fuori ambito.
- Il valore di TC dipende dal sito (pericolosita' sismica): la skill accetta
  TC come input opzionale ma non lo calcola (rinvio alla skill
  `spettro-risposta-ntc`).
