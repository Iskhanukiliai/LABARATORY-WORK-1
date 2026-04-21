import pandas as pd
import numpy as np

#task 1
class DataPipeline:
    def __init__(self, url):
        self.url = url
        self.df = None
    def load_data(self):
        file_id = self.url.split('/')[-2]
        export_url = f'https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx'

        try:
            self.df = pd.read_excel(export_url)

            print("---task 1: Жүктеу және алғашқы тексеру---")
            print(f"DataFrame өлшемі: {self.df.shape}")
            print("\nДеректер типтері:")
            print(self.df.dtypes)
            print("\nБос орындар:")
            print(self.df.isnull().sum())
            print("\nАлғашқы 5 жол:")
            print(self.df.head())
        except Exception as e:
            print(f"Жүктеу кезіндегі қате: {e}.Файлдың қолжетімділігін тексеріңіз")


if self.df is None:
    return

print("\n--- 2-тапсырма: Типтерді келтіру және бос орындарды толтыру---")
for col in self.df.columns:
    converted_col = pd.to_numeric(self.df[col], errors='coerce')
    if not converted_col.isnull().all():
        self.df[col] = converted_col.astype(float)
        mean_value = self.df[col].mean()
        self.df[col] = self.df[col].fillna(mean_value)

        print(f"'{col}' бағаны өңделді. Толтыруға арналған орташа мән: {mean_value:.2f}")

numeric_cols = self.df.select_dtypes(include=[np.number]).columns
remaining_nas = self.df[numeric_cols].isnull().sum().sum()

print(f"\nСандық бағандардағы қалған бос орындар саны: {remaining_nas}")
print("\nЖаңартылған деректер типтері:")
print(self.df.dtypes)

if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/1DWsGw8RNg5k53zhf1-r_G5tf9shJpKNW/edit?usp=sharing"

    pipeline = DataPipeline(url)
    pipeline.load_data()
    pipeline.process_numeric_data()