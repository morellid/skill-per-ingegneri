# AGENTS.md - predimensionamento-flessione-ca-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill code-driven per il pre-dimensionamento SLU in flessione semplice di sezioni rettangolari in c.a. singolarmente armate, ai sensi delle NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2. Riferimenti normativi: DM 17/01/2018 (NTC 2018) e Circolare MIT 21/01/2019 n. 7 - entrambi pubblici e disponibili su Gazzetta Ufficiale. Target: ingegneri strutturisti italiani in fase di pre-dimensionamento.

## Fonti autoritative

Catalogate in `references/sources.yaml`. Sintesi:

- **NTC 2018** (DM 17/01/2018) - id `ntc2018-dm-17-01-2018`, hash da calcolare al fetch
- **Circ. 7/2019 MIT** (21/01/2019) - id `circ-7-2019-mit`, hash da calcolare al fetch

Estratti pertinenti in `references/estratti/`:
- `ntc2018-par-4-1-2.md` - par. 4.1.2.1 (resistenze, diagrammi materiali) e 4.1.2.3.4.2 (flessione SLU)
- `circ-7-2019-c-4-1-2.md` - C4.1.2 commento applicativo

## Articoli e punti chiave

- **NTC par. 4.1.2.1.1.1** - calcestruzzo: f_cd = alpha_cc * fck / gamma_c (eq. [4.1.3]); alpha_cc = 0.85; gamma_c = 1.5 (PERS); per fck <= 50 MPa stress-block rettangolare con lambda = 0.8, eta = 1; per fck > 50 MPa lambda e eta riducono progressivamente (eq. 4.1.10-4.1.11) - **fuori scope skill**
- **NTC par. 11.3.2.1** - acciaio: Es = 200000 MPa (valore standardizzato); eps_yd = fyd / Es
- **NTC par. 4.1.2.1.1.3** - acciaio: f_yd = fyk / gamma_s (eq. [4.1.5]); gamma_s = 1.15 (PERS)
- **NTC par. 4.1.2.3.4.2** - flessione semplice SLU: equilibrio sezione, eps_cu = 0.0035 (Classe 1), zona snervata acciaio, formula M_Rd = A_s * f_yd * z con z = d - 0.4 x (per stress-block lambda = 0.8)
- **NTC 2018 par. 4.1.1.1** - limite x/d <= 0.45 per fck <= 50 MPa (eq. [4.1.1], ridistribuzione momenti travi continue/solette) - NON limite universale per flessione semplice
- **Circ. 7/2019 par. C4.1.2.3.4.2** - duttilita' di curvatura richiesta esplicitamente solo al Cap. 7 NTC (zona sismica); per flessione semplice non sismica la condizione necessaria e' eps_s >= eps_yd

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano" leggendo le formule dagli estratti.** Gli estratti sono materiale di citazione normativa: ti servono per spiegare i passaggi, NON per riprodurre f_cd, f_yd, x, eps_s, z, M_Rd in chat. L'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/flessione_ca.py`. Calcolare a mano introduce errore stocastico LLM e annulla la ragion d'essere code-driven della skill.
- **Non dedurre A_s da numero e diametro barre senza conferma utente**: errore tipico LLM. Es. "3 phi 16" -> A_s = 3 * pi * 16^2 / 4 = 603.19 mm^2. Devi chiedere o presentare il calcolo per verifica esplicita all'utente, oppure passarlo al modulo Python; non improvvisare a memoria.
- **Non assumere d = h - 30 mm o simili**: il copriferro varia con classe esposizione, diametro staffe, diametro barra principale. Va dichiarato o calcolato dall'utente; la skill non lo fa.
- **Non eseguire il calcolo per fck > 50 MPa**: NTC par. 4.1.2.1.1 richiede formulazione modificata (lambda, eta < 1). Il modulo solleva ValueError; riportare il messaggio bloccante e suggerire software di calcolo strutturale completo.
- **Non eseguire il calcolo per sezioni sovra-armate**: quando eps_s < eps_yd, la formula M_Rd = A_s * fyd * z sovrastima la resistenza (l'acciaio non snerva, ma la formula assume sigma_s = fyd). Il modulo solleva ValueError; rinviare a calcolo iterativo o software esterno.
- **Non confondere flessione semplice con pressoflessione**: la skill assume sforzo assiale N = 0. Per N != 0 (pilastri, pareti, archi) servono diagrammi di interazione M-N, fuori scope.
- **Non applicare la skill in zona sismica CD"A" / CD"B" senza avvertire**: NTC par. 7.4.4 e 7.4.6 introducono limitazioni di progettazione capacitiva (limiti su rho_min, rho_max, sovraresistenza, gerarchia delle resistenze) che la skill non verifica.
- **Non confondere M_Ed (sollecitazione) con M_Rd (resistente)**: la skill calcola M_Rd; il confronto M_Ed <= M_Rd resta in capo al progettista, dopo aver calcolato le sollecitazioni di una combinazione SLU (vedi skill `combinazioni-carico-ntc`).
- **Non usare path relativi tipo `tasks/lib/flessione_ca.py`** nei comandi Bash: usa sempre `${CLAUDE_SKILL_DIR}/tasks/lib/flessione_ca.py` (Claude Code) o il path assoluto della skill installata (Codex / altri).

### Cosa fare

- **Citare sempre il paragrafo NTC** per ogni passaggio (es. "f_cd = alpha_cc * fck / gamma_c - eq. [4.1.3] NTC par. 4.1.2.1.1.1", "eps_yd = f_yd / Es - Es da NTC par. 11.3.2.1", "z = d - 0.4 x - stress-block lambda = 0.8 NTC par. 4.1.2.1.2.1").
- **Eseguire il modulo Python** per il calcolo, non riprodurre i numeri "a mano". Output del modulo + parafrasi in linguaggio naturale.
- **Mostrare la struttura completa**: prima i dati di input (geometria, armatura, materiali), poi i materiali derivati (f_cd, f_yd, eps_yd), poi geometria interna (x, x/d, eps_s, z), poi l'output (M_Rd in kNm), poi le avvertenze di duttilita'.
- **Concludere con rinvio al progettista**: "L'output e' un pre-dimensionamento. Restano a carico del progettista la verifica completa con software di calcolo strutturale, le verifiche SLE (fessurazione, deformazione), le verifiche di taglio/torsione, e in zona sismica i requisiti di duttilita' e gerarchia delle resistenze."
- **Quando l'utente non e' sicuro su classe calcestruzzo o acciaio**: B450C (fyk = 450 MPa) e' lo standard italiano; C25/30 (fck = 25 MPa) e' molto comune in edilizia ordinaria; chiedere o suggerire come default ragionevole previa conferma.
- **Quando il modulo segnala sezione sovra-armata**: NON aggirare l'errore. Suggerire al progettista di aumentare b, h o d, o di ridurre A_s, o di passare a calcolo iterativo con sigma_s elastico (fuori scope skill).

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere strutturista che esegua confronto vs casi pubblicati (manuali Pozzati/Rugarli/Aurelio Ghersi/altri testi standard di tecnica delle costruzioni) o vs software di calcolo strutturale certificato (es. SAP2000, MidasGen, ProSAP, EdiLus) su almeno 5 casi reali, copertura: classi C20/25, C25/30, C30/37, C32/40, C45/55; B450A e B450C; sezioni rettangolari e quadrate; rapporti di armatura bassi (~ 0.5%) e medi (~ 1.5%).

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 self-check OK (`./scripts/validate.sh predimensionamento-flessione-ca-ntc`); test suite Python: 34/34 pass (8 classi: materiali f_cd / f_yd / eps_yd con varianti alpha_cc e gamma; equilibrio asse neutro x; deformazione acciaio eps_s con clamp x < d; end-to-end caso standard 300x500 con 3 phi 16 e C25/30 + B450C; monotonia M_Rd in A_s/d/fck; avvertenza zeta > 0.45; rifiuto fck > 50 MPa, d > h, sezione sovra-armata, input non finiti/negativi; CLI con error handling per campi mancanti, fck invalido, sovra-armata). Livello 2 (confronto vs casi pubblicati) da completare prima del release stabile.
- Task files:
  - `tasks/calcola-m-rd.md`
- Modulo di calcolo: `tasks/lib/flessione_ca.py` + `tasks/lib/test_flessione_ca.py`
- Esempi: 1 conforme (`caso-conforme-300x500-3phi16-C25-30`) + 1 problematico (`caso-problematico-sovra-armata`)
