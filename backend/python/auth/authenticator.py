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
from model.account import *
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
        self.__sessions = {}


    def verifyToken(self, token: str) -> bool:
        return token in self.__sessions.keys()
    
    def updateToken(self, token: str, account: Account):
        self.__sessions[token] = account
    
    
    def getAccount(self, token: str) -> Account:
        return self.__sessions.get(token)
    
    def hasPermission(self, token: str, permission: Permission):
        return permission in self.getAccount(token).getPermissions() or Permission.ADMINISTRATOR in self.getAccount(token).getPermissions()
    
    def emailExists(self, email: str) -> bool:
        emailCount = EmailCountQuery(email).get(self.__database)
        return emailCount["COUNT(*)"] > 0

    def login(self, email: str, password: str) -> str:
        # Hash and use email as salt
        hash = hashlib.md5((password + email).encode()).hexdigest()

        hashedPassword = HashedPassword(None)
        result = hashedPassword.get(self.__database, {"email": email, "hash": hash})
        if "accountID" in result:
            accountID = result["accountID"]
        else:
            return None

        # Find account type
        accountType = AccountTypeQuery(accountID).get(self.__database)

        # Create account object, create session token and return
        account = TYPETABLE[accountType](accountID)
        token = secrets.token_hex(32)

        self.__sessions[token] = account

        return token 
    
