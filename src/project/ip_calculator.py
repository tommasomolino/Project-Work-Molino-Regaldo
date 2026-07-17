from .tool import Tool
import ipaddress 
import math

class IpCalculator(Tool):
    def __init__(self, tool_name: str):
        super().__init__(tool_name)

    def execute(self, target: str, host_requirements: list[int]):
        report = super().execute(target)

        try:
            network = ipaddress.ip_network(target, strict=False)
            cursor = network.network_address

            sorted_hosts = sorted(host_requirements, reverse=True)
            subnet_calculated = []

            for host in host_requirements:
                if host <= 0:
                    raise ValueError(f"Specificare il numero di host richiesti. La quantità di host:{host_requirements} non può essere negativa")

            for host in sorted_hosts:
                bit_host = math.ceil(math.log2(host + 2))
                new_prefix = 32 - bit_host
                subnet = ipaddress.ip_network((int(cursor), new_prefix), strict=False)
        
                if not subnet.subnet_of(network):
                    report["esito"] = "Calcolo fallito"
                    report["risultato"] = f"Spazio di indirizzi esaurito: non c'è posto per {host} host"
                    return report
                
                subnet_calculated.append({
                    "host richiesti": host,
                    "rete": str(subnet),
                    "broadcast": str(subnet.broadcast_address)
                })

                cursor = subnet.broadcast_address + 1

        except ValueError as e:
            report["esito"] = "Calcolo fallito"
            report["risultato"] = f"L'indirizzo di rete inserito non è valido: {e}"
            return report
            
        else:            
            report["esito"] = "Calcolo eseguito con successo"
            report["risultato"] = subnet_calculated
            return report
