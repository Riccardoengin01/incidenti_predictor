"""
Questo modulo gestisce la configurazione e l'inizializzazione del database.
Utilizza SQLAlchemy per creare un database SQLite e definire la tabella 'incidents'.
La struttura della tabella viene creata dinamicamente basandosi sulla lista HEADERS
importata da constants.py.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from constants import HEADERS
import os

# Assicura che la directory 'data' esista
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# Percorso completo del file del database SQLite
DB_PATH = os.path.join(DATA_DIR, 'incidents.sqlite3')

# Creazione del motore di connessione al database
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)

# SessionLocal sarà usato da altre parti dell'applicazione per interagire con il DB
SessionLocal = sessionmaker(bind=engine)

# Base per i modelli dichiarativi di SQLAlchemy
Base = declarative_base()

class Incident(Base):
    """Modello SQLAlchemy che rappresenta la tabella 'incidents'."""
    __tablename__ = 'incidents'
    id = Column(Integer, primary_key=True, autoincrement=True)

# Crea dinamicamente le colonne di tipo String per ogni header definito in constants.py
for header in HEADERS:
    setattr(Incident, header, Column(String))

# Crea la tabella nel database se non esiste già
Base.metadata.create_all(engine)
