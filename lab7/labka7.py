import pandas as pd
import numpy as np

df = pd.read_excel('catalog_products.xlsx')

#task 1
print("Алғашқы 5 жол:\n", df.head())
print("\nDataFrame пішіні:", df.shape)
print("\nДеректер түрлері:\n", df.dtypes)
print("\nБос мәндер саны:\n", df.isnull().sum())

#task 2
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].astype(float)

df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

df.dropna(subset=['col_7'], inplace=True)
