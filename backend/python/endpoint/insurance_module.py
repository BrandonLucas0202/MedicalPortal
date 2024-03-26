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
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import InsurancePolicy
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/insurance/view", methods=["GET"])
def insurance_view():
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
    
    insurancePolicyID = util.getParameter("insurancePolicyID")
    if insurancePolicyID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_INSURANCE):
        return {
            "status": 401,
            "message": "You cannot view this insurance!"
        }
    
    connection = __database.connection()
    cursor: MySQLCursor = connection.cursor()
    cursor.execute(InsurancePolicy.select(), [insurancePolicyID])
    for (insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount) in cursor:
        result = {
            "insurancePolicyID": insurancePolicyID,
            "insuranceName": insuranceName,
            "insurancePolicyNumber": insurancePolicyNumber,
            "copayAmount": copayAmount
        }
    
    cursor.close()
    connection.close()
    return result



@__flask.route("/insurance/create", methods=["GET"])
def insurance_create():
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
    
    insurancePolicyID = ''.join(choices(digits + ascii_uppercase, k=36))
    insuranceName = util.getParameter("insuranceName")
    insurancePolicyNumber = util.getParameter("insurancePolicyNumber")
    copayAmount = util.getParameter("copayAmount")

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_PRESCRIPTION):
        return {
            "status": 401,
            "message": "You cannot make insurances!"
        }

    insurance = InsurancePolicy(insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount)

    connection = __database.connection()
    for insert, values in insurance.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "insurancePolicyID": insurancePolicyID
    }
