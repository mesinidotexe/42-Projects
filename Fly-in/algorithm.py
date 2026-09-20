from hub import Hub
from collections import deque

class Simulation():
    
    @classmethod
    def bfs(cls, mapa: dict[str, Hub], start: Hub, end: Hub):
        for hub in mapa['hubs'].values():
            hub.visited = False
        
        mapa['hubs'][start].visited = True
        queue = deque([start])
        parent = {start: None}
        i = 1
        while queue:
            i += 1
            current = queue.popleft()
            if current == end:
                break
            
            for neighbor in mapa['links'][current]:
                point = mapa['hubs'][neighbor]
                if point.visited or not point.allowed:
                    continue
                point.visited = True
                parent[neighbor] = current
                queue.append(neighbor)
                
        if end not in parent:
            return None
        
        path: list[str] = []
        node: str | None = end
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        
        return path