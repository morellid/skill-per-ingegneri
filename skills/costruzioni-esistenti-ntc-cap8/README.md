# costruzioni-esistenti-ntc-cap8

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con strutturista da completare)

Skill di **consultazione del capitolo 8 delle NTC 2018** (costruzioni esistenti)
e del capitolo C8 della Circolare 7/2019. Aiuta il progettista a orientarsi tra
classificazione degli interventi, soglie di zeta_E, livelli di conoscenza e
fattori di confidenza.

**Non e' una skill di calcolo**: non esegue verifiche strutturali, non calcola
zeta_E, non sceglie ne' dimensiona interventi.

## Target

Ingegneri strutturisti, progettisti di interventi su edifici esistenti,
collaudatori statici.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `classifica-intervento` | Data la descrizione di un intervento e la classe d'uso: individua la categoria (riparazione/locale, miglioramento, adeguamento - par. 8.4), se l'adeguamento e' obbligatorio (casi a-e del par. 8.4.3) e la soglia di zeta_E applicabile (a,b,d -> 1,0; c,e -> 0,80; miglioramento 0,6 / +0,1 per classe d'uso) |
| `determina-lc-fc` | Dato lo stato delle indagini: individua il livello di conoscenza LC1/LC2/LC3 e il fattore di confidenza FC (1,35 / 1,20 / 1,00) secondo Circolare C8.5.4 e Tab. C8.5.IV, con le precisazioni su c.a./acciaio, muratura, materiali nuovi |
| `qa-cap8` | Q&A su quando sono obbligatorie la valutazione della sicurezza e la verifica del sistema di fondazione (par. 8.3), stati limite, elaborati minimi (8.7.5), definizioni di zeta_E e zeta_V,i |

## Fonti consultate

- **DM 17/01/2018 (NTC 2018)**, GU n. 42 del 20/02/2018 - **capitolo 8**
  (parr. 8.1-8.7.5)
- **Circolare MIT n. 7 del 21/01/2019**, GU n. 35 dell'11/02/2019 - **capitolo
  C8** (C8.3, C8.4.x, C8.5.4.x, Tab. C8.5.IV)

Dettaglio (URL, SHA256, trascrizioni) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`. I valori numerici dei fattori di
confidenza (1,35/1,2/1,0) provengono dalla **Circolare** C8.5.4, non dal testo
delle NTC.

## Limiti noti

- Non esegue verifiche strutturali ne' calcola zeta_E, le capacita' o le analisi
- Non sceglie ne' dimensiona le tecniche di intervento (par. 8.7)
- Non fornisce i valori di tabella dei parametri meccanici della muratura
  (C8.5.I/II/III)
- Non copre in dettaglio i meccanismi locali/globali e gli aggregati (8.7.1)
- Non sostituisce gli adempimenti procedurali del DPR 380/2001

**La skill supporta la consultazione della norma ma non sostituisce la
valutazione della sicurezza ne' il progettista firmatario (par. 8.3).**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
