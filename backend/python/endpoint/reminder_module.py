"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Reminder endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.appointment import Reminder
from endpoint.utility import *
from datetime import date

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/reminder/view")
def reminder_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    reminder = Reminder(None)

    return {
        "status": 201,
        "reminders": reminder.getMany(__database, {"accountID": __auth.getAccount(token).getAccountID()})
    }


@__flask.route("/reminder/create")
def reminder_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    params["reminderID"] = id()
    params["accountID"] = __auth.getAccount(token).getAccountID()

    reminder = Reminder(params["reminderID"])
    reminder.create(__database, params)

    return { "status": 201 } | reminder.get(__database)
