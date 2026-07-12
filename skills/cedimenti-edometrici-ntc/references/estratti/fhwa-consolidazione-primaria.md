# Cedimento di consolidazione primaria: formulazione FHWA NHI-06-088 par. 7.5.2 (codice internazionale ex cap. 12 NTC 2018)

> Estratto curato. Fonti (trascritte in `references/fonti/`):
> - `fhwa-nhi-06-088.md` (parr. 7.5.2, 7.5.2.1-7.5.2.3, eq. 7-2..7-7; par. 5.4.6.1)
> - `ntc2018-dm-17-01-2018.md` (§ 6.2.4.3 quadro SLE; cap. 12 "altri codici internazionali")
>
> Ogni affermazione seguente e' parafrasi dei passaggi trascritti nei file sopra.

## 1. Inquadramento normativo

Le NTC 2018 (§ 6.2.4.3) chiedono la verifica SLE con Ed <= Cd [6.2.7] ma non
forniscono una formula chiusa per il cedimento edometrico. Il cap. 12 NTC
ammette, per quanto non trattato dalla norma e dai documenti di comprovata
validita' elencati, l'uso di "altri codici internazionali", con la
responsabilita' del progettista di "garantire espressamente livelli di
sicurezza coerenti". La formulazione implementata dalla skill proviene dal
manuale **FHWA NHI-06-088** (U.S. DOT, 2006), pubblico dominio, citato a
questo titolo.

## 2. Classificazione dello stato tensionale (FHWA 7.5.2)

OCR = pc/po, con pc = massima tensione efficace passata (preconsolidazione)
e po = tensione efficace verticale iniziale al centro dello strato:

- **OCR = 1** -> normalconsolidato (NC), pc = po;
- **OCR > 1** -> sovraconsolidato (OC), pc > po;
- **OCR < 1** -> sottoconsolidato (UC), pc < po: la consolidazione sotto il
  carico esistente e' ancora in corso. Se non riconosciuto, il cedimento
  totale viene **sottostimato** (FHWA 7.5.2.3).

## 3. Equazioni (forma in indice dei vuoti; per la forma in deformazione vedere eq. 7-3/7-5/7-7 in fonte)

| Caso | Equazione FHWA | Espressione |
|---|---|---|
| NC (pc = po) | [7-2] | Sc = somma_n [ Cc/(1+eo) * Ho * log10(pf/po) ] |
| OC con pf > pc | [7-4] | S = somma_n [ Ho/(1+eo) * ( Cr*log10(pc/po) + Cc*log10(pf/pc) ) ] |
| UC (pc < po) | [7-6] | S = somma_n [ Ho/(1+eo) * ( Cc*log10(po/pc) + Cc*log10(pf/po) ) ] |

con: Ho = spessore dello strato (o sublayer); eo = indice dei vuoti
iniziale; Cc = indice di compressione (ramo vergine); Cr = indice di
ricompressione; pf = po + delta_p (tensione efficace finale al centro dello
strato). Cc_eps = Cc/(1+eo) (equivalenza dichiarata dopo l'eq. 7-3).

**Caso OC con pf <= pc**: il par. 7.5.2.2 formula le eq. 7-4/7-5 per il caso
pf > pc (figure 7-11); il caso in cui il carico finale resta sotto la
preconsolidazione non e' oggetto di un'equazione numerata nel paragrafo
trascritto. La skill NON inventa la formula: segnala il caso come non
coperto e rinvia al progettista.

## 4. Indicazioni operative (FHWA 7.5.2.2)

- Suddividere lo strato compressibile in **sublayer** entro la zona di
  influenza; tensioni iniziale e finale calcolate **al centro** di ciascun
  sublayer, proprieta' ragionevolmente costanti nel sublayer; spessori
  tipici 1,5-3 m (5-10 ft) nelle applicazioni stradali.
- Il cedimento totale e' la **somma** dei contributi dei sublayer; per
  profili misti NC/OC si combinano le equazioni 7-2..7-5 caso per caso.
- Il calcolo di delta_p (diffusione delle tensioni) e' un input: non e'
  coperto da questo estratto.

## 5. Correlazioni per Cc (FHWA 5.4.6.1) - solo controllo d'ordine di grandezza

Il manuale elenca correlazioni empiriche (Table 5-5, es. Cc = 0,009(LL-10);
Cc = 0,156 eo + 0,0107) avvertendo che i valori possono variare anche di un
**fattore 5** e che **"should not be used for final design"**. La skill le
cita solo per il sanity check dei valori di laboratorio, mai per il calcolo.

## 6. Cosa resta fuori (limiti della formulazione trascritta)

- **Decorso nel tempo** della consolidazione (FHWA 7.5.3) e **compressione
  secondaria** (FHWA 7.5.4): non trascritti, fuori ambito della skill.
- Determinazione di pc dalla curva edometrica (correzione Table 7-6a):
  richiamata ma non trascritta; la qualita' di pc e' responsabilita' del
  progettista.
- Il quadro NTC resta sovraordinato: il risultato va confrontato con i
  limiti Cd dichiarati dal progetto (§ 6.2.4.3) e la coerenza dei livelli
  di sicurezza e' responsabilita' del progettista (cap. 12).
