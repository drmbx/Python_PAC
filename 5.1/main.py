import pandas as pd
import numpy as np

titanic_with_labels = "titanic_with_labels.csv"
df = pd.read_csv(titanic_with_labels, delimiter=' ', index_col=0)
df = df[(df['sex'] == 'ж') | (df['sex'] == 'м') | (df['sex'] == 'M') | (df['sex'] == 'Ж') | (df['sex'] == 'Мужчина')]
df.reset_index(inplace=True, drop=True)
df['sex'].replace({'ж': 1, 'м': 0, 'M': 0, 'Ж': 1, 'Мужчина': 0}, inplace=True)
df['row_number'].fillna(df['row_number'].max(), inplace=True)
df.loc[(df['liters_drunk'] < 0) | (df['liters_drunk'] > 20.0), 'liters_drunk'] = np.nan
df['liters_drunk'].fillna(df['liters_drunk'].mean(), inplace=True)
print(df)
