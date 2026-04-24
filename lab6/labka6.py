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

#task 8
numeric_cols_fix = ['col_2', 'col_3', 'col_5', 'col_6', 'col_8', 'col_9', 'col_11', 'col_12', 'col_14', 'col_15']
correlation_matrix = df[numeric_cols_fix].corr()
print("\n#task 8(Корреляциялық матрица):")
print(correlation_matrix)

#task 9
import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
plt.hist(df['col_2'], bins=50, color='skyblue', edgecolor='black')
plt.title('Бағалардың үлестірімі')
plt.xlabel('Баға')
plt.ylabel('Тауарлар саны')
plt.grid(True)
plt.savefig('price_distribution_task9.png')

#10
plt.figure(figsize=(10, 6))
sns.regplot(x='col_2', y='col_3', data=df,
            scatter_kws={'alpha':0.5, 'color':'blue'},
            line_kws={'color':'red'})
plt.title('Баға мен мөлшер арасындағы байланыс (Регрессия)')
plt.xlabel('Баға (col_2)')
plt.ylabel('Мөлшер (col_3)')
plt.grid(True)
plt.savefig('price_vs_quantity_task10.png')

#task 11
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')

plt.figure(figsize=(12, 6))
sns.boxplot(x='col_1', y='col_2', data=df, hue='col_1', palette='Set3', legend=False)

plt.title('Категориялар бойынша бағалардың үлестірімі')
plt.xlabel('Категория (col_1)')
plt.ylabel('Баға (col_2)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('price_boxplot_task11.png')
plt.show()

#task 12
cols_12 = ['col_2', 'col_3', 'col_5', 'col_6', 'col_7']

sns.pairplot(df[cols_12].head(500), hue='col_7', palette='viridis')
plt.savefig('pairplot_task12.png')
plt.show()

#task 13
numeric_cols_13 = ['col_2', 'col_3', 'col_5', 'col_6', 'col_8', 'col_9', 'col_11']

plt.figure(figsize=(10, 8))
correlation_matrix = df[numeric_cols_13].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Корреляциялық матрицаның жылу картасы')
plt.savefig('heatmap_task13.png')
plt.show()

#task 14
price_limit = df['col_2'].mean() + 3 * df['col_2'].std()
stock_limit = df['col_3'].mean() + 3 * df['col_3'].std()

extreme_items = df[(df['col_2'] > price_limit) | (df['col_3'] > stock_limit)]
print("\n#task 14 (Экстремалды тауарлар саны):")
print(len(extreme_items))