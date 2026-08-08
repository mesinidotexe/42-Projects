from hub import Hub

class Graph():
    
    def __init__(self, hubs: dict[str, Hub], connections: list[dict]):
        self.hubs = hubs
        self.connections = connections
        
    def build(self):
        links = {}
        
        for name in self.hubs:
            links[name] = {}
            
        for link in self.connections:   # each connection dict
            a = link['connection1']
            b = link['connection2']
            cap = link['max_link_capacity']
            links[a][b] = cap
            links[b][a] = cap
            
        return {'hubs': self.hubs,
                'links': links
            }