# Note - Caso problematico: quota a_s > 1500 m

## Perche' e' un caso problematico

- L'altitudine del sito (2000 m) e' fuori dal dominio di validita' della formula della velocita' di riferimento del vento (NTC par. 3.3.2: `a_s <= 1500 m`).
- Il modulo Python rifiuta correttamente il calcolo del vento sollevando ValueError.
- Il calcolo della neve e' eseguito perche' la zona I-Alpina non ha limite superiore di altitudine.

## Cosa la skill deve fare

1. **Vento**: riportare il messaggio bloccante del modulo. Spiegare che NTC par. 3.3.2 richiede indagine specifica per `a_s > 1500 m`. Suggerire studio meteo-eolico locale e rinvio al progettista strutturale.
2. **Neve**: eseguire il calcolo e riportarlo. Segnalare che il valore di `q_sk` e' elevato ma corretto a 2000 m (formula par. 3.4.2). Avvertire che gli accumuli (par. 3.4.5.5) sono fuori scope.
3. **Concludere** con rinvio al progettista per entrambi.

## Anti-pattern da NON commettere

- **Non aggirare l'errore del modulo** modificando l'input (per esempio "uso a_s = 1500 m approssimando"): e' una manipolazione che invalida il calcolo. La skill deve rispettare il dominio di validita' della norma.
- **Non inventare un valore di v_b in quota** estrapolando la formula 3.3.2 a 2000 m: la formula e' definita su `[0, 1500]`. Estrapolare e' fabbricazione.
- **Non eseguire il calcolo della neve in modo "completo"** ignorando gli accumuli: a 2000 m gli accumuli sono spesso preponderanti rispetto a `mu_1 * q_sk`. Va segnalato esplicitamente che la skill non li copre.
- **Non confondere "a_s > 1500" del vento con "a_s > 200" della neve**: sono due soglie diverse, nelle rispettive sezioni NTC.

## Test corrispondente

I test in `tasks/lib/test_carichi_atmosferici.py`:
- `TestVelocitaRiferimento.test_quota_oltre_1500_solleva` verifica che il modulo Python sollevi ValueError per `a_s > 1500`.
- `TestQskZone.test_oltre_200m_cresce` verifica che `q_sk` cresca con l'altitudine sopra 200 m (comportamento atteso).
