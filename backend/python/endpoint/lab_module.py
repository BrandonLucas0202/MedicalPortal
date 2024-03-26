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
from UserO.AllObjects import Laboratory
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/lab/view", methods=["GET"])
def lab_view():
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
    
    labID = util.getParameter("labID")
    if not __auth.hasPermission(token, Permission.VIEW_LAB):
        return {
            "status": 401,
            "message": "You cannot view this lab!"
        }

    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(Laboratory.select(), [labID])
    for (labID, name, address, phoneNumber) in cursor:
        result = {
            "status": 201,
            "labID": labID,
            "name": name,
            "address": address,
            "phoneNumber": phoneNumber
        }
    
    cursor.close()
    connection.close()
    return result


@__flask.route("/lab/create", methods=["GET"])
def lab_create():
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

    labID = ''.join(choices(digits + ascii_uppercase, k=36))
    name = util.getParameter("name")
    address = util.getParameter("address")
    phoneNumber = util.getParameter("phoneNumber")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_LAB):
        return {
            "status": 401,
            "message": "You cannot make labs!"
        }

    chart = Laboratory(labID, name, address, phoneNumber)

    connection = __database.connection()
    for insert, values in chart.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "labID": labID
    }
