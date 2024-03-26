"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Message endpoint module that handles:
- Creation
- Updating
- Viewing
"""
from app_provider import app_instance
from auth.permission import Permission
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import Prescription
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/prescription/view", methods=["GET"])
def prescriptions_view():
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
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_PRESCRIPTIONS):
        return {
            "status": 401,
            "message": "You cannot view these prescriptions!"
        }

    result = {
        "status": 201,
        "prescriptions": []
    }

    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(Prescription.select(), [accountID])
    for (prescriptionID, drug, dosage, frequency, date, pharmacyID, patientAccountID) in cursor:
        result["prescriptions"].append({
            "prescriptionID": prescriptionID,
            "drug": drug,
            "dosage": dosage,
            "frequency": frequency,
            "date": date,
            "pharmacyID": pharmacyID,
            "patientAccountID": patientAccountID
        })

    return result


@__flask.route("/prescription/create", methods=["GET"])
def prescription_create():
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
    
    prescriptionID = ''.join(choices(digits + ascii_uppercase, k=36))
    drug = util.getParameter("drug")
    dosage = util.getParameter("dosage")
    frequency = util.getParameter("frequency")
    date = util.getParameter("date")
    pharmacyID = util.getParameter("pharmacyID")
    patientAccountID = util.getParameter("patientAccountID")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_PRESCRIPTION):
        return {
            "status": 401,
            "message": "You cannot make prescriptions!"
        }

    chart = Prescription(prescriptionID, drug, dosage, frequency, date, pharmacyID, patientAccountID)

    connection = __database.connection()
    for insert, values in chart.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.close()

    return {
        "status": 201,
        "prescriptionID": prescriptionID
    }
