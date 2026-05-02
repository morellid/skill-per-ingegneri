# CHANGELOG - dm37-2008-dichiarazione-conformita

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02

### Added
- SKILL.md con routing verso 2 task files e 7 categorie impianti (a-g)
- AGENTS.md con convenzioni di dominio e articoli chiave DM 37/2008 corretti
- Task `verifica-completezza-ddc.md`: verifica tutti i campi obbligatori del modello Allegato I
- Task `identifica-allegati-obbligatori.md`: determina allegati richiesti per categoria e soglie Art. 5 (progetto da professionista) e Art. 7 (schema sempre necessario)
- `references/sources.yaml` con fonti DM 37/2008 (Normattiva + GU originale)
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md`: parafasi operativa Art. 1, 3, 4, 5, 7 e struttura Allegato I
- Esempio conforme: impianto elettrico residenziale 85 mq, 3 kW, con schema impianto
- Esempio problematico: impianto elettrico ufficio 350 mq, 15 kW, senza progetto professionale

### Fixed (post adversarial review Codex)
- Corretti numeri articoli: progettazione e' Art. 5 (non Art. 6); abilitazioni sono Art. 3 e 4 (non Art. 5)
- Rimosso riferimento a "categoria h" inesistente: categorie sono a-g (Art. 1 DM 37/2008)
- Aggiunto obbligo schema elaborato tecnico in tutti i casi (non solo sopra-soglia)
- Aggiunta distinzione "progetto da professionista" (sopra soglia Art. 5) vs "schema del responsabile tecnico" (sotto soglia, ma sempre necessario)
- Corrette soglie per cat. e) gas: 50 kW (non 35 kW) - da verificare su Normattiva

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2)
- Da considerare draft finche' non passa validazione (vedi methodology/validazione.md)
- Fonti: testo DM 37/2008 da Normattiva (testo consolidato vigente) e GU originale
- Soglie Art. 5 nell'estratto sono parafrasi operative: richiedono verifica su Normattiva prima di v1.0
