# Sistema Predittivo Incidenti HSE

Progetto Python per registrare, analizzare e prevedere incidenti sul lavoro nei contesti Safety, Health & Security.

## Moduli attivi
- Inserimento incidenti CLI (CSV)
- Dashboard in sviluppo
- Analisi predittiva pianificata
- Interfaccia Streamlit

## Struttura
- /data: dati CSV
- /scripts: script Python
- /output: report ed esportazioni

## Requisiti
Le dipendenze principali sono elencate in `requirements.txt` e includono:

- **Flask** (>=2.0) per l'applicazione web
- **Flask-WTF** (>=1.0) per la protezione CSRF
- **pandas** (>=1.3) per l'analisi dati
- **matplotlib** (>=3.4) per i grafici
- **streamlit** (>=1.0) per l'interfaccia web alternativa

Prima di avviare l'applicazione **devi** impostare la variabile
d'ambiente `SECRET_KEY`. Senza di essa l'applicazione Flask non si avvierà,
poiché la chiave viene usata per firmare i cookie di sessione e abilitare la
protezione CSRF.

Esempio:

```bash
export SECRET_KEY="valore-sicuro"
python run.py
```

Se avvii solo la dashboard Streamlit (`streamlit_app.py`) questa variabile non è
necessaria.

## Generazione del dataset e dei grafici

Il file `data/incidents.csv` non è tracciato nel repository. È possibile
crearlo o copiarne uno già esistente in due modi:

1. **Da terminale** con lo script interattivo:

   Per evitare errori di importazione esegui lo script come modulo:

   ```bash
   python -m scripts.inserisci_incidenti
   ```

   Le risposte inserite verranno salvate nel percorso `data/incidents.csv`.

2. **Dall'applicazione web** accedendo alla pagina `/inserisci` dopo
   l'avvio di Flask.

In alternativa, se disponi già di un file con la stessa struttura,
copialo manualmente nella cartella `data/` con il nome `incidents.csv`.

Una volta popolato il CSV, visitando la rotta `/dashboard` verranno creati i
grafici statistici nella cartella `static/` (`grafico_gravita.png` e
`grafico_tipologia.png`). Anche questi file sono esclusi dal controllo di
versione.

## Interfaccia Streamlit

In alternativa al server Flask, è possibile avviare una piccola dashboard
interattiva con Streamlit:

```bash
streamlit run streamlit_app.py
```

Questo comando aprirà l'applicazione nel browser predefinito, permettendo di
consultare gli incidenti registrati, inserirne di nuovi e visualizzare alcune
statistiche di base.

## Test
Per eseguire la suite di test è necessario aver installato le dipendenze del progetto. Una volta installate, lancia:

```bash
pytest
```

I test verificano la corretta scrittura e lettura del file CSV utilizzato dagli script.
