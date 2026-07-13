from .tool import Tool

class PortScanner(Tool):
    def __init__(self, tool_name, port_range, timeout = 1):
        super().__init__(tool_name)
        self.port_range = port_range
        self.timeout = timeout

