"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Account endpoint module that handles:
- Creation
- Updating
"""
from app_provider import app_instance
from flask import abort
from random import choices
from string import digits, ascii_uppercase
from UserO.AllObjects import Account, PatientAccount, StaffAccount
from mysql.connector.cursor import MySQLCursor
import endpoint.utility as util
import hashlib

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/account/patient/update", methods=["PUT"])
def account_update():
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
    password = util.getParameter("password")
    phoneNumber = util.getParameter("phoneNumber")
    address = util.getParameter("address")

    # Must own account
    if accountID != __auth.getAccount(token).getID():
        return {
            "status": 401,
            "message": "You do not control this account!"
        }

    account = Account(accountID, email, password, phoneNumber, address)

    connection = __database.connection()
    for update in account.updates():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(update)
        cursor.close()
    connection.close()

    return {
        "status": 201,
        "message": "Account updated successfully!"
    }


@__flask.route("/account/patient/create", methods=["PUT"])
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
    for insert in account.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert)
        cursor.close()
    
    hash = hashlib.md5((password + email).encode())

    cursor: MySQLCursor = connection.cursor()
    cursor.execute(
        "INSERT INTO HashedPassword (email, hash, accountID) VALUES (%s, %s, %s)",
        (email, hash, accountID)
    )
    cursor.close()
    connection.close()

    token = __auth.login(email, password)

    return {
        "status": 201,
        "token": token
    }


@__flask.route("/account/staff/create", methods=["PUT"])
def staff_account_create():   
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
    for insert in account.inserts():
        cursor: MySQLCursor = connection.cursor()
        cursor.execute(insert)
        cursor.close()
    
    hash = hashlib.md5((password + email).encode())

    cursor: MySQLCursor = connection.cursor()
    cursor.execute(
        "INSERT INTO HashedPassword (email, hash, accountID) VALUES (%s, %s, %s)",
        (email, hash, accountID)
    )
    cursor.close()
    connection.close()

    token = __auth.login(email, password)

    return {
        "status": 201,
        "token": token
    }