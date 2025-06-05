import csv
import os
from datetime import datetime
from constants import HEADERS
import logging

logger = logging.getLogger(__name__)

# Percorso del file CSV
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "data", "incidents.csv")
file_path = os.path.normpath(file_path)


def chiedi_input():
    logger.info("➕ INSERIMENTO NUOVO INCIDENTE")

    incidente = {
        "Data": input("Data (YYYY-MM-DD): "),
        "Ora": input("Ora (HH:MM): "),
        "Luogo": input("Luogo: "),
        "Area": input("Area [Interno/Esterno]: "),
        "Tipologia": input("Tipologia (es. Caduta, Urto...): "),
        "Gravità": input("Gravità [Bassa/Media/Alta/Mortale]: "),
        "Descrizione": input("Descrizione breve: "),
        "Impresa": input("Impresa coinvolta: "),
        "Mansione": input("Mansione lavoratore: "),
        "Fase_lavorativa": input("Fase lavorativa (es. demolizione, carico...): "),
        "Esito": input("Esito [Infortunio/Near Miss/Altro]: "),
        "Azione_correttiva": input("Azione correttiva adottata: "),
    }
    return incidente

def salva_incidente(incidente):
    file_esiste = os.path.exists(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)

        if not file_esiste:
            writer.writeheader()

        writer.writerow(incidente)

    logger.info("✅ Incidente salvato correttamente.")

if __name__ == "__main__":
    incidente = chiedi_input()
    salva_incidente(incidente)
