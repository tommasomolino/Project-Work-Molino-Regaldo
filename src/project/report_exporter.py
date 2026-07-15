import json

def export_report(report: dict, file_path: str) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        print(f"Report esportato correttamente in: {file_path}")

    except PermissionError as e:

        print(f"Permesso negato durante il salvataggio: {e}")

    except FileNotFoundError as e:

        print(f"Il percorso indicato non esiste: {e}")

    except IsADirectoryError as e:

        print(f"Il percorso indicato è una cartella, non un file: {e}")

    except TypeError as e:

        print(f"Il report contiene dati non serializzabili in JSON: {e}")

    except OSError as e:

        print(f"Errore del filesystem durante il salvataggio: {e}")