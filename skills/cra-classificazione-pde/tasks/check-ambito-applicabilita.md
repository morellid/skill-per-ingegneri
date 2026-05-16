# Task: Verifica ambito di applicabilita' del CRA

## Obiettivo

Determinare se un prodotto rientra nell'ambito del **Regolamento (UE) 2024/2847 - Cyber Resilience Act**. La risposta e' un giudizio binario (rientra / non rientra) **motivato** con citazione puntuale degli artt. 2 e 3, indicando eventuali esclusioni applicabili.

## Input richiesti

Chiedere all'utente, prima di applicare la procedura:

1. **Denominazione commerciale** o tipologia del prodotto (es. "router Wi-Fi consumer modello X", "ipervisore enterprise", "software SCADA").
2. **Natura del prodotto**: software, hardware, o combinazione.
3. **Connessione dati**: il prodotto e' progettato o si prevede ragionevolmente che si connetta a un altro dispositivo o a una rete (logica o fisica, diretta o indiretta)?
4. **Eventuali regolamenti settoriali applicabili**: il prodotto e' un dispositivo medico (Reg. 2017/745 o 2017/746), un componente di veicolo a motore omologato (Reg. 2019/2144), un PDE certificato per aviazione civile (Reg. 2018/1139), un equipaggiamento marittimo (Direttiva 2014/90/UE), o e' sviluppato esclusivamente per sicurezza nazionale/difesa/informazioni classificate?
5. **Pezzo di ricambio identico**: il prodotto e' fabbricato come ricambio con le stesse specifiche del componente sostituito (art. 2 par. 6)?

Se uno qualsiasi di questi input manca, chiedi all'utente prima di procedere.

## Fonti

Procedura ancorata a:
- `references/estratti/reg-ue-2024-2847-cra-classificazione.md` sezione "1. Ambito di applicazione".
- `references/fonti/reg-ue-2024-2847-cra.md` (art. 2, art. 3).

## Procedura

**Step A - Filtro positivo (art. 2 par. 1 + art. 3 punto 1)**:

A1. Verifica che il prodotto sia un **PDE** ex art. 3 punto 1: "qualsiasi prodotto software o hardware e le relative soluzioni di elaborazione dati da remoto, compresi i componenti software o hardware immessi sul mercato separatamente".
- Se il prodotto NON e' software ne' hardware con elaborazione dati: **non e' un PDE**, fine procedura con esito **fuori ambito**.

A2. Verifica la **finalita' prevista o l'uso ragionevolmente prevedibile**: include una **connessione dati logica o fisica diretta o indiretta a un dispositivo o a una rete** (art. 2 par. 1)?
- Se il prodotto e' fully air-gapped e nessun uso ragionevolmente prevedibile prevede connessione dati: **non rientra**, fine procedura con esito **fuori ambito**.
- Se il prodotto si connette ad altro dispositivo/rete o e' ragionevolmente prevedibile che lo faccia: prosegui.

**Step B - Esclusioni puntuali (art. 2 par. 2-4, 6-7)**:

B1. Il prodotto rientra nell'ambito di **Reg. (UE) 2017/745** (dispositivi medici) o **Reg. (UE) 2017/746** (diagnostici medici in vitro) o **Reg. (UE) 2019/2144** (omologazione veicoli a motore)? **->** se si', e' escluso (art. 2 par. 2). Fine procedura con esito **fuori ambito**.

B2. Il prodotto e' un PDE **certificato in conformita' del Reg. (UE) 2018/1139** (aviazione civile)? **->** se si', escluso (art. 2 par. 3). Fine procedura con esito **fuori ambito**.

B3. Il prodotto e' equipaggiamento nell'ambito della **Direttiva 2014/90/UE** (equipaggiamento marittimo)? **->** se si', escluso (art. 2 par. 4). Fine procedura con esito **fuori ambito**.

