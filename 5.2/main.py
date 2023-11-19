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

df['age_kid'] = df['age'].apply(lambda x: 1 if x < 18 else 0)
df['age_adult'] = df['age'].apply(lambda x: 1 if 18 <= x <= 50 else 0)
df['age_elderly'] = df['age'].apply(lambda x: 1 if x > 50 else 0)
df['drink'] = df['drink'].apply(lambda x: 1 if (("beer" in x) | ("пиво" in x)) else 0)
cinema_sessions = "cinema_sessions.csv"
df2 = pd.read_csv(cinema_sessions, delimiter=' ', index_col=0)
df = df.merge(df2, on='check_number')
df['session_start'] = pd.to_datetime(df['session_start'], format='%H:%M:%S.%f').dt.time
df['morning'] = df['session_start'].apply(lambda x: 1 if ((x.hour >= 6) & (x.hour < 12)) else 0)
df['daytime'] = df['session_start'].apply(lambda x: 1 if ((x.hour >= 12) & (x.hour < 18)) else 0)
df['evening'] = df['session_start'].apply(lambda x: 1 if ((x.hour >= 18) & (x.hour < 24)) else 0)
print(df)
