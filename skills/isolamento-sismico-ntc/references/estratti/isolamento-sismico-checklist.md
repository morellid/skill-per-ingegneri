# Checklist - Costruzioni con isolamento sismico (NTC 2018 par. 7.10)

> Parafrasi operativa del par. 7.10 delle NTC 2018, ancorata alla trascrizione verbatim in
> `../fonti/ntc2018-par-7-10.md` (PDF GU S.O. n. 8 alla G.U. n. 42 del 20/02/2018, SHA256 `dda1e397...`). Ogni
> voce rinvia al paragrafo della fonte. La skill e' un **supporto documentale**: non esegue l'analisi/verifiche
> ne' progetta i dispositivi (par. 11.9).

## Sezione 1 - Scopo, requisiti, dispositivi, indicazioni progettuali (par. 7.10.1-7.10.4)

- [ ] **Scopo e strategie** (§7.10.1): sistema d'isolamento **sotto la costruzione**; (a) **allungare il periodo**;
      (b) **limitare la forza** orizzontale; eventuale **dissipazione** di energia.
- [ ] **Interfaccia e parti** (§7.10.2): **interfaccia d'isolamento**; **sottostruttura** (sotto, incl.
      fondazioni); **sovrastruttura** (isolata, sopra).
- [ ] **Campo elastico** (§7.10.2): sovra/sottostruttura in campo **sostanzialmente elastico** - particolari
      costruttivi come per costruzioni con **agS <= 0,075g** (deroga c.a. §7.4.6/§7.9.6).
- [ ] **Affidabilita' del sistema** (§7.10.2-7.10.3): al sistema d'isolamento e' richiesta **affidabilita'
      superiore**; i dispositivi si usano **solo se conformi al §11.9** (caratteristiche e prove).
- [ ] **Dispositivi** (§7.10.4.1): **accesso, ispezionabilita', sostituibilita'**; sistemi di contrasto per il
      **ricentraggio**; protezione da fuoco/attacchi chimici-biologici.
- [ ] **Movimenti indesiderati** (§7.10.4.2): centro di massa e centro di rigidezza **coincidenti**; dispositivi
      **perimetrali** e **staticamente ridondanti**; compressioni uniformi; **V >= 0** (se V < 0, trazione **< min(2G,
      1 MPa)** per elastomerici).
- [ ] **Diaframma rigido** (§7.10.4.3): **sopra e sotto** il sistema di isolamento; elementi verticali con
      spostamento **< 1/20** dello spostamento relativo (in campo elastico).
- [ ] **Spazio libero** (§7.10.4.4): tra sovrastruttura isolata e terreno/costruzioni circostanti, in tutte le
      direzioni.

## Sezione 2 - Modellazione e analisi (par. 7.10.5)

- [ ] **Proprieta'** (§7.10.5.1): valori **piu' sfavorevoli** nel VR; velocita' **±30%**; valori medi se estremi
      entro **20%**.
- [ ] **Modellazione** (§7.10.5.2): sovra/sottostruttura **elastiche lineari** (rigidezza non dissipativa); sistema
      **visco-elastico lineare** o **non lineare**; **deformabilita' verticale se KV/Kesi < 800**; iterazione **<
      5%**.
- [ ] **Modello lineare equivalente** (§7.10.5.2): (a) rigidezza equivalente **>= 50%** della secante al **20%**
      dello spostamento di riferimento; (b) smorzamento **< 30%**; (c) forza-spostamento varia **< 10%** (per ±30%
      velocita'); (d) incremento forza tra 0,5 dc e ddc **>= 2,5% del peso** della sovrastruttura.
- [ ] **Metodi** (§7.10.5.3): si applicano i §7.3.3-7.3.4; **NON** e' ammessa l'**analisi statica non lineare**
      (push-over).
- [ ] **Analisi statica lineare** (§7.10.5.3.1): modellabile lineare; **Tis in [3·Tbf, 3,0 s]**; **KV >= 800·Kesi**;
      **TV = 2π√(M/KV) < 0,1 s**; **no trazione**; **regolare in pianta**; edifici: **<= 20 m e <= 5 piani**;
      sottostruttura **T <= 0,05 s**; **pianta < 50 m**; **eccentricita' <= 3%**.
- [ ] **Analisi dinamica lineare** (§7.10.5.3.2): modale con spettro o integrazione al passo; **spettro ridotto per
      T >= 0,8·Tis** (η da ξesi); componente **verticale** anche se KV/Kesi < 800.

## Sezione 3 - Verifiche (par. 7.10.6)

- [ ] **SLE/SLD** (§7.10.6.1): sottostruttura/fondazioni allo SLD soddisfatte se verificate allo SLV; **SLD
      sovrastruttura**: spostamenti d'interpiano **< 2/3 dei limiti SLD del §7.3.6.1**; dispositivi senza danni in
      servizio.
- [ ] **SLV** (§7.10.6.2.1): **γM come costruzioni non isolate**; sottostruttura rigida se **T < 0,05 s** (forze =
      **M × agS**); **q <= 1,50 (edifici)** / **q = 1 (ponti)**; parti non dissipative dei dispositivi in campo
      elastico con **coefficiente di sicurezza >= 1,5**.
- [ ] **SLC** (§7.10.6.2.2): i dispositivi sostengono **senza rotture** gli spostamenti **d2** (azione SLC); per
      sistemi non lineari **+ maggiore tra spostamento residuo SLD e 50%** dello spostamento all'annullamento della
      forza; connessioni gas/impianti pericolosi con adeguata sicurezza.

## Sezione 4 - Manutenzione, sostituibilita', collaudo (par. 7.10.7-7.10.8)

- [ ] **Piano di manutenzione** (§7.10.7): modalita' di messa in opera, controlli periodici, sostituzione durante
      la vita nominale; **sostituibilita'** (martinetti) e **accessibilita'** per l'ispezione.
- [ ] **Collaudo** (§7.10.8): accorgimenti specifici in fase di collaudo.

## Cosa la skill NON fa

- [ ] Non **esegue** l'analisi ne' le verifiche, non calcola forze/spostamenti (formule [7.10.1]-[7.10.5]).
- [ ] Non **progetta** ne' qualifica i dispositivi di isolamento/dissipazione (§11.9).
- [ ] Non sostituisce il **progettista** ne' la lettura diretta del §7.10 delle NTC 2018.
