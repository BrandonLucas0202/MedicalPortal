"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Account endpoint module that handles:
- Creation
- Updating
- Viewing
- Login
"""
from app_provider import app_instance
from auth.permission import Permission
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import PatientAccount, StaffAccount
from account.account import *
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util
import hashlib

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask

@__flask.route("/account/login", methods=["GET"])
def account_login():
    email = util.getParameter("email")
    password = util.getParameter("password")

    token, accountID = __auth.login(email, password)

    if not token or not accountID:
        return {
            "status": 401,
            "message": "Invalid credentials!"
        }
    else:
        return {
            "status": 201,
            "token": token,
            "accountID": accountID
        }

@__flask.route("/account/patient/view", methods=["GET"])
def patient_account_view():
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

    # Must own account or have permission
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_PATIENTS):
        return {
            "status": 401,
            "message": "You cannot view this account!"
        }

    account = LitePatientAccount(accountID).get(__database)

    return {
        "status": 201,
        "accountID": account.accountID,
        "email": account.email,
        "phoneNumber": account.phoneNumber,
        "address": account.address,
        "age": account.age,
        "ssn": account.ssn,
        "insurancePolicyID": account.insurancePolicyID
    }


@__flask.route("/account/staff/view", methods=["GET"])
def staff_account_view():
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

    # Must own account or have permission
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.VIEW_STAFF):
        return {
            "status": 401,
            "message": "You cannot view this account!"
        }

    account = LiteStaffAccount(accountID).get(__database)

    return {
        "status": 201,
        "accountID": account.accountID,
        "email": account.email,
        "phoneNumber": account.phoneNumber,
        "address": account.address,
        "role": account.role,
        "staffAccountID": account.staffAccountID
    }

@__flask.route("/account/patient/update", methods=["GET"])
def patient_account_update():
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
    email = util.getParameter("email")
    phoneNumber = util.getParameter("phoneNumber")
    address = util.getParameter("address")
    age = util.getParameter("age")
    ssn = util.getParameter("ssn")
    insurancePolicyID = util.getParameter("insurancePolicyID")


    # Must own account
    if accountID != __auth.getAccount(token).getID() and not __auth.hasPermission(token, Permission.MODIFY_PATIENTS):
        return {
            "status": 401,
            "message": "You do not control this account!"
        }

    account = PatientAccount(accountID, email, phoneNumber, address, age, ssn, insurancePolicyID)

    connection = __database.connection()
    for (update, values) in account.updates():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(update, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "message": "Account updated successfully!"
    }

@__flask.route("/account/staff/update", methods=["GET"])
def staff_account_update():
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
    email = util.getParameter("email")
    phoneNumber = util.getParameter("phoneNumber")
    address = util.getParameter("address")
    staffAccountID = util.getParameter("staffAccountID")
    role = util.getParameter("role")


    # Must own account
    if not __auth.hasPermission(token, Permission.MODIFY_STAFF):
        return {
            "status": 401,
            "message": "You do not control this account!"
        }

    account = StaffAccount(staffAccountID, email, phoneNumber, address, role, accountID)

    connection = __database.connection()
    for (update, values) in account.updates():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(update, values)
        cursor.close()
    connection.commit()
    connection.close()

    return {
        "status": 201,
        "message": "Account updated successfully!"
    }



@__flask.route("/account/patient/create", methods=["GET"])
def patient_account_create():   
    accountID = ''.join(choices(digits + ascii_uppercase, k=36))
    age = util.getParameter("age")
    ssn = util.getParameter("ssn")
    insurancePolicyID = util.getParameter("insurancePolicyID")
    email = util.getParameter("email")
    password = util.getParameter("password")
    phoneNumber = util.getParameter("phoneNumber")
    address = util.getParameter("address")

    if __auth.emailExists(email):
        return {
        "status": 400,
        "message": "Email is invalid!"
    }

    account = PatientAccount(accountID, email, phoneNumber, address, age, ssn, insurancePolicyID)

    connection = __database.connection()
    for (insert, values) in account.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    
    hash = hashlib.md5((password + email).encode()).hexdigest()

    cursor: MySQLCursor = connection.cursor()
    cursor.execute(
        "INSERT INTO HashedPassword (email, hash, accountID) VALUES (%s, %s, %s)",
        (email, hash, accountID)
    )
    cursor.close()
    connection.commit()
    connection.close()

    token, accountID = __auth.login(email, password)

    return {
        "status": 201,
        "token": token,
        "accountID": accountID
    }



@__flask.route("/account/staff/create", methods=["GET"])
def staff_account_create():   
    # TODO: Make only admins do this
    accountID = ''.join(choices(digits + ascii_uppercase, k=36))
    staffAccountID = ''.join(choices(digits + ascii_uppercase, k=36))
    role = util.getParameter("role")
    email = util.getParameter("email")
    password = util.getParameter("password")
    phoneNumber = util.getParameter("phoneNumber")
    address = util.getParameter("address")

    if __auth.emailExists(email):
        return {
        "status": 400,
        "message": "Email is invalid!"
    }

    account = StaffAccount(staffAccountID, email, phoneNumber, address, role, accountID)

    connection = __database.connection()
    for (insert, values) in account.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert, values)
        cursor.close()
    
    hash = hashlib.md5((password + email).encode()).hexdigest()

    cursor: MySQLCursor = connection.cursor()
    cursor.execute(
        "INSERT INTO HashedPassword (email, hash, accountID) VALUES (%s, %s, %s)",
        (email, hash, accountID)
    )
    cursor.close()
    connection.commit()
    connection.close()

    token, accountID = __auth.login(email, password)

    return {
        "status": 201,
        "token": token,
        "accountID": accountID
    }