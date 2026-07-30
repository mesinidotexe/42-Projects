# General
class NotIntError(Exception):
    """Error when a value is not an integer"""
    pass


class NegativeError(Exception):
    """Error when a number is negative or below the allowed minimum"""
    pass


class NotIntPositionError(Exception):
    """Error when position parameters are not integers"""
    pass


class OpenBracketError(Exception):
    """Error when metadata brackets are missing or unclosed"""
    pass


class InvalidSyntaxError(Exception):
    """Error when a line or metadata token has invalid syntax"""
    pass


# Start / End hub
class NegativePositionError(Exception):
    """Error when start/end hub position is negative"""
    pass


# Hub
class DashInNameError(Exception):
    """Error when a hub name contains '-'"""
    pass


class NegativeHubPositionError(Exception):
    """Error when a hub position is negative"""
    pass


class ZoneError(Exception):
    """Error when a zone name is not in the standards"""
    pass


class DoubledNameError(Exception):
    """Error when there is 2 zones with the same name"""
    pass