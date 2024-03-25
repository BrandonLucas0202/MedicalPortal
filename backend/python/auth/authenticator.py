"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A token authentication system used to track, manage, and 
authenticate account sessions.

TODO Session tokens need switched to a proper cache with TTL (Time to Live) so they expire
"""
from database.sqlconnection import SQLConnection
from account.account import *


class Authenticator():
    """
    A token authentication system used to track and 
    authenticate account sessions.
    """

    def __init__(self, database: SQLConnection) -> None:
        self.__database = database
        self.__sessions = {
            "test": AdminAccount(None)
        }


    def verifyToken(self, token: str) -> bool:
        """
        Verifies that the token is a valid session.
        """
        return token in self.__sessions.keys()
    
    
    def getAccount(self, token: str) -> Account:
        """
        Gets account wrapper from token/
        """
        return self.__sessions.get(token)
    

    def createPatientAccount(self, account: PatientAccount):
        """
        Creates the patient account into the database.
        """
        
    
    
