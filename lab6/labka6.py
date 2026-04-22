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

            def process_numeric_data(self):
                if self.df is None:
                    return
                print("\n---task 2: Типтерді келтіру және бос орындарды толтыру---")

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

import matplotlib.pyplot as plt
import seaborn as sns


#task 3
class CatalogAnalyzer:
    def __init__(self, df):
        self.df = df
        sns.set_theme(style="whitegrid")
    def create_features(self):
        print("\n---task 3: Жаңа көрсеткіштерді жасау ---")
        self.df['total_value'] = self.df['col_2'] * self.df['col_3']
        self.df['double_stock'] = self.df['col_4'] * 2
        self.df['log_price'] = np.log(self.df['col_2'].replace(0, np.nan))
        print("total_value, double_stock, log_price бағандары сәтті қосылды.")


    # task 4
    def filter_expensive_electronics(self):
        print("\n---task 4: Қымбат тауарларды фильтрациялау (Electronics) ---")
        electronics_expensive = self.df[
            (self.df['col_2'] > 500) & (self.df['col_7'] == "Electronics")
            ].copy()
        print(f"Тауарлар табылды: {len(electronics_expensive)}")
        print(electronics_expensive.head())
        return electronics_expensive

#task 5
    def group_by_category(self):
        print("\n--- task 5: Санаттар бойынша топтастыру ---")
        summary = self.df.groupby('col_7').agg(
            mean_price=('col_2', 'mean'),
            max_price=('col_2', 'max'),
            total_quantity=('col_3', 'sum')
        ).reset_index()
        summary.columns = ['category', 'mean_price', 'max_price', 'total_quantity']
        print(summary)
        return summary

# task 6
def get_column_stats(self):
        print("\n--- task 6: Жиынтық статистика (col_2-col_11) ---")
        cols = [f'col_{i}' for i in range(2, 12)]
        stats = []
        for col in cols:
            stats.append({
                'column': col,
                'mean': self.df[col].mean(),
                'median': self.df[col].median(),
                'std': self.df[col].std()
            })
        stats_df = pd.DataFrame(stats)
        print(stats_df)
        return stats_df

#task 7
    def detect_anomalies(self):
        print("\n--- task 7: Баға аномалияларын анықтау  ---")
        mean_p = self.df['col_2'].mean()
        std_p = self.df['col_2'].std()
        threshold = mean_p + 3 * std_p
        anomalies = self.df[self.df['col_2'] > threshold].copy()
        print(f"Анықталған аномалиялар: {len(anomalies)}")
        print(anomalies.head())
        return anomalies


if __name__ == "__main__":
    url = "https://docs.google.com/spreadsheets/d/1DWsGw8RNg5k53zhf1-r_G5tf9shJpKNW/edit?usp=sharing"
    pipeline = DataPipeline(url)
    pipeline.load_data()
    pipeline.process_numeric_data()
