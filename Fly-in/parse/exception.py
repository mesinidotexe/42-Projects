# General
class NotIntPositionError(Exception):
    """Error when position parameters are not int"""
    pass


class NegativeError(Exception):
    """Error when the number is negative"""
    pass


class NotIntError(Exception):
    """Error when there is a non an integer value"""
    pass


class OpenBracketError(Exception):
    """Error when Open bracket"""
    pass


# Start/End hub
class NegativePositionError(Exception):
    """Error when start/end hub value are negative"""
    pass


class InvalidSyntaxError(Exception):
    """Error when Invalid Syntax on start/end hub"""
    pass


class DashInNameError(Exception):
    """Error when there is a '-' in name"""
    pass


class NegativeHubPositionError(Exception):
    """Error when hub position is negative"""
    pass


class ZoneError(Exception):
    """Error when zone name is not in the standard"""
    pass
