import pandas as pd

def load_and_process(url):
    df = (pd.read_csv(url)
           .dropna()
           .drop_duplicates()
           .rename(columns={'dteday':'date'})
           .sort_values(['date','hr']))
    df["workingday"] = df["workingday"].astype(bool)
    return df

