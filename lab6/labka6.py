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


#task 3
print("\nКестенің алғашқы 5 жолы:")
print(df.head())
print("\n--- task 3: Сандық мәліметтердің статистикасы ---")
stat_info = df.describe()
print("Негізгі статистикалық көрсеткіштер:")
print(stat_info.head())
print("\nКестенің жалпы сипаттамасы:")
print(df.info())

#task 4
print("\n--- task 4: Сүзгіленген мәліметтер ---")
mean_val = df['col_2'].mean()
filtered_df = df[df['col_2'] > mean_val]
print(f"Орташа мән ({mean_val:.2f}) жоғары жолдар саны:")
print(len(filtered_df))
print("\nСүзгіленген кестенің алғашқы 3 жолы:")
print(filtered_df.head(3))

#task 5
print("\n--- task 5: Категориялар бойынша топтастыру ---")
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

res_5 = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()
res_5.rename(columns={'col_7': 'category'}, inplace=True)
print(res_5.head())


#task 6
print("\n--- Задача 6: Статистический отчет.  ---")
cols_10 = [f'col_{i}' for i in range(2, 12)]
stats_data = []
for c in cols_10:
    numeric_col = pd.to_numeric(df[c], errors='coerce')
    stats_data.append({
        'column': c,
        'mean': numeric_col.mean(),
        'median': numeric_col.median(),
        'std': numeric_col.std()
    })
res_6 = pd.DataFrame(stats_data)
print(res_6)