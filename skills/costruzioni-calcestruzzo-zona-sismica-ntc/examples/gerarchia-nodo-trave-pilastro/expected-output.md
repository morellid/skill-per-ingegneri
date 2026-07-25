# Output atteso — Gerarchia delle resistenze al nodo trave-pilastro (NTC 2018 §7.4.4)

> Supporto documentale: inquadra la catena della gerarchia delle resistenze. **Non** esegue le verifiche numeriche
> complete né i dettagli costruttivi (§7.4.6).

## 1. Fattore di sovraresistenza (§7.4.4)

- I **fattori di sovraresistenza γRd** da usare nelle verifiche di progettazione in capacità sono nella **Tab. 7.2.I**
  (dipendono dalla classe di duttilità e dal tipo di verifica). → Si prende γRd da questa tabella.

## 2. Nodo pilastro forte-trave debole (§7.4.4.2)

- Per ogni nodo trave-pilastro (**escluso** la sommità dei pilastri dell'**ultimo orizzontamento**), la capacità a
  flessione complessiva dei **pilastri** deve superare quella delle **travi** amplificata di γRd:

  **ΣMc,Rd ≥ γRd · ΣMb,Rd**  [7.4.4]

  dove Mc,Rd è la capacità a flessione del pilastro (per i livelli di sforzo assiale delle combinazioni sismiche) e
  Mb,Rd quella della trave convergente nel nodo.
- Questa condizione garantisce che le plasticizzazioni si formino nelle **travi** e non nei **pilastri** (meccanismo
  duttile «trave debole»).

## 3. Taglio di progetto della trave (§7.4.4.1)

- La **domanda a taglio** della trave si ottiene dall'**equilibrio della trave incernierata agli estremi**, soggetta ai
  **carichi gravitazionali** e all'azione delle **capacità flessionali di progetto** nelle sezioni di plasticizzazione
  (estremità), **amplificate del fattore γRd** (Tab. 7.2.I).
- Essendo la struttura in **CD"A"**: nelle zone dissipative ctgθ = 1; se il rapporto tra domande a taglio min/max è
  **< −0,5** e il maggiore valore assoluto supera **VR1 = (2 − |VEd,min|/VEd,max)·fctd·bw·d** [7.4.1], si dispongono
  **armature diagonali a ±45°** con la capacità affidata per metà alle staffe e per metà alle inclinate
  (**VEd,max ≤ As·fyd/√2** [7.4.2]).

## 4. Limite di compressione del pilastro (§7.4.4.2)

- Per la **pressoflessione** dei pilastri, la **domanda a compressione** non deve eccedere il **55% (CD"A")** [65% in
  CD"B"] della capacità massima a compressione della sezione di **solo calcestruzzo**, per tutte le combinazioni.
- → In CD"A" il limite è **55%**.

## 5. Sintesi della catena gerarchica

| Passo | Regola | Rif. |
|---|---|---|
| Flessione trave | capacità come §4.1.2.3.4 (armature effettive + soletta collaborante) | §7.4.4.1 |
| Taglio trave | domanda da capacità flessionale **amplificata di γRd** | §7.4.4.1 |
| Nodo | **ΣMc,Rd ≥ γRd·ΣMb,Rd** (pilastro forte-trave debole) | [7.4.4] |
| Compressione pilastro (CD"A") | domanda ≤ **55%** capacità del solo cls | §7.4.4.2 |
| Taglio pilastro | da gerarchia (momenti resistenti estremità × γRd) | §7.4.4.2 |

**Fuori scope**: valori numerici completi delle verifiche, dettagli costruttivi (§7.4.6), scelta della tipologia/q
(task `inquadra-tipologie-e-fattore-comportamento`).

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 7.4 delle NTC 2018 e della relativa Circolare applicativa 2019.**
