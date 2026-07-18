from project.tool import Tool
import pytest

def test_execute() -> None:
    tool = Tool("Comando di prova per test")
    result = tool.execute("192.168.1.1")

    assert result == {
        "tool" : "Comando di prova per test",
        "target" : "192.168.1.1",
        "esito" : None,
        "risultato" : None
    } 

def test_error_execute() -> None:
    tool = Tool("Commando di prova per test")

    with pytest.raises(ValueError):
        tool.execute("")