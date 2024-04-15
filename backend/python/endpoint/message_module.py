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
import http.client
import urllib.parse
import base64
from flask import request, jsonify
from flask_cors import CORS




__app = app_instance() # BackendApplication
__database = __app.getDatabase() # SQLConnection
__auth = __app.getAuthenticator() # Authenticator
__flask = __app.getFlask() # Flask
CORS(__app.getFlask())  # Enable CORS for all domains on all routes



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


@__flask.route("/messages", methods=['GET'])
def get_messages():
    token = request.args.get('token')
    if not __auth.verifyToken(token):
        return jsonify({"status": 401, "message": "Token is invalid!"}), 401
    
    user_id = __auth.getAccount(token).getAccountID()
    messages = Message.query.filter_by(user_id=user_id).all()  # Assuming a Message model with a user_id column
    return jsonify([message.serialize() for message in messages]), 200

@__flask.route("/messages", methods=['POST'])
def post_message():
    token = request.json.get('token')
    content = request.json.get('content')
    recipient_id = request.json.get('recipient_id')

    if not __auth.verifyToken(token):
        return jsonify({"status": 401, "message": "Token is invalid!"}), 401

    sender_id = __auth.getAccount(token).getAccountID()
    new_message = Message(content=content, sender_id=sender_id, recipient_id=recipient_id)
    __database.session.add(new_message)
    __database.session.commit()

    return jsonify(new_message.serialize()), 201

@__flask.route("/messages/<message_id>", methods=['DELETE'])
def delete_message(message_id):
    token = request.args.get('token')
    if not __auth.verifyToken(token):
        return jsonify({"status": 401, "message": "Token is invalid!"}), 401

    message = Message.query.get(message_id)
    if message.sender_id != __auth.getAccount(token).getAccountID():
        return jsonify({"status": 403, "message": "Unauthorized to delete this message"}), 403

    __database.session.delete(message)
    __database.session.commit()
    return jsonify({"status": 200, "message": "Message deleted"}), 200

from flask import Flask, request, jsonify
from mailjet_rest import Client
import os

api_key = os.environ.get('0f8768327c2438ffabd921cef9807074')
api_secret = os.environ.get('bbaa6b280f40034bdd809cefafdb1e9c')
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

@__flask.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    token = data.get('token')
    if not __auth.verifyToken(token):
        return jsonify({"status": 401, "message": "Token is invalid!"}), 401

    email_data = {
        'Messages': [
            {
                "From": {
                    "Email": "brandonlucas060@gmail.com",
                    "Name": "Brandon Lucas"
                },
                "To": [
                    {
                        "Email": data['bdog723@hotmail.com'],
                        "Name": data['Docter Smith']
                    }
                ],
                "Subject": data['subject'],
                "TextPart": data['message'],
                "HTMLPart": f"<h3>{data['subject']}</h3><p>{data['message']}</p>"
            }
        ]
    }
    result = mailjet.send.create(data=email_data)
    return jsonify(result.json()), result.status_code
