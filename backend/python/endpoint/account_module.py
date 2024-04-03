"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Account endpoint module that handles:
- Creation
- Updating
- Viewing
- Login
"""
from app_provider import app_instance
from auth.permission import Permission
from model.account import PatientAccount, StaffAccount, HashedPassword
from endpoint.utility import *
import hashlib

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask

@__flask.route("/account/login")
def account_login():
    params = getParameters()
    token = __auth.login(params["email"], params["password"])

    if not token:
        return {
            "status": 401,
            "message": "Invalid credentials!"
        }
    else:
        account = __auth.getAccount(token)
        return {
            "status": 201,
            "token": token
        } | account.get(__database)

@__flask.route("/account/patient/view")
def patient_account_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    accountID = params["accountID"]

    # Must own account or have permission
    if accountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_PATIENTS):
        return {
            "status": 401,
            "message": "You cannot view this account!"
        }

    account = PatientAccount(accountID)
    
    return {"status": 201} | account.get(__database)


@__flask.route("/account/staff/view")
def staff_account_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    accountID = params["accountID"]

    # Must own account or have permission
    if accountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_STAFF):
        return {
            "status": 401,
            "message": "You cannot view this account!"
        }

    account = StaffAccount(accountID)

    return {"status": 201} | account.get(__database)


@__flask.route("/account/patient/update")
def patient_account_update():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    accountID = params["accountID"]

    # Must own account
    if accountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.MODIFY_PATIENTS):
        return {
            "status": 401,
            "message": "You do not control this account!"
        }

    account = PatientAccount(accountID)
    account.update(__database, params)

    return {
        "status": 201,
        "message": "Account updated successfully!"
    }

@__flask.route("/account/staff/update")
def staff_account_update():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    accountID = params["accountID"]

    # Must own account
    if accountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.MODIFY_STAFF):
        return {
            "status": 401,
            "message": "You do not control this account!"
        }

    account = StaffAccount(accountID)
    account.update(__database, params)

    return {
        "status": 201,
        "message": "Account updated successfully!"
    }



@__flask.route("/account/patient/create")
def patient_account_create():   
    params = getParameters()
    
    if __auth.emailExists(params["email"]):
        return {
        "status": 400,
        "message": "Email is invalid!"
    }

    params["accountID"] = id()
    account = PatientAccount(params["accountID"])
    account.create(__database, params)
    
    params["hash"] = hashlib.md5((params["password"] + params["email"]).encode()).hexdigest()
    hashedPassword = HashedPassword(params["accountID"])
    hashedPassword.create(__database, params)

    token = __auth.login(params["email"], params["password"])

    return {
        "status": 201,
        "token": token
    } | account.get(__database)



@__flask.route("/account/staff/create")
def staff_account_create():   
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    # Must own account
    if not __auth.hasPermission(token, Permission.CREATE_STAFF):
        return {
            "status": 401,
            "message": "You cannot create Staff accounts!"
        }
    
    if __auth.emailExists(params["email"]):
        return {
        "status": 400,
        "message": "Email is invalid!"
    }

    params["accountID"] = id()
    params["staffAccountID"] = params["accountID"]

    account = StaffAccount(params["accountID"])
    account.create(__database, params)
    
    params["hash"] = hashlib.md5((params["password"] + params["email"]).encode()).hexdigest()
    hashedPassword = HashedPassword(params["accountID"])
    hashedPassword.create(__database, params)

    token = __auth.login(params["email"], params["password"])

    return {
        "status": 201,
        "token": token
    } | account.get(__database)
