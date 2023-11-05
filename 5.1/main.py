import pandas as pd

cinema_sessions = "cinema_sessions.csv"
titanic_with_labels = "titanic_with_labels.csv"
df1 = pd.read_csv(cinema_sessions)
df2 = pd.read_csv(titanic_with_labels)
print(df2)