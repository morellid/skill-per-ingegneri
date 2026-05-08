# AGENTS.md - carichi-atmosferici-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per il calcolo dei carichi atmosferici (vento ai sensi NTC 2018 par. 3.3 e neve ai sensi par. 3.4) su edifici civili e industriali correnti. Riferimenti normativi: DM 17/01/2018 (NTC 2018) e Circolare MIT 21/01/2019 n. 7 - entrambi pubblici e disponibili su Gazzetta Ufficiale. Target: ingegneri strutturisti italiani che progettano nuove costruzioni o valutano costruzioni esistenti.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **NTC 2018** (DM 17/01/2018) - id `ntc2018-dm-17-01-2018`, hash da calcolare al fetch (`./scripts/fetch-sources.sh`)
- **Circ. 7/2019 MIT** (21/01/2019) - id `circ-7-2019-mit`, hash da calcolare al fetch

Estratti pertinenti in `references/estratti/`:
- `ntc2018-par-3-3.md` - par. 3.3: vento (eq. 3.3.1 p, 3.3.2 v_b, 3.3.3 c_r, 3.3.4 q_r, 3.3.5 c_e), Tab. 3.3.II categorie esposizione I-V
- `ntc2018-par-3-4.md` - par. 3.4: neve (eq. 3.4.1 q_s, q_sk per zona, mu_1, c_E)
- `circ-7-2019-c-3-3-3-4.md` - C3.3 e C3.4: commento applicativo, esempi numerici

## Articoli e punti chiave

### Vento (NTC par. 3.3)

- **par. 3.3.1**: pressione del vento p = q_r * c_e * c_p * c_d (eq. 3.3.1)
- **par. 3.3.2**: velocita' di riferimento v_b in funzione di a_s vs a_0 (eq. 3.3.2). Tab. 3.3.I dei parametri zonali (v_b_0, a_0, k_s) NON incorporata nella skill: input dell'utente
- **par. 3.3.4**: c_r per T_R != 50 anni (eq. 3.3.3); q_r = 0.5 * rho * v_r^2 con rho = 1.25 kg/m^3 (eq. 3.3.4)
- **par. 3.3.7**: c_e(z) = k_r^2 * c_t * ln(z/z_0) * [7 + c_t * ln(z/z_0)] (eq. 3.3.5); Tab. 3.3.II (k_r, z_0, z_min) per categorie I/II/III/IV/V incorporata
- **par. 3.3.8**: c_p coefficienti di forma - NON incorporato, input dell'utente da NTC o Circolare
- **par. 3.3.9**: c_d coefficiente dinamico - default 1, fuori scope per strutture sensibili

### Neve (NTC par. 3.4)

