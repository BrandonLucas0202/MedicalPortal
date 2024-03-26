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
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import Appointment
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/appointment/view", methods=["GET"])
def appointment_view():
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
    
    appointmentID = util.getParameter("appointmentID")

    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(Appointment.select(), [appointmentID])
    for (appointmentID, description, date, time, patientAccountID, doctorAccountID) in cursor:
        result = {
            "status": 201,
            "appointmentID": appointmentID,
            "description": description,
            "date": date,
            "time": time,
            "patientAccountID": patientAccountID,
            "doctorAccountID": doctorAccountID
        }
    cursor.close()
    connection.close()

    if not __auth.hasPermission(token, Permission.VIEW_APPOINTMENT):
        return {
            "status": 401,
            "message": "You cannot view this appointment!"
        }

    return result



@__flask.route("/appointment/create", methods=["GET"])
def appointment_create():
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

    appointmentID = ''.join(choices(digits + ascii_uppercase, k=36))
    description = util.getParameter("description")
    date = util.getParameter("date")
    time = util.getParameter("time")
    patientAccountID = util.getParameter("patientAccountID")
    doctorAccountID = util.getParameter("doctorAccountID")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_APPOINTMENT):
        return {
            "status": 401,
            "message": "You cannot make appointments!"
        }

    chart = Appointment(appointmentID, description, date, time, patientAccountID, doctorAccountID)

    connection = __database.connection()
    for insert, values in chart.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "appointmentID": appointmentID
    }
