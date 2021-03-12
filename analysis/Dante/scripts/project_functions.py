def load_and_process(path):
    
    import pandas as pd
    load = (
    pd.read_csv(path,header = None)
    .rename(columns={0:"instant",1:"dteday",2:"season",3:"yr",4:"mnth",5:"hr",6:"holiday",7:"weekday",
                     8:"workingday",9:"weathersit",10:"temp",11:"atemp",12:"hum",13:"windspeed",
                     14:"casual",15:"registered",16:"cnt"})
    .dropna()
    .rename(index = lambda x: x + 1) 
    )

    return load