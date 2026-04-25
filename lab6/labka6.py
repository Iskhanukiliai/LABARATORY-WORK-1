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
if 'total_value' not in df.columns:
    df['total_value'] = df['col_2'] * df['col_3']
if 'double_stock' not in df.columns:
    df['double_stock'] = df['col_3'] * 2
if 'log_price' not in df.columns:
    import numpy as np
    df['log_price'] = np.log1p(df['col_2'])

#task 15
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

if 'log_price' not in df.columns:
    df['log_price'] = np.log1p(df['col_2'])
category_summary = df.groupby('col_7').agg({
    'col_1': 'count',
    'col_2': 'mean',
    'col_3': 'sum',
    'log_price': 'mean'
})
category_summary.columns = ['count', 'mean_price', 'total_quantity', 'mean_log_price']
print("#task 15")
print(category_summary.head())

#task 16
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')

idx = df.groupby('col_7')['col_2'].idxmax()
most_expensive = df.loc[idx, ['col_1', 'col_2', 'col_7']]
print("task 16 нәтижесі:")
print(most_expensive)

# task 17
df['total_value'] = df['col_2'] * df['col_3']
top_10_expensive = df.sort_values(by='total_value', ascending=False).head(10)
result_17 = top_10_expensive[['col_1', 'col_2', 'col_3', 'total_value']]
print("\n#task 17 нәтижесі:")
print(result_17)

# task 18
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
price_dist = df['price_range'].value_counts().reindex(labels).reset_index()
price_dist.columns = ['price_range', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=price_dist, x='price_range', y='count', hue='price_range', palette='viridis', legend=False)
plt.title('Баға диапазоны бойынша тауарлардың үлестірімі')
plt.show()

# task 19
cat_value = df.groupby('col_7')['total_value'].sum().reset_index()
cat_value.columns = ['category', 'total_stock_value']
max_cat = cat_value.loc[cat_value['total_stock_value'].idxmax()]
print(f"\nЕң көп капиталды категория: {max_cat['category']}")

plt.figure(figsize=(12, 6))
sns.barplot(data=cat_value, x='category', y='total_stock_value', hue='category', palette='magma', legend=False)
plt.title('Категориялар бойынша жалпы құны')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#task 20  and 36
cat_stats = df.groupby('col_7').agg({
    'col_2': well,
    'col_3': 'mean'
}).reset_index()
cat_stats.columns = ['category', 'mean_price', 'mean_quantity']
plt.figure(figsize=(10, 6))
sns.scatterplot(data=cat_stats, x='mean_price', y='mean_quantity', hue='category', s=200)
plt.title('Категориялар бойынша орташа баға мен орташа қордың байланысы')
plt.xlabel('Орташа баға')
plt.ylabel('Орташа қор саны')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('category_scatter_task20.png')
plt.show()
print("\n20 task 36:")
print(cat_stats)

#task 21 and 37
price_variation = df.groupby('col_7')['col_2'].std().reset_index()
price_variation.columns = ['category', 'std_price']
plt.figure(figsize=(10, 8))
sns.barplot(data=price_variation.sort_values('std_price', ascending=False),
            x='std_price', y='category', hue='category', palette='magma', legend=False)
plt.title('Категориялар бойынша бағаның ауытқуы (Standard Deviation)')
plt.xlabel('Стандартты ауытқу')
plt.ylabel('Категория')
plt.savefig('price_variation_task21.png')
plt.show()

#task 22 and 38
out_of_stock = df[df['col_3'] == 0]
result_22 = out_of_stock[['col_1', 'col_7', 'col_2']].head(10)
print("\n22 тапсырма нәтижесі (Қоймада жоқ тауарлар):")
print(result_22)

#task 23 and 39
top_categories = df['col_7'].value_counts().head(5).reset_index()
top_categories.columns = ['category', 'count']
plt.figure(figsize=(10, 6))
sns.barplot(data=top_categories, x='category', y='count', hue='category', palette='coolwarm', legend=False)
plt.title('Тауар саны бойынша үздік 5 категория')
plt.xlabel('Категория')
plt.ylabel('Тауар саны')
plt.savefig('top5_categories_task23.png')
plt.show()
print("\ntask 23 тапсырма нәтижесі:")
print(top_categories)

#task 24 and 40
top_stock = df.sort_values(by='col_3', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_stock, x='col_3', y='col_1', hue='col_1', palette='viridis', legend=False)
plt.title('Қоймадағы тауар саны бойынша үздік 10 тауар')
plt.xlabel('Саны (дана)')
plt.ylabel('Тауар атауы')
plt.savefig('top_stock_task24.png')
plt.show()
print("\ntask 24 нәтижесі:\n", top_stock[['col_1', 'col_3']])
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']

#task 25 and 41
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(pd.to_numeric(df['col_2'], errors='coerce'), bins=bins, labels=labels)
h_map = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(h_map, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Категориялар мен баға диапазондарының жылу картасы')
plt.xlabel('Баға диапазоны')
plt.ylabel('Категория')
plt.savefig('heatmap_task25.png')
plt.show()
print("\ntask 25 нәтижесі:\n", h_map.head())

