# Spettro di risposta elastico NTC 2018 (par. 3.2)

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 self-check); validazione Livello 2 vs CSLP da fare prima del release v0.1.

Skill code-driven per il calcolo dello spettro di risposta elastico in accelerazione (componente orizzontale) ai sensi delle NTC 2018 par. 3.2 e Circolare 7/2019.

## Target

Ingegneri strutturisti italiani che progettano nuovi edifici o valutano edifici esistenti ai sensi delle NTC 2018, e ne devono ricavare lo spettro elastico Se(T) per analisi statiche lineari, modali, push-over o time-history.

Sinergie naturali con altre skill in roadmap: classificazione di rischio sismico DM 58/2017 (codice scheda CV.1), calcolo PAM sismabonus (SC.2), combinazioni di carico (SC.3).

## Cosa fa

- Calcola V_R = V_N * C_U (par. 2.4.3) e i tempi di ritorno T_R per gli stati limite SLO/SLD/SLV/SLC (Tab. 3.2.I).
- Interpola logaritmicamente i parametri di pericolosita' a_g, F_0, T_C* sui 9 T_R di riferimento del reticolo INGV (Allegato A NTC).
- Calcola i coefficienti S_S, C_C (Tab. 3.2.IV), S_T (Tab. 3.2.V), eta (eq. 3.2.6) e i periodi caratteristici T_B, T_C, T_D (eq. 3.2.7-3.2.8).
- Tabula le ordinate Se(T) sull'intervallo richiesto (formule 3.2.4 a tratti).
- Esporta in CSV o JSON.

Sotto-attivita' (vedi `SKILL.md` per il routing):
- `tasks/calcola-spettro.md` - calcolo completo spettro per uno o piu' SL
- `tasks/valida-input-sito.md` - precheck input prima del calcolo
- `tasks/run-test-suite.md` - esecuzione della test suite

## Installazione

Vedi [`AGENTS.md`](../../AGENTS.md) di repo. In sintesi:

```bash
# Claude Code
ln -sfn "$(pwd)/skills/spettro-risposta-ntc" "$HOME/.claude/skills/spettro-risposta-ntc"

# Codex
ln -sfn "$(pwd)/skills/spettro-risposta-ntc" "$HOME/.agents/skills/spettro-risposta-ntc"
```

Riavvia l'agent. Poi:

> "Calcolami lo spettro NTC per questo sito (allego il JSON con i 9 valori dal reticolo INGV)..."

Il modulo Python richiede solo Python 3.9+ standard library.

## Fonti consultate

- DM 17/01/2018 (NTC 2018), Suppl. Ord. n. 8 alla GU n. 42 del 20/02/2018: par. 2.4 (vita nominale, classi d'uso), par. 3.2 (azione sismica), Allegato A (reticolo).
- Circolare MIT n. 7 del 21/01/2019, Suppl. Ord. n. 5 alla GU n. 35 dell'11/02/2019: par. C2.4, C3.2.
- Servizio interattivo INGV [zonesismiche.mi.ingv.it](http://zonesismiche.mi.ingv.it/) - lookup parametri al sito.
- Foglio Excel CSLP del Servizio Tecnico Centrale - benchmark di confronto.

Dettaglio completo (URL, accessed, sha256, license) in `references/sources.yaml`.

## Limiti noti

- Solo componente **orizzontale** (par. 3.2.3.2.1). Lo spettro verticale (3.2.3.2.2) sara' aggiunto in versione successiva.
- Solo spettro **elastico**. Lo spettro di **progetto** S_d(T) con riduzione q (par. 3.2.3.5) richiede scelte progettuali e resta in capo al professionista.
- Categorie di sottosuolo **S1, S2** rifiutate esplicitamente: NTC par. 3.2.2 prescrive analisi specifiche di risposta sismica locale.
- La skill **non incorpora il reticolo INGV**: l'utente fornisce i 9 valori (a_g, F_0, T_C*) al sito, ricavati da INGV o foglio CSLP.
- Categorie topografiche T2/T3/T4 sono applicate **in sommita' del rilievo**: per quote intermedie il professionista corregge l'output con NTC eq. 3.2.5.
- Validazione di Livello 2 (confronto numerico vs CSLP su 10 casi reali) ancora da completare prima del release v0.1 stabile.

**Ogni output va verificato dal progettista strutturale firmatario prima dell'uso in analisi di calcolo o relazioni di calcolo.**

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
