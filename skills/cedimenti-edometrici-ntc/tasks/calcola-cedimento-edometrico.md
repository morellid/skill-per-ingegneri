# Task: Calcolo del cedimento di consolidazione primaria (FHWA NHI-06-088 par. 7.5.2, ex cap. 12 NTC 2018)

Calcola il cedimento di consolidazione primaria di uno o piu' strati/sublayer con le equazioni 7-2/7-4/7-6 del manuale FHWA NHI-06-088, utilizzato come "altro codice internazionale" ai sensi del cap. 12 delle NTC 2018.

## Obiettivo

Restituire all'utente:

- **S totale** [m e mm] come somma dei contributi degli strati (FHWA 7.5.2.2), con per ogni strato: caso (NC/OC/UC), equazione applicata, OCR, sigma_f, contributi dei singoli termini, deformazione media.
- **Inquadramento normativo**: formulazione da codice internazionale ex cap. 12 NTC, risultato da confrontare con il limite Cd del progetto (NTC 6.2.4.3, Ed <= Cd).
- **Avvertenze** sui casi non coperti e sui dati sospetti.

## Input richiesti (per ogni strato/sublayer, valori al CENTRO dello strato)

1. **h0** [m] - spessore (sublayer tipici 1,5-3 m, FHWA 7.5.2.2)
2. **e0** [-] - indice dei vuoti iniziale
3. **Cc** [-] - indice di compressione (ramo vergine, da prova edometrica corretta)
4. **Cr** [-] - indice di ricompressione (necessario per il caso OC)
5. **sigma_0'** [kPa] - tensione efficace verticale iniziale
6. **sigma_p'** [kPa] - tensione di preconsolidazione (assente -> trattato come NC)
7. **delta_sigma'** [kPa] - incremento di tensione al centro dello strato (calcolato dal progettista: la diffusione delle tensioni NON e' coperta dalla skill)

## Fonti normative

Leggere prima di procedere:

- `references/estratti/fhwa-consolidazione-primaria.md` - equazioni, classificazione OCR, limiti
- `references/fonti/fhwa-nhi-06-088.md` - trascrizione parr. 7.5.2 e 5.4.6.1
- `references/fonti/ntc2018-dm-17-01-2018.md` - § 6.2.4.3 (quadro SLE) + cap. 12 (codici internazionali)

## Procedura

### Passo 1 - Esegui il calcolo con il modulo Python

Usa SEMPRE il modulo `tasks/lib/cedimento_edometrico.py` (mai calcoli a mano):

```bash
# singolo strato OC
python3 tasks/lib/cedimento_edometrico.py --h0 2 --e0 0.8 --cc 0.30 --cr 0.05 \
  --sigma0 100 --sigmap 150 --dsigma 200

# multistrato da file JSON: {"strati": [{...}, {...}]}
python3 tasks/lib/cedimento_edometrico.py --json strati.json
```

Comportamenti del modulo da conoscere:

- **NC** (sigma_p assente o = sigma_0): eq. [7-2].
- **OC con sigma_f > sigma_p**: eq. [7-4], richiede Cr; avvertenza se Cr > Cc.
- **OC con sigma_f <= sigma_p**: **rifiutato** - le equazioni trascritte dalla fonte valgono per pf > pc; il caso va risolto dal progettista sulla fonte, la skill non inventa la formula.
- **OCR < 1**: **rifiutato di default** (probabile errore nei dati: verificare sigma_p, unita', scambi di colonne). Solo se l'utente dichiara che il terreno e' realmente **sottoconsolidato** (consolidazione in corso, da giustificare) rieseguire con `--sottoconsolidato`: eq. [7-6], che include anche la consolidazione ancora in corso sotto il carico esistente (FHWA 7.5.2.3).

### Passo 2 - Presenta il risultato

1. **S totale** e ripartizione per strato con caso ed equazione FHWA citata ([7-2]/[7-4]/[7-6], par. 7.5.2).
2. **Inquadramento**: formulazione FHWA NHI-06-088 usata come codice internazionale ex **cap. 12 NTC 2018** ("e' responsabilita' del progettista garantire espressamente livelli di sicurezza coerenti"); il risultato va confrontato con il **limite Cd** dichiarato dal progetto (NTC 6.2.4.3).
3. **Riporta integralmente le avvertenze** del modulo.
4. Se l'utente fornisce Cc da correlazioni: ricorda che le correlazioni della Table 5-5 FHWA variano fino a un fattore 5 e "should not be used for final design" (par. 5.4.6.1) - servono i valori di prova edometrica.

### Passo 3 - Concludi sempre con

- Il calcolo copre il **solo cedimento di consolidazione primaria**: decorso nel tempo (FHWA 7.5.3), compressione secondaria (FHWA 7.5.4) e cedimento immediato sono fuori ambito.
- delta_sigma' e sigma_p' sono input del progettista (diffusione tensioni e correzione della curva edometrica non coperte).
- Il risultato e' un supporto: **non sostituisce il calcolo geotecnico del progettista firmatario** ne' la verifica documentale (task `check-verifica-cedimenti.md`).

## Output

Blocco JSON del modulo + sintesi testuale con citazioni (equazione FHWA per strato, cap. 12 e § 6.2.4.3 NTC) e avvertenze.

## Limiti

- Non calcola la **diffusione delle tensioni** (delta_sigma' e' input).
- Non determina **sigma_p'** dalla curva edometrica (correzione Table 7-6a: richiamata, non implementata).
- Non copre **OC con sigma_f <= sigma_p** ne' consolida i casi dubbi: li rifiuta con messaggio esplicito.
- Non calcola **tempi di consolidazione** ne' **compressione secondaria**.
- Non verifica il rispetto di **Ed <= Cd**: il limite Cd e' del progetto.
