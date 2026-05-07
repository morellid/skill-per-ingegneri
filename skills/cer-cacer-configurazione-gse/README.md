# Configurazione CER/CACER e Qualifica GSE

> Versione: 0.1.0-alpha
> Stato: in sviluppo

Skill di supporto alla configurazione di una **Configurazione di Autoconsumo Collettivo da Energie Rinnovabili (CACER)** - in forma di **Comunita' Energetica Rinnovabile (CER, art. 31)**, **Gruppo di Autoconsumatori (GAC, art. 30 c. 2)** o **Autoconsumatore Individuale a Distanza (AID, art. 30 c. 1 lett. a) n. 2)** - e alla **qualifica del servizio** sul portale del GSE, ai sensi del **D.Lgs. 199/2021**, del **DM MASE 7 dicembre 2023 n. 414** come modificato dal **DM MASE 16 maggio 2025 n. 127** e da ultimo dal **DL 19 febbraio 2026 n. 19 art. 27** ("Decreto PNRR 2026").

## Target

- Ingegneri (industriali, energetici, gestionali) e periti industriali
- Energy manager, EGE, ESCo
- Consulenti GSE / consulenti PNRR
- Enti locali (Comuni, Unioni di Comuni) e in particolare Comuni con popolazione < 50.000 abitanti che valutano il contributo PNRR (regime vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27; soglia originaria del DM 414/2023 era < 5.000 ab., poi estesa a < 50.000 ab. dal DM 127/2025)
- Amministratori di condominio per GAC condominiali

## Cosa fa

Sotto-attivita' supportate (per il dettaglio tecnico vedi `SKILL.md`):

- **Verifica perimetro e scelta della configurazione** - cabina primaria, scelta AID/GAC/CER
- **Redazione guidata dello statuto CER** - finalita', soggetti ammessi, governance, ripartizione benefici
- **Simulazione autoconsumo condiviso e flussi economici** - energia condivisa oraria, TIP, tariffa di restituzione (TR), contributo PNRR
- **Checklist qualifica GSE (CACER + TIP + PNRR)** - documenti, dati impianto, dati referente, allegati

## Installazione

```bash
# Claude Code
ln -sfn "$(pwd)/skills/cer-cacer-configurazione-gse" "$HOME/.claude/skills/cer-cacer-configurazione-gse"

# OpenAI Codex
ln -sfn "$(pwd)/skills/cer-cacer-configurazione-gse" "$HOME/.agents/skills/cer-cacer-configurazione-gse"
```

Riavviare l'agent per la discovery.

## Fonti consultate

- D.Lgs. 8 novembre 2021 n. 199, art. 30, 31, 32 (recepimento RED II)
- DM MASE 7 dicembre 2023 n. 414 (Decreto CACER, testo originario)
- DM MASE 16 maggio 2025 n. 127 (modifiche al DM 414/2023)
- DL 19 febbraio 2026 n. 19, art. 27 (Decreto PNRR 2026, ulteriori modifiche al regime PNRR CACER - **regime vigente al 2026-05-07**)
- Delibera ARERA 727/2022/R/eel - TIAD (Testo Integrato Autoconsumo Diffuso)
- Regole Operative CACER del GSE (Allegato 1 - procedure di qualifica)

Dettaglio completo con URL, hash e date di consultazione in [`references/sources.yaml`](references/sources.yaml). Estratti operativi in [`references/estratti/`](references/estratti/).

## Limiti noti

- Non produce statuti pronti per la formalizzazione: a seconda della forma giuridica scelta, lo statuto va finalizzato con atto pubblico presso notaio, scrittura privata autenticata, procedura RUNTS per gli enti del terzo settore, ecc.
- Non sostituisce il calcolo ufficiale GSE dell'energia condivisa, eseguito su dati di misura orari.
- Non determina importi puntuali della TIP: la parte variabile dipende dal prezzo zonale e va validata sulle pubblicazioni GSE/MASE vigenti.
- Non gestisce aspetti fiscali, antitrust o aiuti di Stato.
- Non sostituisce la mappa cabine primarie pubblicata dal GSE.

Per ogni dubbio significativo, rinvio al **soggetto referente** della CACER, al **professionista firmatario** della relazione tecnica, al **soggetto chiamato a formalizzare lo statuto** secondo la forma giuridica scelta (notaio per atto pubblico, intermediario abilitato per scrittura privata autenticata, procedura RUNTS per ETS, ecc.), al **commercialista** per gli aspetti fiscali e al **GSE** per la qualifica formale.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
