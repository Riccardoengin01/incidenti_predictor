import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

logger = logging.getLogger(__name__)

# Percorso del file
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.normpath(os.path.join(base_dir, "..", "data", "incidents.csv"))

# Caricamento dati
try:
    df = pd.read_csv(csv_path, sep=",")
    logger.info("🧪 Colonne trovate: %s", df.columns.tolist())
    logger.info("%s", df.head())
except FileNotFoundError:
    logger.error("❌ ERRORE: Il file incidents.csv non è stato trovato.")
    exit()

# Totale incidenti
logger.info("📌 Totale incidenti registrati: %s", len(df))

# Incidenti per tipologia
tipi = df['Tipologia'].value_counts()
logger.info("\n📊 Incidenti per tipologia:")
logger.info("%s", tipi)

# Incidenti per gravità
gravita = df['Gravità'].value_counts()
logger.info("\n📊 Incidenti per gravità:")
logger.info("%s", gravita)

# Grafico incidenti per tipologia
plt.figure(figsize=(8, 5))
tipi.plot(kind='bar')
plt.title("Incidenti per Tipologia")
plt.xlabel("Tipologia")
plt.ylabel("Numero di incidenti")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Analisi per anno ---
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
by_year = df['Data'].dt.year.value_counts().sort_index()

logger.info("\n📈 Incidenti per anno:")
logger.info("%s", by_year)

plt.figure(figsize=(8, 5))
by_year.plot(kind='bar')
plt.title("Incidenti per Anno")
plt.xlabel("Anno")
plt.ylabel("Numero di incidenti")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
