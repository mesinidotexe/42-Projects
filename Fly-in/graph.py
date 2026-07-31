from hub import Hub

class Graph():
    
    def __init__(self, hubs: dict[str, Hub], connections):
        self.hubs = hubs
        self.connections = connections
        
    def create(self):
        blueprint = dict[str]