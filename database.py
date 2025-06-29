from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from constants import HEADERS
import os

# Ensure data directory exists
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, 'incidents.sqlite3')
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Incident(Base):
    __tablename__ = 'incidents'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Dynamically create string columns for each header

for header in HEADERS:
    setattr(Incident, header, Column(String))

Base.metadata.create_all(engine)
