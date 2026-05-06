# Task: Redazione guidata dello statuto / atto costitutivo di una CER

Costruisce una **bozza strutturata di statuto** di una Comunita' di Energia Rinnovabile, allineata ai contenuti minimi richiesti dal **DM MASE 7/12/2023 art. 4-5** e dal **D.Lgs. 199/2021 art. 31**, da finalizzare in atto pubblico presso un notaio.

## Obiettivo

Produrre un documento markdown con:

- denominazione, forma giuridica, sede;
- finalita' coerenti con l'art. 31 D.Lgs. 199/2021 (benefici ambientali/economici/sociali, non profitto finanziario primario);
- requisiti soggettivi dei soci;
- governance (assemblea, organo amministrativo, voto, autonomia);
- perimetro territoriale (cabina primaria, zona di mercato);
- criteri di ripartizione dei benefici;
- ruolo del referente verso il GSE;
- norme su modifiche, recesso, scioglimento.

Lo statuto NON e' definitivo: la skill produce una **bozza tecnica** da consegnare al notaio.

## Input richiesti

### Identificazione
- Denominazione proposta della CER.
- Forma giuridica scelta (associazione / fondazione / cooperativa / ente del terzo settore / consorzio / partenariato).
- Comune e indirizzo della sede legale.

### Soci fondatori
- Elenco dei soci fondatori con tipologia (persona fisica, PMI, ente locale, terzo settore, ente religioso, ente di ricerca/formazione).
- Per le PMI: dichiarazione che la partecipazione alla CER non e' attivita' commerciale o industriale principale (vincolo art. 31 D.Lgs. 199/2021).

### Perimetro
- Cabina primaria di riferimento (identificata su mappa GSE).
- Zona di mercato.
- Comuni inclusi nel perimetro (per CER con piu' Comuni nella stessa cabina).

### Governance
- Modalita' di voto preferita (capitario / per quote, nei limiti dell'autonomia).
- Frequenza assemblea ordinaria.
- Composizione organo di amministrazione.

### Benefici e impianti
- Logica di ripartizione benefici tra soci (es. proporzionale al consumo, quota fissa + variabile, quota a finalita' sociali della comunita').
- Soggetti proprietari degli impianti (CER stessa, soci, ESCo terza).
- Eventuale ESCo / referente esterno.

### Durata
- Durata della CER (es. 30 anni).

## Fonti

Leggere prima:

- [`../references/estratti/dlgs-199-2021-art-30-31-32.md`](../references/estratti/dlgs-199-2021-art-30-31-32.md)
- [`../references/estratti/dm-mase-414-2023.md`](../references/estratti/dm-mase-414-2023.md)
- [`../references/estratti/gse-regole-operative-cacer.md`](../references/estratti/gse-regole-operative-cacer.md)

## Procedura

### Passo 1 - Verifica di compatibilita' soggettiva

Prima di scrivere lo statuto, verifica:

- nessun socio fondatore e' una **grande impresa**;
- per ogni PMI socio, e' acquisibile la dichiarazione che la partecipazione alla CER **non e' attivita' principale** dell'impresa;
- e' stato individuato un **referente** (puo' essere la CER stessa, un socio, un'ESCo terza con mandato);
- la **forma giuridica** scelta e' coerente con l'art. 31 D.Lgs. 199/2021.

Se uno di questi punti non e' chiaro, chiedi all'utente prima di procedere.

### Passo 2 - Mappa i contenuti minimi richiesti dal DM 7/12/2023

Lo statuto della CER deve coprire **almeno** queste voci:

| Riferimento | Contenuto |
|---|---|
| DM 7/12/2023 art. 5, contenuti minimi | denominazione, forma giuridica, sede |
| | finalita' (ambientale/sociale/economica, non profitto finanziario primario) |
| | requisiti dei soci e modalita' di adesione/recesso |
| | governance (assemblea, organo amministrativo, principio di autonomia) |
| | perimetro CACER (cabina primaria, zona di mercato) |
| | titolarita' e gestione degli impianti FER |
| | criteri di ripartizione dei benefici economici e quota a finalita' di comunita' |
| | individuazione del referente verso il GSE |
| | modifiche statutarie, scioglimento, destinazione del patrimonio residuo |
| D.Lgs. 199/2021 art. 31 c. 2 | divieto di partecipazione delle grandi imprese |
| | partecipazione delle PMI subordinata al carattere non principale |

### Passo 3 - Genera la bozza con sezioni numerate

Usa la struttura di output indicata sotto. Per ogni voce non chiarita dall'utente, inserisci `DA DEFINIRE CON I FONDATORI` o `DA VERIFICARE CON NOTAIO`.

