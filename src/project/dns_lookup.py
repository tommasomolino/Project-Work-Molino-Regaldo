from .tool import Tool
import dns.resolver
import dns.exception

class DNSLookup(Tool):
    def __init__(self, tool_name, record_types):
        super().__init__(tool_name)
        self.record_types = record_types

    def execute(self, target:str) -> dict:
        report = super().execute(target)

        dns_results = {}
        record_status = {}

        for record_type in self.record_types:

            try:
                answers = dns.resolver.resolve(target, record_type)

                record_values = []
                for answer in answers:
                    record_values.append(answer.to_text())

                dns_results[record_type] = record_values
                record_status[record_type] = "Risolto con successo"

            except dns.resolver.NXDOMAIN as e:
                report["esito"] = "Dominio inesistente"
                report["risultato"] = f"Il dominio scelto ha restituito l'errore: {e}"
                return report

            except dns.resolver.NoAnswer as e:
                record_status[record_type] = f"Il record non è presente: {e}"
                dns_results[record_type] = []

            except dns.exception.Timeout as e:
                record_status[record_type] = f"Timeout durante la risoluzione: {e}"
                dns_results[record_type] = []

            except dns.resolver.NoNameservers as e:
                record_status[record_type] = f"Nessun server DNS disponibile: {e}"
                dns_results[record_type] = []

        report["esito"] = record_status
        report["risultato"] = dns_results

        return report
