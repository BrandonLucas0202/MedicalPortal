"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Bill endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import Bill
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/bill/view", methods=["GET"])
def bill_view():
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
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_BILL):
        return {
            "status": 401,
            "message": "You cannot view these bills!"
        }

    result = {
        "status": 201,
        "bills": []
    }

    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(Bill.select(), [accountID])
    for (billID, description, amount, dateIssued, dueDate, patientAccountID) in cursor:
        result["bills"].append({
            "billID": billID,
            "description": description,
            "amount": amount,
            "dateIssued": dateIssued,
            "dueDate": dueDate,
            "patientAccountID": patientAccountID
        })
    cursor.close()
    connection.close()

    return result


@__flask.route("/bill/create", methods=["GET"])
def bill_create():
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
    
    billID = ''.join(choices(digits + ascii_uppercase, k=36))
    description = util.getParameter("description")
    amount = util.getParameter("amount")
    dateIssued = util.getParameter("dateIssued")
    dueDate = util.getParameter("dueDate")
    patientAccountID = util.getParameter("patientAccountID")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_BILL):
        return {
            "status": 401,
            "message": "You cannot make bills!"
        }

    chart = Bill(billID, description, amount, dateIssued, dueDate, patientAccountID)

    connection = __database.connection()
    for insert, values in chart.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "billID": billID
    }
