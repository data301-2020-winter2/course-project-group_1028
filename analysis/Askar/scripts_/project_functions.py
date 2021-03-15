import pandas as pd

def load_and_process(url):
    df = (pd.read_csv(url)
           .dropna()
           .drop(['weathersit','season'], axis=1)
           .drop_duplicates()
           .rename(columns={'dteday':'date', 'yr':'year', 'hr':'hour'})
           .sort_values(['date']))
    df["workingday"] = df["workingday"].astype(bool)
    return df
