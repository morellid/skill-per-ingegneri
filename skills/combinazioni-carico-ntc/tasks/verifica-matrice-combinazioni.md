# Verifica matrice combinazioni

## Obiettivo

Controllare una matrice di combinazioni gia' prodotta dall'utente rispetto alle regole NTC 2018 par. 2.5.3 e alle tabelle 2.5.I/2.6.I.

## Input richiesti

- elenco delle azioni originarie con categoria e valori caratteristici;
- matrice da verificare, preferibilmente in tabella con coefficienti per ciascuna azione;
- profilo gamma atteso (`A1`, `A2`, `EQU`);
- indicazione se si vogliono verificare solo coefficienti o anche valori risultanti.

## Procedura

1. Ricostruisci un JSON input equivalente alla situazione dell'utente.
2. Esegui il modulo `tasks/lib/combinazioni.py` per generare la matrice attesa.
3. Confronta:
   - presenza di una combinazione SLU per ogni variabile principale;
   - uso di `psi0` per accompagnatrici SLU e SLE rara;
   - uso di `psi1` per principale in SLE frequente e `psi2` per accompagnatrici;
   - uso di `psi2` per SLE quasi permanente, sismica ed eccezionale;
   - gamma corretti secondo profilo scelto;
   - trattamento di `G2` compiutamente definito.
4. Segnala discrepanze in tabella.

## Output atteso

Usa questa struttura:

```markdown
## Esito
- Stato: conforme / da correggere / non verificabile
- Profilo gamma atteso: A1

## Discrepanze
| Combinazione | Azione | Atteso | Trovato | Riferimento |
|---|---:|---:|---:|---|

## Note
...
```

## Limiti

Se la matrice proviene da software FEM, la skill non interpreta automaticamente convenzioni proprietarie su segni, pattern loading o inviluppi. Richiedi legenda e coefficienti espliciti.
