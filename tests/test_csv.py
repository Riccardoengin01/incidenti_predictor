import sys
from pathlib import Path
from sqlalchemy import create_engine

# Ensure project root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts import inserisci_incidenti
import database


def test_salva_e_leggi_incidente(tmp_path):
    db_path = tmp_path / "incidents.sqlite3"
    engine = create_engine(f"sqlite:///{db_path}")
    database.SessionLocal.configure(bind=engine)
    database.Base.metadata.create_all(engine)

    incidente = {h: f"val_{i}" for i, h in enumerate(inserisci_incidenti.HEADERS)}
    inserisci_incidenti.salva_incidente(incidente)

    with database.SessionLocal() as session:
        row = session.query(database.Incident).first()
        retrieved = {h: getattr(row, h) for h in inserisci_incidenti.HEADERS}

    assert retrieved == incidente
