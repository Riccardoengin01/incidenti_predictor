import sys
from pathlib import Path
import pandas as pd

# Ensure project root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts import inserisci_incidenti


def test_salva_e_leggi_incidente(tmp_path):
    csv_path = tmp_path / "incidents.csv"
    inserisci_incidenti.file_path = str(csv_path)

    incidente = {h: f"val_{i}" for i, h in enumerate(inserisci_incidenti.HEADERS)}
    inserisci_incidenti.salva_incidente(incidente)

    df = pd.read_csv(csv_path)
    assert list(df.columns) == inserisci_incidenti.HEADERS
    assert df.iloc[0].to_dict() == incidente
