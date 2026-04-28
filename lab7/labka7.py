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

#task 8
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

model_simple = LinearRegression()
model_simple.fit(X_train[['col_3']], y_train)
y_pred_simple = model_simple.predict(X_test[['col_3']])
print("MAE:", mean_absolute_error(y_test, y_pred_simple))
print("MSE:", mean_squared_error(y_test, y_pred_simple))

#task 9
model_full = LinearRegression()
model_full.fit(X_train, y_train)

y_pred_full = model_full.predict(X_test)
print("Жақсартылған MAE:", mean_absolute_error(y_test, y_pred_full))

#task 10
plt.scatter(y_test, y_pred_full)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Нақты баға')
plt.ylabel('Болжалды баға')
plt.title('Нақты және болжалды бағаларды салыстыру')
plt.show()

#task 11
from sklearn.preprocessing import StandardScaler
cols_to_scale = ['col_3', 'total_value', 'double_stock', 'log_price']
scaler = StandardScaler()
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled[cols_to_scale] = scaler.fit_transform(X_train[cols_to_scale])
X_test_scaled[cols_to_scale] = scaler.transform(X_test[cols_to_scale])

#task 12
from sklearn.tree import DecisionTreeRegressor

dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
importance = pd.Series(dt_model.feature_importances_, index=X_train.columns)
importance.nlargest(10).plot(kind='barh')
plt.title('Белгілердің маңыздылығы')
plt.show()