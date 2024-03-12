"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

An Enum sotring the different permissions an account can hold
Virtually every single endpoint will need its own permission,
so as we progress, a permission needs made and used for each module.

"""
from enum import Enum


class AccountPermission(Enum):
    TEST = 0