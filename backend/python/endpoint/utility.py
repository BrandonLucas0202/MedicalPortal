"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

An endpoint utility used for endpoint modules.
"""
from flask import request


def getParameter(name: str, default = None, type = str, verifier = None):
    """
    Trys retrieving a passed request argument and verifies
    the argument with the provided function.
    """
    param = request.args.get(name, default, type)

    if param == None or (not verifier == None and not verifier(param)):
        raise InvalidParameterException()
    
    return param



class InvalidParameterException(Exception):
    """Exception thrown if invalid parameter is provided."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        