"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Account objects and HashedPassword object.
"""
from auth.permission import Permission
from database.sqlconnection import SQLConnection
from model.model import Model, StaticModel, QueryModel


class HashedPassword(StaticModel):
    def __init__(self, accountID: str) -> None:
        Model.__init__(self, "HashedPassword", [
           "email", "hash", "accountID"
        ], {"accountID": accountID})
        self.__accountID = accountID

    def getAccountID(self):
        return self.__accountID
    
class AccountTypeQuery(QueryModel):
    def __init__(self, accountID) -> None:
        Model.__init__(self, "Account LEFT JOIN StaffAccount ON StaffAccount.staffAccountID = Account.accountID", [
           "CASE WHEN role IS NULL THEN \"Patient\" ELSE role END AS type"
        ], {"accountID": accountID})

class EmailCountQuery(QueryModel):
    def __init__(self, email) -> None:
        Model.__init__(self, "HashedPassword", [
           "COUNT(*)"
        ], {"email": email})


class Account(Model):

    def __init__(self, id: str, permissions: list[Permission]) -> None:
        Model.__init__(self, "Account", [
           "accountID", "email", "phoneNumber", "address", "firstName", "middleName", "lastName", "dob"
        ], {"accountID": id})
        self.__id = id
        self.__permissions = permissions

    def getPermissions(self) -> list[Permission]:
        return self.__permissions
    
    def getAccountID(self) -> str:
        return self.__id
    
    def getBase(self) -> "Account":
        return Account(self.__id, self.__permissions)
    
    def delete(self, database: SQLConnection):
        hashedPass = HashedPassword(self.__id)
        hashedPass.delete(database)

class PatientAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            Permission.VIEW_PHARMACY,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_LAB,
            Permission.CREATE_PAYMENT
        ])
        Model.__init__(self, "PatientAccount", [
           "patientAccountID", "ssn", "insurancePolicyID"
        ], {"patientAccountID": id})

    def update(self, database: SQLConnection, data: dict):
        super().update(database, data)
        self.getBase().update(database, data)

    def create(self, database: SQLConnection, data: dict):
        self.getBase().create(database, data)
        super().create(database, data)

    def get(self, database: SQLConnection, filter: dict = None) -> dict:
        return super().get(database, filter) | self.getBase().get(database, filter)

class StaffAccount(Account):

    def __init__(self, id: str, permissions = [
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
        ]) -> None:
        Account.__init__(self, id, permissions)
        Model.__init__(self, "StaffAccount", [
           "staffAccountID", "role"
        ], {"staffAccountID": id})

    def update(self, database: SQLConnection, data: dict):
        super().update(database, data)
        self.getBase().update(database, data)

    def create(self, database: SQLConnection, data: dict):
        self.getBase().create(database, data)
        super().create(database, data)

    def get(self, database: SQLConnection, filter: dict = None) -> dict:
        return super().get(database, filter) | self.getBase().get(database, filter)


class AdminAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        StaffAccount.__init__(self, id, [
            Permission.ADMINISTRATOR
        ])
    

class NurseAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        StaffAccount.__init__(self, id, [
            Permission.VIEW_CHARTS,
            Permission.CREATE_CHART,
            Permission.VIEW_PRESCRIPTIONS,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_PHARMACY,
            Permission.CREATE_PHARMACY,
            Permission.CREATE_LAB,
            Permission.VIEW_LAB,
            Permission.CREATE_APPOINTMENT,
            Permission.VIEW_APPOINTMENT,
            Permission.CREATE_REMINDER,
            Permission.VIEW_REMINDER,
            Permission.VIEW_TEST,
            Permission.CREATE_TEST,
            Permission.CREATE_RESULT
        ])
    

class DoctorAccount(StaffAccount):

    def __init__(self, id: str) -> None:
        StaffAccount.__init__(self, id, [
            Permission.VIEW_CHARTS,
            Permission.CREATE_CHART,
            Permission.VIEW_PRESCRIPTIONS,
            Permission.CREATE_PRESCRIPTION,
            Permission.VIEW_INSURANCE,
            Permission.VIEW_PHARMACY,
            Permission.CREATE_PHARMACY,
            Permission.CREATE_LAB,
            Permission.VIEW_LAB,
            Permission.CREATE_APPOINTMENT,
            Permission.VIEW_APPOINTMENT,
            Permission.CREATE_REMINDER,
            Permission.VIEW_REMINDER,
            Permission.VIEW_TEST,
            Permission.CREATE_TEST,
            Permission.CREATE_RESULT
        ])
