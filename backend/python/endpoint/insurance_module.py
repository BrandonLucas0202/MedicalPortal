"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Insurance endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.data import InsurancePolicy
from endpoint.utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/insurance/view")
def insurance_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_INSURANCE):
        return {
            "status": 401,
            "message": "You cannot view this insurance!"
        }

    insurance = InsurancePolicy(params["insurancePolicyID"])

    return {
        "status": 201,
        "insurance": insurance.get(__database)
    }

@__flask.route("/insurance/search")
def insurance_search():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_INSURANCE):
        return {
            "status": 401,
            "message": "You cannot view insurance!"
        }

    insurance = InsurancePolicy(None)

    return {
        "status": 201,
        "insurances": insurance.search(__database, params)
    }


@__flask.route("/insurance/create")
def insurance_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_INSURANCE):
        return {
            "status": 401,
            "message": "You cannot create insurances!"
        }

    params["insurancePolicyID"] = id()

    insurance = InsurancePolicy(params["insurancePolicyID"])
    insurance.create(__database, params)

    return { "status": 201 } | insurance.get(__database)
