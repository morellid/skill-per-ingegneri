# Reg. di esecuzione (UE) 2024/2690 - Ambito di applicazione

> Fonte: Regolamento di esecuzione (UE) 2024/2690 della Commissione del 17 ottobre 2024.
> Fonte catalogata in `sources.yaml` come `reg-ese-2024-2690`.
> URL: https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=OJ:L_202402690
> Data consultazione: 2026-04-29.

## Cosa fa questo regolamento

Stabilisce i **requisiti tecnici e metodologici** delle misure di gestione del rischio di cybersicurezza previste dall'art. 21 della Direttiva (UE) 2022/2555 (NIS 2) per un **sottoinsieme specifico di soggetti**. Si applica direttamente in Italia senza necessita' di trasposizione (e' un regolamento UE).

## Ambito soggettivo (art. 1)

Il Regolamento si applica esclusivamente ai seguenti soggetti, indipendentemente dal loro Stato membro di stabilimento:

1. Fornitori di servizi DNS
2. Gestori di registri dei nomi di dominio di primo livello (TLD)
3. Fornitori di servizi cloud computing
4. Fornitori di servizi di data center
5. Fornitori di reti di distribuzione dei contenuti (CDN)
6. Fornitori di servizi gestiti
7. Fornitori di servizi di sicurezza gestiti
8. Mercati online
9. Motori di ricerca online
10. Piattaforme di social network
11. Prestatori di servizi fiduciari (trust service providers)

## Ambito di NON applicazione

Il Regolamento NON si applica agli **altri soggetti NIS2**: ad esempio operatori energia, trasporti, banche, sanita', acqua, manifattura, PA, ricerca. Per questi soggetti il riferimento operativo italiano sono le **misure di base ACN** (Determinazioni 164179/2025 e 379907/2025).

## Principio di proporzionalita'

Il Regolamento riconosce il principio di proporzionalita' (considerando di apertura): i soggetti possono adottare **misure compensative** se non possono attuare alcuni requisiti per dimensioni o specificita' operativa. Le misure devono essere documentate.

## Allineamento con ISO/IEC 27001

Il Regolamento e' costruito in modo da risultare coerente con l'adesione alla **norma ISO/IEC 27001** (sistema di gestione della sicurezza delle informazioni - SGSI) come strada di compliance pratica per i soggetti coperti.

## Definizione di incidente significativo

Il Regolamento contiene anche le specifiche per determinare quando un incidente e' "significativo" ai sensi dell'art. 23 della Direttiva, **per il sottoinsieme di soggetti coperti**. Per gli altri soggetti italiani vale la definizione dell'art. 25 co. 4 D.Lgs. 138/2024 + soglie ACN.

## Linee guida ENISA

L'ENISA ha pubblicato (versione draft 2024 e versione finale 2025) le **Technical implementation guidance** sul Regolamento 2024/2690, disponibili sul portale `enisa.europa.eu`. Costituiscono il riferimento tecnico per l'implementazione operativa dei requisiti del Regolamento.

## Quando questa skill rinvia al Regolamento 2024/2690

La skill `nis2-self-assessment` e' tarata sul recepimento italiano D.Lgs. 138/2024 + ACN. Quando l'utente classifica la propria organizzazione come uno dei 11 tipi di soggetto coperti dal Reg. 2024/2690, la skill:

1. Conferma la classificazione NIS2 (perimetro essenziale/importante);
2. Segnala che il riferimento operativo per le misure tecniche e' il **Reg. UE 2024/2690 + linee guida ENISA**, non solo le determinazioni ACN;
3. Rinvia al CISO/consulente cyber specializzato per il dettaglio dei requisiti tecnici;
4. Non produce gap analysis dettagliata sul Reg. 2024/2690 (skill futura dedicata se richiesta).
