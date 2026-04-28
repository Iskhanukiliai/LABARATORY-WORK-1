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

#task 3
df['total_value'] = df['col_2'] * df['col_3']
df['log_price'] = np.log(df['col_2'])
df['double_stock'] = df['col_3'] * 2

#task 4
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['col_2'], kde=True)
plt.title('Бағаның таралуы')
plt.show()

sns.scatterplot(data=df, x='col_3', y='col_2')
plt.title('Баға мен Саны арасындағы байланыс')
plt.show()

sns.boxplot(x='col_7', y='col_2', data=df)
plt.xticks(rotation=45)
plt.title('Санаттар бойынша бағалар')
plt.show()

#task 5
mean = df['col_2'].mean()
std = df['col_2'].std()

anomalies = df[(df['col_2'] > mean + 3*std) | (df['col_2'] < mean - 3*std)]

df = df.drop(anomalies.index)


#task 6
df = pd.get_dummies(df, columns=['col_7'], drop_first=True)

#task 7
from sklearn.model_selection import train_test_split
y = df['col_2']
X = df.select_dtypes(include=[np.number]).drop(columns=['col_2'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
