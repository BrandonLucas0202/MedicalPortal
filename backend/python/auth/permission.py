"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Permission Enums describing permission values for different
endpoint interactions

TODO Implement the rest of permissions
"""
from enum import Enum

class Permission(Enum):
    # Admin permission
    ADMINISTRATOR = -1

    MODIFY_PATIENTS = 1
    MODIFY_STAFF = 2
    
    VIEW_PATIENTS = 3
    VIEW_STAFF = 4

    VIEW_CHARTS = 5
    CREATE_CHART = 6

    VIEW_PRESCRIPTIONS = 7
    CREATE_PRESCRIPTION = 8

    VIEW_INSURANCE = 9
    CREATE_INSURANCE = 10

    VIEW_PHARMACY = 11
    CREATE_PHARMACY = 12

    VIEW_LAB = 13
    CREATE_LAB = 24

    VIEW_APPOINTMENT = 15
    CREATE_APPOINTMENT = 16

    VIEW_BILL = 17
    CREATE_BILL = 18

    VIEW_PAYMENT = 19
    CREATE_PAYMENT = 20

    VIEW_REMINDER = 21
    CREATE_REMINDER = 22

