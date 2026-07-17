# CHANGELOG - domicilio-digitale-pec-cad

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #326)
- Prima versione della skill di supporto documentale al domicilio digitale e ai pubblici
  elenchi dei domicili digitali (PEC) secondo il Codice dell'amministrazione digitale
  (D.Lgs. 82/2005).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 7/3/2005 n. 82 (CAD) - testo su Normattiva, pagina indice pinnata
    `!vig=2026-07-17` SHA256:
    a54022efcaea5f63f7e5b62a2ce2513b724b85e2695589d1af8eecd54f20fb47
    (riproducibile, doppio download; codice redazionale 005G0104, stesso indice della skill
    documento-informatico-firme-cad). Artt. 3-bis (identità e domicilio digitale), 6
    (utilizzo ed effetti), 6-bis (INI-PEC), 6-ter (IPA) e 6-quater (INAD) letti via AJAX
    (caricaArticolo, idGruppo 2) e trascritti verbatim in
    `references/fonti/dlgs-82-2005-domicilio-digitale.md` (incluse note di abrogazione/
    aggiornamento; le note esplicative lunghe degli AGGIORNAMENTI 21/28 dell'art. 3-bis sono
    abbreviate con l'indicazione esplicita [...]).
- Estratto operativo `references/estratti/domicilio-digitale-checklist.md` con nozione,
  obbligo/facoltà, effetti giuridici, notifica diretta, i tre indici (INI-PEC/IPA/INAD) e la
  sintesi soggetto→indice.
- Due task: `inquadra-domicilio-digitale.md` (indice competente e regime) e
  `inquadra-effetti-notifica.md` (effetti giuridici e notifica diretta).
- Due esempi: mappatura soggetto→indice (ingegnere, cittadino, Comune); effetti e notifica
  di una comunicazione PEC (verbale di sanzione).

### Nota di source-grounding (#326)
La skill e' source-grounded sul **testo vigente degli artt. 3-bis, 6, 6-bis, 6-ter,
6-quater del CAD letto da Normattiva** (fonte ufficiale). Le **Linee guida AgID** attuative
e i decreti (es. **DM MISE 19/3/2013** per INI-PEC) sono **citati come rinvio e non
riprodotti**. Gli artt. 2 (soggetti), 18-bis (sanzioni), 22/23-bis (copie), 62 (ANPR),
64/64-bis (identità digitale SPID/CIE) sono citati. Le **firme elettroniche/il documento
informatico** sono coperti dalla skill `documento-informatico-firme-cad`. Il testo tra
doppi tondi `(( ))` e le note di abrogazione sono riportati come da fonte; le note
esplicative lunghe degli aggiornamenti dell'art. 3-bis sono abbreviate con [...].

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati (il CAD è oggetto di frequenti correttivi).
- Validazione Livello 2 da effettuare con esperto CAD/amministrazione digitale.
- Possibili estensioni future: raccordo con l'identità digitale (SPID/CIE, artt. 64/64-bis),
  con l'ANPR (art. 62) e con la piattaforma notifiche (SEND, art. 26 D.L. 76/2020).
