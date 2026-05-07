import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:maxk62242@localhost/spotify_analytics"
)

df = pd.read_csv(
    "../data/processed/clean_spotify_tracks.csv"
)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df.to_sql(
    "tracks",
    con=engine,
    if_exists="replace",
    index=False
)

print("Данные загружены в MySQL!")