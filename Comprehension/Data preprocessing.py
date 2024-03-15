import pandas as pd

# Read the data into a DataFrame
df = pd.read_csv(r'C:\Users\SightSpectrum\Downloads\Sample.csv')
print(df)
print(df.shape)
# Drop duplicates
df = df.drop_duplicates()
print(df)
print(df.shape)
# # Drop rows with missing values
df = df.dropna()
print(df)
print(df.shape)
df=pd.DataFrame({"manufacturer":["Apple", "Samsung"], "Model":["Pixel5", "Mi11"], "color": ["White", "black"],
                 "storage_capacity":["64GB", "256GB"],
                 "screen_size":["5.9", "6.4"], "battery_capacity": ["3440", "5439"], "date":["Aug 18", "may 18"]})
print(df)
print(df.shape)
df.to_csv(r'C:\Users\SightSpectrum\Downloads\Final.csv', encoding = 'utf-8' , index = False)
