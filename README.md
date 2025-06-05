# Sistema Predittivo Incidenti HSE

Progetto Python per registrare, analizzare e prevedere incidenti sul lavoro nei contesti Safety, Health & Security.

## Moduli attivi
- Inserimento incidenti CLI (CSV)
- Dashboard in sviluppo
- Analisi predittiva pianificata

## Struttura
- /data: dati CSV
- /scripts: script Python
- /output: report ed esportazioni

## Requisiti
Le dipendenze principali sono elencate in `requirements.txt` e includono:

- **Flask** (>=2.0) per l'applicazione web
- **pandas** (>=1.3) per l'analisi dati
- **matplotlib** (>=3.4) per i grafici

Prima di avviare l'applicazione è necessario definire la variabile
d'ambiente `SECRET_KEY` che verrà utilizzata da Flask per firmare i cookie
di sessione.

Esempio:

```bash
export SECRET_KEY="valore-sicuro"
python run.py
```

## Generazione del dataset e dei grafici

Il file `data/incidents.csv` non è tracciato nel repository. È possibile
crearlo in due modi:

1. **Da terminale** con lo script interattivo:

   ```bash
   python scripts/inserisci_incidenti.py
   ```

   Le risposte inserite verranno salvate nel percorso `data/incidents.csv`.

2. **Dall'applicazione web** accedendo alla pagina `/inserisci` dopo
   l'avvio di Flask.

Una volta popolato il CSV, visitando la rotta `/dashboard` verranno creati i
grafici statistici nella cartella `static/` (`grafico_gravita.png` e
`grafico_tipologia.png`). Anche questi file sono esclusi dal controllo di
versione.
