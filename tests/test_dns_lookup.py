import pytest
from project.dns_lookup import DNSLookup

def test_execute():
    tool = DNSLookup("Comando di prova", record_types=["A"])
    result = tool.execute("example.com")

    assert result["esito"] == {"A": "Risolto con successo"}
    assert len(result["risultato"]["A"]) > 0


def test_ErrorDomain_execute():
    tool = DNSLookup("Comando di prova", record_types=["A"])
    result = tool.execute("Dominio completamente inventato")

    assert result["esito"] == "Dominio inesistente"