B4. Il prodotto e' un **pezzo di ricambio** messo a disposizione per sostituire componenti identici, fabbricato secondo le stesse specifiche del componente sostituito? **->** se si', escluso (art. 2 par. 6). Fine procedura con esito **fuori ambito**.

B5. Il prodotto e' sviluppato o modificato **esclusivamente per scopi di sicurezza nazionale o di difesa**, o specificamente progettato per **trattare informazioni classificate**? **->** se si', escluso (art. 2 par. 7). Fine procedura con esito **fuori ambito**.

**Step C - Se nessuna esclusione si applica**: il prodotto **rientra nell'ambito del CRA**. Procedi alla classificazione (rinvia l'utente al task `classifica-pde.md`).

**Step D - Casi di confine (sovrapposizione con altre norme dell'Unione, art. 2 par. 5)**: se altre normative dell'Unione coprono **tutti o alcuni dei rischi** dei requisiti essenziali dell'Allegato I del CRA, **segnala il dubbio**: l'art. 2 par. 5 prevede che la Commissione possa limitare/escludere l'applicazione del CRA con atti delegati, e che le norme settoriali devono garantire un livello di protezione pari o superiore. La skill non si pronuncia su questa valutazione: rinvia al consulente legale del fabbricante.

## Output atteso

Risposta strutturata in 4 sezioni:

```
1. Sintesi dell'esito:
   - Esito: [RIENTRA nell'ambito del CRA / NON RIENTRA / DA VALUTARE in concertazione con consulente legale]
   - Motivazione (1-2 frasi).

2. Verifica dell'art. 2 par. 1 (filtro positivo):
   - Il prodotto e' un PDE ex art. 3 punto 1? [si/no, con motivazione]
   - Il prodotto ha (o si prevede ragionevolmente che abbia) una connessione dati a dispositivo/rete? [si/no, con motivazione]

3. Verifica delle esclusioni (art. 2 par. 2-4, 6-7):
   - Reg. 2017/745 / 2017/746 (medicali): [non applicabile / applicabile -> escluso]
   - Reg. 2019/2144 (veicoli motore): [non applicabile / applicabile -> escluso]
   - Reg. 2018/1139 (aviazione civile, prodotto certificato): [non applicabile / applicabile -> escluso]
   - Direttiva 2014/90/UE (equipaggiamento marittimo): [non applicabile / applicabile -> escluso]
   - Pezzo di ricambio identico (art. 2 par. 6): [non applicabile / applicabile -> escluso]
   - Sicurezza nazionale/difesa/informazioni classificate (art. 2 par. 7): [non applicabile / applicabile -> escluso]

4. Note e prossimi passi:
   - [Eventuali zone d'ombra, sovrapposizioni con altre norme settoriali ex art. 2 par. 5]
   - Se rientra: prosegui con task `classifica-pde.md`.
   - Se non rientra: il prodotto puo' essere comunque soggetto ad altre normative di armonizzazione; verificare con il responsabile compliance.

Disclaimer: questa verifica e' un ausilio alla riflessione tecnica. La responsabilita' della corretta inquadramento ricade sul fabbricante o sul rappresentante autorizzato ex art. 13 e 18-21 del Regolamento (UE) 2024/2847.
```

## Limiti

- Il task non valuta gli atti delegati che la Commissione puo' adottare ex art. 2 par. 5 per limitare/escludere l'applicazione del CRA: in casi di sovrapposizione settoriale, rinvia al consulente legale.
- Il task non interpreta la **definizione di "elaborazione dati da remoto"** in casi limite (es. SaaS dove l'utente locale non ha software installato): per questi casi rinvia al considerando 11 del Regolamento (UE) 2024/2847 e/o al fabbricante.
- Il task non valuta se un prodotto **gia' immesso sul mercato prima dell'11 dicembre 2027** richieda riadeguamento: l'art. 69 par. 2 prevede che siano soggetti al regolamento solo se sottoposti a **modifiche sostanziali** dopo tale data (con la deroga dell'art. 14 segnalazione, che si applica a tutti i prodotti in ambito immessi anche prima).
