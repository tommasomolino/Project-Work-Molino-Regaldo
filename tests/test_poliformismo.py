from project.tool import Tool
from project.dns_lookup import DNSLookup
from project.port_scanner import PortScanner
from project.ip_calculator import IpCalculator

def test_SubclassesAreTool():
    assert isinstance(IpCalculator("Calcolatore"), Tool)
    assert isinstance(PortScanner("Scanner", port_range=(20, 100), timeout=1), Tool)
    assert isinstance(DNSLookup("DNS", record_types=["A"]), Tool)

def test_UniformReport():
    tools = [
        (IpCalculator("Calcolatore"), ("192.168.1.0/24", [10])),
        (PortScanner("Scanner", port_range=(40000, 45000), timeout=1), ("127.0.0.1", False)),
        (DNSLookup("DNS", record_types=["A"]), ("example.com",))
    ]

    for tool, args in tools:
        report = tool.execute(*args)
        assert set(report.keys()) == {"tool", "target", "esito", "risultato"}
