# Output atteso - Caso problematico: quota a_s > 1500 m

## Pressione vento (NTC par. 3.3) - RIFIUTATO

La skill deve **rifiutare** il calcolo del vento. Il modulo Python ritorna codice di errore 2 e stampa su stderr:

```
ERRORE: a_s > 1500 m: NTC par. 3.3.2 richiede indagine specifica, fuori scope skill
```

Risposta attesa dell'agent:

> Il sito si trova a 2000 m s.l.m. Il dominio di validita' di NTC par. 3.3.2 (formula della velocita' di riferimento `v_b`) si estende fino a 1500 m; per altitudini superiori la norma rinvia a indagini specifiche (anemometri locali, studio del profilo di vento in quota). La skill non esegue il calcolo. Va commissionato uno studio meteo-eolico al sito o consultata la regione/ente locale per dati di vento misurati in quota; il progettista strutturale firmatario decide come procedere.

## Carico neve (NTC par. 3.4) - ESEGUITO

NTC par. 3.4 non pone un limite superiore di altitudine, quindi la skill esegue il calcolo.

### Input riportati
- Zona: `I-Alpina`, `a_s = 2000 m`
- `alpha = 30 deg`, classe esposizione: `battuta_dai_venti`, `c_t = 1.0`

### Valori intermedi
- `q_sk = 11.881 kN/m^2` (par. 3.4.2 NTC zona I-Alpina, a_s = 2000 > 200 -> q_sk = 1.39 * [1 + (2000/728)^2])
- `mu_1 = 0.8` (par. 3.4.5.2.1 NTC, alpha = 30 al limite della prima fascia)
- `c_E = 0.9` (Tab. 3.4.I, classe battuta dai venti)

### Output
- **q_s = 8.554 kN/m^2** (eq. 3.4.1 NTC: q_s = mu_1 * q_sk * c_E * c_t)

### Note
- Il valore `q_sk = 11.88 kN/m^2` e' molto elevato perche' a quota 2000 m la formula della zona I-Alpina cresce quadraticamente (e' il comportamento corretto della norma).
- A quote estreme il progettista deve comunque considerare carichi di accumulo aggiuntivi (par. 3.4.5.5 NTC e Circolare C3.4) **non coperti dalla skill**.
- Verifica del progettista strutturale firmatario obbligatoria.

## Comportamento atteso dell'agent

1. Per il vento: riportare il messaggio bloccante senza tentare workaround (per esempio NON arrotondare `a_s` a 1499 m per far passare il calcolo).
2. Per la neve: eseguire il calcolo, riportare i valori e segnalare che `q_sk = 11.88 kN/m^2` e' un valore elevato ma corretto a 2000 m, e che eventuali accumuli (par. 3.4.5.5) restano da valutare separatamente.
