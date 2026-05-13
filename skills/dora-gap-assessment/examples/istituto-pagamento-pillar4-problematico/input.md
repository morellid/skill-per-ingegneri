# Esempio problematico - Pillar 4 (fornitori terzi TIC) - istituto di pagamento

> Caso fittizio costruito per testare la skill su uno scenario con lacune diffuse. Le evidenze sono realistiche per una startup di pagamenti che ha esternalizzato pesantemente l'infrastruttura.

## Entita'

**Nome**: FastPay S.p.A. (fittizio).
**Categoria DORA art. 2 par. 1**: lettera d (istituto di pagamento ai sensi della direttiva 2015/2366/UE).
**Microimpresa (art. 3 n. 60)**: no (50 dipendenti, fatturato 12M EUR/anno).
**Quadro semplificato (art. 16 par. 1)**: l'utente afferma che FastPay rientra nelle "imprese di investimento piccole e non interconnesse", **ma e' un istituto di pagamento, non un'impresa di investimento**. L'art. 16 par. 1 si applica solo a categorie elencate (imprese di investimento piccole non interconnesse, istituti di pagamento esentati dalla direttiva 2015/2366, ecc.) - il professionista deve verificare con attenzione il quadro applicabile. Assumere QUADRO COMPLETO finche' non verificato.

## Pillar oggetto del gap assessment

Pillar 4 (DORA artt. 28-30).

## Documentazione disponibile

- Procedura interna "Gestione Fornitori IT" v1.0 (2023): copre 3 pagine, descrive solo il processo di scelta del fornitore.
- Foglio Excel con elenco dei 47 fornitori IT (non chiamato "registro delle informazioni" ma di fatto svolge quella funzione).
- Modello standard di contratto IT versione 2022 (precedente a DORA): include riservatezza, SLA generici, durata, recesso. **Non include** clausole specifiche TLPT, monitoraggio continuo, strategie di uscita.
- I 3 contratti per "funzioni essenziali" (provider cloud principale AWS, provider switch pagamenti, provider KYC) sono basati sul modello standard, con sole modifiche di SLA.
- Non esiste documento "strategia per i rischi da terzi" ne' "politica per l'uso di servizi TIC a supporto di funzioni essenziali o importanti".
- Non esistono strategie di uscita documentate.

## Evidenze operative

- Il registro non e' mai stato comunicato all'autorita' competente (l'utente non era a conoscenza dell'obbligo dell'art. 28 par. 3).
- L'organo di gestione non riesamina periodicamente i rischi (l'argomento e' stato discusso al CdA solo 2 volte negli ultimi 18 mesi).
- Nessuna due diligence formale eseguita sui fornitori esistenti (sono stati scelti per relazioni commerciali pregresse o per costo).
- Audit/ispezione: previsto contrattualmente solo per 1 dei 3 fornitori critici, e mai esercitato.
- Subappalti: l'utente sa che AWS subappalta servizi (es. supporto), ma non e' stato valutato il rischio.
- Fornitori in paesi terzi: 2 dei 47 fornitori IT hanno sede negli USA, ma non e' stata documentata alcuna valutazione di rischio paese terzo.

## Domanda

Fai il gap assessment Pillar 4 di FastPay rispetto a DORA artt. 28-30. Indica le aree non conformi e quelle che richiedono urgenza di rimediazione.
