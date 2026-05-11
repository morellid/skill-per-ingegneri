---
name: predimensionamento-flessione-ca-ntc
description: Calcola il momento resistente M_Rd di una sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU, ai sensi delle NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2. Dato b, h, d, A_s, fck (<= 50 MPa Classe 1), fyk e i parametri di sicurezza, restituisce f_cd, f_yd, eps_yd, profondita' asse neutro x, rapporto x/d, deformazione acciaio eps_s, braccio leva z = d - 0.4 x e M_Rd in kNm. Usa il diagramma stress-block rettangolare equivalente (eta = 1, lambda = 0.8). Verifica duttilita' (snervamento acciaio + raccomandazione x/d <= 0.45). Implementazione code-driven, deterministica. Use when an Italian structural engineer asks to pre-dimension a singly-reinforced rectangular RC section in bending under NTC 2018, compute the resisting moment, or audit values produced by other software. Target users are structural engineers in pre-design phase; the skill does not replace full software verification.
license: MIT
---

# Pre-dimensionamento sezione c.a. SLU flessione semplice (NTC 2018 par. 4.1.2)

## Quando usare questa skill

Usare quando un ingegnere strutturista italiano deve:
- Pre-dimensionare una sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU, ai sensi di NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2
- Calcolare M_Rd di una sezione esistente data l'armatura tesa A_s, per confrontarla con il momento sollecitante M_Ed di una combinazione SLU
- Determinare profondita' asse neutro x e rapporto x/d per valutare duttilita' della sezione (raccomandazione Circolare 7/2019 C4.1.2: x/d <= 0.45)
- Verificare valori prodotti da altri software o fogli di calcolo

