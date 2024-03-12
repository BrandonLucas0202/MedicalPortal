"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal


"""
from permission import AccountPermission

class LiteAccount():
    """
    As the name suggests, it is a "lite" version of an account.
    Only stores the account's ID and its permissions, since
    that is really all we will need for querying.
    """

    def __init__(self, id: str, permissions: list[AccountPermission]) -> None:
        self.__id = id
        self.__permissions = permissions
