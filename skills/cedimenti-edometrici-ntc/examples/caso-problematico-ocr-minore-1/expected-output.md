# Output atteso - caso problematico: OCR < 1 rifiutato di default

## Comando eseguito

```bash
python3 tasks/lib/cedimento_edometrico.py --h0 2 --e0 0.8 --cc 0.30 --cr 0.05 \
  --sigma0 200 --sigmap 100 --dsigma 50
```

## Risultato (JSON del modulo)

```json
{
  "errore": "OCR < 1 (sigma_p < sigma_0): o i dati edometrici sono errati (verificare sigma_p, unita' di misura, scambio di colonne) oppure il terreno e' realmente sottoconsolidato (consolidazione ancora in corso, FHWA 7.5.2.3). In quest'ultimo caso rieseguire dichiarando esplicitamente sottoconsolidato=True (CLI: --sottoconsolidato)."
}
```

Exit code 1.

## Sintesi testuale attesa

La risposta corretta della skill NON e' produrre un numero, ma:

1. **riportare il messaggio bloccante del modulo senza aggirarlo**: OCR = 100/200 = 0,5 < 1;
2. spiegare le due letture possibili, entrambe da chiarire con il progettista:
   - **dati errati** (caso di gran lunga piu' frequente): sigma_p' mal determinata dalla curva edometrica, errore di unita' di misura, scambio di colonne;
   - **terreno realmente sottoconsolidato** (FHWA 7.5.2.3): la consolidazione sotto il carico esistente e' ancora in corso; in tal caso, e SOLO su dichiarazione esplicita e giustificata, si riesegue con `--sottoconsolidato` e il modulo applica l'**eq. [7-6]**, che include anche la consolidazione in corso (ignorarla sottostimerebbe il cedimento totale);
3. NON scegliere autonomamente tra le due letture: la decisione e la giustificazione della sottoconsolidazione sono del **progettista firmatario**.

Un output che calcolasse comunque un cedimento con questi dati, senza il passaggio dichiarativo, sarebbe un output SBAGLIATO per questa skill.
