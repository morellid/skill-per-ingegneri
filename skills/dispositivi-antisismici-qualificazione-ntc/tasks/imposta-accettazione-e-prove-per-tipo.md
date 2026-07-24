# Task — Imposta l'accettazione e le prove per tipo dei dispositivi antisismici (NTC 2018 §11.9.3-11.9.10)

Supporto documentale per impostare, dal lato del **Direttore dei Lavori**, i **controlli di accettazione in cantiere**
dei dispositivi antisismici (§11.9.3) e le **prove/limiti prestazionali per tipo** (§11.9.4-11.9.10) secondo le NTC
2018 (DM 17/1/2018). **Non** esegue il progetto né dimensiona i dispositivi.

Fonte: `../references/fonti/ntc2018-par-11-9.md`; checklist: `../references/estratti/dispositivi-antisismici-checklist.md`.

## Input tipico

- Tipologia del dispositivo (isolatore elastomerico/a scorrimento, dissipatore lineare/non lineare/viscoso, vincolo
  a fusibile/provvisorio) e numero di dispositivi da mettere in opera.
- Documentazione di qualificazione (UNI EN 15129 + CE, o CVT) e disponibilità di un laboratorio ex art. 59.

## Passi

1. **Procedura di accettazione (§11.9.3)**
   - Ricorda che i controlli di accettazione sono **obbligatori per tutte le tipologie** e **demandati al Direttore
     dei Lavori**, che prima della messa in opera **accerta la documentazione di qualificazione**, effettua la
     **verifica geometrica e delle tolleranze dimensionali** e **rifiuta le forniture non conformi**.
   - Il **campionamento** dei dispositivi va effettuato **sui lotti destinati allo specifico cantiere, dal Direttore
     dei Lavori**; le prove sono **eseguite e certificate da un laboratorio ex art. 59 DPR 380/2001**, con
     certificati che indicano il/i cantiere/i. Riferimento alle prove di **Controllo di Produzione in Fabbrica (FPC)**.

2. **Numerosità delle prove per ogni tipo (§§11.9.4.1, 11.9.6.1-11.9.10.1)**
   - **Almeno il 20% dei dispositivi, comunque non meno di 4** e non più del numero da mettere in opera.
   - Per **lineari/non lineari**: su **almeno un dispositivo** prova **«quasi statica»** con **≥ 5 cicli** completi
     alternati, ampiezza **±d2**.

3. **Limiti prestazionali per tipo (variazioni al 3° ciclo)**
   - **Lineari** (§11.9.4): **ξe < 15%** [11.9.1]; **|Ke−Kin|/Kin < 20%** [11.9.2]; stabilità **≤ 10%**;
     **Tab. 11.9.I** (Ke ±15/±20/±40/±10 %; ξe ±15/±15/±15/±10 %).
   - **Non lineari** (§11.9.5): del = d2/20; **Tab. 11.9.II** (K2 ±15/±20/±20/±10 %; Ksec ±15/±20/±40/±10 %; ξe
     ±10/±15/±15/±10 %); se **K2/K1 ≤ 0,05** → variazione K2/K1 **< 0,01**.
   - **Viscosi** (§11.9.6): **|Ed(i)−Ed(3)|/Ed(3) ≤ 10%**; **Tab. 11.9.III** (Fmax ±15/±5/±5/±10 %; Ed
     −15/−5/−5/±10 %); **γv = (1+td)·(1,5)^α**; rotazione cerniere **≥ 2°**, forza trasversale **≥ 2× peso proprio**.
   - **Isolatori elastomerici** (§11.9.7): piastre **allungamento 18%**, spessore **2 mm interne / 20 mm esterne**;
     **Tab. 11.9.IV** (Ke ±20 %; Kv −30 %; ξe ±20 %); frequenze **0,1 e 0,5 Hz**; carico verticale **≤ 15%**.
   - **Isolatori a scorrimento** (§11.9.8): sotto d2 **≥ 5 cicli**; attrito **|f(i)−f(3)|/f(3) ≤ 0,25**; se incremento
     forza tra 0,5 ddc e ddc **< 1,25% del peso** → appoggio fino a **1,25 d2**.
   - **A fusibile** (§11.9.9): risultati entro **±10%**; geometria **±10% spessori / ±5% lunghezze**; **≥ 3 cicli
     monotonici** a carico di servizio (+10%); forza di rilascio **±15%**.
   - **Vincolo provvisorio** (§11.9.10): corsa **≥ ±50 mm ponti / ±25 mm edifici**; FS sovrappressioni **1,5** (o
     **≥ 1,1** con protezione incorporata); velocità attivazione **0,5–5 mm/s**; prova sovrappressione a) carico di
     progetto **< 0,5 s** mantenuto **≥ 5 s**, b) inversione **< 1 s** mantenuta **≥ 5 s**.

4. **Output**: piano di accettazione (chi campiona, quale laboratorio, quanti dispositivi, quali prove per il tipo
   dato) con i limiti prestazionali della/e tabella/e pertinente/i ed esito accettazione/rifiuto.

## Cosa NON fare

- Non **progettare/dimensionare** i dispositivi (§7.10, → skill `isolamento-sismico-ntc`).
- Non confondere le **prove di accettazione** (in cantiere, sui lotti del cantiere) con le **prove di qualificazione**
  (sul tipo, in fase di immissione sul mercato).
- Non inventare numerosità/tolleranze: ogni valore deve essere rintracciabile in
  `../references/fonti/ntc2018-par-11-9.md`.
