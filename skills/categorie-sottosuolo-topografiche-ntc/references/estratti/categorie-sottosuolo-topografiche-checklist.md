# Checklist - Categorie di sottosuolo e condizioni topografiche (NTC 2018 par. 3.2.2)

> Parafrasi operativa del par. 3.2.2 delle NTC 2018, ancorata alla trascrizione verbatim in
> `../fonti/ntc2018-par-3-2-2.md` (PDF GU S.O. n. 8 alla G.U. n. 42 del 20/02/2018, SHA256 `dda1e397...`).
> Ogni voce rinvia al paragrafo/tabella/formula della fonte. La skill e' un **supporto documentale**: non calcola
> lo spettro ne' i coefficienti di amplificazione (par. 3.2.3), ne' esegue analisi di risposta locale (par.
> 7.11.3).

## Sezione 1 - Categorie di sottosuolo (par. 3.2.2, Tab. 3.2.II)

- [ ] **Approccio** (§3.2.2): la risposta sismica locale si valuta con **specifiche analisi** (§7.11.3) oppure, se
      le condizioni sono chiaramente riconducibili alla Tab. 3.2.II, con l'**approccio semplificato** basato sulle
      onde di taglio VS. I VS/parametri sono parte della **caratterizzazione geotecnica** (§6.2.2).
- [ ] **Velocita' equivalente** (§3.2.2): **VS,eq = H / Σ(hi/VS,i)** [3.2.1], con hi spessore dello strato i, VS,i
      velocita' dello strato i, N numero di strati, H profondita' del **substrato** (formazione con **VS ≥ 800
      m/s**). Formula verificata sull'immagine.
- [ ] **Piano di riferimento del substrato** (§3.2.2): **fondazioni superficiali** -> piano di imposta;
      **fondazioni su pali** -> testa dei pali; **opere di sostegno di terreni naturali** -> testa dell'opera;
      **muri di terrapieni** -> piano di imposta della fondazione.
- [ ] **Regola dei 30 m** (§3.2.2): per **H > 30 m** si usa **VS,30** (si pone H = 30 m nella [3.2.1] e si
      considerano gli strati fino a 30 m).
- [ ] **Categorie** (Tab. 3.2.II): **A** VS > 800 m/s (eventuale copertura scadente di spessore ≤ 3 m); **B**
      VS,eq **360-800**; **C** VS,eq **180-360** con substrato **> 30 m**; **D** VS,eq **100-180** con substrato
      **> 30 m**; **E** riconducibile a **C o D** ma con substrato **≤ 30 m**.
- [ ] **Non classificabile** (§3.2.2): per sottosuoli non riconducibili a queste categorie -> **analisi di
      risposta locale** (§7.11.3).

## Sezione 2 - Condizioni topografiche (par. 3.2.2, Tab. 3.2.III)

- [ ] **Approccio** (§3.2.2): condizioni topografiche **complesse** -> analisi di risposta locale; per
      configurazioni **semplici** si adotta la classificazione della Tab. 3.2.III.
- [ ] **Categorie** (Tab. 3.2.III): **T1** superficie pianeggiante / pendii e rilievi isolati con **i ≤ 15°**;
      **T2** pendii con **i > 15°**; **T3** rilievi con larghezza in cresta molto minore che alla base e
      **15° ≤ i ≤ 30°**; **T4** rilievi (cresta stretta) con **i > 30°**. Operatori verificati sull'immagine.
- [ ] **Ambito di applicazione** (§3.2.2): configurazioni prevalentemente **bidimensionali** (creste/dorsali
      allungate); le categorie topografiche si considerano nella definizione dell'azione sismica **se l'altezza e'
      maggiore di 30 m**.

## Cosa la skill NON fa

- [ ] Non **calcola** lo **spettro** ne' i **coefficienti di amplificazione** stratigrafica SS/CC e topografica ST
      (§3.2.3.2): a valle usa `spettro-risposta-ntc`.
- [ ] Non esegue le **analisi di risposta sismica locale** (§7.11.3) ne' la **caratterizzazione geotecnica** del
      volume significativo (§6.2.2).
- [ ] Non sostituisce il **geologo/geotecnico** ne' la lettura diretta del par. 3.2.2 delle NTC 2018.
