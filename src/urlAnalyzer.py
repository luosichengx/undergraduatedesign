import pandas as pd

urldf = pd.read_csv("top-1m.csv", index_col=["index"])
print(urldf.head())
empty_sample = urldf[urldf.isnull().any(axis=1)]
print(empty_sample.head())