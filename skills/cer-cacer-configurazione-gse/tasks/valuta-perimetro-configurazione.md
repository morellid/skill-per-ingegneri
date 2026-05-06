# Task: Verifica perimetro cabina primaria e scelta della configurazione (AID / GAC / CER)

Aiuta a decidere se l'iniziativa di autoconsumo da rinnovabile rientra nel servizio CACER del GSE e in quale forma giuridica conviene impostarla, ai sensi del **D.Lgs. 199/2021 art. 30-32** e del **DM MASE 7/12/2023**.

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
- Comune ospite con popolazione **< 5.000 abitanti** (rilevante per il contributo PNRR).

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

### Passo 2 - Verifica perimetro cabina primaria

Per accedere alla TIP, **tutti i POD** della CACER (sia di immissione sia di prelievo) devono trovarsi nell'**area sottesa alla stessa cabina primaria**, identificata sulla mappa pubblicata dal GSE.

- Se l'utente fornisce la cabina primaria, registra il dato.
- Se non la fornisce, indica come **azione obbligatoria** la consultazione della mappa GSE (tramite portale Autoconsumo) prima della costituzione della CACER.
- Annota il caso in cui i POD ricadano in **cabine primarie diverse**: in tal caso si possono comunque ipotizzare CACER **distinte** per cabina primaria, oppure escludere alcuni POD.

### Passo 3 - Mappa la configurazione

Usa il seguente albero decisionale (output testuale, non grafico):

1. **Un solo soggetto** che possiede sia impianto sia POD di prelievo distinti -> **AID** (art. 30 D.Lgs. 199/2021).
2. **Piu' soggetti** che si trovano nello **stesso edificio o condominio** -> **GAC** (art. 32 D.Lgs. 199/2021), tipicamente strutturato come accordo privato/regolamento condominiale.
3. **Piu' soggetti** in posizioni diverse, ma sotto la **stessa cabina primaria**, con disponibilita' a un soggetto giuridico autonomo -> **CER** (art. 31 D.Lgs. 199/2021).

Se piu' rami sono compatibili, presentali come opzioni con i loro pro/contro:
- **CER** vs **GAC**: CER e' piu' aperta (anche soggetti distanti, anche enti locali), ma richiede atto costitutivo/statuto e governance. GAC e' piu' snello ma limitato a stesso edificio/condominio.
- **AID** vs **GAC**: AID e' adatto al singolo soggetto multi-POD; non si applica se ci sono piu' soggetti distinti.

### Passo 4 - Valuta il contributo PNRR

Per gli impianti situati in Comuni con popolazione **< 5.000 abitanti**:

- Segnala l'opportunita' del **contributo PNRR a fondo perduto** ex art. 8 DM 7/12/2023.
- Ricorda la **riduzione della parte fissa della TIP** in caso di cumulo.
- Ricorda gli obblighi PNRR (DNSH, milestone, controlli ANAC/RGS): rinvio alla skill `dnsh-pnrr-checker`.

Se il Comune ha popolazione >= 5.000 abitanti, il contributo PNRR non e' accessibile per quell'impianto: la TIP resta comunque accessibile.

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
- Configurazione: AID | GAC | CER (con motivazione richiamando art. 30/31/32 D.Lgs. 199/2021)
- Configurazioni alternative compatibili: [se applicabili]

## 5. Verifiche obbligatorie residue
- [ ] Verifica cabina primaria sulla mappa GSE
- [ ] Verifica titolo abilitativo dell'impianto (PAS / Comunicazione / Modello Unico / AU)
- [ ] Verifica cumulabilita' incentivi (art. 11 DM 7/12/2023)
- [ ] (Solo CER) Decisione forma giuridica + costituzione presso notaio
- [ ] (Solo PNRR) Verifica popolazione Comune ISTAT < 5.000 ab.
- [ ] (Solo PNRR) Predisposizione adempimenti DNSH

## 6. Avvertenza finale
La presente scheda e' un supporto preliminare. La qualifica formale del servizio
CACER e' rilasciata dal GSE secondo le Regole Operative vigenti. La forma
giuridica della CER richiede la consulenza di notaio e commercialista.
```

## Limiti del task

- Non sostituisce la verifica della cabina primaria sul portale GSE.
- Non valuta in autonomia la cumulabilita' con incentivi pre-esistenti: rinvio al GSE / consulente.
- Non determina la forma giuridica concreta della CER: rinvio al notaio.
- Non considera vincoli regionali o piani territoriali energetici, da verificare a parte.
