# stabilita-pendii-naturali-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere geotecnico/geologo da completare)

Skill di **supporto documentale** al **progettista geotecnico** e al **geologo** per l'**inquadramento dello
studio e della verifica di stabilita' dei pendii naturali** secondo le **NTC 2018** (D.M. 17 gennaio 2018),
**paragrafo 6.3**: prescrizioni e indagini, modellazione geologica e geotecnica, verifica di sicurezza,
interventi di stabilizzazione e monitoraggio.

**Non calcola** il coefficiente di sicurezza né **esegue** le verifiche, **non definisce** il modello
geologico/geotecnico né **progetta** gli interventi, e **non sostituisce** il progettista: fornisce i criteri,
la definizione della verifica (F = τf/τ su valori caratteristici), i criteri di scelta delle superfici e le
regole di monitoraggio.

## Target

Ingegneri geotecnici e geologi che devono inquadrare lo studio e la verifica di stabilita' di un pendio naturale
(versante) secondo le NTC 2018 par. 6.3.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-stabilita-pendio` | Verifica di sicurezza: F = τf/τ su valori caratteristici (senza coefficienti parziali), superfici accertate/critiche, pressioni interstiziali, margine giustificato dal progettista (§6.3.4) |
| `inquadra-indagini-interventi-monitoraggio` | Prescrizioni e indagini, modellazione geologica/geotecnica, interventi di stabilizzazione e monitoraggio (§6.3.1-6.3.3, 6.3.5-6.3.6) |

Nucleo: **coefficiente di sicurezza F = τf/τ** (resistenza al taglio disponibile / tensione agente) su
**parametri e azioni al valore caratteristico** (a differenza di muri/fondazioni/tiranti, **senza** i
coefficienti parziali A1/A2, M, R), **superfici accertate** per i pendii in frana o **ricerca della superficie
critica** negli altri casi, e **monitoraggio** con soglie di attenzione/allarme (§6.3).

## Relazione con altre skill

- **Complementa** `opere-sostegno-ntc` (§6.5), `tiranti-ancoraggio-ntc` (§6.6) e
  `relazione-geologica-geotecnica-ntc` (che esclude esplicitamente i §6.3-6.12). Condivide la fonte GU con le
  altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.3** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** il coefficiente di sicurezza né **esegue** le verifiche (equilibrio limite/metodi numerici);
  **non** definisce il modello geologico/geotecnico né **progetta** gli interventi.
- **Non tratta** la stabilità dei pendii in **condizioni sismiche** (§7.11.3.5) né le **opere in materiali
  sciolti / fronti di scavo** (§6.8).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/geologo, né la lettura del par. 6.3 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
