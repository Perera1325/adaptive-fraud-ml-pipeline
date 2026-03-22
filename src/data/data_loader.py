import pandas as pd
import os

def load_all_datasets(data_path="data/raw"):
    datasets = {}

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            full_path = os.path.join(data_path, file)
            try:
                df = pd.read_csv(full_path)
                datasets[file] = df
                print(f"Loaded: {file} | Shape: {df.shape}")
            except Exception as e:
                print(f"Error loading {file}: {e}")

    return datasets