# Det. ACN 127437/2026 - Elencazione fornitori rilevanti NIS (art. 18 + definizioni e finestra)

> Fonte: Agenzia per la Cybersicurezza Nazionale, Determinazione del Direttore Generale del 13 aprile 2026, protocollo n. 127437/2026 (codice documento `detacn_piattaformanis_251218-v9_signed`).
> Fonte catalogata in `sources.yaml` come `acn-det-127437-2026`.
> URL canonico: https://www.acn.gov.it/portale/en/nis/la-normativa
> Estratto selettivo: art. 1 (lett. ll), art. 16 co. 1 e co. 3 lett. g), art. 18, art. 24 (applicazione). Trascrizione integrale in `references/fonti/acn-det-127437-2026.md`.
> Data consultazione: 2026-05-17.

## Inquadramento

La determinazione 127437/2026 e' adottata ai sensi dell'**art. 7 co. 6 D.Lgs. 138/2024** (piattaforma digitale NIS) e dell'**art. 40 co. 5 lett. b)** dello stesso decreto. Aggiorna e sostituisce la Det. ACN 379887/2025. Si applica **dal 15 aprile 2026** (art. 24 co. 3) - il Capo V sulla categorizzazione e' invece differito al **1 maggio 2026**.

Tra le novita' di questa determinazione c'e' l'obbligo di **elencare i fornitori rilevanti NIS** nell'ambito dell'aggiornamento annuale delle informazioni sulla piattaforma ACN. Le tre disposizioni operative sono qui sotto.

## Art. 1 co. 1 lett. ll) - Definizione di "fornitori rilevanti NIS"

> ll) "fornitori rilevanti NIS", un soggetto che assicura la fornitura di servizi o di prodotti a un soggetto NIS che soddisfa **almeno uno** dei seguenti criteri di rilevanza:
> 1) la fornitura e' riconducibile alle attivita' o ai servizi di cui all'allegato I, punti 8 e 9, del decreto NIS (fornitura ICT);
> 2) l'interruzione o la compromissione della fornitura comporta un impatto significativo sulla capacita' del soggetto NIS, anche per effetto della indisponibilita' di fornitori alternativi, di erogare le attivita' o i servizi per i quali rientra nell'ambito di applicazione del decreto NIS (fornitura non fungibile).

**Nota operativa**: i criteri sono **alternativi**. Basta che la fornitura ricada in **uno solo** dei due perche' il fornitore vada elencato.

**Riferimento del criterio 1** - Allegato I, punti 8 e 9, del D.Lgs. 138/2024:
- Punto 8 - Infrastrutture digitali (fornitori IXP, DNS, TLD, cloud computing, data center, CDN, fornitori di servizi fiduciari, fornitori di reti pubbliche di comunicazione elettronica, fornitori di servizi di comunicazione elettronica accessibili al pubblico)
- Punto 9 - Gestione dei servizi TIC (fornitori di servizi gestiti, fornitori di servizi gestiti di sicurezza)

Vedi `references/estratti/dlgs-138-2024-allegati-i-iv.md` per il testo verbatim degli allegati.

**Criterio 2 - "fornitura non fungibile"**: il test e' duplice e si applica congiuntamente:
- l'interruzione o la compromissione della fornitura impatta in modo significativo la capacita' del soggetto NIS di erogare i servizi per i quali e' in ambito NIS;
- l'impatto significativo puo' derivare anche dall'**indisponibilita' di fornitori alternativi** (non fungibilita').

Quindi un fornitore non ICT puo' comunque essere "rilevante" se l'interruzione del servizio bloccherebbe l'attivita' core del soggetto NIS e non ha sostituti rapidi.

## Art. 16 co. 1 - Finestra dell'aggiornamento annuale

> 1. **Dal 15 aprile al 31 maggio di ogni anno**, gli utenti aggiornano, tramite il "Servizio NIS/Aggiornamento annuale informazioni", le informazioni per conto del soggetto per cui operano, assicurandone la correttezza.

**Nota operativa**: la finestra e' annuale e fissa. L'**elencazione dei fornitori rilevanti NIS** rientra in questo aggiornamento (art. 16 co. 3 lett. g, sotto). Per l'**anno 2026** la finestra e' aperta dal **15 aprile al 31 maggio 2026**; questo e' il **primo anno** in cui l'obbligo si applica perche' la determinazione si applica dal 15 aprile 2026 (art. 24 co. 3).

Per i soggetti gia' nell'elenco NIS 2025, la piattaforma presenta informazioni precompilate sulla base di quelle trasmesse fino al 14 aprile 2026 (art. 16 co. 12).

## Art. 16 co. 3 lett. g) - Inclusione dei fornitori rilevanti nell'aggiornamento

> 3. Per tutti i soggetti NIS, gli utenti verificano la correttezza e l'aggiornamento:
> ...
> **g) dell'elenco dei fornitori rilevanti NIS, ai fini dell'articolo 3, comma 9, lettera f), del decreto NIS.**

