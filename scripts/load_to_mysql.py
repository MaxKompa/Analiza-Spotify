import pandas as pd
from sqlalchemy import create_engine

def load_to_db(file_path):
    engine = create_engine(
        "mysql+mysqlconnector://root:maxk62242@localhost/spotify_analytics"
    )

    df = pd.read_csv(file_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df.to_sql(
        "tracks",
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print("Dane zostały załadowane do bazy danych MySQL!")