### Passo 4 - Inserisci una sezione operativa "GSE"

Aggiungi un articolo che disciplini:

- la nomina e i poteri del referente verso il GSE;
- l'autorizzazione del referente a sottoscrivere mandati e dichiarazioni necessarie alla qualifica del servizio CACER;
- l'obbligo del referente di rendicontare ai soci i flussi TIP/TR ricevuti dal GSE.

### Passo 5 - Inserisci la clausola di non lucro principale

Esplicita che eventuali avanzi di gestione sono destinati a:

- reinvestimento in impianti o servizi della CER;
- riduzione delle quote/contributi dei soci;
- progetti di efficienza energetica o riduzione poverta' energetica nella comunita';
- finalita' ambientali/sociali coerenti con la mission.

### Passo 6 - Disclaimer finale

Concludi con: "La presente bozza non costituisce statuto definitivo. La sua validita' giuridica richiede la sottoscrizione presso notaio o intermediario abilitato e la verifica da parte di un consulente legale e fiscale, in particolare per gli aspetti del terzo settore e degli aiuti di Stato."

## Output

Il task produce un documento markdown strutturato come segue:

```markdown
# Statuto della Comunita' di Energia Rinnovabile [DENOMINAZIONE]

> Bozza tecnica - non sottoscritta - da finalizzare in atto pubblico presso notaio.
> Riferimenti: D.Lgs. 199/2021 art. 31 + DM MASE 7/12/2023 art. 4-5.

## Art. 1 - Denominazione, forma giuridica, sede
[...]

## Art. 2 - Finalita' della Comunita'
La Comunita' persegue come finalita' principale [...]
Eventuali avanzi di gestione sono destinati a [...]

## Art. 3 - Perimetro della CACER
La Comunita' opera nell'ambito della cabina primaria [ID] e dei seguenti
Comuni: [...]. La sede legale resta nel Comune di [...].

## Art. 4 - Soci della Comunita'
4.1 Possono essere soci: [persone fisiche, PMI, enti locali, terzo settore, ...]
4.2 Le grandi imprese non possono essere soci.
4.3 La partecipazione delle PMI e' ammessa solo se la stessa non costituisce
    attivita' commerciale o industriale principale.
4.4 L'adesione avviene su domanda; il recesso e' libero secondo le modalita'
    previste dal regolamento interno.

## Art. 5 - Governance
5.1 Sono organi della Comunita': assemblea dei soci, organo di amministrazione, [...]
5.2 Le decisioni sono assunte secondo il principio dell'autonomia, con voto
    [capitario / proporzionale entro limiti, da definire].
5.3 [Frequenza assemblea, deleghe, quorum.]

## Art. 6 - Impianti e gestione tecnica
[Titolarita' impianti, manutenzione, ESCo se applicabile.]

## Art. 7 - Energia condivisa e flussi economici
La Comunita' aderisce al servizio CACER del GSE secondo D.Lgs. 199/2021 art. 31 e
DM MASE 7/12/2023. Il calcolo dell'energia condivisa segue il TIAD ARERA.

## Art. 8 - Ripartizione dei benefici
[Criteri: quota proporzionale al consumo / quota fissa + variabile / quota
sociale destinata a finalita' di comunita'. DA DEFINIRE CON I FONDATORI.]

## Art. 9 - Referente verso il GSE
9.1 La Comunita' nomina come referente [...]
9.2 Il referente e' autorizzato a sottoscrivere mandati e dichiarazioni
    necessarie per la qualifica del servizio CACER.
9.3 Il referente rendiconta ai soci i flussi TIP e TR ricevuti dal GSE.

## Art. 10 - Patrimonio e contributi
[...]

## Art. 11 - Modifiche statutarie
[...]

## Art. 12 - Scioglimento e destinazione del patrimonio residuo
[...]

## Art. 13 - Norma di rinvio
Per quanto non espressamente previsto, si applicano le disposizioni del
D.Lgs. 199/2021 art. 31, del DM MASE 7/12/2023, del TIAD ARERA 727/2022/R/eel
e delle Regole Operative CACER del GSE pro tempore vigenti.

## Avvertenza
Bozza tecnica di supporto; richiede revisione di notaio, consulente legale e
commercialista prima della sottoscrizione.
```

## Limiti del task

- La bozza non e' atto pubblico ne' valido ai fini civili.
- Non sostituisce la verifica del terzo settore (RUNTS, regimi fiscali) ne' il regime aiuti di Stato.
- Non disciplina aspetti contrattuali tra CER e ESCo / EPC esterno: rinvio a contratti separati.
