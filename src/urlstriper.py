import pandas as pd

urldf = pd.read_csv("sample1.csv", encoding="gb2312")
empty_sample = urldf[urldf.isnull().any(axis=1)]
print(empty_sample.head())