# Changelog - periodo-proprio-t1-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-12

### Added (closes #30)
- Prima versione della skill di stima del periodo proprio T1 (NTC 2018 par. 7.3.3.2 + Circ. 7/2019 par. C7.3.3.2)
- Fonti scaricate, hashate e trascritte (Regola zero):
  - NTC 2018 (GU n. 42/2018 S.O. 8) SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 -> `references/fonti/ntc2018-dm-17-01-2018.md` (par. 7.3.3.2 integrale + [2.5.7] dal par. 2.5.3)
  - Circ. 7/2019 (GU n. 35/2019 S.O. 5) SHA256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c -> `references/fonti/circ-7-2019-mit.md` (par. C7.3.3.2 integrale + nota 9; trascrizione dalla lettura visiva di pag. 204 GU, pagine del cap. C7 senza layer testo nel PDF)
- Estratto operativo `references/estratti/t1-formule-e-limiti.md`
- Modulo deterministico `tasks/lib/periodo_t1.py`: [7.3.6] T1 = 2*sqrt(d); [C7.3.2] T1 = C1*H^(3/4) con C1 = 0,085/0,075/0,050; check H <= 40 m e massa uniforme; condizione T1 <= 2,5*TC; lambda 0,85/1,0 per la [7.3.7]; CLI con output JSON
- Test suite `tasks/lib/test_periodo_t1.py` (22 test, valori chiusi verificabili a mano)
- Task `tasks/stima-periodo-t1.md`; SKILL.md; AGENTS.md; agents/openai.yaml
- Esempi: telaio c.a. 5 piani H=16 m con TC (conforme) + torre 48 m con massa non uniforme (caso limite fuori ambito)

### Nota di conformita' (Regola zero)
- L'issue #30 citava la formula "C1*H^(3/4)" come "NTC 2018 par. 7.3.3.2": la lettura del PDF ha mostrato che il par. 7.3.3.2 delle NTC 2018 contiene la [7.3.6] T1 = 2*sqrt(d), mentre la formula C1*H^(3/4) e' nella Circolare 7/2019 come [C7.3.2] (nelle NTC 2008 era in norma). La skill implementa entrambe con la gerarchia dichiarata dalla Circolare e cita ciascuna formula alla propria fonte.

### Note di sviluppo
- Validazione Livello 2 da effettuare con ingegnere strutturista
- Possibile estensione futura: calcolo della distribuzione delle forze [7.3.7] dati i pesi di piano
