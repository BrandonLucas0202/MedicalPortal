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

    """
    Appointment Permissions
    0000-0099
    """
    APPOINTMENT_CREATE = 0
    APPOINTMENT_CANCEL = 1
    APPOINTMENT_EDIT = 2
    APPOINTMENT_FINISH = 3

    """
    Bill Permissions
    0100-0199
    """
    BILL_CREATE = 100
    BILL_CANCEL = 101
    BILL_PAY = 102
    BILL_REFUND = 103

    """
    Chart Permissions
    0200-0299
    """
    CHART_CREATE = 200
    CHART_EDIT = 201

    """
    Message Permissions
    0300-0399
    """
    MESSAGE_SEND = 300
    MESSAGE_DELETE = 301
    MESSAGE_EDIT = 302