**Nota operativa**: l'obbligo si applica a **tutti i soggetti NIS** (essenziali e importanti). Il riferimento e' all'art. 3 co. 9 lett. f) del D.Lgs. 138/2024, che richiede all'Autorita' nazionale competente NIS di individuare gli elementi sistemici della catena di approvvigionamento (anche digitale) dei soggetti essenziali e importanti.

**Esenzione** (art. 16 co. 13): le **entita' finanziarie** ai sensi del Reg. UE 2022/2554 (DORA) che rientrano in ambito NIS sono esentate dall'attuazione di quanto previsto dal comma 3 lett. b) (organi di amministrazione e direttivi) e dall'art. 17. **L'esenzione NON copre la lett. g) sui fornitori rilevanti NIS**: i soggetti DORA-NIS devono comunque elencare i fornitori rilevanti.

## Art. 18 - Informazioni richieste per ogni fornitore rilevante

> 1. Ai fini dell'articolo 16, comma 3, lettera g), tramite il "Servizio NIS/Aggiornamento annuale informazioni", gli utenti elencano i fornitori rilevanti NIS, indicandone:
> a) la denominazione;
> b) il codice fiscale;
> c) il Paese in cui hanno la sede legale;
> d) i codici CPV (Common Procurement Vocabulary), di cui al Regolamento (CE) n. 2195/2002, relativi alle forniture di cui fruisce il soggetto NIS;
> e) il criterio di rilevanza, di cui all'articolo 1, comma 1, lettera ll), utilizzato.

**Nota operativa - 5 campi obbligatori per fornitore**:
1. Denominazione (ragione sociale)
2. Codice fiscale (P.IVA per i soggetti italiani; in mancanza, identificativo equivalente del Paese estero)
3. Paese della sede legale
4. **Codici CPV** del Regolamento (CE) n. 2195/2002 - vocabolario europeo per gli appalti pubblici, struttura 8 cifre + cifra di controllo. Una fornitura puo' coprire piu' codici CPV; vanno indicati i codici **delle forniture di cui il soggetto NIS fruisce** (non l'intero catalogo del fornitore).
5. Criterio di rilevanza applicato (criterio 1 oppure criterio 2 della lett. ll). Quando entrambi si applicano, va indicato almeno uno (lett. ll: "almeno uno"); per chiarezza espositiva e' opportuno indicarne entrambi se applicabili.

**Riferimento CPV**: il Regolamento (CE) n. 2195/2002 e' il riferimento europeo per il vocabolario comune degli appalti pubblici. La struttura e' XXXXXXXX-Y dove i primi 8 caratteri sono il codice e Y la cifra di controllo. Esempi rilevanti per le forniture ICT:
- 72000000-5 (Servizi informatici: consulenza, sviluppo software, Internet e supporto)
- 72500000-0 (Servizi informatici)
- 64200000-8 (Servizi di telecomunicazione)
- 30200000-1 (Apparecchiature informatiche e forniture)

I codici CPV vengono indicati dal soggetto NIS in autonomia e non sono vincolati alla forma contrattuale (anche fornitori non passati da gara pubblica devono essere descritti con i CPV corrispondenti alle forniture ricevute).

## Art. 24 co. 3 - Applicazione

> 3. La presente determinazione si applica a decorrere dal **15 aprile 2026**, fatte salve le disposizioni di cui al capo V la cui applicazione e' differita al **1 maggio 2026**.

**Nota operativa**: l'obbligo dell'art. 18 (elenco fornitori rilevanti) rientra nel Capo IV ed e' quindi applicabile dal **15 aprile 2026**. Il primo adempimento concreto cade nella finestra **15 aprile - 31 maggio 2026** (art. 16 co. 1). Il Capo V (categorizzazione delle attivita' e dei servizi - art. 20-21) si applica dal 1 maggio 2026 ed ha una propria finestra annuale **1 maggio - 30 giugno**.

## Sintesi operativa per la skill

| Elemento | Riferimento | Contenuto |
|----------|-------------|-----------|
| Cosa | Det. 127437/2026 art. 18 + art. 16 co. 3 lett. g) | Comunicare alla piattaforma ACN l'elenco dei fornitori rilevanti NIS |
| Chi | art. 16 co. 1 + art. 18 | Tutti i soggetti NIS (essenziali e importanti); esenzione lett. g) non concessa neppure ai soggetti DORA |
| Quando | art. 16 co. 1 + art. 24 co. 3 | Finestra annuale **15 aprile - 31 maggio**; prima applicazione anno **2026** |
| Quali fornitori | art. 1 co. 1 lett. ll) | I fornitori che soddisfano **almeno uno** dei due criteri: (1) fornitura ICT (Allegato I p. 8-9 D.Lgs. 138/2024); (2) fornitura non fungibile con impatto significativo |
| Quali informazioni | art. 18 | 5 campi per fornitore: denominazione, CF, Paese sede legale, codici CPV (Reg. CE 2195/2002), criterio di rilevanza applicato |
| Come | art. 16 co. 1 + art. 18 co. 1 | Tramite "Servizio NIS/Aggiornamento annuale informazioni" sul Portale ACN |
| Conferma finale | art. 16 co. 7 | Il punto di contatto conferma le informazioni ai sensi del DPR 445/2000 e le trasmette telematicamente |
