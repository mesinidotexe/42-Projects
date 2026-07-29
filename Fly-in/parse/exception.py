class NegativeDronesErroor(Exception):
    """Error when the number of drones is negative"""
    pass

class NotIntError(Exception):
    """Error when nb_drones is not an integer"""
    pass

class ZoneError(Exception):
    """Error when zone name is not in the standard"""
    pass
