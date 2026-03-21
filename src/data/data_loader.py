import pandas as pd

def load_csv(path):
    try:
        df = pd.read_csv(path)
        print(f"Loaded dataset: {path}")
        return df
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None