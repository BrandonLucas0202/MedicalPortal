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
from model.message import Message, OpenConversationsQuery
from endpoint.utility import *

__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask


@__flask.route("/message/conversations")
def message_conversations():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    params["senderAccountID"] = __auth.getAccount(token).getAccountID()

    conversations = OpenConversationsQuery(params["senderAccountID"])

    return {
        "status": 201,
        "conversations": conversations.getMany(__database)
    }

@__flask.route("/message/conversation")
def message_conversation():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }
    
    params["senderAccountID"] = __auth.getAccount(token).getAccountID()

    message = Message(None)

    return {
        "status": 201,
        "messages": message.getMany(__database, {
            "senderAccountID": params["senderAccountID"], 
            "recipientAccountID": params["recipientAccountID"]
        }, orderBy=["date", "time"])
    }


@__flask.route("/message/create")
def message_create():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    params["senderAccountID"] = __auth.getAccount(token).getAccountID()
    params["messageID"] = id()

    message = Message(params["messageID"])
    message.create(__database, params)

    return { "status": 201 } | message.get(__database)

@__flask.route("/message/delete")
def message_delete():
    params = getParameters()
    token = params["token"]
    if not __auth.verifyToken(token):
        return {
            "status": 401,
            "message": "Token is invalid!"
        }

    message = Message(params["messageID"])
    if not message.get()["senderAccountID"] == __auth.getAccount(token).getAccountID():
        return {
            "status": 401,
            "message": "You can only delete messages that you sent!"
        }

    message.delete(__database)

    return { "status": 201 }