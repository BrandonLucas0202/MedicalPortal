"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Appointment endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.appointment import Appointment, Reminder
from utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/appointment/patient/view")
def appointment_patient_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    patientAccountID = params["patientAccountID"]

    # Must own account or have permission
    if patientAccountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_APPOINTMENT):
        return {
            "status": 401,
            "message": "You cannot view these appointments!"
        }

    appointment = Appointment(None)

    return {
        "status": 201,
        "appointments": appointment.getMany(__database, {"patientAccountID": patientAccountID})
    }

@__flask.route("/appointment/doctor/view")
def appointment_doctor_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    doctorAccountID = params["doctorAccountID"]

    # Must own account or have permission
    if doctorAccountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_APPOINTMENT):
        return {
            "status": 401,
            "message": "You cannot view these appointments!"
        }

    appointment = Appointment(None)

    return {
        "status": 201,
        "appointments": appointment.getMany(__database, {"doctorAccountID": doctorAccountID})
    }


@__flask.route("/appointment/create")
def appointment_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_APPOINTMENT):
        return {
            "status": 401,
            "message": "You cannot create appointments!"
        }

    params["appointmentID"] = id()

    appointment = Appointment(params["appointmentID"])
    appointment.create(__database, params)

    createReminder(__database, "Appointment", params["date"], params["time"], params["patientAccountID"])
    createReminder(__database, "Appointment", params["date"], params["time"], params["doctorAccountID"])

    return { "status": 201 } | appointment.get(__database)
