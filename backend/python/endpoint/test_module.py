"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Test endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.test import Test, TestResult, TestWithResult
from utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/test/view")
def test_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
        
    patientAccountID = params["patientAccountID"]

    # Must own account or have permission
    if patientAccountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_TEST):
        return {
            "status": 401,
            "message": "You cannot view these tests!"
        }

    test = TestWithResult(None)

    return {
        "status": 201,
        "tests": test.getMany(__database, {"patientAccountID": patientAccountID})
    }


@__flask.route("/test/create")
def test_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_TEST):
        return {
            "status": 401,
            "message": "You cannot create tests!"
        }

    params["testID"] = id()

    test = Test(params["testID"])
    test.create(__database, params)

    createReminder(__database, "Lab Test", params["date"], params["time"], params["patientAccountID"])

    return { "status": 201 } | test.get(__database)


@__flask.route("/test/result/create")
def test_result_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_RESULT):
        return {
            "status": 401,
            "message": "You cannot create test results!"
        }

    params["testResultID"] = id()

    result = TestResult(params["testResultID"])
    result.create(__database, params)

    return { "status": 201 } | result.get(__database)
