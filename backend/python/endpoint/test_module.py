"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

An example module that uses the endpoint "/test"
"""
from app_provider import app_instance
from flask import abort
import endpoint.utility as util

__app = app_instance() # BackendApplication
__flask = __app.getFlask() # Flask


# Accessible by going to 127.0.0.1:5000/test
# Attach ?token=test at the end to see it work
@__flask.route("/test", methods=["GET"])
def test():
    # Retrieve token sent in request
    # Pass authenticator's verification method as verifier
    try:
        token = util.getParameter(
            "token", 
            verifier = __app.getAuthenticator().verifyToken
        )
    except Exception as e:
        # Invalid token was provided
        abort(401)
    

    return {
        "message": "This is an example JSON response"
    }
