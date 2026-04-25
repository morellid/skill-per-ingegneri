# DVR Generico (D.Lgs. 81/2008 art. 17, 28, 29)

> Versione: 0.1.0-alpha
> Stato: in sviluppo

Skill di supporto alla redazione, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) per qualsiasi azienda italiana.

## Target

- **Datori di lavoro** (responsabilita' non delegabile art. 17 co. 1 lett. a)
- **RSPP** interni o esterni
- **HSE manager** aziendali
- **Consulenti sicurezza sul lavoro** che redigono DVR per clienti

Skill **trasversale** ai settori: uffici, manifattura, servizi, sanita', commercio, ristorazione, ecc. Sinergica con `pos-allegato-xv-checker` per cantieri.

## Cosa fa

Quattro sotto-attivita':

1. **Stesura DVR** (`draft-dvr.md`) - guida la stesura conforme art. 28 co. 2
2. **Verifica DVR esistente** (`check-dvr.md`) - check 6 contenuti minimi + formali (data certa, firme)
3. **Valutazione aggiornamento** (`valuta-aggiornamento.md`) - decide se serve rielaborare per art. 29 co. 3
4. **Mappa rischi mansione** (`mappa-rischi-mansione.md`) - rischi attesi per profilo lavorativo

Vedi [SKILL.md](SKILL.md) per il dettaglio.

## Fonti consultate

- D.Lgs. 9 aprile 2008 n. 81 - testo coordinato gennaio 2025 INL (hash uguale a `pos-allegato-xv-checker`)
- INAIL strumenti settoriali (OIRA), riferimenti
- Coordinamento Tecnico Regioni - DM 30/11/2012 (procedure standardizzate < 50 lav.)

Vedi [references/sources.yaml](references/sources.yaml).

## Sinergie

- **POS** (`pos-allegato-xv-checker`): per cantieri temporanei o mobili
- **GDPR** (`gdpr-registro-dpia`): se DVR include sorveglianza sanitaria, biometria accessi, videosorveglianza
- **AI Act** (`ai-act-compliance`): se uso sistemi AI per HR/monitoraggio lavoratori

## Limiti noti

- **Alpha**: non validata da RSPP esterno
- Non sostituisce RSPP/medico competente/datore di lavoro firmatario
- Non quantifica numericamente esposizioni (rumore, vibrazioni, chimico) - servono tecnici abilitati
- Non sostituisce sorveglianza sanitaria
- Per cantieri usare `pos-allegato-xv-checker`

Vedi [SKILL.md](SKILL.md) sezione "Limiti".

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).

## Disclaimer

Strumento di supporto. **Ogni DVR prodotto richiede revisione del RSPP, validazione del datore di lavoro, e consultazione obbligatoria del RLS (art. 29 co. 2). Coinvolgimento del medico competente nei casi di art. 41.**

Sanzioni: arresto 3-6 mesi o ammenda 2.949 - 7.532 EUR per omessa redazione; ammende fino a 5.695 EUR per DVR con elementi mancanti.
