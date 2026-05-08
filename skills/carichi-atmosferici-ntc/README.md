# Carichi atmosferici NTC 2018 (vento + neve)

> Versione: 0.1.0-alpha
> Stato: in sviluppo, validazione Livello 1 OK; Livello 2 (confronto vs casi pubblicati) da completare.

Skill per il calcolo della pressione del vento p (NTC 2018 par. 3.3) e del carico neve sulla copertura q_s (par. 3.4) per edifici civili e industriali correnti. Implementazione code-driven, deterministica, riproducibile: ogni numerico deriva dall'esecuzione del modulo Python, non da elaborazione testuale.

## Target

Ingegneri strutturisti italiani che progettano nuove costruzioni o valutano costruzioni esistenti e devono determinare le azioni atmosferiche caratteristiche secondo NTC 2018, senza ricorrere a fogli Excel proprietari o software di calcolo strutturale completi.

## Cosa fa

Sotto-attivita' supportate:
- **Pressione vento** (par. 3.3): dato il sito (parametri zonali da Tab. 3.3.I, altitudine), categoria di esposizione I-V, quota z, c_p e c_d, restituisce v_b, c_r, v_r, q_r, c_e, p in N/m^2 e kN/m^2 con riferimenti normativi puntuali
- **Carico neve** (par. 3.4): data zona (I-Alpina, I-Mediterranea, II, III), altitudine, inclinazione delle falde alpha e classe di esposizione, restituisce q_sk, mu_1, c_E, q_s in kN/m^2 con riferimenti normativi puntuali

Per il dettaglio tecnico vedi [`SKILL.md`](SKILL.md). Per le convenzioni di dominio e gli articoli citati vedi [`AGENTS.md`](AGENTS.md).

## Installazione

Clonare il repository e copiare/linkare la cartella `skills/carichi-atmosferici-ntc/` nel proprio ambiente Claude Code o Codex secondo lo schema di distribuzione skill in vigore. Vedi `../../README.md` del repo per dettagli.

## Fonti consultate

- DM 17/01/2018 (NTC 2018), GU n. 42 del 20/02/2018 - par. 3.3 e par. 3.4
- Circolare MIT n. 7 del 21/01/2019, GU n. 35 dell'11/02/2019 - par. C3.3 e C3.4

Dettaglio in [`references/sources.yaml`](references/sources.yaml).

## Limiti noti

- Tab. 3.3.I (zone vento) NON incorporata: l'utente fornisce v_b_0, a_0, k_s
- Categoria di esposizione I-V dichiarata dall'utente (non calcolata da Tab. 3.3.III)
- c_p del vento NON calcolato (input dell'utente)
- Solo mu_1 per coperture ad una/due falde regolari (no accumuli, deriva, sporgenze)
- a_s vento limitato a 1500 m; T_R limitato a 5-500 anni
- Validazione Livello 2 (vs casi pubblicati) non ancora eseguita

**La skill non sostituisce il giudizio del progettista strutturale firmatario.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
