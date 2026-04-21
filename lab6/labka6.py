import pandas as pd
import numpy as np

class DataPipeline:
    def __init__(self, url):
        self.url = url
        self.df = None
    def load_data(self):
        file_id = self.url.split('/')[-2]
        export_url = f'https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx'

        try:
            self.df = pd.read_excel(export_url)

            print("--- Задача 1: Загрузка и первичная проверка ---")
            print(f"Форма DataFrame: {self.df.shape}")
            print("\nТипы данных:")
            print(self.df.dtypes)
            print("\nПропуски:")
            print(self.df.isnull().sum())
            print("\nПервые 5 строк:")
            print(self.df.head())
        except Exception as e:
            print(f"Жүктеу кезіндегі қате: {e}.Файлдың қолжетімділігін тексеріңіз")