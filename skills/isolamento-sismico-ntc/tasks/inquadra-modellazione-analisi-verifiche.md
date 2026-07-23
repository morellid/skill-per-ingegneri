# Task: inquadra-modellazione-analisi-verifiche

Inquadra la **modellazione**, i **metodi di analisi** e le **verifiche SLE/SLV/SLC** delle costruzioni con
isolamento sismico secondo le **NTC 2018 par. 7.10.5-7.10.8**. Supporto documentale: **non** esegue l'analisi.

## Quando usarla

Il progettista deve scegliere il modello e il metodo di analisi della struttura isolata e impostare le verifiche.
Per scopo, requisiti e dispositivi usa `inquadra-scopo-requisiti-dispositivi`.

## Passi

1. **Proprietà del sistema** (§7.10.5.1): adottare i valori **più sfavorevoli** nel periodo di riferimento VR
   (deformazioni, variabilità di fornitura, velocità **±30%**, carichi verticali, temperatura, invecchiamento); si
   eseguono **più analisi per ciascuno stato limite**; se i valori estremi differiscono di **non più del 20%** dal
   valor medio si possono usare i **valori medi**.
2. **Modellazione** (§7.10.5.2): sovrastruttura e sottostruttura **elastiche lineari**; sistema di isolamento
   **visco-elastico lineare** o **non lineare**. La **deformabilità verticale** va messa in conto se **KV/Kesi <
   800**. Se rigidezza/smorzamento dipendono dallo spostamento, **procedura iterativa** fino a differenza **< 5%**.
   Il comportamento è modellabile come **lineare equivalente** se: (a) rigidezza equivalente **≥ 50%** della secante
   al **20%** dello spostamento di riferimento; (b) smorzamento **< 30%**; (c) variazione forza-spostamento **< 10%**
   (per ±30% velocità); (d) incremento forza tra 0,5 dc e ddc **≥ 2,5% del peso** della sovrastruttura.
3. **Metodi di analisi** (§7.10.5.3): si applicano i §7.3.3-7.3.4; **NON** è ammessa l'**analisi statica non
   lineare** (push-over).
   - **statica lineare** (§7.10.5.3.1) applicabile se: sistema modellabile lineare; **Tis ∈ [3·Tbf, 3,0 s]**;
     **KV ≥ 800·Kesi**; **TV = 2π√(M/KV) < 0,1 s**; nessun isolatore in trazione; **regolare in pianta**. Per gli
     **edifici**: sovrastruttura **≤ 20 m e ≤ 5 piani**; sottostruttura **T ≤ 0,05 s**; **pianta < 50 m**;
     eccentricità **≤ 3%**;
   - **dinamica lineare** (§7.10.5.3.2): modale con spettro o integrazione al passo; **spettro ridotto per T ≥
     0,8·Tis** (η da ξesi); componente **verticale** anche quando KV/Kesi < 800.
4. **Verifiche** (§7.10.6):
   - **SLE/SLD** (§7.10.6.1): la protezione di sottostruttura/fondazioni allo SLD si ritiene conseguita se sono
     soddisfatte le verifiche allo **SLV**; per la **sovrastruttura**, gli **spostamenti d'interpiano** devono
     essere **< 2/3 dei limiti SLD del §7.3.6.1**; i dispositivi non devono subire danni in servizio;
   - **SLV** (§7.10.6.2.1): capacità con **γM delle costruzioni non isolate**; se la sottostruttura è infinitamente
     rigida (**T < 0,05 s**) le forze d'inerzia sono **masse × agS**; domanda con **q ≤ 1,50 (edifici)** / **q = 1
     (ponti)**; parti dei dispositivi non dissipative in campo elastico con **coefficiente di sicurezza ≥ 1,5**;
   - **SLC** (§7.10.6.2.2): i dispositivi sostengono **senza rotture** gli spostamenti **d2** (azione SLC); per
     sistemi non lineari si aggiunge il **maggiore tra spostamento residuo SLD e 50%** dello spostamento
     all'annullamento della forza.
5. **Manutenzione e collaudo** (§7.10.7-7.10.8): **piano di manutenzione**, **sostituibilità** (martinetti),
   **accessibilità** per l'ispezione; accorgimenti specifici in fase di **collaudo**.

Usa la checklist in `../references/estratti/isolamento-sismico-checklist.md` (sezioni 2, 3 e 4).

## Output atteso

Un inquadramento che indichi il modello (condizioni del lineare equivalente), il metodo di analisi applicabile
(statica/dinamica lineare, no push-over) con i requisiti, e le verifiche SLD/SLV/SLC con le relative soglie
(interpiano < 2/3, q≤1,50/1, coeff. sicurezza ≥1,5, spostamenti d2 allo SLC), con **rinvio ai paragrafi** NTC.
Nessun calcolo.

## Cosa NON fare

- Non **eseguire** l'analisi né le verifiche; non calcolare Tis, Kesi, spostamenti o forze (formule [7.10.1]-[7.10.5]).
- Non progettare i **dispositivi** (§11.9).
