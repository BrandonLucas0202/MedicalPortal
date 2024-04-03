"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

An endpoint utility used for endpoint modules.
"""
from flask import request
from random import choices
from string import digits, ascii_uppercase, ascii_lowercase
from model.appointment import Reminder

def getParameters():
    """
    Trys retrieving a passed request argument and verifies
    the argument with the provided function.
    """
    return request.args.to_dict()


def id():
    """
    Generates a random 36 digit id.
    """
    return ''.join(choices(digits + ascii_uppercase + ascii_lowercase, k=36))


def createReminder(database, description, date, time, accountID):
    """
    Creates a reminder.
    """
    reminder = Reminder(id())
    reminder.create(database, {
        "reminderID": id(),
        "description": description,
        "date": date,
        "time": time,
        "accountID": accountID
    })