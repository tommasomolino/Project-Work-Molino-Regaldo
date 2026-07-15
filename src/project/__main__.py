from pprint import pprint

from .dns_lookup import DNSLookup
from .port_scanner import PortScanner
from .report_exporter import export_report


def dns_lookup() -> None:
    domain = input("Inserisci il dominio da risolvere: ").strip()
    if domain == "":
        print("Devi indicare un dominio.")
        return

    allowed_records = ["A", "AAAA", "MX", "TXT"]
    record_input= input(f"Scegli uno o più tipi di record ({allowed_records} oppure ALL): ").strip().upper()

    if record_input == "ALL":
        record_types = list(allowed_records)
    else:
        record_types = []

        for record in record_input.split(","):
            record = record.strip()

            if record == "":
                print("Devi indicare almeno un tipo di record.")
                return

            if record not in allowed_records:
                print(f"Il record {record} non è valido.")
                return

            record_types.append(record)


    dns_lookup = DNSLookup(
        tool_name="DNSLookup",
        record_types=record_types
    )

    report = dns_lookup.execute(domain)

    print("\n--- RISULTATO DNS LOOKUP ---")
    pprint(report)
    export(report)


def port_scanner() -> None:
    target = input("Inserisci IP o hostname da scansionare: ").strip()

    if target == "":
        print("Devi indicare un IP o un hostname.")
        return

    start_port = int(input("Inserisci la porta iniziale: "))
    end_port = int(input("Inserisci la porta finale: "))

    if start_port > end_port:
        print("La porta iniziale non può essere maggiore della porta finale.")
        return

    port_range = range(start_port, end_port + 1)

    scanner = PortScanner(
        tool_name="PortScanner",
        port_range=port_range,
        timeout=1
    )

    report = scanner.execute(target, verbose=True)

    print("\n--- RISULTATO PORT SCANNER ---")
    pprint(report)
    export(report)

def export(report: dict) -> None:
    choice = input(
        "Vuoi esportare il report in un file JSON? s/n: ").strip().lower()

    if choice == "s":
        file_path = input("Inserisci il percorso: ").strip()

        if file_path == "":
            print("Devi indicare un nome o un percorso per il file.")
            return

        if not file_path.lower().endswith(".json"):
            file_path += ".json"

        export_report(report, file_path)

    elif choice == "n":
        return

    else:
        print("Scelta non valida.")

def main() -> None:
    while True:
        print("\n=== NETWORK TOOLKIT ===")
        print("1. DNS Lookup")
        print("2. Port Scanner")
        print("0. Esci")

        choice = input("Seleziona uno strumento: ").strip()

        try:
            if choice == "1":
                dns_lookup()

            elif choice == "2":
                port_scanner()

            elif choice == "0":
                print("Chiusura del Network Toolkit.")
                break

            else:
                print("Scelta non valida.")

        except ValueError as error:
            print(f"Errore nei dati inseriti: {error}")

        except Exception as error:
            print(f"Errore durante l'esecuzione: {error}")


if __name__ == "__main__":
    main()