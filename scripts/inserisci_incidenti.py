from constants import HEADERS
from database import SessionLocal, Incident
import logging

logger = logging.getLogger(__name__)

# Dati salvati in SQLite


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

def salva_incidente(incidente: dict):
    """Persist incident into SQLite database"""
    with SessionLocal() as session:
        record = Incident(**incidente)
        session.add(record)
        session.commit()
    logger.info("✅ Incidente salvato correttamente.")

if __name__ == "__main__":
    incidente = chiedi_input()
    salva_incidente(incidente)
