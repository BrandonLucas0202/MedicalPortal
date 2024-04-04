"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Chart endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from model.data import Chart
from endpoint.utility import *
from datetime import date

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/chart/view")
def chart_view():
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
            "message": "You cannot view these charts!"
        }

    chart = Chart(None)

    return {
        "status": 201,
        "charts": chart.getMany(__database, {"patientAccountID": patientAccountID})
    }


@__flask.route("/chart/create")
def chart_create():
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
            "message": "You cannot create charts!"
        }

    params["chartID"] = id()
    params["date"] = date.today().strftime('%Y-%m-%d')

    chart = Chart(params["chartID"])
    chart.create(__database, params)

    return { "status": 201 } | chart.get(__database)
