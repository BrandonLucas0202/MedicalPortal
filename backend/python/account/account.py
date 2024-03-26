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


class LiteAccount():

    def __init__(self, id: str, permissions: list[Permission]) -> None:
        self.__id = id
        self.__permissions = permissions

    def getPermissions(self) -> list[Permission]:
        return self.__permissions
    
    def getID(self) -> str:
        return self.__id

class LitePatientAccount(LiteAccount):

    def __init__(self, id: str) -> None:
        LiteAccount.__init__(self, id, [
            Permission.VIEW_PHARMACY,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_LAB,
            Permission.CREATE_PAYMENT
        ])

    def get(self, database: SQLConnection) -> AllObjects.PatientAccount:
        # Get connection and cursor
        connection = database.connection()
        cursor: MySQLCursor = connection.cursor()

        cursor.execute(AllObjects.PatientAccount.select(), self.__id)

        for (accountID, email, phoneNumber, address, age, ssn, insurancePolicyID) in cursor:
            account = AllObjects.PatientAccount(accountID, email, phoneNumber, address, age, ssn, insurancePolicyID)
            break

        cursor.close()
        connection.close()

        return account



class LiteStaffAccount(LiteAccount):

    def __init__(self, id: str) -> None:
        LiteAccount.__init__(self, id, [
            Permission.MODIFY_PATIENTS,
            Permission.VIEW_INSURANCE,
            Permission.CREATE_INSURANCE,
            Permission.VIEW_PHARMACY,
            Permission.CREATE_PHARMACY,
            Permission.CREATE_LAB,
            Permission.VIEW_LAB,
            Permission.CREATE_APPOINTMENT,
            Permission.VIEW_APPOINTMENT,
            Permission.CREATE_BILL,
            Permission.VIEW_BILL,
            Permission.CREATE_PAYMENT,
            Permission.VIEW_PAYMENT,
            Permission.CREATE_REMINDER,
            Permission.VIEW_REMINDER
        ])

    def get(self, database: SQLConnection) -> AllObjects.StaffAccount:
        # Get connection and cursor
        connection = database.connection()
        cursor: MySQLCursor = connection.cursor()

        cursor.execute(AllObjects.StaffAccount.select(), self.__id)

        for (staffAccountID, email, phoneNumber, address, role, accountID) in cursor:
            account = AllObjects.StaffAccount(staffAccountID, email, phoneNumber, address, role, accountID)
            break

        cursor.close()
        connection.close()

        return account


class LiteAdminAccount(LiteStaffAccount):

    def __init__(self, id: str) -> None:
        LiteAccount.__init__(self, id, [
            Permission.ADMINISTRATOR
        ])
    

class LiteNurseAccount(LiteStaffAccount):

    def __init__(self, id: str) -> None:
        LiteAccount.__init__(self, id, [
            Permission.VIEW_CHARTS,
            Permission.CREATE_CHART,
            Permission.VIEW_PRESCRIPTIONS,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_PHARMACY,
            Permission.VIEW_LAB,
            Permission.CREATE_APPOINTMENT,
            Permission.VIEW_APPOINTMENT,
            Permission.CREATE_REMINDER,
            Permission.VIEW_REMINDER
        ])
    

class LiteDoctorAccount(LiteStaffAccount):

    def __init__(self, id: str) -> None:
        LiteAccount.__init__(self, id, [
            Permission.VIEW_CHARTS,
            Permission.CREATE_CHART,
            Permission.VIEW_PRESCRIPTIONS,
            Permission.CREATE_PRESCRIPTION,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_PHARMACY,
            Permission.VIEW_LAB,
            Permission.CREATE_APPOINTMENT,
            Permission.VIEW_APPOINTMENT,
            Permission.CREATE_REMINDER,
            Permission.VIEW_REMINDER
        ])
