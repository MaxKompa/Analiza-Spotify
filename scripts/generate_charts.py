import pandas as pd
import matplotlib.pyplot as plt
import os


def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def find_column(df, candidates):
    for col in df.columns:
        if col in candidates:
            return col
    return None

def generate_charts(file_path, output_dir="dashboard"):
    df = pd.read_csv(file_path, encoding="utf-8", engine="python")

    if df.shape[1] == 1:
        df = pd.read_csv(file_path, encoding="latin1", engine="python")

    df = normalize_columns(df)

    df = df.loc[:, ~df.columns.str.contains("^unnamed")]
    df.dropna(inplace=True)

    os.makedirs(output_dir, exist_ok=True)

    print("\nDostępne kolumny:", list(df.columns))

    genre_col = find_column(df, ["genre", "top_genre", "track_genre", "music_genre"])
    pop_col = find_column(df, ["pop", "popularity", "score", "rating"])
    duration_col = find_column(df, ["dur", "duration", "duration_ms", "length"])

    energy_col = find_column(df, ["nrgy", "energy"])
    dance_col = find_column(df, ["dnce", "danceability"])
    valence_col = find_column(df, ["val", "valence"])

    if genre_col:
        plt.figure(figsize=(10, 6))
        df[genre_col].value_counts().head(10).plot(kind="bar")
        plt.title("Top Genres")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{output_dir}/genres.png")
        plt.close()
    else:
        print("Nie znaleziono kolumny gatunków — pomijam")

    if pop_col:
        plt.figure(figsize=(10, 6))
        df[pop_col].hist(bins=20)
        plt.title("Popularity distribution")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/popularity.png")
        plt.close()
    else:
        print("Nie znaleziono popularity — pomijam")

    if duration_col:
        plt.figure(figsize=(10, 6))
        df[duration_col].hist(bins=30)
        plt.title("Duration distribution")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/duration.png")
        plt.close()
    else:
        print("Nie znaleziono duration — pomijam")

    for col, name in [
        (energy_col, "energy"),
        (dance_col, "danceability"),
        (valence_col, "valence"),
    ]:
        if col:
            plt.figure(figsize=(10, 6))
            df[col].hist(bins=20)
            plt.title(f"{name} distribution")
            plt.tight_layout()
            plt.savefig(f"{output_dir}/{name}.png")
            plt.close()


    print(f"\nWszystkie wykresy zapisane w: {output_dir}/")