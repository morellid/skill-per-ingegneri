# Cedimenti edometrici - SLE NTC 2018 par. 6.2.4

> Versione: 0.1.0-alpha
> Stato: in sviluppo, validazione Livello 1 OK; Livello 2 (vs casi pubblicati e software geotecnico) da completare.

Skill per la stima del cedimento edometrico di un singolo strato omogeneo per verifiche agli stati limite di esercizio (SLE) ai sensi di NTC 2018 par. 6.2.4. Usa la formulazione classica della meccanica dei terreni (Terzaghi 1925, Skempton 1944): compressione monodimensionale a tratti su rami OC e NC della curva edometrica.

## Target

Ingegneri strutturisti e geotecnici italiani in fase di pre-dimensionamento di fondazioni superficiali su terreni coesivi (argille, limi). La skill stima il cedimento medio di un singolo strato; per stratigrafie multilayer e cedimenti differenziali servono software geotecnici dedicati.

## Cosa fa

Sotto-attivita' supportate:
- **Calcolo cedimento edometrico**: dato h0 (m), e0, Cc, Cr, sigma_0' (kPa), sigma_p' (kPa), Delta sigma' (kPa), restituisce sigma_f', OCR, ramo (OC / NC / transizione), contributi parziali Delta h_OC e Delta h_NC, cedimento totale Delta h in m e mm, deformazione media epsilon.

Per il dettaglio tecnico vedi [`SKILL.md`](SKILL.md). Per le convenzioni di dominio vedi [`AGENTS.md`](AGENTS.md).

## Installazione

Clonare il repository e copiare/linkare la cartella `skills/cedimenti-edometrici-ntc/` nel proprio ambiente Claude Code o Codex secondo lo schema di distribuzione skill. Vedi `../../README.md` del repo.

## Fonti consultate

- DM 17/01/2018 (NTC 2018), GU n. 42 del 20/02/2018 - par. 6.2.2 e 6.2.4
- Circolare MIT n. 7 del 21/01/2019, GU n. 35 dell'11/02/2019 - par. C6.2
- Lancellotta R., "Geotecnica" - riferimento didattico standard (testo a pagamento, non incorporato)

Dettaglio in [`references/sources.yaml`](references/sources.yaml).

## Limiti noti

- Solo singolo strato omogeneo (no multilayer)
- Solo compressione monodimensionale (no 2D / 3D, no drenaggio radiale)
- Solo cedimento primario di consolidazione (no immediato elastico, no secondario / creep)
- Solo carico in compressione (Delta sigma >= 0; no rebound)
- Non stima Cc, Cr, e0, sigma_p' (input dalla relazione geotecnica)
- Non calcola Delta sigma' a profondita' (Boussinesq separato)
- Non calcola tempi di consolidazione (Cv + Terzaghi 1D, fuori scope v0.1)
- Non valuta cedimenti differenziali, distorsioni, tilt
- Validazione Livello 2 (vs casi pubblicati e software geotecnico) non ancora eseguita

**La skill non sostituisce la relazione geotecnica firmata dal progettista.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
