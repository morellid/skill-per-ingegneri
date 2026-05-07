# Esempio: caso problematico - non monotonia residua dopo il capping

> Caso patologico dove il capping prescritto dal decreto NON risolve la non monotonia, e l'agent deve riportare un warning chiaro.

## Profilo edificio (fittizio)

- Tipologia: muratura portante a 2 piani in zona costiera
- Anno di costruzione: anni '50, costruito senza criteri antisismici
- Sito: zona sismica 2 (PGA_D(SLV) = 0.12 g)
- Livello di Conoscenza: LC1 (FC = 1.35)

## Dati di input (con anomalia non risolvibile dal capping)

| SL  | TR_C [anni] | PGA_C [g] |
|:---:|:-----------:|:---------:|
| SLO | **80**          | 0.025     |
| SLD | **40**          | 0.020     |
| SLV | 150         | 0.060     |
| SLC | 250         | 0.075     |

**Anomalia**: TR_C(SLO) = 80 > TR_C(SLD) = 40, ovvero l'edificio raggiunge SLD (CR=15%) PRIMA di SLO (CR=7%) sotto azione sismica crescente. Cio' implica una Curva di Individuazione **non monotona** in (lambda, CR).

## Capping del decreto NON risolve

Il capping prescritto al passo 2.1.3 dell'Allegato A pone:

```
TR_C(SLO) := min(TR_C(SLO), TR_C(SLV)) = min(80, 150) = 80   -> nessuna modifica
TR_C(SLD) := min(TR_C(SLD), TR_C(SLV)) = min(40, 150) = 40   -> nessuna modifica
```

Entrambi i TR_C sono gia' inferiori a TR_C(SLV), quindi il capping non fa nulla. Tuttavia la non monotonia tra SLO e SLD (che il decreto NON disciplina esplicitamente) rimane.

## Cosa significa fisicamente

In edifici molto rigidi e fragili (muratura a sacco, calcestruzzi vecchi non confinati) si puo' osservare che il danneggiamento non strutturale "diffuso" (SLD) si manifesta a livelli di azione sismica MOLTO bassi - prima ancora che l'edificio cessi di essere "operativo" secondo la definizione SLO. Questo e' raro ma fisicamente possibile.

Piu' spesso, la non monotonia e' segnale di un **errore di analisi**:
- LC e FC scelti male per i diversi SL;
- modello di degrado di rigidezza inconsistente;
- analisi pushover con curva di capacita' non interpretata correttamente in corrispondenza di stati limite.

## Comportamento atteso della skill

Il modulo `sismabonus.py` con il capping di default attivo:
- **NON solleva eccezione** (input fisicamente valido ma raro);
- Calcola PAM con la formula trapezoidale standard;
- **Segnala `monotona: false`** nell'output JSON;
- Riporta nel campo `capping` i valori originali e quelli effettivamente usati (entrambi invariati per questo caso);
- Il valore di PAM calcolato in questa modalita' **potrebbe non essere fisicamente significativo** se la non monotonia e' un errore di analisi.

L'agent deve:
1. Riportare i numeri come restituiti dal modulo;
2. Inserire un warning esplicito in output, p.es.: "ATTENZIONE: la Curva di Individuazione resta non monotona anche dopo il capping prescritto dall'Allegato A passo 2.1.3 (TR_C(SLO)=80 > TR_C(SLD)=40, situazione non disciplinata esplicitamente dal decreto). Verificare l'analisi di vulnerabilita'. La PAM calcolata potrebbe non essere fisicamente significativa.";
3. **NON applicare alcuna correzione automatica oltre il capping del decreto**: ulteriori interventi sui TR_C sono scelte di analisi del progettista.

## Cosa deve fare il progettista

1. Verificare i parametri di input dell'analisi (LC, FC, modello strutturale);
2. Se la non monotonia e' confermata come fisica: documentare l'analisi e procedere con asseverazione;
3. Se e' errore di analisi: rieseguire e rifornire input al modulo;
4. Asseverare la classe finale solo dopo aver chiarito la natura della non monotonia.

## Risultato del modulo (per riferimento)

- PAM = 1.61% -> classe C
- IS-V = 50% -> classe C
- Classe finale = C
- monotona = false
- capping_attivo = true (ma non ha modificato nulla in questo caso)

(La PAM e' formalmente calcolabile dalla formula trapezoidale, ma la non monotonia residua rende dubbia la sua corrispondenza con l'integrale geometrico atteso. Vedi note in `references/estratti/dm-58-2017-allegato-a-formula-pam.md`.)
