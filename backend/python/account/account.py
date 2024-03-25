"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal


"""
from auth.permission import Permission


class Account():

    def __init__(self, id: str, permissions: list[Permission]) -> None:
        self.__id = id
        self.__permissions = permissions

class PatientAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])


class StaffAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            # All permissions would go here
        ])


class AdminAccount(Account):

    def __init__(self, id: str) -> None:
        Account.__init__(self, id, [
            Permission.ADMINISTRATOR
        ])