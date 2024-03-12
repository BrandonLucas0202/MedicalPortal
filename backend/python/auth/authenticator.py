"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A token authentication system used to track and 
authenticate account sessions.

TODO Session tokens need switched to a proper cache with TTL (Time to Live) so they expire
"""
from database.sqlconnection import SQLConnection


class Authenticator():
    """
    A token authentication system used to track and 
    authenticate account sessions.
    """

    def __init__(self, database: SQLConnection) -> None:
        self.database = database
        self.sessions = {
            "test": None
        }


    def verifyToken(self, token: str) -> bool:
        """
        Verifies that the token is a valid session
        """
        return token in self.sessions.keys()
    
    
