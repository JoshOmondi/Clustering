import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print("Data loaded. Columns:", df.columns.tolist())
    return df