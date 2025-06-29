import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from constants import HEADERS
from database import SessionLocal, Incident

# Percorso file CSV (non più utilizzato)
CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "incidents.csv")


def load_data():
    """Load incidents from the SQLite database"""
    with SessionLocal() as session:
        incidents = session.query(Incident).all()
        rows = [
            {h: getattr(inc, h) for h in HEADERS}
            for inc in incidents
        ]
    if rows:
        return pd.DataFrame(rows, columns=HEADERS)
    return pd.DataFrame(columns=HEADERS)


def append_incident(data: dict):
    """Insert a new incident into the SQLite database"""
    with SessionLocal() as session:
        incident = Incident(**data)
        session.add(incident)
        session.commit()


st.title("HSE Incidenti - Streamlit")
choice = st.sidebar.radio("Menu", ["Elenco", "Nuovo", "Statistiche"])

if choice == "Elenco":
    df = load_data()
    st.dataframe(df)

elif choice == "Nuovo":
    st.subheader("Inserisci nuovo incidente")
    with st.form("incident_form"):
        inputs = {h: st.text_input(h) for h in HEADERS}
        submitted = st.form_submit_button("Salva")
        if submitted:
            append_incident(inputs)
            st.success("Incidente salvato con successo")

else:  # Statistiche
    df = load_data()
    if df.empty:
        st.info("Nessun dato disponibile")
    else:
        st.subheader("Incidenti per Tipologia")
        fig1 = plt.figure()
        df['Tipologia'].value_counts().plot(kind='bar')
        plt.tight_layout()
        st.pyplot(fig1)

        st.subheader("Distribuzione Gravità")
        fig2 = plt.figure()
        df['Gravità'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.tight_layout()
        st.pyplot(fig2)

        st.subheader("Incidenti per Anno")
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
        fig3 = plt.figure()
        df['Data'].dt.year.value_counts().sort_index().plot(kind='bar')
        plt.tight_layout()
        st.pyplot(fig3)
