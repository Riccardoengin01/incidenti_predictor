from flask import render_template, request, redirect, flash
from app import app
from app.constants import HEADERS
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

# Percorso CSV
CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "incidents.csv"))

# ROUTE PRINCIPALE
@app.route("/")
def index():
    return render_template("index.html")

# INSERIMENTO INCIDENTE
@app.route("/inserisci", methods=["GET", "POST"])
def inserisci():
    if request.method == "POST":
        incidente = [request.form.get(h) for h in HEADERS]
        file_esiste = os.path.exists(CSV_PATH)
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_esiste:
                writer.writerow(HEADERS)
            writer.writerow(incidente)
        flash("✅ Incidente salvato con successo!")
        return redirect("/inserisci")
    return render_template("form.html", headers=HEADERS)

# TABELLA INCIDENTI
@app.route("/incidenti")
def elenco_incidenti():
    dati = []
    intestazioni = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            intestazioni = next(reader)
            dati = list(reader)
    return render_template("incidenti.html", dati=dati, intestazioni=intestazioni)

@app.route("/dashboard")
def dashboard():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Percorsi
    csv_path = CSV_PATH
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))

    print("📂 CSV path:", csv_path)
    print("📂 Static path:", static_path)

    if not os.path.exists(csv_path):
        return "File CSV non trovato."

    df = pd.read_csv(csv_path)

    if df.empty:
        return "Nessun dato da visualizzare."

    # Grafico Tipologia
    fig1 = plt.figure()
    df['Tipologia'].value_counts().plot(kind='bar')
    plt.title("Incidenti per Tipologia")
    plt.ylabel("Numero")
    plt.xticks(rotation=45)
    fig1.tight_layout()
    tip_path = os.path.join(static_path, "grafico_tipologia.png")
    fig1.savefig(tip_path)
    plt.close(fig1)
    print(f"✅ Grafico 1 salvato in: {tip_path}")

    # Grafico Gravità
    fig2 = plt.figure()
    df['Gravità'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Distribuzione Gravità")
    fig2.tight_layout()
    grav_path = os.path.join(static_path, "grafico_gravita.png")
    fig2.savefig(grav_path)
    plt.close(fig2)
    print(f"✅ Grafico 2 salvato in: {grav_path}")

    # Grafico Anno
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    fig3 = plt.figure()
    df['Data'].dt.year.value_counts().sort_index().plot(kind='bar')
    plt.title("Incidenti per Anno")
    plt.ylabel("Numero")
    plt.xticks(rotation=45)
    fig3.tight_layout()
    year_path = os.path.join(static_path, "grafico_anno.png")
    fig3.savefig(year_path)
    plt.close(fig3)
    print(f"✅ Grafico 3 salvato in: {year_path}")

    return render_template("dashboard.html")
