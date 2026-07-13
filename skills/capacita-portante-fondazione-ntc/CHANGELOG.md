# CHANGELOG - capacita-portante-fondazione-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-12

### Added (closes #31)
- Prima versione della skill di capacita' portante per fondazioni superficiali (verifica GEO carico limite NTC 2018 par. 6.4.2.1)
- Fonti scaricate, hashate e lette (Regola zero):
  - NTC 2018 (GU n. 42/2018 S.O. 8) SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 -> trascrizioni parr. 6.2.4.1.1/6.2.4.1.2 (Tab. 6.2.I/6.2.II), 6.4.2/6.4.2.1 (Tab. 6.4.I: gamma_R = 2,3), cap. 12
  - Circ. 7/2019 (GU n. 35/2019 S.O. 5) SHA256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c -> trascrizione C6.4.2.1
  - **FHWA NHI-06-089** "Soils and Foundations - Reference Manual Volume II" (U.S. DOT, dic. 2006, pubblico dominio) SHA256: 181a02c8c1ba7310d4c299f8bfb4f154d441d77f136f93879a0fd53ae2d64ccb (riproducibile, doppio download verificato) -> trascrizioni parr. 8.4.2-8.4.3.3 (eq. 8-1..8-9, Table 8-4/8-5/8-6, prime righe Table 8-2 per cross-check)
- Estratto operativo `references/estratti/fhwa-capacita-portante-ntc.md`
- Modulo deterministico `tasks/lib/capacita_portante.py` (+ 21 test): fattori Nc/Nq/Ngamma (eq. 8-2..8-5), eq. 8-6 con base/piano campagna orizzontali e carico verticale, fattori di forma Table 8-4, falda Table 8-5 con interpolazione, dimensioni efficaci eq. 8-7..8-9 con rifiuto per e >= 1/6 (FHWA 8.4.3.1), dq default 1,0 (omissione conservativa Table 8-6); catena NTC q_Rd = qult/2,3 e R_d = q_Rd*A' con confronto Ed <= Rd [6.2.1]
- Task `tasks/calcola-capacita-portante.md` con screening preliminare dei casi fuori ambito (carico inclinato, base inclinata, pendio, stratificazione, rottura locale, sisma)
- Esempi: plinto 2x3 drenato con falda e confronto Ed (conforme) + eccentricita' oltre 1/6 (rifiuto)

### Nota sulla scheda originaria (#31)
La scheda citava "formula Brinch-Hansen / Vesic" con fonte "NTC 2018 par. 6.4 + Circ. 7/2019": la lettura dei PDF conferma che NTC e Circolare NON contengono la formula del carico limite (il C6.4.2.1 elenca solo i fattori da cui dipende la resistenza). La formulazione implementata e' quella del FHWA NHI-06-089 par. 8.4 (fattori AASHTO; l'espressione di Ngamma = 2(Nq+1)tan phi e' quella di Vesic), usata come "altro codice internazionale" ai sensi del cap. 12 NTC, con i coefficienti parziali NTC per la verifica.

### Note di sviluppo
- Validazione Livello 2 da effettuare (confronto con Example 8-1 del manuale FHWA e/o software geotecnico)
- Possibili estensioni future (solo con trascrizione delle relative sezioni FHWA): carico inclinato (8.4.3.5), pendio (8.4.3.6, Ncq/Ngamma_q), verifica a scorrimento (gamma_R = 1,1)
