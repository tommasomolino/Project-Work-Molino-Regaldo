from pprint import pprint

from .dns_lookup import DNSLookup
from .port_scanner import PortScanner


def test_dns_lookup() -> None:
    domain = input("Inserisci il dominio da risolvere: ").strip()

    dns_lookup = DNSLookup("DNSLookup")
    report = dns_lookup.execute(domain)

    print("\n--- RISULTATO DNS LOOKUP ---")
    pprint(report)


def test_port_scanner() -> None:
    target = input("Inserisci IP o hostname da scansionare: ").strip()

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


def main() -> None:
    while True:
        print("\n=== NETWORK TOOLKIT ===")
        print("1. DNS Lookup")
        print("2. Port Scanner")
        print("0. Esci")

        choice = input("Seleziona uno strumento: ").strip()

        try:
            if choice == "1":
                test_dns_lookup()

            elif choice == "2":
                test_port_scanner()

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