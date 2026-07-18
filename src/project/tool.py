class Tool:
    def __init__(self, tool_name: str):
        self.tool_name = tool_name

    def execute(self, target: str):
        if not target:
            raise ValueError("Necessario specificare il target")
        
        report = {
            "tool" : self.tool_name,
            "target" : target,
            "esito" : None,
            "risultato" : None
        }
        return report

