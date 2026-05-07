# Esempio: caso problematico - curva di individuazione non monotona

> Caso patologico: la skill deve segnalare il problema senza interrompere il calcolo, e l'agent deve riportare un warning chiaro.

## Profilo edificio (fittizio)

- Tipologia: muratura portante a 2 piani in zona costiera
- Anno di costruzione: anni '50, costruito senza criteri antisismici
- Sito: zona sismica 2 (PGA_D(SLV) = 0.12 g)
- Livello di Conoscenza: LC1 (FC = 1.35)

## Dati di input (con anomalia)

| SL  | TR_C [anni] | PGA_C [g] |
|:---:|:-----------:|:---------:|
| SLO | **80**          | 0.025     |
| SLD | **40**          | 0.020     |
| SLV | 150         | 0.060     |
| SLC | 250         | 0.075     |

**Anomalia**: TR_C(SLO) = 80 > TR_C(SLD) = 40, ovvero l'edificio raggiunge SLD (CR=15%) PRIMA di SLO (CR=7%) sotto azione sismica crescente. Cio' implica una Curva di Individuazione **non monotona** in (lambda, CR).

## Cosa significa fisicamente

In edifici molto rigidi e fragili (muratura a sacco, calcestruzzi vecchi non confinati) si puo' osservare che il danneggiamento non strutturale (SLD) si manifesta a livelli di azione sismica MOLTO bassi - prima ancora che l'edificio cessi di essere "operativo" secondo la definizione SLO. Questo e' raro ma fisicamente possibile.

Piu' spesso, la non monotonia e' segnale di un **errore di analisi**:
- LC e FC scelti male per i diversi SL;
- modello di degrado di rigidezza inconsistente;
- analisi pushover con curva di capacita' non interpretata correttamente in corrispondenza di stati limite.

## Comportamento atteso della skill

Il modulo `sismabonus.py`:
- **NON solleva eccezione** (non e' invalid input: e' input fisicamente valido ma raro);
- Calcola PAM con la formula trapezoidale standard;
- **Segnala `monotona: false`** nell'output JSON;
- Il valore di PAM calcolato in questa modalita' **potrebbe non essere fisicamente significativo**.

L'agent deve:
1. Riportare i numeri come restituiti dal modulo;
2. Inserire un warning esplicito in output, p.es.: "ATTENZIONE: la Curva di Individuazione non e' monotona (TR_C(SLO)=80 > TR_C(SLD)=40). Verificare l'analisi di vulnerabilita' o applicare capping coerente con DM 58/2017 Allegato A punto 2.1. La PAM calcolata potrebbe non essere fisicamente significativa.";
3. **NON applicare capping automatico**: il capping e' una scelta di analisi del progettista, non automatizzabile dalla skill.

## Cosa deve fare il progettista

1. Verificare i parametri di input dell'analisi (LC, FC, modello strutturale);
2. Se la non monotonia e' confermata come fisica: applicare il capping manualmente (es. porre TR_C(SLO) := TR_C(SLD) = 40 anni, riducendo SLO al livello di SLD - intervento conservativo) e rieseguire la skill;
3. Asseverare la classe finale solo dopo aver applicato e documentato il capping nel report di vulnerabilita'.

## Risultato del modulo (per riferimento)

- PAM = 1.61% -> classe C
- IS-V = 50% -> classe C
- Classe finale = C
- monotona = false

(Il valore di PAM e' formalmente calcolabile dalla formula trapezoidale, ma la non monotonia rende dubbia la sua corrispondenza con l'integrale geometrico atteso. Vedi note in `references/estratti/dm-58-2017-allegato-a-formula-pam.md`.)