- **par. 3.4.1**: q_s = mu_1 * q_sk * c_E * c_t (eq. 3.4.1)
- **par. 3.4.2**: q_sk per Zona I-Alpina, I-Mediterranea, II, III; formule a tratti su a_s con soglia 200 m. Le 4 zone e le formule sono incorporate nel modulo
- **par. 3.4.3**: c_E (Tab. 3.4.I): battuta dai venti = 0.9; normale = 1.0; riparata = 1.1
- **par. 3.4.4**: c_t coefficiente termico, default 1.0
- **par. 3.4.5.2.1**: mu_1 per copertura ad una/due falde; alpha <= 30 -> 0.8; 30 < alpha < 60 -> 0.8 * (60 - alpha)/30; alpha >= 60 -> 0
- **par. 3.4.5.5**: accumuli, deriva - NON coperti

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti sono materiale di citazione normativa: ti servono per spiegare i passaggi, NON per riprodurre v_b, c_r, q_r, c_e, p, q_sk, mu_1, q_s in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/carichi_atmosferici.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non inventare i parametri zonali del vento** (v_b_0, a_0, k_s): la skill non incorpora Tab. 3.3.I e li richiede all'utente. Mai estrarli da memoria o da training data: chiedere all'utente di consultare NTC Tab. 3.3.I per la zona del sito.
- **Non assegnare automaticamente la categoria di esposizione I-V**: NTC Tab. 3.3.III dipende da rugosita' del territorio, distanza dalla costa, altitudine, raccordi tra zone. Va dichiarata dall'utente; chiedere conferma se ambigua.
- **Non confondere zona vento con zona neve**: sono mappe diverse. Anche la nomenclatura interna NTC differisce: zona vento = numero (1-9, NON incorporata); zona neve = stringa (I-Alpina, I-Mediterranea, II, III).
- **Non eseguire il calcolo per a_s > 1500 m (vento)**: NTC par. 3.3.2 richiede indagine specifica. Il modulo solleva ValueError; riportare il messaggio bloccante e suggerire indagine specifica al sito.
- **Non eseguire il calcolo per c_p su geometrie non correnti**: cupole, ciminiere, ponti, segnali, paratie -> NTC par. 3.3.8 rinvia a documenti di comprovata validita' o prove sperimentali. La skill richiede c_p come input numerico; se l'utente non lo ha, rinviare al progettista.
- **Non sostituire mu_1 con mu_2 o mu_3** (carichi accidentali a deriva, accumulo, sporgenze): la skill copre solo mu_1 per copertura ad una/due falde regolari (par. 3.4.5.2.1). Per accumuli (par. 3.4.5.5) la skill rinvia a calcolo separato.
- **Non confondere q_sk (al suolo, kN/m^2) con q_s (sulla copertura, kN/m^2)**: q_s = mu_1 * q_sk * c_E * c_t.
- **Non usare path relativi tipo `tasks/lib/carichi_atmosferici.py`** nei comandi Bash: usa sempre `${CLAUDE_SKILL_DIR}/tasks/lib/carichi_atmosferici.py` (Claude Code) o il path assoluto della skill installata (Codex / altri).

### Cosa fare

- **Citare sempre il paragrafo NTC** per ogni passaggio (es. "v_b = v_b_0 * (1 + k_s * (a_s/a_0 - 1)) - eq. 3.3.2 NTC", "mu_1 = 0.8 * (60 - alpha)/30 - par. 3.4.5.2.1 NTC").
- **Eseguire il modulo Python** per il calcolo, non riprodurre i numeri "a mano". Output del modulo + parafrasi in linguaggio naturale.
- **Mostrare la struttura completa**: prima i dati di input (zona, altitudine, esposizione, geometria), poi i valori intermedi (v_b, c_r, q_r, c_e o q_sk, mu_1, c_E), poi l'output finale (p o q_s) in N/m^2 e/o kN/m^2.
- **Concludere con rinvio al progettista**: "L'output e' un valore caratteristico, va combinato con gli altri carichi via skill `combinazioni-carico-ntc` o software di calcolo strutturale e verificato dal progettista firmatario."
- **Quando c_p e' incerto**: rinviare il calcolo al progettista o suggerire valori di letteratura (es. CNR-DT 207/2008) come orientamento, senza fissarli automaticamente.
- **Quando l'utente fornisce zona vento non standard** (numero non in 1-9, "speciale", ecc.): chiedere comunque parametri zonali numerici espliciti dalla Tab. 3.3.I.

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere strutturista che esegua confronto vs casi pubblicati (es. esempi Circolare C3.3 e C3.4) o vs software di calcolo strutturale certificato su almeno 5 casi reali per ciascuna formula (5 vento + 5 neve).

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh carichi-atmosferici-ntc`); test suite Python: 46/46 pass (12 classi: velocita' di riferimento con raccordo a_s = a_0 e validazione fuori dominio, c_r in [5, 500] anni con monotonia, q_r formula chiusa, c_e per categorie I-V con clamp z_min e formula esplicita per cat. II, vento end-to-end con T_R != 50, q_sk per 4 zone con raccordo a 200 m e formula esplicita zona Alpina 1000 m, mu_1 con raccordo a 30 e 60 deg, c_E neve con normalizzazione case/spazi/trattini, neve end-to-end, CLI vento/neve con error handling per campi mancanti e zone invalide). Livello 2 (confronto vs casi pubblicati) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-vento.md`
  - `tasks/calcola-neve.md`
- Modulo di calcolo: `tasks/lib/carichi_atmosferici.py` + `tasks/lib/test_carichi_atmosferici.py`
- Esempi: 1 conforme (`caso-conforme-zona1-pianura-cat-II`) + 1 problematico (`caso-problematico-quota-oltre-1500`)
