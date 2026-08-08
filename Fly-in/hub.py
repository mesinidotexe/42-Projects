class Hub:
    
    _ZONE_COST = {
        'normal': 1,
        'priority': 1,
        'restricted': 2,
        'blocked': None,
        }

    @staticmethod
    def get_cost(zone: str) -> int | None:
        return Hub._ZONE_COST.get(zone)
    
    def __init__(self, name: str, position: tuple[int, int], color: str | None=None, zone: str ='normal', max_drones: int=1, role: str='hub'):
        self.name = name
        self.position = position
        self.color = color
        self.zone = zone
        self.max_drones = max_drones
        self.role = role
        self.cost = self.get_cost(self.zone)
        self.allowed = self.cost is not None
        self.priority = self.zone == 'priority'
        self.visited = False