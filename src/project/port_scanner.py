from .tool import Tool
import socket

class PortScanner(Tool):
    def __init__(self, tool_name: str, port_range: int, timeout: int):
        super().__init__(tool_name)
        self.port_range = port_range
        self.timeout = timeout

        for port in port_range:
            if port < 0 or port > 65535:
                raise ValueError(f"Il valore della porta {port} non è valido")
        if timeout <= 0:
            raise ValueError(f"Il timeout {timeout} non è valido")
        
    def execute(self, target, verbose):
        report = super().execute(target)
        self.verbose = verbose

        port_opened = []
        port_closed = []
        port_timeout = []

        for port in self.port_range:
            try:
                with socket.socket() as s:
                    s.settimeout(self.timeout)
                    s.connect((target, port))

            except ConnectionRefusedError as e:
                port_closed.append(port)
                if self.verbose:
                    print(f"Connessione rifiutata sulla porta {port}: {e}")

                
            except TimeoutError as e:
                port_timeout.append(port)
                if self.verbose:
                    print(f"Timeout sulla porta {port}: {e}")
            
            except OSError as e:
                port_closed.append(port)
                if self.verbose:
                    print(f"Errore di rete sulla porta {port}: {e}")
                
            else:
                port_opened.append(port)
                if self.verbose:
                    print(f"Porta {port} aperta")
        
        report["esito"] = "Scansione effettuata"
        report["risultato"] = (
            f"Le porte aperte sono:{port_opened}"
            f"Le porte chiuse sono:{port_closed}"
            f"Le porte andate in timeout sono:{port_timeout}"
        )
        return report  






    
