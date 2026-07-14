from .tool import Tool
import socket

class PortScanner(Tool):
    def __init__(self, tool_name, port_range, timeout = 1):
        super().__init__(tool_name)
        self.port_range = port_range
        self.timeout = timeout

    def execute(self, target):
        report = super().execute(target)

        try: 
            with socket.socket() as s:
                s.settimeout(self.timeout) 
                s.connect((target, 80))  

        except ConnectionRefusedError as e:
            print(f"La connessione non è andata a buon fine:{e}")
            report["esito"] = "Scansione avvenuta, nessuna porta aperta"
            report["risultato"] = "Porta 80 chiusa"
            return report
            
        
        except socket.timeout as e:
            print(f"La scansione ci ha messo troppo tempo:{e}")
            report["esito"] = "Scansione bloccata, richiesto troppo tempo"
            report["risultato"] = "Porta 80 irraggiungibile"
            return report
        
        else:
            report["esito"] = "Scansione avvenuta con successo"
            report["risultato"] = "Porta 80 aperta"
            return report






    
