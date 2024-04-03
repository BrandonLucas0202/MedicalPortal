"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Prescription endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.data import Prescription
from utility import *
from datetime import date

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/prescription/view")
def prescription_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    patientAccountID = params["patientAccountID"]

    # Must own account or have permission
    if patientAccountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_CHARTS):
        return {
            "status": 401,
            "message": "You cannot view these prescriptions!"
        }

    prescription = Prescription(None)

    return {
        "status": 201,
        "prescriptions": prescription.getMany(__database, {"patientAccountID": patientAccountID})
    }


@__flask.route("/prescription/create")
def prescription_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_CHART):
        return {
            "status": 401,
            "message": "You cannot create prescriptions!"
        }

    params["prescriptionID"] = id()
    params["date"] = date.today().strftime('%Y-%m-%d')

    prescription = Prescription(params["prescriptionID"])
    prescription.create(__database, params)

    return { "status": 201 } | prescription.get(__database)
