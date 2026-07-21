# CHANGELOG - sottoprodotti-end-of-waste-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #322)
- Prima versione della skill di supporto documentale all'inquadramento del sottoprodotto
  (art. 184-bis) e della cessazione della qualifica di rifiuto - End of Waste (art.
  184-ter) del D.Lgs. 152/2006 (Codice dell'ambiente), Parte IV.
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 3/4/2006 n. 152 - testo su Normattiva, pagina indice pinnata `!vig=2026-07-17`
    SHA256: c2175fe5c9313db1087d444b07e71d727154140d579ffcf6357ababa5d57b45c
    (riproducibile, doppio download; codice redazionale 006G0171, stesso indice delle
    altre skill D.Lgs. 152). Artt. 184-bis (Sottoprodotto, idSottoArticolo 2) e 184-ter
    (Cessazione della qualifica di rifiuto/End of Waste, idSottoArticolo 3) letti via AJAX
    (caricaArticolo, idGruppo 34) e trascritti verbatim in
    `references/fonti/dlgs-152-2006-184bis-184ter.md` (incluse le note di abrogazione/
    soppressione e l'AGGIORNAMENTO 127).
- Estratto operativo `references/estratti/sottoprodotti-eow-checklist.md` con le quattro
  condizioni del sottoprodotto, le condizioni e i criteri dell'End of Waste, la via
  autorizzativa con parere ISPRA/ARPA, gli adempimenti (RECER), il computo, il REACH e il
  Nucleo NEW.
- Due task: `verifica-sottoprodotto.md` (quattro condizioni cumulative) e
  `inquadra-end-of-waste.md` (recupero, condizioni, criteri, autorizzazioni, controlli).
- Due esempi: segatura/cippato come sottoprodotto (art. 184-bis); aggregato riciclato da
  rifiuti inerti come End of Waste (art. 184-ter).

### Nota di source-grounding (#322)
La skill e' source-grounded sul **testo vigente degli artt. 184-bis e 184-ter del D.Lgs.
152/2006 letto da Normattiva** (fonte ufficiale). I **decreti ministeriali di criterio**
(rinvio del c. 2, es. DM 264/2016 sui sottoprodotti; regolamenti UE e DM End of Waste per
tipologia) sono **citati come rinvio e non riprodotti**. L'**art. 183** (definizioni di
rifiuto/produttore), gli **artt. 208/209/211** e il **Titolo III-bis** (autorizzazioni) e
la **direttiva 2008/98/CE** sono citati, non riprodotti. Le note tra doppi tondi `(( ))` e
le note di abrogazione/soppressione sono riportate come da fonte.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati.
- Validazione Livello 2 da effettuare con esperto rifiuti/economia circolare.
- Possibili estensioni future: trascrizione mirata dell'art. 183 (definizioni), raccordo
  con `deposito-classificazione-rifiuti-dlgs152` e con i DM di criterio (264/2016 e EoW per
  tipologia).
