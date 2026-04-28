# Det. ACN n. 164179/2025 - Allegato 1 - Misure di base per soggetti importanti

> Fonte: Agenzia per la Cybersicurezza Nazionale, Determinazione n. 164179 del 14 aprile 2025, Allegato 1.
> Fonte catalogata in `sources.yaml` come `acn-det-164179-2025`.
> Estratto strutturale. Per il testo verbatim integrale fare riferimento al PDF in `not_in_repo/acn-det-164179-2025-allegato1.pdf` (da scaricare dal portale ACN).
> Data consultazione: 2026-04-29.
>
> **Avvertenza**: la Determinazione ACN 164179/2025 e' stata sostituita dalla **Determinazione ACN 379907/2025** (in vigore dal 15 gennaio 2026). Per i soggetti importanti la versione aggiornata 2026 prevede 37 misure e 87 requisiti. Verificare la determinazione vigente sul portale ACN (`acn.gov.it/portale/en/nis/modalita-specifiche-base`) prima di citare requisiti specifici.

## Approccio

L'Allegato 1 contiene un **sottoinsieme** delle misure dell'Allegato 2 (essenziali), tarato sulla minore esposizione/criticita' dei soggetti importanti. La struttura per funzioni del Framework Nazionale Cybersecurity (ed. 2025) e' la stessa:

1. **GOVERNO (GOVERN)** - GV.OC, GV.RM, GV.RR, GV.PO, GV.SC
2. **IDENTIFICAZIONE (IDENTIFY)** - ID.AM, ID.RA, ID.IM
3. **PROTEZIONE (PROTECT)** - PR.AA, PR.AT, PR.DS, PR.PS, PR.IR
4. **RILEVAMENTO (DETECT)** - DE.CM
5. **RISPOSTA (RESPOND)** - RS.MA, RS.CO
6. **RIPRISTINO (RECOVER)** - RC.RP, RC.CO

## Differenze chiave rispetto agli essenziali

I soggetti **importanti** hanno requisiti generalmente **piu' leggeri** rispetto agli essenziali nelle stesse sottocategorie. Esempi tipici di alleggerimento:

- **MFA (PR.AA-03)**: per gli importanti puo' bastare per accessi privilegiati e remoti. Per gli essenziali e' tipicamente esteso e con autenticazione continua per asset critici.
- **Backup (PR.DS-11)**: per gli importanti backup periodici testati. Per gli essenziali backup off-line/air-gapped + test di ripristino frequente.
- **SOC/Monitoraggio (DE.CM)**: per gli importanti monitoraggio essenziale degli eventi sui sistemi rilevanti. Per gli essenziali SOC/SIEM con presidio attivo.
- **Supply chain (GV.SC)**: per gli importanti requisiti di base. Per gli essenziali esercizio di TPRM (third-party risk management) approfondito.

## Numerica complessiva

- Soggetti importanti (Allegato 1): ~ 28-30 sottocategorie nella Det. 164179/2025; **37 misure / 87 requisiti** nella Det. 379907/2025 aggiornata.
- Soggetti essenziali (Allegato 2): ~ 35 sottocategorie nella Det. 164179/2025; **43 misure / 116 requisiti** nella Det. 379907/2025.

## Tempi di adeguamento

- **18 mesi** dalla notifica di inserimento nell'elenco NIS per implementare le misure di sicurezza.
- **9 mesi** dalla notifica per l'obbligo di notifica incidenti significativi.
- **31 ottobre 2026**: termine ultimo per la piena operativita' delle misure di base (art. 4 Det. 379907/2025).

## Fonte primaria da scaricare

Per il testo verbatim e i requisiti specifici di ciascuna sottocategoria, scaricare dal portale ACN:
- Pagina riepilogativa: `https://www.acn.gov.it/portale/en/nis/modalita-specifiche-base`
- Determinazione 164179/2025 firmata: `https://www.acn.gov.it/portale/documents/d/guest/detacn_nis_specifiche_2025_164179_signed`

E catalogare il file in `not_in_repo/` con SHA256 in `sources.yaml`.
