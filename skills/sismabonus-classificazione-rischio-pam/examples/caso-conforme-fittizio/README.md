# Esempio: caso conforme fittizio

> Caso di test "ben condizionato" usato come fixture anti-drift della test suite.

## Profilo edificio (fittizio)

- Tipologia: c.a. a telaio, 4 piani
- Anno di costruzione: 1980 (esistente, soggetto a sismabonus)
- Sito: zona sismica 3 (Italia centro-settentrionale tipica), PGA_D(SLV) = 0.10 g
- Livello di Conoscenza: LC2 (FC = 1.20)
- Tipo di analisi: statica lineare con spettro elastico ridotto (q=1.5 esistenti, NTC 2018 par. 8.7.2.1)

I valori di TR_C e PGA_C sono fittizi ma realistici per il profilo descritto: sufficienti a illustrare il funzionamento della skill, non sono presi da un edificio reale.

## Stato di fatto

| SL  | TR_C [anni] | PGA_C [g] | PGA_D [g] |
|:---:|:-----------:|:---------:|:---------:|
| SLO | 30          | 0.030     | 0.030     |
| SLD | 50          | 0.040     | 0.045     |
| SLV | 200         | 0.075     | 0.100     |
| SLC | 350         | 0.090     | 0.130     |

Risultato:
- PAM = 1.29% -> classe B
- IS-V = 75% -> classe B
- **Classe finale: B**

## Intervento

Rinforzo locale dei nodi trave-pilastro + incamiciatura selettiva di 4 pilastri di base. Coerente con NTC 2018 cap. 8.4 (intervento di "miglioramento sismico" che incrementa la sicurezza senza adeguamento totale).

## Stato di progetto (atteso post-intervento)

| SL  | TR_C [anni] | PGA_C [g] | PGA_D [g]      |
|:---:|:-----------:|:---------:|:---------------:|
| SLO | 100         | 0.045     | 0.030 (invariato)|
| SLD | 250         | 0.060     | 0.045 (invariato)|
| SLV | 600         | 0.135     | 0.100 (invariato)|
| SLC | 1100        | 0.165     | 0.130 (invariato)|

Risultato:
- PAM = 0.60% -> classe A
- IS-V = 135% -> classe A+
- **Classe finale: A**

## Salto classi

**Salto = 1 classe (da B ad A).** Miglioramento PAM = 0.70 punti percentuali; miglioramento IS-V = 60 punti percentuali.

## Esecuzione

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/sismabonus.py --input-json input.json
```

L'output deve corrispondere a `expected.json` (test anti-drift `TestAntiDriftFixture.test_fixture_conforme` in `tasks/lib/test_sismabonus.py`).

## Limiti dell'esempio

- I numeri sono **fittizi**: non sono presi da un edificio reale ne' da un report di software certificato. Servono come smoke test della pipeline.
- L'aliquota di detrazione fiscale per "salto = 1 classe" sismabonus va verificata sulla legislazione fiscale vigente, non e' calcolata dalla skill.
- L'asseverazione (Allegato B / B-bis) NON e' generata dalla skill: il professionista deve trasferire i numeri sul modulo ministeriale e firmare.
