# CBAM Declarant - Reg. (UE) 2023/956 fase definitiva

> Versione: 0.1.0-alpha
> Stato: alpha (validazione di Livello 1 - autore + lettura adversarial delle fonti)

Skill di supporto al **dichiarante CBAM autorizzato** (importatore stabilito UE o rappresentante doganale indiretto) negli adempimenti del Carbon Border Adjustment Mechanism nella fase definitiva (dal **1° gennaio 2026**), per come disciplinato dal Regolamento (UE) 2023/956 come modificato dal Reg. (UE) 2025/2083 (Omnibus CBAM).

## Target

Importatore di merci CBAM (Allegato I) stabilito UE; rappresentante doganale indiretto; responsabile dogane / compliance / supply chain di azienda importatrice; consulente fiscale, legale o doganale che li supporta.

**Non destinata a**: operatori extra-UE / gestori di impianti di paesi terzi (lato Art. 10), verificatori accreditati (Art. 18 + Reg. esec. 2018/2067), autorita' competenti (MASE per Italia) o autorita' doganali (ADM).

## Cosa fa

Quattro sotto-attivita' (file in `tasks/`):

- **Verifica della qualifica e applicabilita' delle deroghe** [`tasks/check-qualifica-e-deroghe.md`] - valuta se serve la qualifica di dichiarante CBAM autorizzato, se si applica l'**esenzione de minimis** (Art. 2bis, soglia **50 t/anno civile**), e quale **codice TARIC** dichiarativo utilizzare (Y128 vs Y134-Y137-Y237-Y238).
- **Pianificazione equilibrio trimestrale 50 %** [`tasks/plan-equilibrio-trimestrale.md`] - stima dei certificati CBAM da detenere sul conto al termine di ogni trimestre **dal 2027** (Art. 22 §2), via valori predefiniti senza maggiorazione (lettera a) o via baseline dell'anno precedente (lettera b); calendario di acquisto sulla **piattaforma centrale comune** (dal 1/2/2027, Art. 20 §1).
- **Redazione dichiarazione CBAM annuale** [`tasks/draft-dichiarazione-cbam-annuale.md`] - check-list dei contenuti obbligatori della dichiarazione annuale Art. 6 (entro 30/9, **prima volta nel 2027 per l'anno 2026**), inclusa la coerenza con le dichiarazioni doganali Hx, la gestione di emissioni effettive vs predefinite (Art. 7) e la documentazione per la detrazione del carbon price paese terzo (Art. 9).
- **Valutazione esposizione sanzionatoria** [`tasks/assess-rischio-sanzionatorio.md`] - mappa dell'esposizione Art. 26 §§1, 1bis, 2, 2bis, 4bis: mancata restituzione, importazione non consentita o autorizzazione respinta (moltiplicatore 3x-5x), non autorizzato che supera la soglia (sanzione su tutte le emissioni dell'anno).

Per il dettaglio operativo vedi `SKILL.md`.

## Installazione

Vedi `README.md` alla root del repo per istruzioni generali di installazione delle skill in Claude Code e in OpenAI Codex.

## Fonti consultate

- **Regolamento (UE) 2023/956 (CBAM)** - testo consolidato 20/10/2025 (incorpora le modifiche del Reg. (UE) 2025/2083).
- **Regolamento (UE) 2025/2083** (Omnibus CBAM) dell'8/10/2025.
- **Circolare ADM n. 36/2025** del 24/12/2025 - avvio fase definitiva CBAM in Italia (codici TARIC, articolazioni territoriali).
- **Avviso ADM del 21/10/2025** - conseguenze in caso di mancata qualifica.

Dettagli (SHA256, URL, accessed, binary path, md path, estratti) in `references/sources.yaml`.

## Limiti noti

La skill **non**:

- Sostituisce il giudizio del professionista responsabile (responsabile compliance, consulente doganale/fiscale, rappresentante legale) sulle interpretazioni di confine: qualificazione di "importatore" ai fini CBAM (Art. 3 punto 15), applicabilita' dell'esenzione de minimis (Art. 2bis) in casi di importazioni miste / perfezionamenti / reintroduzioni, pratiche di elusione (Art. 27 §2 lettera b), determinazione del prezzo del carbonio pagato in paese terzo (Art. 9).
- Produce **documenti pronti al deposito** nel registro CBAM (domanda di autorizzazione Art. 5 §§5-7, dichiarazione CBAM annuale Art. 6, richiesta di riacquisto Art. 23) ne' attestazioni di conformita'.
- Calcola **emissioni effettive** ex Allegato IV punti 2-3 (richiede dati impianto del gestore paese terzo + verifica del verificatore accreditato Art. 8).
- Calcola l'**adeguamento per l'assegnazione gratuita** Art. 31 (atti di esecuzione in evoluzione legati al phase-out delle quote ETS free).
- Sostituisce la consulenza del **MASE** (autorita' competente nazionale CBAM) sul procedimento autorizzatorio, ne' la consulenza di **ADM** su questioni prettamente doganali (perfezionamenti attivi/passivi, reintroduzioni, origine).
- Valuta gli **atti delegati e di esecuzione** di secondo livello (in continua evoluzione) richiamati dal Reg. CBAM consolidato (artt. 2 §§10-11, 2bis §3, 7 §7, 9 §5, 14 §6, 18 §3, 20 §§5bis-6, 21 §3, 27 §6).

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
