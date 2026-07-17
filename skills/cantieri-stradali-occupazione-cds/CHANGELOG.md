# CHANGELOG - cantieri-stradali-occupazione-cds

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #329)
- Prima versione della skill di supporto documentale all'occupazione della sede stradale e
  all'apertura di opere, depositi e cantieri stradali, artt. 20 e 21 del Codice della Strada
  (D.Lgs. 285/1992).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 30/4/1992 n. 285 (CdS) - testo su Normattiva, pagina indice pinnata
    `!vig=2026-07-17` SHA256:
    e541dc1a2a210a4ffbc9edb9fb8c5bb21ee41241638dffbb0cee783cadb84918
    (riproducibile, doppio download; codice redazionale 092G0306, stesso indice della skill
    trasporti-eccezionali-cds-art10). Artt. 20 (occupazione della sede stradale) e 21
    (opere, depositi e cantieri stradali) letti via AJAX (caricaArticolo, idGruppo 2) e
    trascritti verbatim in `references/fonti/cds-285-1992-20-21.md`.
- Estratto operativo `references/estratti/cantieri-stradali-checklist.md` con occupazione
  per tipo di strada, chioschi/marciapiedi, cantieri (autorizzazione, sicurezza,
  segnalazione), sanzioni e sequenza operativa.
- Due task: `inquadra-cantiere-stradale.md` (autorizzazione e obblighi del cantiere) e
  `inquadra-occupazione-suolo.md` (ammissibilità dell'occupazione e limiti).
- Due esempi: apertura di un cantiere temporaneo su strada urbana (tipo E); dehors su
  marciapiede in centro abitato e mercato su strada extraurbana (tipo C).

### Nota di source-grounding (#329)
La skill e' source-grounded sul **testo vigente degli artt. 20 e 21 del Codice della Strada
letto da Normattiva** (fonte ufficiale). Gli **importi delle sanzioni** riportati sono
quelli vigenti al 2026-07-17 (adeguamenti biennali ex art. 195 c. 3 CdS; le numerose note
AGGIORNAMENTO, di identico tenore, sono riportate in coda in forma compatta). Il
**Regolamento (DPR 495/1992, artt. 30-43)** e il **disciplinare tecnico DM 10/7/2002**
(schemi di segnaletica temporanea) sono **citati come rinvio e non riprodotti**; gli artt. 2
(classificazione strade), 18 (fasce/visibilità) e 26 (autorizzazioni/concessioni) sono
citati. La **sicurezza dei lavoratori** nei cantieri stradali (D.Lgs. 81/2008) e' fuori
perimetro.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli; verificare gli importi delle sanzioni (adeguamento biennale).
- Validazione Livello 2 da effettuare con esperto CdS/gestione strade.
- Possibili estensioni future: art. 26 (autorizzazioni e concessioni), trascrizione mirata
  degli artt. 30-43 del Regolamento (segnaletica temporanea) e raccordo con la sicurezza dei
  cantieri (D.Lgs. 81/2008).
