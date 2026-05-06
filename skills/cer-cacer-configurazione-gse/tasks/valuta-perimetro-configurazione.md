# Task: Verifica perimetro cabina primaria e scelta della configurazione (AID / GAC / CER)

Aiuta a decidere se l'iniziativa di autoconsumo da rinnovabile rientra nel servizio CACER del GSE e in quale forma giuridica conviene impostarla, ai sensi del **D.Lgs. 199/2021** (AID art. 30 c. 1 lett. a) n. 2, GAC art. 30 c. 2, CER art. 31) e del **DM MASE 7/12/2023 n. 414** come modificato dal **DM MASE 16/5/2025 n. 127** e da ultimo dal **DL 19 febbraio 2026 n. 19 art. 27** (regime PNRR vigente al 2026-05-07: Comuni < 50.000 ab.; stipula accordi di concessione entro 30/6/2026; esercizio entro 24 mesi dalla comunicazione dell'accordo, max 31/12/2027).

## Obiettivo

Produrre una **scheda di pre-fattibilita'** che indichi:

- se il caso e' compatibile con AID, GAC, CER (singola o multipla compatibilita');
- se il perimetro **cabina primaria** e' rispettato per i POD coinvolti;
- se la potenza degli impianti FER rientra nel limite ammesso al servizio CACER (1 MW per impianto, fatte salve eccezioni);
- la **configurazione consigliata** con motivazione e segnalazione delle verifiche residue.

## Input richiesti

### Soggetti
- Numero e tipologia dei soggetti (persone fisiche, PMI, ente locale, terzo settore, ecc.).
- Presenza di **grandi imprese** (incompatibili con CER come socie).
- Esistenza di un eventuale **referente** gia' identificato (ESCo, produttore, soggetto giuridico ad hoc).

### Posizione fisica
- Comune e indirizzo del/i POD di prelievo.
- Comune e indirizzo del/i POD di immissione (impianto).
- Se i soggetti sono nello **stesso edificio o condominio** (rilevante per GAC).
- Cabina primaria di riferimento, se gia' nota dalla mappa GSE.

### Impianti FER
- Tecnologia (FV, eolico, idroelettrico, biomassa, ecc.) - solo FER ammesse.
- Potenza nominale (kW).
- Stato: in progetto / autorizzato / in costruzione / in esercizio.
- Data prevista o effettiva di entrata in esercizio.
- Per impianti gia' in esercizio: data e regime di accesso a eventuali altri incentivi (es. Conto Energia residuo, scambio sul posto), per gestire la cumulabilita'.

### Obiettivi del cliente
- Solo riduzione dei costi energetici? Anche obiettivi sociali/ambientali a livello di comunita'? Coinvolgimento di soggetti pubblici?
- Disponibilita' a costituire un **soggetto giuridico autonomo** (necessario per la CER).
- Comune ospite con popolazione **inferiore a 50.000 abitanti** (regime vigente post DM 127/2025; rilevante per il contributo PNRR a fondo perduto).

## Fonti

Leggere prima:

- [`../references/estratti/dlgs-199-2021-art-30-31-32.md`](../references/estratti/dlgs-199-2021-art-30-31-32.md)
- [`../references/estratti/dm-mase-414-2023.md`](../references/estratti/dm-mase-414-2023.md)
- [`../references/estratti/gse-regole-operative-cacer.md`](../references/estratti/gse-regole-operative-cacer.md)

## Procedura

### Passo 1 - Verifica preliminare di ammissibilita'

Verifica che:

