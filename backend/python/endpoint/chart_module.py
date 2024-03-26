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
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import Chart
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/chart/view", methods=["GET"])
def charts_view():
    try:
        token = util.getParameter(
            "token", 
            verifier = __auth.verifyToken
        )
    except Exception as e:
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    accountID = util.getParameter("accountID")
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_CHARTS):
        return {
            "status": 401,
            "message": "You cannot view these charts!"
        }

    result = {
        "status": 201,
        "charts": []
    }

    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(Chart.select(), [accountID])
    for (chartID, weight, height, bloodPressure, temperature, diagnoses, allergies, date, patientAccountID) in cursor:
        result["charts"].append({
            "chartID": chartID,
            "weight": weight,
            "height": height,
            "bloodPressure": bloodPressure,
            "temperature": temperature,
            "diagnoses": diagnoses,
            "allergies": allergies,
            "date": date,
            "patientAccountID": patientAccountID
        })
    
    cursor.close()
    connection.close()
    return result


@__flask.route("/chart/create", methods=["GET"])
def chart_create():
    try:
        token = util.getParameter(
            "token", 
            verifier = __auth.verifyToken
        )
    except Exception as e:
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    chartID = ''.join(choices(digits + ascii_uppercase, k=36))
    accountID = util.getParameter("accountID")
    weight = util.getParameter("weight")
    height = util.getParameter("height")
    bloodPressure = util.getParameter("bloodPressure")
    temperature = util.getParameter("temperature")
    diagnoses = util.getParameter("diagnoses")
    allergies = util.getParameter("allergies")
    date = util.getParameter("date")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_CHART):
        return {
            "status": 401,
            "message": "You cannot make charts!"
        }

    chart = Chart(chartID, weight, height, bloodPressure, temperature, diagnoses, allergies, date, accountID)

    connection = __database.connection()
    for insert, values in chart.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "chartID": chartID
    }
