import os
from process_spotify_data import process_file
from load_to_mysql import load_to_db
from generate_charts import generate_charts


def main():
    selected_file = None
    processed_file = None

    while True:
        print("\n=== Spotify Analytics Console ===")
        print(f"Aktualny plik: {selected_file if selected_file else 'nie wybrano'}")
        print()
        print("1 - Wybierz plik CSV")
        print("2 - Przetworzyć plik CSV")
        print("3 - Prześlij do MySQL")
        print("4 - Wykreślić wykresy")
        print("5 - Wykonaj cały proces")
        print("0 - Exit")

        choice = input("Wpisz numer: ").strip()

        # Exit
        if choice == "0":
            print("Wyjście z programu.")
            break

        # Wybór pliku
        elif choice == "1":
            file_path = input("Wprowadź ścieżkę do pliku CSV: ").strip()

            if os.path.exists(file_path):
                selected_file = file_path
                print("Plik został wybrany.")
            else:
                print("Nie znaleziono pliku.")

        # Przetwarzanie plików CSV
        elif choice == "2":
            if not selected_file:
                print("Najpierw wybierz plik CSV.")
                continue

            processed_file = process_file(selected_file)

        # Wgrywanie danych do MySQL
        elif choice == "3":
            if processed_file:
                load_to_db(processed_file)
            elif selected_file:
                load_to_db(selected_file)
            else:
                print("Najpierw wybierz plik.")

        # Generowanie wykresów
        elif choice == "4":
            if processed_file:
                generate_charts(processed_file)
            elif selected_file:
                generate_charts(selected_file)
            else:
                print("Najpierw wybierz plik.")

        # Pełny proces
        elif choice == "5":
            if not selected_file:
                print("Najpierw wybierz plik CSV.")
                continue

            processed_file = process_file(selected_file)
            load_to_db(processed_file)
            generate_charts(processed_file)

        else:
            print("Zły wybór.")


if __name__ == "__main__":
    main()