# Task: inquadra-obblighi

Determina, per il trasporto di rifiuti, l'obbligo del formulario (art. 193) e
dell'iscrizione all'Albo nazionale gestori ambientali (art. 212), incluse le
semplificazioni.

## Input richiesto

- Soggetto: **produttore/detentore** dei rifiuti, **trasportatore in conto
  terzi** o **produttore che trasporta i propri rifiuti**?
- Natura del rifiuto: **pericoloso** o **non pericoloso** (codice EER se noto).
- Quantita' trasportata al giorno (per la soglia dei propri rifiuti pericolosi).
- Tipo di trasporto: rifiuti urbani ai centri di raccolta? spedizione
  transfrontaliera?

## Procedura

1. **Formulario - FIR (art. 193)**:
   - **Obbligo** (c. 1): il trasporto di rifiuti eseguito da enti o imprese e'
     accompagnato dal **FIR**.
   - **Esclusioni** (c. 7-8): **rifiuti urbani** ai centri di raccolta dal
     **produttore iniziale**; determinati **rifiuti speciali** individuati dalla
     norma. **Transfrontalieri** (c. 9): documentazione del Reg. (CE) 1013/2006.
   - **Pericolosi** (c. 6): imballaggio ed etichettatura secondo le norme vigenti
     (ADR su strada).

2. **Iscrizione all'Albo (art. 212)**:
   - **Regola** (c. 5): l'**iscrizione all'Albo** e' **requisito** per svolgere
     **raccolta e trasporto di rifiuti** (categorie e classi, garanzie
     finanziarie).
   - **Semplificazione per i propri rifiuti** (c. 8): i **produttori iniziali di
     rifiuti non pericolosi** che trasportano i **propri rifiuti**, e i
     **produttori iniziali di rifiuti pericolosi** che trasportano i propri fino a
     **30 kg / 30 litri al giorno**, **non sono soggetti** ai commi 5-7 se
     l'operazione e' **parte integrante e accessoria** dell'impresa; **non
     prestano garanzie** e sono **iscritti con procedura semplificata**.
   - **La skill non stabilisce categorie/classi**: rinvia all'Albo.

## Output

- Obbligo del FIR sì/no (con esclusioni), citando l'art. 193.
- Regime dell'Albo: iscrizione ordinaria (c. 5) o **semplificata** per i propri
  rifiuti (c. 8), con la soglia 30 kg/30 l per i pericolosi.
- Avvertenza: la classificazione del rifiuto (EER) e le categorie/classi vanno
  verificate con il gestore/Albo.

## Regole

- Distinguere il **trasporto in conto terzi** (Albo ordinario) dal **trasporto
  dei propri rifiuti** (semplificazione art. 212 c. 8).
- Non classificare il rifiuto ne' stabilire categorie/classi: rinviare.
- Citare l'articolo (193, 212).
