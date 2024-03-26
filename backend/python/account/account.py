"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Account objects containing ids and permissions.
"""
from auth.permission import Permission
from database.sqlconnection import SQLConnection
from UserO import AllObjects
from mysql.connector.cursor import MySQLCursor


class Account():

    def __init__(self, id: str, permissions: list[Permission]) -> None:
        self.__id = id
        self.__permissions = permissions

    def getPermissions(self) -> list[Permission]:
        return self.__permissions
    
    def getID(self) -> str:
        return self.__id

class PatientAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])

    def get(self, database: SQLConnection) -> AllObjects.PatientAccount:
        # Get connection and cursor
        connection = database.connection()
        cursor: MySQLCursor = connection.cursor()

        cursor.execute(AllObjects.PatientAccount.select(), self.__id)

        for (accountID, email, phoneNumber, address, calendarID, inboxID, outboxID, age, ssn, chart, insurancePolicy, bills) in cursor:
            account = AllObjects.PatientAccount(accountID, email, phoneNumber, address, calendarID, inboxID, outboxID, age, ssn, chart, insurancePolicy, bills)
            break

        cursor.close()
        connection.close()

        return account



class StaffAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])

    def get(self, database: SQLConnection) -> AllObjects.StaffAccount:
        # Get connection and cursor
        connection = database.connection()
        cursor: MySQLCursor = connection.cursor()

        cursor.execute(AllObjects.StaffAccount.select(), self.__id)

        for (staffAccountID, email, phoneNumber, address, calendarID, inboxID, outboxID, role, accountID) in cursor:
            account = AllObjects.StaffAccount(staffAccountID, email, phoneNumber, address, calendarID, inboxID, outboxID, role, accountID)
            break

        cursor.close()
        connection.close()

        return account


class AdminAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            Permission.ADMINISTRATOR
        ])
    

class NurseAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])
    

class DoctorAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])
