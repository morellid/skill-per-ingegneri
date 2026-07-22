# Output atteso

Inquadramento documentale secondo le **NTC 2018 (D.M. 17 gennaio 2018), par. 2.4**. Nessun calcolo di spettro o
periodi di ritorno.

## 1. Vita nominale di progetto V_N (§2.4.1, Tab. 2.4.I)

Un edificio residenziale ordinario è una **costruzione con livelli di prestazioni ordinari** (tipo 2 della Tab.
2.4.I): il valore **minimo** di vita nominale di progetto è

> **V_N = 50 anni**

È un valore minimo: il progettista può adottarne uno superiore. I valori di V_N possono servire anche per definire
le azioni dipendenti dal tempo (§2.4.1).

## 2. Classe d'uso (§2.4.2)

Un edificio residenziale prevede **normali affollamenti**, senza contenuti pericolosi per l'ambiente e senza
funzioni pubbliche o sociali essenziali: ricade in

> **Classe II**

(La Classe I è riservata a costruzioni con presenza solo occasionale di persone o edifici agricoli; la Classe III
agli affollamenti significativi; la Classe IV alle funzioni pubbliche/strategiche importanti.)

## 3. Periodo di riferimento V_R (§2.4.3, formula [2.4.1], Tab. 2.4.II)

Il periodo di riferimento per l'azione sismica è il prodotto della vita nominale per il coefficiente d'uso:

> **V_R = V_N · C_U**   [2.4.1]

Per la **Classe II** il coefficiente d'uso è **C_U = 1,0** (Tab. 2.4.II), quindi:

> **V_R = 50 · 1,0 = 50 anni**

## 4. Uso a valle (rinvio §3.2)

V_R è il periodo di riferimento da cui, tramite le probabilità di superamento di ciascuno stato limite, si
ricavano i **periodi di ritorno T_R** dell'azione sismica e lo **spettro di risposta**: questo passaggio è
trattato nel **§3.2** (skill `spettro-risposta-ntc`) e non da questa skill.

## Riferimenti

- NTC 2018 §2.4.1 e Tab. 2.4.I - vita nominale di progetto V_N (50 anni per prestazioni ordinarie);
- NTC 2018 §2.4.2 - classi d'uso (Classe II: normali affollamenti);
- NTC 2018 §2.4.3, formula [2.4.1] e Tab. 2.4.II - V_R = V_N · C_U, C_U = 1,0 per la Classe II.

**Questo output è un supporto documentale e non sostituisce il progettista né la lettura diretta del par. 2.4
delle NTC 2018.**
