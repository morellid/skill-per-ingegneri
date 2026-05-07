# DM 58/2017 Allegato A punto 3 - Salto classi e asseverazione

> Fonte: DM 58/2017 Allegato A (testo aggiornato dal DM 65/2017, DM 24/2020, DM 329/2020).
> Consultata su: https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017
> Data accesso: 2026-05-07
> Licenza: dominio pubblico (atto normativo italiano)

## Salto classi

L'efficacia tecnica di un intervento di miglioramento sismico, ai fini della detrazione fiscale sismabonus, e' misurata dal **numero di classi di rischio guadagnate** (salto classi) tra:
- la **classe di rischio nello stato di fatto** (ante operam)
- la **classe di rischio nello stato di progetto** (post operam)

Il salto classi e' calcolato come:

```
salto_classi = posizione_in_graduatoria(classe_fatto) - posizione_in_graduatoria(classe_progetto)
```

con graduatoria A+ (idx 0) -> A (1) -> B (2) -> C (3) -> D (4) -> E (5) -> F (6) -> G (7).

Salto positivo => intervento efficace (classe migliorata).
Salto zero => nessun miglioramento di classe (anche se PAM/IS-V sono migliorati internamente, la classe e' la stessa).
Salto negativo => intervento peggiora la classe di rischio (anomalia: l'intervento non e' migliorativo, da rivedere).

## Asseverazione

L'attestazione del salto classi pre/post intervento e' redatta dal **professionista incaricato** (ingegnere strutturista o architetto abilitato per le strutture, in funzione delle competenze) tramite i modelli ministeriali:

- **Allegato B** al DM 58/2017: asseverazione classe pre-intervento + descrizione intervento (testo originario).
- **Allegato B-bis** introdotto dal DM 329/2020: asseverazione gia' nella fase di progetto strutturale, con classe attesa post-intervento.

Entrambi gli allegati prevedono firma digitale del professionista, marca da bollo, e deposito allegato alla pratica edilizia (CILA / SCIA / PdC) presso il SUE / SUAP del Comune. La formalizzazione dell'asseverazione **NON e' nello scope di questa skill**: la skill produce numeri (PAM, IS-V, classe, salto classi) che il professionista poi trasferisce sul modulo cartaceo / digitale.

## Aliquote fiscali (rinvio fuori scope)

Le aliquote di detrazione (50%, 70%, 75%, 80%, 85%, super-sismabonus 110% e successive evoluzioni "sismabonus rafforzato", "sismabonus acquisti") sono fissate dalla legislazione fiscale vigente (TUIR + leggi di bilancio successive). La determinazione dell'aliquota applicabile dipende da:
- numero classi guadagnate (1, 2 o piu')
- tipologia di edificio (singola unita', condominio)
- destinazione d'uso (residenziale, produttivo)
- tempistica dell'intervento (l'aliquota cambia per anno fiscale)
- specifiche varianti normative (super-sismabonus, sismabonus acquisti, ecc.)

**Questo va verificato dal commercialista o consulente fiscale del committente.** La skill produce solo il salto classi tecnico, NON traduce in aliquota.

## Note operative

- Il **metodo di analisi** (lineare, non lineare, push-over, time-history) e il **livello di conoscenza** LC1/LC2/LC3 (con relativo fattore di confidenza FC, NTC 2018 par. 8.5.4) **devono essere gli stessi** per stato di fatto e stato di progetto, per garantire la confrontabilita' del salto classi. La skill non controlla questo (input dell'utente), ma il task `valida-input.md` lo segnala come check da eseguire dal professionista.
- La PGA_D al sito **non cambia** tra fatto e progetto (dipende dal sito, non dall'edificio). La skill assume che PGA_D fornita per "fatto" valga anche per "progetto" se non ridichiarata.

## Riferimenti puntuali

- DM 58/2017 Allegato A punto 3 (testo coordinato DM 329/2020): salto classi
- DM 58/2017 art. 3 + Allegati B, B-bis: modelli di asseverazione (fuori scope skill)
- TUIR + leggi di bilancio: aliquote fiscali (fuori scope skill)
