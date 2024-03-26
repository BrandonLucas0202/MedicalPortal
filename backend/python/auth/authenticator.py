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
from mysql.connector.cursor import MySQLCursor
import secrets
import hashlib


TYPETABLE = {
    "Patient": PatientAccount,
    "Doctor": DoctorAccount,
    "Nurse": NurseAccount,
    "Staff": StaffAccount,
    "Admin": AdminAccount
}


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
    
    def updateToken(self, token: str, account: Account):
        """
        Updates token with an account.
        """
        self.__sessions[token] = account
    
    
    def getAccount(self, token: str) -> Account:
        """
        Gets account wrapper from token.
        """
        return self.__sessions.get(token)
    
    def hasPermission(self, token: str, permission: Permission):
        """
        Checks if token has a permission.
        """
        return permission in self.getAccount(token).getPermissions()
    
    def emailExists(self, email: str) -> bool:
        connection = self.__database.connection()
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM HashedPassword WHERE email = %s",
            (email)
        )

        for value in cursor:
            count = value
            break

        cursor.close()
        connection.close()

        return count > 0

    def login(self, email: str, password: str) -> str:
        # Hash and use email as salt
        hash = hashlib.md5((password + email).encode())

        connection = self.__database.connection()

        # Execute and find account
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT accountID FROM HashedPassword WHERE email=%s AND hash=%s",
            (email, hash)
        )

        for accountID in cursor:
            id = accountID
            break
        else: # Did not find an account
            return None
        cursor.close()

        # Find account type
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(
            "SELECT CASE WHEN role IS NULL THEN \"Patient\" ELSE role END as accountType FROM Account LEFT JOIN StaffAccount ON StaffAccount.accountID = Account.accountID WHERE Account.accountID = %s",
            id
        )

        for role in cursor:
            accountType = role
            break
        cursor.close()
        connection.close()

        # Create account object, create session token and return
        account = TYPETABLE[role](id)
        token = secrets.token_hex(32)

        self.__sessions[token] = account

        return token    
    
