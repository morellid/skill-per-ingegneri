# CHANGELOG - cra-classificazione-pde

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Noti per v0.2 (rinviati)
- Sotto-attivita' dedicata agli **obblighi di segnalazione** ex art. 14 (vulnerabilita' attivamente sfruttate e incidenti gravi al CSIRT coordinatore e all'ENISA tramite piattaforma unica di segnalazione art. 16).
- Sotto-attivita' di supporto alla redazione della **politica di divulgazione coordinata delle vulnerabilita' (CVD)** ex Allegato I parte II.
- Guida operativa alla redazione della **SBOM** in formato standard (richiesta dall'Allegato I parte II punto 1, dall'Allegato VII punto 8 e dall'art. 13 par. 24).
- Skill complementare sull'integrazione con il **Reg. (UE) 2019/881** (sistemi europei di certificazione della cibersicurezza, livello "sostanziale" minimo).
- Aggiornamento alla pubblicazione dell'**atto di esecuzione ex art. 7 par. 4** (descrizione tecnica categorie Allegato III, attesa per 11/12/2025) e degli **atti delegati ex art. 8 par. 1** sulle categorie dell'Allegato IV soggette a certificazione europea obbligatoria.
- Sostituire le denominazioni abbreviate delle 19 categorie di Classe I in `tasks/classifica-pde.md` con le denominazioni letterali dell'Allegato III, allineando l'estratto curato. Aggiungere art. 2 par. 8 alla discussione delle esclusioni (limite degli obblighi di comunicazione per sicurezza nazionale).

## [0.1.0-alpha] - 2026-05-17

### Added
- Prima versione alpha della skill.
- Task files iniziali (4 sotto-attivita': `check-ambito-applicabilita`, `classifica-pde`, `scegli-procedura-conformita`, `check-documentazione-tecnica`).
- Trascrizione fedele del Regolamento (UE) 2024/2847 in `references/fonti/reg-ue-2024-2847-cra.md` (PDF ufficiale EUR-Lex, SHA256 verificato).
- Estratto curato di classificazione e moduli in `references/estratti/reg-ue-2024-2847-cra-classificazione.md`.
- Esempi: caso conforme (firewall hardware, importante Classe II) e caso problematico (router consumer con norme armonizzate non applicate).
- AGENTS.md di skill e dual-agent metadata (`agents/openai.yaml`) per discovery sia in Claude Code sia in Codex.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2 in `methodology/validazione.md`).
- Da considerare draft finche' non passa validazione Livello 2.
- Il Regolamento (UE) 2024/2847 si applica dall'**11 dicembre 2027** (generale); art. 14 dall'**11 settembre 2026**; Capo IV dall'**11 giugno 2026**. Fino a queste date la skill ha valore di pianificazione anticipata: gli output non possono essere usati per immissioni sul mercato attualmente in corso, le cui valutazioni di conformita' seguono regimi pre-CRA.
- Outputs della skill devono essere riletti dopo la pubblicazione degli atti di esecuzione/delegati attesi (art. 7 par. 4 entro 11/12/2025; art. 8 par. 1, tempistica aperta).