- gli impianti siano **a fonte rinnovabile** (no impianti a combustibili fossili, no impianti di sola cogenerazione fossile);
- nessun impianto FER del perimetro abbia potenza superiore a **1 MW** (segnala come fuori perimetro CACER se superato);
- nessun socio sia una **grande impresa** (se l'utente vuole una CER); per GAC/AID il vincolo non opera, ma valgono i requisiti soggettivi specifici;
- ci sia un **referente** ipotizzabile o costituibile (anche dopo, ma va segnalato).

Se uno di questi vincoli e' violato, segnala chiaramente nel report.

### Passo 2 - Verifica perimetro cabina primaria (sotto-configurazione incentivata)

Distingui due piani:

1. **Perimetro tecnico per la TIP**: per ogni **sotto-configurazione incentivata** (richiesta GSE con accesso alla tariffa incentivante), tutti i POD coinvolti - di immissione e di prelievo - devono trovarsi nell'**area sottesa alla stessa cabina primaria**, identificata sulla mappa pubblicata dal GSE. Questo vincolo opera ai fini dell'incentivo, non come requisito costitutivo del soggetto.
2. **Perimetro soggettivo della CER**: la CER come **soggetto giuridico** non e' obbligata a stare in una sola cabina primaria. Una CER puo' avere soci sotto cabine primarie diverse e presentare al GSE **piu' richieste**, una per ciascun perimetro tecnico.

Procedi cosi':

- Se l'utente fornisce la cabina primaria, registra il dato.
- Se non la fornisce, indica come **azione obbligatoria** la consultazione della mappa GSE (tramite portale Autoconsumo) prima della richiesta di qualifica della singola sotto-configurazione.
- Se i POD ricadono in **cabine primarie diverse**:
  - per AID o GAC, la configurazione resta legata a una sola cabina primaria (per AID per definizione di "POD prelievo + POD immissione", per GAC perche' il vincolo "stesso edificio o condominio" implica una sola cabina);
  - per CER, valuta l'opzione di una **CER unica con piu' sotto-configurazioni incentivate distinte** (una per cabina primaria) oppure di restringere il perimetro tecnico iniziale, mantenendo aperto il futuro ampliamento.

### Passo 3 - Mappa la configurazione

Usa il seguente albero decisionale (output testuale, non grafico):

1. **Un solo soggetto** che possiede sia impianto sia POD di prelievo distinti, connessi tramite la rete pubblica -> **AID** (art. 30 c. 1 lett. a) n. 2 D.Lgs. 199/2021).
2. **Piu' soggetti** che si trovano nello **stesso edificio o condominio** -> **GAC** (art. 30 c. 2 D.Lgs. 199/2021, con il vincolo edificio/condominio alla lett. a)), tipicamente strutturato come accordo privato/regolamento condominiale, con un referente unico verso il GSE ai sensi dell'art. 32.
3. **Piu' soggetti** distinti che si associano in un soggetto giuridico autonomo per scopi di benefici ambientali/economici/sociali -> **CER** (art. 31 D.Lgs. 199/2021). Per accedere alla TIP, ciascuna sotto-configurazione incentivata deve restare nella stessa cabina primaria, ma il soggetto CER puo' coprire un perimetro piu' ampio.

Se piu' rami sono compatibili, presentali come opzioni con i loro pro/contro:
- **CER** vs **GAC**: la CER e' piu' aperta (anche soggetti distanti, anche enti locali, possibilita' di piu' sotto-configurazioni incentivate), ma richiede atto costitutivo/statuto e governance. Il GAC e' piu' snello ma limitato a stesso edificio/condominio.
- **AID** vs **GAC**: AID e' adatto al singolo soggetto multi-POD; non si applica se ci sono piu' soggetti distinti.

### Passo 4 - Valuta il contributo PNRR (regime vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27)

Per gli impianti situati in Comuni con popolazione **inferiore a 50.000 abitanti** (soglia introdotta dal DM MASE 127/2025; il testo originario del DM 414/2023 limitava il regime a Comuni < 5.000 ab.):

- Segnala l'opportunita' del **contributo PNRR a fondo perduto** ex art. 8 DM 7/12/2023, nel testo modificato dal DM 127/2025 e dall'art. 27 DL 19/2026.
- Ricorda le **scadenze PNRR vigenti** (post DL 19/2026): **stipula degli accordi di concessione** lato GSE **entro il 30 giugno 2026**; entrata in esercizio entro **24 mesi dalla comunicazione dell'accordo di concessione** e comunque **non oltre il 31 dicembre 2027** (limite invalicabile).
- Ricorda la **riduzione della parte fissa della TIP** in caso di cumulo per evitare doppio finanziamento.
- Ricorda l'articolazione del rimborso in tre fasi: **anticipazione** fino al **30%** del contributo massimo, **quota intermedia** pari al **40%** del contributo (richiedibile dopo aver sostenuto il 40% delle spese ammissibili e comunicato l'avvio dei lavori), **saldo** finale.
- Ricorda gli obblighi PNRR (DNSH, milestone, controlli ANAC/RGS): rinvio alla skill `dnsh-pnrr-checker`.

