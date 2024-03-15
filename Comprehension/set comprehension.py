

import pandas as pd
df=pd.read_csv(r"C:\Users\SightSpectrum\Documents\phones.csv")
# print(df.drop_duplicates())
print(df.fillna(56))
#df=pd.read_csv(r"C:\Users\SightSpectrum\Desktop\New folder\Mobilephones_dataset_final.csv")
# print(df.shape)
# print(df.dropna(how="any").shape)
# print(df.isnull().sum())
# print(df.describe())
# print(df.tail())
# print(df.head())
# df.info()
# df.dropna(inplace=True)
# print(df.to_string())

