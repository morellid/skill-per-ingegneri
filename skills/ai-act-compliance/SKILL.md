---
name: ai-act-compliance
description: Verifica la conformita' di un sistema di IA al Reg. UE 2024/1689 (AI Act). Classifica il sistema (vietato / alto rischio / rischio limitato / GPAI), identifica gli obblighi applicabili per fornitore e deployer, e guida la redazione dei documenti richiesti. Use when user asks to assess an AI system for EU AI Act compliance, identify applicable obligations, or classify a system under the regulation.
license: MIT
---

# AI Act Compliance (Reg. UE 2024/1689)

## Quando usare questa skill

Usa questa skill quando un ingegnere o un team tecnico deve:
- Classificare un sistema di IA secondo il Reg. UE 2024/1689 (vietato / alto rischio Allegato III / rischio limitato / GPAI)
- Identificare gli obblighi applicabili come fornitore (provider) o deployer di un sistema di IA
- Verificare la conformita' agli obblighi di trasparenza (art. 50)
- Valutare se un modello rientra nella categoria GPAI con rischio sistemico (art. 51)
- Supportare la redazione della FRIA (Fundamental Rights Impact Assessment, art. 27)

Non e' adatta a:
- Sostituire consulenza legale per casi complessi o contenziosi
- Coprire normative nazionali di attuazione (DDL italiano AI Act, linee guida AGID) non ancora disponibili
- Certificazione o audit ufficiale

**Target**: ingegneri software, product manager, responsabili tecnici che sviluppano o mettono in servizio sistemi di IA nell'Unione europea.

## Avvertenza

Questa skill e' uno strumento di supporto tecnico alla verifica di conformita'. **Non sostituisce il giudizio del professionista legale.** Gli output sono orientativi e devono essere validati da un consulente legale prima di decisioni operative. La skill non produce documenti pronti al deposito o alla firma.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il file task appropriato:

- **Classificazione sistema**: quando l'utente chiede di classificare un sistema di IA (vietato? alto rischio? rischio limitato?), leggere `tasks/classifica-sistema.md`
- **Obblighi fornitore alto rischio**: quando l'utente e' fornitore di un sistema ad alto rischio e chiede quali obblighi deve rispettare, leggere `tasks/check-high-risk-provider.md`
- **Obblighi deployer alto rischio**: quando l'utente deployer vuole verificare i propri obblighi (art. 26, 27), leggere `tasks/check-deployer-obligations.md`
- **Obblighi GPAI provider**: quando l'utente sviluppa o distribuisce un modello GPAI (es. LLM), leggere `tasks/check-gpai-provider.md`
- **Trasparenza (art. 50)**: quando l'utente vuole verificare gli obblighi di disclosure per chatbot, deep fake, emozioni, contenuti sintetici, leggere `tasks/check-trasparenza.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera o proponi la classificazione come primo step.

## Processo generale

1. Identifica il ruolo dell'utente (fornitore / deployer / entrambi) e il tipo di sistema (IA system, GPAI model, sistema integrato)
2. Esegui prima la classificazione (`tasks/classifica-sistema.md`) se il sistema non e' gia' classificato
3. Carica il task file pertinente al ruolo e alla categoria del sistema
4. Richiedi gli input necessari come specificato nel task (descrizione del sistema, finalita' prevista, settore di utilizzo)
5. Applica la procedura descritta nel task
6. Produci l'output nel formato atteso
7. Indica sempre le date di applicazione pertinenti (le obbligazioni entrano in vigore in date diverse)
8. Includi sempre un rinvio alla verifica del professionista legale per i punti critici

## Date di applicazione (art. 113)

| Obblighi | Applicazione |
|----------|-------------|
| Pratiche vietate (art. 5), alfabetizzazione (art. 4) | 2 febbraio 2025 - **gia' in vigore** |
| GPAI (capo V), governance, sanzioni GPAI | 2 agosto 2025 - **gia' in vigore** |
| Alto rischio Allegato III, trasparenza art. 50, FRIA art. 27 | 2 agosto 2026 |
| Alto rischio Allegato I (componenti sicurezza prodotti) | 2 agosto 2027 |

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione fedele della fonte in `references/fonti/ai-act-it-eurlex.md`. Estratti tematici in `references/estratti/`.

## Limiti

Cosa questa skill NON fa:
- Non produce dichiarazioni di conformita' CE
- Non sostituisce valutazioni di conformita' da parte di organismi notificati
- Non copre la normativa settoriale di armonizzazione dell'Allegato I (dispositivi medici, macchine, ecc.)
- Non interpreta normativa ambigua senza rinvio al professionista legale
- Non tiene aggiornamento automatico per atti delegati della Commissione che modificano Allegato III o soglie art. 51
