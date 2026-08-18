import pandas as pd
from pathlib import Path


def load_data():
    """Load the supermarket sales dataset."""
    file_path = Path(__file__).resolve().parent.parent / "data" / "supermarket_sales.csv"

    df = pd.read_csv(file_path)

    return df