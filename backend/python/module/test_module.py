"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

An example module that uses the endpoint "/test"
"""
from flask_provider import instance

# Flask Application
__app = instance()


# Accessible by going to webpage.com/test
@__app.route("/test", methods=["GET"])
def test():
    return {
        "message": "This is an example JSON response"
    }