Se il Comune ha popolazione **>= 50.000 abitanti**, il contributo PNRR non e' accessibile per quell'impianto: la TIP resta comunque accessibile.

### Passo 5 - Componi la scheda di pre-fattibilita'

Output strutturato come segue.

## Output

```markdown
# Scheda di pre-fattibilita' CACER

## 1. Soggetti coinvolti
- [N persone fisiche, M PMI, K enti locali, ...]
- Eventuali grandi imprese: SI/NO
- Referente ipotizzato: [...]

## 2. Posizione e perimetro
- POD prelievo: [Comune/i e numero]
- POD immissione (impianto/i): [Comune/i e numero]
- Cabina primaria: [identificata: ID / DA VERIFICARE SU MAPPA GSE]
- Stesso edificio/condominio: SI/NO

## 3. Impianti FER
- Tecnologia: [...]
- Potenza singolo impianto: [...] kW (limite 1.000 kW per servizio CACER)
- Stato: [in progetto / autorizzato / in esercizio]

## 4. Configurazione consigliata
- Configurazione: AID | GAC | CER (con motivazione e citazione puntuale di art. 30 c. 1 lett. a) n. 2 / art. 30 c. 2 / art. 31 D.Lgs. 199/2021)
- Configurazioni alternative compatibili: [se applicabili]

## 5. Verifiche obbligatorie residue
- [ ] Verifica cabina primaria sulla mappa GSE (per ciascuna sotto-configurazione incentivata)
- [ ] Verifica titolo abilitativo dell'impianto (Comunicazione / Modello Unico / PAS / AU) DA VERIFICARE: la skill non ha tra le fonti il DPR 380/2001 ne' il DM 19/5/2015 sul Modello Unico, l'utente o il professionista determinano il titolo applicabile
- [ ] Verifica cumulabilita' incentivi (art. 11 DM 7/12/2023)
- [ ] (Solo CER) Decisione forma giuridica + formalizzazione secondo la forma scelta (atto pubblico, scrittura privata autenticata, RUNTS, ecc.)
- [ ] (Solo PNRR) Verifica popolazione Comune ISTAT < 50.000 ab. (regime post DM 127/2025)
- [ ] (Solo PNRR) Verifica scadenze (post DL 19/2026): stipula accordi di concessione GSE entro 30/6/2026, esercizio entro 24 mesi dalla comunicazione dell'accordo e comunque non oltre 31/12/2027
- [ ] (Solo PNRR) Predisposizione adempimenti DNSH

## 6. Avvertenza finale
La presente scheda e' un supporto preliminare. La qualifica formale del servizio
CACER e' rilasciata dal GSE secondo le Regole Operative vigenti. La forma
giuridica della CER richiede la consulenza di un professionista (consulente legale, commercialista) e la formalizzazione dello statuto secondo la forma scelta (atto pubblico, scrittura privata autenticata, procedura RUNTS, ecc.).
```

## Limiti del task

- Non sostituisce la verifica della cabina primaria sul portale GSE.
- Non valuta in autonomia la cumulabilita' con incentivi pre-esistenti: rinvio al GSE / consulente.
- Non determina la forma giuridica concreta della CER: rinvio al consulente legale e alla modalita' di formalizzazione richiesta dalla forma scelta (atto pubblico, scrittura privata autenticata, RUNTS, ecc.).
- Non considera vincoli regionali o piani territoriali energetici, da verificare a parte.
