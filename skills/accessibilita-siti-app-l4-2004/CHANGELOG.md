# CHANGELOG - accessibilita-siti-app-l4-2004

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #52)
- Prima versione della skill di supporto documentale agli obblighi di
  accessibilita' dei siti web e delle applicazioni mobili (Legge Stanca, L.
  4/2004).
- Fonte scaricata, hashata e letta (Regola zero):
  - L. 9/1/2004 n. 4 (Legge Stanca) - testo multivigente su Normattiva, pagina
    indice pinnata `!vig=2026-07-14` SHA256:
    1cbf3409031e4cf1a0599c3e1a9c7243c5e7bbe01cd5deecc29cafa566324ec2
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 2 (definizioni), 3 (soggetti erogatori), 4 (obblighi), 7 (compiti
    AgID), 9 (responsabilita') e 11 (requisiti tecnici) letti via AJAX
    (caricaArticolo) e trascritti verbatim in
    `references/fonti/legge-4-2004.md`. Il testo vigente incorpora il D.Lgs.
    106/2018 (recepimento dir. UE 2016/2102).
- Estratto operativo `references/estratti/accessibilita-checklist.md` con
  ambito, obblighi, requisiti (rinvio AgID), vigilanza e sanzioni.
- Due task: `verifica-obbligo.md` (ambito ed esclusioni) e
  `checklist-appalto-contratto.md` (obblighi negli appalti e nei contratti).
- Due esempi: comune con appalto sito/app (obbligato, nullita' del contratto) e
  PMI privata sotto soglia (non obbligata dalla Legge Stanca).

### Nota di source-grounding (#52)
La scheda #52 (SW.4) citava le **WCAG 2.1** (W3C) e le linee guida AgID
sull'accessibilita'. La skill e' source-grounded sul **testo vigente della Legge
Stanca (L. 4/2004) letto da Normattiva** (fonte ufficiale italiana che recepisce,
via D.Lgs. 106/2018, la dir. UE 2016/2102), con la pagina indice pinnata a data di
vigenza per hash riproducibile e la trascrizione verbatim degli artt. 2, 3, 4, 7,
9, 11. I **requisiti tecnici** di dettaglio (linee guida AgID, EN 301 549, WCAG
2.1) non sono riprodotti: il perimetro copre il **quadro giuridico degli obblighi**
(ambito, appalti/contratti, nullita', vigilanza, sanzioni) e rinvia alle linee
guida AgID e alle WCAG per l'audit tecnico, evitando la riproduzione di norme
tecniche.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con esperto di accessibilita'/RTD.
- Possibili estensioni future: dichiarazione di accessibilita' e modelli AgID;
  raccordo con l'European Accessibility Act (D.Lgs. 82/2022) per prodotti/servizi.
