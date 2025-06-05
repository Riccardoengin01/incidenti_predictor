import pandas as pd
import matplotlib.pyplot as plt
import os

# Percorso del file
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.normpath(os.path.join(base_dir, "..", "data", "incidents.csv"))

# Caricamento dati
try:
    df = pd.read_csv(csv_path, sep=",")
    print("🧪 Colonne trovate:", df.columns.tolist())
    print(df.head())
except FileNotFoundError:
    print("❌ ERRORE: Il file incidents.csv non è stato trovato.")
    exit()

# Totale incidenti
print(f"📌 Totale incidenti registrati: {len(df)}")

# Incidenti per tipologia
tipi = df['Tipologia'].value_counts()
print("\n📊 Incidenti per tipologia:")
print(tipi)

# Incidenti per gravità
gravita = df['Gravità'].value_counts()
print("\n📊 Incidenti per gravità:")
print(gravita)

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

print("\n📈 Incidenti per anno:")
print(by_year)

plt.figure(figsize=(8, 5))
by_year.plot(kind='bar')
plt.title("Incidenti per Anno")
plt.xlabel("Anno")
plt.ylabel("Numero di incidenti")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
