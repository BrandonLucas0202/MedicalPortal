"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Lab endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.data import Laboratory
from utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/lab/view")
def lab_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_LAB):
        return {
            "status": 401,
            "message": "You cannot view this lab!"
        }

    lab = Laboratory(params["labID"])

    return {
        "status": 201,
        "lab": lab.get(__database)
    }

@__flask.route("/lab/search")
def lab_search():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.VIEW_LAB):
        return {
            "status": 401,
            "message": "You cannot view lab!"
        }

    lab = Laboratory(None)

    return {
        "status": 201,
        "labs": lab.search(__database, params)
    }


@__flask.route("/lab/create")
def lab_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_LAB):
        return {
            "status": 401,
            "message": "You cannot create labs!"
        }

    params["labID"] = id()

    lab = Laboratory(params["labID"])
    lab.create(__database, params)

    return { "status": 201 } | lab.get(__database)
