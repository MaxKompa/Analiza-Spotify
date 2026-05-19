import pandas as pd
import os

def process_file(input_path):
    try:
        df = pd.read_csv(input_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding="latin1")
    
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    popularity_column = None

    possible_names = [
        "popularity",
        "track_popularity",
        "score",
        "rating"
    ]

    for col in df.columns:
        if col.lower() in possible_names:
            popularity_column = col
            break

    if popularity_column is None:
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

        for col in numeric_cols:
            if df[col].min() >= 0 and df[col].max() <= 100:
                popularity_column = col
                break

    if popularity_column:
        df['category'] = pd.cut(
            df[popularity_column],
            bins=[0, 40, 70, 100],
            labels=['Low', 'Medium', 'High']
        )
        print(f"Wykorzystano kolumnę: {popularity_column}")
    else:
        print("Nie znaleziono odpowiedniej kolumny, pominięto kategoryzację")

    os.makedirs("../data/processed", exist_ok=True)

    output_path = "../data/processed/clean_data.csv"
    df.to_csv(output_path, index=False)

    print("Przetwarzanie zakończone:", output_path)

    return output_path