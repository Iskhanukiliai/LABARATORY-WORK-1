import pandas as pd
import numpy as np

try:
    df = pd.read_excel('catalog_products.xlsx')
    print("Деректер сәтті жүктелді.")
except FileNotFoundError:
    print("Қате: catalog_products.xlsx файлы табылмады!")
    raise
except Exception as e:
    print(f"Қате орын алды: {e}")
    raise

#task 1
print(f"\nКесте өлшемі (пішімі): {df.shape}")
print("\nБағандардың деректер типі (алғашқы 5):")
print(df.dtypes.head())

#task 2
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna("Белгісіз")
print("\n--- Тексеру (task 2) ---")
print("Бос ұяшықтар саны (нөл болуы керек):")
print(df.isnull().sum().head())

print("\nКестенің алғашқы 5 жолы:")
print(df.head())