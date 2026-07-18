import pytest
from project.port_scanner import PortScanner

def test_ErrorPort_init():
    with pytest.raises(ValueError):
        PortScanner(tool_name="Scanner di prova", port_range=range(-1, 1), timeout=1)

def test_ErrorTimeout_init():
    with pytest.raises(ValueError):
        PortScanner(tool_name="Scanner di prova", port_range=(1, 2), timeout=0)
        