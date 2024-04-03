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
from utility import *
from model.bill import Bill, Payment, BillWithPayments
from datetime import date

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/bill/view")
def bill_view():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    patientAccountID = params["patientAccountID"]

    # Must own account or have permission
    if patientAccountID != __auth.getAccount(token).getAccountID() and not __auth.hasPermission(token, Permission.VIEW_BILL):
        return {
            "status": 401,
            "message": "You cannot view these bills!"
        }

    bill = BillWithPayments(None)

    return {
        "status": 201,
        "bills": bill.getMany(__database, {"patientAccountID": patientAccountID})
    }

@__flask.route("/bill/pay")
def payment_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    params["date"] = date.today().strftime('%Y-%m-%d')
    params["paymentID"] = id()

    payment = Payment(params["paymentID"])
    payment.create(__database, params)

    return { "status": 201 } | payment.get(__database)


@__flask.route("/bill/create")
def bill_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    # Must have permission
    if not __auth.hasPermission(token, Permission.CREATE_BILL):
        return {
            "status": 401,
            "message": "You cannot create bills!"
        }

    params["billID"] = id()
    params["dateIssued"] = date.today().strftime('%Y-%m-%d')

    bill = Bill(params["billID"])
    bill.create(__database, params)

    createReminder(__database, "Bill", params["dateDue"], "00:00:00", params["patientAccountID"])

    return { "status": 201 } | bill.get(__database)