**Non usare** quando l'utente chiede:
- Sezioni doppiamente armate (con armatura compressa A's): la skill v0.1 copre solo singolarmente armate. Per A's significativa il progettista deve usare software di calcolo strutturale o calcolo iterativo separato
- Sezioni a T, L, circolari, cave, profili speciali: la skill copre solo rettangolari b x h piene
- Calcestruzzi ad alta resistenza fck > 50 MPa (Classe 2): NTC eq. 4.1.10-4.1.11 richiede stress-block con eta < 1 e lambda < 0.8 - fuori scope
- Pressoflessione retta o deviata: la skill copre solo flessione semplice (sforzo assiale = 0)
- Sezioni sovra-armate (sovra dosaggio acciaio): la skill rifiuta il calcolo perche' la formula M_Rd = A_s * fyd * z non vale quando l'acciaio non snerva al collasso
- Verifica SLE (fessurazione, deformabilita'): la skill copre solo SLU
- Verifica taglio, torsione, punzonamento: skill diversa
- Strutture in zona sismica con fattore q > 1.5 (CD"A" / CD"B"): le NTC par. 7.4.4 e 7.4.6 prescrivono limiti di progettazione capacitiva piu' stringenti. La skill non li applica; il progettista deve verificarli a parte
- Combinazione delle azioni: per la matrice di combinazioni SLU vedi la skill `combinazioni-carico-ntc`

## Avvertenza

Questa skill e' uno strumento di **PRE-DIMENSIONAMENTO** della flessione semplice SLU per sezioni rettangolari in c.a. singolarmente armate. **Non sostituisce il giudizio del progettista strutturale firmatario, ne' la verifica completa con software di calcolo strutturale.** L'output e' deterministico (formule chiuse) ed e' confrontabile dal progettista contro fogli di calcolo o software certificati: il confronto resta in capo al professionista. **Nello stato v0.1.0-alpha la skill non e' ancora stata validata con confronto numerico vs casi reali pubblicati**; i test interni coprono solo la consistenza delle formule. La skill non produce relazioni di calcolo pronte al deposito e non firma elaborati. Per sezioni doppiamente armate, calcestruzzi ad alta resistenza, pressoflessione, taglio, torsione, fessurazione, deformabilita' o requisiti di gerarchia delle resistenze in zona sismica, **la skill rinvia ai paragrafi NTC pertinenti e a software di calcolo strutturale completo**.

## Sotto-attivita' disponibili

In base alla richiesta dell'utente, carica il task file appropriato:

- **Calcolo di M_Rd**: l'utente chiede "qual e' il momento resistente di questa sezione?", "verifica se M_Rd > M_Ed", "calcolami M_Rd per b=300, h=500, As=3 phi 16", "che M_Rd ho con C25/30 e B450C?" -> leggi [`tasks/calcola-m-rd.md`](tasks/calcola-m-rd.md)

Se la richiesta e' generica ("aiutami con la flessione SLU NTC"), chiedi conferma che si tratta di pre-dimensionamento di sezione rettangolare singolarmente armata; in caso contrario rinvia.

## Modulo di calcolo (code-driven - regola di invocazione)

Le formule NTC par. 4.1.2.1 e 4.1.2.3.4.2 sono implementate nel modulo Python [`tasks/lib/flessione_ca.py`](tasks/lib/flessione_ca.py). La test suite [`tasks/lib/test_flessione_ca.py`](tasks/lib/test_flessione_ca.py) copre **solo consistenza interna**: formule materiali (f_cd, f_yd, eps_yd) per casi standard C25/30 e B450C, equilibrio asse neutro, deformazione acciaio, raccordi e validazione input non finiti / fuori dominio (fck > 50 MPa, sezione sovra-armata, x >= d, d > h), monotonia di M_Rd in A_s/d/fck, avvertenza per x/d > 0.45 (sezione poco duttile), CLI con error handling. **Non** confronta vs casi pubblicati: la validazione di campo e' prerequisito del release stabile.

> **REGOLA OPERATIVA INVIOLABILE.** Per ogni calcolo numerico (f_cd, f_yd, x, eps_s, z, M_Rd) **devi invocare il modulo Python via Bash**. NON riprodurre i numeri "a mano" leggendo le formule dagli estratti in `references/estratti/`: gli estratti sono materiale di citazione normativa, non sostituiscono l'esecuzione del modulo. Calcolare a mano vanifica la ragion d'essere code-driven della skill (output deterministico e riproducibile, confrontabile dal progettista) e introduce errore stocastico.

### Path del modulo

In Claude Code la variabile `${CLAUDE_SKILL_DIR}` punta a questa skill. Usala in tutti i comandi Bash:

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/flessione_ca.py --input-json input.json
```

In Codex e altri agent compatibili AGENTS.md, se la variabile non e' risolta, sostituiscila con il path assoluto della directory che contiene **questo** `SKILL.md`. Non usare path relativi: la CWD dell'utente quasi mai coincide con la skill dir.

Il modulo non ha dipendenze esterne (solo libreria standard Python 3.9+).

## Processo generale

1. Identifica la sotto-attivita' (al momento solo "calcolo M_Rd").
2. Carica il task file `tasks/calcola-m-rd.md`.
3. Acquisisci dall'utente i dati della sezione (b, h, d, A_s) e dei materiali (fck, fyk).
4. Esegui il calcolo invocando il modulo. NON inventare A_s da diametro e numero barre senza confermare con l'utente.
5. Produci output strutturato: input riportati, materiali (f_cd, f_yd, eps_yd), geometria interna (x, x/d, eps_s, z), output (M_Rd in kNm), avvertenze duttilita', riferimenti normativi.
6. Concludi con rinvio al progettista: la skill copre solo flessione semplice SLU per sezioni singolarmente armate; ogni altra verifica (taglio, fessurazione, deformazione, sezioni sismiche) resta a carico del progettista con software di calcolo strutturale.

## Fonti normative

Riferimenti completi in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:
- DM 17/01/2018 (NTC 2018) - in particolare par. 4.1.2.1 (resistenze, diagrammi tensione/deformazione), par. 4.1.2.3.4.2 (flessione semplice SLU)
- Circolare MIT n. 7 del 21/01/2019 - par. C4.1.2 con commento applicativo

Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti

Questa skill NON fa:
- Solo sezioni rettangolari piene b x h (no T, L, circolari, cave, profili)
- Solo sezioni singolarmente armate (no A's compressa)
- Solo flessione semplice (no pressoflessione, no flessione deviata)
- Solo Classe 1 (fck <= 50 MPa); per fck > 50 MPa NTC richiede stress-block con eta < 1 e lambda < 0.8
- Solo SLU (no SLE, no fessurazione, no deformabilita')
- Non verifica taglio, torsione, punzonamento
- Non applica regole di progettazione capacitiva NTC par. 7.4.4 (CD"A" / CD"B" sismico)
- Non automatizza il calcolo di d a partire da copriferro/staffe/diametro: l'utente fornisce d direttamente
- Non automatizza il calcolo di A_s a partire da numero/diametro barre: l'utente fornisce A_s in mm^2
- Rifiuta sezioni sovra-armate (acciaio non snerva): segnala l'errore, non calcola con sigma_s elastico
- Non sostituisce la firma del progettista strutturale sulle relazioni di calcolo

**Ogni output va verificato dal progettista strutturale prima di essere usato per dimensionamento, asseverazione o deposito.**
