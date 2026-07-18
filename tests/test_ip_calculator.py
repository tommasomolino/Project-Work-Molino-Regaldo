import pytest
from project.ip_calculator import IpCalculator

def test_execute():
    tool = IpCalculator("Calcolatore di prova")
    result = tool.execute("192.168.1.0/24", [100, 50])

    assert result == {
        "tool" : "Calcolatore di prova",
        "target" : "192.168.1.0/24",
        "esito" : "Calcolo eseguito con successo",
        "risultato" :  [
        {"host richiesti": 100, "rete": "192.168.1.0/25", "broadcast": "192.168.1.127"},
        {"host richiesti": 50, "rete": "192.168.1.128/26", "broadcast": "192.168.1.191"}
    ]
    }

def test_ErrorNetwork_execute():
    tool = IpCalculator("Calcolatore di prova")
    result = tool.execute("Non è un indirizzo IP", [10])

    assert result["esito"] == "Calcolo fallito"
    assert result["risultato"].startswith("L'indirizzo di rete inserito non è valido:")

def test_ErrorHost_execute():
    tool = IpCalculator("Calcolatore di prova")
    result = tool.execute("192.168.1.0/24", [-10])

    assert result["esito"] == "Calcolo fallito"
    assert ("Specificare il numero di host richiesti. La quantità di host:[-10] non può essere negativa") in result["risultato"] 

def test_ErrorSubnet_execute():
    tool = IpCalculator("Calcolatore di prova")
    result = tool.execute("192.168.1.0/30", [100])

    assert result["esito"] == "Calcolo fallito"
    assert result["risultato"] == "Spazio di indirizzi esaurito: non c'è posto per 100 host"