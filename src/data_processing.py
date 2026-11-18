"""Loading and basic data preparation."""
import pandas as pd

def load_health_data(path):
    """Load the health CSV and clean its column names."""
    data = pd.read_csv(path)
    data.columns = data.columns.astype(str).str.strip()
    return data

def disease_prevalence(data, column="disease"):
    """Return disease case count, total records and prevalence percentage."""
    cases = int((data[column] == 1).sum())
    total = int(data[column].notna().sum())
    return {"cases": cases, "total": total,
            "percentage": 100 * cases / total if total else float("nan")}
