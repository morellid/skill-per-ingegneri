# Reg. di esecuzione (UE) 2024/2690 - Nota strutturale

> Fonte: Regolamento di esecuzione (UE) 2024/2690 della Commissione del 17 ottobre 2024.
> Fonte catalogata in `sources.yaml` come `reg-ese-2024-2690`.
> URL: https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=OJ:L_202402690
> Data consultazione: 2026-04-29.
>
> **AVVISO**: il PDF di questo regolamento non e' stato scaricato ne' letto in v0.1.0-alpha
> (`sources.yaml`: `binary_path: null`, `sha256: null`, nessun `md_path`).
> Questo file contiene SOLO informazioni strutturali ricavabili dai metadati pubblici del
> regolamento (titolo, ambito dichiarato, natura giuridica). Non contiene estratti verbatim
> ne' parafrasi di contenuto normativo. Per l'uso operativo del Reg. 2024/2690 e' necessario
> scaricare il PDF, verificarne l'hash SHA256 e creare `references/fonti/reg-ese-2024-2690.md`.

---

## Che cosa e' questo regolamento

Regolamento di esecuzione (UE) 2024/2690 della Commissione europea del 17 ottobre 2024,
adottato ai sensi dell'art. 21 della Direttiva (UE) 2022/2555 (NIS 2). Si applica direttamente
negli Stati Membri senza trasposizione.

## Ambito soggettivo dichiarato (dal titolo e dai metadati ufficiali EU)

Il regolamento riguarda i requisiti tecnici e metodologici delle misure di gestione dei rischi di
cibersicurezza per un sottoinsieme specifico di soggetti NIS2. L'elenco ufficiale dei soggetti
coperti e' definito all'art. 1 del Regolamento stesso (non verificabile senza il PDF).

Per il contesto della skill: i soggetti NON coperti da questo Regolamento (ossia la generalita'
degli operatori italiani: energia, trasporti, banche, sanita', acqua, manifattura, PA, ricerca)
seguono come riferimento operativo la **Determinazione ACN 379907/2025** (vigente dal
15/01/2026), che e' la fonte primaria di questa skill.

## Come usare questa informazione nella skill

Quando l'utente appartiene a una categoria potenzialmente coperta dal Reg. 2024/2690 (es.
fornitore cloud, gestore DNS, data center, CDN, servizi gestiti, piattaforme social, trust service
providers), la skill:

1. Segnala che oltre alle misure ACN (Allegati 1/2 Det. 379907/2025) potrebbe applicarsi anche
   il Reg. UE 2024/2690 come requisito tecnico specifico;
2. Rinvia al CISO o consulente cyber specializzato per il dettaglio;
3. Non produce gap analysis sul Reg. 2024/2690 (fuori scope v0.1.0-alpha).

## Nota per iterazioni successive

Per estendere la skill a soggetti coperti dal Reg. 2024/2690:
1. Scaricare il PDF da EUR-Lex (URL in `sources.yaml`).
2. Verificare SHA256 e aggiornare `sources.yaml`.
3. Creare `references/fonti/reg-ese-2024-2690.md` con trascrizione verbatim degli articoli
   rilevanti.
4. Solo dopo, aggiornare estratti e task.
