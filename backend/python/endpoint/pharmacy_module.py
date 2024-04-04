"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Pharmacy endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.data import Pharmacy
from endpoint.utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/pharmacy/view")
def pharmacy_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_PHARMACY):
        return {
            "status": 401,
            "message": "You cannot view this pharmacy!"
        }

    pharmacy = Pharmacy(params["pharmacyID"])

    return { "status": 201 } | pharmacy.get(__database)

@__flask.route("/pharmacy/search")
def pharmacy_search():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_PHARMACY):
        return {
            "status": 401,
            "message": "You cannot view pharmacies!"
        }

    pharmacy = Pharmacy(None)

    return {
        "status": 201,
        "pharmacies": pharmacy.search(__database, params)
    }


@__flask.route("/pharmacy/create")
def pharmacy_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_PHARMACY):
        return {
            "status": 401,
            "message": "You cannot create pharmacies!"
        }

    params["pharmacyID"] = id()

    pharmacy = Pharmacy(params["pharmacyID"])
    pharmacy.create(__database, params)

    return { "status": 201 } | pharmacy.get(__database)
