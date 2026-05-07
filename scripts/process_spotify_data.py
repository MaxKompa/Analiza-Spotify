import pandas as pd

df = pd.read_csv("../data/raw/dataset.csv")

print(df.head())

print(df.info())

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df['popularity_category'] = pd.cut(
    df['popularity'],
    bins=[0, 40, 70, 100],
    labels=['Low', 'Medium', 'High']
)

df.to_csv(
    "../data/processed/clean_spotify_tracks.csv",
    index=False
)

print("Обработка завершена!")