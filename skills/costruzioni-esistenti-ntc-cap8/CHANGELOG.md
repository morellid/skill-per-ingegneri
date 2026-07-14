# CHANGELOG - costruzioni-esistenti-ntc-cap8

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-13

### Added (closes #21)
- Prima versione della skill di consultazione del capitolo 8 delle NTC 2018
  (costruzioni esistenti) e del capitolo C8 della Circolare 7/2019.
- Fonti scaricate, hashate e lette (Regola zero):
  - NTC 2018 (GU n. 42/2018 S.O. 8) SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
    -> trascrizione integrale del cap. 8 (parr. 8.1-8.7.5) in `references/fonti/ntc2018-dm-17-01-2018.md`
  - Circ. 7/2019 (GU n. 35/2019 S.O. 5) SHA256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
    -> trascrizione C8.3, C8.4.x, C8.5.4.x + Tabella C8.5.IV in `references/fonti/circ-7-2019-mit.md`
  - Hash identici a quelli gia' registrati dalle altre skill NTC del repo
    (stessa edizione GU), riverificati il 2026-07-13 con doppio download.
- Estratto operativo `references/estratti/ntc2018-cap8-costruzioni-esistenti.md`
  con le tabelle di sintesi (categorie di intervento, casi di adeguamento
  a-e e soglie zeta_E, soglie miglioramento per classe d'uso, LC/FC).
- Tre task: `classifica-intervento.md` (categoria + soglia zeta_E),
  `determina-lc-fc.md` (livello di conoscenza e fattore di confidenza),
  `qa-cap8.md` (valutazione della sicurezza, verifica fondazione, stati limite,
  elaborati minimi).
- Due esempi: cambio di destinazione d'uso verso scuola (adeguamento caso e),
  zeta_E >= 0,80, LC1/FC 1,35) e apertura di un vano in parete portante
  (intervento locale, no valutazione globale, no collaudo statico).

### Nota sulla scheda originaria (#21)
La scheda chiedeva una skill di "consultazione norma" su LC/FC e distinzione
adeguamento/miglioramento/locale (par. 8.4), posizionata come **non**
sostitutiva del progettista. La skill implementa esattamente questo perimetro:
- i valori numerici dei fattori di confidenza (FC = 1,35/1,2/1,0) NON sono nel
  testo del par. 8.5.4 delle NTC (che li richiama soltanto): provengono dalla
  Circolare 7/2019 par. C8.5.4 e dalla Tabella C8.5.IV, come dichiarato nelle
  trascrizioni e negli output;
- le soglie di zeta_E (adeguamento a,b,d -> 1,0 e c,e -> 0,80; miglioramento
  0,6 / +0,1) sono citate al par. 8.4.2/8.4.3 delle NTC.

### Note di sviluppo
- Skill di sola consultazione: nessun modulo di calcolo (coerente con lo scopo
  Q&A della scheda #21).
- Validazione Livello 2 da effettuare con ingegnere strutturista.
- Possibili estensioni future (solo con trascrizione delle relative sezioni):
  meccanismi locali della muratura (C8.7.1.2), valori di tabella dei parametri
  meccanici (C8.5.I/II/III), analisi cinematica dei cinematismi.
