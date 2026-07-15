from .tool import Tool
import dns.resolver

class DNSLookup(Tool):
    def __init__(self, tool_name):
        super().__init__(tool_name)

    def execute(self, target:str) -> dict:
        report = super().execute(target)

        try:
            answers = dns.resolver.resolve(target, "A")

            ip_addresses = []
            for answer in answers:
                ip_addresses.append(answer.to_text())

            report["esito"] = "Dominio risolto con successo"
            report["risultato"] = ip_addresses

        except dns.resolver.NXDOMAIN as e:
            report["esito"] = "Dominio inesistente"
            report["risultato"] = f"Il dominio scelto ha restituito l'errore: {e}"

        return report