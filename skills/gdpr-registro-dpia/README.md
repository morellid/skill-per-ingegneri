# GDPR Registro trattamenti + DPIA

> Versione: 0.1.0-alpha
> Stato: in sviluppo (post-estratti normativi, post-task, post-2-esempi)

Skill di supporto alla compliance GDPR per Registro delle attivita' di trattamento (art. 30) e Valutazione d'impatto sulla protezione dei dati (DPIA - art. 35).

## Target

Titolari del trattamento, responsabili del trattamento, DPO, ingegneri dell'informazione che progettano sistemi che trattano dati personali (in particolare nelle aziende italiane). Tipico early adopter al laboratorio CNI AI Initiative del 10 maggio 2026.

## Cosa fa

Quattro sotto-attivita' distinte:

1. **Stesura Registro art. 30** - guida la compilazione del Registro per titolare o responsabile
2. **Verifica Registro esistente** - controlla la completezza delle 7 voci (titolare) o 4 (responsabile)
3. **Valutazione soglia DPIA** - decide se una DPIA e' richiesta, basandosi su 12 tipologie italiane (Provv. Garante 467/2018) + 9 criteri WP248 + art. 35 par. 3
4. **Stesura/verifica DPIA** - struttura una DPIA con i 4 contenuti minimi (par. 7) o verifica una DPIA esistente

Vedi [SKILL.md](SKILL.md) per il dettaglio.

## Fonti consultate

- Reg. UE 2016/679 (GDPR) - testo italiano arricchito Garante (hash registrato)
- Provv. Garante n. 467/2018 - Allegato 1 - 12 tipologie soggette a DPIA (hash registrato)
- WP248 rev. 01 - linee guida DPIA (Article 29 WP, endorsed EDPB) - riferimento, no embed
- D.Lgs. 196/2003 (Codice Privacy come modificato dal D.Lgs. 101/2018) - riferimento

Vedi [references/sources.yaml](references/sources.yaml) per metadata completi e [references/estratti/](references/estratti/) per testi.

## Limiti noti

- **Alpha**: non ancora validata da DPO esterno
- Non sostituisce parere legale ne' parere DPO (obbligatorio per DPIA)
- Non valuta i trasferimenti extra-UE caso per caso
- Non copre AI Act (Reg. UE 2024/1689) - skill futura dedicata
- Non genera privacy policy verso interessati (art. 13/14) - skill futura

Vedi [SKILL.md](SKILL.md) sezione "Limiti".

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).

## Disclaimer

Strumento di supporto. **Ogni output richiede revisione del DPO o del consulente legale prima dell'adozione formale.** Sanzioni amministrative ex art. 83 GDPR (fino a 20M EUR o 4% del fatturato globale annuo).
