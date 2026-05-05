# Output atteso

Profilo gamma SLU: `A1`

| ID | Tipo | Principale | Espressione | Valore | Riferimento |
|---|---|---|---|---:|---|
| SLU-A1-1 | SLU fondamentale A1 | Q_A | `1.3*G1 + 1.5*G2 + 1.5*Q_A + 0.75*Neve + 0.9*Vento` | 22.12 | NTC 2018 eq. 2.5.1 + Tab. 2.6.I |
| SLU-A1-2 | SLU fondamentale A1 | Neve | `1.3*G1 + 1.5*G2 + 1.05*Q_A + 1.5*Neve + 0.9*Vento` | 21.67 | NTC 2018 eq. 2.5.1 + Tab. 2.6.I |
| SLU-A1-3 | SLU fondamentale A1 | Vento | `1.3*G1 + 1.5*G2 + 1.05*Q_A + 0.75*Neve + 1.5*Vento` | 21.25 | NTC 2018 eq. 2.5.1 + Tab. 2.6.I |
| SLE-RARA-1 | SLE rara | Q_A | `1*G1 + 1*G2 + 1*Q_A + 0.5*Neve + 0.6*Vento` | 16.08 | NTC 2018 eq. 2.5.2 |
| SLE-FREQ-1 | SLE frequente | Q_A | `1*G1 + 1*G2 + 0.5*Q_A` | 13.5 | NTC 2018 eq. 2.5.3 |
| SLE-QP-1 | SLE quasi permanente | - | `1*G1 + 1*G2 + 0.3*Q_A` | 12.9 | NTC 2018 eq. 2.5.4 |
| SIS-1 | Sismica | E | `1*E + 1*G1 + 1*G2 + 0.3*Q_A` | 17.4 | NTC 2018 eq. 2.5.5 |

Nota: l'output reale contiene anche le combinazioni SLE rara/frequente con `Neve` e `Vento` principali.
