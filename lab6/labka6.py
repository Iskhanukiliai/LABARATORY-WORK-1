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
analysis_results = df.groupby('col_1').agg(
    avg_value=('col_2', 'mean'),
    max_value=('col_2', 'max'),
    total_items=('col_3', 'sum')
).reset_index()
analysis_results = analysis_results.rename(columns={'col_1': 'Категория'})
print("\n#5 Тапсырма нәтижесі:")
print(analysis_results)


#task 6
numeric_cols = [f'col_{i}' for i in range(2, 12)]
data_subset = df[numeric_cols].copy()
for column in numeric_cols:
    data_subset[column] = pd.to_numeric(data_subset[column], errors='coerce')
detailed_stats = data_subset.agg(['mean', 'median', 'std']).T
detailed_stats = detailed_stats.reset_index().rename(columns={'index': 'Бағандар'})
print("\n#6 Тапсырма нәтижесі:")
print(detailed_stats)

#task 7
avg_p = df['col_2'].mean()
std_p = df['col_2'].std()
anomalies_data = df[df['col_2'] > (avg_p + 3 * std_p)]
print("\n#task 7 (Аномальды тауарлар):")
print(anomalies_data.head())