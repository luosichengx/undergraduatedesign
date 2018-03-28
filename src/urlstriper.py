import pandas as pd

httpdf = pd.read_csv("sample1.csv", encoding="gb2312")
id_url_df = httpdf.loc[:,["用户名","域名"]]
print(id_url_df)
# empty_sample = id_url_df[id_url_df.isnull().any(axis=1)]
